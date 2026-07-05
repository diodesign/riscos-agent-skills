# `scrolllist`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/scrolllist`

Category: `extension`

Purpose: C veneers to the Methods provided by the ScrollList gadget

Use it when: Read for the ScrollList gadget extension, including selection and database-query helpers.

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `ScrollList`
- `ScrollListSelectionEvent`
- `ScrollListQueryCompletedEvent`

## Public Functions

- `scrolllist_select_item`: Selects the given item from the specified scrolllist
  Prototype: `extern _kernel_oserror *scrolllist_select_item ( unsigned int flags, ObjectId window, ComponentId scrolllist, int index );`
- `scrolllist_set_font`: Set the font for the specified scrolllist.
  Prototype: `extern _kernel_oserror *scrolllist_set_font ( unsigned int flags, ObjectId window, ComponentId scrolllist, const char *font_name, unsigned int width, unsigned int height );`
- `scrolllist_get_colour`: Gets the colours currently being used for the specified scrolllist.
  Prototype: `extern _kernel_oserror *scrolllist_get_colour ( unsigned int flags, ObjectId window, ComponentId scrolllist, unsigned int *foreground, unsigned int *background );`
- `scrolllist_set_colour`: Sets the colours for the specified scrolllist.
  Prototype: `extern _kernel_oserror *scrolllist_set_colour ( unsigned int flags, ObjectId window, ComponentId scrolllist, unsigned int foreground, unsigned int background );`
- `scrolllist_get_item_text`: Gets the text of the specified scrolllist item.
  Prototype: `extern _kernel_oserror *scrolllist_get_item_text ( unsigned int flags, ObjectId window, ComponentId scrolllist, char *buffer, int size, int index, int *nbytes );`
- `scrolllist_set_item_text`: Sets the text of the specified scrolllist item.
  Prototype: `extern _kernel_oserror *scrolllist_set_item_text ( unsigned int flags, ObjectId window, ComponentId scrolllist, const char *new_text, int index );`
- `scrolllist_set_state`: Sets the state of the specified scrolllist.
  Prototype: `extern _kernel_oserror *scrolllist_set_state ( unsigned int flags, ObjectId window, ComponentId scrolllist, unsigned int state );`
- `scrolllist_get_state`: Gets the state of the specified scrolllist.
  Prototype: `extern _kernel_oserror *scrolllist_get_state ( unsigned int flags, ObjectId window, ComponentId scrolllist, unsigned int *state );`
- `scrolllist_add_item`: Adds an item to the specified scrolllist
  Prototype: `extern _kernel_oserror *scrolllist_add_item ( unsigned int flags, ObjectId window, ComponentId scrolllist, const char *text, const void *sprite_area, const char *sprite_name, int index );`
- `scrolllist_delete_items`: Deletes the items from the specified scrolllist
  Prototype: `extern _kernel_oserror *scrolllist_delete_items ( unsigned int flags, ObjectId window, ComponentId scrolllist, int start, int end );`
- `scrolllist_get_selected`: Gets the selected items from the specified scrolllist.
  Prototype: `extern _kernel_oserror *scrolllist_get_selected ( unsigned int flags, ObjectId window, ComponentId scrolllist, int offset, int *new_offset );`
- `scrolllist_make_visible`: Forces the given item of the specified scrolllist to be visible.
  Prototype: `extern _kernel_oserror *scrolllist_make_visible ( unsigned int flags, ObjectId window, ComponentId scrolllist, int index );`
- `scrolllist_deselect_item`: Deselects the specified item from the specified scrolllist
  Prototype: `extern _kernel_oserror *scrolllist_deselect_item ( unsigned int flags, ObjectId window, ComponentId scrolllist, int index );`
- `scrolllist_count_items`: Returns the number of items in the scrolllist
  Prototype: `extern _kernel_oserror *scrolllist_count_items ( unsigned int flags, ObjectId window, ComponentId scrolllist, unsigned int *items );`
