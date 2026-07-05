# RISC OS Sprites: Data Format

Reference for sprite control blocks, sprite mode words, palette data, pixel layout, mask sizing, and validation checks. Use this when parsing, constructing, or diagnosing sprite data directly.

---

## Sprite Control Block

Each sprite immediately follows the previous one, or the sprite area header for the first sprite. All offsets inside the control block are relative to the start of that sprite's control block.

| Offset | Size | Content |
|--------|------|---------|
| 0 | word | Byte offset to next sprite from start of this sprite, or 0 if last |
| 4 | 12 bytes | Sprite name: up to 12 characters, null-padded, case-insensitive |
| 16 | word | Width of sprite in words minus 1 |
| 20 | word | Height in scan lines minus 1 |
| 24 | word | First bit used in the left-most word of each row |
| 28 | word | Last bit used in the right-most word of each row |
| 32 | word | Byte offset to sprite image data from start of control block |
| 36 | word | Byte offset to transparency mask from start of control block; equals offset 32 if no mask |
| 40 | word | Mode: old-format screen mode number or new-format sprite mode word |
| 44+ | - | Optional palette data |

Useful derived values:

| Value | Formula |
|-------|---------|
| `width_words` | `width_words_minus_1 + 1` |
| `height` | `height_minus_1 + 1` |
| `image_bytes` | `mask_offset - image_offset` if a mask is present, otherwise `next - image_offset` |
| `mask_bytes` | `next - mask_offset` if a mask is present |

Pixel width is not stored directly. Derive it from the row word count, edge bits, and pixel depth:

```
used_bits = width_words * 32 - lbit - (31 - rbit)
pixel_width = used_bits / bits_per_pixel
```

This is especially important for partial-word sprites and screen-window captures.

## Palette Data

If a palette is present, it sits between the 44-byte sprite header and the image data.

```
palette_bytes = image_offset - 44
```

Each palette entry is 8 bytes:

| Word | Content |
|------|---------|
| 0 | First physical colour in `&BBGGRR00` format |
| 1 | Second physical colour in `&BBGGRR00` format, normally the same as word 0 |

For many real sprites, both words match. If they differ, warn about it, but do not treat it as an immediate hard parse failure.

Typical indexed-palette sizes:

| Depth | Plausible entry counts |
|-------|------------------------|
| 1bpp | 0 or 2 |
| 2bpp | 0 or 4 |
| 4bpp | 0 or 16 |
| 8bpp | 0, 16, 64, or 256 |

True-colour and CMYK sprites normally do not need palette blocks. Palettes in new-type sprites require RISC OS 3.6 or later.

## Old-Format Mode Numbers

If the sprite-type bits are clear, the mode field is an old-format mode number.

For sprite work, the useful derived fields are text resolution, graphics resolution, OS-unit resolution, logical colour count, and inferred bits per pixel. Text and teletext modes can exist in the mode table, but they are usually suspicious for graphics sprites and worth reporting.

For old modes with known logical-colour counts, bits per pixel can be inferred as:

| Logical colours | Bits per pixel |
|-----------------|----------------|
| 2 | 1 |
| 4 | 2 |
| 16 | 4 |
| 256 | 8 |

## New-Format Sprite Mode Words

If the sprite-type bits are non-zero, the mode field is a new-format sprite mode word. Do not identify sprite mode words by bit 0 alone; odd mode numbers and mode selector blocks can also have bit 0 set in other contexts.

```
mode_word = (type << 27) | (ydpi << 14) | (xdpi << 1) | 1
```

| Bits | Content |
|------|---------|
| 0 | Always 1 |
| 1-13 | Horizontal DPI |
| 14-26 | Vertical DPI |
| 27-30 | Base sprite type |
| 31 | 1 = alpha-channel mask; 0 = binary mask |

Typical DPI values are 180, 90, 45, and 22.

| Type | Bits/pixel | Format |
|------|------------|--------|
| 1 | 1 | Indexed, 2 colours |
| 2 | 2 | Indexed, 4 colours |
| 3 | 4 | Indexed, 16 colours |
| 4 | 8 | Indexed, 256 colours |
| 5 | 16 | RGB, 32K colours |
| 6 | 32 | RGB, 16M colours |
| 7 | 32 | CMYK |

Bit 31 should be handled separately from the base type. For example, type 4 with bit 31 set is still an 8bpp indexed sprite, but it has an 8bpp alpha mask.

## Pixel Formats

### 16bpp RGB, Type 5

| Bits | Component |
|------|-----------|
| 0-4 | Red, 5 bits |
| 5-9 | Green, 5 bits |
| 10-14 | Blue, 5 bits |
| 15 | Reserved, normally 0 |

### 32bpp RGB, Type 6

| Bits | Component |
|------|-----------|
| 0-7 | Red |
| 8-15 | Green |
| 16-23 | Blue |
| 24-31 | Reserved, normally 0 |

Alpha-channel sprites store alpha in the mask data, not in the high byte of the image pixels.

## Mask Sizing

For classic masked sprites, mask data is often the same row stride and total size as the image data.

For new-format sprites without the alpha flag, the mask is a 1bpp bitmap regardless of image depth. Each mask row is word-aligned.

For alpha-channel sprites, treat the mask as its own 8bpp bitmap:

```
mask_bits_per_pixel = 8
mask_row_bytes = round_up_to_word(pixel_width * 8) / 8
mask_bytes = mask_row_bytes * height
```

Do not assume that alpha masks consume the same number of bytes as the image data, especially for 16bpp or 32bpp sprites.

Mask pixel meaning:

| Mask form | Meaning |
|-----------|---------|
| Binary mask | 1 = solid, 0 = transparent |
| Alpha mask | 255 = opaque, 0 = transparent, intermediate values are translucent |

## Validation Checks

Useful non-fatal checks:

* `image_offset` and `mask_offset` lie within the sprite.
* Palette size is a multiple of 8 bytes.
* `lbit` and `rbit` are within `0..31`.
* Derived pixel width is integral for the decoded bits per pixel.
* Image size matches `width_words * 4 * height`.
* Mask size matches either the image size, a 1bpp mask, or the alpha-mask expectation.
* Palette entry count is plausible for the indexed depth.
* A true-colour sprite does not unexpectedly carry a palette.
* The file `free_offset`, after subtracting 4, reaches the end of the on-disc file.

These checks are useful for diagnostics, but many should be warnings rather than fatal parse errors.

For routine checking in this build environment, prefer:

* `riscos-dumpsprites --check <file>` for structural validation
* `riscos-dumpsprites <file>` for a summary of the sprites present

This is especially useful after generating sprite files programmatically or
when constructing a nominally empty sprite file by hand.
