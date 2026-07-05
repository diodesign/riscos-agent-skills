# Close confirmation

Use this reference when the user needs a close-confirmation window for a single document with unsaved changes.

## Asset

- Copy [../assets/window_close.txt](../assets/window_close.txt) into the destination `TemplateText` file.
- The asset contains a single `wimp_window` block with `template_name:"close"`.

## Behaviour notes

- Use this window only when one document is being closed and it has unsaved changes.
- Replace the window title text `Paint` with the application name.
- Replace the message text with the close warning for the current document.
- The standard wording is `This document had unsaved changes. Do you wish to save the data before closing it?`
- The message icon uses indirected text with validation `l40`, so long warnings may need wording adjusted to fit the available space.
- The standard action buttons are `Discard`, `Cancel`, and `Save`.

## Icon numbers

| Icon | Purpose | Notes |
| --- | --- | --- |
| 0 | Save button | Saves the document before closing it. |
| 1 | Warning message | Indirected text for the unsaved-changes warning. |
| 2 | Discard button | Closes the document and discards unsaved changes. |
| 3 | Cancel button | Leaves the document open. |
| 4 | Divider | Decorative sprite divider. |
