# ColourTrans overview

All palette entries use `&BBGGRR00` format. Fixed-point values use 16.16
format, so `1.0 = &10000`.

## Graphics colours

| SWI | Number | Summary |
|-----|--------|---------|
| `ColourTrans_ReturnGCOL` | &40742 | Return the closest GCOL to a palette entry. |
| `ColourTrans_SetGCOL` | &40743 | Set graphics foreground or background to the closest GCOL. |
| `ColourTrans_ReturnGCOLForMode` | &40745 | Return the closest GCOL for a specified mode. |
| `ColourTrans_ReturnOppGCOL` | &40747 | Return the most contrasting GCOL in the current mode. |
| `ColourTrans_SetOppGCOL` | &40748 | Set the most contrasting graphics colour. |
| `ColourTrans_ReturnOppGCOLForMode` | &4074A | Return the most contrasting GCOL for a specified mode. |
| `ColourTrans_ReturnColourNumber` | &40744 | Return the closest colour number. |
| `ColourTrans_ReturnColourNumberForMode` | &40746 | Return the closest colour number for a specified mode. |
| `ColourTrans_GCOLToColourNumber` | &4074C | Convert a GCOL to a colour number. |
| `ColourTrans_ColourNumberToGCOL` | &4074D | Convert a colour number to a GCOL. |
| `ColourTrans_SetColour` | &4075E | Apply a known GCOL directly. |

## Text colours

| SWI | Number | Summary |
|-----|--------|---------|
| `ColourTrans_SetTextColour` | &40761 | Set text foreground or background to the closest GCOL. |
| `ColourTrans_SetOppTextColour` | &40762 | Set text colour to the most contrasting GCOL. |

## Font colours

| SWI | Number | Summary |
|-----|--------|---------|
| `ColourTrans_ReturnFontColours` | &4074E | Return logical colours and max anti-alias offset. |
| `ColourTrans_SetFontColours` | &4074F | Find the best anti-alias colour ramp and set it. |
| `ColourTrans_InvalidateCache` | &40750 | Flush the colour cache after palette changes. |

## Sprite pixel translation tables

| SWI | Number | Summary |
|-----|--------|---------|
| `ColourTrans_SelectTable` | &40740 | Build a pixel translation table. |
| `ColourTrans_SelectGCOLTable` | &40741 | Build a GCOL list for source palette entries. |
| `ColourTrans_GenerateTable` | &40763 | Enhanced `SelectTable` with stricter validation. |

When generating a sprite translation table:

* `R0 = sprite area`, or `256` for direct-sprite addressing
* `R1 = sprite name` or sprite pointer
* `R2 = destination mode`, commonly `-1`
* `R3 = destination palette`, commonly `-1` or `0`
* `R4 = output buffer`, or `0` to query the required size
* `R5 = flags`

The common sprite-area case is `R0 = area`, `R1 = name`, `R2 = -1`,
`R3 = -1`, `R4 = buffer`, `R5 = flags`.

## Colour conversion

| SWI | Number | Summary |
|-----|--------|---------|
| `ColourTrans_ConvertRGBToCIE` | &40755 | Convert RGB to CIE XYZ. |
| `ColourTrans_ConvertCIEToRGB` | &40756 | Convert CIE XYZ to RGB. |
| `ColourTrans_ConvertRGBToHSV` | &40758 | Convert RGB to HSV. |
| `ColourTrans_ConvertHSVToRGB` | &40759 | Convert HSV to RGB. |
| `ColourTrans_ConvertRGBToCMYK` | &4075A | Convert RGB to CMYK. |
| `ColourTrans_ConvertCMYKToRGB` | &4075B | Convert CMYK to RGB. |
| `ColourTrans_ConvertDeviceColour` | &40753 | Map one device colour through calibration. |
| `ColourTrans_ConvertDevicePalette` | &40754 | Batch-convert a palette through calibration. |

## Palette and calibration

| SWI | Number | Summary |
|-----|--------|---------|
| `ColourTrans_ReadPalette` | &4075C | Read a palette. |
| `ColourTrans_WritePalette` | &4075D | Write a palette buffer. |
| `ColourTrans_SetCalibration` | &40751 | Load a new screen calibration table. |
| `ColourTrans_ReadCalibration` | &40752 | Read the current calibration table. |
| `ColourTrans_WriteCalibrationToFile` | &40757 | Export calibration as star commands. |

## Focused ColourTrans references

* Graphics colours: [colourtrans-graphics-colours.md](colourtrans-graphics-colours.md)
* Text colours: [colourtrans-text-colours.md](colourtrans-text-colours.md)
* Font colours: [colourtrans-font-colours.md](colourtrans-font-colours.md)
* Sprite translation: [colourtrans-sprite-translation.md](colourtrans-sprite-translation.md)
* Colour conversion: [colourtrans-colour-conversion.md](colourtrans-colour-conversion.md)
