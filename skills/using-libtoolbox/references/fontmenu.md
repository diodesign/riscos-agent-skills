# `fontmenu`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/fontmenu`

Category: `class`

Purpose: C veneers to the Methods provided by the FontMenu class

Use it when: Read for menu-based font selection.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/fontmenu.html

## Includes

- `kernel.h`
- `toolbox.h`

## Main Types

- `FontMenuTemplate`
- `FontMenuAboutToBeShownEvent`
- `FontMenuHasBeenHiddenEvent`
- `FontMenuSelectionEvent`

## Public Functions

- `fontmenu_get_font`: Gets the currently selected (ticked) font id for the specified font menu
  Prototype: `extern _kernel_oserror *fontmenu_get_font ( unsigned int flags, ObjectId fontmenu, char *buffer, int buff_size, int *nbytes );`
- `fontmenu_set_font`: Set the font to be selected (ticked) in the specified font menu
  Prototype: `extern _kernel_oserror *fontmenu_set_font ( unsigned int flags, ObjectId fontmenu, char *font_id );`

## Public Constants And Method Codes

- `FontMenu_GenerateShowEvent` = `0x00000001`
- `FontMenu_GenerateHideEvent` = `0x00000002`
- `FontMenu_SystemFont` = `0x00000004`
- `FontMenu_SWIChunkBase` = `0x82a40`
- `FontMenu_ObjectClass` = `FontMenu_SWIChunkBase`
- `FontMenu_ClassSWI` = `(FontMenu_SWIChunkBase + 0)`
- `FontMenu_PostFilter` = `(FontMenu_SWIChunkBase + 1)`
- `FontMenu_PreFilter` = `(FontMenu_SWIChunkBase + 2)`
- `FontMenu_SetFont` = `0`
- `FontMenu_GetFont` = `1`
- `FontMenu_AboutToBeShown` = `FontMenu_SWIChunkBase`
- `FontMenu_HasBeenHidden` = `(FontMenu_SWIChunkBase + 1)`
- `FontMenu_Selection` = `(FontMenu_SWIChunkBase + 2)`
