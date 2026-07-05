# Implementation Details

## Contents

- Legal operations
- Responsiveness
- Measurements
- Sprite metrics
- Window, menu, and dialogue geometry

## Use this reference for

- Low-level UI implementation choices
- Geometry and sizing rules
- Sprite metrics
- Performance-sensitive redraw work

## Legal operations

- Use published OS interfaces rather than touching hardware or undocumented memory directly.
- Do not bypass the operating system to access devices or system state.
- Keep implementation choices forward-compatible with later machines and OS revisions.

## Responsiveness

- Make redraw fast.
- Use the clipping rectangle supplied by the Wimp.
- Avoid unnecessary redraw work, especially for dialogue boxes and static UI.
- Keep interaction responsive enough that the application feels co-operative inside a multi-tasking desktop.

## Measurement model

- Work in OS units rather than pixels whenever practical.
- Design templates in a standard low-resolution mode, then verify them in high-resolution modes as well.
- Allow for screen-mode variation rather than assuming a single geometry.
- For dialogue layout, measure content placement from the visible work area rather than from the outer screen coordinates or title bar.
- Keep a minimum clearance of `12` OS units between controls and the visible window edge.
- Keep ordinary control-to-control spacing at `8` OS units.
- Treat alignment that is within `8` OS units of exact alignment as a layout fault to correct, not as acceptable variation.

## Sprite metrics

- Use compact sprite formats where possible.
- Supply transparency masks for irregular outlines.
- A large icon must be `68` OS units high.
- A small icon must be `34` OS units high.
- Keep file-icon borders at `4` OS units for large icons and `2` OS units for small icons.
- Position icon bar icons with text `16` OS units below the icon bar work-area origin.
- Use large-icon-sized sprites for iconised windows.

## Window geometry

- Centre the first application window horizontally and vertically on screen.
- Keep the first window to no more than roughly a quarter of the screen.
- Use the standard title and background colour combinations for focused and unfocused windows.
- Prefer `New Format` windows.
- Do not set `RealColours` on ordinary desktop windows.
- If a window has both horizontal and vertical scroll bars, also provide the resize icon.
- Do not provide a resize icon on its own; pair it with at least one scroll bar.
- If a window has title and resize icons, also provide the toggle icon.
- If a window has a close icon, also provide the back icon.
- Do not set both foreground and background stacking bits together.
- Keep titles free of leading spaces, trailing spaces, and trailing colons.
- Aim for a width:height or height:width ratio near `1.414` with roughly `25%` tolerance either side.
- Keep a dialogue-sized window within about `800 x 600` OS units unless the task clearly requires more.

## Control geometry

- Use these concrete control heights when building classic 3D templates:
- `44` OS units for option, radio, and tick controls.
- `40` OS units for labels, with taller labels acceptable only when needed to align with adjacent controls.
- `52` OS units for display icons and ordinary writable fields.
- `68` OS units for sunk writable fields and default-action buttons.
- `44` OS units for menu buttons.
- `32` OS units for single-arrow adjusters.
- `16` OS units for horizontal dividers.
- Size text-bearing controls on a `16` OS unit text grid.
- Use these minimum width bases before adding `16` OS units per text character:
- Action button base `12`.
- Default button base `28`.
- Display icon base `0`.
- Writable field base `8`.
- Sunk writable field base `16`.
- Menu button base `44`.
- Adjuster base `32`.
- For action buttons, a good default width is `188` OS units and a common secondary width is `140`.
- For default buttons, a good default width is `204` OS units and a common secondary width is `156`.
- Treat action-button widths below `108` or above `364` as out of family.
- Treat default-button widths below `124` or above `380` as out of family.
- Make dividers at least as wide as the visible window and align their left edge with the visible left edge.

## Menu geometry

- Make each menu item `44` OS units high.
- Keep submenus as narrow as practical.
- Open menus with the standard pointer offset and positioning expected by the Wimp model.

## Dialogue geometry

- Build dialogues to the standard 3D visual model.
- Use the standard control spacing, grouping, and button placement described by the guide.
- For a simple stacked dialogue, balance the upper and lower content clearances within the visible work area instead of leaving a large surplus gap above the first row.
- When a default button row is separated by a divider, keep the last content row `12` OS units above the divider in the generic case, but preserve captured family spacing when a known standard template intentionally uses a different balance.
- Validate templates in more than one screen mode before treating them as finished.
