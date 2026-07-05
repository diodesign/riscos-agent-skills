# External Edit Protocol

Use this file when a Wimp task implements either side of the External Edit
protocol:

* a client that asks another task to edit, display, or play some data
* an editor that accepts an external edit request and later returns data

Treat ExtEdit as a Wimp message protocol layered on top of the ordinary
RISC OS data-transfer messages. Read `references/user-messages.md` and
`references/data-transfer.md` alongside this file.

## Core model

An ExtEdit session is a task-to-task relationship identified by a 32-bit
job handle:

* low 16 bits chosen by the client
* high 16 bits chosen by the editor
* both halves non-zero
* never changed once the session is established

Keep per-session state keyed by the full 32-bit handle, not just one half.
If the implementation uses a local array slot or index inside its own 16-bit
half, still validate the full 32-bit handle before acting on a message.

The protocol normally involves:

1. discovery by broadcast
2. acknowledgement by direct reply
3. one or more normal data transfers scoped by the ExtEdit job handle
4. optional cursor or selection updates
5. either return of edited data or explicit abort

## Message set

The six core Wimp messages are:

* `Message_EditRq` (`&45D80`): client broadcasts a request for an editor
* `Message_EditAck` (`&45D81`): editor claims the request
* `Message_EditReturn` (`&45D82`): client asks for the current data back
* `Message_EditAbort` (`&45D83`): either side terminates the session
* `Message_EditDataSave` (`&45D84`): either side starts a normal data transfer
* `Message_EditCursor` (`&45D85`): client sets or reads cursor and selection state

The names above are Wimp message names, not function names. For PRMinXML
message definitions and message references, omit the `Message_` prefix from
the XML `name` attribute.

Register only the ExtEdit messages the task actually handles in its
`Wimp_Initialise` message list. A pure editor may only need
`Message_EditRq`, `Message_EditDataSave`, `Message_EditReturn`, and
`Message_EditAbort`.

## Shared fields and flags

Most ExtEdit messages carry:

* a 32-bit data type word
* a 32-bit job handle
* a 32-bit flag word

The data type word is not just the base RISC OS file type. The low 16 bits are
the file type, and the high 16 bits are an extension that distinguishes more
specific data formats when required.

Common flag bits:

* bit 0: Continue editing after return
* bit 1: Selection only
* bit 2: Read-only
* bit 3: Immediate execution or playback
* bit 4: Adjust selection

Unsupported flags should normally be ignored, but preserved or reflected where
the protocol requires the receiver to report current state back to the sender.

## Client workflow

The normal client-side flow is:

1. Broadcast `Message_EditRq` with the desired data type, low 16 bits of the
   job handle filled in, and the initial flags.
2. If an editor accepts, record the replying task handle, the full returned job
   handle, and the status flags from `Message_EditAck`.
3. If initial data should be inserted, send `Message_EditDataSave` directly to
   that editor task and then follow the normal `DataSave` / `RAMTransmit`
   protocol.
4. If cursor or selection state matters, send `Message_EditCursor`.
5. When the user asks for the data back, send `Message_EditReturn`.
6. Accept the editor's `Message_EditDataSave` reply path and complete the
   normal data-transfer protocol.
7. If the session must be abandoned, send `Message_EditAbort`.

Guidance:

* do not treat the broadcast reply as proof that the returned editing mode is
  acceptable; inspect the flags from `Message_EditAck`
* keep the remote task handle and the ExtEdit job handle as separate state
* treat externally edited data as modified data in the client document model
* if no editor replies, the fallback path may involve launching an editor and
  retrying, but that is outside the Wimp message mechanics themselves

## Editor workflow

The normal editor-side flow is:

1. Receive broadcast `Message_EditRq`.
2. Decide whether the task can handle the data type and requested mode.
3. Open a blank editing or playback context.
4. Reply with `Message_EditAck`, filling in the high 16 bits of the job handle.
5. Accept any later `Message_EditDataSave` from the client and insert the
   transferred data into the current editing context.
6. Accept `Message_EditCursor` if the data type has a meaningful cursor or
   selection model.
7. When the client sends `Message_EditReturn`, or when the user explicitly
   saves or closes, send `Message_EditDataSave` back to the client and perform
   the normal data-transfer sequence.
