# Dialogue action buttons and divider

Use this reference when building the standard action-button row at the bottom of a dialogue box.

## Sources

- File: `WimpTemplates,fec`
- Template: `error`
- Source icons: 1, 4, 5, 6
- File: `Templates,fec`
- Template: `quit`
- Source icons: 0, 2, 3

## Pattern

- Put the default-confirmation button at the bottom right of the dialogue.
- Put any secondary action or cancel button immediately to its left on the same baseline.
- Separate the main dialogue content from the action row with a full-width `divider` sprite.
- Use standard grey desktop colours for the buttons; do not colour confirmation buttons specially.

## Captured geometry

- Default button height: `68` OS units.
- Default button width in the examples: `204` OS units (`R6,3`).
- Secondary action button height: `52` or `68` OS units in the captured templates. Prefer `52` for ordinary `R5,3` buttons and `68` when matching an existing family that already uses the taller style.
- Secondary action button width in the examples: `188` OS units (`R5,3`).
- When an ordinary `R5,3` button sits beside a default `R6,3` button, place the `R5,3` button `8` OS units higher so their visual centres align in the standard 3D style.
- Gap from visible right edge to the default button: `16` OS units in the `error` template. `riscos-fixuptemplate` prefers `20` OS units for a clean single-button dialogue row.
- Gap from visible bottom edge to the button row: `16` OS units in the `error` template. `riscos-fixuptemplate` prefers `20` OS units for a clean single-button dialogue row.
- Gap between adjacent action buttons: `10` OS units in the `error` template and `14` OS units in the `quit` template. The captured `Cancel` plus default `OK` pair in `ROBEInfo` uses `16` OS units and fits the family cleanly. Keep buttons in that family; `12` to `16` OS units is a reasonable default range for new work.
- Divider height: `16` OS units.
- Gap from the bottom of the divider to the top of the button row: `4` OS units in the `error` template and `6` OS units in the `quit` template. `riscos-fixuptemplate` prefers a cleaner `12` OS unit separation for a single-button row.
- Gap from the nearest content icon above to the top of the divider: keep the usual spacing family. The captured templates leave a larger visual pause here; `riscos-fixuptemplate` prefers `12` OS units in the simple dialogue case.

## Practical rules

- Use indirected text for any button label longer than `11` characters.
- Default buttons should use `R6,3`.
- Secondary action and cancel buttons should use `R5,3` unless the captured family clearly uses a different validation.
- Keep the default button as the rightmost button even when there is only one button in the row.
- When mixing `R5,3` and `R6,3` buttons in one row, do not force matching heights; keep the `R5,3` button narrower and shorter, and raise it `8` OS units.
- Make the divider at least as wide as the visible window and align it to the visible left edge.
- Keep buttons in one row visually aligned as a set. For mixed `R5`/`R6` rows, that means the shorter `R5` buttons sit `8` OS units higher rather than sharing the same bottom edge.
- Measure these gaps from the visible work area of the dialogue.
- For a simple two-row informational dialogue, keep the last content row `20` OS units above the divider and match that with a `20` OS unit gap from the top of the visible work area to the first content row.
- After laying out a new dialogue, run `riscos-fixuptemplate` and accept its action-row spacing corrections unless they conflict with an established captured family that you are deliberately preserving.

## Example icon definitions

```text
wimp_icon {
  extent:340,-238,528,-186
  icon_flags:wimp_ICON_TEXT | wimp_ICON_BORDER | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_FILLED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text.text:"Cancel"
  text.size:12
  text.validation:"R5,3"
}

wimp_icon {
  extent:544,-298,748,-230
  icon_flags:wimp_ICON_TEXT | wimp_ICON_BORDER | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_FILLED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text.text:"OK"
  text.size:12
  text.validation:"R6,3"
}

wimp_icon {
  extent:0,-218,768,-202
  icon_flags:wimp_ICON_SPRITE | wimp_ICON_VCENTRED
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  sprite_only:"divider"
}
```
