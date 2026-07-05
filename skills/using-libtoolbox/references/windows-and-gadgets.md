# Windows And Gadgets

Primary sources:

- Header: `/riscos-resources/Export/Lib/tboxlibs/h/window`
- Header: `/riscos-resources/Export/Lib/tboxlibs/h/gadgets`
- Manual: `http://www.riscos.com/support/developers/toolbox/windows.html`
- DrawFile notes: `http://www.riscos.com/support/developers/toolbox/render.html`

## Window Model

A Toolbox `Window` is a Wimp window plus Toolbox-managed behaviour such as:

- attached menu handling
- help replies
- custom pointer shapes
- keyboard shortcut dispatch
- gadget hosting
- toolbar attachment

Treat raw Wimp access as a bridge, not the default model. Changing gadget-owned icons directly is risky because the Window module owns much of the low-level behaviour.

Important window methods to recognise:

- `Window_GetWimpHandle`
- `Window_AddGadget` and `Window_RemoveGadget`
- `Window_SetMenu` and `Window_GetMenu`
- `Window_SetPointer` and `Window_GetPointer`
- `Window_SetHelpMessage` and `Window_GetHelpMessage`
- `Window_AddKeyboardShortcuts` and `Window_RemoveKeyboardShortcuts`
- `Window_SetTitle` and `Window_GetTitle`
- `Window_SetDefaultFocus` and `Window_GetDefaultFocus`
- `Window_SetExtent` and `Window_GetExtent`
- `Window_ForceRedraw`
- `Window_SetToolBars` and `Window_GetToolBars`

Use `Window_GetPointerInfo`, `Window_WimpToToolbox`, and `Window_ExtractGadgetInfo` when code must bridge raw Wimp state back into Toolbox object/component identities.

Important behavioural constraints:

- `Window_SetDefaultFocus` affects the next show, not the currently visible window.
- Default focus `-1` means no focus gadget; `-2` means focus the window itself so keyboard shortcuts still work without a caret.
- `Window_AboutToBeShown` is the normal last-minute population hook and receives the original show arguments.
- `Window_HasBeenHidden` can be raised by more than an explicit `Toolbox_HideObject`, including non-local action-button closure and dismissal of CreateMenu-style windows.
- `Window_SetMenu` must not be used while that window's menu is currently being shown.
- `Window_SetHelpMessage` covers the work area and any pointer position that does not resolve to a gadget-specific help string.

## Toolbars

- Toolbars are specialised windows.
- They attach to a parent window in one of four slots.
- They are not independent top-level objects in normal use.
- Existing code often treats them as auxiliary UI strips such as tool palettes or status panes.
- Toolbars cannot sensibly own toolbars themselves.
- Only default show semantics are defined for toolbars.
- A toolbar can only be shown while its parent is showing.
- Replacing toolbars on a shown window can immediately hide old toolbars and show the new ones.
- Existing code sometimes treats a toolbar template as a normal `Window` object shown with `Toolbox_ShowObject_AsSubWindow` and a `WindowShowObjectBlock`. That is a valid pattern for a control strip that tracks the parent window's position and clipping.

## Generic Gadget Model

Every gadget is identified by:

- the parent `Window` object id
- the gadget `ComponentId`

Start with the generic gadget methods when you need to inspect or manipulate an unknown gadget:

- `Gadget_GetFlags` and `Gadget_SetFlags`
- `Gadget_SetHelpMessage` and `Gadget_GetHelpMessage`
- `Gadget_GetIconList`
- `Gadget_SetFocus`
- `Gadget_GetType`
- `Gadget_MoveGadget`
- `Gadget_GetBBox`

Additional constraints:

- `Gadget_GetIconList` is implementation-specific; do not cache icon handles long-term.
- `Gadget_SetFlags` is really only safe for fading. Arbitrary flag mutation is undefined.
- Prefer family-level gadget APIs before reaching into child components of composite gadgets.

## Built-In Gadget Families

- `ActionButton`: command buttons, often default or cancel actions, with optional click-show behaviour.
- `OptionButton`: independent on/off state.
- `RadioButton`: exclusive choice within a group.
- `DisplayField`: read-only text.
- `WritableField`: editable text and allowable-character control.
- `Slider`: numeric value with bounds and colour settings.
- `Draggable`: sprite or text drag source.
- `PopUp`: menu-bound control.
- `AdjusterArrow`: increment/decrement arrow, often inside composites.
- `NumberRange`: composite numeric control built from simpler parts.
- `StringSet`: composite choice/text control built from simpler parts.
- `Button`: low-level Wimp-like gadget with fewer Toolbox semantics.

