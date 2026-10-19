# Redraw And Open Protocol

Use this file for runtime window protocol handling:

* `Redraw_Window_Request`
* `Open_Window_Request`
* redraw and update rectangle loops
* text rendering in redraw loops (Font Manager, Wimp_PlotIcon, VDU 5)
* `Wimp_GetWindowOutline`
* `Wimp_ForceRedraw`

## Open-window requests

When the Wimp returns an open-window request:

* satisfy it through the documented open-window path
* do not treat it as a generic application event
* preserve the requested visible area, scroll offsets, and stacking semantics unless the task has a specific reason to adjust them

## Redraw requests

If the Wimp returns a redraw request, treat that as a protocol event.

For auto-redraw windows, first confirm whether redraw requests should be happening at all:

* compare template flags with the original implementation
* check whether memory corruption or incorrect creation flags have changed the window behaviour
* check whether the window block handed to `Wimp_CreateWindow` still matches the template-loaded flags and layout

If redraw requests are expected for the task, complete the `Wimp_RedrawWindow` / `Wimp_GetRectangle` protocol in the documented order.

The important sequencing rule from the PRM is:

* `Wimp_RedrawWindow` must be the first Wimp operation after the poll returns a redraw request

## Update loops

When the task is using explicit update/redraw loops:

* treat the returned rectangle set as authoritative
* keep drawing bounded to the current clip rectangle
* do not mix unrelated Wimp activity into the middle of the redraw or update cycle

## Window outlines

`Wimp_GetWindowOutline` is useful when invalidating a title area or another screen-space region tied to a window frame rather than its work area.

Check which coordinate space the next call expects before using the returned outline values directly.

A common case is title or furniture redraw after changing metadata such as the
window title. Read the outline in screen coordinates, then force the redraw in
screen coordinates rather than trying to express the frame area relative to the
work-area origin.

## Force redraw

Check the SWI contract before using `Wimp_ForceRedraw`. It takes raw register coordinates, not a `R1 -> block`.

* if `R0 = -1`, the redraw area is in screen coordinates
* if `R0` is a window handle, the redraw area is relative to the work area origin

## Rendering text in redraw loops

When drawing text inside a `Wimp_RedrawWindow` or `Wimp_UpdateWindow` loop, strive to use the desktop antialiased font system instead of raw `VDU 5` system text.

### Option 1: Wimp_PlotIcon (Recommended for UI text, labels, and panels)

For buttons, status labels, score readouts, or fixed panels, the cleanest method is `Wimp_PlotIcon` (`wimp_plot_icon`):
* Construct a transient `wimp_icon` block with `wimp_ICON_TEXT` (and optional `wimp_ICON_BORDER`, `wimp_ICON_FILLED`, `wimp_ICON_VCENTRED`, etc.).
* Call `wimp_plot_icon(&icon)`.
* **Advantages**: Automatically renders using the configured desktop outline font (`Homerton.Medium`), respects desktop colours and 3D borders, and clips to the icon box without manual font handle tracking.
* **Coordinate convention**: When called inside a `Wimp_RedrawWindow` or `Wimp_UpdateWindow` loop, the icon bounding box must contain **window-relative (work area) coordinates** (e.g. `0` to `WINDOW_WIDTH`, `-WINDOW_HEIGHT` to `0`), **not screen coordinates** (`ox + x`). Adding screen offsets (`ox, oy`) causes the icon to be placed far outside the clip rectangle so nothing renders.
* **3D Borders and validation**: When applying 3D border validation strings like `"R5"` (sunken display field) or `"R2"` (action button), ensure `wimp_ICON_BORDER` is set in `icon.flags` alongside `wimp_ICON_INDIRECTED`.

### Option 2: Font Manager Direct Paint (For canvas graphics, code, and tabular data)

When plotting text directly to the graphics canvas:
1. **Startup**: Cache font handles using `Font_FindFont` (`font_find_font`):
   * Proportional text: `"Homerton.Medium"` at 12pt (`12 * 16 = 192`).
   * Monospaced/code/hex text: `"Corpus.Medium"` at 10pt (`160`) or 12pt (`192`).
2. **Redraw loop**:
   * Set colours using `ColourTrans_SetFontColours` (`colourtrans_set_font_colours`) to enable anti-aliasing against the window background (passing a non-zero font handle in `R0` also selects that font as current).
   * Paint text using `Font_Paint` (`font_paint`) with bit 4 set (`font_OS_UNITS`, coordinates in OS units) and bit 8 set (`font_GIVEN_FONT`) if passing a font handle in `R0` to override the current font.
   * **Coordinate convention**: Unlike `Wimp_PlotIcon`, `Font_Paint` ignores VDU origins and takes **absolute screen coordinates** (`ox + x`, `oy + y`) for the **baseline** of the text (descenders hang below the baseline).
3. **Shutdown**: Release handles with `Font_LoseFont` (`font_lose_font` / `xfont_lose_font`).

### VDU 5 Caveats (Legacy Fallback Only)

If `VDU 5` must be used for retro 8-bit styling or quick debugging:
* `VDU 5` renders an archaic 8×8 teletext bitmap font without anti-aliasing.
* **Top-left coordinate convention**: In `VDU 5` mode, coordinates specify the **top-left** of the character cell (drawn downwards). Plotting text at the bottom of a row (`y_bot`) will cause characters to hang below the line and clip or corrupt the row below. Text baseline must be offset downward by `32` OS units (in mode 27/28).

## Diagnostics

When a task hangs in the poll loop:

1. log the event sequence
2. check whether redraw or open requests are repeating
3. confirm whether the task is failing to satisfy the Wimp protocol, or whether it is receiving requests that should never have been generated in the first place
