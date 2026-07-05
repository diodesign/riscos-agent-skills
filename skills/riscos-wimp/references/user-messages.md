# User Messages

Use this file for Wimp user messages outside the standard file-transfer paths.

## Scope

This is for messages such as:

* `HelpReply`
* filer-facing messages such as open-directory or share requests
* browser plug-in messages such as `Message_PlugIn_Open`, `Message_PlugIn_Reshape`, `Message_PlugIn_Focus`, `Message_PlugIn_Status`, and stream-control messages
* `AppControl`
* task close-down tracking

Read `references/data-transfer.md` instead when the path is specifically about `DataLoad`, `DataSave`, or scrap-file transfers.
Read `references/colour-picker.md` as well when the task handles `&47700` to `&47704` ColourPicker messages.

## Message construction

When constructing a Wimp message:

* fill in the message-specific payload first
* compute `hdr.size` from the fixed header plus the live payload length
* round the size up to a word boundary
* set `your_ref` deliberately rather than leaving stale data in place
* choose the target task explicitly

Do not assume a fixed whole-structure size is always correct. Many Wimp messages have a variable-length tail such as a pathname or returned text.

For browser plug-in messages, also check whether any payload fields are `string_value`s rather than inline text. Those can be message-body offsets or shared-memory pointers, and the ownership rules differ from ordinary fixed-tail Wimp messages.

## Help replies

For `HelpReply`:

* copy the looked-up text into the reply buffer
* set `your_ref` from the original message's `my_ref`
* send the reply back to the original sender

If the help text is token-derived, keep the token-generation path deterministic so that help debugging is reproducible.

## Filer and broadcast-style messages

Some Wimp messages are normally sent either to a specific task or broadcast:

* send to a known task handle when the recipient is explicit
* use the documented broadcast behaviour only when the protocol expects it

Plug-in protocol traffic is especially sensitive to this distinction:

* open discovery is broadcast
* most other plug-in messages are direct task-to-task messages
* focus, reshape, close, status, URL access, and stream control should not be broadcast unless the protocol explicitly says so

If a message opens a directory, shares an object, or asks another application to reveal UI, validate the target and payload before sending the message so that failures remain local to that path.

When a protocol defines both task handles and opaque instance handles, keep both. The task handle tells you where to send the message; the instance handle tells the peer which object or stream is being discussed.

## AppControl

`AppControl` is useful when a task should ask another task to reveal or reopen itself rather than starting a second copy.

When using it:

* confirm that the stored task handle still refers to the intended task
* send the appropriate reason code rather than assuming "open" is always right
* clear or refresh remembered task handles when close-down messages arrive
