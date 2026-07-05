# Visual Design

## Use this reference for

- Application and file icons
- Desktop harmony
- Colour usage
- Sound usage

## Icon rules

- Make application icons attractive, intelligible, and harmonious with the rest of the desktop.
- Use irregular outlines for application and device icons on the icon bar.
- Use square file icons with the standard border treatment.
- Provide separate large and small icon artwork; do not rely on scaling large icons down.
- Provide icons for the supported screen-resolution variants, including high-resolution modes where appropriate.
- Load the application by double-clicking its icon in a directory display and install the icon bar icon as part of startup.

## Colour rules

- Never assume the default palette is active.
- Read and use the current palette and cope with palette changes while running.
- Make the design work acceptably in monochrome or greyscale as well as colour.
- Use colour to clarify meaning, not as decoration that obscures structure.
- Avoid using blue for information that must stand out strongly.
- Keep pointers legible against their background.
- Reverse foreground and background for highlighted text.
- Use standard desktop colours outside the work area so windows, menus, and dialogues remain consistent with other applications.

## Sound rules

- Use sound sparingly and only when it adds meaning.
- Avoid harsh or startling sounds.
- Prefer distinct voices over arbitrary pitch changes when you need to differentiate sounds.
- Allow users to turn application sound off.
- Respect global system sound settings and direct users to system configuration for overall volume control.
- Never disable system sound globally on the user's behalf.

## 3D look and feel

- Treat the guide's 3D dialogue and window styling as the expected direction for new applications.
- Use standard Wimp-pool icons for standard controls rather than custom replacements.

## Standard control presentation

- Avoid raised outdented borders for ordinary controls.
- Avoid ridge borders in new work.
- Use channel borders only for grouping; they should not carry text, sprite content, or filled backgrounds.
- Treat indented bordered display fields as filled, horizontally centred, and vertically centred, without right justification.
- Treat action and default buttons as filled, horizontally centred, vertically centred `Click` buttons with grey `1` background and black foreground.
- Treat confirmation buttons exactly like the standard button family in colour and border style; do not highlight them with non-standard fills.
- Treat writable fields as filled bordered controls with white background, black foreground, and both horizontal and vertical centring.
- Use the standard pointer names for validation strings: `ptr_write` for writable fields and `ptr_menu` for menu buttons. Any pointer sprite named by validation should use a `ptr_` prefix.

## Standard sprite/button patterns

- Radio buttons should use `radiooff,radioon`, button type `Radio`, a non-zero ESG, no fill, no border, vertical centring, and visible label text.
- Option buttons should use `optoff,opton`, button type `Radio`, ESG `0`, no fill, no border, vertical centring, and visible label text.
- Tick controls should normally use the standard tick sprites, ESG `0`, no fill, no border, vertical centring, and visible label text.
- Menu buttons should use `gright,pgright` or `grightc,pgrightc`, button type `Click`, and a hidden action-border style rather than a visible custom border.
- Single-arrow adjusters should use `up,pup`, `down,pdown`, `left,pleft`, or `right,pright`, with button type `Repeat` and hidden action-border styling.
- Divider icons should use the standard `divider` sprite, be vertically centred, and not be filled, bordered, horizontally centred, or right justified.

## Validation-string cautions

- Avoid `B` validation in new templates; it exists for older interface-border behaviour.
- Do not use `X` validation on windowed icons.
- Use `D` validation only on writable fields.
- Treat `L` multi-line validation on writable fields as undefined, and use values above `32` where multi-line counts are supplied.
- Use `K` key-notification validation only on writable fields.
