# Text and editing helpers

This note covers the `txt*` and editor-facing parts of `RISC_OSLib`.

## `txt.h`

`txt` is the library's editable text-buffer object. It combines:

* a mutable character array
* a notion of `dot` (caret position in the text model)
* optional window display
* selection and markers
* a small event queue/callback mechanism

The handle type is `typedef struct txt1_str *txt;`.

### Lifecycle and display

* `txt_new(title)`: create an empty text object.
* `txt_show(t)`: show it in a free-standing window.
* `txt_hide(t)`
* `txt_settitle(t, title)`
* `txt_dispose(&t)`

### Buffer sizing and flags

* `txt_bufsize(t)`: current storage capacity.
* `txt_setbufsize(t, n)`: enlarge capacity so at least `n` characters fit.
* `txt_charoptions(t)`: current `txt_charoption` flags.
* `txt_setcharoptions(t, affect, values)`
* `txt_setdisplayok(t)`: re-enable display updates after a batched edit.

`txt_charoption` bits:

* `txt_DISPLAY`: redraw as edits happen.
* `txt_CARET`: show a visible caret.
* `txt_UPDATED`: content has been modified.

### Dot, size, and editing operations

Indices use `txt_index`, an integer in the range `0..size`.

Main functions:

* `txt_dot(t)`, `txt_setdot(t, i)`, `txt_movedot(t, by)`
* `txt_size(t)`
* `txt_insertchar(t, c)`, `txt_insertstring(t, s)`
* `txt_delete(t, n)`
* `txt_replacechars(t, ntodelete, a, n)`
* `txt_replaceatend(t, ntodelete, a, n)`
* `txt_charatdot(t)`, `txt_charat(t, i)`
* `txt_charsatdot(t, buffer, &n)`
* `txt_movevertical(t, by, caretstill)`
* `txt_movehorizontal(t, by)`
* `txt_visiblelinecount(t)`, `txt_visiblecolcount(t)`

### Markers

Markers track positions through edits.

* `txt_newmarker(t, &mark)`
* `txt_movemarker(t, &mark, to)`
* `txt_movedottomarker(t, &mark)`
* `txt_indexofmarker(t, &mark)`
* `txt_disposemarker(t, &mark)`

### Selection

* `txt_selectset(t)`
* `txt_selectstart(t)`, `txt_selectend(t)`
* `txt_setselect(t, start, end)`

### Event queue and callback support

* `txt_get(t)`: retrieve the next `txt_eventcode`.
* `txt_queue(t)`: number of queued events.
* `txt_unget(t, code)`: push one back.
* `txt_eventhandler(t, proc, handle)`: register a callback.
* `txt_readeventhandler(t, &proc, &handle)`

### Access to the backing characters

* `txt_arrayseg(t, at, &a, &n)`: returns a contiguous segment of the backing
  store starting at logical index `at`.

This is important for streaming and bulk operations. The buffer can be gapped
or wrapped internally, so `txt_arrayseg()` gives you one contiguous run, not
necessarily the whole remainder of the text.

### Other state

* `txt_lastref(t)`, `txt_setlastref(t, ref)`: used to track the
  `Message_DataSaved` reference associated with the current unmodified state.
* `txt_syshandle(t)`: underlying Wimp window handle.
* `txt_init()`

## `txtedit.h`

`txtedit` layers !Edit-like behaviour on top of `txt`.

### Main state structure

`txtedit_state` is public enough that callers often inspect it directly.

Fields:

* `t`: the underlying `txt`.
* `selpivot`: marker used by mouse-selection logic.
* `seltype`: `txtedit_CHARSEL`, `WORDSEL`, or `LINESEL`.
* `selectrecent`, `selectctl`: selection-tracking state.
* `filename[256]`: current file name, or an empty/null-name state.
* `ty`: `typdat` filetype/load-exec pair for the file.
* `deletepending`: internal selection/delete state.
* `next`: next state in the library's linked list of open editors.
* `overwrite`: overwrite mode flag.
* `wordtab`: whether tab/word behaviour is enabled.
* `wordwrap`: word-wrap mode flag.

