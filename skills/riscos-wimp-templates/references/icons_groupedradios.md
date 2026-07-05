# Grouped radio icons

Use this reference when creating a set of radio icons inside a grouped box.

## Pattern

- Use sprite-and-text icons with `Sradiooff,radioon` validation.
- Give all radios in one logical set the same exclusive-selection group.
- Use a different exclusive-selection group for a different set in another box.

## Example geometry

Layout group:

```text
Label:  extent 46,-66,206,-22
Radio:  extent 60,-124,488,-80
Radio:  extent 60,-176,488,-132
ESG:    1
```

Colours group:

```text
Label:  extent 46,-286,226,-242
Radio:  extent 60,-344,488,-300
Radio:  extent 60,-396,488,-352
ESG:    2
```

## Practical rules

- Keep each radio row aligned to the same left edge within the group box.
- Keep vertical spacing consistent between radio rows.
- Reuse the same ESG only within one mutually exclusive set.
- Change the ESG when a second independent radio set is present in the same pane.
- Keep related icons in the same set the same width and height where practical, using the largest required hit area for the whole set so the click target feels consistent.

## Example icon definitions

```text
wimp_icon {
  extent:46,-66,206,-22
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"Layout"
  text_and_sprite.size:7
  text_and_sprite.validation:"S"
}

wimp_icon {
  extent:60,-124,488,-80
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK
  icon_esg:1
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"Drawing and name"
  text_and_sprite.size:17
  text_and_sprite.validation:"Sradiooff,radioon"
}

wimp_icon {
  extent:60,-176,488,-132
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK
  icon_esg:1
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"Full info"
  text_and_sprite.size:10
  text_and_sprite.validation:"Sradiooff,radioon"
}

wimp_icon {
  extent:46,-286,226,-242
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"Colours"
  text_and_sprite.size:8
  text_and_sprite.validation:"S"
}

wimp_icon {
  extent:60,-344,488,-300
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK
  icon_esg:2
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"Desktop colours"
  text_and_sprite.size:16
  text_and_sprite.validation:"Sradiooff,radioon"
}

wimp_icon {
  extent:60,-396,488,-352
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK
  icon_esg:2
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:"BBC-style colours"
  text_and_sprite.size:18
  text_and_sprite.validation:"Sradiooff,radioon"
}
```
