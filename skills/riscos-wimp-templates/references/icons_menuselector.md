# Menu selector row

Use this reference when creating a row with a label, a display field showing the current choice, and a menu or chooser icon to the right.

## Source

- File: `StyleGuide,fec`
- Template: `icons`
- Source icons: 25, 2, 3

## Pattern

- Place a right-justified label on the left.
- Use a bordered indirected text field to show the current selection.
- Place a chooser button immediately to the right of the field.

## Example geometry

```text
Label:          extent 40,-324,152,-284
Value field:    extent 160,-330,528,-278
Chooser button: extent 542,-328,584,-280
```

## Practical rules

- Use this pattern when the option list is longer than a short radio group, or when the available choices are dynamic.
- Keep the chooser button close enough to read as part of the same control.
- Preserve a writable-looking field only if users can type into it; otherwise keep it read-only as in the example.

## Example icon definitions

```text
wimp_icon {
  extent:40,-324,152,-284
  icon_flags:wimp_ICON_TEXT | wimp_ICON_VCENTRED | wimp_ICON_RJUSTIFIED
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_only:"Voice"
}

wimp_icon {
  extent:160,-330,528,-278
  icon_flags:wimp_ICON_TEXT | wimp_ICON_BORDER | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_FILLED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text.text:"WaveSynth-Beep"
  text.size:21
  text.validation:"R2"
}

wimp_icon {
  extent:542,-328,584,-280
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_RELEASE
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:""
  text_and_sprite.size:1
  text_and_sprite.validation:"Sgright,pgright;R5"
}
```
