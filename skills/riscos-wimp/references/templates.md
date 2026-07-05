# Templates

Use this file when working with `Wimp_OpenTemplate` and `Wimp_LoadTemplate`.

## Key rules

* Open the template file before loading entries.
* Close it after all required templates are loaded.
* If asking `Wimp_LoadTemplate` for size information, set `R1 <= 0`.
* The name buffer passed in `R5` may be overwritten with the actual template name found.
* The name buffer passed in `R5` must be word-aligned and large enough for the returned actual name.

That last point matters. Do not pass a string literal in `R5` to `Wimp_LoadTemplate`. Use a writable, word-aligned buffer.

## Buffer sizing

When loading multiple windows from templates:

* calculate the largest template body size
* calculate the total indirected workspace required across all templates
* use scratch space for the temporary window load buffer
* use separate persistent workspace for indirected data that must live after creation
* remember that the reported template body size and indirected workspace size are different outputs and must not be conflated

## Indirected data

When a template contains indirected text, validation strings, or sprite names:

* the indirected workspace passed to `Wimp_LoadTemplate` must remain valid after the window is created
* do not free or overwrite that memory while the window still exists
* `R2` is updated to point at the remaining indirected workspace after each load; preserve that progression when loading multiple templates into one backing block

If a template is being reused as a base window definition rather than created
directly in place:

* copy the loaded window block before per-instance edits such as title-buffer
  pointers, extents, or scroll positions
* keep any replacement indirected text buffers alive for the lifetime of the
  created window
* if the template uses standard Wimp sprites rather than the application's
  sprite area, make that `spritearea` choice explicit before window creation

## Font reference array

`Wimp_LoadTemplate` also accepts a font-reference array in `R4`. Passing `-1` means no fonts. If a task later needs templates with fonts, revisit this rather than assuming the current shortcut is always valid.

## Porting guidance

If the original assembler uses `Wimp_LoadTemplate` twice, once to size and once to load, keep that shape unless there is a proven reason to change it.
