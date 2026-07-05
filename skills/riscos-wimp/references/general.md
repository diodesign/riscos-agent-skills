# General Wimp Rules

Use this file when the task touches Wimp structures or the event loop but is not yet narrowed to one area.

## Core principles

* The Wimp is protocol-heavy. Small call-contract mistakes often look like unrelated UI bugs.
* Different Wimp SWIs use different calling styles:
  * some take `R1 -> block`
  * some take raw registers
  * some mix both
* Many Wimp calls preserve parts of the block and fill other parts in. Do not assume a call leaves the whole block untouched or rewrites all of it.
* Preserve the distinction between:
  * window handles
  * icon handles
  * menu pointers
  * task handles
  * protocol instance handles that are not Wimp handles at all

Treat returned handles as opaque 32-bit values. Keep signed values only where the API genuinely uses negative sentinels such as `-1`, `-2`, or `-8`.

## Event-loop invariants

* `Wimp_Poll` or `Wimp_PollIdle` drives the task.
* Some returned events require an immediate protocol response:
  * redraw requests
  * open window requests
  * close window requests
  * menu warnings
* Do not perform unrelated Wimp operations between a protocol event and the SWI that satisfies it.
* Event numbers are part of the protocol surface. Keep the poll loop readable enough that you can compare event flow against the PRM and any original implementation.
* If the task has dependent panes, toolboxes, or other follower windows, first
  satisfy the main window's open request, then query fresh state and reposition
  the dependants from that updated state. Do not calculate follower geometry
  from stale pre-open coordinates.

## Structure layout discipline

* Use the active exported header definitions instead of reconstructed ad hoc structs.
* Be careful when porting from assembler:
  * old code may use offsets into packed Wimp blocks
  * the C translation must match the real structure layout, not the comment summary

## Diagnostics

When behaviour is wrong:

1. Log the event stream from the poll loop.
2. Log the key handles returned by `Wimp_CreateWindow`, `Wimp_CreateIcon`, and `Wimp_Initialise`.
3. Log the window or icon flags being handed to the Wimp before creation.
4. Check whether corruption appears before creation, at creation, or after later state updates.

When a menu, dialogue, or pane behaves differently on the first open versus an
Adjust reopen, also log whether the code is rebuilding the same logical object
or re-picking a fresh one from the current pointer position.
