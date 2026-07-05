# TaskWindow Protocol

Use this file when a Wimp task launches, tracks, or communicates with a TaskWindow child task.

Public references:

* TaskWindow PRM chapter: `https://www.riscos.com/support/developers/prm/taskwindow.html`
* Wimp PRM chapter, TaskWindow messages section: `https://www.riscos.com/support/developers/prm/wimp.html#54184`

## Scope

This is for cases where a Wimp task:

* starts a TaskWindow helper with `Wimp_StartTask`
* receives TaskWindow-specific Wimp messages
* consumes helper output as either line-oriented text or raw data
* needs to detect both orderly helper exit and unexpected helper death

Treat this as a child-task message protocol layered on top of ordinary Wimp message handling.

## Startup interfaces

TaskWindow integration is normally started through `*TaskWindow`, invoked from a Wimp task via `Wimp_StartTask` or `*WimpTask`, not through `OS_CLI`.

The common direct-parent form uses:

* `-task &xxxxxxxx` to identify the owning Wimp task
* `-txt &xxxxxxxx` to provide a parent-defined correlation or identity value

That is the pattern to use when your Wimp task intends to own and track the TaskWindow explicitly.

If `-task` and `-txt` are omitted, TaskWindow uses a different discovery path:

* it broadcasts `TaskWindow_NewTask`
* another application may acknowledge the broadcast and start the child on behalf of the request

This is a different protocol shape. Do not mix the direct-parent and broadcast-provider models casually inside one design.

## Core model

Keep these concepts distinct:

* owning Wimp task
* TaskWindow slot or logical handle in your code
* TaskWindow task handle returned later by the protocol
* startup correlation token or identifier
* optional cooked-output buffer
* document or view object associated with that TaskWindow

Do not assume the task handle is known at launch time. A TaskWindow often starts asynchronously, so startup correlation needs an explicit identifier.

## Message set

The common TaskWindow messages are:

* input
* output
* startup or ego notification
* clean close notification
* forced close request
* suspend
* resume

In addition, the owner should usually watch `Message_Task_CloseDown` for the helper task so that unexpected termination is handled separately from the normal TaskWindow close message.

If the code may also run inside a task window itself, `TaskWindow_TaskInfo` can be used to ask the TaskWindow module whether the calling task is running in a task window.

## Startup matching

A robust startup path usually:

1. allocates a local TaskWindow slot
2. records the callback base, private state, and startup correlation id
3. launches `TaskWindow ... -task &<owner-task> -txt &<correlation-id>`
4. waits for the TaskWindow startup message
5. records the real helper task handle when the correlation id matches

That correlation step matters. Matching only on task name or launch order is fragile when multiple TaskWindows may be starting at once.

If the design instead relies on the broadcast-provider path, make that explicit in the code and documentation. In that model, the owner is no longer just matching a child it launched directly; it is participating in a looser task-discovery workflow.

## Output handling

TaskWindow output is commonly consumed in one of two modes:

* cooked output
  * buffer bytes until newline
  * emit line-level callbacks or events
  * optionally strip carriage return and destructive editing characters
* raw output
  * pass each block through unchanged

Choose deliberately which one the caller needs.

Cooked mode is often useful for:

* progress reporting
* parsing tagged status lines
* per-document console views

Raw mode is better when:

* output length or structure matters exactly
* binary-safe handling is needed
* line editing characters should not be interpreted

## Buffered final output

If cooked mode is used, the helper may terminate with data still buffered but not newline-terminated.

On clean or unexpected termination:

* flush any buffered partial line through the same cooked-output path
* decide whether the synthetic final line should be marked as terminated
* free the cooked buffer only after the caller has received the last output

Dropping the trailing partial line is a common bug in TaskWindow integrations.

## Sending input

When sending input to a TaskWindow:

* keep message payload lengths bounded
* split long strings into manageable chunks if needed
* make the caller responsible for explicit line termination rather than assuming every send is a complete command

This keeps protocol and command semantics separate.

## Clean exit versus unexpected death

Differentiate these paths:

* helper sent its normal close message
* helper task died and only `Message_Task_CloseDown` was observed
* owner explicitly sent a terminate request

The caller often needs to know which happened.

Useful pattern:

* report a clean close reason separately from forced termination
* mark the slot inactive exactly once
* forget the task handle as soon as shutdown handling begins

## Suspend and resume

If the integration exposes suspend and resume:

* treat them as advisory control messages to the helper task
* keep the local state explicit so the UI knows whether a helper is meant to be paused
* do not infer that suspend or resume succeeded merely because the message was sent

## Per-document consoles

When a helper task exists to serve one document or one embedded object, it is often better to keep one output console or display per logical document rather than one global console.

Benefits:

* output remains attributable to the right document
* copy and inspection of logs is simpler
* shutdown of one document does not destroy the output history of another

This is a design rule, not a protocol requirement, but it usually leads to clearer Wimp behaviour.

## Review traps

Look for these problems first:

* startup code assumes `Wimp_StartTask` returned the final helper task handle
* output parsing ignores the last partial line on termination
* helper task handles are not cleared on `Message_Task_CloseDown`
* one callback path handles normal TaskWindow close but another path forgets unexpected termination
* helper output is stored in global buffers without identifying which document or window it belongs to
