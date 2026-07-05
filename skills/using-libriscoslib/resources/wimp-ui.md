# Wimp and UI helpers

This note covers the `RISC_OSLib` headers that sit directly on top of the
Wimp and common desktop protocols.

## `wimp.h`

`wimp.h` is the low-level public interface. Most functions are thin wrappers
around the correspondingly named Wimp SWIs.

### Core handles and structures

* `wimp_w`, `wimp_i`, `wimp_t`: opaque window, icon, and task handles.
* `wimp_box`: `x0`, `y0`, `x1`, `y1` in OS units.
* `wimp_icondata`:
  * `text[12]` / `sprite_name[12]`: in-place short data.
  * `indirecttext.buffer`: pointer to the writable text buffer.
  * `indirecttext.validstring`: pointer to the validation string.
  * `indirecttext.bufflen`: buffer length.
  * `indirectsprite.name`: sprite name or sprite pointer.
  * `indirectsprite.spritearea`: `0` for the common sprite area, `1` for the
    Wimp sprite area, otherwise a real sprite-area pointer.
  * `indirectsprite.nameisname`: non-zero means `name` is a sprite name.
* `wimp_icon`:
  * `box`: icon box relative to the window work-area origin.
  * `flags`: packed icon flags.
  * `data`: one of the `wimp_icondata` forms above.
* `wimp_wind`:
  * `box`: visible work-area box on screen.
  * `scx`, `scy`: scroll positions.
  * `behind`: window to open behind, or `-1` for top.
  * `flags`: `wimp_wflags`. `wimp_WNEW` must be set for the modern flag word.
  * `colours[8]`: indexed by `wimp_wcolours`.
  * `ex`: work-area extent.
  * `titleflags`: icon flags for the title.
  * `workflags`: mainly the work-area button type.
  * `spritearea`: sprite area for indirected sprite icons.
  * `minsize`: packed 16-bit minimum width/height.
  * `title`: title icon data.
  * `nicons`: icon count. Icon definitions, if any, follow the structure in
    memory immediately.
* `wimp_openstr`:
  * `w`: target window.
  * `box`: visible work area on screen.
  * `x`, `y`: work-area origin corresponding to the visible box.
  * `behind`: `-1` top, `-2` bottom, otherwise another window handle.
* `wimp_wstate`: `o` is the open-state block; `flags` are the current state.

### Important flag families

* `wimp_wflags`: window behaviour and furniture. The important practical point
  is that `wimp_WNEW` should be present when you populate a full window block.
* `wimp_iconflags`:
  * `wimp_ITEXT`, `wimp_ISPRITE`, `wimp_INDIRECT` choose the content form.
  * `wimp_IBTYPE`, `wimp_IFORECOL`, `wimp_IBACKCOL` are packed bitfields.
  * `wimp_ISELECTED`, `wimp_INOSELECT`, `wimp_IFILLED` drive typical state.
* `wimp_ibtype`: button semantics such as `wimp_BCLICKDEBOUNCE`,
  `wimp_BWRITABLE`, `wimp_BRELEASEDRAG`.
* `wimp_etype` / `wimp_emask`: event numbers and their poll-mask bits.

### Common functions

Window and icon lifecycle:

* `wimp_create_wind`, `wimp_delete_wind`
* `wimp_create_icon`, `wimp_delete_icon`
* `wimp_open_wind`, `wimp_close_wind`
* `wimp_get_wind_state`, `wimp_get_wind_info`, `wimp_get_icon_info`
* `wimp_set_extent`, `wimp_force_redraw`, `wimp_getwindowoutline`

Polling and messages:

* `wimp_poll`, `wimp_pollidle`
* `wimp_sendmessage`
* `wimp_processkey`

Redraw/open protocols:

* `wimp_redraw_wind`
* `wimp_update_wind`
* `wimp_get_rectangle`

Menus and templates:

* `wimp_create_menu`, `wimp_create_submenu`, `wimp_decode_menu`
* `wimp_open_template`, `wimp_load_template`, `wimp_close_template`

