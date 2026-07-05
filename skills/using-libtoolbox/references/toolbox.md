# `toolbox`

Installed header: `/riscos-resources/Export/Export/Lib/tboxlibs/h/toolbox`

Category: `core`

Purpose: SWI veneers to the SWI's provided by the toolbox core module

Use it when: Read first for Toolbox object ids, resource file structures, core SWIs, and generic event/layout types.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/toolintro.html

## Includes

- `kernel.h`
- `wimp.h`

## Main Types

- `ObjectId`
- `ComponentId`
- `ObjectClass`
- `IdBlock`
- `MessagesFD`
- `ObjectTemplateHeader`
- `StringReference`
- `MessageReference`
- `Relocation`
- `RelocationTable`
- `ResourceFileHeader`
- `ResourceFileObjectTemplateHeader`
- `EventInterest`
- `TopLeft`
- `ToolboxEventHeader`
- `ToolboxEvent`
- `ToolboxMsgEvent`
- `ToolboxErrorEvent`
- `ToolboxObjectAutoCreatedEvent`
- `ToolboxObjectDeletedEvent`
- `ToolboxTimerEvent`

## Public Functions

- `toolbox_get_sys_info`: returns information about a task
  Prototype: `extern _kernel_oserror *toolbox_get_sys_info ( unsigned int reason_code, _kernel_swi_regs *regs );`
- `toolbox_get_template_name`: gets the name of the specified object
  Prototype: `extern _kernel_oserror *toolbox_get_template_name ( unsigned int flags, ObjectId id, char *buffer, int buff_size, int *nbytes );`
- `toolbox_create_object`: creates a named object
  Prototype: `extern _kernel_oserror *toolbox_create_object ( unsigned int flags, void *name_or_template, ObjectId *id );`
- `toolbox_delete_object`: deletes a specified object
  Prototype: `extern _kernel_oserror *toolbox_delete_object ( unsigned int flags, ObjectId id );`
- `toolbox_show_object`: shows the specified object
  Prototype: `extern _kernel_oserror *toolbox_show_object ( unsigned int flags, ObjectId id, int show_type, void *type, ObjectId parent, ComponentId parent_component );`
- `toolbox_hide_object`: hides a specified object
  Prototype: `extern _kernel_oserror *toolbox_hide_object ( unsigned int flags, ObjectId id );`
- `toolbox_get_object_state`: gets information for a specified object
  Prototype: `extern _kernel_oserror *toolbox_get_object_state ( unsigned int flags, ObjectId id, unsigned int *state );`
- `toolbox_set_client_handle`: sets a client handle for the specified object
  Prototype: `extern _kernel_oserror *toolbox_set_client_handle ( unsigned int flags, ObjectId id, void *client_handle );`
- `toolbox_get_client_handle`: gets a client handle from the specified object
  Prototype: `extern _kernel_oserror *toolbox_get_client_handle ( unsigned int flags, ObjectId id, void **client_handle );`
- `toolbox_get_object_class`: gets the class for the specified object
  Prototype: `extern _kernel_oserror *toolbox_get_object_class ( unsigned int flags, ObjectId id, ObjectClass *object_class );`
- `toolbox_get_parent`: gets the parent object and component id for the object
  Prototype: `extern _kernel_oserror *toolbox_get_parent ( unsigned int flags, ObjectId id, ObjectId *parent, ComponentId *parent_component );`
- `toolbox_get_ancestor`: gets the ancestor object and component id for the object
  Prototype: `extern _kernel_oserror *toolbox_get_ancestor ( unsigned int flags, ObjectId id, ObjectId *ancestor, ComponentId *ancestor_component );`
- `toolbox_raise_toolbox_event`: raises a specific event for a specific object/component
  Prototype: `extern _kernel_oserror *toolbox_raise_toolbox_event ( unsigned int flags, ObjectId id, ComponentId component, ToolboxEvent *event );`
- `toolbox_initialise`: called by client when initialising the application
  Prototype: `extern _kernel_oserror *toolbox_initialise ( unsigned int flags, int wimp_version, int *wimp_messages, int *toolbox_events, char *directory, MessagesFD *mfd, IdBlock *idb, int *current_wimp_version, int *task, void **sprite_area );`
- `toolbox_load_resources`: loads the resources file
  Prototype: `extern _kernel_oserror *toolbox_load_resources ( unsigned int flags, char *resources );`

## Public Constants And Method Codes

