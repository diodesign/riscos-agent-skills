# `window`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/window`

Category: `class`

Purpose: C veneers to the Methods provided by the Window class

Use it when: Read for Toolbox windows, toolbars, pointer/help/menu attachment, keyboard shortcuts, and Wimp bridging.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/windows.html

## Includes

- `kernel.h`
- `toolbox.h`
- `gadgets.h`
- `wimp.h`

## Main Types

- `KeyboardShortcut`
- `Gadget`
- `WindowTemplate`
- `WindowShowObjectBlock`
- `WindowAboutToBeShownEvent`
- `WindowHasBeenHiddenEvent`
- `WindowGadgetLostFocusEvent`
- `WindowGadgetMouseScrollEvent`

## Public Functions

- `window_extract_gadget_info`: Veneer for SWI Window_ExtractGadgetInfo
  Prototype: `extern _kernel_oserror *window_extract_gadget_info ( unsigned int flags, ObjectTemplateHeader *templ, ComponentId gadget, void **desc, int *size );`
- `window_wimp_to_toolbox`: Gets the object handle and component id that contains the
  Prototype: `extern _kernel_oserror *window_wimp_to_toolbox ( unsigned int flags, int window_handle, int icon_handle, ObjectId *object, ComponentId *component );`
- `window_get_pointer_info`: gets the ObjectId's and CompontentId's if the
  Prototype: `extern _kernel_oserror *window_get_pointer_info ( unsigned int flags, int *x_pos, int *y_pos, int *buttons, ObjectId *window, ComponentId *component );`
- `window_get_tool_bars`: returns the toolbars that are attached to a window
  Prototype: `extern _kernel_oserror *window_get_tool_bars ( unsigned int flags, ObjectId window, ObjectId *ibl, ObjectId *itl, ObjectId *ebl, ObjectId *etl );`
- `window_set_tool_bars`: Sets the toolbars attached to a window
  Prototype: `extern _kernel_oserror *window_set_tool_bars ( unsigned int flags, ObjectId window, ObjectId ibl, ObjectId itl, ObjectId ebl, ObjectId etl );`
- `window_set_menu`: Sets the menu that will be displayed when MENU is clicked over window object
  Prototype: `extern _kernel_oserror *window_set_menu ( unsigned int flags, ObjectId window, ObjectId menu_id );`
- `window_remove_gadget`: Removes a gadget for the specified window object
  Prototype: `extern _kernel_oserror *window_remove_gadget ( unsigned int flags, ObjectId window, ComponentId gadget );`
- `window_add_gadget`: Adds a gadget to the list of gadgets for the specified window object
  Prototype: `extern _kernel_oserror *window_add_gadget ( unsigned int flags, ObjectId window, Gadget *gadget, ComponentId *gadget_component );`
- `window_get_wimp_handle`: Gets the underlying Wimp handle for the specified window object
  Prototype: `extern _kernel_oserror *window_get_wimp_handle ( unsigned int flags, ObjectId window, int *window_handle );`
- `window_get_menu`: Gets the menu that will be displayed when MENU us clicked over window object
  Prototype: `extern _kernel_oserror *window_get_menu ( unsigned int flags, ObjectId window, ObjectId *menu_id );`
- `window_set_pointer`: Sets the pointer shape that will be used when pointer enters window object
  Prototype: `extern _kernel_oserror *window_set_pointer ( unsigned int flags, ObjectId window, char *sprite_name, int x_hot_spot, int y_hot_spot );`
- `window_get_pointer`: Gets the pointer shape that is shown when the pointer enters the window object
  Prototype: `extern _kernel_oserror *window_get_pointer ( unsigned int flags, ObjectId window, char *buffer, int buff_size, int *nbytes, int *x_hot_spot, int *y_hot_spot );`
- `window_set_help_message`: Sets the help message that is associated with the specified window object
  Prototype: `extern _kernel_oserror *window_set_help_message ( unsigned int flags, ObjectId window, char *message_text );`
- `window_get_help_message`: Gets the help message that is associated with the specified window object
  Prototype: `extern _kernel_oserror *window_get_help_message ( unsigned int flags, ObjectId window, char *buffer, int buff_len, int *nbytes );`
- `window_add_keyboard_shortcuts`: Adds the number of keyboard shortcuts to the list for this window object
  Prototype: `extern _kernel_oserror *window_add_keyboard_shortcuts ( unsigned int flags, ObjectId window, int no_shortcuts, KeyboardShortcut *shortcuts );`
- `window_remove_keyboard_shortcuts`: Removes a number of keyboard shortcuts from the list for the window obj
  Prototype: `extern _kernel_oserror *window_remove_keyboard_shortcuts ( unsigned int flags, ObjectId window, int no_remove, KeyboardShortcut *shortcuts );`
- `window_set_title`: Sets the title for the specified window object
  Prototype: `extern _kernel_oserror *window_set_title ( unsigned int flags, ObjectId window, char *title );`