Pointer/caret/palette:

* `wimp_get_point_info`, `wimp_drag_box`
* `wimp_set_caret_pos`, `wimp_get_caret_pos`
* `wimp_set_point_shape`
* `wimp_readpalette`, `wimp_setpalette`, `wimp_setcolour`

Task lifecycle:

* `wimp_initialise`, `wimp_closedown`, `wimp_taskclose`, `wimp_starttask`

### Practical interface notes

* `wimp_load_template()` is a thin register-block wrapper. The writable name
  buffer and indirected workspace rules from the Wimp PRM apply directly.
* `wimp_taskclose(t)` passes back the task handle plus the literal task ID
  word `"TASK"` to `Wimp_CloseDown`.
* `wimp_open_template()` and `wimp_close_template()` are just thin SWI calls;
  there is no extra lifetime management unless you use `template.h`.

## `wimpt.h`

`wimpt` is the common startup and polling layer for small applications.

### Main functions

* `wimpt_wimpversion(int version)`: set the minimum Wimp version before init.
* `wimpt_messages(wimp_msgaction *messages)`: set the required message list
  before init. The list must end with `wimp_MCLOSEDOWN`.
* `wimpt_init(char *programname)`: calls `Wimp_Initialise`, stores the task
  handle, initialises mode cache, and arranges clean shutdown.
* `wimpt_poll(mask, result)`: preferred poll wrapper.
* `wimpt_fake_event()`: injects an event to be returned by `wimpt_poll()`.
* `wimpt_last_event()`, `wimpt_last_event_was_a_key()`: inspect the last
  event returned by `wimpt_poll()`.
* `wimpt_task()`: returns the Wimp task handle.
* `wimpt_programname()`: returns the name passed to `wimpt_init()`.
* `wimpt_noerr()`, `wimpt_complain()`, `wimpt_reporterror()`: standard error
  handling/reporting helpers.
* `wimpt_checkmode()`, `wimpt_mode()`, `wimpt_dx()`, `wimpt_dy()`,
  `wimpt_bpp()`: cached screen-mode information.
* `wimpt_install_signal_handlers()`: explicit install if needed before init.

### Behaviour from the implementation

* If you did not call `wimpt_wimpversion()`, `wimpt_init()` chooses:
  * version `200` when no message list was supplied
  * version `300` when a message list was supplied
* If the chosen version is `300` and you did not set a message list, the
  implementation supplies a single-entry list ending at `wimp_MCLOSEDOWN`.
* `wimpt_init()` installs signal handlers, records the returned task handle,
  calls `wimpt_checkmode()`, registers an `atexit()` close-down handler, and
  initialises the `win` module.
* `wimpt_noerr()` raises an OS error via `OS_GenerateError` rather than merely
  returning the error pointer.

### Practical startup and background-message patterns

* If the task needs iconbar or background Wimp messages without a normal
  application window, register a handler on `win_ICONBARLOAD` and then claim
  unknown events for that pseudo-window. That gives a concrete sink for
  `DataLoad`, `DataOpen`, `PreQuit`, help, palette/mode-change, and similar
  task-level messages.
* Keep the `wimpt_messages()` list complete for every message family the task
  expects to receive. If a protocol handler is wired up in the poll loop but
  the message number is absent from the initialisation list, the task will not
  see that message reliably.
* `wimpt_init()` is usually followed immediately by initialisers for the
  higher-level helper modules that depend on the Wimp already being live, such
  as `dbox_init()`, resource/template loading, sprite resources, or menu/icon
  setup.

Concrete recipe for an iconbar task with background messages:

1. Build a `wimp_msgaction` list covering every protocol the task expects, and
   terminate it with `wimp_MCLOSEDOWN`.
2. Call `wimpt_wimpversion(...)` if a specific minimum Wimp version is
   required.
3. Call `wimpt_messages(messages)`.
4. Call `wimpt_init(task_name)`.
5. Create the iconbar icon and any fixed top-level menus.
6. Register a background handler on `win_ICONBARLOAD` with
   `win_register_event_handler(win_ICONBARLOAD, handler, handle)`.
