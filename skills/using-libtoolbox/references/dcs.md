# `dcs`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/dcs`

Category: `class`

Purpose: C veneers to the Methods provided by the DCS class

Use it when: Read for Discard/Cancel/Save confirmation flows.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/dcs.html

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `DCSTemplate`
- `DCSAboutToBeShownEvent`
- `DCSDiscardEvent`
- `DCSSaveEvent`
- `DCSDialogueCompletedEvent`
- `DCSCancelEvent`

## Public Functions

- `dcs_get_title`: Gets the title for the specified DCS object
  Prototype: `extern _kernel_oserror *dcs_get_title ( unsigned int flags, ObjectId dcs, char *buffer, int buff_size, int *nbytes );`
- `dcs_set_title`: Sets the title for the specified DCS object
  Prototype: `extern _kernel_oserror *dcs_set_title ( unsigned int flags, ObjectId dcs, char *title );`
- `dcs_get_message`: Gets the message used in the DCS object
  Prototype: `extern _kernel_oserror *dcs_get_message ( unsigned int flags, ObjectId dcs, char *buffer, int buff_size, int *nbytes );`
- `dcs_set_message`: Sets the message used in the DCS object
  Prototype: `extern _kernel_oserror *dcs_set_message ( unsigned int flags, ObjectId dcs, char *message );`
- `dcs_get_window_id`: Get the id of the underlying window object for the DCS object
  Prototype: `extern _kernel_oserror *dcs_get_window_id ( unsigned int flags, ObjectId dcs, ObjectId *window );`

## Public Constants And Method Codes

- `DCS_GenerateAboutToBeShown` = `0x00000001`
- `DCS_GenerateDialogueCompleted` = `0x00000002`
- `DCS_SWIChunkBase` = `0x82a80`
- `DCS_ObjectClass` = `DCS_SWIChunkBase`
- `DCS_ClassSWI` = `(DCS_SWIChunkBase + 0)`
- `DCS_PostFilter` = `(DCS_SWIChunkBase + 1)`
- `DCS_PreFilter` = `(DCS_SWIChunkBase + 2)`
- `DCS_GetWindowId` = `0`
- `DCS_SetMessage` = `1`
- `DCS_GetMessage` = `2`
- `DCS_SetTitle` = `3`
- `DCS_GetTitle` = `4`
- `DCS_AboutToBeShown` = `(DCS_SWIChunkBase+0)`
- `DCS_Discard` = `(DCS_SWIChunkBase+1)`
- `DCS_Save` = `(DCS_SWIChunkBase+2)`
- `DCS_DialogueCompleted` = `(DCS_SWIChunkBase+3)`
- `DCS_Cancel` = `(DCS_SWIChunkBase+4)`
