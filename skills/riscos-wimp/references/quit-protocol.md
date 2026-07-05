# Quit And PreQuit Protocol

Use this file when a Wimp task can be exited from its own UI, from the Task Manager, or as part of desktop shutdown.

## Core rule

Treat the two quit-stage messages differently:

* `Message_PreQuit (8)` is the point where the task may object, usually because it has unsaved work or live state that the user must confirm.
* `Message_Quit (0)` is final. Do not ignore it, defer it, or try to object there. Tidy up and terminate.

## What to check on `Message_PreQuit`

Check only the state that can justify delaying shutdown:

* unsaved document changes
* pending transfers or network sessions that the user should explicitly abandon
* temporary state that must be offered for saving before exit

Do not acknowledge `Message_PreQuit` just because the task is busy. If the task is happy to terminate, ignore the message and let the close-down continue.

## How to stop close-down continuing

To object to `Message_PreQuit`:

1. Keep the poll block exactly as returned by `Wimp_Poll`.
2. Copy `my_ref` to `your_ref` by writing `poll_block!12 = poll_block!8`.
3. Send the same block back with `Wimp_SendMessage` and `User_Message_Acknowledge (19)`.

That acknowledgement stops the normal Task Manager sequence. The sender field of the original `Message_PreQuit` identifies the task that must receive any restart request later.

## How to prompt the user

After acknowledging `Message_PreQuit`, present a confirmation or save/discard flow immediately.

The prompt should answer whether the task may really exit, for example:

* save changes, then continue exit
* discard changes or abandon connections, then continue exit
* cancel and keep the task running

Keep enough state from the original `Message_PreQuit` to finish correctly afterwards:

* the sender task handle from the message
* whether the request was a desktop shutdown or only this task being asked to quit

## Knowing when it is not a desktop shutdown

Inspect the `Message_PreQuit` flag word at `poll_block!20`:

* bit 0 clear: desktop shutdown is in progress
* bit 0 set: only this task is being asked to quit

Ignore the remaining bits.

On older systems that do not provide the flag word distinction, treat the request conservatively if compatibility matters.

## How to restart desktop shutdown

If the user confirms exit after objecting to a desktop shutdown:

1. Call `Wimp_GetCaretPosition` to obtain a message block.
2. Set `block!24 = &1FC` for the `Ctrl-Shift-F12` key-pressed event.
3. Send that block with `Wimp_SendMessage` action `Message_PreQuit (8)` to the sender task recorded from the original `Message_PreQuit`.

This restarts the Task Manager close-down sequence.

If bit 0 of the original flag word was set, do not restart desktop shutdown. Just close this task normally, because the request was only for this task.

## Handling `Message_Quit`

When `Message_Quit` arrives:

* stop accepting that the task can remain open
* close files, windows, sessions, and other owned resources
* call `Wimp_CloseDown`
* terminate the task

Any user confirmation must already have happened during `Message_PreQuit`.

## Practical pattern

A robust application-level pattern is:

1. On `Message_PreQuit`, inspect dirty or live state.
2. If no objection exists, ignore the message.
3. If objection exists, acknowledge it, cache sender plus flag word, and open a prompt.
4. If the user cancels, dismiss the prompt and keep running.
5. If the user confirms and the original request was desktop shutdown, send the restart key event.
6. If the user confirms and the original request was task-only quit, close the task directly.
7. On `Message_Quit`, always terminate promptly.

## Example pattern seen in practice

JFTerm follows the intended structure:

* on `Message_PreQuit`, it checks whether live connections remain
* if so, it acknowledges the message, records whether bit 0 says "quit only this task", and opens a confirmation dialogue
* if the user confirms a desktop shutdown, it issues the `Ctrl-Shift-F12` restart event to the original sender
* if the request was task-only quit, it exits without trying to restart desktop shutdown

## Reference source

Primary source: `https://www.riscos.com/support/developers/prm/wimp.html`, especially the `Message_PreQuit (8)` and `Message_Quit (0)` sections.
