# Toolbox Application Structure

Use this reference when the task is about the overall shape of a Toolbox application rather than one specific class.

This is the useful middle ground between the core API notes and a single worked example:

- how to declare message and event interest
- how to create and link objects at startup
- when to fetch underlying Wimp handles
- how to mix Toolbox handlers with Wimp and null-event work
- how to apply runtime UI state without dropping through to raw Wimp unnecessarily

## Startup Sequence

A practical Toolbox task startup order is:

1. Build the Wimp-message and Toolbox-event arrays first.
2. Call `toolbox_initialise`.
3. Call `event_initialise` with the shared `IdBlock`.
4. Set the poll mask explicitly if the task needs null events or wants to suppress specific raw Wimp events.
5. Create the initial objects by template name.
6. Fetch underlying Wimp handles only for the objects that must participate in raw Wimp protocols.
7. Link menus, submenus, or click-show relationships.
8. Register Wimp message handlers, raw Wimp event handlers, and Toolbox handlers.
9. Apply runtime state such as version text, menu ticks, or iconbar sprite changes.

Two important constraints:

- The Toolbox event list passed to `toolbox_initialise` is a delivery filter. If an event code is missing there, registering a handler later is not enough.
- `toolbox_create_object` takes template names, not class names. Keep those names stable and documented.

## Object Wiring Pattern

A small or medium Toolbox application often creates a set such as:

- one `Iconbar` object for entry and background presence
- one shared `Menu`
- one shared `ProgInfo` or `Quit` dialogue
- one or more `Window` objects, including auxiliary windows such as toolbars, palettes, or transient display windows

Useful wiring patterns are:

- `iconbar_set_menu` to attach the root iconbar menu
- `menu_set_sub_menu_show` to attach a submenu or standard dialogue from a menu entry
- class-specific setters such as `proginfo_set_version`, `iconbar_set_sprite`, or `menu_set_tick` for runtime state

Prefer those object-level links over manual `Toolbox_ShowObject` calls when the relationship is static.

## Wimp Bridging

A Toolbox task is still a Wimp task, so selective bridging is normal.

Fetch the underlying Wimp handle with `window_get_wimp_handle` only when code genuinely needs it, for example:

- excluding one of the application's own windows from a raw pointer or help path
- reading visible area or scroll state through `Wimp_GetWindowState`
- satisfying a Wimp-only message or event protocol
- opening or positioning a Toolbox-backed window through a raw Wimp protocol after Toolbox-managed state such as extent or content has been updated

Do not use raw Wimp handles as the main identity of a Toolbox object. Keep the `ObjectId` as the authoritative handle and bridge down only for the specific operation.

If only two or three objects need raw-handle access, fetch handles only for those objects. Do not turn every Toolbox object into a shadow Wimp identity just because a small part of the feature needs bridging.

## Event Registration Pattern

A useful split is:

- Wimp message handlers for protocol traffic such as `ModeChange`, `Quit`, file transfer, or help messages
- raw Wimp event handlers for null events or special low-level cases
- Toolbox handlers for semantic UI events such as `Menu_Selection` or `Iconbar_Clicked`

That lets the application stay mostly Toolbox-driven while still handling system protocols correctly.

This mixed model is especially useful when the task is semantically Toolbox-led but still has a background behaviour such as hover tracking, delayed dismissal, or retry/fallback logic that naturally belongs in the raw poll stream.

When a task mixes the event library with Toolbox:

- keep one shared `IdBlock`
- expect meaningful object/component context only on Toolbox events
- do not assume Wimp messages refresh the id block for you

## Null Events And Background Work

Toolbox tasks can still use null events for background or hover-driven behaviour.

Typical uses are:

- pointer-still timers
- periodic housekeeping
- delayed UI dismissal
- poll-time fallbacks when another task does not answer a message

Only request `Wimp_Poll_NullMask` when the task really needs it. If the feature is user-toggleable, changing the poll mask at runtime is a reasonable pattern.

For hover-driven features, a good default is:

- sample pointer position on null polls
- accumulate “still” time only while the pointer remains within a movement tolerance
- trigger the expensive action only after that dwell threshold is exceeded
- clear the transient UI again when the pointer moves away or the feature times out

That avoids flooding the desktop with requests while keeping the UI responsive.

## Runtime UI Updates

Prefer class or gadget veneers for live UI changes:

- `iconbar_set_sprite` instead of poking the iconbar icon directly
- `menu_set_tick` or `menu_set_fade` instead of mutating raw menu blocks
- `window_set_extent` and `gadget_move_gadget` instead of rewriting gadget-owned Wimp icons
- `proginfo_set_version` or similar class setters for standard dialogues

This keeps Toolbox-managed state, redraw, and help behaviour coherent.

If a background feature can be suspended, update its visible state and event activity together. A solid pattern is:

- change the user-visible affordance such as iconbar sprite, menu tick, or faded state
- update any internal enabled flag
- add or remove `Wimp_Poll_NullMask` or similar raw-event interest to match

That keeps the runtime behaviour aligned with what the UI claims.

## Interactive Help Placement

For Toolbox-based help:

- set object-wide help on `Window`, `Iconbar`, or `Menu` objects for generic context
- set gadget or menu-entry help where the action needs more specific guidance
- let the Toolbox answer normal `HelpRequest` traffic automatically

If you need help for raw Wimp-only areas such as window furniture or other non-gadget icons, handle that in the Wimp help path rather than trying to force it through gadget APIs.
