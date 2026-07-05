# Browser Plug-In Protocol

Use this file when a Wimp task is embedded inside a browser or another host through the Acorn plug-in protocol.

Public references:

* Plug-In Protocol functional specification: `https://gerph.github.io/riscos-prminxml-staging/prm/html/acorn/plugin_protocol/plug-in_protocol.html`
* Nested Window Manager functional specification: `https://gerph.github.io/riscos-prminxml-staging/prm/html/acorn/nested_window_manager/nested_window_manager.html`

## Scope

This is for plug-in tasks that:

* receive `Message_PlugIn_Open` and related messages
* create child windows inside a browser window
* exchange focus with the browser
* accept streamed data or request URL fetches through the browser
* parse the browser-provided parameter file for `OBJECT` and `PARAM` data

Treat this as a Wimp message protocol built on top of nested windows, not as a library callback API.

## Core model

The browser and the plug-in are separate tasks.

Keep these identities separate:

* browser task handle
* browser instance handle
* plug-in task handle
* plug-in instance handle
* browser stream handle
* plug-in stream handle

Do not collapse any of these into a single "handle" concept in code or reviews. Confusing them tends to break close-down, reshape, or stream teardown paths long after startup appears to work.

## Startup and message registration

Plug-in tasks should register only the `Message_PlugIn_*` messages they actually process, plus any close-down tracking they need.

If the embedded window depends on nested child-window behaviour, make sure the task initialises the Wimp at a version that enables the required nested-Wimp semantics, and reject older environments cleanly.

## Open and close lifecycle

The normal lifecycle is:

1. Browser broadcasts `Message_PlugIn_Open`.
2. Plug-in decides whether it will handle the object.
3. Plug-in replies with `Message_PlugIn_Opening` if it accepts.
4. Browser may then start initial data streaming.
5. Browser later sends `Message_PlugIn_Close` directly to the plug-in task.
6. Plug-in destroys its child window, releases state, and replies with `Message_PlugIn_Closed`.

Guidance:

* keep the acceptance decision separate from the later "opened" work
* destroy embedded windows before discarding the per-instance state they need
* honour the close protocol even if startup partly failed
* process task close-down messages from the browser as a separate path, because the host may die without sending the normal close message

## Embedded window ownership

The parent window belongs to the browser, not to the plug-in.

For embedded windows:

* treat the browser-supplied parent handle and work-area coordinates as authoritative
* expect reshape messages to move the child to a different parent window
* re-open the child window through the nested-Wimp form rather than trying to maintain parent-relative geometry manually
* do not assume the Wimp will send ordinary open-window requests when the parent scrolls; nested positioning is normally handled automatically

If the plug-in changes its preferred size, it should request a reshape from the browser rather than directly assuming it can resize the embedded region unilaterally.

Some plug-ins also switch the same logical view between standalone and embedded forms by recreating the window with different furniture flags. If so:

* keep the per-instance render state separate from the window definition
* preserve enough state to survive window recreation cleanly
* make the plug-in and standalone furniture choices explicit rather than leaving them as side effects of the current launch path

## Focus and input routing

Focus transfer is explicit in this protocol.

When the plug-in or browser wants the other side to take focus:

* send `Message_PlugIn_Focus` directly to the peer task
* acknowledge the message if focus is accepted
* ignore it if focus is refused

For key presses or mouse clicks that the plug-in does not handle itself:

* forward them to the browser as messages addressed to the browser task
* set the window field to the browser's parent window handle
* do not treat `Wimp_ProcessKey` as a substitute for returning input to the host in this embedded case

## Parameter files

The filename in `Message_PlugIn_Open` is not the media data itself. It is a browser-generated parameter file describing the embedded object.

Treat that file as the source of:

* `OBJECT` attributes
* enclosed `PARAM` values
* browser-generated special values such as `BASEHREF`, `USERAGENT`, `UAVERSION`, `APIVERSION`, and optional `BGCOLOR`

The file format is binary and record-based. Preserve that distinction in documentation and reviews; it is not just an HTML fragment written to disc.

Keep parameter parsing separate from UI creation so that malformed data can be rejected cleanly before the child window is fully established.

## String values and memory lifetime

Many plug-in-protocol strings are `string_value`s:

* small values may be stored inline as offsets within the message body
* larger values may be pointers to shared memory

Guidance:

* decode both forms explicitly
* ensure pointer-backed strings live until the message has either been replied to or bounced
* use null-terminated strings, not language-native terminators
* keep ownership tracking explicit so that stream teardown and instance close-down free the right allocations exactly once

## Streams and URL access

The protocol can deliver initial data, browser-fetched URLs, or plug-in initiated browser writes through the stream messages.

When reviewing or implementing stream handling:

* keep per-stream state separate from per-instance state
* treat `Message_PlugIn_Stream_New`, `Write`, `Written`, `Destroy`, `As_File`, and `Notify` as one linked protocol
* decide early whether the implementation supports progressive writes, file-only delivery, or both
* close and free stream state on every destroy or notify path, including error and user-abort cases

When asking the browser to fetch a URL:

* use `Message_PlugIn_URL_Access`
* request completion notification only when the result must be tracked
* expect browser implementations to vary slightly in edge cases, especially around notify data and partial stream features

The specification notes that some browsers do not implement every stream variant. Keep code defensive around optional POST and browser-window streaming cases.

For streamed image or document viewers, keep the render-state machine explicit. States such as fetching, showing, stopped, and failed often need different redraw behaviour even though the plug-in protocol messages are the same.

## Status, busy, action, and abort

The later protocol versions add:

* `Message_PlugIn_Status`
* `Message_PlugIn_Busy`
* `Message_PlugIn_Action`
* `Message_PlugIn_Abort`

Treat them as per-instance control messages, not task-global state.

In particular:

* a Stop or abort request applies to one embedded object
* UI state changes should not leak across other active instances in the same task
* if the plug-in advertises action support, review the returned busy-state updates as part of the same protocol
