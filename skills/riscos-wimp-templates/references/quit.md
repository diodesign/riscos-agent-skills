# Quit confirmation

Use this reference when the user needs a quit-confirmation window that is shown only when modified documents would be lost.

## Asset

- Copy [../assets/window_quit.txt](../assets/window_quit.txt) into the destination `TemplateText` file.
- The asset contains a single `wimp_window` block with `template_name:"quit"`.

## Behaviour notes

- Use this window only when there are modified documents and quitting would discard unsaved changes.
- Replace the window title text `Paint` with the application name.
- Replace the message text with the quit warning that matches the current state.
- Typical messages include `Do you want to close document '...' without saving?` and `There are 5 documents open. Are you sure you want to quit without saving?`.
- The message icon uses indirected text with validation `l40`, so long warnings may need wording adjusted to fit the available space.
- The standard action buttons are `Discard` and `Cancel`.

## Icon numbers

| Icon | Purpose | Notes |
| --- | --- | --- |
| 0 | Discard button | Confirms quitting and discarding unsaved changes. |
| 1 | Warning message | Indirected text for the modified-document quit message. |
| 2 | Cancel button | Leaves the application running. |
| 3 | Divider | Decorative sprite divider. |