- `scrolllist_get_heading_text`: Gets the heading of the specified scrolllist.
  Prototype: `extern _kernel_oserror *scrolllist_get_heading_text ( unsigned int flags, ObjectId window, ComponentId scrolllist, char *buffer, int size, int *nbytes );`
- `scrolllist_set_heading_text`: Set text of the scrolllist heading
  Prototype: `extern _kernel_oserror *scrolllist_set_heading_text ( unsigned int flags, ObjectId window, ComponentId scrolllist, const char *new_text );`
- `scrolllist_get_font`: Read the font for the specified scrolllist.
  Prototype: `extern _kernel_oserror *scrolllist_get_font ( unsigned int flags, ObjectId window, ComponentId scrolllist, char *buffer, int size, int *xsize, int *ysize, int *nbytes );`
- `scrolllist_database_attach`: Attach a database to a scrolling list
  Prototype: `extern _kernel_oserror *scrolllist_database_attach ( unsigned int flags, ObjectId window, ComponentId scrolllist, int db_id, const char *db_name );`
- `scrolllist_database_query`: Query the database, generating results to the scrolling list
  Prototype: `extern _kernel_oserror *scrolllist_database_query ( unsigned int flags, ObjectId window, ComponentId scrolllist, int db_id, void *db_handle, const char *query_string );`
- `scrolllist_set_column_properties`: Set properties for the columns in the list
  Prototype: `extern _kernel_oserror *scrolllist_set_column_properties ( unsigned int flags, ObjectId window, ComponentId scrolllist, int number_of_columns, unsigned long *data_list );`
- `scrolllist_decode_position`: Decode a pair of screen coordinates into relative coordinates, item and column
  Prototype: `extern _kernel_oserror *scrolllist_decode_position ( unsigned int flags, ObjectId window, ComponentId scrolllist, int screen_x, int screen_y, int *relative_x, int *relative_y, int *index, int *column );`

## Public Constants And Method Codes

