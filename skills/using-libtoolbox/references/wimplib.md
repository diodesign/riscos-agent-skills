# `wimplib`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/wimplib`

Category: `support`

Purpose: Public header.

Use it when: Read when code uses the older helper structures and colour/icon convenience definitions from `wimplib`.

## Includes

- `kernel.h`
- `wimp.h`

## Main Types

- `Palette`
- `SpriteParams`
- `WimpSysInfo`

## Public Constants And Method Codes

- `CancelDrag` = `0`
- `CloseMenu` = `((void *) -1)`
- `Wimp_BackgroundColour` = `(128)`

## Notes

- This header is constant/type-oriented and does not publish C veneer functions.
