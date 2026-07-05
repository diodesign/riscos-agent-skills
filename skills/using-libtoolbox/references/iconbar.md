# `iconbar`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/iconbar`

Category: `class`

Purpose: C veneers to the Methods provided by the IconBar class

Use it when: Read for iconbar object templates, Select/Adjust behaviour, menus, help, and icon presentation.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/iconbar.html

## Includes

- `kernel.h`
- `toolbox.h`

## Main Types

- `IconbarTemplate`
- `IconbarClickedEvent`
- `IconbarAboutToBeShownEvent`

## Public Functions

- `iconbar_get_icon_handle`: Gets the underlying Wimp icon handler for the iconbar object
  Prototype: `extern _kernel_oserror *iconbar_get_icon_handle ( unsigned int flags, ObjectId iconbar, int *icon_handle );`
- `iconbar_set_menu`: Sets the menu which will be displayed when MENU is clicked over iconbar object
  Prototype: `extern _kernel_oserror *iconbar_set_menu ( unsigned int flags, ObjectId iconbar, ObjectId menu_id );`
- `iconbar_get_menu`: Gets the menu which will be displayed when MENU is clicked over iconbar
  Prototype: `extern _kernel_oserror *iconbar_get_menu ( unsigned int flags, ObjectId iconbar, ObjectId *menu_id );`
- `iconbar_set_event`: Sets events that will be raised when SELECT/ADJUST are clicked on iconbar
  Prototype: `extern _kernel_oserror *iconbar_set_event ( unsigned int flags, ObjectId iconbar, int select_event, int adjust_event );`
- `iconbar_get_event`: Gets events which will be raised when SELECT/ADJUST are clicked on iconbar
  Prototype: `extern _kernel_oserror *iconbar_get_event ( unsigned int flags, ObjectId iconbar, int *select_event, int *adjust_event );`
- `iconbar_set_show`: Sets objects to be shown which SELECT/ADJUST are clicked on iconbar
  Prototype: `extern _kernel_oserror *iconbar_set_show ( unsigned int flags, ObjectId iconbar, ObjectId select, ObjectId adjust );`
- `iconbar_get_show`: Gets the objects that will be shown when SELECT/ADJUST are clicked on iconbar
  Prototype: `extern _kernel_oserror *iconbar_get_show ( unsigned int flags, ObjectId iconbar, ObjectId *select, ObjectId *adjust );`
- `iconbar_set_help_message`: Sets the iconbar objects interactive help message
  Prototype: `extern _kernel_oserror *iconbar_set_help_message ( unsigned int flags, ObjectId iconbar, char *message_text );`
- `iconbar_get_help_message`: Gets the iconbar objects interactive help message
  Prototype: `extern _kernel_oserror *iconbar_get_help_message ( unsigned int flags, ObjectId iconbar, char *buffer, int buff_size, int *nbytes );`
- `iconbar_set_text`: Sets the text string that will be used for text & sprite iconbar objects
  Prototype: `extern _kernel_oserror *iconbar_set_text ( unsigned int flags, ObjectId iconbar, char *text );`
- `iconbar_get_text`: Gets the text string that will be used for text & sprite iconbar objects
  Prototype: `extern _kernel_oserror *iconbar_get_text ( unsigned int flags, ObjectId iconbar, char *buffer, int buff_size, int *nbytes );`
- `iconbar_set_sprite`: Sets the sprite to be used for the iconbar object
  Prototype: `extern _kernel_oserror *iconbar_set_sprite ( unsigned int flags, ObjectId iconbar, char *sprite_name );`
- `iconbar_get_sprite`: Gets the sprite that is used for the iconbar object
  Prototype: `extern _kernel_oserror *iconbar_get_sprite ( unsigned int flags, ObjectId iconbar, char *buffer, int buff_len, int *nbytes );`

## Public Constants And Method Codes

- `Iconbar_GenerateSelectAboutToBeShown` = `0x00000001`
- `Iconbar_GenerateAdjustAboutToBeShown` = `0x00000002`
- `Iconbar_ShowSelectTransient` = `0x00000004`
- `Iconbar_ShowAdjustTransient` = `0x00000008`
- `Iconbar_GenerateSelectClickedEvent` = `0x00000020`
- `Iconbar_GenerateAdjustClickedEvent` = `0x00000040`
- `Iconbar_ValidFlags` = `0x00000177`
- `Iconbar_SWIChunkBase` = `0x82900`
- `Iconbar_ObjectClass` = `Iconbar_SWIChunkBase`
- `Iconbar_ClassSWI` = `(Iconbar_SWIChunkBase + 0)`
- `Iconbar_PostFilter` = `(Iconbar_SWIChunkBase + 1)`
- `Iconbar_PreFilter` = `(Iconbar_SWIChunkBase + 2)`
- `Iconbar_GetIconHandle` = `0`
- `Iconbar_SetMenu` = `1`
- `Iconbar_GetMenu` = `2`
- `Iconbar_SetEvent` = `3`
- `Iconbar_GetEvent` = `4`
- `Iconbar_SetShow` = `5`
- `Iconbar_GetShow` = `6`
- `Iconbar_SetHelpMessage` = `7`
- `Iconbar_GetHelpMessage` = `8`
- `Iconbar_SetText` = `9`
- `Iconbar_GetText` = `10`
- `Iconbar_SetSprite` = `11`
- `Iconbar_GetSprite` = `12`
- `Iconbar_SetEvent_Select` = `0x00000001`
- `Iconbar_SetEvent_Adjust` = `0x00000002`
- `Iconbar_SetShow_Select` = `0x00000001`
- `Iconbar_SetShow_Adjust` = `0x00000002`
- `Iconbar_Clicked` = `(Iconbar_SWIChunkBase + 0)`
- `Iconbar_SelectAboutToBeShown` = `(Iconbar_SWIChunkBase + 1)`
- `Iconbar_AdjustAboutToBeShown` = `(Iconbar_SWIChunkBase + 2)`
- `Iconbar_Clicked_Adjust` = `0x00000001`
- `Iconbar_Clicked_Select` = `0x00000004`
