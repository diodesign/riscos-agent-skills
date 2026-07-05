# Colour Picker dialogues

Use this file when a Wimp task launches or tracks a ColourPicker dialogue, including menu and submenu forms.

## Core model

* The ColourPicker module is not a separate Wimp task. It installs Wimp filters around the client task when a picker is opened.
* Clients must be Wimp tasks.
* The client talks to the picker through `ColourPicker_OpenDialogue`, `ColourPicker_CloseDialogue`, `ColourPicker_UpdateDialogue`, `ColourPicker_ReadDialogue`, and optionally `ColourPicker_HelpReply`, and receives feedback through Wimp user messages.
* Every open picker has:
  * a dialogue handle used in `ColourPicker_*` SWIs and ColourPicker messages
  * a window handle returned by `ColourPicker_OpenDialogue`
* Wimp events for the picker's window are still delivered to the client after the picker has already processed them. Normally ignore them unless your task has generic per-window handling that would interfere.

## Dialogue types

Pass the type in bits 0-1 of `R0` to `ColourPicker_OpenDialogue`:

* `0`: normal dialogue
* `1`: menu dialogue
* `2`: toolbox dialogue
* `3`: submenu dialogue

The types differ in protocol:

* Normal dialogue:
  * has `OK` and `Cancel`
  * sends `Message_ColourPickerColourChoice` when `OK` is used
  * usually later sends `Message_ColourPickerCloseDialogueRequest`
* Toolbox dialogue:
  * has Back and Close icons instead of `OK` and `Cancel`
  * does not send `Message_ColourPickerColourChoice`
  * read the current colour with `ColourPicker_ReadDialogue` or track it with `Message_ColourPickerColourChanged`
  * may send `Message_ColourPickerOpenParentRequest`
* Menu dialogue:
  * transient
  * the module opens it with `Wimp_CreateMenu`
  * the Wimp closes it automatically when the menu tree is dismissed
* Submenu dialogue:
  * transient
  * the module opens it with `Wimp_CreateSubMenu`
  * use it from the `MenuWarning` path when a menu entry expands into a colour picker

Transient pickers are closed by the Wimp rather than by the usual close-request message.

## Opening a picker

`ColourPicker_OpenDialogue` takes:

* `R0 =` dialogue type in bits 0-1
* `R1 ->` colour picker block

It returns:

* `R0 =` dialogue handle
* `R1 =` window handle

The colour picker block is the protocol surface you reuse for open, update, and read operations:

* `+0`: flags
  * bit 0: show `None` button
  * bit 1: `None` initially selected
  * bits 2-3: when `Message_ColourPickerColourChanged` is sent
  * bit 4: ignore `Message_HelpRequest`
  * bit 5: do not pass unhandled keys to the Wimp on RISC OS 3.6+
* `+4`: title pointer, or `0` for the default title
* `+8`: visible area's top-left X coordinate
* `+12`: must be `&80000000`
* `+16`: must be `&7FFFFFFF`
* `+20`: visible area's top-left Y coordinate
* `+24`: reserved, must be `0`
* `+28`: reserved, must be `0`
* `+32...`: colour descriptor

For changed-message timing in bits 2-3:

* `0`: never send changed messages
* `1`: send on changes, but only once at drag end during drags
* `2`: send on every change, including during drags

The colour descriptor begins with a 24-bit RGB value and may carry extra model-specific data. Preserve the whole descriptor if you want to reopen the picker with the same model and state later.

## Message protocol

Register and handle these message actions:

* `&47700` `Message_ColourPickerColourChoice`
  * `R1+20`: dialogue handle
  * `R1+24`: flags, bit 0 means `None` chosen
  * `R1+28...`: chosen colour descriptor
  * Sent when the user makes a definite choice, normally by `OK`
* `&47701` `Message_ColourPickerColourChanged`
  * `R1+20`: dialogue handle
  * `R1+24`: flags, bit 0 means `None`, bit 1 means drag in progress
  * `R1+28...`: current colour descriptor
  * Optional; controlled by the button-type bits in the colour picker block
