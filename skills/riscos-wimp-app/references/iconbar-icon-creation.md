# Iconbar icon creation

For the low-level iconbar protocol details, read `riscos-wimp` and especially
its `references/icons.md` and `references/interactions.md`. This reference is
about the usual application-level choices.

## Recommended defaults for applications

For an ordinary application icon:

* prefer a right-side sprite-only icon
* use a sprite-plus-text icon on the left side only when the application is
  deliberately following that convention
* if no better sprite is known, use the sprite name `application`

## Recommended geometry

For a right-side sprite-only application icon:

* start with `x0 = 0`
* start with `y0 = 0`
* start with `y1 = 68`
* read the sprite size in OS units and enlarge `x1` and `y1` if needed

For a left-side sprite-plus-text icon:

* start with `x0 = 0`
* start with `y0 = -16`
* start with `y1 = 84`
* start with width `12 + 16 * max(4, text_length)`
* enlarge the box if the sprite is bigger than the initial geometry

## Button type

For a clickable application icon:

* do not use button type `0` (`Never`)
* prefer a click-capable type such as `wimp_BCLICKDEBOUNCE`

If the icon shows but ignores clicks, verify the button type first, then the
event decoding.

## Click decoding

For `Wimp_Poll` button-change events, the practical button values are:

* `1` = Adjust
* `2` = Menu
* `4` = Select

Do not assume these are the same values as the more general button-state masks.
