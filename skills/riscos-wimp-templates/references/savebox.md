# Save box

Use this reference when the user needs a standard save box window template.

## Asset

- Copy [../assets/window_savebox.txt](../assets/window_savebox.txt) into the destination `TemplateText` file.
- The asset contains a single `wimp_window` block with `template_name:"savebox"`.

## Behaviour notes

- This is a classic save dialogue with Save and Cancel action buttons.
- The writable icon uses `Pptr_write,2,2` validation and is intended for the file name/path field.
- Icon `1` is unused in the saved template and should normally be left alone unless the user asks for a specific repurposing.
- Icon `3` is the sprite drag icon that the user drags to a destination window to save the file there.
- The default filetype sprite validation on icon `3` is `Sfile_fff`, which represents `&FFF` (Text).
- Ask the user which filetype will be saved and update icon `3` validation from `Sfile_fff` to `Sfile_xxx`, where `xxx` is the lowercase hexadecimal filetype.

## Icon numbers

| Icon | Purpose | Notes |
| --- | --- | --- |
| 0 | Save button | Button icon. |
| 1 | Unused | Present in the template but not used by the standard save box behaviour. |
| 2 | Writable file field | Writable icon for the save path or leafname. |
| 3 | Filetype drag icon | Drag this sprite icon to the destination window; default validation `Sfile_fff`, replace with `Sfile_xxx` for the saved filetype. |
| 4 | Cancel button | Button icon. |