7. Call `win_claim_unknown_events(win_ICONBARLOAD)` if that background handler
   should receive task-level messages that are not part of the `win` module's
   built-in known-event set.
8. Install any task-global unknown-event processors, then enter the normal
   `event_process()` or `wimpt_poll()` loop.

## `win.h` and `event.h`

These two modules are the normal dispatch layer above `wimpt`.

### `win.h`

Window dispatch:

* `win_register_event_handler(wimp_w, handler, handle)`: attach/remove a
  per-window handler.
* `win_read_eventhandler()`: inspect a registration.
* `win_processevent()`: dispatch one event through the window system.

Idle and unknown events:

* `win_claim_idle_events(wimp_w)` / `win_idle_event_claimer()`
* `win_claim_unknown_events(wimp_w)` / `win_unknown_event_claimer()`
* `win_add_unknown_event_processor(proc, handle)`
* `win_remove_unknown_event_processor(proc, handle)`

Menu attachment/state:

* `win_setmenuh()`, `win_getmenuh()`

Other helpers:

* `win_activeinc()`, `win_activedec()`, `win_activeno()`: active-window count.
* `win_give_away_caret()`
* `win_settitle()`
* `win_init()`

Known-vs-unknown event split in this implementation:

* Known events are `ENULL`, `EREDRAW`, `ECLOSE`, `EOPEN`, `EPTRLEAVE`,
  `EPTRENTER`, `EKEY`, `ESCROLL`, `EBUT`, plus sent messages for
  `MCLOSEDOWN`, `MDATASAVE`, `MDATALOAD`, and `MHELPREQUEST`.
* Everything else goes through the unknown-event processor stack and then the
  unknown-event claimer window, if any.

Practical consequences:

* Use `win_add_unknown_event_processor()` for task-global protocols that are
  not tied to one ordinary window, such as help fallbacks, drag/file-transfer
  helpers, or other message families that should run before per-window logic.
* Use `win_claim_unknown_events(window)` when one specific window or pseudo
  window should receive the leftover unknown traffic after the processors have
  had a chance to inspect it.
* `win_register_event_handler()` is the normal final step immediately after
  `wimp_create_wind()`. If you are creating a window wrapper helper, keep that
  registration in the same helper so that a half-created window does not
  escape without a handler.

### `event.h`

* `event_process()`: the standard top-level poll-and-dispatch loop step.
* `event_anywindows()`: whether the library still thinks windows are active.
* `event_attachmenu(window, menu, proc, handle)`: attach a fixed menu.
* `event_attachmenumaker(window, maker, proc, handle)`: build the menu on
  demand when it is about to be shown.
* `event_clear_current_menu()`
* `event_setmask()`, `event_getmask()`
* `event_is_menu_being_recreated()`: whether the current maker call is part of
  an Adjust reopen rather than a first open.

Use `event_attachmenumaker()` when the menu contents depend on live state.

When using `event_attachmenumaker()`:

* Recompute pointer-sensitive or selection-sensitive state only on the first
  open. On Adjust-driven recreation, use `event_is_menu_being_recreated()` to
  preserve the original logical target where practical, and revalidate it
  against current model objects instead of blindly re-picking from the pointer.
* If the menu-help token family changes with the menu being built, register the
  appropriate `help_register_handler()` inside the menu-maker before returning
  the menu. The help module stores one task-global handler, so menu help should
  be rebound to match the currently active menu tree.

Concrete recipe for a dynamic menu maker:

1. Keep explicit task state for the current top-level menu, popup coordinates,
   and logical target object.
2. In the maker, test `event_is_menu_being_recreated()`.
3. On the first open, derive the logical target from the pointer or click
   context and store it.
4. On Adjust reopen, reuse the stored target if it is still valid; only
   re-pick from the pointer if the stored object has disappeared.
