# `ToolAction`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/ToolAction`

Category: `extension`

Purpose: C veneers to the Methods provided by the ToolAction gadget

Use it when: Read for the ToolAction gadget extension used for toolbar-like controls with separate Select/Adjust behaviour.

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`

## Main Types

- `ToolAction`
- `ToolActionSelectedEvent`

## Public Functions

- `toolaction_set_ident`: Set the ident string for a toolaction gadget
  Prototype: `extern _kernel_oserror *toolaction_set_ident ( unsigned int flags, ObjectId window, ComponentId toolaction, char *identity );`
- `toolaction_get_ident`: Read the ident string for a toolaction gadget
  Prototype: `extern _kernel_oserror *toolaction_get_ident ( unsigned int flags, ObjectId window, ComponentId toolaction, char *buffer, int buffersize, int *bufferused );`
- `toolaction_set_action`: Set the action to perform on triggering the tool
  Prototype: `extern _kernel_oserror *toolaction_set_action ( unsigned int flags, ObjectId window, ComponentId toolaction, int select_action, int adjust_action );`
- `toolaction_get_action`: Read the action performed on triggering the tool
  Prototype: `extern _kernel_oserror *toolaction_get_action ( unsigned int flags, ObjectId window, ComponentId toolaction, int *select_action, int *adjust_action );`
- `toolaction_set_click_show`: Set the objects to be shown when the gadget is clicked
  Prototype: `extern _kernel_oserror *toolaction_set_click_show ( unsigned int flags, ObjectId window, ComponentId toolaction, ObjectId select_show, ObjectId adjust_show );`
- `toolaction_get_click_show`: Read the objects which will be shown when the gadget is clicked
  Prototype: `extern _kernel_oserror *toolaction_get_click_show ( unsigned int flags, ObjectId window, ComponentId toolaction, ObjectId *select_show, ObjectId *adjust_show );`
- `toolaction_set_state`: Set the state of the ToolAction gadget
  Prototype: `extern _kernel_oserror *toolaction_set_state ( unsigned int flags, ObjectId window, ComponentId toolaction, int state );`
- `toolaction_get_state`: Read the state of the ToolAction gadget
  Prototype: `extern _kernel_oserror *toolaction_get_state ( unsigned int flags, ObjectId window, ComponentId toolaction, int *state );`
- `toolaction_set_pressed`: Set the pressed state
  Prototype: `extern _kernel_oserror *toolaction_set_pressed ( unsigned int flags, ObjectId window, ComponentId toolaction, int pressed );`
- `toolaction_get_pressed`: Read the pressed state
  Prototype: `extern _kernel_oserror *toolaction_get_pressed ( unsigned int flags, ObjectId window, ComponentId toolaction, int *pressed );`

## Public Constants And Method Codes

- `ToolAction_GenerateSelectedEvent` = `(1<<0)`
- `ToolAction_IsText` = `(1<<1)`
- `ToolAction_On` = `(1<<2)`
- `ToolAction_AutoToggle` = `(1<<3)`
- `ToolAction_NoPressedSprite` = `(1<<4)`
- `ToolAction_AutoRepeat` = `(1<<5)`
- `ToolAction_ShowTransient` = `(1<<6)`
- `ToolAction_ShowPopUp` = `(1<<7)`
- `ToolAction_HasFadeSprite` = `(1<<8)`
- `ToolAction_SelectWhenOver` = `(1<<9)`
- `ToolActionValidFlags` = `0xC00003FF`
- `ToolAction_Base` = `0x14014`
- `ToolAction_Type` = `((sizeof(ToolAction)) << 16 | (ToolAction_Base & 0xFFFF))`
- `ToolAction_SWIBase` = `0x140140`
- `ToolAction_SetIdent` = `(ToolAction_SWIBase + 0)`
- `ToolAction_GetIdent` = `(ToolAction_SWIBase + 1)`
- `ToolAction_SetAction` = `(ToolAction_SWIBase + 2)`
- `ToolAction_GetAction` = `(ToolAction_SWIBase + 3)`
- `ToolAction_SetClickShow` = `(ToolAction_SWIBase + 4)`
- `ToolAction_GetClickShow` = `(ToolAction_SWIBase + 5)`
- `ToolAction_SetState` = `(ToolAction_SWIBase + 6)`
- `ToolAction_GetState` = `(ToolAction_SWIBase + 7)`
- `ToolAction_SetPressed` = `(ToolAction_SWIBase + 8)`
- `ToolAction_GetPressed` = `(ToolAction_SWIBase + 9)`
- `ToolAction_Selected` = `(ToolAction_SWIBase + 0)`
- `ToolAction_Selected_Adjust` = `(1<<0)`
- `ToolAction_Selected_Select` = `(1<<2)`
- `ToolAction_SetIdent_Off` = `(0<<0)`
- `ToolAction_SetIdent_On` = `(1<<0)`
- `ToolAction_SetIdent_Fade` = `(2<<0)`
- `ToolAction_SetIdent_Mask` = `(15<<0)`