8. On close, fatal error, or user discard, send or honour `Message_EditAbort`.

Guidance:

* only claim requests the task can actually satisfy
* if the task is effectively read-only, only claim writable requests when the
  protocol and UI truly support them
* keep session state alive until any active transfer has completed or failed
* if immediate playback is supported, make its state changes explicit rather
  than mixing them into ordinary edit-window lifetime
* many real editors also gate acceptance on current document state, for
  example refusing a new ExtEdit request while another ExtEdit session is
  active, while the current document is already modified, or while the editor
  is not in a blank initial state

## `Message_EditRq` and `Message_EditAck`

`Message_EditRq` is always broadcast by the client.

The editor should inspect:

* extended data type
* read-only flag
* immediate execution flag
* suggested parent name and leafname

`Message_EditAck` is sent directly back to the requesting task. The reply must
quote the client's low 16-bit handle value and add the editor's own high
16-bit value.

Treat the reply flags as the editor's accepted session mode, not as a blind
echo of the request. Real editors may preserve supported bits while clearing
requested modes they do not implement, such as writable or immediate-execute
behaviour.

Do not re-use old session handles casually. A late or misdirected message from
an earlier session should fail the full-handle check rather than hitting a new
session by accident.

One practical handle-generation pattern seen in existing code is:

* store a persistent high-order sequence number in a system variable
* combine that sequence with a small in-task slot number
* use the result as the local 16-bit half of the ExtEdit handle

That is not required by the protocol, but it is a reasonable way to reduce the
chance of stale-session collisions across task restarts.

Another practical pattern is to seed the local 16-bit half from monotonic time
on first use and then increment it for each new session, skipping zero. The
important rule is not the source of uniqueness, but that stale messages should
not accidentally match a newly-created session.

## `Message_EditDataSave` and ordinary transfers

`Message_EditDataSave` is the ExtEdit equivalent of `Message_DataSave`.

Important rule:

* the initial ExtEdit message carries the job handle where `Message_DataSave`
  would normally carry the destination window handle
* all follow-up transfers are the normal RISC OS transfer messages

So the implementation needs two layers:

* ExtEdit session tracking
* standard `DataSave`, `DataLoad`, `RAMFetch`, `RAMTransmit`, and scrap-file
  handling

Do not invent a second payload transfer protocol. Reuse the task's existing
data-transfer implementation where possible.

Because the subsequent messages are normal transfer messages, keep clear which
state is keyed by:

* ExtEdit job handle
* transfer reference number
* remote task handle

That distinction matters when more than one ExtEdit session or more than one
outstanding transfer is active.

Existing editors often reuse their ordinary `DataSave` sender and receiver
paths almost unchanged:

* on incoming `Message_EditDataSave`, rewrite the proposed filename to
  `<Wimp$Scrap>` or another controlled temporary path, send a normal
  `DataSaveAck`, then wait for the ordinary `DataLoad`
* on outgoing `Message_EditDataSave`, remember the returned `my_ref`, wait for
  `DataSaveAck`, write the file to the acknowledged pathname, then send the
  normal `DataLoad`

That reuse is usually better than creating a parallel transfer implementation
just for ExtEdit.

If the task uses `<Wimp$Scrap>`, keep the transfer reference that owns the
scrap file and only delete the scrap file when the matching load or ack path
completes.

Track the transfer reference separately from the ExtEdit job handle. Existing
implementations commonly remember the `my_ref` created by the outgoing
`Message_EditDataSave` or `DataSaveAck`, then require the later `DataLoad` or
bounce to match that saved reference before treating it as belonging to the
session.

## `Message_EditReturn`

The client sends `Message_EditReturn` directly to the editor task when it wants
the current data back.

This message may request:

* a particular return data type
* selection only versus the whole object
* whether the session should continue after the return

If the editor cannot convert the data to the requested return type, it should
ignore the request rather than guessing silently. The client may retry with a
different type.

If servicing `Message_EditReturn` requires the task to recover data from helper
tasks, child editors, or other asynchronous sources, acknowledge the return
message first. Existing Wimp tasks do this specifically to avoid the sender
seeing a bounce while the editor enters a nested poll loop to recover the data.

For read-only sessions, do not build a writable return path accidentally just
because the editor has local data buffers.

