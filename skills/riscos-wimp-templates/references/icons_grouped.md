# Grouped icon boxes

Use this reference when creating a bordered group box with a label above related controls.

## Pattern

- Use a bordered indirected text icon as the group box.
- Use a separate sprite/text label icon near the top-left of the box to name the group.
- Start the grouped controls below the label, leaving clear space between the label and the first control row.

## Example geometry

From the example pane:

```text
Group box: extent 22,-440,632,-262
Label:     extent 46,-66,206,-22
First row: extent 60,-124,488,-80
Second row: extent 60,-176,428,-132
```

## Practical rules

- The group box should extend far enough above and below the contained controls to leave a visual margin.
- The label should sit inside the top region of the box, slightly inset from the left edge.
- Start the first control row below the label rather than level with it.
- Keep the left edges of grouped controls aligned unless the control type requires a different layout.
- Resize the box to fit the controls; do not make the controls fit an arbitrary box height.

## Example icon definitions

```text
wimp_icon {
  extent:22,-440,632,-262
  icon_flags:wimp_ICON_TEXT | wimp_ICON_BORDER | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text.text:""
  text.size:1
  text.validation:"R4"
}

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
```
