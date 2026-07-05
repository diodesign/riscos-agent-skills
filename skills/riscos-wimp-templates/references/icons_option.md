# Option icon

Use this reference when creating a single on/off option row with a sprite that shows the off and on states.

## Source

- File: `StyleGuide,fec`
- Template: `icons`
- Source icon: 16

## Pattern

- Use one sprite-and-text icon for the whole row.
- Put the option text to the right of the sprite.
- Toggle the sprite between off and on artwork through the validation string.

## Example geometry

```text
Option row: extent 40,-590,632,-546
```

## Practical rules

- Use this for independent options rather than mutually exclusive choices.
- Keep the clickable area wide enough to include both the sprite and the caption.
- Reuse the same validation format when matching the standard option button appearance.

## Example icon definitions

```text
wimp_icon {
  extent:40,-590,632,-546
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_RELEASE_DRAG
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"Horizontal scroll"
  text_and_sprite.size:18
  text_and_sprite.validation:"N7/;soptoff,opton"
}
```
