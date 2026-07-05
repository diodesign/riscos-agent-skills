# `printdbox`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/printdbox`

Category: `class`

Purpose: C veneers to the Methods provided by the PrintDBox class

Use it when: Read for standard print dialogue flows.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/print.html

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `PrintDboxTemplate`
- `PrintDboxAboutToBeShownEvent`
- `PrintDboxDialogueCompletedEvent`
- `PrintDboxSetUpAboutToBeShownEvent`
- `PrintDboxSaveEvent`
- `PrintDboxSetUpEvent`
- `PrintDboxPrintEvent`

## Public Functions

- `printdbox_get_draft`: Gets whether draft printing is set for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_get_draft ( unsigned int flags, ObjectId printdbox, int *draft );`
- `printdbox_set_draft`: Sets whether draft printing is set for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_set_draft ( unsigned int flags, ObjectId printdbox, int draft );`
- `printdbox_get_title`: Gets the title for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_get_title ( unsigned int flags, ObjectId printdbox, char *buffer, int buff_size, int *nbytes );`
- `printdbox_get_orientation`: Gets the orientation for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_get_orientation ( unsigned int flags, ObjectId printdbox, int *orientation );`
- `printdbox_set_orientation`: Sets the orientation for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_set_orientation ( unsigned int flags, ObjectId printdbox, int orientation );`
- `printdbox_get_scale`: Gets the scale factor for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_get_scale ( unsigned int flags, ObjectId printdbox, int *scale_factor );`
- `printdbox_set_scale`: Sets the scale factor for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_set_scale ( unsigned int flags, ObjectId printdbox, int scale_factor );`
- `printdbox_get_copies`: Gets the number of copies set for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_get_copies ( unsigned int flags, ObjectId printdbox, int *copies );`
- `printdbox_set_copies`: Sets the number of copies to print for the print dbox
  Prototype: `extern _kernel_oserror *printdbox_set_copies ( unsigned int flags, ObjectId printdbox, int copies );`
- `printdbox_get_page_range`: Gets the page range for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_get_page_range ( unsigned int flags, ObjectId printdbox, int *start, int *end );`
- `printdbox_set_page_range`: Sets the page range for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_set_page_range ( unsigned int flags, ObjectId printdbox, int start, int end );`
- `printdbox_get_window_id`: Gets the id of the underlying window object for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_get_window_id ( unsigned int flags, ObjectId printdbox, ObjectId *window );`
- `printdbox_set_page_limit`: Sets the maximum page range for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_set_page_limit ( unsigned int flags, ObjectId printdbox, int page_limit );`
- `printdbox_get_page_limit`: Gets the maximum page range for the specified print dbox
  Prototype: `extern _kernel_oserror *printdbox_get_page_limit ( unsigned int flags, ObjectId printdbox, int *page_limit );`

## Public Constants And Method Codes

- `PrintDbox_GenerateShowEvent` = `0x00000001`
- `PrintDbox_GenerateHideEvent` = `0x00000002`
- `PrintDbox_GenerateSetupEvent` = `0x00000004`
- `PrintDbox_IncludeAllFromTo` = `0x00000008`
- `PrintDbox_IncludeCopies` = `0x00000010`
- `PrintDbox_IncludeScale` = `0x00000020`
- `PrintDbox_IncludeOrientation` = `0x00000040`
- `PrintDbox_IncludeSave` = `0x00000080`
- `PrintDbox_IncludeSetUp` = `0x00000100`
- `PrintDbox_IncludeDraft` = `0x00000200`
- `PrintDbox_SelectFromTo` = `0x00000400`
- `PrintDbox_SelectSideways` = `0x00000800`
- `PrintDbox_SelectDraft` = `0x00001000`
- `PrintDbox_AltWinNumberRange` = `0x00002000 /* CJB */`
- `PrintDbox_SWIChunkBase` = `0x82b00`
- `PrintDbox_ObjectClass` = `PrintDbox_SWIChunkBase`
- `PrintDbox_ClassSWI` = `(PrintDbox_SWIChunkBase + 0)`
- `PrintDbox_PostFilter` = `(PrintDbox_SWIChunkBase + 1)`
- `PrintDbox_PreFilter` = `(PrintDbox_SWIChunkBase + 2)`
- `PrintDbox_PageRangeAll` = `-1`
- `PrintDbox_GetWindowId` = `0`
- `PrintDbox_SetPageRange` = `1`
- `PrintDbox_GetPageRange` = `2`
- `PrintDbox_SetCopies` = `3`
- `PrintDbox_GetCopies` = `4`
- `PrintDbox_SetScale` = `5`
- `PrintDbox_GetScale` = `6`
- `PrintDbox_SetOrientation` = `7`
- `PrintDbox_GetOrientation` = `8`
- `PrintDbox_GetTitle` = `9`
- `PrintDbox_SetDraft` = `10`
- `PrintDbox_GetDraft` = `11`
- `PrintDbox_SetPageLimit` = `12 /* CJB */`
- `PrintDbox_GetPageLimit` = `13 /* CJB */`
- `PrintDbox_AboutToBeShown` = `PrintDbox_SWIChunkBase`
- `PrintDbox_DialogueCompleted` = `(PrintDbox_SWIChunkBase + 1)`
- `PrintDbox_SetUpAboutToBeShown` = `(PrintDbox_SWIChunkBase + 2)`
- `PrintDbox_Save` = `(PrintDbox_SWIChunkBase + 3)`
- `PrintDbox_SetUp` = `(PrintDbox_SWIChunkBase + 4)`
- `PrintDbox_Print` = `(PrintDbox_SWIChunkBase + 5)`
- `PrintDboxEvents_PrintSave_Sideways` = `0x00000001`
- `PrintDboxEvents_PrintSave_Draft` = `0x00000002`
