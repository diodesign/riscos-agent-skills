# `colourswatch`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/colourswatch`

Category: `extension`

Purpose: C veneers to the Methods provided by the ColourSwatch class

Use it when: Read for the ColourSwatch gadget extension.

## Includes

- `kernel.h`
- `toolbox.h`
- `gadgets.h`

## Main Types

- `ColourSwatch`
- `ColourSwatchColourChangedEvent`

## Public Functions

- `colourswatch_get_colour`: Read the colour used by the Swatch
  Prototype: `extern _kernel_oserror *colourswatch_get_colour ( unsigned int flags, ObjectId window, ComponentId swatch, int *outflags, unsigned long *colour );`
- `colourswatch_set_colour`: Select the colour used by the Swatch
  Prototype: `extern _kernel_oserror *colourswatch_set_colour ( unsigned int flags, ObjectId window, ComponentId swatch, unsigned long colour );`
- `colourswatch_get_none_available`: Read whether the 'none' option is available
  Prototype: `extern _kernel_oserror *colourswatch_get_none_available ( unsigned int flags, ObjectId window, ComponentId swatch, int *out_flags );`
- `colourswatch_set_none_available`: Select whether a 'none' option is available
  Prototype: `extern _kernel_oserror *colourswatch_set_none_available ( unsigned int flags, ObjectId window, ComponentId swatch, int none );`
- `colourswatch_get_title`: Read the title to use on the colour selector
  Prototype: `extern _kernel_oserror *colourswatch_get_title ( unsigned int flags, ObjectId window, ComponentId swatch, char *buffer, int buff_size, int *nbytes );`
- `colourswatch_set_title`: Set the title of the colour selector window
  Prototype: `extern _kernel_oserror *colourswatch_set_title ( unsigned int flags, ObjectId window, ComponentId swatch, char *title );`

## Public Constants And Method Codes

- `ColourSwatchValidFlags` = `0xC000000C`
- `ColourSwatch_IncludeNoneButton` = `0x00000004`
- `ColourSwatch_SelectNoneButton` = `0x00000008`
- `ColourSwatch_SWIBase` = `0x140300`
- `ColourSwatch_MethodBase` = `(ColourSwatch_SWIBase<<4)`
- `ColourSwatch_EventBase` = `(ColourSwatch_SWIBase)`
- `ColourSwatch_Type` = `( (sizeof(ColourSwatch)) << 16 | \`
- `ColourSwatch_GetColour` = `(ColourSwatch_MethodBase + 0)`
- `ColourSwatch_SetColour` = `(ColourSwatch_MethodBase + 1)`
- `ColourSwatch_GetTitle` = `(ColourSwatch_MethodBase + 2)`
- `ColourSwatch_SetTitle` = `(ColourSwatch_MethodBase + 3)`
- `ColourSwatch_GetNoneAvailable` = `(ColourSwatch_MethodBase + 4)`
- `ColourSwatch_SetNoneAvailable` = `(ColourSwatch_MethodBase + 5)`
- `ColourSwatch_ColourChanged` = `(ColourSwatch_EventBase + 0)`
- `ColourSwatch_ColourNoneSelected` = `0x00000001`
