# `fileinfo`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/fileinfo`

Category: `class`

Purpose: C veneers to the Methods provided by the FileInfo class

Use it when: Read for the standard file metadata dialogue.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/fileinfo.html

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `FileInfoTemplate`
- `FileInfoAboutToBeShownEvent`
- `FileInfoDialogueCompletedEvent`

## Public Functions

- `fileinfo_get_window_id`: Gets the underlyling window object ID for the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_get_window_id ( unsigned int flags, ObjectId fileinfo, ObjectId *window );`
- `fileinfo_set_modified`: Set the modified flag for the specified fileinfo object
  Prototype: `extern _kernel_oserror *fileinfo_set_modified ( unsigned int flags, ObjectId fileinfo, int modified );`
- `fileinfo_get_modified`: Gets the modified flag for the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_get_modified ( unsigned int flags, ObjectId fileinfo, int *modified );`
- `fileinfo_set_file_type`: Sets the file type for the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_set_file_type ( unsigned int flags, ObjectId fileinfo, int file_type );`
- `fileinfo_get_file_type`: Gets the file type for the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_get_file_type ( unsigned int flags, ObjectId fileinfo, int *file_type );`
- `fileinfo_set_file_name`: Sets the filename for the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_set_file_name ( unsigned int flags, ObjectId fileinfo, char *file_name );`
- `fileinfo_get_file_name`: Gets the filename from the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_get_file_name ( unsigned int flags, ObjectId fileinfo, char *buffer, int buff_size, int *nbytes );`
- `fileinfo_set_file_size`: Sets the file size for the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_set_file_size ( unsigned int flags, ObjectId fileinfo, int file_size );`
- `fileinfo_get_file_size`: Gets the file size from the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_get_file_size ( unsigned int flags, ObjectId fileinfo, int *file_size );`
- `fileinfo_set_date`: Set the date for the specified file info object (using a 5 byte UTC)
  Prototype: `extern _kernel_oserror *fileinfo_set_date ( unsigned int flags, ObjectId fileinfo, int *UTC );`
- `fileinfo_get_date`: Gets the date for the specified file info object (a 5 byte UTC)
  Prototype: `extern _kernel_oserror *fileinfo_get_date ( unsigned int flags, ObjectId fileinfo, int *UTC );`
- `fileinfo_set_title`: Sets the title for the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_set_title ( unsigned int flags, ObjectId fileinfo, char *title );`
- `fileinfo_get_title`: Gets the title from the specified file info object
  Prototype: `extern _kernel_oserror *fileinfo_get_title ( unsigned int flags, ObjectId fileinfo, char *buffer, int buff_size, int *nbytes );`

## Public Constants And Method Codes

- `FileInfo_GenerateShowEvent` = `0x00000001`
- `FileInfo_GenerateHideEvent` = `0x00000002`
- `FileInfo_SWIChunkBase` = `0x82ac0`
- `FileInfo_ObjectClass` = `FileInfo_SWIChunkBase`
- `FileInfo_ClassSWI` = `(FileInfo_SWIChunkBase + 0)`
- `FileInfo_PostFilter` = `(FileInfo_SWIChunkBase + 1)`
- `FileInfo_PreFilter` = `(FileInfo_SWIChunkBase + 2)`
- `FileInfo_Directory` = `0x1000`
- `FileInfo_Application` = `0x2000`
- `FileInfo_GetWindowId` = `0`
- `FileInfo_SetModified` = `1`
- `FileInfo_GetModified` = `2`
- `FileInfo_SetFileType` = `3`
- `FileInfo_GetFileType` = `4`
- `FileInfo_SetFileName` = `5`
- `FileInfo_GetFileName` = `6`
- `FileInfo_SetFileSize` = `7`
- `FileInfo_GetFileSize` = `8`
- `FileInfo_SetDate` = `9`
- `FileInfo_GetDate` = `10`
- `FileInfo_SetTitle` = `11`
- `FileInfo_GetTitle` = `12`
- `FileInfo_AboutToBeShown` = `FileInfo_SWIChunkBase`
- `FileInfo_DialogueCompleted` = `(FileInfo_SWIChunkBase + 1)`
