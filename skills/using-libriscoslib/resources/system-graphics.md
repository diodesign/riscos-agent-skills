# System, resources, graphics, and printing

This note covers the non-text parts of `RISC_OSLib` outside the main Wimp/UI
helpers.

## `os.h`

`os.h` is the low-level OS/SWI utility header.

### Main types and macros

* `os_regset`: register block used by the SWI wrappers.
* `os_error`: standard RISC OS error block.
* `os_X`: X-bit modifier for SWIs.
* `os_swi(...)`, `os_swix(...)`: direct SWI wrappers using an `os_regset`.
* `os_swi0`..`os_swi6`, `os_swi1r`..`os_swi6r`: variadic wrappers for common
  input/output register shapes.
* `os_swix0`..`os_swix6`, `os_swix1r`..`os_swix6r`: X-bit forms.

### Common wrapper functions

* `os_byte(a, &x, &y)`
* `os_word(code, p)`
* `os_gbpb(block)`
* `os_file(block)`
* `os_args(regs)`
* `os_find(regs)`
* `os_cli(cmd)`
* `os_read_var_val(name, buf, size)`

This header is for code that needs direct OS entry points but prefers
slightly more C-shaped call sites than raw `_swix()`.

## Resources and messages

### `res.h`

* `res_init(progname)`: set the application prefix used for resources.
* `res_findname(resname, buf)`: build `ProgramName:resname`.
* `res_openfile(resname, mode)`: open a resource by leafname.

Behaviour from the implementation:

* `res_findname()` builds `programname:leafname`.
* `res_openfile()` tries a country-specific variant first when opening for
  read, then falls back to the unsuffixed name.

### `msgs.h`

* `msgs_init()`: load `Messages` from the application resource area.
* `msgs_lookup(tag_or_tag:default)`: main token lookup helper.
* `msgs_main_control_block()`: MessageTrans control block for the app file.
* `msgs_default_control_block()`: control block for the library-default file.

Important details:

* The application messages file is expected to be named `Messages`.
* `msgs_lookup("Token:Fallback text")` returns the found message if present,
  otherwise the text after the colon.
* The implementation also falls back to the library-default messages file
  `RISC_OSLibrary:Messages`.

Constants:

* `msgs_TAG_MAX`
* `msgs_MSG_MAX`
* `msgs_VARIANT_MAX`

### `msgtrans.h`

This is mostly direct macro wrappers around MessageTrans SWIs.

* `msgtrans_control_block`
* `msgtrans_file_info`
* `msgtrans_open_file`
* `msgtrans_lookup`
* `msgtrans_gs_lookup`
* `msgtrans_error_lookup`
* `msgtrans_make_menus`
* `msgtrans_close_file`

Use this when you want direct MessageTrans access rather than `msgs_lookup()`.

## Memory helpers

### `flex.h`

`flex` manages a movable expandable block.

* `flex_alloc(anchor, n)`
* `flex_free(anchor)`
* `flex_size(anchor)`
* `flex_extend(anchor, newsize)`
* `flex_midextend(anchor, at, by)`
* `flex_init()`

`anchor` is a pointer-to-pointer (`flex_ptr`) so the implementation can move
the underlying block.

### `heap.h`

`heap` builds a malloc-like allocator on top of a flex block.

* `heap_init(heap_shrink)`: call after `flex_init()`.
* `heap_alloc(size)`
* `heap_free(ptr)`

The header notes that allocation can fail if the underlying flex block must
move or cannot be extended.

## Timing, tracing, and simple utilities

### `alarm.h`

Alarm queue for Wimp tasks.

* `alarm_handler(called_at, handle)`: callback type.
* `alarm_init()`
* `alarm_timenow()`
* `alarm_timedifference(t1, t2)`: wrap-safe monotonic delta.
* `alarm_set(at, proc, handle)`
* `alarm_remove(at, handle)`
* `alarm_removeall(handle)`
* `alarm_anypending(handle)`
* `alarm_next(&time)`
* `alarm_callnext()`

Implementation-backed behaviour:

* Alarms are kept in time order in a linked list.
* `alarm_init()` cancels and frees all pending alarms.
* Typical polling code should use `alarm_next()` and then `wimp_pollidle()`.

