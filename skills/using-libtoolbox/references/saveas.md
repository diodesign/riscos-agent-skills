# `saveas`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/saveas`

Category: `class`

Purpose: C veneers to the Methods provided by the SaveAs class

Use it when: Read for SaveAs dialogues and the Toolbox-managed save protocol.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/saveas.html

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `SaveAsTemplate`
- `SaveAsAboutToBeShownEvent`
- `SaveAsDialogueCompletedEvent`
- `SaveAsSaveToFileEvent`
- `SaveAsFillBufferEvent`
- `SaveAsSaveCompletedEvent`

## Public Functions

- `saveas_file_save_completed`: Confirms whether a file save was completed successfully for the saveas object
  Prototype: `extern _kernel_oserror *saveas_file_save_completed ( unsigned int flags, ObjectId saveas, char *filename );`
- `saveas_buffer_filled`: Confirms that a buffer has been filled for the saveas object
  Prototype: `extern _kernel_oserror *saveas_buffer_filled ( unsigned int flags, ObjectId saveas, void *buffer, int bytes_written );`
- `saveas_set_data_address`: Sets the address of the data (and selection) for the saveas object
  Prototype: `extern _kernel_oserror *saveas_set_data_address ( unsigned int flags, ObjectId saveas, void *data, int data_size, void *selection, int selection_size );`
- `saveas_selection_available`: Indicates whether there is a selection available for the saveas object
  Prototype: `extern _kernel_oserror *saveas_selection_available ( unsigned int flags, ObjectId saveas, int selection );`
- `saveas_get_file_size`: Gets the estimated file size for the specified
  Prototype: `extern _kernel_oserror *saveas_get_file_size ( unsigned int flags, ObjectId saveas, int *file_size );`
- `saveas_set_file_size`: Sets the estimated file size for the specified saveas object
  Prototype: `extern _kernel_oserror *saveas_set_file_size ( unsigned int flags, ObjectId saveas, int file_size );`
- `saveas_get_file_type`: Gets the filetype for the specified saveas object
  Prototype: `extern _kernel_oserror *saveas_get_file_type ( unsigned int flags, ObjectId saveas, int *file_type );`
- `saveas_set_file_type`: Sets the filetype for the specified saveas object
  Prototype: `extern _kernel_oserror *saveas_set_file_type ( unsigned int flags, ObjectId saveas, int file_type );`
- `saveas_get_file_name`: Gets the filename for the specified saveas object
  Prototype: `extern _kernel_oserror *saveas_get_file_name ( unsigned int flags, ObjectId saveas, char *buffer, int buff_size, int *nbytes );`
- `saveas_set_file_name`: Sets the filename for the specified saveas object
  Prototype: `extern _kernel_oserror *saveas_set_file_name ( unsigned int flags, ObjectId saveas, char *file_name );`
- `saveas_get_title`: Gets the title for the specified saveas object
  Prototype: `extern _kernel_oserror *saveas_get_title ( unsigned int flags, ObjectId saveas, char *buffer, int buff_size, int *nbytes );`
- `saveas_set_title`: Sets the title for the specified saveas object
  Prototype: `extern _kernel_oserror *saveas_set_title ( unsigned int flags, ObjectId saveas, char *title );`
- `saveas_get_window_id`: Gets the id of the underlying window of object for the saveas object
  Prototype: `extern _kernel_oserror *saveas_get_window_id ( unsigned int flags, ObjectId saveas, ObjectId *window );`

## Public Constants And Method Codes

- `SaveAs_GenerateShowEvent` = `0x00000001`
- `SaveAs_GenerateHideEvent` = `0x00000002`
- `SaveAs_ExcludeSelectionButton` = `0x00000004`
- `SaveAs_AutomaticRAMTransfer` = `0x00000008`
- `SaveAs_ClientSupportsRAMTransfer` = `0x00000010`
- `SaveAs_AllowMultipleSaves` = `0x00000020 /* CJB */`
- `SaveAs_SWIChunkBase` = `0x82bc0`
- `SaveAs_ObjectClass` = `SaveAs_SWIChunkBase`
- `SaveAs_ClassSWI` = `(SaveAs_SWIChunkBase + 0)`
- `SaveAs_PostFilter` = `(SaveAs_SWIChunkBase + 1)`
- `SaveAs_PreFilter` = `(SaveAs_SWIChunkBase + 2)`
- `SaveAs_Directory` = `0x1000`
- `SaveAs_Application` = `0x2000`
- `SaveAs_OnlySaveSelection` = `0x00000001`
- `SaveAs_SuccessfulSave` = `0x00000001`
- `SaveAs_GetWindowId` = `0`
- `SaveAs_SetTitle` = `1`
- `SaveAs_GetTitle` = `2`
- `SaveAs_SetFileName` = `3`
- `SaveAs_GetFileName` = `4`
- `SaveAs_SetFileType` = `5`
- `SaveAs_GetFileType` = `6`
- `SaveAs_SetFileSize` = `7`
- `SaveAs_GetFileSize` = `8`
- `SaveAs_SelectionAvailable` = `9`
- `SaveAs_SetDataAddress` = `10`
- `SaveAs_BufferFilled` = `11`
- `SaveAs_FileSaveCompleted` = `12`
- `SaveAs_AboutToBeShown` = `SaveAs_SWIChunkBase`
- `SaveAs_DialogueCompleted` = `(SaveAs_SWIChunkBase + 1)`
- `SaveAs_SaveToFile` = `(SaveAs_SWIChunkBase + 2)`
- `SaveAs_FillBuffer` = `(SaveAs_SWIChunkBase + 3)`
- `SaveAs_SaveCompleted` = `(SaveAs_SWIChunkBase + 4)`
- `SaveAs_SelectionBeingSaved` = `0x00000001`
- `SaveAs_SelectionSaved` = `0x00000001`
- `SaveAs_DestinationSafe` = `0x00000002`
