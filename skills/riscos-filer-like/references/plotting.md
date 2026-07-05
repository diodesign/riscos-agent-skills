# Plotting Conventions For Filer-Like Objects

Use this file after `design.md` when choosing how one object cell is drawn.

For lower-level text, sprite, font, `ColourTrans`, and graphics details, use the `riscos-output` skill.

## Scope

This reference covers:

* common ordering of background, icon, text, and overlays
* conventions for small-icon and large-icon object views
* colour and selection handling
* when to use Wimp icon plotting versus lower-level output

## General drawing order

Within one object cell, a robust order is:

1. fill or clear the object background if needed
2. draw the main icon or sprite
3. draw the primary label
4. draw secondary metadata fields
5. draw overlays such as selection fills, borders, or highlight frames

The exact order may vary slightly with the visual style, but keep it consistent across all view formats.

## Prefer Wimp-managed plotting where possible

For filer-like views, `Wimp_PlotIcon` is often the simplest way to draw:

* a sprite
* a text field
* a filled selected background
* text with Wimp validation-string colour controls

That keeps text and sprites aligned with the desktop look.

Drop to lower-level drawing only when you need:

* a custom border or highlight frame
* non-standard graphics not naturally expressed as icons
* drawing that spans more than one icon-style region

If you need that lower level, route to the `riscos-output` skill for `ColourTrans`, `OS_Plot`, fonts, and sprite details.

## Coordinate conventions

Treat the object-box calculation as the source of truth.

Within an object cell, define named subregions such as:

* icon region
* primary label region
* secondary metadata region
* optional border region

Do not hand-code one-off offsets in multiple places. Keep a small set of layout helpers that convert a cell box into these regions.

## Small and large object forms

Common patterns:

* small view
  * icon at the left
  * one or more text fields to the right
* large view
  * icon above
  * caption or metadata below or alongside

Make the format select which subregions are active, rather than branching inside the low-level drawing calls for every field.

## Text plotting conventions

Primary label:

* should usually be the most visually stable field
* often determines the minimum useful width

Secondary fields:

* may be appended horizontally
* may be split onto another row
* may be omitted in compact formats

Guidance:

* measure with the active text metrics before committing width policy
* clip or truncate consistently
* use one alignment rule per field type, such as left-aligned names and right-aligned sizes, rather than ad hoc per-format alignment

If the interface needs custom font work or non-Wimp text rendering, use `riscos-output`.

## Sprite conventions

For object icons:

* keep a stable mapping from item kind to sprite identity
* provide a fallback sprite for unknown or unsupported kinds
* decide whether small and large views use separate sprite names or scaled rendering

If sprites come from a shared pool, keep cache ownership separate from per-item state so redraw does not repeatedly rediscover the same sprite names.

For sprite plotting, translation, or custom sprite creation, refer to `riscos-output`.

## Colour conventions

A filer-like view typically needs independent colours for:

* default background
* default foreground
* selected background
* selected foreground
* highlight or attention border
* shaded state if used

Selection and highlight should usually be separate visual channels:

* selection often changes fill and text colour
* highlight often adds an outline or border

This avoids one state hiding the other.

## Overlay and border conventions

Use overlays sparingly and consistently.

Typical overlays:

* selection fill
* highlight frame
* unavailable or shaded treatment

If drawing a custom frame:

* derive the frame rectangle from the object cell bounds
* keep the frame inside the cell so adjacent items do not overlap
* redraw the same region when removing the frame as when adding it

Custom border drawing is a good case for routing to `riscos-output`.

## Performance considerations

To keep redraw cheap:

* avoid recomputing sprite identity during every plot if it can be cached
* avoid measuring every metadata field on every redraw when width policy has not changed
* keep object plotting helpers side-effect free so they are safe to call repeatedly in redraw loops

## When To Read `riscos-output`

Read `riscos-output` when the filer-like design reaches any of these points:

* you need direct graphics drawing for borders, highlights, or custom badges
* you need explicit `ColourTrans` behaviour
* you need font metrics or non-Wimp text rendering
* you need sprite translation, custom sprite areas, or sprite creation
