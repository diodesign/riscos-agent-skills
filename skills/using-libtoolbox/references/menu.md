# `menu`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/menu`

Category: `class`

Purpose: C veneers to the Methods provided by the Menu class

Use it when: Read for shared menus, per-entry state, submenu wiring, and selection dispatch.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/menus.html

## Includes

- `kernel.h`
- `toolbox.h`

## Main Types

- `MenuTemplateHeader`
- `MenuTemplateEntry`
- `MenuTemplate`
- `MenuAboutToBeShownEvent`
- `MenuHasBeenHiddenEvent`
- `MenuSubMenuEvent`
- `MenuSelectionEvent`

## Public Functions

- `menu_get_title`: Gets the title for the specified menu object
  Prototype: `extern _kernel_oserror *menu_get_title ( unsigned int flags, ObjectId menu, char *buffer, int buff_size, int *nbytes );`
- `menu_set_title`: Sets the title of the specified menu object
  Prototype: `extern _kernel_oserror *menu_set_title ( unsigned int flags, ObjectId menu, char *title );`
- `menu_get_width`: Gets the width of a menu if OS units
  Prototype: `extern _kernel_oserror *menu_get_width ( unsigned int flags, ObjectId menu, int *width );`
- `menu_get_height`: Get the height of a menu in OS units
  Prototype: `extern _kernel_oserror *menu_get_height ( unsigned int flags, ObjectId menu, int *height );`
- `menu_remove_entry`: Removes an entry from a menu object
  Prototype: `extern _kernel_oserror *menu_remove_entry ( unsigned int flags, ObjectId menu, ComponentId entry );`
- `menu_add_entry`: Adds an entry to a menu object
  Prototype: `extern _kernel_oserror *menu_add_entry ( unsigned int flags, ObjectId menu, ComponentId at_entry, char *entry_description, ComponentId *new_entry );`
- `menu_get_help_message`: Gets the help message for a menu object
  Prototype: `extern _kernel_oserror *menu_get_help_message ( unsigned int flags, ObjectId menu, char *buffer, int buff_size, int *nbytes );`
- `menu_set_help_message`: Sets the help message for a menu object
  Prototype: `extern _kernel_oserror *menu_set_help_message ( unsigned int flags, ObjectId menu, char *help_message );`
- `menu_get_entry_help_message`: Gets the help message for a menu entry
  Prototype: `extern _kernel_oserror *menu_get_entry_help_message ( unsigned int flags, ObjectId menu, ComponentId entry, char *buffer, int buff_size, int *nbytes );`
- `menu_set_entry_help_message`: Sets the help message for a menu entry
  Prototype: `extern _kernel_oserror *menu_set_entry_help_message ( unsigned int flags, ObjectId menu, ComponentId entry, char *help_message );`
- `menu_get_click_event`: Gets the event that will be raised when the menu entry is clicked
  Prototype: `extern _kernel_oserror *menu_get_click_event ( unsigned int flags, ObjectId menu, ComponentId entry, int *toolbox_event );`
- `menu_set_click_event`: Sets the event that will be raised when the menu entry is clicked
  Prototype: `extern _kernel_oserror *menu_set_click_event ( unsigned int flags, ObjectId menu, ComponentId entry, int toolbox_event );`
- `menu_get_click_show`: Gets the id of the object that will be shown when the menu entry is clicked
  Prototype: `extern _kernel_oserror *menu_get_click_show ( unsigned int flags, ObjectId menu, ComponentId entry, ObjectId *object, int *show_flags );`
- `menu_set_click_show`: Set the id of the object that will be shown when the menu entry is clicked
  Prototype: `extern _kernel_oserror *menu_set_click_show ( unsigned int flags, ObjectId menu, ComponentId entry, ObjectId object, int show_flags );`
- `menu_get_sub_menu_event`: Gets the event to be raised when the pointer is moved over the sub menu arrow
  Prototype: `extern _kernel_oserror *menu_get_sub_menu_event ( unsigned int flags, ObjectId menu, ComponentId entry, int *toolbox_event );`
- `menu_set_sub_menu_event`: Sets the event to be raised when the pointer is moved over sub menu arrow
  Prototype: `extern _kernel_oserror *menu_set_sub_menu_event ( unsigned int flags, ObjectId menu, ComponentId entry, int toolbox_event );`
- `menu_get_sub_menu_show`: Gets the id of the object to be shown when pointer moves over sub menu arrow
  Prototype: `extern _kernel_oserror *menu_get_sub_menu_show ( unsigned int flags, ObjectId menu, ComponentId entry, ObjectId *sub_menu );`
- `menu_set_sub_menu_show`: Sets the id of the object to be shown when pointer is moved over sub menu arrow
  Prototype: `extern _kernel_oserror *menu_set_sub_menu_show ( unsigned int flags, ObjectId menu, ComponentId entry, ObjectId sub_menu );`
