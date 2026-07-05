# Help Messages

Use this file for `HelpRequest` and `HelpReply` flows.

## HelpRequest handling

For `HelpRequest`:

* preserve the original pointer context from the incoming block; the reply should describe what was actually under the pointer
* identify the source window, icon, or menu item
* map that source to the token family the application uses
* generate the token deterministically

When the application is actively polling pointer position to decide whether to send a request:

* do not send a fresh `HelpRequest` on every null poll
* wait until the pointer has remained within a movement tolerance for a dwell period
* reset that dwell timer when the pointer moves materially

That keeps interactive help usable without flooding target tasks.

When the hovered target is standard window furniture rather than application work-area content:

* expect negative icon numbers for the built-in window tools
* handle those explicitly if the task wants custom help for close, back, iconise, scroll, or adjust-size furniture
* do not try to route furniture help through window-work-area logic or Toolbox gadget ids

If the UI is Toolbox-managed:

* remember that `Window`, `Gadget`, `Menu`, and `Iconbar` objects can answer normal help requests automatically
* only add a raw Wimp `HelpRequest` path when the application needs to override that behaviour or cover Wimp-only targets such as furniture icons

Common distinctions include:

* icon bar help
* window-level help
* icon-specific help
* menu-item help

For menu-item help generated from the current selection tree:

* read the live menu selection state from the Wimp
* treat the returned selection list as `-1` terminated
* derive the token from the full selection path, not just the top-level entry
* if different menus use different help-token families, switch the active help
  routing at the same time that you build or return the menu, rather than
  leaving it set to whichever menu happened to be opened previously

That pattern is useful for token families such as `HM0`, `HM30`, or similar menu-depth encodings.

## HelpReply construction

When building a `HelpReply`:

* copy `my_ref` from the request into the reply `your_ref`
* place the looked-up text in the reply buffer
* compute the message size from the header plus the returned text
* round the size to the alignment the Wimp expects
* send the reply to the original sender with the expected action code, not back to the hovered window/icon handles

Do not leave `your_ref` as zero unless the protocol explicitly permits it. Matching replies to requests matters when the sender tracks stale or missing responses.

If the reply text will be shown directly to the user:

* de-tokenise or expand any documented inline escapes before display
* preserve deliberate line breaks if the help format supports them
* reject or truncate oversized replies rather than overflowing the presentation buffer

Treat this as presentation sanitisation, not as part of the transport protocol itself.

Concrete recipe for replying to `HelpRequest`:

1. Read the incoming `HelpRequest` block and determine the hovered window,
   icon, or live menu selection path.
2. Map that context to the correct token family or literal help text.
3. Copy the request's `my_ref` into the reply's `your_ref`.
4. Set the reply action to `Message_HelpReply`.
5. Fill the reply text buffer with the looked-up help text.
6. Set the message size to the header plus the returned text, rounded to the
   alignment the Wimp expects.
7. Send the reply to the original sender task handle from the request, not to
   the hovered window or icon handle.

## Display lifetime

If the task presents help in its own bubble, window, or status area:

* remember the pointer position and time associated with the accepted reply
* clear the displayed help when the pointer moves beyond the intended tolerance
* optionally clear it after a timeout if the help is meant to be transient

Do not keep stale hover help visible once the pointer has clearly moved to a different target.

## Missing-reply fallback

If a direct `HelpRequest` is sent with acknowledgement semantics and no task replies:

* expect a `UserMessageAcknowledge` for the original `HelpRequest`
* treat that as “no help provider answered”, not as a successful help result
* use it only for fallback UI such as a generic description of the target task or icon

This is especially useful for iconbar targets where the user still expects some descriptive text even if the application under the pointer has no explicit help implementation.

If the application tracks the task that was asked for help:

* keep that recipient handle only for the outstanding request
* use it to derive a generic fallback such as the target task or icon name when no help reply arrives
* clear that remembered handle once the request has been satisfied or acknowledged as unanswered

## Help enable control

Some environments also use `Message_HelpEnable` to control interactive help globally.

When handling it:

* treat enable/disable separately from ordinary hover requests
* if the flags request a settings reload, rebuild any cached help presentation state after re-reading configuration
* do not assume the message itself implies a pointer query or a pending reply

## MessageTrans use

For token-based help:

* keep token generation simple and stable
* check the message-file contract and returned text length
* treat lookup failures as a help-path problem, not as a reason to corrupt general UI state
* keep menu-help token schemes deterministic enough that the same active menu path always maps to the same token