5. Update ticked, shaded, writable, and submenu state from the current model.
6. If menu help uses a task-global token family, call
   `help_register_handler()` for that family before returning the menu.
7. Return a menu object whose backing storage and indirected buffers will stay
   valid until the Wimp deletes the menu tree.

## `template.h`

This is the library's in-memory template cache.

### Public API

* `template_init()`: loads the application's `Templates` resource.
* `template_loaded()`: whether anything was loaded.
* `template_find(name)`: returns the cached template wrapper.
* `template_copy(template *from)`: duplicate a cached template record.
* `template_syshandle(name)`: returns the underlying `wimp_wind *`.
* `template_use_fancyfonts()`: request font-reference tracking before loading.

### Structure shape

The public `template` structure contains:

* `next`: linked-list pointer.
* `name[12]`: template name returned by the Wimp.
* `workspace`: start of indirected workspace.
* `workspacesize`: size of that workspace.
* `window`: the `wimp_wind` definition loaded from the template.

### Behaviour from the implementation

* `template_init()` always resolves `<App$Dir>.Templates` through
  `res_findname("Templates", ...)`.
* Each template is loaded into one allocation containing:
  * the wrapper structure
  * the full `wimp_wind` block and following icon definitions
  * a persistent indirected workspace block
* The implementation sets `window.spritearea = resspr_area()` on every loaded
  template.
* `template_use_fancyfonts()` must be called before `template_init()`. It
  allocates the font-reference array used by `Wimp_LoadTemplate`.

Practical guidance:

* If the application package name or lookup context is uncertain, avoid
  assuming the implicit `Templates` search. Read the template resource by an
  explicit application path first, then use `template_*` helpers over the
  already-opened resource.
* `template_syshandle(name)` returns the live cached `wimp_wind *`, so direct
  field tweaks are possible before window creation. That is useful for cases
  such as fixing `spritearea`, changing default flags, or reusing a template
  as a base structure for multiple created windows. Treat those edits as
  persistent changes to the cached template, not one-shot scratch mutations.

## `menu.h`

`menu` is a higher-level mutable wrapper around a live `wimp_menustr`.

### Description-string syntax

Entry separators:

* `,` separates normal adjacent items.
* `|` inserts a line/gap before the next item.

Entry prefixes:

* `!` tick the item.
* `~` fade the item.
* `>` mark it as a dialogue/submenu entry.

Entries are indexed from `1`, not `0`.

### Public API

* `menu_new(name, description)`
* `menu_dispose(&menu, recursive)`
* `menu_extend(menu, description)`
* `menu_setflags(menu, entry, tick, fade)`
* `menu_submenu(menu, entry, submenu)`
* `menu_make_writeable(menu, entry, buffer, bufferlength, validstring)`
* `menu_make_sprite(menu, entry, spritename)`
* `menu_syshandle(menu)`: returns the underlying `wimp_menustr *`.

### Important details

* Backing storage is stable heap memory owned by the `menu` object; the Wimp
  uses that memory in place.
* `menu_make_writeable()` and `menu_make_sprite()` depend on caller-owned
  buffers/names remaining valid.
* Once a menu is attached as a submenu, the interface treats it as part of a
  strict hierarchy. Do not extend or free it independently.
* The wrapper does not prevent direct edits to the returned `wimp_menustr *`
  and `wimp_menuitem *` fields. That escape hatch is sometimes necessary for
  header-width changes, title rewrites, special menu flags, or other Wimp
  fields the convenience API does not expose, but the storage still has to
  remain valid while the menu is live.

## `dbox.h`

`dbox` wraps a dialogue-box window built from a loaded template.

### Core functions

Lifecycle and visibility:

* `dbox_new(name)`
* `dbox_dispose(&dbox)`
* `dbox_show(dbox)`: transient, near the last menu selection/caret position.
* `dbox_showstatic(dbox)`: ordinary persistent display.
* `dbox_hide(dbox)`

Fields:

* `dbox_setfield`, `dbox_getfield`
* `dbox_setnumeric`, `dbox_getnumeric`
* `dbox_fadefield`, `dbox_unfadefield`

