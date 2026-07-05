# Compact radio icons

Use this reference when laying out four or more radio icons in a compact grid rather than a single vertical list.

## Source

- File: `StyleGuide,fec`
- Template: `icons`
- Source icons: 10, 11, 15, 12

## Pattern

- Use sprite-and-text radio icons with `Sradiooff,radioon` validation.
- Keep the first column left-aligned and place additional choices in a second column when the set would become too tall.
- Keep every icon in the same exclusive-selection group.

## Example geometry

```text
None:      extent 52,-148,208,-104
Parallel:  extent 276,-148,476,-104
Serial:    extent 52,-200,216,-156
Net:       extent 276,-200,436,-156
ESG:       1
```

## Practical rules

- Keep the row spacing consistent across both columns.
- Align the radio sprite and label baselines between columns.
- Use this layout when a longer single-column set would waste horizontal space or push later controls too far down the pane.

## Example icon definitions

```text
wimp_icon {
  extent:52,-148,208,-104
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_RADIO
  icon_esg:1
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"None"
  text_and_sprite.size:5
  text_and_sprite.validation:"Sradiooff,radioon"
}

wimp_icon {
  extent:276,-148,476,-104
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_RADIO
  icon_esg:1
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"Parallel"
  text_and_sprite.size:9
  text_and_sprite.validation:"Sradiooff,radioon"
}

wimp_icon {
  extent:52,-200,216,-156
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_RADIO
  icon_esg:1
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"Serial"
  text_and_sprite.size:7
  text_and_sprite.validation:"Sradiooff,radioon"
}

wimp_icon {
  extent:276,-200,436,-156
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_RADIO
  icon_esg:1
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"Net"
  text_and_sprite.size:4
  text_and_sprite.validation:"Sradiooff,radioon"
}
```