If the editor already has a normal save box or save action, that UI may need
to route to the ExtEdit return path rather than writing a standalone file when
the current document is attached to an active ExtEdit session.

## `Message_EditCursor`

`Message_EditCursor` is a direct task-to-task message used to set or inspect:

* current cursor position
* selection start
* selection end
* current read-only or playback state

Special values:

* `-1` means "leave unchanged" for new values
* `-2` means "end of data"

The editor replies immediately with the previous or current positions.

Guidance:

* keep the unit of measurement explicit for each supported file type
* return `-1` in the old-value fields when the task cannot express the current
  selection as a single contiguous range
* do not poll this message aggressively as a general liveness or playback
  mechanism unless the protocol genuinely needs it

## Session closure and failure

Either side may send `Message_EditAbort`.

After abort:

* destroy or close any editing UI for that session
* stop playback started for that session
* drop the per-session state
* ignore later messages for that handle

Treat the sender as responsible for user-facing error reporting. The receiver
should clean up, not raise a second unrelated error dialogue.

Do not send abort before a valid session exists, and do not tear down the
session mid-transfer without understanding what the ordinary data-transfer path
will do next.

On task shutdown, walk every live ExtEdit session and send `Message_EditAbort`
to each peer before dropping the local session records. This avoids leaving the
other side believing the session is still active.

Also watch for `Message_TaskCloseDown` from the peer task. If the remote task
handle matches an active ExtEdit session, treat that as a dead peer, notify the
user if appropriate, and detach the session state so later messages for that
handle are ignored.

An implementation pattern from existing code is to defer final abort or window
closure until the ordinary return transfer has been acknowledged. For example:

* if `Message_EditReturn` or a save action starts an outgoing
  `Message_EditDataSave`
* and the Continue editing flag is clear
* mark the session as "abort after transfer"
* wait for the matching `DataLoadAck` or equivalent transfer-complete event
* only then close the editor window and drop the session state

That avoids tearing down the UI while the standard data-transfer protocol still
expects the task to complete the save/load exchange.

## Read-only and display-only editors

ExtEdit is not limited to writable editors. A task may accept a request simply
to display or play the data.

For display-only implementations:

* only claim requests that match the supported mode
* keep read-only state explicit in `Message_EditAck`
* do not accept save or return paths that imply modified data unless the task
  genuinely supports them

## UI integration patterns

Real editors often surface ExtEdit state in their ordinary UI:

* set the temporary document title to something derived from the parent task or
  document name and the supplied leafname
* route the save icon or RETURN in the save box to `Message_EditReturn` when
  the current document is an ExtEdit session
* keep the ordinary standalone save path for non-ExtEdit documents
* route both direct-save and save-box-triggered save operations through the
  same ExtEdit-aware helper so both paths use identical return-transfer logic

If the editor has a "blank document" concept, it may be simplest to accept an
ExtEdit request only when the current document is still blank and unmodified.

When the incoming transfer is a normal `DataLoad` that follows an earlier
ExtEdit `DataSave` or `EditDataSave`, acknowledge that `DataLoad` first if the
subsequent import path may run nested polling or other message-driven recovery.
That pattern avoids spurious bounces for the ordinary data-transfer phase in
the same way as the earlier `Message_EditReturn` acknowledgement rule.

## Review checklist

When reviewing ExtEdit code, check these first:

* client and editor halves of the job handle mixed up or truncated
* session lookup keyed only by local handle half
* broadcast used where a direct task-to-task message is required
* `Message_EditDataSave` treated as a wholly separate transfer protocol
* transfer state confused between job handle and `my_ref` or `your_ref`
* `Message_EditReturn` or follow-up `DataLoad` not acknowledged before code
  enters a nested poll loop, helper-task recovery path, or other delayed import
* read-only sessions that still allow modification or return changed data
* editor claims ExtEdit requests even though the current document state means
  it cannot safely replace or discard the local contents
* window close or save paths write standalone files instead of returning data
  through the active ExtEdit session
* session teardown happens before the outgoing return transfer has been
  acknowledged
* editor close paths that forget to return data, abort, or free per-session state
* stale session records left behind after failed transfers
* peer `Message_TaskCloseDown` ignored, leaving dead sessions associated with a
  vanished task
* cursor units undocumented or inconsistent across file types