Interaction:

* `dbox_get(dbox)`: non-blocking field/action read.
* `dbox_read(dbox)`: raw read helper.
* `dbox_eventhandler()`: field-level callback.
* `dbox_raw_eventhandler()`: raw Wimp-event callback.
* `dbox_fillin()`: modal loop; places caret at the end of the lowest writable.
* `dbox_fillin_fixedcaret()`: modal loop without moving the caret.
* `dbox_popup(name, message)`: simple one-shot popup.
* `dbox_persist()`: whether the last fillin action requested persistence.
* `dbox_syshandle(dbox)`: underlying `wimp_w`.
* `dbox_init()`

### Field model

`dbox_field` is an integer icon/field index.

`dbox_fieldtype` distinguishes:

* `dbox_FACTION`
* `dbox_FOUTPUT`
* `dbox_FINPUT`
* `dbox_FONOFF`

Special result:

* `dbox_CLOSE` is `(dbox_field)-1`.

### Practical details

* `dbox_new()` registers the underlying window with the `win` system
  immediately, even before showing it.
* `dbox_setfield()` truncates to the icon's indirected buffer length, or to
  12 bytes for a non-indirected text icon.
* `dbox_fillin()` runs by repeatedly calling `event_process()`, so it depends
  on the rest of the event subsystem being initialised and cooperating.
* `dbox_raw_eventhandler()` is the right hook when the dialogue needs to
  inspect raw Wimp events such as `EKEY`, `EBUT`, or help requests rather than
  only completed field actions.
* `dbox_syshandle()` lets you mix the dialogue wrapper with lower-level Wimp
  helpers such as `win_register_event_handler()`, `wimp_set_caret_pos()`, or
  explicit synthetic events sent back to one dialogue icon.

## Help and file-transfer helpers

### `help.h`

* `help_process(e)`: process `Message_HelpRequest`.
* `help_register_handler(proc, handle)`: one task-global menu-help handler.
* `help_genmessage(prefix, hit)`: generate a message-token name from a hit
  string and reply from the Messages file.
* `help_simplehandler(handle, hit)`: thin wrapper around `help_genmessage()`.
* `help_dboxrawevents(dbox, event, handle)`: dialogue-box help support.
* `help_reply(message)`: send the reply explicitly.

The implementation stores one global handler/handle pair.

Practical consequence:

* `help_register_handler()` is task-global state, not menu-local or
  window-local state. If different menus need different token families, set the
  handler immediately before returning the active menu.

### `xfersend.h`

Caller callback types:

* `xfersend_saveproc(filename, handle)`: save to a real file.
* `xfersend_sendproc(handle, &maxbuf)`: perform RAM transfer by calling
  `xfersend_sendbuf()`.
* `xfersend_printproc(filename, handle)`: print or save-for-printing.

Public functions:

* `xfersend(...)`: drag-to-save/export from a mouse-drag event.
* `xfersend_print(...)`: queue/trigger printing.
* `xfersend_pipe(...)`: send without a drag gesture, to a known task.
* `xfersend_sendbuf(buffer, size)`: push one RAM-transfer chunk.
* `xfersend_file_is_safe()`, `xfersend_set_fileissafe()`
* `xfersend_close_on_xfer(do_close, window)`
* `xfersend_clear_unknowns()`
* `xfersend_read_last_ref()`

Implementation-backed details:

* The module tracks global transfer state; one active transfer path at a time
  is the safe assumption.
* `xfersend()` installs unknown-event processors to drive the protocol.
* `xfersend_sendbuf()` uses `wimp_transferblock()` and may run a nested
  `event_process()` loop waiting for the receiver's next fetch/ack.
* `xfersend_close_on_xfer(TRUE, w)` causes an `ECLOSE` event to be sent to the
  given window when the transfer completes.

### `xferrecv.h`

* `xferrecv_checkinsert(&filename)`: handle `MDATALOAD` / `MDATAOPEN`.
* `xferrecv_insertfileok()`: acknowledge completed insert and delete the scrap
  file if needed.
