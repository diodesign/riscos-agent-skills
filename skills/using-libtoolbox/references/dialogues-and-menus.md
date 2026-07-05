# Dialogues, Menus, And Iconbar

Primary manual pages:

- `http://www.riscos.com/support/developers/toolbox/colourdbox.html`
- `http://www.riscos.com/support/developers/toolbox/colmenu.html`
- `http://www.riscos.com/support/developers/toolbox/dcs.html`
- `http://www.riscos.com/support/developers/toolbox/fileinfo.html`
- `http://www.riscos.com/support/developers/toolbox/fontdbox.html`
- `http://www.riscos.com/support/developers/toolbox/fontmenu.html`
- `http://www.riscos.com/support/developers/toolbox/iconbar.html`
- `http://www.riscos.com/support/developers/toolbox/menus.html`
- `http://www.riscos.com/support/developers/toolbox/print.html`
- `http://www.riscos.com/support/developers/toolbox/proginfo.html`
- `http://www.riscos.com/support/developers/toolbox/quit.html`
- `http://www.riscos.com/support/developers/toolbox/saveas.html`
- `http://www.riscos.com/support/developers/toolbox/scale.html`

## Common Pattern

Most standard dialogue classes follow the same pattern:

1. Create from a resource template.
2. Set dynamic state in `*_AboutToBeShown`.
3. Handle one or more semantic Toolbox events, not raw button clicks.
4. Use `*_DialogueCompleted` only for cleanup or close handling.

Important refinements:

- For most standard dialogues, the `*_AboutToBeShown` event block mirrors the pending `Toolbox_ShowObject` request. Use that event for last-minute state synchronisation on shared or persistent objects.
- If you replace a standard class's default underlying window template, preserve the documented gadget layout, component ids, title-bar behaviour, and button semantics. These classes are not free-form skins.
- `DialogueCompleted` does not always mean “nothing happened”. Some classes allow `Adjust` on the main action, after which completion may occur later even though a successful apply/save/scale already happened.
- Menu-style state refresh must happen in the event handler before the next `Wimp_Poll`.

## Practical Per-Class Summary

