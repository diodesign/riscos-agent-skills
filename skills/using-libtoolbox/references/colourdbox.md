# `colourdbox`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/colourdbox`

Category: `class`

Purpose: C veneers to the Methods provided by the ColourDBox class

Use it when: Read for the standard colour selection dialogue.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/colourdbox.html

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `ColourDboxTemplate`
- `ColourDboxAboutToBeShownEvent`
- `ColourDboxDialogueCompletedEvent`
- `ColourDboxColourSelectedEvent`
- `ColourDboxColourChangedEvent`

## Public Functions

- `colourdbox_get_none_available`: Gets whether the "none" option is available for the specified ColourDbox
  Prototype: `extern _kernel_oserror *colourdbox_get_none_available ( unsigned int flags, ObjectId colourdbox, int *out_flags );`
- `colourdbox_set_none_available`: Set whether a "none" option appears in the specified ColourDbox
  Prototype: `extern _kernel_oserror *colourdbox_set_none_available ( unsigned int flags, ObjectId colourdbox, int none );`
- `colourdbox_get_colour_model`: Gets the current colour model for the specified ColourDbox
  Prototype: `extern _kernel_oserror *colourdbox_get_colour_model ( unsigned int flags, ObjectId colourdbox, int *buffer, int buff_size, int *nbytes );`
- `colourdbox_set_colour_model`: Set the colour model for the specified ColourDbox
  Prototype: `extern _kernel_oserror *colourdbox_set_colour_model ( unsigned int flags, ObjectId colourdbox, int *colour_model_block );`
- `colourdbox_get_colour`: Gets the colour that is currently being shown in the specified ColourDbox
  Prototype: `extern _kernel_oserror *colourdbox_get_colour ( unsigned int flags, ObjectId colourdbox, int *buffer, int buff_size, int *outflags, int *nbytes );`
- `colourdbox_set_colour`: Set the colour to be displayed in the specified ColourDbox
  Prototype: `extern _kernel_oserror *colourdbox_set_colour ( unsigned int flags, ObjectId colourdbox, int *colour_block );`
- `colourdbox_get_dialogue_handle`: Gets the underlying dialogue handle for the specified ColourDbox
  Prototype: `extern _kernel_oserror *colourdbox_get_dialogue_handle ( unsigned int flags, ObjectId colourdbox, int *dialogue_handle );`
- `colourdbox_get_wimp_handle`: Gets the underlying window handle for the specified ColourDbox
  Prototype: `extern _kernel_oserror *colourdbox_get_wimp_handle ( unsigned int flags, ObjectId colourdbox, int *wimp_handle );`

## Public Constants And Method Codes

- `ColourDbox_GenerateShowEvent` = `0x00000001`
- `ColourDbox_GenerateHideEvent` = `0x00000002`
- `ColourDbox_IncludeNoneButton` = `0x00000004`
- `ColourDbox_SelectNoneButton` = `0x00000008`
- `ColourDbox_SWIChunkBase` = `0x829c0`
- `ColourDbox_ObjectClass` = `ColourDbox_SWIChunkBase`
- `ColourDbox_ClassSWI` = `(ColourDbox_SWIChunkBase + 0)`
- `ColourDbox_PostFilter` = `(ColourDbox_SWIChunkBase + 1)`
- `ColourDbox_PreFilter` = `(ColourDbox_SWIChunkBase + 2)`
- `ColourDbox_ColourNoneSelected` = `0x00000001`
- `ColourDbox_GetWimpHandle` = `0`
- `ColourDbox_GetDialogueHandle` = `1`
- `ColourDbox_SetColour` = `2`
- `ColourDbox_GetColour` = `3`
- `ColourDbox_SetColourModel` = `4`
- `ColourDbox_GetColourModel` = `5`
- `ColourDbox_SetNoneAvailable` = `6`
- `ColourDbox_GetNoneAvailable` = `7`
- `ColourDbox_AboutToBeShown` = `ColourDbox_SWIChunkBase`
- `ColourDbox_DialogueCompleted` = `(ColourDbox_SWIChunkBase + 1)`
- `ColourDbox_ColourSelected` = `(ColourDbox_SWIChunkBase + 2)`