- `ScrollList_SingleSelections` = `0x00000000`
- `ScrollList_MultipleSelections` = `0x00000001`
- `ScrollList_IconSelection` = `0x00000002 /* Use icons to select, rather than highlights */`
- `ScrollList_NoUserSelection` = `0x00000004 /* Don't allow anything to be selected by the user */`
- `ScrollList_VScroll_Optional` = `(0<<3) /* Allow VScroll to appear when the window becomes too large */`
- `ScrollList_VScroll_On` = `(1<<3) /* Force VScroll on all the time */`
- `ScrollList_VScroll_Off` = `(2<<3) /* Force VScroll off all the time */`
- `ScrollList_VScroll_Invalid` = `(3<<3) /* Invalid selection */`
- `ScrollList_VScroll_Mask` = `(3<<3) /* Mask for scroll bar type */`
- `ScrollList_HScroll_Optional` = `(0<<5) /* Allow HScroll to appear when the window becomes too large */`
- `ScrollList_HScroll_On` = `(1<<5) /* Force HScroll on all the time */`
- `ScrollList_HScroll_Off` = `(2<<5) /* Force HScroll off all the time */`
- `ScrollList_HScroll_Invalid` = `(3<<5) /* Invalid selection */`
- `ScrollList_HScroll_Mask` = `(3<<5) /* Mask for scroll bar type */`
- `ScrollListValidFlags` = `0xC000007f`
- `ScrollList_Base` = `0x401A`
- `ScrollList_Type` = `(sizeof(ScrollList)) << 16 | ScrollList_Base`
- `ScrollList_SWIBase` = `0x140182`
- `ScrollList_GetState` = `(ScrollList_Base + 0)`
- `ScrollList_SetState` = `(ScrollList_Base + 1)`
- `ScrollList_AddItem` = `(ScrollList_Base + 2)`
- `ScrollList_DeleteItems` = `(ScrollList_Base + 3)`
- `ScrollList_SelectItem` = `(ScrollList_Base + 4)`
- `ScrollList_DeselectItem` = `(ScrollList_Base + 5)`
- `ScrollList_GetSelected` = `(ScrollList_Base + 6)`
- `ScrollList_MakeVisible` = `(ScrollList_Base + 7)`
- `ScrollList_SetColour` = `(ScrollList_Base + 8)`
- `ScrollList_GetColour` = `(ScrollList_Base + 9)`
- `ScrollList_SetFont` = `(ScrollList_Base + 10)`
- `ScrollList_GetItemText` = `(ScrollList_Base + 11)`
- `ScrollList_CountItems` = `(ScrollList_Base + 12)`
- `ScrollList_SetItemText` = `(ScrollList_Base + 13)`
- `ScrollList_SetHeadingText` = `(ScrollList_Base + 14)`
- `ScrollList_GetHeadingText` = `(ScrollList_Base + 15)`
- `ScrollList_GetFont` = `(ScrollList_Base + 16)`
- `ScrollList_DatabaseAttach` = `(ScrollList_Base + 17)`
- `ScrollList_DatabaseRead` = `(ScrollList_Base + 18) /* N/I */`
- `ScrollList_DatabaseQuery` = `(ScrollList_Base + 19)`
- `ScrollList_SetColumnProperties` = `(ScrollList_Base + 20)`
- `ScrollList_GetColumnProperties` = `(ScrollList_Base + 21) /* N/I */`
- `ScrollList_DecodePosition` = `(ScrollList_Base + 22)`
- `ScrollList_Selection` = `(0x140180 + 1)`
- `ScrollList_Selection_Flags_Set` = `(1<<0)`
- `ScrollList_Selection_Flags_DoubleClick` = `(1<<1)`
- `ScrollList_Selection_Flags_AdjustClick` = `(1<<2)`
- `ScrollList_Selection_Flags_ClickData` = `(1<<3)`
- `ScrollList_QueryCompleted` = `(0x140180 + 2)`
- `ScrollList_QueryCompleted_Flags_OK` = `(0<<0) /* Success */`
- `ScrollList_QueryCompleted_Flags_Failed` = `(1<<0) /* The query failed */`
- `ScrollList_QueryCompleted_Flags_Reset` = `(2<<0) /* Query reset by user */`
- `ScrollList_QueryCompleted_Flags_TypeMask` = `(3<<0) /* Mask for the type */`
- `ScrollList_DesktopColours` = `(1<<0)`
- `ScrollList_HeadingColours` = `(1<<1)`
- `ScrollList_SelectionChangingMethod_SendEvent` = `(1u<<0)`
- `ScrollList_SelectionChangingMethod_OnAll` = `(1u<<1)`
- `ScrollList_AddItem_SpriteType_WimpPool` = `(0u<<0) /* name-> wimp sprite name */`
- `ScrollList_AddItem_SpriteType_UserPool` = `(1u<<0) /* area-> user area, name-> sprite name */`
- `ScrollList_AddItem_SpriteType_Pointer` = `(2u<<0) /* name-> sprite */`
- `ScrollList_AddItem_SpriteType_Invalid` = `(3u<<0)`
- `ScrollList_AddItem_SpriteHalfSize` = `(1u<<2)`
- `ScrollList_AddItem_MakeVisible` = `(1u<<3)`
- `ScrollList_AddItem_IndentMask` = `(15)`
- `ScrollList_AddItem_IndentShift` = `(4)`
- `ScrollList_DeleteItems_DoNotJumpToTop` = `(1u<<1)`
- `ScrollList_DatabaseQuery_ClearFirst` = `(1<<0)`
- `ScrollList_DatabaseQuery_UseQueryHeadings` = `(1<<1)`
- `ScrollList_CountItems_Rows` = `(0)`
- `ScrollList_CountItems_Columns` = `(1)`
- `ScrollList_CountItems_FullWidth` = `(2)`
- `ScrollList_CountItems_FullHeight` = `(3)`
- `ScrollList_CountItems_TypeMask` = `(255)`
- `ScrollList_ColumnProperties_TypeMask` = `(255)`
- `ScrollList_ColumnProperties_Widths` = `(0)`
