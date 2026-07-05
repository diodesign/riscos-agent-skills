# Document window

Use this reference when the user needs a resizeable document window whose contents are fully redrawn by the application.

## Asset

- Copy [../assets/window_document.txt](../assets/window_document.txt) into the destination `TemplateText` file.
- The asset contains a single `wimp_window` block with `template_name:"document"`.

## Behaviour notes

- This is a general template for document windows when the application redraws the entire work area itself.
- The window is moveable, closeable, resizeable, and supports both horizontal and vertical scrolling.
- The default work background is `wimp_COLOUR_TRANSPARENT`, which is suitable when the whole work area is user-redrawn.
- If only parts of the work area are redrawn, change `work_bg` to `7` or `0` to make the background black or white.
- The title would commonly be set to the name of the file being edited.
- Append ` *` to the title when the document has been modified.
- The default title text in the asset is `<Sprite>` and should normally be replaced by the application.

## Icon numbers

This template has no `wimp_icon` blocks. The application is expected to redraw the work area directly.
