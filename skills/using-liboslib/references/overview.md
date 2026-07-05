# OSLib overview

OSLib in this environment is exported at `/riscos-resources/Export/Lib/OSLib`.

Its main layout is:

* `Core/h` and `Core/hdr`
* `Computer/h` and `Computer/hdr`
* `User/h` and `User/hdr`
* `Toolbox/h` and `Toolbox/hdr`
* `o/` for the built library objects

Use `h/` when you need the public C API surface. The files are the generated
typed SWI interface headers.

Use `hdr/` when you need the parallel assembler or DefMod-facing names for the
same component. The filenames mirror the `h/` tree.

Use `o/` when you need to know which compiled library object variants exist.
At present the exported objects are `OSLib`, `OSLib-32`, `OSLib-64`,
`OSLibzm`, `OSLibzm-32`, and `OSLibzm-64`.

## Area split

`Core`

The foundational OS-facing layer. This is where the generic types and the
largest API surfaces live, including `types`, `os`, `osbyte`, `osword`,
`osspriteop`, `colourtrans`, `messagetrans`, `territory`, `osmodule`,
`osheap`, `buffer`, `dma`, and related service/event helpers.

`Computer`

Machine and filing-system oriented interfaces. This includes the file APIs
(`osfile`, `osfind`, `osgbpb`, `osargs`, `osfscontrol`), filing systems such
as `adfs`, `cdfs`, `dosfs`, `netfs`, `nfs`, `ramfs`, and `resourcefs`, and
other device/network interfaces such as `socket`, `scsi`, `parallel`,
`osserialop`, and `fileraction`.

`User`

Desktop and graphics-oriented interfaces. This includes `wimp`, `font`,
`draw`, `drawfile`, `jpeg`, `dragasprite`, `wimpspriteop`, `taskwindow`,
`taskmanager`, `hourglass`, `help`, `colourpicker`, `pdumper`, and `pdriver`.

`Toolbox`

The Toolbox base plus Toolbox object and gadget modules. The root `toolbox`
header provides the common object model, and the other headers cover specific
objects or gadgets such as `window`, `menu`, `iconbar`, `saveas`, `proginfo`,
`fontmenu`, `button`, `slider`, `displayfield`, and `writablefield`.

## How to use the inventories

The area reference files are the first stop when you need to know:

* which header likely owns a given wrapper family
* whether a public type already exists
* whether OSLib exports a wrapper for a given SWI or service

After locating the right family, re-open the actual exported header to confirm
the exact parameter and return types before writing code.
