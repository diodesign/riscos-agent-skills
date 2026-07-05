# Initialisation And Shutdown

Use this file for task startup and shutdown outside the module-service path.

## Startup

Typical task startup:

1. Build the message list for the messages the task wants.
2. Call `Wimp_Initialise` with the minimum Wimp version required by the task.
3. Record the returned task handle exactly as returned.
4. Open resources needed for the task.
5. Create icon bar icons, windows, and menus in a controlled order.
6. Enter the poll loop only after startup state is coherent.

`Wimp_Initialise` also returns the actual Wimp version. If the returned version is too old for the task, close down cleanly rather than continuing with partial assumptions.

## Message lists

The message list passed to `Wimp_Initialise` should contain only the messages the task expects to process. Terminate it with zero.

The message list is part of how the Wimp decides which messages to deliver. If a message path appears dead, confirm the message is actually listed at initialise time.

For browser plug-ins, this usually includes the relevant `Message_PlugIn_*` set and task close-down tracking. If the plug-in never receives its open or reshape traffic, check the initialise-time message list before debugging the higher-level protocol.

## Shutdown

Shutdown should happen in reverse order of ownership:

1. close Wimp task with `Wimp_CloseDown`
2. close message files and other resources
3. release module-area allocations or other workspaces
4. clear global state

When using `Wimp_CloseDown`, pass back the task handle and task identifier in the documented shape.

If shutdown can be called repeatedly after errors, make it idempotent.

## Error handling

If startup fails part-way through:

* do not continue into the poll loop
* release any successfully created resources
* report the startup failure once, not through repeated poll-loop errors
