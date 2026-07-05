# Windows

## Use this reference for

- Window titles and layout
- Closing, iconising, moving, resizing, and scrolling
- Drag behaviour within windows
- Context-sensitive pointers
- Screen takeover decisions

## Titles and naming

- Use the standard names for window parts in documentation and help text.
- Show a sensible default document name for unsaved editor windows.
- Append ` *` to the title when the document has been modified.
- Do not overload the title bar with unrelated status if another pane or display can show it.

## Standard behaviour

- Let the Wimp handle normal front, back, move, resize, and scroll behaviour.
- Preserve the user's chosen resized window size as the new standard size where the Wimp expects it.
- Reopen iconised windows with the same unsaved state and view position.
- Provide an application-specific inner sprite for iconised windows.
- Keep window behaviour consistent whether the user acts with `Select`, `Adjust`, or standard Shift-modified close/iconise gestures.

## Closing and data safety

- When closing a window would lose unsaved data, offer the user a chance to save first.
- Follow the standard close semantics rather than inventing new close-button behaviour.
- Keep iconising distinct from closing when Shift-modified close is used.

## Scrolling and dragging

- Use automatic scrolling when the pointer is held near the edge during text or object drags.
- Use copy semantics for cross-window drags unless a deliberate move gesture is indicated.
- Let `Escape` cancel a drag and restore the original position.
- Restrict custom drag logic to cases where the normal Wimp drag model is insufficient.

## Pointers and full-screen use

- Use established context-sensitive pointer shapes rather than novel ones.
- Do not take over the whole screen unless the application genuinely requires it.
- Where full-screen operation is needed, still preserve a route back to normal desktop behaviour if possible.
