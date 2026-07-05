# Clipboard Protocol

Use this file when implementing or reviewing Wimp cut, copy, paste, selection ownership, or clipboard-manager behaviour.

This reference folds in the older Acorn selection-and-clipboard note and the later clipboard-manager extension so that the protocol can be implemented without depending on the original private URLs.

Public references:

* Clipboard Holder overview and SWIs: `https://www.riscos.com/support/developers/riscos6/desktop/clipboardholder.html`
* WindowManager cut-and-paste notes: `https://www.riscos.com/support/developers/riscos6/desktop/wimp/wimpcnp.html`

Treat those public RISC OS documents as the canonical references for this topic. Implementation sources from elsewhere may still be useful background, but they are not authoritative if they disagree with the public interface description.

## Scope

The Wimp clipboard is not a shared memory buffer. It is a message-level protocol built on:

* per-window caret and selection state inside each task
* `Message_ClaimEntity` for ownership changes
* `Message_DataRequest` with the clipboard flag set
* the normal `DataSave` / `DataSaveAck` / `DataLoad` file-transfer path
* the later `Message_ReleaseEntity` handover when a clipboard owner is about to quit

Read `references/data-transfer.md` as well for the normal `DataSave` and `DataLoad` rules.

## Prefer `ClipboardHolder` when raw Wimp messaging is not needed

Applications do not have to implement the full clipboard negotiation themselves.

If the task only needs a straightforward "copy this payload" or "paste the current clipboard data" interface, prefer the `ClipboardHolder` SWIs:

* `ClipboardHolder_Copy` (`SWI &54040`)
* `ClipboardHolder_Paste` (`SWI &54041`)

These calls let a task use the clipboard without manually broadcasting `Message_ClaimEntity` or constructing `Message_DataRequest` and `DataSave` messages.

Use the raw Wimp protocol directly when:

* the task itself is the clipboard manager
* you are implementing desktop-wide clipboard interoperability rules
* you need full control over handover, filetype negotiation, or the exact message flow
* you are debugging another task's clipboard protocol behaviour

## `ClipboardHolder_Copy`

`ClipboardHolder_Copy` stores clipboard data in one of two source forms:

* memory copy
* file copy

Inputs:

* `R0` flags: bits `0` to `2` select the copy type
* `0` = memory copy
* `1` = file copy
* other bits reserved and should be `0`
* `R1`: filetype of the data
* `R2`: pointer to the memory block, or pointer to the filename
* `R3`: length of the memory block for memory copies

Results:

* all registers preserved

Usage rules:

* always provide a real RISC OS filetype
* use the memory form for data you already hold in a buffer
* use the file form when the clipboard payload already exists as a file
* `Cut` is still an application operation: call `ClipboardHolder_Copy`, then delete the source selection yourself

## `ClipboardHolder_Paste`

`ClipboardHolder_Paste` retrieves clipboard data or reports whether suitable data is available.

Inputs:

* `R0` flags: bits `0` to `2` select the paste destination type
* `0` = paste to memory
* `1` = paste to file
* bit `3` requests a status-only probe
* other bits reserved and should be `0`
* `R1`: preferred filetype, or `-1` for the native clipboard type
* `R2`: destination window handle, or `0` if a new window is appropriate
* `R3`: private handle identifying the request

Results:

* `R0` state flags:
* bit `0`: clipboard can be delivered in memory
* bit `1`: clipboard can be delivered as a file
* bit `8`: clipboard must be delivered through the Wimp clipboard protocol
* `R1`: returned filetype
* `R2`: pointer to memory data or pointer to filename
* `R3`: memory length for memory delivery, preserved for file delivery

Important compatibility note:

* the public `ClipboardHolder` page says the protocol-delivery flag is bit `2`
* one non-canonical implementation source and its local SWI notes use bit `8`
* keep that discrepancy visible when reviewing code that talks to existing implementations
* if you are documenting the interface, present the public documentation as the canonical definition

Practical interpretation:

* no bits set means no clipboard data is available
* bit `0` means the caller can use `R2` and `R3` as an in-memory buffer
* bit `1` means the caller can use `R2` as a filename
* bit `8` means the clipboard data currently lives in another task and will arrive through the normal Wimp message path

## Using `ClipboardHolder_Paste` safely

Typical patterns:

* probe first by setting the status-only bit
* request a preferred interchange filetype where possible
* fall back to `-1` when native-format paste is acceptable
* if the result says memory delivery is available, consume the returned block immediately and treat it as owned by the clipboard holder
* if the result says file delivery is available, copy or load the returned file rather than assuming it is permanent
* if the result says protocol delivery is required, be ready to receive the ordinary clipboard `DataSave` and `DataLoad` sequence

The `window` and private handle arguments matter when protocol delivery is required, because the later `DataRequest` / `DataSave` exchange uses them to direct the paste to the right destination.

