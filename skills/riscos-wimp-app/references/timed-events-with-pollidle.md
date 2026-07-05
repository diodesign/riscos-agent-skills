# Timed events with `Wimp_PollIdle`

Use this pattern when a desktop application must perform regular background
work without blocking the Wimp event loop.

Typical cases:

* animation or blinking state
* periodic status-field refresh
* deferred UI updates
* polling a network or device interface from the foreground task
* short shutdown or progress sequences driven by timed callbacks

## Core pattern

Keep a timer queue in application state. Each timer stores:

* callback function
* private closure value
* due time
* optional repeat delay

The main loop then works in two modes:

1. If no timer is pending, call `Wimp_Poll`.
2. If a timer is pending, call `Wimp_PollIdle` with the next timer deadline.

When `Wimp_PollIdle` returns a null event, run the timeout dispatcher and
invoke every callback now due.

This keeps the task responsive to ordinary Wimp events while still waking at a
known time for background work.

## Structure to reproduce

Split the implementation into three pieces:

1. Timer registration helpers such as "set once", "set every", "clear", and
   "next timeout".
2. Poll-loop plumbing that chooses between `Wimp_Poll` and `Wimp_PollIdle`.
3. Small callbacks that update application state and return quickly.

The callback should usually change state, queue follow-up work, or trigger a
redraw. Avoid long-running work in the callback itself because it executes on
the single Wimp thread.

## Deadline handling

If your timer queue stores the same timebase that `Wimp_PollIdle` expects,
pass the next due time straight through.

If your queue stores a different timebase, convert it before calling
`Wimp_PollIdle`. One practical example is a helper library that schedules with
`clock()` values but must pass a monotonic timestamp to `Wimp_PollIdle`; in
that case, read `OS_ReadMonotonicTime` and translate the next due time before
the idle poll.

## Event-loop usage

The usual flow is:

1. Initialise Wimp.
2. Register any repeating timers needed during normal operation.
3. Enter the poll loop.
4. Read the next due timeout from the timer queue.
5. Call `Wimp_Poll` if there is no timeout, otherwise call `Wimp_PollIdle`.
6. On a null poll, trigger due timeouts.
7. On quit or mode change, clear or replace timers as needed.

Do not spin in a manual delay loop, and do not call the timeout dispatcher on
every iteration if you can sleep until the next due event.

## Shutdown and mode changes

Treat timer handles as owned resources:

* clear repeating timers when the feature they drive is no longer active
* replace one timer sequence with another when application state changes
* ensure quit handling cannot leave stale repeating callbacks registered

For example, an application may stop a normal repeating "tick" timer when it
receives a quit request and then start a short repeating shutdown timer to run
the final sequence.

## Example repository

The repository <https://github.com/gerph/riscos-timed-events-example> shows
this pattern in both forms:

* a small timeout library with queue, repeat, clear, and dispatch helpers
* a CLI example that calls the dispatcher explicitly from its own work loop
* a desktop Wimp example that uses `TO_NextTimeout()`, `Wimp_PollIdle`, and
  null-poll handling to drive timed callbacks

Use it as a worked example of integrating regular callbacks into a RISC OS
desktop application's main loop.
