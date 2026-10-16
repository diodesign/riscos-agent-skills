# Fonts overview

Coordinates:

* millipoints = 1/72000 inch internally
* OS units = 1/180 inch on screen
* default scale = 400 millipoints per OS unit
* point sizes passed to `Font_FindFont` are multiplied by 16

## Font handles

| SWI | Number | Summary |
|-----|--------|---------|
| `Font_FindFont` | &40081 | Obtain a handle for a named font at a given size. |
| `Font_LoseFont` | &40082 | Release a font handle. |
| `Font_ReadDefn` | &40083 | Read identifier string, point sizes, DPI, age, and usage count. |
| `Font_SetFont` | &4008A | Set the current font for subsequent paint and measurement calls. |
| `Font_CurrentFont` | &4008B | Query current handle, colours, and anti-alias offset. |
| `Font_FutureFont` | &4008C | Return the font and colour state after the next string scan. |

## Sizing and measurement

| SWI | Number | Summary |
|-----|--------|---------|
| `Font_ReadInfo` | &40084 | Read overall font bounding box in OS units. |
| `Font_CharBBox` | &4008E | Read a single character bounding box. |
| `Font_StringBBox` | &40097 | Return a string bounding box in millipoints. |
| `Font_StringWidth` | &40085 | Measure string width; deprecated in favour of `ScanString`. |
| `Font_ScanString` | &400A1 | Comprehensive scan: width, caret, bbox, split count. |
| `Font_ReadFontMetrics` | &4009F | Read IntMetrics data into caller-supplied buffers. |

## Coordinate conversion

| SWI | Number | Summary |
|-----|--------|---------|
| `Font_ConverttoOS` | &40088 | Convert millipoints to OS units. |
| `Font_Converttopoints` | &40089 | Convert OS units to millipoints. |
| `Font_ReadScaleFactor` | &4008F | Read millipoints-per-OS-unit factors. |
| `Font_SetScaleFactor` | &40090 | Set millipoints-per-OS-unit factors. |

## Rendering

| SWI | Number | Summary |
|-----|--------|---------|
| `Font_Paint` | &40086 | Paint a string. |
| `Font_Caret` | &40087 | Paint a text cursor. |
| `Font_FindCaret` | &4008D | Find nearest character position; deprecated. |
| `Font_FindCaretJ` | &40096 | Justified-string variant; deprecated. |
| `Font_SwitchOutputToBuffer` | &4009E | Redirect `Font_Paint` output to a Draw path buffer. |
| `Font_MakeBitmap` | &40099 | Pre-render and cache a font. |

## Colours and anti-aliasing

| SWI | Number | Summary |
|-----|--------|---------|
| `Font_SetFontColours` | &40092 | Set logical font colours and anti-alias offset. |
| `Font_SetPalette` | &40093 | Set physical palette entries for anti-aliasing. |
| `Font_ReadColourTable` | &40098 | Read the 16-entry anti-alias logical colour table. |
| `Font_ReadThresholds` | &40094 | Read the anti-alias threshold table. |
| `Font_SetThresholds` | &40095 | Write a new anti-alias threshold table. |

## Cache and configuration

| SWI | Number | Summary |
|-----|--------|---------|
| `Font_CacheAddr` | &40080 | Return Font Manager version and cache sizes. |
| `Font_ListFonts` | &40091 | Enumerate fonts or build a Wimp font menu. |
| `Font_DecodeMenu` | &400A0 | Convert a Wimp menu selection back to a font identifier. |
| `Font_ReadFontMax` | &4009C | Read FontMax and cache threshold settings. |
| `Font_SetFontMax` | &4009B | Set FontMax and cache thresholds. |
| `Font_UnCacheFile` | &4009A | Evict or reload a specific font file. |
| `Font_ReadFontPrefix` | &4009D | Return the source directory path for a font handle. |

## Key constants and formats

| Item | Value / Format |
|------|----------------|
| Millipoints per inch | 72 000 |
| OS units per inch | 180 |
| Millipoints per OS unit | 400 by default |
| Point size encoding | points × 16 |
| Palette entry format | `&BBGGRR00` |
| Max anti-alias offset | 14 |
| `Font_FindFont` DPI | 0 = default 90; −1 = current screen |
| String terminators | null or CR |

## Standard desktop fonts

| Font Identifier | Category | Typical Use |
|-----------------|----------|-------------|
| `Homerton.Medium` | Sans-serif (Helvetica-style) | Standard desktop font for UI labels, titles, and dialogue controls |
| `Trinity.Medium` | Serif (Times-style) | Document body text, documentation |
| `Corpus.Medium` | Monospaced (Courier-style) | Terminal emulators, code, hex editors, tabular aligned data |

*Note: In `Font_Paint`, coordinates specify the **text baseline** (descenders hang below the Y coordinate), unlike VDU 5 which uses the top-left of the 8×8 cell.*

## Focused font references

* Rendering details: [font-rendering.md](font-rendering.md)
* Sizing and metrics: [font-sizing.md](font-sizing.md)
* Font colours: [font-colours.md](font-colours.md)
* Font files and naming: [font-files-reference.md](font-files-reference.md)
* Font Manager configuration: [font-manager-config.md](font-manager-config.md)
