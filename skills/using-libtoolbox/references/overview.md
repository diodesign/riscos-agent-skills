# Toolbox Overview

Use this skill for code that works with the Toolbox veneer headers installed in:

- `/riscos-resources/Export/Lib/tboxlibs/h/`
- `/riscos-resources/Export/Export/Lib/tboxlibs/h/toolbox`

Use the public Toolbox manual at:

- `http://www.riscos.com/support/developers/toolbox/index.html`

That manual is the behavioural reference for the standard Toolbox classes. The installed headers are the concrete API reference for types, method numbers, events, flags, and veneer function names.

## Working Model

A Toolbox application is still a Wimp task, but it is intended to operate mostly through Toolbox objects, Toolbox events, and resource-file templates rather than constructing the UI procedurally with raw Wimp calls.

Normal flow:

1. Call `Toolbox_Initialise`.
2. Let the Toolbox load `res`, `Sprites*`, and `Messages`.
3. Create or auto-create objects from resource templates.
4. Show and hide objects with Toolbox SWIs.
5. Handle Toolbox events from `Wimp_Poll`, using the id block to recover ancestor, parent, object, and component context.
6. Drop to Wimp-level APIs only when you need raw window handles, redraw rectangles, icon handles, or low-level message handling.

## Important Core Ideas

- Treat the resource file as the primary UI definition.
- Treat an `ObjectId` as opaque runtime identity.
- Treat a `ComponentId` as the stable identity of a gadget or menu entry inside an object.
- Use `Toolbox_SetClientHandle` and `Toolbox_GetClientHandle` for per-document or per-view state.
- Use `AboutToBeShown` events to populate dynamic menus and dialogues immediately before display.
- Expect many standard classes to expose the underlying `Window` object, but do not bypass the Toolbox unless there is a clear reason.

## What To Read Next

- Read [core-toolbox.md](./core-toolbox.md) first for core SWIs, object relationships, resource files, and event flow.
- Read [simple-application.md](./simple-application.md) when you need a compact end-to-end example of a Toolbox task built around an iconbar object and attached menu.
- Read [application-structure.md](./application-structure.md) when you need generic Toolbox task structure, object wiring, event registration, null-event work, or runtime UI state updates without depending on one specific application shape.
- Read [header-map.md](./header-map.md) next to select the right header reference.
- Read [dialogues-and-menus.md](./dialogues-and-menus.md) for the standard dialogue, menu, and iconbar classes.
- Read [windows-and-gadgets.md](./windows-and-gadgets.md) for `window`, `gadgets`, toolbars, Wimp bridging, and DrawFile redraw work.
- Read [extensions.md](./extensions.md) for the non-core gadget and object modules that are present in `tboxlibs` but are not part of the classic Toolbox manual chapters.
