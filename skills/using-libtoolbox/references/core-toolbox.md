# Core Toolbox

Primary sources:

- Header: `/riscos-resources/Export/Export/Lib/tboxlibs/h/toolbox`
- Manual: `http://www.riscos.com/support/developers/toolbox/toolintro.html`
- Examples: `http://www.riscos.com/support/developers/toolbox/toolboxexamples.html`
- Resource format: `http://www.riscos.com/support/developers/toolbox/resourcefilefmts.html`
- ResEd: `http://www.riscos.com/support/developers/toolbox/reseditor.html`
- ResTest: `http://www.riscos.com/support/developers/toolbox/restest.html`
- RISC OS 3.10 support: `http://www.riscos.com/support/developers/toolbox/support310.html`

## Core SWIs To Recognise

- `Toolbox_Initialise`: register as a Toolbox task, load resources, and obtain the per-poll id block.
- `Toolbox_LoadResources`: load extra resource files after startup.
- `Toolbox_CreateObject` and `Toolbox_DeleteObject`: create and destroy runtime instances from templates.
- `Toolbox_ShowObject` and `Toolbox_HideObject`: show and hide objects with Toolbox-managed context.
- `Toolbox_ObjectMiscOp`: dispatch class-specific methods.
- `Toolbox_SetClientHandle` and `Toolbox_GetClientHandle`: attach application state to objects.
- `Toolbox_GetObjectClass`, `Toolbox_GetParent`, `Toolbox_GetAncestor`, and `Toolbox_GetTemplateName`: inspect relationships and origin.
- `Toolbox_RaiseToolboxEvent`: raise custom Toolbox events when the application needs them.

Important clarifications:

- `toolbox_create_object` takes a template name or in-core template pointer, not a Toolbox class name. A template called `Window` may happen to be a `Window` object, but that name match is incidental.
- The Toolbox event list passed to `toolbox_initialise` is a delivery filter. If an event code is omitted there, registering a handler for it later will not make it arrive.

## Event Model

- Toolbox events arrive through `Wimp_Poll` as `Wimp_ToolboxEvent`.
- The id block filled by the Toolbox carries:
  - ancestor object/component
  - parent object/component
  - object/component that actually raised the event
- Use the id block to map a click or selection back to the current document, window, or control.
- Wimp messages do not normally refresh the id block, so do not assume message handling has current object context.
- Underlying Wimp events are not all delivered unchanged. Auto-open windows can suppress `OpenWindowRequest`, auto-close windows can suppress `CloseWindowRequest`, and some object modules consume low-level Wimp traffic on the application's behalf.

## Object Relationships

- Attached objects are created and shown in relation to another object.
- Shared objects are reused across multiple creates and are reference-counted.
- Parent identifies what caused another object to be shown.
- Ancestor carries a higher-level application context, which is important in multi-document trees.
- When showing an object manually, provide the correct parent object and component ids so later events can be routed sensibly.
- Auto-shown objects appear in their default place with no parent, so code must not assume meaningful parent or ancestor context for them.
- Sharedness propagates to attached objects.
- Parent and ancestor context are especially important when one shared object services multiple commands. In `SaveAs` and similar attached-object flows, `id_block->parent_component` can be the only reliable way to recover which menu entry or gadget launched the object.

## Resource Files

Toolbox resource files are binary object-template files, not classic Wimp template files.

Important structures are defined in the core `toolbox` header:

- `ObjectTemplateHeader`
- `ResourceFileHeader`
- `ResourceFileObjectTemplateHeader`
- `Relocation` and `RelocationTable`

Important practical points:

- Template names are limited to 12 bytes including the terminator.
- Strings passed into many Toolbox veneers are control-terminated; strings returned in buffers or event blocks are usually NUL-terminated.
- Buffer lengths include the terminator. If a supplied buffer is too short, the string is truncated without an error, so callers must check the returned required length.
- Resource-file message text and the application `Messages` file are separate mechanisms.
- Keep undefined flag bits clear on Toolbox SWIs and methods.
- `ObjectId` values are opaque. Window component ids above `0x7FFFFF` and menu component ids above `0xFFFFFFFD` are reserved for Toolbox internals. `0xFFFFFFFF` means “no component”.

## Practical Guidance

- Prefer templates and object methods over procedural UI construction.
- Use `AboutToBeShown` handlers for late binding and dynamic state refresh.
- Use shared objects when multiple views need the same menu or dialogue.
- Use ResEd to inspect or create templates and ResTest to exercise auto-created objects and inspect event payloads quickly.
- Treat `Toolbox_ShowObject` as potentially asynchronous. If an object warns before show, the visible result may happen after a later `Wimp_Poll`, and failures may arrive as `Toolbox_Error` events rather than a direct SWI error.
- Prefer event-code-driven handlers over hard-wiring logic to menu positions or specific UI placements.
- Use client handles aggressively for per-document or per-view state, especially in multi-document applications.
- If runtime gadgets are needed, prefer extracting a gadget template from a resource-defined window rather than constructing large gadget blocks by hand.
- Keep keyboard shortcuts in the resource file where possible instead of implementing bespoke key handling.
- When showing subwindows or menus programmatically, remember that placement is split between `flags` and `show_type`: for example `Toolbox_ShowObject_AsSubWindow` in `flags`, with a full `WindowShowObjectBlock` passed via `show_type`/`type`.

## ResEd And ResTest Notes

- The generic object flags that matter most are auto-create, auto-show, shared, and ancestor.
- Object names may be auto-disambiguated on copy or import.
- Help text buffer sizes matter. If text will change at runtime, reserve more space than the exact initial length.
- Turning help off removes it. Leaving help enabled with an empty string can blank the interactive help display for that object.
- Exported messages are only safe to re-import if object names, gadget structure, and generated tags have not been altered.
- ResTest is useful for validating event codes, id-block contents, auto-created attached objects, and transient versus persistent show behaviour before writing much code.

## Compatibility

- On RISC OS 3.10, Toolbox applications are affected by missing native 3D icons, inconsistent fading, and a crash risk if a window is deleted while a slabbed button is pressed.
- The `ThreeTen` support module mitigates these issues and is auto-loaded by the Window module on RISC OS 3.10.
