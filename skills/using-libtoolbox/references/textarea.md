# `textarea`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/textarea`

Category: `extension`

Purpose: C veneers to the Methods provided by the TextArea gadget

Use it when: Read for the TextArea gadget extension and its text-editing API.

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `TextArea`
- `TextAreaDataLoadedEvent`

## Public Functions

- `textarea_replace_text`: Replaces a block of text with new text in a specified textarea
  Prototype: `extern _kernel_oserror *textarea_replace_text ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int index_start, unsigned int index_end, const char *text );`
- `textarea_insert_text`: Inserts text at a specified offset into the specified textarea
  Prototype: `extern _kernel_oserror *textarea_insert_text ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int index, const char *text );`
- `textarea_set_state`: Sets the state of the specified textarea.
  Prototype: `extern _kernel_oserror *textarea_set_state ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int state );`
- `textarea_get_state`: Gets the state of the specified textarea.
  Prototype: `extern _kernel_oserror *textarea_get_state ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int *state );`
- `textarea_get_selection_text`: Gets the selected text of the specified textarea.
  Prototype: `extern _kernel_oserror *textarea_get_selection_text ( unsigned int flags, ObjectId window, ComponentId textarea, char *buffer, int size, unsigned int *nbytes );`
- `textarea_set_selection`: Sets the selection for the specified textarea.
  Prototype: `extern _kernel_oserror *textarea_set_selection ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int index_start, unsigned int index_end );`
- `textarea_get_selection_points`: Gets the selection points for the specified textarea.
  Prototype: `extern _kernel_oserror *textarea_get_selection_points ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int *index_start, unsigned int *index_end );`
- `textarea_set_colour`: Sets the colours for the specified textarea.
  Prototype: `extern _kernel_oserror *textarea_set_colour ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int foreground, unsigned int background );`
- `textarea_get_colour`: Gets the colours currently being used for the specified textarea.
  Prototype: `extern _kernel_oserror *textarea_get_colour ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int *foreground, unsigned int *background );`
- `textarea_get_text`: Gets the text that is current displayed in the specified textarea.
  Prototype: `extern _kernel_oserror *textarea_get_text ( unsigned int flags, ObjectId window, ComponentId writable, char *buffer, int buff_size, int *nbytes );`
- `textarea_set_text`: Sets the text string to be shown in the specified textarea
  Prototype: `extern _kernel_oserror *textarea_set_text ( unsigned int flags, ObjectId window, ComponentId writable, const char *text );`
- `textarea_set_font`: Set the font for the specified textarea.
  Prototype: `extern _kernel_oserror *textarea_set_font ( unsigned int flags, ObjectId window, ComponentId textarea, const char *font_name, unsigned int width, unsigned int height );`
- `textarea_set_cursor_position`: Sets the cursor position in a textarea
  Prototype: `extern _kernel_oserror *textarea_set_cursor_position ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int index, unsigned int *old_index );`
- `textarea_get_cursor_position`: Gets the cursor position in a textarea
  Prototype: `extern _kernel_oserror *textarea_get_cursor_position ( unsigned int flags, ObjectId window, ComponentId textarea, unsigned int *index );`
- `textarea_set_background`: Set window background
  Prototype: `extern _kernel_oserror *textarea_set_background ( unsigned int flags, ObjectId window, ComponentId textarea, void *sprite_area, void *sprite, int x_off, int y_off );`
- `textarea_get_window_id`: Read the underlying Window ObjectId for the gadget
  Prototype: `extern _kernel_oserror *textarea_get_window_id ( unsigned int flags, ObjectId window, ComponentId textarea, ObjectId *textarea_window );`

## Public Constants And Method Codes

- `TextArea_Scrollbar_Vertical` = `0x00000001`
- `TextArea_Scrollbar_Horizontal` = `0x00000002`
- `TextArea_WordWrap` = `0x00000004`
- `TextArea_AllowSelection` = `0x00000008`
- `TextArea_AllowSave` = `0x00000010`
- `TextArea_AllowLoad` = `0x00000020`
- `TextArea_Clipboard` = `0x00000040`
- `TextArea_AutoScroll` = `0x00000080`
- `TextArea_KeyNotify` = `0x00000100`
- `TextArea_DisplayOnly` = `0x00000200`
- `TextArea_BgAlignH_Default` = `(0<<10)`
- `TextArea_BgAlignH_Left` = `(1<<10)`
- `TextArea_BgAlignH_Right` = `(2<<10)`
- `TextArea_BgAlignH_Centre` = `(3<<10)`
- `TextArea_BgAlignH_Mask` = `(3<<10)`
- `TextArea_BgAlignV_Default` = `(0<<12)`
- `TextArea_BgAlignV_Bottom` = `(1<<12)`
- `TextArea_BgAlignV_Top` = `(2<<12)`
- `TextArea_BgAlignV_Centre` = `(3<<12)`
- `TextArea_BgAlignV_Mask` = `(3<<12)`
- `TextArea_BgTileHorizontal` = `0x00004000`
- `TextArea_BgTileVertical` = `0x00008000`
- `TextArea_BgNoScroll` = `0x00010000`
- `TextAreaValidFlags` = `0xC003FFFF`
- `TextArea_Base` = `0x4018`
- `TextArea_Type` = `(sizeof(TextArea)) << 16 | TextArea_Base`
- `TextArea_SWIBase` = `0x140180`
- `TextArea_GetState` = `(TextArea_Base + 0)`
- `TextArea_SetState` = `(TextArea_Base + 1)`
- `TextArea_SetText` = `(TextArea_Base + 2)`
- `TextArea_GetText` = `(TextArea_Base + 3)`
- `TextArea_InsertText` = `(TextArea_Base + 4)`
- `TextArea_ReplaceText` = `(TextArea_Base + 5)`
- `TextArea_GetSelection` = `(TextArea_Base + 6)`
- `TextArea_SetSelection` = `(TextArea_Base + 7)`
- `TextArea_SetFont` = `(TextArea_Base + 8)`
- `TextArea_SetColour` = `(TextArea_Base + 9)`
- `TextArea_GetColour` = `(TextArea_Base + 10)`
- `TextArea_SetCursorPosition` = `(TextArea_Base + 11)`
- `TextArea_GetCursorPosition` = `(TextArea_Base + 12)`
- `TextArea_SetBackground` = `(TextArea_Base + 13)`
- `TextArea_GetBackground` = `(TextArea_Base + 14) /* N/I */`
- `TextArea_GetWindowId` = `(TextArea_Base + 15)`
- `TextArea_DataLoaded` = `(TextArea_SWIBase + 0)`
- `TextArea_DesktopColours` = `(1<<0)`
- `TextArea_NamedSprite` = `(1<<0)`
- `TextArea_TextEnd` = `(-1)`
- `TextArea_TextStart` = `(0)`
- `TextArea_GetSelection_ReturnText` = `(1<<0)`
- `TextArea_SetCursorPosition_Force` = `(1<<0) /* Place caret even if not present */`
- `TextArea_SetCursorPosition_Invisible` = `(1<<1) /* Don't show a visible caret */`
