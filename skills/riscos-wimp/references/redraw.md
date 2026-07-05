# Redraw And Open Protocol

Use this file for runtime window protocol handling:

* `Redraw_Window_Request`
* `Open_Window_Request`
* redraw and update rectangle loops
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

## Diagnostics

When a task hangs in the poll loop:

1. log the event sequence
2. check whether redraw or open requests are repeating
3. confirm whether the task is failing to satisfy the Wimp protocol, or whether it is receiving requests that should never have been generated in the first place