## Important Behavioural Points

- The Window module converts many low-level Wimp interactions into Toolbox events.
- `OpenWindowRequest` and `CloseWindowRequest` may be intercepted entirely when auto-open or auto-close behaviour is enabled.
- Help replies are automatic for windows and gadgets; gadget help takes precedence over window help.
- A good default is broad window help plus short, action-specific gadget help on controls that the user can operate directly.
- Window furniture is not exposed as Toolbox gadgets. If custom help is required for close/back/iconise/scroll icons or other raw icon handles, handle that through the raw Wimp help protocol instead of `gadget_set_help_message`.
- If code has to identify the hovered Toolbox object from a raw pointer position, use `window_get_pointer_info` or `window_wimp_to_toolbox` rather than caching icon handles from `gadget_get_icon_list`.
- Pointer-enter and pointer-leave handling can automatically switch the pointer shape.
- Keyboard shortcuts are Wimp key-code based. Some combinations such as `Shift-Ctrl-letter` need client-side handling.
- Many gadget families use a default Toolbox event when the template event field is zero, or a caller-supplied event code when configured.
- `Button` is the main exception: clicks remain Wimp events with the Toolbox id block updated.
- Composite gadgets such as `NumberRange` and `StringSet` may expose child component ids through `GetComponents`; use that only when the family-level API is not enough.
- Action buttons normally close the parent window on Select unless marked local; Adjust raises the event but keeps the window open. Return triggers the default action button and Escape triggers the cancel button when the window has focus.
- Pop-up menus raise `PopUp_AboutToBeShown` before the menu appears; the actual show happens on the next `Wimp_Poll`. Menu selections are reported on the `Menu` object, not the popup gadget itself.
- Radio buttons cannot be forced off if that would leave no selection in the group.
- Writable field and string set change events can report truncated visible text; follow up with `GetValue` or `GetSelected` if exact content matters.
- String set available values are comma-separated with escaping, there is no `StringSet_GetAvailable`, and non-listed typed text can leave the gadget with no ticked menu entry.
- Slider event timing can be configured, and the event flags distinguish drag start, movement, and end.
- It is normal to bridge down to raw Wimp only for geometry-sensitive jobs: obtaining the Wimp handle with `Window_GetWimpHandle`, reading visible area and scroll from `Wimp_GetWindowState`, then returning to Toolbox calls such as `Window_SetExtent` or `Gadget_MoveGadget`.
- For keyboard-driven applications, clearing the caret from a gadget or the window itself can be enough to hand focus back to the window-level shortcut machinery while keeping the UI Toolbox-managed.

## DrawFile In Redraw Code

When Toolbox window redraw code handles Draw content, the important veneers are in `drawfile`:

- `drawfile_render`
- `drawfile_bbox`
- `drawfile_declare_fonts`

Expect redraw code to combine the current Wimp redraw rectangle with a translation or scaling matrix before calling `DrawFile_Render`.

Additional DrawFile constraints:

- `Window_ForceRedraw` uses work-area coordinates, not screen coordinates.
- The intended clipping rectangle for `DrawFile_Render` is the Wimp redraw rectangle.
- `DrawFile_Render` assumes screen origin unless a transform is supplied; translation belongs in that transform.
- `DrawFile_BBox` is useful for computing extents before show or redraw work.
- `DrawFile_DeclareFonts` is required in printing paths between `PDriver_SelectJob` and `PDriver_DrawPage`.
- Missing fonts fall back to the system font, transformed missing-font text loses the transform, text-area wrapping can differ from `!Draw`, and sprites without palettes use Wimp palette colours.

## Single-Document Window Pattern

A practical mixed approach for a document-style application is:

- use a Toolbox `Window` as the main document surface
- show a second window as a Toolbox subwindow to behave like a toolbar
- resize gadgets with `gadget_get_bbox` and `gadget_move_gadget` rather than poking Wimp icons directly
- preserve scroll and visible geometry by reading Wimp window state before recalculating extents
- use raw Wimp open/close handlers only where Toolbox auto-open/auto-close is not the desired behaviour