- `NULL_ObjectId` = `(ObjectId)0`
- `NULL_ComponentId` = `(ComponentId)-1`
- `BOOL` = `int`
- `TRUE` = `1`
- `FALSE` = `0`
- `NULL` = `0`
- `MAX_OBJECT_NAME` = `12`
- `Object_CreateOnLoad` = `0x00000001`
- `Object_ShowOnCreate` = `0x00000002`
- `Object_Shared` = `0x00000004`
- `Object_Ancestor` = `0x00000008`
- `Relocate_StringReference` = `1`
- `Relocate_MsgReference` = `2`
- `Relocate_SpriteAreaReference` = `3`
- `Relocate_ObjectOffset` = `4`
- `Toolbox_SWIChunkBase` = `0x44ec0`
- `Toolbox_CreateObject` = `(Toolbox_SWIChunkBase + 0)`
- `Toolbox_DeleteObject` = `(Toolbox_SWIChunkBase + 1)`
- `Toolbox_ShowObject` = `(Toolbox_SWIChunkBase + 3)`
- `Toolbox_HideObject` = `(Toolbox_SWIChunkBase + 4)`
- `Toolbox_GetObjectState` = `(Toolbox_SWIChunkBase + 5)`
- `Toolbox_ObjectMiscOp` = `(Toolbox_SWIChunkBase + 6)`
- `Toolbox_SetClientHandle` = `(Toolbox_SWIChunkBase + 7)`
- `Toolbox_GetClientHandle` = `(Toolbox_SWIChunkBase + 8)`
- `Toolbox_GetObjectClass` = `(Toolbox_SWIChunkBase + 9)`
- `Toolbox_GetParent` = `(Toolbox_SWIChunkBase + 10)`
- `Toolbox_GetAncestor` = `(Toolbox_SWIChunkBase + 11)`
- `Toolbox_GetTemplateName` = `(Toolbox_SWIChunkBase + 12)`
- `Toolbox_RaiseToolboxEvent` = `(Toolbox_SWIChunkBase + 13)`
- `Toolbox_GetSysInfo` = `(Toolbox_SWIChunkBase + 14)`
- `Toolbox_Initialise` = `(Toolbox_SWIChunkBase + 15)`
- `Toolbox_LoadResources` = `(Toolbox_SWIChunkBase + 16)`
- `Toolbox_TimerOp` = `(Toolbox_SWIChunkBase + 56)`
- `Toolbox_Memory` = `(Toolbox_SWIChunkBase + 57)`
- `Toolbox_DeRegisterObjectModule` = `(Toolbox_SWIChunkBase + 58)`
- `Toolbox_TemplateLookUp` = `(Toolbox_SWIChunkBase + 59)`
- `Toolbox_GetInternalHandle` = `(Toolbox_SWIChunkBase + 60)`
- `Toolbox_RegisterObjectModule` = `(Toolbox_SWIChunkBase + 61)`
- `Toolbox_RegisterPreFilter` = `(Toolbox_SWIChunkBase + 62)`
- `Toolbox_RegisterPostFilter` = `(Toolbox_SWIChunkBase + 63)`
- `Toolbox_GetSysInfo_TaskName` = `0`
- `Toolbox_GetSysInfo_MessagesFD` = `1`
- `Toolbox_GetSysInfo_DirName` = `2`
- `Toolbox_GetSysInfo_TaskHandle` = `3`
- `Toolbox_GetSysInfo_SpriteArea` = `4`
- `Toolbox_CreateObject_InCore` = `0x00000001`
- `Toolbox_DeleteObject_DontRecurse` = `0x00000001`
- `Toolbox_CopyObject_DontRecurse` = `0x00000001`
- `Toolbox_GetObjectState_Showing` = `0x00000001`
- `Toolbox_RegisterPreFilter_Remove` = `0x00000001`
- `Toolbox_RegisterPostFilter_Remove` = `0x00000001`
- `Toolbox_RegisterPostFilter_WimpEvent` = `1`
- `Toolbox_RegisterPostFilter_WimpMessage` = `2`
- `Toolbox_RegisterPostFilter_ToolboxEvent` = `3`
- `Toolbox_RegisterPostFilter_AnyClass` = `(-1)`
- `Toolbox_RegisterPostFilter_WimpObject` = `0`
- `Toolbox_ShowObject_AsMenu` = `0x00000001`
- `Toolbox_ShowObject_AsSubMenu` = `0x00000002`
- `Toolbox_ShowObject_AsSubWindow` = `0x00000004`
- `Toolbox_ShowObject_Default` = `0`
- `Toolbox_ShowObject_FullSpec` = `1`
- `Toolbox_ShowObject_TopLeft` = `2`
- `Toolbox_ShowObject_Centre` = `3`
- `Toolbox_ShowObject_AtPointer` = `4`
- `Toolbox_Memory_ValidReasonBits` = `0xFF`
- `Toolbox_Memory_Alloc` = `0x00`
- `Toolbox_Memory_Free` = `0x01`
- `Toolbox_Memory_Reallocate` = `0x02`
- `Toolbox_TimerOp_After` = `0x00`
- `Toolbox_TimerOp_Every` = `0x01`
- `Toolbox_TimerOp_Remove` = `0x02`
- `Toolbox_TimerOp_Poll` = `0x03 /* Internal use only */`
- `Toolbox_Error` = `(Toolbox_SWIChunkBase + 0)`
- `Toolbox_ObjectAutoCreated` = `(Toolbox_SWIChunkBase + 1)`
- `Toolbox_ObjectDeleted` = `(Toolbox_SWIChunkBase + 2)`
- `Toolbox_Timer` = `(Toolbox_SWIChunkBase + 3)`
- `ToolboxObjectDeleted_ExtendedInformation` = `0x00000001`
