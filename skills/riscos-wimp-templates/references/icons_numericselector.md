# Numeric selector with bump icons

Use this reference when creating a numeric selector with a label, a writable numeric field, decrement and increment bump icons, and a units suffix.

## Source

- File: `StyleGuide,fec`
- Template: `icons`
- Source icons: 5, 7, 6, 8, 9

## Pattern

- Put a right-justified label to the left of the value field.
- Place decrement and increment icons immediately beside the numeric field.
- Use a separate suffix label for the units rather than embedding them in the writable field.

## Example geometry

```text
Label:      extent 40,-512,216,-472
Value:      extent 232,-518,328,-466
Decrease:   extent 336,-510,372,-474
Increase:   extent 368,-510,404,-474
Units:      extent 414,-512,522,-472
```

## Practical rules

- Restrict the writable field validation to numeric input when only numbers are valid.
- Use repeat-click bump icons so users can hold the mouse button to step through values.
- Leave enough spacing between the field and units label that the units remain readable at small widths.

## Example icon definitions

```text
wimp_icon {
  extent:40,-512,216,-472
  icon_flags:wimp_ICON_TEXT | wimp_ICON_RJUSTIFIED | wimp_BUTTON_CLICK_DRAG
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_only:"Font cache"
}

wimp_icon {
  extent:232,-518,328,-466
  icon_flags:wimp_ICON_TEXT | wimp_ICON_BORDER | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_FILLED | wimp_ICON_INDIRECTED | wimp_BUTTON_WRITE_CLICK_DRAG
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_WHITE
  text.text:"1024"
  text.size:12
  text.validation:"a0-9;KARTN;Pptr_write"
}

wimp_icon {
  extent:336,-510,372,-474
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_REPEAT
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:""
  text_and_sprite.size:1
  text_and_sprite.validation:"R5;sdown,pdown"
}

wimp_icon {
  extent:368,-510,404,-474
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_REPEAT
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:""
  text_and_sprite.size:1
  text_and_sprite.validation:"R5;sup,pup"
}

wimp_icon {
  extent:414,-512,522,-472
  icon_flags:wimp_ICON_TEXT | wimp_ICON_VCENTRED | wimp_BUTTON_CLICK_DRAG
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_CREAM
  text_only:"KBytes"
}
```
