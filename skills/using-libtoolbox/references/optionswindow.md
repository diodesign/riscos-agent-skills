# `optionswindow`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/optionswindow`

Category: `extension`

Purpose: Read the underlying Window ObjectId for the options window

Use it when: Read for the extra OptionsWindow object module and pane-management API.

## Includes

- `kernel.h`
- `toolbox.h`

## Main Types

- `OptionsWindowTemplate`
- `OptionsWindowDialogueCompletedEvent`
- `OptionsWindowFillInPaneEvent`
- `OptionsWindowConfigurePaneEvent`
- `OptionsWindowSaveEvent`

## Public Functions

- `optionswindow_get_window_id`: Read the underlying Window ObjectId for the options window
  Prototype: `extern _kernel_oserror *optionswindow_get_window_id ( unsigned int flags, ObjectId optionswindow, ObjectId *window );`
- `optionswindow_add_pane`: Add a pane to the options window
  Prototype: `extern _kernel_oserror *optionswindow_add_pane ( unsigned int flags, ObjectId optionswindow, ComponentId new_componentid, ObjectId new_panewindow );`
- `optionswindow_remove_pane`: Remove a pane from the OptionsWindow
  Prototype: `extern _kernel_oserror *optionswindow_remove_pane ( unsigned int flags, ObjectId optionswindow, ComponentId component );`
- `optionswindow_select_pane`: Select the pane to be displayed
  Prototype: `extern _kernel_oserror *optionswindow_select_pane ( unsigned int flags, ObjectId optionswindow, ComponentId component );`
- `optionswindow_set_modified`: Set the OptionsWindow as having been modified
  Prototype: `extern _kernel_oserror *optionswindow_set_modified ( unsigned int flags, ObjectId optionswindow, int modified );`
- `optionswindow_get_modified`: Read whether the OptionsWindow has been modified or not
  Prototype: `extern _kernel_oserror *optionswindow_get_modified ( unsigned int flags, ObjectId optionswindow, int *modified );`
- `optionswindow_enumerate_panes`: Enumerate the panes which are used by the OptionsWindow
  Prototype: `extern _kernel_oserror *optionswindow_enumerate_panes ( unsigned int flags, ObjectId optionswindow, ComponentId last_component, ObjectId *window, ComponentId *component );`

## Public Constants And Method Codes

- `OptionsWindow_NoAutoModified` = `(1<<0)`
- `OptionsWindow_HasSetButton` = `(1<<1)`
- `OptionsWindow_HasCancelButton` = `(1<<2)`
- `OptionsWindow_HasSaveButton` = `(1<<3)`
- `OptionsWindow_HasDefaultButton` = `(1<<4)`
- `OptionsWindow_ObjectVersionNumber` = `(100)`
- `OptionsWindow_SWIChunkBase` = `0x100280`
- `OptionsWindow_ObjectClass` = `OptionsWindow_SWIChunkBase`
- `OptionsWindow_ClassSWI` = `(OptionsWindow_SWIChunkBase + 0)`
- `OptionsWindow_PostFilter` = `(OptionsWindow_SWIChunkBase + 1)`
- `OptionsWindow_PreFilter` = `(OptionsWindow_SWIChunkBase + 2)`
- `OptionsWindow_GetWindowId` = `0`
- `OptionsWindow_AddPane` = `1`
- `OptionsWindow_RemovePane` = `2`
- `OptionsWindow_SelectPane` = `3`
- `OptionsWindow_SetModified` = `4`
- `OptionsWindow_GetModified` = `5`
- `OptionsWindow_EnumeratePanes` = `6`
- `OptionsWindow_DialogueCompleted` = `(OptionsWindow_SWIChunkBase + 0)`
- `OptionsWindow_FillInPaneDefault` = `(OptionsWindow_SWIChunkBase + 1)`
- `OptionsWindow_FillInPaneCurrent` = `(OptionsWindow_SWIChunkBase + 2)`
- `OptionsWindow_ConfigurePane` = `(OptionsWindow_SWIChunkBase + 3)`
- `OptionsWindow_Save` = `(OptionsWindow_SWIChunkBase + 4)`
- `Program_Error` = `(0x1b000000)`
- `OptionsWindow_ErrorBase` = `(Program_Error | 0x80ab00) /* Check this base */`
- `OptionsWindow_AllocFailed` = `(OptionsWindow_ErrorBase+0x01)`
- `OptionsWindow_ShortBuffer` = `(OptionsWindow_ErrorBase+0x02)`
- `OptionsWindow_BadObjectVersion` = `(OptionsWindow_ErrorBase+0x03)`
- `OptionsWindow_BadFlags` = `(OptionsWindow_ErrorBase+0x04)`
- `OptionsWindow_NoSuchTask` = `(OptionsWindow_ErrorBase+0x11)`
- `OptionsWindow_NoSuchMethod` = `(OptionsWindow_ErrorBase+0x12)`
- `OptionsWindow_NoSuchMiscOpMethod` = `(OptionsWindow_ErrorBase+0x13)`
- `OptionsWindow_BadMethodFlags` = `(OptionsWindow_ErrorBase+0x14)`
- `OptionsWindow_BadComponent` = `(OptionsWindow_ErrorBase+0x15)`
- `OptionsWindow_TasksActive` = `(OptionsWindow_ErrorBase+0x21)`