- `menu_get_entry_sprite`: Gets the sprite name for a specific menu entry
  Prototype: `extern _kernel_oserror *menu_get_entry_sprite ( unsigned int flags, ObjectId menu, ComponentId entry, char *buffer, int buff_size, int *nbytes );`
- `menu_set_entry_sprite`: Sets the sprite name of a specific menu entry
  Prototype: `extern _kernel_oserror *menu_set_entry_sprite ( unsigned int flags, ObjectId menu, ComponentId entry, char *sprite_name );`
- `menu_get_entry_text`: Gets the text of a specific menu entry
  Prototype: `extern _kernel_oserror *menu_get_entry_text ( unsigned int flags, ObjectId menu, ComponentId entry, char *buffer, int buff_size, int *nbytes );`
- `menu_set_entry_text`: Sets the text of a specific menu entry
  Prototype: `extern _kernel_oserror *menu_set_entry_text ( unsigned int flags, ObjectId menu, ComponentId entry, char *text );`
- `menu_get_fade`: Gets the faded state of a specific menu entry
  Prototype: `extern _kernel_oserror *menu_get_fade ( unsigned int flags, ObjectId menu, ComponentId entry, int *faded );`
- `menu_set_fade`: Sets the fade state of a specific menu entry
  Prototype: `extern _kernel_oserror *menu_set_fade ( unsigned int flags, ObjectId menu, ComponentId entry, int fade );`
- `menu_get_tick`: Gets the tick state of a specific menu entry
  Prototype: `extern _kernel_oserror *menu_get_tick ( unsigned int flags, ObjectId menu, ComponentId entry, int *ticked );`
- `menu_set_tick`: Sets the tick state of a specific menu entry
  Prototype: `extern _kernel_oserror *menu_set_tick ( unsigned int flags, ObjectId menu, ComponentId entry, int tick );`

## Public Constants And Method Codes

- `Menu_GenerateShowEvent` = `0x00000001`
- `Menu_GenerateHideEvent` = `0x00000002`
- `Menu_Entry_Ticked` = `0x00000001`
- `Menu_Entry_DottedLine` = `0x00000002`
- `Menu_Entry_Faded` = `0x00000100`
- `Menu_Entry_IsSprite` = `0x00000200`
- `Menu_Entry_SubMenu` = `0x00000400`
- `Menu_Entry_GenerateSubMenuEvent` = `0x00000800`
- `Menu_Entry_ClickShowTransient` = `0x00001000`
- `Menu_SWIChunkBase` = `0x828c0`
- `Menu_ObjectClass` = `Menu_SWIChunkBase`
- `Menu_ClassSWI` = `(Menu_SWIChunkBase + 0)`
- `Menu_PostFilter` = `(Menu_SWIChunkBase + 1)`
- `Menu_PreFilter` = `(Menu_SWIChunkBase + 2)`
- `Menu_UpdateTree` = `(Menu_SWIChunkBase + 3)`
- `Menu_ClickShowTransient` = `0x00000001`
- `Menu_AddEntryBefore` = `0x00000001`
- `Menu_AddEntryAtBeginning` = `-1`
- `Menu_AddEntryAtEnd` = `-2`
- `Menu_SetTick` = `0`
- `Menu_GetTick` = `1`
- `Menu_SetFade` = `2`
- `Menu_GetFade` = `3`
- `Menu_SetEntryText` = `4`
- `Menu_GetEntryText` = `5`
- `Menu_SetEntrySprite` = `6`
- `Menu_GetEntrySprite` = `7`
- `Menu_SetSubMenuShow` = `8`
- `Menu_GetSubMenuShow` = `9`
- `Menu_SetSubMenuEvent` = `10`
- `Menu_GetSubMenuEvent` = `11`
- `Menu_SetClickShow` = `12`
- `Menu_GetClickShow` = `13`
- `Menu_SetClickEvent` = `14`
- `Menu_GetClickEvent` = `15`
- `Menu_SetHelpMessage` = `16`
- `Menu_GetHelpMessage` = `17`
- `Menu_SetEntryHelpMessage` = `18`
- `Menu_GetEntryHelpMessage` = `19`
- `Menu_AddEntry` = `20`
- `Menu_RemoveEntry` = `21`
- `Menu_GetHeight` = `22`
- `Menu_GetWidth` = `23`
- `Menu_SetTitle` = `24`
- `Menu_GetTitle` = `25`
- `Menu_AboutToBeShown` = `Menu_SWIChunkBase`
- `Menu_HasBeenHidden` = `(Menu_SWIChunkBase + 1)`
- `Menu_SubMenu` = `(Menu_SWIChunkBase + 2)`
- `Menu_Selection` = `(Menu_SWIChunkBase + 3)`
