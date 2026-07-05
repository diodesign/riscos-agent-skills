# `quit`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/quit`

Category: `class`

Purpose: C veneers to the Methods provided by the Quit class

Use it when: Read for quit-confirmation dialogues.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/quit.html

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `QuitTemplate`
- `QuitAboutToBeShownEvent`
- `QuitQuitEvent`
- `QuitDialogueCompletedEvent`
- `QuitCancelEvent`

## Public Functions

- `quit_get_window_id`: Get the id of the underlying window object for the quit object
  Prototype: `extern _kernel_oserror *quit_get_window_id ( unsigned int flags, ObjectId quit, ObjectId *window );`
- `quit_set_message`: Sets the message used in the quit object
  Prototype: `extern _kernel_oserror *quit_set_message ( unsigned int flags, ObjectId quit, char *message );`
- `quit_get_message`: Gets the message used in the quit object
  Prototype: `extern _kernel_oserror *quit_get_message ( unsigned int flags, ObjectId quit, char *buffer, int buff_size, int *nbytes );`
- `quit_set_title`: Sets the title for the specified quit object
  Prototype: `extern _kernel_oserror *quit_set_title ( unsigned int flags, ObjectId quit, char *title );`
- `quit_get_title`: Gets the title for the specified quit object
  Prototype: `extern _kernel_oserror *quit_get_title ( unsigned int flags, ObjectId quit, char *buffer, int buff_size, int *nbytes );`

## Public Constants And Method Codes

- `Quit_GenerateAboutToBeShown` = `0x00000001`
- `Quit_GenerateDialogueCompleted` = `0x00000002`
- `Quit_SWIChunkBase` = `0x82a90`
- `Quit_ObjectClass` = `Quit_SWIChunkBase`
- `Quit_ClassSWI` = `(Quit_SWIChunkBase + 0)`
- `Quit_PostFilter` = `(Quit_SWIChunkBase + 1 - 0x10)`
- `Quit_PreFilter` = `(Quit_SWIChunkBase + 2 - 0x10)`
- `Quit_GetWindowId` = `0`
- `Quit_SetMessage` = `1`
- `Quit_GetMessage` = `2`
- `Quit_SetTitle` = `3`
- `Quit_GetTitle` = `4`
- `Quit_AboutToBeShown` = `(Quit_SWIChunkBase+0)`
- `Quit_Quit` = `(Quit_SWIChunkBase+1)`
- `Quit_DialogueCompleted` = `(Quit_SWIChunkBase+2)`
- `Quit_Cancel` = `(Quit_SWIChunkBase+3)`