## Writable icons and WindowManager cut-and-paste

Writable icons have a separate high-level path documented by the public WindowManager cut-and-paste note.

For ordinary writable icons:

* selection exists only in the icon that currently has the caret
* moving the caret to another icon or window ends that writable-icon selection
* `Select` positions the caret or starts a selection in the usual text-editing way
* `Adjust` can create or extend a selection from the caret to the clicked position
* double-click selection expands to a word boundary

The important implementation point is that these selection operations are handled by WindowManager for writable icons. Applications using standard writable icons do not need to reimplement low-level text-selection mechanics merely to get normal cut-and-paste behaviour.

When relying on the WindowManager path:

* keep using standard writable icons rather than custom text widgets
* do not fight the caret and selection state that WindowManager is maintaining
* make sure the icon really owns the caret before assuming icon-level cut or paste applies
* if you replace the standard writable-icon editing model with custom code, you must provide equivalent user-visible behaviour yourself

This writable-icon support is complementary to the task-level clipboard protocol:

* WindowManager handles editing and selection behaviour inside the icon
* clipboard transfer beyond the icon still uses the normal clipboard interfaces
* applications that only need standard writable-icon editing can often use `ClipboardHolder` rather than manual Wimp clipboard messaging

## Writable-icon review checks

When reviewing writable-icon text editing:

* selection should be tied to the caret-owning icon, not shared across unrelated icons
* `Adjust` should extend or create the selection rather than acting as an unrelated shortcut
* word selection on double-click should follow the standard text model
* custom writable-icon handlers should not bypass standard clipboard behaviour without a strong reason
* code should not assume every clipboard operation for writable icons requires manual `Message_DataRequest` handling

## Selection model

Keep these UI rules straight:

* Each window keeps its own caret or selection state, even when multiple windows view the same document.
* Within one window, caret and selection are normally mutually exclusive.
* When the user creates a selection, hide the caret.
* When the user positions the caret, clear any existing selection in that window.
* Keyboard input and paste should replace the active selection, otherwise insert at the caret.
* After a paste, select the newly inserted data so the user can immediately cut it again if needed.
* If ordinary typing replaces a selection, cut the replaced data to the clipboard as a safety measure.
* Do not perform that safety cut when the replacement itself came from a paste, otherwise repeated paste becomes impossible.

For graphical editors that do not draw a text-style caret, still claim the input focus and choose a deterministic insertion location for paste.

## Owning caret, selection, and clipboard

Tasks track two separate ideas:

* whether one of their windows currently owns the input focus
* whether they currently own the clipboard contents

Ownership changes are announced with `Message_ClaimEntity` (`15`):

* size: `24`
* `your_ref`: `0`
* action: `Message_ClaimEntity`
* bits `0` and `1` together mean the task is claiming the caret or selection focus
* bit `2` means the task is claiming the clipboard
* all other bits are reserved and should be `0`

Rules:

* Broadcast the message when claiming focus or clipboard, unless the task already owns that entity.
* Treat a received focus claim with only one of bits `0` or `1` set as if both were set.
* When another task claims focus, clear the local "has focus" state and hide any task-drawn caret.
* When another task claims clipboard ownership, forget any cached clipboard payload owned on that basis.

Ignore `GainCaret` and `LoseCaret` for clipboard ownership logic. The Wimp may borrow the caret for writable menu icons, and older tasks may still manipulate the caret without participating in the clipboard protocol.

## Focus without destroying the selection

To let the user return to a window without losing an existing selection:

* treat clicks inside the current selection, or in a dead area such as a border, as focus restoration rather than caret repositioning
* broadcast `Message_ClaimEntity` with the focus bits set
* set the Wimp caret to that window
* keep the caret invisible if a selection still exists
* otherwise restore the previous caret position

This preserves a fiddly selection while restoring keyboard focus.

## Cut and copy

For `Cut` and `Copy`:

* if there is no selection, the action is unavailable
* if the task already owns the clipboard, discard the old clipboard payload first
* otherwise claim the clipboard with `Message_ClaimEntity` bit `2`
* capture the selected data in the task's native representation
* `Cut` then deletes the selection
* `Copy` leaves the source selection intact

The task that most recently performed `Cut` or `Copy` is the effective clipboard owner until another task claims it.

## Paste request

If the destination task already owns the clipboard, it may use the data directly.

Otherwise it broadcasts `Message_DataRequest` (`16`) with the clipboard flag set:

* `window`: destination window handle
* `icon` or private handle: destination-specific identifier
* `x`, `y`: insertion location if relevant, otherwise `0`
* flags: bit `2` set for clipboard, other bits `0`
* filetype list: preferred filetypes in order, terminated by `-1`

Clipboard rules for this request:

