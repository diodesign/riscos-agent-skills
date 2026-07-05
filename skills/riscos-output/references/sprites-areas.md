# RISC OS Sprites: Areas

Reference for sprite areas, sprite files, addressing flags, and the area-level operations used to initialise, load, merge, save, and inspect sprite collections.

---

## Sprite Areas

A sprite area is a contiguous block of memory containing an area header followed by zero or more sprite control blocks. Three kinds exist:

| Kind | Description |
|------|-------------|
| System area | Built-in OS workspace; publicly accessible. Avoid in commercial applications. |
| Wimp pool | Shared pool managed by the Wimp; used for Wimp sprites such as window furniture. |
| User area | Private block allocated by the application; referenced by its address. |

## Sprite Area Header

An in-memory sprite area begins with four words:

| Offset | Size | Content |
|--------|------|---------|
| 0 | word | Total size of sprite area in bytes |
| 4 | word | Number of sprites in area |
| 8 | word | Byte offset to first sprite from start of area |
| 12 | word | Byte offset to first free word, which is the end of the last sprite |

When initialising a user area with `OS_SpriteOp 9`, the caller must pre-fill:

| Offset | Value |
|--------|-------|
| 0 | Total area size in bytes |
| 8 | First sprite offset, normally 16 |

The OS fills offsets 4 and 12.

## Sprite Files on Disc

RISC OS sprite files omit the leading area size word. A sprite file starts with:

| File offset | Area offset | Content |
|-------------|-------------|---------|
| 0 | 4 | Number of sprites |
| 4 | 8 | Byte offset to first sprite from start of area |
| 8 | 12 | Byte offset to first free word |

Sprite offsets stored in the file remain area offsets, not raw file offsets. To convert an area offset from the file header or sprite chain into a host file offset, subtract 4. A normal sprite file often reports `first_sprite_offset = &10`, which corresponds to file offset `&0C`.

When loading a sprite file image into private workspace for direct `OS_SpriteOp` use, prepend a 32-bit area size word. Keep that prepended size field as an explicit 32-bit quantity, for example `int32_t`, so the layout remains correct on 64-bit builds.

### Empty sprite files

An empty sprite file on disc is not the same layout as an empty in-memory
`sprite_area`.

Use these three words on disc:

| File offset | Value | Meaning |
|-------------|-------|---------|
| 0 | `0` | Number of sprites |
| 4 | `16` | First sprite offset as an area offset |
| 8 | `16` | First free offset as an area offset |

This produces a valid 12-byte empty sprite file.

Do not write the in-memory area `size` word at the start of the file. That
fourth word belongs only to the in-memory `sprite_area` header used with
`OS_SpriteOp`.

## R0 Addressing Flags

Every `OS_SpriteOp` call encodes both the reason code and the interpretation of R1 and R2 in R0:

```
R0 = reason_code + addressing_flags
```

| Addition | Bits 8-9 | R1 | R2 |
|----------|----------|----|----|
| +0 | 00 | Not used | Pointer to sprite name in the system area |
| +256 | 01 | Pointer to user sprite area | Pointer to sprite name |
| +512 | 10 | Pointer to user sprite area | Pointer to sprite control block |

Example: to call reason 28, Put Sprite, using a sprite control block pointer in a user area, use `R0 = 28 + 512 = 540`.

## Area Operations

| Reason | R0 base | Operation |
|--------|---------|-----------|
| 8 | 8 | Read area control block -> R2=size, R3=count, R4=first offset, R5=free offset |
| 9 | 9 | Initialise sprite area |
| 10 | 10+flags | Load sprite file, overwriting existing sprites |
| 11 | 11+flags | Merge sprite file into area |
| 12 | 12+flags | Save sprite area to file |
| 2 | 2 | Screen save to file |
| 3 | 3 | Screen load from file, changing mode if needed |

See [sprites-management.md](sprites-management.md) for the full register contracts for load, save, merge, copy, rename, delete, and enumeration operations.

## Practical validation

When creating, editing, or diagnosing a sprite file on disc:

* use `riscos-dumpsprites --check <file>` to confirm that the file layout is
  structurally valid
* use `riscos-dumpsprites <file>` to list the sprites present
* if a file was constructed from a user sprite area in memory, re-check that
  the leading size word was removed before writing the disc file
