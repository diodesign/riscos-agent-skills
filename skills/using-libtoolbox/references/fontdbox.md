# `fontdbox`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/fontdbox`

Category: `class`

Purpose: C veneers to the Methods provided by the FontDBox class

Use it when: Read for the standard font chooser dialogue.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/fontdbox.html

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `FontDboxTemplate`
- `FontDboxAboutToBeShownEvent`
- `FontDboxDialogueCompletedEvent`
- `FontDboxApplyFontEvent`

## Public Functions

- `fontdbox_get_title`: Gets the title from the specified font dbox
  Prototype: `extern _kernel_oserror *fontdbox_get_title ( unsigned int flags, ObjectId fontdbox, char *buffer, int buff_size, int *nbytes );`
- `fontdbox_set_title`: Sets the title for the specified font dbox
  Prototype: `extern _kernel_oserror *fontdbox_set_title ( unsigned int flags, ObjectId fontdbox, char *title );`
- `fontdbox_get_try_string`: Gets the string used in the "try" writable for the specified font dbox
  Prototype: `extern _kernel_oserror *fontdbox_get_try_string ( unsigned int flags, ObjectId fontdbox, char *buffer, int buff_size, int *nbytes );`
- `fontdbox_set_try_string`: Sets the string used in the "try" writable for the specified font dbox
  Prototype: `extern _kernel_oserror *fontdbox_set_try_string ( unsigned int flags, ObjectId fontdbox, char *try_string );`
- `fontdbox_get_size`: Gets the height and/or aspect ratio for the specified font dbox
  Prototype: `extern _kernel_oserror *fontdbox_get_size ( unsigned int flags, ObjectId fontdbox, int *height, int *aspect_ratio );`
- `fontdbox_set_size`: Sets the height and/or the aspect ratio for the specified font dbox
  Prototype: `extern _kernel_oserror *fontdbox_set_size ( unsigned int flags, ObjectId fontdbox, int height, int aspect_ratio );`
- `fontdbox_get_font`: Gets the font id of the currently selected font for the specified font dbox
  Prototype: `extern _kernel_oserror *fontdbox_get_font ( unsigned int flags, ObjectId fontdbox, char *buffer, int buff_size, int *nbytes );`
- `fontdbox_set_font`: Sets the font for the specified font dbox
  Prototype: `extern _kernel_oserror *fontdbox_set_font ( unsigned int flags, ObjectId fontdbox, char *font_id );`
- `fontdbox_get_window_id`: returns the Window Object Id for the given Font Dbox
  Prototype: `extern _kernel_oserror *fontdbox_get_window_id ( unsigned int flags, ObjectId fontdbox, ObjectId *window );`

## Public Constants And Method Codes

- `FontDbox_GenerateShowEvent` = `0x00000001`
- `FontDbox_GenerateHideEvent` = `0x00000002`
- `FontDbox_IncludeSystemFont` = `0x00000004`
- `FontDbox_SystemFontFixSize` = `0x00000008`
- `FontDbox_SWIChunkBase` = `0x82a00`
- `FontDbox_ObjectClass` = `FontDbox_SWIChunkBase`
- `FontDbox_ClassSWI` = `(FontDbox_SWIChunkBase + 0)`
- `FontDbox_PostFilter` = `(FontDbox_SWIChunkBase + 1)`
- `FontDbox_PreFilter` = `(FontDbox_SWIChunkBase + 2)`
- `FontDbox_SetSize_Height` = `1`
- `FontDbox_SetSize_Aspect` = `2`
- `FontDbox_GetWindowId` = `0`
- `FontDbox_SetFont` = `1`
- `FontDbox_GetFont` = `2`
- `FontDbox_SetSize` = `3`
- `FontDbox_GetSize` = `4`
- `FontDbox_SetTryString` = `5`
- `FontDbox_GetTryString` = `6`
- `FontDbox_SetTitle` = `7`
- `FontDbox_GetTitle` = `8`
- `FontDbox_AboutToBeShown` = `FontDbox_SWIChunkBase`
- `FontDbox_DialogueCompleted` = `(FontDbox_SWIChunkBase + 1)`
- `FontDbox_ApplyFont` = `(FontDbox_SWIChunkBase + 2)`
