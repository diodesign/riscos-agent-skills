# Input, Mouse, And Selection

## Use this reference for

- Mouse vocabulary and behaviour
- Caret and input-focus handling
- Keyboard shortcuts
- Text and object selection
- Drag and drop, cut, copy, and paste

## Mouse rules

- Use the established names `Select`, `Menu`, and `Adjust`.
- Do not repurpose the three mouse buttons for novel core meanings.
- Use `Select` for primary actions and `Adjust` for additive, alternative, or keep-open behaviour.
- Support standard editor shortcuts such as double-click word selection where relevant.

## Caret and focus

- Move the caret only when the user takes a definite action that places input focus.
- Do not bring a window to the front merely because it gains the caret.
- Do not give a window the caret merely because it comes to the front.
- Surrender the caret when menus or dialogues that took it are closed.
- Pass unknown keystrokes on with `Wimp_ProcessKey` rather than swallowing them.

## Keyboard shortcuts

- Keep common commands consistent across applications.
- Use the established function-key and named-key shortcuts for common operations when the application supports those operations.
- Do not invent conflicting shortcuts for standard commands.
- Avoid using `Alt` for general shortcuts in the classic style model described by the guide.
- Preserve the normal meaning of named keys such as `Print`.
- Refer to function keys in user-facing text as `F1`, `F2`, and so on.

## Selection rules

- Clicking `Select` should create a primary selection.
- `Adjust` should add to or modify the current selection without forcing a restart.
- Support drag selection for text and objects.
- Double-click selection should expand to words where text is involved.
- Use automatic scrolling when selection drags approach the edge of a window.
- In standard writable icons, keep the selection tied to the icon that currently owns the caret.
- In standard writable icons, `Adjust` should be able to create or extend a selection from the caret position.
- Leaving a writable icon or moving the caret elsewhere should end that icon-local selection.

## Clipboard and drag/drop

- Prefer cut/copy/paste as the standard transfer model for new applications.
- Copying must leave the original selection in place.
- Paste text immediately after the caret.
- Paste objects with their top-left corner at the pointer position unless the object model demands another standard anchor.
- Distinguish copy and move gestures consistently during drag and drop.
- For ordinary writable icons, prefer the standard WindowManager cut-and-paste behaviour over custom text-editing semantics.

## Accessibility

- Remain compatible with non-standard input devices supported through normal RISC OS input paths.
