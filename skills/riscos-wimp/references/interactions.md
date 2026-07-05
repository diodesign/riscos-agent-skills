# Interactions

Use this file for mouse clicks and key handling.

## Mouse clicks

Split the logic by:

* source window
* source icon
* button semantics: Select, Adjust, Menu

When debugging click issues, log all three before assuming the action mapping is wrong.

For `Wimp_Poll` button-change events, remember that the returned click values
depend on the icon or work-area button type.

For ordinary `wimp_BCLICKDEBOUNCE` icon paths, the common returned values are:

* `1` = Adjust
* `2` = Menu
* `4` = Select

Do not generalise those three values to every icon type. The local PRM is
explicit that button type changes how Select and Adjust are handled, while Menu
is always reported for window work areas. If the icon or work area uses a
different button type, confirm the expected click semantics from the PRM's
button-type rules before hard-coding `1`/`2`/`4`.

Do not confuse these button-change event values with the separate button-state
bitfields such as `wimp_BCLICKLEFT` or `wimp_BCLICKRIGHT` unless you have
confirmed the current block layout and semantics for the exact path you are
decoding.

When a click handler seems wrong, check in this order:

* that the source window and icon are the ones you expected
* that the icon was created with the button type you think it has
* that the returned mouse value is being decoded using rules for that button
  type, not for some other icon style

When handling iconbar clicks specifically, also filter by both:

* source window handle `-2` for the icon bar
* the specific icon handle returned by `Wimp_CreateIcon`

Checking only the icon handle is brittle once the application owns multiple
windows or expands its event handling.

Do not dereference event-specific blocks before casting the poll block to the correct event structure.

## Key presses

For writable fields or dialogue windows:

* inspect the caret window and icon
* handle Return or Escape explicitly when needed
* otherwise pass keys on with the normal Wimp processing path

For standard writable icons specifically:

* assume WindowManager owns the low-level cut-and-paste editing behaviour
* keep the caret state authoritative for which icon may hold a text selection
* avoid duplicating selection motion, double-click word selection, or clipboard keystroke handling unless you have deliberately replaced the standard writable-icon model

For embedded browser plug-ins:

* do not assume unhandled keys should always go through `Wimp_ProcessKey`
* if the plug-in protocol expects the browser to receive unhandled input, forward that input to the browser using the documented message path and the parent window handle
* keep "input handled locally" and "focus returned to host" as separate decisions

## Drag boxes

For UI paths that use `Wimp_DragBox`:

* derive the drag bounds from the current window state and icon geometry rather than cached guesses
* keep the drag workspace small and explicit
* finish the interaction on the matching drag-complete poll event
* redraw only the changed region after resizing or moving a dragged visual element

If the drag updates icons within a window, re-check whether the changed region should be refreshed with `Wimp_ForceRedraw`, icon-state changes, or both.

If the task also uses menus, help, or file-transfer messages, read the dedicated reference for that area rather than overloading this one.
