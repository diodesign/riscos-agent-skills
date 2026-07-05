# Sprites overview

All sprite operations use `OS_SpriteOp` (SWI `&2E`). `R0` encodes both the
reason code and the sprite addressing mode.

## R0 encoding

```text
R0 = reason_code + addressing_flags
```

| Addition | R1 | R2 |
|----------|----|----|
| +0 | System area pointer or unused | Sprite name pointer |
| +256 | User sprite area pointer | Sprite name pointer |
| +512 | User sprite area pointer | Sprite control block pointer |

## Sprite area and file operations

| Reason | R0 base | Operation |
|--------|---------|-----------|
| 8 | 8 | Read area control block |
| 9 | 9 | Initialise sprite area |
| 10 | 10+flags | Load sprite file |
| 11 | 11+flags | Merge sprite file |
| 12 | 12+flags | Save sprite area |
| 2 | 2 | Screen save to file |
| 3 | 3 | Screen load from file |

When loading a sprite file into private workspace for later `OS_SpriteOp` use:

* a sprite file image is not itself a complete sprite area
* a user sprite area begins with a 32-bit size word followed by sprite-file data
* keep that prepended size field as an explicit 32-bit quantity in 64-bit-safe code

## Sprite creation and capture

| Reason | R0 base | Operation |
|--------|---------|-----------|
| 15 | 15+flags | Create blank sprite |
| 14 | 14+flags | Get sprite from current graphics window |
| 16 | 16+flags | Get sprite from explicit coordinates |

## Sprite information and lookup

| Reason | R0 base | Operation |
|--------|---------|-----------|
| 13 | 13+flags | Return sprite name by index |
| 40 | 40+flags | Read sprite info |
| 37 | 37+flags | Palette operations |

## Sprite modification

| Reason | R0 base | Operation |
|--------|---------|-----------|
| 25 | 25+flags | Delete sprite |
| 26 | 26+flags | Rename sprite |
| 27 | 27+flags | Copy sprite |
| 29 | 29+flags | Create mask |
| 30 | 30+flags | Remove mask |
| 31 | 31+flags | Insert row |
| 32 | 32+flags | Delete row |
| 33 | 33+flags | Flip about X axis |
| 45 | 45+flags | Insert column |
| 46 | 46+flags | Delete column |
| 47 | 47+flags | Flip about Y axis |
| 35 | 35+flags | Append sprite |
| 54 | 54+flags | Remove left-hand wastage |
| 57 | 57+flags | Insert or delete multiple rows |
| 58 | 58+flags | Insert or delete multiple columns |

## Pixel access

| Reason | R0 base | Operation |
|--------|---------|-----------|
| 41 | 41+flags | Read pixel colour |
| 42 | 42+flags | Write pixel colour |
| 43 | 43+flags | Read mask pixel |
| 44 | 44+flags | Write mask pixel |

## Rendering

| Reason | R0 base | Operation |
|--------|---------|-----------|
| 28 | 28+flags | Put sprite at graphics cursor |
| 34 | 34+flags | Put sprite at explicit coordinates |
| 48 | 48+flags | Plot mask at graphics cursor |
| 49 | 49+flags | Plot mask at explicit coordinates |
| 52 | 52+flags | Put sprite scaled |
| 53 | 53+flags | Put sprite grey-scaled |
| 50 | 50+flags | Plot mask scaled |
| 51 | 51 | Paint character scaled |
| 56 | 56+flags | Put sprite transformed |
| 55 | 55+flags | Plot mask transformed |
| 24 | 24+flags | Select sprite for VDU plotting |
| 36 | 36+flags | Set hardware pointer shape from sprite |

## Output redirection

| Reason | R0 base | Operation |
|--------|---------|-----------|
| 62 | 62+flags | Query save-area size |
| 60 | 60+flags | Switch output to sprite image |
| 61 | 61+flags | Switch output to sprite mask |

## Plot action values

| Value | Effect | +8 |
|-------|--------|-----|
| 0 | Overwrite | Use mask |
| 1 | OR | Use mask |
| 2 | AND | Use mask |
| 3 | XOR | Use mask |
| 4 | Invert screen | Use mask |
| 5 | No change | — |
| 6 | AND NOT | Use mask |
| 7 | OR NOT | Use mask |

## Scale factors block

```text
DCD  x_mult, y_mult
DCD  x_div,  y_div
```

Scaled size = original × multiplier / divisor. `R6 = 0` means no scaling.

## Sprite mode word

```text
mode_word = (type << 27) | (ydpi << 14) | (xdpi << 1) | 1
```

| Type | bpp | Colours |
|------|-----|---------|
| 1 | 1 | 2 |
| 2 | 2 | 4 |
| 3 | 4 | 16 |
| 4 | 8 | 256 |
| 5 | 16 | 32K |
| 6 | 32 | 16M |
| 7 | 32 | CMYK |

Bit 31 set means alpha channel; clear means binary mask.

## Key sprite facts

* sprite names are at most 12 characters and case-insensitive
* row 0 is the bottom row
* column 0 is the left column
* mask bits use 1 for solid and 0 for transparent
* new-type binary masks are 1bpp regardless of image depth
* alpha-channel masks are 8bpp
* sprite palettes in new-type sprites require RISC OS 3.6+
* SpriteExtend reason codes require the SpriteExtend module
* do not call `Wimp_Poll` while output is redirected to a sprite
* validate sprite files with `riscos-dumpsprites --check <file>` rather than
  assuming that an in-memory header layout is also valid on disc

## Focused sprite references

* Area headers and file layout: [sprites-areas.md](sprites-areas.md)
* Sprite format and validation: [sprites-format.md](sprites-format.md)
* Sprite rendering: [sprites-rendering.md](sprites-rendering.md)
* Sprite management: [sprites-management.md](sprites-management.md)
* Sprite creation and modification: [sprites-creation-modification.md](sprites-creation-modification.md)
* Sprite redirection: [sprites-redirection.md](sprites-redirection.md)
