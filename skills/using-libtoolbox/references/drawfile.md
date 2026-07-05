# `drawfile`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/drawfile`

Category: `support`

Purpose: C veneers to the drawfile swis

Use it when: Read when redraw code renders Draw files inside Toolbox windows or prints Draw content.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/render.html

## Includes

- `kernel.h`
- `wimp.h`

## Public Functions

- `drawfile_render`: renders a drawfile from memory
  Prototype: `extern _kernel_oserror *drawfile_render (unsigned int flags, void *data, int size, Transform *trfm, BBox *clip,int flatness);`
- `drawfile_render`: get the bounding box of a drawfile
  Prototype: `extern _kernel_oserror *drawfile_bbox (unsigned int flags, void *data, int size, Transform *trfm, BBox *box);`
- `drawfile_render`: declares the fonts for printing a drawfile
  Prototype: `extern _kernel_oserror *drawfile_declare_fonts (unsigned int flags, void *data, int size);`

## Public Constants And Method Codes

- `DrawFile_Render` = `0x45540`
- `XDrawFile_Render` = `0x65540`
- `DrawFile_BBox` = `0x45541`
- `XDrawFile_BBox` = `0x65541`
- `DrawFile_DeclareFonts` = `0x45542`
- `XDrawFile_DeclareFonts` = `0x65542`
- `Drawfile_RenderBoundingBoxes` = `0x00000001`
- `Drawfile_DoNotRenderObjects` = `0x00000002`
- `Drawfile_RenderWithFlatness` = `0x00000004`
- `Drawfile_DoNotDownloadFont` = `0x00000001`