* `xferrecv_checkprint(&filename)`, `xferrecv_printfileok(type)`
* `xferrecv_checkimport(&estsize)`: handle `MDATASAVE`.
* `xferrecv_doimport(buf, size, buffer_processor)`: drive RAM import.
* `xferrecv_file_is_safe()`

Implementation-backed details:

* Safety is derived from whether the sender used the scrap-file path.
* `xferrecv_doimport()` temporarily installs an unknown-event processor and
  loops on `event_process()` until the transfer finishes or breaks.
* The buffer processor is called only when the sender exactly filled the
  current buffer with a non-zero chunk.

### `saveas.h`

* `saveas(...)`: display the standard `xfer_send` template and export data.
* `saveas_read_leafname_during_send(name, length)`: read back the live leaf
  name while the save box is active.

The implementation expects a template called `xfer_send`, uses `fileicon()`
for the file-type icon, and hooks `xfersend_close_on_xfer()` so the dialogue
can close after a transfer.

### `fileicon.h`

* `fileicon(window, icon, filetype)`: rewrite an existing icon to display the
  standard Wimp file icon for the given file type.

### Smaller UI helpers

* `baricon.h`:
  * `baricon()`, `baricon_left()`
  * `baricon_textandsprite()`, `baricon_textandsprite_left()`
  * `baricon_newsprite()`
  * Caveat: effectively one global click handler/icon instance.
* `colourmenu.h`:
  * `colourmenu_make(title, includeNone)`: returns a `menu` containing the
    16 Wimp colours, optionally plus `None`.
  * The implementation reads the current palette and chooses black or white
    text depending on colour brightness.
* `magnify.h`:
  * `magnify_select(...)`: drives a `magnifier` template with the documented
    icon layout.
* `pointer.h`:
  * `pointer_set_shape(area, id, hotx, hoty)`
  * `pointer_reset_shape()`
* `visdelay.h`:
  * `visdelay_init()`, `visdelay_begin()`, `visdelay_percent()`, `visdelay_end()`
  * Intended for hourglass/progress indication around visible delays.

## `colourpick.h`

This header is data-only in this source tree.

### Main abstract/data types

* `colourpicker_d`: opaque dialogue handle.
* `colourpicker_colour`:
  * `colour`: packed current colour value.
  * `size`: size in bytes of the model-specific payload.
  * `info[]`: model-specific payload.
* `colourpicker_dialogue`:
  * `flags`: dialogue behaviour bits.
  * `title`: title string.
  * `visible`: visible box.
  * `xscroll`, `yscroll`
  * `colour`, `size`, `info[]`
* `colourpicker_model`:
  * `flags`, `name`, `description`
  * `info_size`
  * `pane_size`
  * `entries[8]`: model entry-point table indexed by `colourpicker_ENTRY_*`
* Message payload structs:
  * `colourpicker_message_colour_choice`
  * `colourpicker_message_colour_changed`
  * `colourpicker_message_open_parent_request`
  * `colourpicker_message_close_dialogue_request`

### Important constants

Dialogue flags:

* `colourpicker_DIALOGUE_OFFERS_TRANSPARENT`
* `colourpicker_DIALOGUE_TRANSPARENT`
* `colourpicker_DIALOGUE_TYPE`, with shift/value constants
* `colourpicker_DIALOGUE_IGNORE_HELP`

Open/update flags:

* `colourpicker_OPEN_TRANSIENT`
* `colourpicker_OPEN_SUB_MENU`
* `colourpicker_UPDATE_*`

Colour/message/model constants:

* `colourpicker_COLOUR_TRANSPARENT`
* `colourpicker_COLOUR_DRAGGING`
* `colourpicker_MODEL_RGB`, `CMYK`, `HSV`
* `message_COLOUR_PICKER_*`

Use this header when you need the block layouts or message IDs, but expect to
call the ColourPicker SWIs directly or through another wrapper layer.
