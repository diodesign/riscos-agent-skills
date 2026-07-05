# ImageFileRender

ImageFileRender is the generic image-file rendering API. Use it when the input
is a complete image file in memory and the caller should not need to know
whether the renderer underneath is JPEG, DrawFile, Sprite, PNG via conversion,
or a third-party filetype renderer.

Master documentation:
https://gerph.github.io/riscos-prminxml-staging/prm/html/select/graphics/imagefilerender.html

## Concepts

Every image has a bounding box and a resolution. Bitmaps usually have a box
based at the origin; vector formats such as DrawFiles may have a non-zero
origin. Use `FLAG_IGNORE_DOCUMENT_OFFSET` when the caller wants to treat the
image as if it starts at `(0,0)`.

Files may contain more than one logical image. Sequence number `0` means the
default image. Sequence number `1` means the first explicit image. `-1` is
commonly used by the headers as `SEQUENCE_LAST`.

Quality is encoded in bits 6-9 of the render flags. `0` requests the renderer's
default, `1` is lowest quality, and `15` is highest quality. The renderer's
registered flags limit and default the actual value passed to the renderer.

ImageFileRender clips to the normal graphics rectangle. Use `VDU 24` for a
plain screen program, or call from the Wimp redraw loop so the current redraw
rectangle constrains output.

## Constants

The usual C headers define these values:

```c
#define TRANSFORMTYPE_SIZE      (0 << 0)
#define TRANSFORMTYPE_SCALE     (1 << 0)
#define TRANSFORMTYPE_TRANSFORM (2 << 0)
#define FLAG_COLOURMAP          (1 << 3)
#define FLAG_IGNORE_DOCUMENT_OFFSET (1 << 4)
#define FLAG_RETURN_OSUNITS     (1 << 5)
#define FLAG_QUALITY_SHIFT      6
#define SEQUENCE_DEFAULT        0
#define SEQUENCE_LAST           (-1)
#define QUERY_BASEDETAILS       0
```

Transformation type occupies bits 0-2 in `R0`. Other reserved bits must be
clear.

## Transform Data

`TRANSFORMTYPE_SIZE` uses a 16-byte "to fit" block:

```c
struct ifr_tofit {
    int width;   /* OS units */
    int height;  /* OS units */
    int border;  /* OS units on all edges */
    int angle;   /* degrees as 16.16 fixed point */
};
```

This scales the image to fit the supplied rectangle. The document origin is
ignored for this mode.

`TRANSFORMTYPE_SCALE` uses a standard 16-byte RISC OS scale block:

```c
struct ifr_scale {
    int xmult;
    int ymult;
    int xdiv;
    int ydiv;
};
```

`TRANSFORMTYPE_TRANSFORM` uses a standard six-word transform matrix:

```c
struct ifr_transform {
    int m00; /* 16.16 */
    int m10; /* 16.16 */
    int m01; /* 16.16 */
    int m11; /* 16.16 */
    int m20; /* 24.8 */
    int m21; /* 24.8 */
};
```

The matrix is:

```text
{ m00, m01, 0 }
{ m10, m11, 0 }
{ m20, m21, 1 }
```

Not all renderers support arbitrary transforms. JPEG renderers, for example,
may support scaling but reject rotation or skew with `IFR_CantTransform`.

## Direct Rendering

Basic sequence for a screen or Wimp redraw renderer:

1. Load the file into memory.
2. Derive the filetype, normally from `(load_address >> 8) & &FFF`.
3. Set any graphics window or enter the Wimp redraw rectangle.
4. Fill the appropriate transform block.
5. Call `ImageFileRender_Render`.

Register use for `ImageFileRender_Render`:

| Register | Use |
|----------|-----|
| `R0` | Render flags |
| `R1` | Filetype |
| `R2` | Pointer to image data |
| `R3` | Image data length |
| `R4` | Pointer to extension data, or 0 |
| `R5` | Image sequence number |
| `R6` | X origin in OS units |
| `R7` | Y origin in OS units |
| `R8` | Pointer to transform data |
| `R9` | Pointer to colour map descriptor, or 0 |

