# Slider selector

Use this reference when creating a proportional selector row with a label, decrement and increment arrows, and a bar that shows the current value.

## Source

- File: `StyleGuide,fec`
- Template: `icons`
- Source icons: 1, 27, 22, 23, 24, 26

## Pattern

- Put a right-justified label to the left of the slider.
- Use repeat-click left and right arrow icons at the ends.
- Build the slider body from a bordered outer icon plus separate background and filled-value icons.

## Example geometry

```text
Label:          extent 40,-436,152,-396
Decrease:       extent 158,-432,190,-400
Outer bar:      extent 196,-436,518,-396
Bar background: extent 208,-424,506,-408
Bar value:      extent 208,-424,357,-408
Increase:       extent 528,-432,560,-400
```

## Practical rules

- Keep the inner bar icons inset from the border so the outline remains visible.
- Resize only the filled-value icon to reflect the current proportion.
- Use repeat-click arrows when the control should ramp continuously while held down.

## Example icon definitions

```text
wimp_icon {
  extent:40,-436,152,-396
  icon_flags:wimp_ICON_TEXT | wimp_ICON_VCENTRED | wimp_ICON_RJUSTIFIED
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_only:"Volume"
}

wimp_icon {
  extent:158,-432,190,-400
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_REPEAT
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_LIGHT_GREY
  text_and_sprite.text:""
  text_and_sprite.size:1
  text_and_sprite.validation:"R5;sleft,pleft"
}

wimp_icon {
  extent:196,-436,518,-396
  icon_flags:wimp_ICON_TEXT | wimp_ICON_BORDER | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK_DRAG
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text.text:""
  text.size:12
  text.validation:"N5//23/24;R2"
}

wimp_icon {
  extent:208,-424,506,-408
  icon_flags:wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_FILLED | wimp_BUTTON_CLICK_DRAG
  icon_esg:0
  icon_fg:wimp_COLOUR_VERY_DARK_GREY
  icon_bg:wimp_COLOUR_WHITE
}

wimp_icon {
  extent:208,-424,357,-408
  icon_flags:wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_FILLED | wimp_BUTTON_CLICK_DRAG
  icon_esg:0
  icon_fg:wimp_COLOUR_VERY_DARK_GREY
  icon_bg:wimp_COLOUR_DARK_GREY
}

wimp_icon {
  extent:528,-432,560,-400
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_REPEAT
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_LIGHT_GREY
  text_and_sprite.text:""
  text_and_sprite.size:1
  text_and_sprite.validation:"R5;sright,pright"
}
```
