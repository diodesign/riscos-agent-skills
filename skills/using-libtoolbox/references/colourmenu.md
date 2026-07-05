# `colourmenu`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/colourmenu`

Category: `class`

Purpose: C veneers to the Methods provided by the ColourMenu class

Use it when: Read for menu-based colour selection.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/colmenu.html

## Includes

- `kernel.h`
- `toolbox.h`

## Main Types

- `ColourMenuTemplate`
- `ColourMenuAboutToBeShownEvent`
- `ColourMenuSelectionEvent`
- `ColourMenuHasBeenHiddenEvent`

## Public Functions

- `colourmenu_get_title`: Gets the title for the specified colour menu
  Prototype: `extern _kernel_oserror *colourmenu_get_title ( unsigned int flags, ObjectId colourmenu, char *buffer, int buff_size, int *nbytes );`
- `colourmenu_set_title`: Sets the title of the specified colour menu
  Prototype: `extern _kernel_oserror *colourmenu_set_title ( unsigned int flags, ObjectId colourmenu, char *title );`
- `colourmenu_get_none_available`: Gets whether the specified colour menu has a "none" entry
  Prototype: `extern _kernel_oserror *colourmenu_get_none_available ( unsigned int flags, ObjectId colourmenu, int *none );`
- `colourmenu_set_none_available`: Set whether there is a "none" entry for the specified colour menu
  Prototype: `extern _kernel_oserror *colourmenu_set_none_available ( unsigned int flags, ObjectId colourmenu, int none );`
- `colourmenu_get_colour`: Gets the currently selected colour for the specified colour menu
  Prototype: `extern _kernel_oserror *colourmenu_get_colour ( unsigned int flags, ObjectId colourmenu, int *wimp_colour );`
- `colourmenu_set_colour`: Sets the currently selected colour (ticks it) for the specified colour menu
  Prototype: `extern _kernel_oserror *colourmenu_set_colour ( unsigned int flags, ObjectId colourmenu, int wimp_colour );`

## Public Constants And Method Codes

- `ColourMenu_GenerateAboutToBeShownEvent` = `0x00000001`
- `ColourMenu_GenerateHasBeenHiddenEvent` = `0x00000002`
- `ColourMenu_NoneEntry` = `0x00000004`
- `ColourMenu_SWIChunkBase` = `0x82980`
- `ColourMenu_ObjectClass` = `ColourMenu_SWIChunkBase`
- `ColourMenu_ClassSWI` = `(ColourMenu_SWIChunkBase + 0)`
- `ColourMenu_PostFilter` = `(ColourMenu_SWIChunkBase + 1)`
- `ColourMenu_PreFilter` = `(ColourMenu_SWIChunkBase + 2)`
- `ColourMenu_ColourNone` = `16`
- `ColourMenu_SetColour` = `0`
- `ColourMenu_GetColour` = `1`
- `ColourMenu_SetNoneAvailable` = `2`
- `ColourMenu_GetNoneAvailable` = `3`
- `ColourMenu_SetTitle` = `4`
- `ColourMenu_GetTitle` = `5`
- `ColourMenu_AboutToBeShown` = `ColourMenu_SWIChunkBase`
- `ColourMenu_HasBeenHidden` = `(ColourMenu_SWIChunkBase + 1)`
- `ColourMenu_Selection` = `(ColourMenu_SWIChunkBase + 2)`