### `trace.h`

Compile-time-controlled tracing.

* `TRACE` controls whether trace calls are active.
* `tracef`, `tracef0`..`tracef4`
* `trace_is_on()`, `trace_on()`, `trace_off()`

When `TRACE` is unset, the numbered trace macros compile away.

### `werr.h`

* `werr(fatal, format, ...)`: report an error through a Wimp-style path.

### `ctl.h`

Command/menu binding helper layer.

Types:

* `ctl_action_proc`
* `ctl_entry_proc`

Main functions:

* `ctl_init(load)`, `ctl_load()`
* `ctl_attach_menu(window, ctlname, menuname, handle)`
* `ctl_add_action(name, syntax, proc, handle)`
* `ctl_tick_action`, `ctl_untick_action`
* `ctl_set_action_text`
* `ctl_set_caret_in_action`
* `ctl_disable_action`, `ctl_enable_action`
* `ctl_make_action_writeable`
* `ctl_find_entries`
* `ctl_process()`
* `ctl_attach_external_menu`
* `ctl_return_external_hit()`

Special constant:

* `win_ICONBAR` here is `-3` for iconbar attachment.

This header is a higher-level convenience layer. Use it only if the command
table/menu pattern already exists in the codebase.

### `dboxquery.h`, `dboxfile.h`, `dboxtcol.h`

Small dialogue helpers:

* `dboxquery(question)`: yes/no style query result.
* `dboxquery_close(question)`, `dboxquery_quit(question)`: specialised query
  dialogues.
* `dboxfile(message, filetype, buf, bufsize)`: file-name query helper.
* `dboxtcol_colourhandler`
* `dboxtcol_Transparent`

Use these when the standard template names they expect are already present.

## BBC-style graphics and sound: `bbc.h`

This is an older compatibility layer that wraps VDU and related SWIs.

### Important constant families

VDU command constants:

* `bbc_CharToPrinter` through `bbc_MoveText`

Plot action constants:

* line/point/fill/circle/ellipse families such as `bbc_SolidBoth`,
  `bbc_Point`, `bbc_RectangleFill`, `bbc_Circle`, `bbc_Ellipse`
* movement variants such as `bbc_MoveCursorAbs`, `bbc_DrawAbsFore`
* block variants such as `bbc_BMoveAbs`, `bbc_BCopyRectAbs`

### Main functions

Text/VDU:

* `bbc_vdu`, `bbc_vduw`, `bbc_vduq`
* `bbc_stringprint`, `bbc_cls`, `bbc_colour`
* `bbc_pos`, `bbc_vpos`, `bbc_tab`

Graphics:

* `bbc_plot`, `bbc_mode`
* `bbc_move`, `bbc_moveby`, `bbc_draw`, `bbc_drawby`
* `bbc_rectangle`, `bbc_rectanglefill`
* `bbc_circle`, `bbc_circlefill`
* `bbc_origin`, `bbc_gwindow`, `bbc_clg`
* `bbc_fill`, `bbc_gcol`, `bbc_tint`, `bbc_palette`
* `bbc_point`

Mode/VDU variables and input:

* `bbc_vduvar`, `bbc_vduvars`, `bbc_modevar`
* `bbc_get`, `bbc_cursor`, `bbc_adval`, `bbc_inkey`

Sound:

* `bbc_getbeat`, `bbc_getbeats`, `bbc_gettempo`
* `bbc_setbeats`, `bbc_settempo`
* `bbc_sound`, `bbc_soundoff`, `bbc_soundon`
* `bbc_stereo`, `bbc_voices`

The implementation is mostly straightforward sequences of VDU writes or SWIs.

## Coordinates and colours

### `coords.h`

Types:

* `coords_cvtstr`: conversion context.
* `coords_pointstr`: point.

Functions:

* `coords_x_toscreen`, `coords_y_toscreen`
* `coords_x_toworkarea`, `coords_y_toworkarea`
* `coords_box_toscreen`, `coords_box_toworkarea`
* `coords_point_toscreen`, `coords_point_toworkarea`
* `coords_withinbox`
* `coords_offsetbox`
* `coords_intersects`
* `coords_boxesoverlap`