Example C pattern for "fit this image into a box":

```c
struct ifr_tofit tofit;
_kernel_oserror *err;

tofit.width = bbox->x1 - bbox->x0;
tofit.height = bbox->y1 - bbox->y0;
tofit.border = border;
tofit.angle = 0;

err = _swix(ImageFileRender_Render, _INR(0, 8),
            TRANSFORMTYPE_SIZE |
                FLAG_IGNORE_DOCUMENT_OFFSET |
                (15 << FLAG_QUALITY_SHIFT),
            filetype,
            data,
            datalen,
            NULL,
            SEQUENCE_LAST,
            bbox->x0,
            bbox->y0,
            &tofit);
```

Example BASIC pattern:

```bbcbasic
SYS "OS_File",5,file$ TO obj%,,load%,,len%
type%=(load%>>8) AND &FFF
DIM file% len%
SYS "OS_File",255,file$,file%,0

DIM scale% 16
scale%!0=1:scale%!4=1:scale%!8=1:scale%!12=1

quality%=(15<<6)
SYS "ImageFileRender_Render",1 OR quality% OR (1<<4),type%,file%,len%,0,0,x%,y%,scale%,0
```

## Bounding Boxes and Layout

Use `ImageFileRender_BBox` when the caller needs the natural or transformed
size before drawing. Its input registers match `Render` except that `R6` points
to transform data and `R7` points to a four-word bounding box. Set
`FLAG_RETURN_OSUNITS` when layout code needs OS units; otherwise the box is in
Draw units.

Example:

```c
struct ifr_scale scale = { 1, 1, 1, 1 };
bbox_t box;

err = _swix(ImageFileRender_BBox, _INR(0, 7),
            TRANSFORMTYPE_SCALE |
                FLAG_IGNORE_DOCUMENT_OFFSET |
                FLAG_RETURN_OSUNITS,
            filetype,
            data,
            datalen,
            NULL,
            SEQUENCE_LAST,
            &scale,
            &box);
```

Use `ImageFileRender_Transform` when code needs the actual transform matrix
that ImageFileRender would use, for example to map mouse positions back into
image coordinates.

Use `ImageFileRender_Info` query `0` for base details. The 20-byte result block
contains sequence number, X DPI, Y DPI, colour type, and image flags. The low
bit of image flags says the image is solid across its whole bounding box.

## Colour Mapping and Extension Data

Set `FLAG_COLOURMAP` when `R9` points to a colour map descriptor:

```c
typedef struct colourmap_s {
    void *workspace;
    void (*function)(void);
} colourmap_t;
```

The function receives and returns mapped colours according to the common
SpriteExtend, DrawFile, and ColourTrans-style colour mapping convention.

Renderer-specific extension data is passed in `R4`. It must be word-aligned,
and the first word is the renderer magic value. For sprite files, the RISCOS Ltd
sprite extension magic is `&66990101`, followed by a sprite name of up to 12
characters. The named sprite is used only when the sequence is left as default.

## Registering a New Renderer

To add a new filetype, write an ImageFileRender renderer module and register it
with `ImageFileRender_Register`. Toolbox ImageFileGadget is only a client of
ImageFileRender; once a renderer is registered for a filetype, ImageFileGadget
can use that filetype through its normal `SetValue` method. For ImageFileGadget
application methods and events, use the `using-toolbox-imagefilegadget` skill.

Renderers normally register at module initialisation and when they receive
`Service_ImageFileRender_Started`. Deregister at finalisation and handle
`Service_ImageFileRender_Dying` by forgetting any cached assumption that the
service is available. `Service_ImageFileRender_RendererChanged` tells clients
that renderer details for a filetype have changed.

`ImageFileRender_Register` uses:

| Register | Use |
|----------|-----|
| `R0` | Flags, must be 0 |
| `R1` | Pointer to renderer definition block, or 0 to query API version |

The renderer definition block is copied by ImageFileRender:

| Offset | Field |
|--------|-------|
| 0 | API version, currently 102 |
| 4 | Renderer capability flags |
| 8 | Filetype |
| 12 | Magic value, or 0 |
| 16 | Pointer to name string, copied |
| 20 | Workspace value to pass in `R12` |
| 24 | `IFR_Start` entry, or 0 |
| 28 | `IFR_Stop` entry, or 0 |
| 32 | `IFR_Render` entry |
| 36 | `IFR_BBox` entry |
| 40 | `IFR_DeclareFonts` entry, or 0 |
| 44 | `IFR_Info` entry |

The renderer name string contains three tab-separated fields:

```text
<renderer name><tab><version x.xx><tab><author>
```

Capability flags:

| Bits | Meaning |
|------|---------|
| 0-1 | Transform capability: 0 = identity scale/translation only; 1 = translate and uniform scale; 2 = translate and independent X/Y scale; 3 = arbitrary transform |
| 2 | Supports colour mapping |
| 3 | Irregular shape; call renderer for transformed bounding boxes |
| 4-7 | Maximum quality level, 1-15 |
| 8-11 | Default quality level, 1-15, or 0 if ignored |

Deregister with:

| Register | Use |
|----------|-----|
| `R0` | Flags, must be 0 |
| `R1` | Filetype |
| `R2` | Pointer to the same name used at registration |
| `R3` | Matching magic value |

Use `*ImageFileRenderers`, `ImageFileRender_EnumerateRenderers`, or
`ImageFileRender_RendererInfo` to inspect active renderers while debugging.

## Renderer Entry Points

All renderer entries receive `R0 = API version * 100` and `R12 = workspace`
from the registration block. Errors are returned by setting V and returning an
error block pointer in `R0`.

`IFR_Start` receives an image descriptor in `R1`:

| Offset | Field |
|--------|-------|
| 0 | Pointer to data |
| 4 | Length |
| 8 | Pointer to extension data, or 0 |
| 12 | Sequence number |
| 16 | Private image data, initially 0 |

Use `IFR_Start` to validate the file and cache decoded state by storing a
pointer in the private word. `IFR_Stop` receives the same descriptor and should
free cached state.

`IFR_Render` receives the image descriptor in `R1` and a render descriptor in
`R2`:

| Offset | Field |
|--------|-------|
| 0 | Flags, including colour-map and quality bits |
| 4 | Transform matrix, six words |
| 28 | Minimum X clip in external coordinates |
| 32 | Minimum Y clip in external coordinates |
| 36 | Maximum X clip in external coordinates |
| 40 | Maximum Y clip in external coordinates |
| 44 | Colour mapping function pointer |
| 48 | Colour mapping workspace |

`IFR_BBox` receives the image descriptor in `R1` and a bounding-box descriptor
in `R2`:

| Offset | Field |
|--------|-------|
| 0 | Flags, currently 0 |
| 4 | Transform matrix, six words |
| 28 | Minimum X position in Draw coordinates |
| 32 | Minimum Y position in Draw coordinates |
| 36 | Maximum X position in Draw coordinates |
| 40 | Maximum Y position in Draw coordinates |

Return the transformed bounding box in Draw coordinates, which are OS units
multiplied by 256. If the renderer registration did not set the irregular-shape
flag, ImageFileRender calls the renderer only for identity bounds and performs
rectangular transform calculations itself.

`IFR_DeclareFonts` is only needed for renderers which use fonts and should call
`PDriver_DeclareFont` with the supplied flags. It receives the image descriptor
in `R1` and a declare-fonts descriptor in `R2`:

| Offset | Field |
|--------|-------|
| 0 | Flags, currently 0 |
| 4 | Flags to pass to `PDriver_DeclareFont` |

`IFR_Info` receives the image descriptor in `R1` and an information descriptor
in `R2`:

| Offset | Field |
|--------|-------|
| 0 | Query type |
| 4 | Query data length |
| 8 | Pointer to data block to read from or fill in |

Implement query `0` for base details. Return special error code `1` for an
unknown query or `2` for a recognised query with an invalid length.

Base details query block:

| Offset | Field |
|--------|-------|
| 0 | Sequence number |
| 4 | X DPI |
| 8 | Y DPI |
| 12 | Colour type |
| 16 | Image flags; bit 0 means the image is solid across its whole bounding box |