- `ColourDbox`: use for full colour picking. Set the current colour before showing; use `ColourSelected` for live preview and `DialogueCompleted` for final commit/cancel logic.
- `ColourDbox`: the colour block carries RGB data plus an extension area; current clients should leave the extra-size field as `0`. `GetWimpHandle` and `GetDialogueHandle` are only valid while the dialogue is showing. If `None` is selected, the event still returns the current colour block and reports the `None` state separately.
- `ColourMenu`: use for quick colour changes from a menu. Refresh the current selection in `AboutToBeShown`; handle `Selection` as the actual action.
- `ColourMenu`: selection state updates automatically after a pick; the main reason to intervene is to retick it to match external state just before showing.
- `DCS`: use in modified-document close flows. React to `DCS_Save`, `DCS_Discard`, and `DCS_Cancel` directly.
- `DCS`: `DCS_Save` means “save now or show SaveAs yourself”. If shown transiently, clicking away may produce only `DialogueCompleted`.
- `FileInfo`: mostly a read-only metadata dialogue. Populate file name, type, size, date, and modified state immediately before display.
- `FileInfo`: filetype sprites follow `file_xxx`; `0x1000` means directory and `0x2000` means application. The date is a 5-byte UTC time shown in `*time` format.
- `FontDbox`: use for full font and size selection. Set the current font, size, and try string before showing; use `ApplyFont` for live updates.
- `FontDbox`: displayed names may be localised, but the API always uses actual font identifiers such as `Corpus.Bold.Oblique`. `SystemFont` is a special sentinel. `DialogueCompleted` may follow a prior successful `ApplyFont`.
- `FontMenu`: menu-based font selection. Treat it like `ColourMenu`, with synchronisation before display.
- `FontMenu`: same font-id rule as `FontDbox`; do not confuse displayed font names with the API strings you must pass.
- `Iconbar`: use for application entry points. The main runtime customisation points are menu/show/event bindings and sprite/text changes.
- `Iconbar`: positions `-3` and `-4` cannot be combined with auto-show. In those cases, call `Toolbox_ShowObject` explicitly and supply the neighbour icon handle. Select and Adjust can each independently raise an event and/or show an attached object, and the `SelectAboutToBeShown` or `AdjustAboutToBeShown` events let you swap the target object at the last moment.
- `Iconbar`: a small application can create only the iconbar object explicitly and leave its attached menu/submenu objects to auto-create on demand. That keeps startup small and lets `Toolbox_ObjectAutoCreated` perform one-time state fixes such as fading unavailable menu entries.
- `Iconbar`: Toolbox does not replace every iconbar protocol. Drag-and-drop onto an iconbar icon can still be handled as raw Wimp `DataSave` and `DataLoad` messages even when the icon itself is a Toolbox object.
- `Iconbar`: set interactive help with `iconbar_set_help_message` for the icon itself. If the application needs different help on raw iconbar-adjacent Wimp targets, that belongs in the Wimp help protocol, not the Iconbar object.
- `Menu`: keep shared where possible. Refresh ticked, faded, or dynamic entries in `Menu_AboutToBeShown`; treat `Menu_Selection` as command dispatch.
- `Menu`: per-window versus shared menus is a real tradeoff between simpler state handling and lower memory use. Mutually recursive submenu trees are invalid and not checked by the module. Click-show objects are shown only after the menu event is delivered. Writable menu entries are not supported; use a dialogue instead.
- `Menu`: for a small fixed menu, resource-defined custom Toolbox event codes can be simpler than catching `Menu_Selection` and decoding component ids in C. Reserve direct component-id manipulation for jobs such as `menu_set_fade` and `menu_set_tick`.
- `Menu`: menu-level and per-entry help are first-class APIs. Use `menu_set_help_message` for the menu as a whole and `menu_set_entry_help_message` for actionable entries; entry help is the right place to explain what a command does or what dialogue it will open.
- `PrintDbox`: populate print parameters before showing and handle semantic events such as `Print`, `Save`, and `SetUp`.
- `PrintDbox`: page range uses `-1` for “All”. The title reflects the selected printer and updates automatically for persistent dialogues. `Set Up...` can either show an attached object or raise `PrintDbox_SetUp`. The Save button stores print settings; it is not the print action.
- `ProgInfo`: usually static and shared. Use when the app needs a standard About box.
- `ProgInfo`: mostly static, but version and licence type are intended runtime fields. Licence type is a fixed set, not arbitrary free text.
- `ProgInfo`: treat it as a standard class, not a generic window skin. Prefer `proginfo_set_version`, `proginfo_set_title`, `proginfo_set_uri`, and related veneers instead of reaching through its underlying window unless the task genuinely needs lower-level control.
- `Quit`: use for application-level quit confirmation. `Quit_Quit` is the actual proceed signal.
- `Quit`: both Return and Escape act as Cancel.
- `SaveAs`: this one carries a protocol, not just a window. Use the SaveAs events and veneer methods instead of raw `DataSave`/`RAMFetch` message handling unless the code intentionally bypasses Toolbox.
- `SaveAs`: there are three client modes:
  1. Supply a contiguous memory block with `SaveAs_SetDataAddress` and let Toolbox handle the save.
  2. Save to file on `SaveAs_SaveToFile`.
  3. Save to file and also support RAM transfer with `SaveAs_FillBuffer` and `SaveAs_BufferFilled`.
- `SaveAs`: `SaveAs_FileSaveCompleted` must be called before the next `Wimp_Poll`. `SaveAs_SelectionAvailable` errors if the dialogue has no Selection option. `SaveAs_SaveCompleted` reports whether the destination was safe and can carry the original `Message_DataSave` reference. A leafname alone is not a valid destination for the Save button; that path is intended for drag save.
- `SaveAs`: when one shared `SaveAs` object is launched from multiple menu entries, use `SaveAs_AboutToBeShown` to retarget the dialogue and use the id block context during both `AboutToBeShown` and `SaveToFile`. In particular, `id_block->self_id` is the `SaveAs` object, while `id_block->parent_component` identifies the menu entry or gadget that opened it.
- `Scale`: set current bounds and scale before display; `ApplyFactor` is the real business event.
- `Scale`: the standard factor buttons only change the number-range value; they do not apply the scale. `Scale To Fit` reports `0xffffffff` in `Scale_ApplyFactor`.

## Reading Existing Code

- If code calls `*_get_window_id`, it is about to manipulate the underlying `Window` object directly.
- If a class is auto-created and shared, expect state refresh in `AboutToBeShown` rather than immediate post-create setup.
- If a menu or dialogue opens another object, look for click-show or submenu-show configuration before assuming the application calls `Toolbox_ShowObject` manually.
- If a menu is populated dynamically and then opens a shared dialogue, expect a two-stage flow: `Menu_AboutToBeShown` mutates the menu, then the launched object's `AboutToBeShown` handler uses parent context to specialise the dialogue.
- If a class uses an alternative underlying window template, verify that the expected standard components are still present before changing it.