Use this when your code mixes work-area-relative and screen coordinates.

### `colourtran.h`

Wrappers around ColourTrans conversion logic:

* `colourtran_returnGCOL(entry, &gcol)`
* `colourtran_return_colournumber(entry, &col)`
* `colourtran_return_OppGCOL(entry, &gcol)`
* `colourtran_GCOL_tocolournumber(gcol, &col)`
* `colourtran_colournumbertoGCOL(col, &gcol)`
* `colourtran_invalidate_cache()`

These convert between:

* `wimp_paletteword` values
* Wimp colour numbers
* GCOL actions/values

## Fonts: `font.h`

This is the main Font Manager wrapper.

### Core types

* `font`: opaque font handle.
* `font_def`:
  * `name[16]`
  * `xsize`, `ysize` in sixteenths of a point
  * `xres`, `yres` in dpi
  * `usage`
  * `age`
* `font_info`:
  * `minx`, `miny`, `maxx`, `maxy`
* `font_string`:
  * `s`: string pointer
  * `x`, `y`: in/out position
  * `split`: split character on input, count on output
  * `term`: termination index in/out
* `font_state`:
  * `f`
  * `back_colour`
  * `fore_colour`
  * `offset`
* `font_threshold`: threshold settings block.

### Important constants

Paint options:

* `font_JUSTIFY`
* `font_RUBOUT`
* `font_ABS`
* `font_OSCOORDS`

Colour packing helpers:

* `font_BlueGun`
* `font_GreenGun`
* `font_RedGun`

### Main functions

Font lifecycle/state:

* `font_cacheaddress`
* `font_find`
* `font_lose`
* `font_setfont`
* `font_current`
* `font_future`

Metrics and conversion:

* `font_readdef`
* `font_readinfo`
* `font_strwidth`
* `font_converttoos`
* `font_converttopoints`
* `font_findcaret`
* `font_findcaretj`
* `font_charbbox`
* `font_stringbbox`
* `font_readscalefactor`
* `font_setscalefactor`
* `font_readthresholds`
* `font_setthresholds`

Painting/output:

* `font_paint`
* `font_caret`
* `font_setcolour`
* `font_output_size`
* `font_output_to_screen`

Enumeration/menu support:

* `font_list`
* `font_makemenu`
* `font_decodemenu`

## Sprites and DragASprite

### `sprite.h`

Core types:

* `sprite_palflag`: `sprite_nopalette` / `sprite_haspalette`
* `sprite_factors`: `xmag`, `ymag`, `xdiv`, `ydiv`
* `sprite_area`:
  * `size`
  * `number`
  * `sproff`
  * `freeoff`
* `sprite_header`:
  * `next`
  * `name[12]`
  * `width`, `height`
  * `lbit`, `rbit`
  * `image`
  * `mask`
  * `mode`
* `sprite_id`:
  * `s.name` or `s.addr`
  * `tag`: `sprite_id_name` or `sprite_id_addr`
* `sprite_mainarea`: `(sprite_area *)0`

Main functions:

Screen and area operations:

* `sprite_screensave`, `sprite_screenload`
* `sprite_area_initialise`
* `sprite_area_readinfo`
* `sprite_area_reinit`
* `sprite_area_load`, `sprite_area_merge`, `sprite_area_save`

Create/capture/select/manage:

* `sprite_getname`
* `sprite_get`, `sprite_get_rp`
* `sprite_get_given`, `sprite_get_given_rp`
* `sprite_create`, `sprite_create_rp`
* `sprite_select`, `sprite_select_rp`
* `sprite_delete`, `sprite_rename`, `sprite_copy`

Plot and transform:

* `sprite_put`, `sprite_put_given`
* `sprite_put_scaled`, `sprite_put_scaled_given`
* `sprite_put_mask`, `sprite_put_mask_given`
* `sprite_create_mask`, `sprite_remove_mask`
* `sprite_insert_row`, `sprite_delete_row`
* `sprite_insert_column`, `sprite_delete_column`
* `sprite_flip_x`, `sprite_flip_y`

State/output:

* `sprite_readsize`, `sprite_readpixel`, `sprite_readmask`
* `sprite_readsavearea`, `sprite_readsavelog2`, `sprite_readfactors`
* `sprite_readinfo`, `sprite_readpalette`, `sprite_readcontrol`
* `sprite_restorestate`
* `sprite_outputtoscreen`
* `sprite_sizeof_screencontext`
* `sprite_removewastage`

The `sprite_id.tag` must be set correctly by the caller before use.

### `dragasprit.h`

* `dragasprite_options`: packed options for justification, bounding mode, and
  drop-shadow behaviour.
* `dragasprite_start(options, area, name, box, userbox)`
* `dragasprite_stop()`

`xfersend` uses this when the system configuration says DragASprite is active.

### `resspr.h`

* `resspr_init()`
* `resspr_area()`: sprite area containing the loaded resource sprites.

Templates loaded through `template.h` are rebound to this sprite area.

## Draw-file helpers

### `drawftypes.h`

Core Draw-file structure and packed-style definitions used by the other Draw
headers, including the style bit masks:

* `packmask_join`
* `packmask_endcap`
* `packmask_startcap`
* `packmask_windrule`
* `packmask_dashed`

and the corresponding shifts.

### `drawferror.h`

Named verification/error codes such as:

* `draw_BadObject`
* `draw_BBoxWrong`
* `draw_BadPathTag`
* `draw_NotDrawFile`
* `draw_BadObjectType`
* text-area-specific validation failures

Use these when reporting or interpreting Draw verification results.

### `drawmod.h`

Low-level Draw-module structures and constants, including:

* path-element structures
* join styles: `join_mitred`, `join_round`, `join_bevelled`
* cap styles: `cap_butt`, `cap_round`, `cap_square`, `cap_triang`

### `drawfdiag.h`

Diagram-level helpers.

Main functions/types:

* `draw_verify_diag(diag, error)`
* `draw_append_diag(diag1, diag2, error)`
* `draw_shift_diag(diag, xMove, yMove)`
* `draw_queryBox(diag, box, screenUnits)`
* `draw_convertBox(from, to, toScreen)`
* `draw_rebind_diag(diag)`
* `drawfdiag_init()`
* callback types:
  * `draw_allocate`
  * `draw_extend`
  * `draw_free`
  * `draw_unknown_object_handler`

Useful macros:

* `draw_drawToScreen(i)`
* `draw_screenToDraw(i)`

### `drawfobj.h`

Object-level Draw helpers.

* `draw_NoObject`
* `draw_FirstObject`
* `draw_LastObject`
* `draw_create_diag(diag, creator, bbox)`
* `draw_setFontTable(diag)`
* `draw_translateText(diag)`
* `drawfobj_init()`

## Printing: `print.h`

Printer driver support.

### Key enums and structures

* `print_identity`: `print_PostScript`, `print_FX80compatible`
* `print_features`: colour capability, shape limitations, screendump support,
  transform support
* `print_infostr`:
  * `version`
  * `identity`
  * `xres`, `yres`
  * `features`
  * `description`
  * `xhalf`, `yhalf`
  * `number`
* `print_box`: `x0`, `y0`, `x1`, `y1`
* `print_pagesizestr`:
  * `xsize`, `ysize`
  * `bbox`
* `print_transmatstr`: `xx`, `xy`, `yx`, `yy`
* `print_positionstr`: `dx`, `dy`

Units:

* page sizes and positions are in `1/72000` inch
* rectangle coordinates passed to `print_giverectangle()` are OS units
* transform matrix values are fixed-point with 16 binary places

### Main functions

Driver/job configuration:

* `print_info`, `print_setinfo`
* `print_checkfeatures`
* `print_pagesize`, `print_setpagesize`
* `print_selectjob`, `print_currentjob`
* `print_endjob`, `print_abortjob`, `print_canceljob`, `print_reset`
* `print_selectillustration`

Page/rectangle output:

* `print_giverectangle`
* `print_drawpage`
* `print_getrectangle`
* `print_screendump`

Use this layer when talking to the printer driver directly rather than going
through the user-facing Save/print drag protocols.