- `window_get_title`: Gets the title for the specified window object
  Prototype: `extern _kernel_oserror *window_get_title ( unsigned int flags, ObjectId window, char *buffer, int buff_size, int *nbytes );`
- `window_set_default_focus`: Sets the component that gets the input focus for the specified window
  Prototype: `extern _kernel_oserror *window_set_default_focus ( unsigned int flags, ObjectId window, ComponentId focus );`
- `window_get_default_focus`: Gets the id of the component that has the input focus for the specified window
  Prototype: `extern _kernel_oserror *window_get_default_focus ( unsigned int flags, ObjectId window, ComponentId *focus );`
- `window_set_extent`: Sets the extent of the specified window
  Prototype: `extern _kernel_oserror *window_set_extent ( unsigned int flags, ObjectId window, BBox *extent );`
- `window_get_extent`: Gets the extent of the specified window
  Prototype: `extern _kernel_oserror *window_get_extent ( unsigned int flags, ObjectId window, BBox *extent );`
- `window_force_redraw`: Forces a redraw of the supplied area for the specified window
  Prototype: `extern _kernel_oserror *window_force_redraw ( unsigned int flags, ObjectId window, BBox *redraw_box );`
- `window_set_colour`: Sets the colour of the window
  Prototype: `extern _kernel_oserror *window_set_colour ( unsigned int flags, ObjectId window, int colour_index, unsigned int colour );`
- `window_get_colour`: Returns the colour that is assigned to part of the window
  Prototype: `extern _kernel_oserror *window_get_colour ( unsigned int flags, ObjectId window, int colour_index, unsigned int *colour );`

## Public Constants And Method Codes

- `KeyboardShortcut_ShowAsTransient` = `0x00000001`
- `Window_GenerateAboutToBeShown` = `0x00000001`
- `Window_AutoOpen` = `0x00000002`
- `Window_AutoClose` = `0x00000004`
- `Window_GenerateHasBeenHidden` = `0x00000008`
- `Window_IsToolBar` = `0x00000010`
- `Window_ToolBarButtonHideParent` = `0x00000020`
- `Window_GetWimpHandle` = `0`
- `Window_AddGadget` = `1`
- `Window_RemoveGadget` = `2`
- `Window_SetMenu` = `3`
- `Window_GetMenu` = `4`
- `Window_SetPointer` = `5`
- `Window_GetPointer` = `6`
- `Window_SetHelpMessage` = `7`
- `Window_GetHelpMessage` = `8`
- `Window_AddKeyboardShortcuts` = `9`
- `Window_RemoveKeyboardShortcuts` = `10`
- `Window_SetTitle` = `11`
- `Window_GetTitle` = `12`
- `Window_SetDefaultFocus` = `13`
- `Window_GetDefaultFocus` = `14`
- `Window_SetExtent` = `15`
- `Window_GetExtent` = `16`
- `Window_ForceRedraw` = `17`
- `Window_SetToolBars` = `18`
- `Window_GetToolBars` = `19`
- `Window_GetColour` = `20`
- `Window_SetColour` = `21`
- `Window_AboutToBeShown` = `(Window_SWIChunkBase + 0)`
- `Window_HasBeenHidden` = `(Window_SWIChunkBase + 16)`
- `Window_GadgetLostFocus` = `(Window_SWIChunkBase + 17)`
- `Window_GadgetMouseScroll` = `(Window_SWIChunkBase + 18)`
- `Window_SWIChunkBase` = `0x82880`
- `Window_ObjectClass` = `Window_SWIChunkBase`
- `Window_ClassSWI` = `(Window_SWIChunkBase + 0)`
- `Window_PostFilter` = `(Window_SWIChunkBase + 1)`
- `Window_PreFilter` = `(Window_SWIChunkBase + 2)`
- `Window_GetPointerInfo` = `(Window_SWIChunkBase + 3)`
- `Window_WimpToToolbox` = `(Window_SWIChunkBase + 4)`
- `Window_ExtractGadgetInfo` = `(Window_SWIChunkBase + 62)`
- `Window_InternalBottomLeftToolbar` = `1`
- `Window_InternalTopLeftToolbar` = `2`
- `Window_ExternalBottomLeftToolbar` = `4`
- `Window_ExternalTopLeftToolbar` = `8`
- `Window_GetPointerAdjust` = `0x00000001`
- `Window_GetPointerMenu` = `0x00000002`
- `Window_GetPointerSelect` = `0x00000004`
- `Window_GetPointerNotToolboxWindow` = `0x00000100`
- `Window_ColourTitleFG` = `0`
- `Window_ColourTitleBG` = `1`
- `Window_ColourWorkFG` = `2`
- `Window_ColourWorkBG` = `3`
- `Window_ColourScrollOuter` = `4`
- `Window_ColourScrollInner` = `5`
- `Window_ColourInputFocus` = `6`
- `Window_ColourDesktopColours` = `1 /* Flag for Set/Get Colour */`
