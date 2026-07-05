# `scale`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/scale`

Category: `class`

Purpose: C veneers to the Methods provided by the Scale class

Use it when: Read for scale-factor dialogues.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/scale.html

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `ScaleTemplate`
- `ScaleAboutToBeShownEvent`
- `ScaleDialogueCompletedEvent`
- `ScaleApplyFactorEvent`

## Public Functions

- `scale_get_title`: Gets the title for the specified scale object
  Prototype: `extern _kernel_oserror *scale_get_title ( unsigned int flags, ObjectId scale, char *buffer, int buff_size, int *nbytes );`
- `scale_set_title`: Sets the title for the specifed scale object
  Prototype: `extern _kernel_oserror *scale_set_title ( unsigned int flags, ObjectId scale, char *title );`
- `scale_get_bounds`: Gets the bounds and/or step size for the specified scale object
  Prototype: `extern _kernel_oserror *scale_get_bounds ( unsigned int flags, ObjectId scale, int *lower_bound, int *upper_bound, int *step_size );`
- `scale_set_bounds`: Sets the bounds and/or step size for the specified scale object
  Prototype: `extern _kernel_oserror *scale_set_bounds ( unsigned int flags, ObjectId scale, int lower_bound, int upper_bound, int step_size );`
- `scale_get_value`: Gets the scale factor value for the specified scale object
  Prototype: `extern _kernel_oserror *scale_get_value ( unsigned int flags, ObjectId scale, int *value );`
- `scale_set_value`: Sets the scale factor value for the specified scale object
  Prototype: `extern _kernel_oserror *scale_set_value ( unsigned int flags, ObjectId scale, int value );`
- `scale_get_window_id`: Gets the id of the underlying window object for the scale object
  Prototype: `extern _kernel_oserror *scale_get_window_id ( unsigned int flags, ObjectId scale, ObjectId *window );`

## Public Constants And Method Codes

- `Scale_GenerateShowEvent` = `0x00000001`
- `Scale_GenerateHideEvent` = `0x00000002`
- `Scale_IncludeScaleToFit` = `0x00000004`
- `Scale_SWIChunkBase` = `0x82c00`
- `Scale_ObjectClass` = `Scale_SWIChunkBase`
- `Scale_ClassSWI` = `(Scale_SWIChunkBase + 0)`
- `Scale_PostFilter` = `(Scale_SWIChunkBase + 1)`
- `Scale_PreFilter` = `(Scale_SWIChunkBase + 2)`
- `Scale_SetLowerBound` = `0x00000001`
- `Scale_SetUpperBound` = `0x00000002`
- `Scale_SetStepSize` = `0x00000004`
- `Scale_GetWindowId` = `0`
- `Scale_SetValue` = `1`
- `Scale_GetValue` = `2`
- `Scale_SetBounds` = `3`
- `Scale_GetBounds` = `4`
- `Scale_SetTitle` = `5`
- `Scale_GetTitle` = `6`
- `Scale_AboutToBeShown` = `Scale_SWIChunkBase`
- `Scale_DialogueCompleted` = `(Scale_SWIChunkBase + 1)`
- `Scale_ApplyFactor` = `(Scale_SWIChunkBase + 2)`
