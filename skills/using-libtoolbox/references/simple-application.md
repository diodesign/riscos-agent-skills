# Toolbox Application Patterns

This reference captures a practical Toolbox application shape for a medium-sized single-window application. It is not the smallest possible Toolbox task, but it is a good general-purpose pattern for an application that mixes Toolbox objects, standard dialogues, extension gadgets, and a controlled amount of raw Wimp work.

Use this reference when you need a compact end-to-end structure for an application that:

- starts as a Toolbox task
- creates one or more windows by template name
- uses Toolbox gadgets and standard dialogue classes
- still drops to raw Wimp for messages, geometry, or caret policy

## Typical Object Set

A common arrangement is to create several objects by template name:

- `Window` as the main viewer window
- `Toolbar` as a subwindow-style control strip
- `Options` as the options dialogue/window

An application of this shape often also relies on:

- an attached menu for context-sensitive commands
- a shared `SaveAs` object for standard save/export protocol
- one or more extension gadgets inside the main window

## General Application Shape

This shape follows a repeatable structure that scales beyond tiny iconbar utilities:

1. Call `toolbox_initialise` with the Wimp messages and Toolbox events the task wants delivered.
2. Initialise the event library with the shared `IdBlock`.
3. Register message handlers first, then Toolbox and Wimp UI handlers.
4. Create the root objects by template name.
5. Show the main object, then show any subordinate object such as a toolbar with explicit Toolbox show context.
6. Enter an `event_poll` loop.

Important points:

- `toolbox_initialise` replaces a direct `Wimp_Initialise`.
- The Toolbox event list is a filter as well as documentation of intent.
- The `IdBlock` is central when shared menus and dialogues need to know which control launched them.
- A Toolbox application can still receive and handle plain Wimp messages such as `DataOpen`, `DataLoad`, `ModeChange`, `WindowInfo`, and `Quit`.

## Startup Pattern

This is a practical event-interest declaration:

```c
static int main_initialise(void)
{
    static int mess_wanted[] = {
                                Wimp_MDataLoad,
                                Wimp_MDataOpen,
                                Wimp_MWindowInfo,
                                Wimp_MModeChange,
                                Wimp_MQuit
                               };
    static int tbox_wanted[] = {Toolbox_Error,
                                ActionButton_Selected,
                                OptionButton_StateChanged,
                                StringSet_ValueChanged,
                                NumberRange_ValueChanged,
                                Window_HasBeenHidden,
                                Adjuster_Clicked,
                                Scale_ApplyFactor,
                                Scale_AboutToBeShown,
                                Scale_DialogueCompleted,
                                ImageFileGadget_MouseClick,
                                0x23,
                                Event_Next, Event_Previous,
                                Event_InternalNext, Event_InternalPrevious,
                                Event_CloseApp,
                                Event_UpdateMenu,
                                SaveAs_AboutToBeShown,
                                SaveAs_SaveToFile,
                                0};
    int task_handle;

    error_trap(toolbox_initialise(0, 430, mess_wanted, tbox_wanted,
                                  "<App$Dir>", &messages_desc, &idb,
                                  0, &task_handle, 0), 1);
    error_trap(event_initialise(&idb), 0);
    error_trap(event_set_mask(Wimp_Poll_NullMask), 0);
    return 1;
}
```

Useful lessons:

- list both Toolbox semantic events and custom event codes here
- include Wimp messages for file-open or iconise protocols even in a Toolbox-led UI
- use one shared `IdBlock` so later handlers can recover `self`, `parent`, and `ancestor` context

## Object Creation And Show Pattern

Create objects by template name, not by class constant:

```c
error_trap(toolbox_create_object(0, "MainWindow", &main_window), 1);
error_trap(toolbox_create_object(0, "Toolbar", &tool_window), 1);
error_trap(toolbox_create_object(0, "Options", &opts_window), 1);
```

That distinction matters. `toolbox_create_object` is looking up a template in the resource file; the template name only sometimes matches the class.

The main window is shown first, then the toolbar is attached as a subwindow with an explicit `WindowShowObjectBlock`:

```c
error_trap(toolbox_show_object(0, main_window,
                               Toolbox_ShowObject_Centre, buffer, 0, 0), 0);

error_trap(toolbox_show_object(Toolbox_ShowObject_AsSubWindow, tool_window, 1,
                               &pos, NULL_ObjectId, NULL_ComponentId), 1);
```

This is a good pattern when:

- the main document window should stay a normal Toolbox `Window`
- a secondary control strip should track it visually
- the application needs tighter positioning control than an attached menu or standard dialogue provides

## Mixed Toolbox/Wimp Layout Pattern

This is a useful pattern for when to bridge to raw Wimp without abandoning Toolbox:

- `window_get_wimp_handle` fetches the underlying Wimp handle
- `wimp_get_window_state` provides visible area and scroll positions
- `window_set_extent` updates the Toolbox window extent
- `gadget_move_gadget` repositions Toolbox gadgets after size changes
- raw `Wimp_EOpenWindow` and `Wimp_ECloseWindow` handlers are still used for custom open/close behaviour

Use this split when:

- Toolbox owns the object lifetime and semantic events
- Wimp geometry or message protocols still need low-level control
- direct icon poking would be more fragile than moving gadgets through the Toolbox veneer

## Shared Menu And SaveAs Pattern

For export or format-selection work, a generic dynamic-menu flow is:

1. Handle a menu refresh event before display.
2. Rebuild the menu entries for the current document state.
3. Let a menu entry show a shared `SaveAs` object.
4. In `SaveAs_AboutToBeShown`, use the id block parent context to configure filetype and default leafname.
5. In `SaveAs_SaveToFile`, use the same parent context to perform the actual export.
6. Call `saveas_file_save_completed` before the next poll.

The important generic detail is that a shared dialogue can be specialised entirely from the `IdBlock`:

- `id_block->self_id` is the `SaveAs` object
- `id_block->parent_component` identifies the launching menu entry

That pattern avoids duplicating one `SaveAs` object per export format.

## Extension Gadget Pattern

One useful extension-gadget pattern is to use `ImageFileGadget` as the central display surface:

- `imagefilegadget_set_value` hands the image buffer to the gadget
- `imagefilegadget_set_quality`, `imagefilegadget_set_index`, and `imagefilegadget_set_transform` adjust presentation
- `imagefilegadget_get_bounds` reports the rendered image bounds used for layout
- `imagefilegadget_get_scroll` and `imagefilegadget_set_scroll` preserve view position during extent changes
- `ImageFileGadget_MouseClick` is used to clear the caret so window-level key handling remains effective

This is a good model for extension gadgets in general: let the gadget own presentation semantics while the application keeps layout, document state, and surrounding window behaviour.

## Practical Rules

- Keep template structure authoritative and do runtime mutation only for state that genuinely depends on the current document or environment.
- Prefer semantic Toolbox events for gadgets and standard classes; use raw Wimp handlers only for messages and geometry-sensitive jobs.
- Treat shared dialogues and menus as context-sensitive objects driven by `IdBlock` parent/ancestor information.
- Preserve scroll state explicitly when resizing windows or moving display gadgets.
- Use template names consistently and document them; they are part of the application's UI contract even though they are not class identifiers.
