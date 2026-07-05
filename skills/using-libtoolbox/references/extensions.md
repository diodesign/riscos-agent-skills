# Extension Modules

The `tboxlibs` header set includes more than the classic Toolbox core. Several headers describe additional object or gadget modules that are not part of the standard RISCOS.com Toolbox chapters.

Treat these headers as the primary reference when they appear in code or templates.

There are no matching classic Toolbox manual chapters for several of these newer modules, so the installed headers are the authoritative source for their types, methods, events, and flags.

## Extra Object Module

- `optionswindow`: multi-pane options/configuration window support.

## Extra Gadgets

- `ToolAction`: toolbar-style action gadget with separate Select/Adjust behaviour and alternate identities.
- `amplayercontrol`: GAMPlayer media-control gadget family.
- `colourswatch`: colour swatch gadget.
- `divider`: divider/separator gadget.
- `imagefilegadget`: image presentation gadget with index, quality, transform, colour-map, and scroll control.
- `mdnsservice`: gadget for service/domain presentation.
- `scrollbar`: standalone scrollbar gadget API.
- `scrolllist`: scrollable list gadget with selection, item mutation, and database-query helpers.
- `textarea`: editable multi-line text gadget with selection, cursor, colour, and background control.
- `urlimage`: gadget that fetches and displays an image from a URL.

## How To Work With Them

- Read the specific generated header reference in `references/`.
- Do not assume these gadgets share the exact behaviour of the built-in `gadgets.h` families.
- Check the method base, event base, and type constants in the header before inferring how `Toolbox_ObjectMiscOp` calls are formed.
- If the code mixes these gadgets with classic `Window` APIs, read `window.md` and `gadgets.md` as well.

## Practical Notes For `imagefilegadget`

- `imagefilegadget` works well as the display surface in a mostly standard `Window` object; the application can still manage window extent, scroll position, and sibling gadgets through the normal `window` and `gadgets` veneers.
- Treat `imagefilegadget_get_bounds` as the authoritative rendered-image size after updating the gadget's value, quality, index, colour map, or transform.
- If the window extent changes, preserve the user's position by reading scroll with `imagefilegadget_get_scroll` before layout changes and restoring it with `imagefilegadget_set_scroll` afterwards.
- `ImageFileGadget_MouseClick` can be used for focus management as well as image interaction; clearing the caret on click can be enough to return control to window-level keyboard shortcuts.
