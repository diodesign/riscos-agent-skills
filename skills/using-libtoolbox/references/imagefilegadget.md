# `imagefilegadget`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/imagefilegadget`

Category: `extension`

Purpose: C veneers to the Methods provided by the ImageFile gadget

Use it when: Read for the ImageFileGadget extension used to present converted image content in windows.

## Includes

- `kernel.h`
- `toolbox.h`
- `window.h`
- `wimp.h`

## Main Types

- `ImageFileGadget`
- `ImageFileGadgetMouseClickEvent`

## Public Functions

- `imagefilegadget_set_value`: Set the position of the image to render
  Prototype: `extern _kernel_oserror *imagefilegadget_set_value ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, int filetype, const char *filedata, int length );`
- `imagefilegadget_get_value`: Read the image data to render
  Prototype: `extern _kernel_oserror *imagefilegadget_get_value ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, int *filetype, char * *filedata, int *length );`
- `imagefilegadget_set_colour`: Set the colour used in the image file.
  Prototype: `extern _kernel_oserror *imagefilegadget_set_colour ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, unsigned int colour );`
- `imagefilegadget_get_colour`: Get the colour used in the image.
  Prototype: `extern _kernel_oserror *imagefilegadget_get_colour ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, unsigned int *colour );`
- `imagefilegadget_get_state`: Read the state of the gadget.
  Prototype: `extern _kernel_oserror *imagefilegadget_get_state ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, unsigned int *state );`
- `imagefilegadget_set_state`: Set the state of the gadget.
  Prototype: `extern _kernel_oserror *imagefilegadget_set_state ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, unsigned int new_state );`
- `imagefilegadget_set_index`: Set the index of the image which should be rendered
  Prototype: `extern _kernel_oserror *imagefilegadget_set_index ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, unsigned int index );`
- `imagefilegadget_get_index`: Get the index of the image which is being rendered
  Prototype: `extern _kernel_oserror *imagefilegadget_get_index ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, unsigned int *index );`
- `imagefilegadget_get_quality`: Get the quality to which the image is being rendered
  Prototype: `extern _kernel_oserror *imagefilegadget_get_quality ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, unsigned int *quality );`
- `imagefilegadget_set_quality`: Set the quality to which the image should be rendered
  Prototype: `extern _kernel_oserror *imagefilegadget_set_quality ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, unsigned int quality );`
- `imagefilegadget_set_colour_map`: Set the colourmap descriptor with which the image should be rendered
  Prototype: `extern _kernel_oserror *imagefilegadget_set_colour_map ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, void *colourmap );`
- `imagefilegadget_set_transform`: Set the transformation used on the image
  Prototype: `extern _kernel_oserror *imagefilegadget_set_transform ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, unsigned long transform_type, unsigned long *transform_data );`
- `imagefilegadget_set_scroll`: Set the scroll position of the image
  Prototype: `extern _kernel_oserror *imagefilegadget_set_scroll ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, int xscroll, int yscroll );`
- `imagefilegadget_get_scroll`: Get the scroll position of the image
  Prototype: `extern _kernel_oserror *imagefilegadget_get_scroll ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, int *xscroll, int *yscroll );`
- `imagefilegadget_get_bounds`: Read the bounds of the image being rendered
  Prototype: `extern _kernel_oserror *imagefilegadget_get_bounds ( unsigned int flags, ObjectId window, ComponentId imagefilegadget, BBox * image_box, int *screen_width, int *screen_height );`

## Public Constants And Method Codes

- `ImageFileGadget_NoBorder` = `0x00000001 /* the border is disabled */`
- `ImageFileGadget_ColourMapWhole` = `0x00000002 /* the whole gadget a */`
- `ImageFileGadgetValidFlags` = `0xC0000003`
- `ImageFileGadget_Base` = `0x4024`
- `ImageFileGadget_Type` = `(sizeof(ImageFileGadget)) << 16 | ImageFileGadget_Base`
- `ImageFileGadget_SWIBase` = `0x140240`
- `ImageFileGadget_GetState` = `(ImageFileGadget_Base + 0)`
- `ImageFileGadget_SetState` = `(ImageFileGadget_Base + 1)`
- `ImageFileGadget_SetColour` = `(ImageFileGadget_Base + 2)`
- `ImageFileGadget_GetColour` = `(ImageFileGadget_Base + 3)`
- `ImageFileGadget_SetValue` = `(ImageFileGadget_Base + 4)`
- `ImageFileGadget_GetValue` = `(ImageFileGadget_Base + 5)`
- `ImageFileGadget_GetIndex` = `(ImageFileGadget_Base + 6)`
- `ImageFileGadget_SetIndex` = `(ImageFileGadget_Base + 7)`
- `ImageFileGadget_GetQuality` = `(ImageFileGadget_Base + 8)`
- `ImageFileGadget_SetQuality` = `(ImageFileGadget_Base + 9)`
- `ImageFileGadget_SetColourMap` = `(ImageFileGadget_Base + 10)`
- `ImageFileGadget_SetTransform` = `(ImageFileGadget_Base + 12)`
- `ImageFileGadget_SetScroll` = `(ImageFileGadget_Base + 14)`
- `ImageFileGadget_GetScroll` = `(ImageFileGadget_Base + 15)`
- `ImageFileGadget_GetBounds` = `(ImageFileGadget_Base + 16)`
- `ImageFileGadget_DesktopColours` = `(1<<0) /* For [Get|Set]Colour */`
- `ImageFileGadget_ImageCoords` = `(1<<0) /* For [Get|Set]Scroll */`
- `ImageFileGadget_MouseClick` = `(ImageFileGadget_SWIBase + 0)`
- `ImageFileGadget_MouseClick_Flags_DoubleClick` = `(1<<1)`
- `ImageFileGadget_MouseClick_Flags_AdjustClick` = `(1<<2)`
- `ImageFileGadget_MouseClick_Flags_StartDrag` = `(1<<3)`
- `ImageFileGadget_MouseClick_Flags_XInImage` = `(0<<4)`
- `ImageFileGadget_MouseClick_Flags_XLow` = `(1<<4)`
- `ImageFileGadget_MouseClick_Flags_XHigh` = `(2<<4)`
- `ImageFileGadget_MouseClick_Flags_YInImage` = `(0<<6)`
- `ImageFileGadget_MouseClick_Flags_YLow` = `(1<<6)`
- `ImageFileGadget_MouseClick_Flags_YHigh` = `(2<<6)`
- `ImageFileGadget_MouseClick_Flags_MenuClick` = `(1<<8)`

## Observed Usage Patterns

- `imagefilegadget_set_value` is the main handoff point from an application's decode/load path into the gadget. Passing filetype, data pointer, and byte length lets the gadget own presentation while the application keeps ownership of the backing buffer.
- `imagefilegadget_set_transform` is suitable for both fixed scaling and fit-to-window behaviour. A common split is `TRANSFORMTYPE_SCALE` for explicit zoom and `TRANSFORMTYPE_SIZE` for fit mode.
- `imagefilegadget_get_bounds` is useful immediately after quality/index/transform changes when the surrounding window or toolbar layout depends on the rendered image size.
- `imagefilegadget_get_scroll` and `imagefilegadget_set_scroll` are the right way to preserve image position across extent recalculation; do not assume the surrounding window scroll values alone are enough.
- `ImageFileGadget_MouseClick` is a semantic event, not just a raw Wimp click mirror. Existing code may use it for focus/caret policy instead of image editing.
