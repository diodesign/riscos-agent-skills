# Windows

Use this file for window creation, static layout, and basic open/close behaviour.

## Creating windows

* `Wimp_CreateWindow` takes `R1 -> window block`.
* The block must contain the exact flags and icon layout expected by the Wimp.
* If behaviour differs from an original implementation, log the flags just before creation.
* For new-format windows, use the active exported structure definitions. Incorrect field layout will often appear as later event-protocol failures rather than an immediate create-window error.

## Opening windows

* `Wimp_OpenWindow` updates the active window list.
* Be precise about the `behind` field:
  * `-1` top
  * `-2` bottom
  * other negative values are special in specific contexts
* For helpers that open one window behind another, calculate the visible area from the current window state rather than inventing fixed coordinates.

For applications with attached panes, toolboxes, or info windows:

* satisfy the main window's open request first
* then call `Wimp_GetWindowState` on the newly opened main window
* if frame-relative positioning matters, use `Wimp_GetWindowOutline` to derive
  border and title-bar geometry
* reopen each dependent pane from that fresh state, with explicit `behind`
  relationships between the main window and the follower windows

Do not position followers from stale pre-open coordinates. The Wimp may have
adjusted stacking or visible geometry while satisfying the original request.

Concrete recipe for reopening a main window with follower panes:

1. Receive `Open_Window_Request` for the main window.
2. Call `Wimp_OpenWindow` for that main window request first.
3. Call `Wimp_GetWindowState` for the now-open main window.
4. If the follower geometry depends on borders, title bar, or furniture,
   obtain the main window outline with `Wimp_GetWindowOutline`.
5. Compute each follower pane's visible box from the fresh main-window state
   and, where needed, the outline-derived border sizes.
6. Set each follower pane's `behind` field explicitly so the stacking order is
   deterministic relative to the main window and the other followers.
7. Call `Wimp_OpenWindow` for each follower pane using those recomputed boxes.

If the task is using nested child windows:

* be explicit about whether this call is the base form or the extended `"TASK"` form
* do not mix parent-relative child-window positioning logic with stale top-level coordinates
* if a child window may move between parents, re-open it using the current parent handle rather than assuming the original parent is still valid

## Close requests

When the Wimp issues a close-window request, reply with the proper close protocol rather than mutating state silently.

Read `references/redraw.md` for runtime redraw, update, and outline protocol details.
