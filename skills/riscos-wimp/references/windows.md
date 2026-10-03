# Windows

Use this file for window creation, static layout, and basic open/close behaviour.

## Creating windows

* `Wimp_CreateWindow` takes `R1 -> window block`.
* The block must contain the exact flags and icon layout expected by the Wimp.
* If behaviour differs from an original implementation, log the flags just before creation.
* For new-format windows, use the active exported structure definitions. Incorrect field layout will often appear as later event-protocol failures rather than an immediate create-window error.

### Window flags and furniture rules

* **Ordinary Application / Canvas Windows**: Must provide Moveable, Title, Close, and Back furniture:
  `wimp_WINDOW_MOVEABLE | wimp_WINDOW_TITLE_ICON | wimp_WINDOW_CLOSE_ICON | wimp_WINDOW_BACK_ICON | wimp_WINDOW_NEW_FORMAT`
* **Scrollable / Document Windows**: Additionally provide scroll bars, toggle, and size icons:
  `| wimp_WINDOW_TOGGLE_ICON | wimp_WINDOW_SIZE_ICON | wimp_WINDOW_VSCROLL | wimp_WINDOW_HSCROLL`
* **Back Icon Rule**: Any window with a close icon or title bar MUST have `wimp_WINDOW_BACK_ICON` (`&01000000`, bit 24) so the user can send the window to the bottom of the window stack without closing it.
* **Exceptions (No Back Icon)**: Only omit `wimp_WINDOW_BACK_ICON` for:
  1. Windows opened as submenus attached to menus (such as `ProgInfo`, `SaveAs`, colour pickers).
  2. Transient query or modal alert dialogues that lack standard title furniture.

### Work area extent and boundary calculation

* Base window dimensions on the maximum extent of content plus generous margins, not arbitrary small hardcoded values.
* When setting window `extent` `(xmin, ymin, xmax, ymax)`:
  * For custom-drawn windows (games, tools, graphics displays), compute `xmax` and `ymin` so that all elements, labels, and controls fit with at least `16` to `24` OS units padding inside the boundary.
  * Never place text labels flush against the right or bottom edges of the work area; text truncation or clipping at window edges is a severe desktop visual defect.

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