Treat most fields as observable state rather than a stable ABI for mutation.
The safer pattern is to drive behaviour through the public functions.

### Creating and destroying editors

* `txtedit_install(t)`: attach editor behaviour to an existing `txt`.
* `txtedit_new(filename, filetype)`: open a file or create a new untitled
  editor.
* `txtedit_dispose(state)`
* `txtedit_getstates()`: head of the linked list of open editor states.

Behaviour from the implementation:

* `txtedit_new()` returns the existing state if the file is already open.
* The implementation attaches both a text-event handler and a dynamic
  menu-maker to the underlying `txt` window.

### Quitting and shutdown

* `txtedit_mayquit()`: prompts if needed and reports whether quitting is safe.
* `txtedit_prequit()`: handle Task Manager pre-quit flow.

`txtedit_prequit()` disposes open texts and sends the appropriate
acknowledgement only if `txtedit_mayquit()` allows it.

### Menus

* `txtedit_menu(state)`: build an !Edit-style menu for the current state.
* `txtedit_menuevent(state, hit)`: apply a menu hit string.

This menu is meant to be attached through `event_attachmenumaker()`.

### Import/open helpers

* `txtedit_doimport(state, filetype, estsize)`: handle RAM/file imports.
* `txtedit_doinsertfile(state, filename, replaceifwasnull)`: insert file
  contents, optionally adopting the file identity.
* `txtedit_settexttitle(state)`: refresh titles to reflect state.

The implementation uses `xferrecv_file_is_safe()` when deciding whether a
dragged-in file can safely become the editor's backing file identity.

### Callback registration

These all replace the current task-global handler and return the previous one.

* `txtedit_register_update_handler(h, handle)`
* `txtedit_register_save_handler(h, handle)`
* `txtedit_register_close_handler(h, handle)`
* `txtedit_register_shutdown_handler(h, handle)`
* `txtedit_register_undofail_handler(h, handle)`
* `txtedit_register_open_handler(h, handle)`

Important behaviour from the comments and implementation:

* The update handler can veto a recent modification by returning `FALSE`, but
  only when the change is small enough for the editor's undo path to reverse.
* The save handler is called for file saves, not RAM transfers.

### BASIC-specific helpers

* `txtedit_setBASICaddresses(tokenise, detokenise)`
* `txtedit_setBASICstrip(strip)`
* `txtedit_setBASICincrement(increment)`
* `txtedit_init()`

These configure the BASIC tokenise/detokenise support used by the editor.

## `txtwin.h`

This header exposes the window-management side of `txt`.

* `txtwin_new(t)`: create/show the text window support for a `txt`.
* `txtwin_number(t)`: window count/index information for that text.
* `txtwin_dispose(t)`
* `txtwin_setcurrentwindow(t)`

Use these only when you need to manage the text window layer explicitly rather
than through `txt_show()` and `txt_hide()`.

## `txtscrap.h`

Selection/scrap support for `txt`:

* `txtscrap_setselect(t, from, to)`
* `txtscrap_selectowner()`: which `txt` currently owns the selection.

## `txtopt.h`

Task-global option naming:

* `txtopt_set_name(name)`
* `txtopt_get_name()`

This is used by the editor/text layer for named option resources.

## `akbd.h`

Keyboard/type-ahead helpers for Wimp applications.

Constants:

* `akbd_Fn`, `akbd_Sh`, `akbd_Ctl`
* special-key codes such as `akbd_TabK`, `akbd_CopyK`, arrow keys,
  `akbd_Fn10`..`akbd_Fn12`, `akbd_InsertK`, `akbd_PrintK`,
  `akbd_PageUpK`, `akbd_PageDownK`

Functions:

* `akbd_pollsh()`: non-zero if SHIFT is down.
* `akbd_pollctl()`: non-zero if CTRL is down.
* `akbd_pollkey(&keycode)`: non-zero if type-ahead is available; returns the
  queued key code.

Implementation-backed detail:

* Function keys are reported as values above `256`, matching the Wimp event
  encoding.

## `typdat.h`

`typdat` is just:

* `ex`: exec address
* `ld`: load address

`txtedit_state.ty` uses it to carry the file's RISC OS type/date metadata.
