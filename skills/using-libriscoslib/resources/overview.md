# RISC_OSLib header map

This note summarises the public headers shipped by `RISC_OSLib` and points to
the more detailed notes in this skill.

The library is a mix of:

* thin SWI wrappers
* small stateful helper layers built on top of the Wimp
* higher-level UI helpers such as dialogue boxes, text editing, and file transfer
* utility headers that are mostly constants, structure definitions, or macros

The implementation is old and not uniformly re-entrant. When a helper layer
stores global state, that is called out below.

## Core Wimp-facing headers

Read `wimp-ui.md` for these.

* `wimp.h`: C structure layouts and wrappers for core Wimp SWIs.
* `wimpt.h`: task-startup and poll-loop helper layer around `Wimp_Initialise`,
  `Wimp_Poll`, mode tracking, and error reporting.
* `win.h`: dispatch table for window-specific event handlers plus unknown-event
  and idle-event claimers.
* `event.h`: top-level event loop and menu attachment helpers built on
  `wimpt` and `win`.
* `template.h`: in-memory template cache. Loads the application `Templates`
  resource and keeps each template's indirected workspace alive.
* `menu.h`: menu builder from compact description strings, with helpers for
  writable and sprite entries.
* `dbox.h`: dialogue-box abstraction on top of templates and Wimp windows.
* `help.h`: interactive-help message helpers.
* `saveas.h`, `xfersend.h`, `xferrecv.h`, `fileicon.h`: data-transfer and
  Save box helpers.
* `baricon.h`, `colourmenu.h`, `magnify.h`, `pointer.h`, `visdelay.h`:
  convenience UI helpers.
* `colourpick.h`: ColourPicker structures and constants only. This header
  describes block layouts and message IDs; it does not have matching wrapper
  functions in this source tree.

## Text-editing headers

Read `text-editing.md` for these.

* `txt.h`: editable/displayable text object with markers, selection, queue,
  and event callback support.
* `txtedit.h`: !Edit-style editor behaviour on top of `txt`.
* `txtwin.h`: management of the text window attached to a `txt`.
* `txtscrap.h`: selection ownership and scrap support for `txt`.
* `txtopt.h`: task-global option name for text/editor configuration.
* `akbd.h`: Wimp keyboard helper for SHIFT/CTRL/type-ahead polling.

## OS, resources, and utility headers

Read `system-graphics.md` for these.

* `os.h`: SWI invocation macros and wrappers for common OS calls.
* `res.h`: resource-file naming and opening relative to the application.
* `msgs.h`, `msgtrans.h`: messages-file lookup helpers and direct MessageTrans
  macros.
* `flex.h`, `heap.h`: movable-block and heap-on-flex allocation helpers.
* `alarm.h`: alarm queue driven by null events / `wimp_pollidle`.
* `ctl.h`: command/menu binding helper layer.
* `werr.h`: Wimp error-box reporting.
* `trace.h`: trace macros that compile away unless `TRACE` is enabled.
* `typdat.h`: filetype/load-exec pair structure.

## Graphics, font, sprite, draw, and printing headers

Read `system-graphics.md` for these as well.

* `bbc.h`: BBC BASIC style text, graphics, palette, and sound wrappers.
* `coords.h`: work-area/screen coordinate conversion.
* `colourtran.h`: ColourTrans conversion wrappers between palette words,
  colour numbers, and GCOL values.
* `font.h`: Font Manager wrappers and related structures.
* `sprite.h`: SpriteOp wrappers, sprite-area structures, and plotting helpers.
* `dragasprit.h`: DragASprite start/stop wrappers.
* `print.h`: Printer driver wrappers and page/rectangle structures.
* `drawftypes.h`, `drawferror.h`, `drawmod.h`, `drawfdiag.h`, `drawfobj.h`:
  Draw-file structure definitions and helper layers.
* `resspr.h`: access to the application's loaded resource sprite area.

## Important library-wide caveats

* Many helpers are stateful singletons. They are convenient, but not isolated.
* Some headers are more ambitious than the implementation quality justifies.
  Prefer the simplest layer that solves the task.
* Template and menu backing storage must stay valid while the Wimp may still
  reference it.
* Several helpers assume conventional application resources:
  `Templates`, `Messages`, and sprites in the resource sprite area.
* Some convenience wrappers are materially less flexible than the raw SWIs.
  If the helper hard-codes naming or lookup behaviour, switch to the lower
  level Wimp or OS wrapper.

## Notable implementation caveats

* `baricon.h` is effectively single-instance despite the interface shape:
  the implementation keeps one global click callback and one global icon block,
  so later calls overwrite earlier bar-icon state.
* `template_init()` always resolves and loads the `Templates` resource via
  `res_findname("Templates", ...)`.
* `msgs_lookup()` falls back to the library-default messages file and then, if
  no token is found, to the text after `:` in the lookup string.
* `res_openfile()` tries a country-specific resource filename first when
  opening for read.
* `wimpt_init()` chooses a default Wimp version based on whether you supplied
  a message list, and it installs exit/signal handlers.
