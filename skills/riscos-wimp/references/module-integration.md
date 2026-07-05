# Module Integration

Use this file only when the Wimp is being driven from inside a module rather than from a normal application.

## Scope

This is for cases such as:

* `Service_StartWimp`
* `Service_StartedWimp`
* `Service_StartFiler`
* `Service_StartedFiler`
* `Service_FilerDying`
* `Service_Reset`
* `Desktop_...` command startup
* module-managed task lifetime
* pollword-driven deferred Wimp work

## Service_StartWimp

When a module wants the desktop to start its Wimp task:

* claim the service only when the module genuinely wants to start
* return the startup command string in the documented register
* do not overwrite unrelated private-word state just because the module is servicing StartWimp
* keep the StartWimp path and the module command path behaviourally aligned so desktop startup and manual startup do not diverge

## Task ownership

Keep the separation clear between:

* module global state
* task-running state
* deferred UI work such as pollword flags

Repeated startup and shutdown paths should be safe across reset and desktop restart cases.

## Filer-driven startup

Some desktop components are started through filer services rather than directly through `Service_StartWimp`.

When servicing filer startup:

* only claim the startup service when the module genuinely wants to create its desktop task
* record any filer task handle or caller state before returning the `Desktop_...` command
* keep an explicit intermediate state so that "startup requested" and "Wimp task fully running" are not conflated
* clear that intermediate state if the follow-up started-service indicates that startup did not complete

This avoids re-entrancy and duplicate-start bugs where the module thinks the task is already running when the desktop launch path never actually completed.

## Pollword work

Use pollword processing for deferred Wimp-safe work such as:

* mode refreshes
* title refreshes
* icon refreshes

Keep the pollword flags small and explicit. Process them in a deterministic order.

## Desktop commands

If the task is started from a `Desktop_...` command:

* make sure the command path and the StartWimp service path agree
* avoid two competing startup paths that both think they own task initialisation
* reject direct manual startup cleanly if the task is only valid through the desktop service path

## Close-down tracking

If the module talks to helper applications or child tasks:

* track their task handles separately from the module's own Wimp task handle
* handle task-close-down messages by forgetting stale helper-task handles
* use that state to avoid launching duplicate helpers when the original task is still alive

## Error reporting

In module-integrated Wimp code, repeated errors are especially damaging because they can trap the desktop in a loop. Prefer one-shot reporting plus a clean shutdown over letting the poll loop repeatedly hit the same fault.
