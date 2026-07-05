# Modes overview

## Key SWIs

| SWI | Number | Summary |
|-----|--------|---------|
| `OS_ScreenMode 0` | &65, R0=0 | Select a mode by number or selector. |
| `OS_ScreenMode 1` | &65, R0=1 | Return current mode specifier. |
| `OS_ScreenMode 2` | &65, R0=2 | Enumerate available modes. |
| `OS_ScreenMode 15` | &65, R0=15 | Select a mode by string. |
| `OS_CheckModeValid` | &26 | Validate a mode specifier. |
| `OS_ReadModeVariable` | &35 | Read one mode variable. |
| `OS_ReadVduVariables` | &31 | Read multiple mode or VDU variables. |
| `OS_Byte 135` | — | Return char at cursor and current mode number. |

## VDU sequence

| Sequence | Effect |
|----------|--------|
| `VDU 22, n` | Change to mode `n`. |

## Mode variable numbers

| Number | Name | Returns |
|--------|------|---------|
| 0 | `ModeFlags` | Mode flags |
| 1 | `ScrRCol` | Text columns − 1 |
| 2 | `ScrBCol` | Text rows − 1 |
| 3 | `NColour` | Colours − 1 |
| 4 | `XEigFactor` | OS units per pixel in X |
| 5 | `YEigFactor` | OS units per pixel in Y |
| 6 | `LineLength` | Bytes per screen row |
| 7 | `ScreenSize` | Total screen memory in bytes |
| 8 | `YShftFactor` | log2(LineLength/2) |
| 9 | `Log2BPP` | log2(bits per pixel) |
| 10 | `Log2BPC` | log2(bits per character cell) |
| 11 | `XWindLimit` | Rightmost pixel column |
| 12 | `YWindLimit` | Topmost pixel row |

## Mode selector block

```text
DCD 1
DCD x_pixels
DCD y_pixels
DCD depth_code
DCD frame_rate
DCD -1
```

`depth_code` values:

* 0 = 1bpp
* 1 = 2bpp
* 2 = 4bpp
* 3 = 8bpp
* 4 = 16bpp
* 5 = 32bpp

## Mode string format

`X640 Y480 C256 F60`

Space or comma separated:

* `X` = width
* `Y` = height
* `C` = colours
* `F` = refresh rate
* `EX` and `EY` = EIG factors

## Common mode reference

| Mode | Resolution | OS units | Colours | bpp | Hz | Notes |
|------|-----------|----------|---------|-----|----|-------|
| 12 | 640×256 | 1280×1024 | 16 | 4 | 50 | Classic desktop |
| 13 | 320×256 | 1280×1024 | 256 | 8 | 50 | Wide pixels |
| 15 | 640×256 | 1280×1024 | 256 | 8 | 50 | Highest-colour 50 Hz mode |
| 27 | 640×480 | 1280×960 | 16 | 4 | 60 | VGA |
| 28 | 640×480 | 1280×960 | 256 | 8 | 60 | VGA desktop |
| 31 | 800×600 | 1600×1200 | 16 | 4 | 56 | SVGA |

## Pixel depth encoding

| Code | bpp | NColour | Log2BPP |
|------|-----|---------|---------|
| 0 | 1 | 1 | 0 |
| 1 | 2 | 3 | 1 |
| 2 | 4 | 15 | 2 |
| 3 | 8 | 255 | 3 |
| 4 | 16 | 65535 | 4 |
| 5 | 32 | &FFFFFFFF | 5 |

## Monitor types

| Type | Standard | Typical Hz |
|------|----------|-----------|
| 0 | TV / PAL | 50 |
| 1 | Multi-frequency | 50–64 |
| 2 | 64 Hz hi-res mono | 64 |
| 3 | VGA | 60 |
| 4 | Super-VGA | 56–75 |
| 5 | LCD | varies |

## Key mode facts

* OS units per pixel = `1 << EigFactor`
* shadow-bank modes add 128 to the mode number
* VIDC1 8bpp has only 64 base colours plus 4 tints
* mode selectors and mode strings require RISC OS 3.5+

## Focused mode references

* Mode information: [modes-mode-information.md](modes-mode-information.md)
* Mode numbers: [modes-mode-numbers.md](modes-mode-numbers.md)
* Mode selection: [modes-mode-selection.md](modes-mode-selection.md)
* Mode specifiers: [modes-mode-specifiers.md](modes-mode-specifiers.md)
