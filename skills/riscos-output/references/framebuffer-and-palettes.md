# Framebuffer and palettes

## Direct screen buffer access

When code reads or writes screen memory directly, treat it as a lower-level
driver path, not as normal graphics output.

* Use `OS_ReadVduVariables` to discover the current screen geometry and memory
  layout. The useful variables commonly include the graphics window bounds,
  screen base address, line length, and eig factors.
* Remove cursors before direct framebuffer reads or writes, and restore them
  afterwards. Otherwise text or pointer cursors may be captured into saved
  image data or corrupted by screen writes.
* This cursor remove/restore is only needed for direct screen-buffer
  manipulation. It is not a general requirement for high-level plotting
  through `OS_SpriteOp`, `OS_Plot`, Font, or Draw operations.
* If the code changes screen mode before continuing with direct screen access,
  remove cursors again after the mode change.
* Windowed screen capture and restore can still be represented as sprites:
  copy full words per row from screen memory, and describe the exact pixel
  bounds with the sprite `lbit` and `rbit` fields.

## VideoV pointer operations

VideoV pointer driver calls are not covered by the public PRM. When
implementing or translating code that uses `VideoV_Pointer_*`, check the
PRM-in-XML staging documentation before assuming the register contract:
https://gerph.github.io/riscos-prminxml-staging/prm/html/select/graphics/videov.html

In particular:

* `VideoV_Pointer_Update` uses `R0 = pointer height`, `R1 = y`, `R2 = x`, and
  `R3 = screen height`.
* `VideoV_Pointer_Remove` uses `R3 = screen height`.

## Screen palettes

* If a screen image is saved as a sprite in a paletted mode, preserve the
  palette block alongside the image data.
* When restoring a paletted screen image, apply the palette before copying the
  pixel data into the framebuffer.
* Screen palette restoration uses palette-programming interfaces such as
  `OS_Word 12`; this is separate from sprite plotting translation tables.
* If you are emitting `VDU 19` palette programming sequences, write them via
  `OS_WriteC` or `OS_WriteN`. Do not treat them as `OS_Byte` calls.