* the sender must set the clipboard flag
* the receiver must ignore the request if the clipboard flag is not set
* a null or immediate `-1` filetype list means "send native format"
* the clipboard owner should choose the earliest requested type it can provide
* if none match, it should fall back to its native type

The reply is an ordinary `Message_DataSave`:

* copy bytes `20` to `35` from the original `DataRequest`
* fill in the estimated size, filetype, and leaf name
* continue through the normal `DataSave` / `DataSaveAck` / `DataLoad` path

The paste destination must still validate the returned filetype. A clipboard owner is allowed to return its native type when none of the preferred types were available.

## Probing whether Paste should be enabled

To decide whether `Paste` should be shaded:

* broadcast the same clipboard `Message_DataRequest`
* if the message returns unclaimed, no clipboard owner is available
* if a `Message_DataSave` arrives, inspect its filetype
* if the type is unsuitable, simply do not acknowledge it

Failing to continue the `DataSave` transaction silently aborts the probe at the sender side.

## Payload and filetype rules

Preserve both payload bytes and the intended filetype:

* do not assume clipboard traffic is always text
* request preferred interchange types first, then tolerate native fallback where useful
* if the owner returns a scrap-file path, honour the normal `DataSave` and `DataLoad` cleanup rules
* when storing clipboard data internally, keep enough metadata to regenerate a correct `DataSave` later

Many interoperability failures preserve the bytes but lose the original RISC OS filetype, which breaks later paste decisions.

## Clipboard-manager extension

The later extension adds a clipboard manager so the clipboard can survive when the owning application quits.

At protocol level, this is still built from ordinary Wimp messages:

* the clipboard owner announces ownership with `Message_ClaimEntity`
* a clipboard manager listens for those broadcasts
* when the owner is about to exit, it sends `Message_ReleaseEntity`
* the manager then acquires the clipboard payload through the normal `DataRequest` and `DataSave` path and re-claims the clipboard itself

If you are implementing either side, keep the following behaviour compatible.

## `Message_ReleaseEntity` handover

The quitting clipboard owner sends `Message_ReleaseEntity` to say "I currently own the clipboard and am releasing it".

The intended receiver is a clipboard manager task. On receipt, the manager should:

* verify that the message is about the clipboard entity
* remember which task currently holds the clipboard
* issue a `Message_DataRequest` back to that task with the clipboard flag set
* request native format by sending a filetype list beginning with `-1`
* preserve the release message's `my_ref` in the follow-up request's `your_ref` so the handover remains tied to the release

That handover request typically uses an internal handle to mark that this fetch is a forced takeover from a quitting owner.

## Manager behaviour on ordinary claims

A clipboard manager can also watch ordinary `Message_ClaimEntity` broadcasts to track who now owns the clipboard.

Useful manager behaviour:

* forget any previous cached payload when another task claims the clipboard
* record the claiming task as the live clipboard owner
* optionally probe for the native type using a clipboard `DataRequest`
* if the returned data is small enough and in a directly useful format such as text, cache a local copy

That cache lets the manager answer future paste requests even if the original owner later dies.

## Manager data transfer details

When a clipboard manager accepts handover, it should receive the payload through the standard transfer protocol, then become the owner itself by broadcasting `Message_ClaimEntity` for the clipboard.

Practical rules:

* use `<Wimp$Scrap>` for scrap-file transfers when available
* if scrap is unavailable, fall back to another deterministic temporary path
* small text payloads can be copied into memory
* larger payloads can be retained in a private file and re-served later
* once the manager has taken ownership, it should answer clipboard `DataRequest` messages like any other clipboard owner

## Interoperability assumptions from the later manager implementation

The later `ClipboardHolder` implementation shows a few behaviours that are worth matching because other software may depend on them:

* clipboard requests use `Message_DataRequest` with the clipboard flag, not a private message type
* native-format request is represented by a filetype list beginning with `-1`
* small text data is often materialised in memory, while larger data is kept in a scrap or temporary file
* when the original owner disappears before transfer completes, the manager treats the clipboard as lost
* the manager ignores clipboard `ClaimEntity` broadcasts that it sent itself

Do not invent a second clipboard transfer path when the standard `DataRequest` and `DataSave` flow already does the job.

## Review checklist

When reviewing clipboard code, check these first:

* focus claims and clipboard claims are not being confused
* `Message_ClaimEntity` broadcasts are suppressed when ownership has not changed
* clipboard `DataRequest` sets the clipboard flag and terminates the filetype list with `-1`
* `DataSave` replies copy the destination window, handle, coordinates, and flags from the request
* the paste path validates the returned filetype instead of assuming the preferred type was honoured
* typing over a selection performs the safety cut, but pasting over a selection does not
* quit-time handover uses `Message_ReleaseEntity` plus normal transfer, not ad hoc private storage
* file-backed clipboard data keeps the correct RISC OS filetype