* `&47702` `Message_ColourPickerCloseDialogueRequest`
  * `R1+20`: dialogue handle
  * For non-transient pickers, call `ColourPicker_CloseDialogue`
  * Not sent for menu or submenu pickers
* `&47703` `Message_ColourPickerOpenParentRequest`
  * `R1+20`: dialogue handle
  * Toolbox-only; reopen or front the parent dialogue
  * An Adjust close is followed by `Message_ColourPickerCloseDialogueRequest`
* `&47704` `Message_ColourPickerResetColourRequest`
  * `R1+20`: dialogue handle
  * Sent when the user Adjust-clicks `Cancel`
  * Reply by calling `ColourPicker_UpdateDialogue` to restore the colour currently in effect
  * Not issued under RISC OS 3.5

Do not assume `Message_ColourPickerColourChoice` closes the dialogue. A choice may or may not be followed by a close request.

## Reading and updating

Use `ColourPicker_ReadDialogue` to read live state:

* first call with `R2 = 0` to get the required buffer size back in `R2`
* allocate that many bytes
* call again with `R2 -> buffer`

This matters because the colour descriptor size varies with the active colour model.

Use `ColourPicker_UpdateDialogue` to change a live picker. Common cases:

* bits 0-1: add/remove the `None` button and select it
* bit 2: change changed-message behaviour
* bit 5: change the title
* bit 6: update the current colour from the descriptor's RGB triplet only
* bit 7: update the colour model and model-dependent data; this overrides bit 6
* bit 8: change whether the picker handles `Message_HelpRequest`
* bit 9: change unhandled-key forwarding on RISC OS 3.6+

If you set bit 3 to move the visible area, fill offsets `+8` to `+20` exactly, including the reserved words.

## Menu and submenu integration

For a colour picker used as part of menu interaction:

* use a menu dialogue for a standalone popup picker
* use a submenu dialogue when the picker is attached to an open menu tree
* open submenu pickers from the `MenuWarning` path, while the Wimp is asking for submenu creation
* supply the popup coordinates in the colour picker block; the ColourPicker module performs the `Wimp_CreateMenu` or `Wimp_CreateSubMenu` call itself

Do not add a separate `Wimp_CreateSubMenu` call around a type-3 picker. The ColourPicker module already owns that part of the protocol.

Because transient pickers are Wimp-closed:

* do not wait for `Message_ColourPickerCloseDialogueRequest`
* if you keep client-side bookkeeping, clear it when the picker choice arrives or when your surrounding menu state is torn down

## Event-loop discipline

When you have generic key, help, or menu handling:

* compare the returned window handle against the event block before treating the event as one of your own
* avoid sending your own help text for the picker's window unless you deliberately opened it in "ignore help requests" mode
* if you suppress unhandled keys for the picker's window, do so because the picker has already consumed them, not because the picker is a normal application window

## BASIC wrapper pattern

`Library/BASIC/ColPick/ColPick,ffb` is a practical client wrapper:

* `PROCinitcolpick` initialises message constants and workspace
* `PROCcolpick_addmessages` adds all ColourPicker messages, plus `Message_MenusDeleted`
* `FNcolpick_msg(mess)` handles the ColourPicker message protocol and dispatches client callbacks
* `FNcolpick_create(...)` wraps `ColourPicker_OpenDialogue`
* `PROCcolpick_kill(handle%)` wraps `ColourPicker_CloseDialogue`
* `FNcolpick_read(handle%)` wraps the two-call `ColourPicker_ReadDialogue` pattern
* `PROCcolpick_updatecolour(handle%, colour%)` resets the live dialogue with `ColourPicker_UpdateDialogue`

The wrapper also captures two application-level rules worth preserving in other clients:

* menu and submenu pickers are transient, so the wrapper only supports a choice callback there
* toolbox parent handling is a separate callback, and a normal dialogue with a parent concept is promoted to a toolbox-style picker
