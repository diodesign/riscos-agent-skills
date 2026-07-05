# Application structure

Use this reference for the overall structure of a small desktop application
rather than for the raw Wimp protocol details. For the protocol itself, also
use the `riscos-wimp` skill.

## Basic split

Keep the application split into distinct layers:

* startup and shutdown plumbing
* event-loop plumbing
* business logic for user actions
* narrow SWI wrappers for Wimp and OS calls

This keeps `_swix` and raw block handling out of the higher-level application
logic and makes it easier to test or replace the logic later.

## Event handling structure

Dispatch the poll loop in stages:

1. read the event
2. identify the source window and icon
3. decode the button or message semantics
4. hand off to a small action-specific helper

Do not jump directly from a raw poll block to application behaviour when the
application is expected to grow beyond one icon or one window.

## Filtering discipline

When responding to user interaction, filter as narrowly as practical:

* for iconbar actions, check both window handle `-2` and the icon handle
* for window actions, check both the window handle and the icon handle
* treat the button meaning as a separate dimension from the source

This avoids accidental cross-talk once extra windows, menus, or icons are
added.

## Application slot sizing

For packaged Wimp applications, keep the `Resources/!Run` slot allocation in
step with the built absolute:

* after creating the application and after later feature changes, check the
  size of the built `!RunImage` absolute
* add 32K headroom to the binary size, then round the result up to a whole 4K
  page size for `WimpSlot -min`
* never set `WimpSlot -min` below 32K, even for very small applications
* set `WimpSlot -max` to greater than or equal to the chosen minimum
* in normal maintenance, keep `-max` tracking `-min` unless there is a clear
  reason to reserve extra headroom

Do not leave the skeleton `32K` slot values in place once the application is
large enough to exceed them.
