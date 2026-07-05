# Informational label and display field

Use this reference when showing read-only information as a label plus a bordered display field.

## Source

- File: `StyleGuide,fec`
- Template: `icons`
- Source icons: 20, 21

## Pattern

- Put a right-justified label on the left.
- Use a bordered indirected text field on the right for the displayed value.
- Keep the field read-only when the user is not expected to edit it.
- Unless otherwise directed, always capitalise the label.

## Example geometry

```text
Label:         extent 32,-840,164,-800
Display field: extent 164,-846,640,-794
```

## Practical rules

- Use indirected text for static labels once the text is longer than `11` characters.
- Use a display field rather than plain text when long values need a bounded region or standard field appearance.
- Keep the label width stable so several information rows can align cleanly in a pane.
- In a simple dialogue with stacked information rows, align the rows against the visible work area so the top margin matches the clearance above the divider or action-row separator.
- Preserve read-only validation on the display field unless the row is being changed into an editable control.

## Example icon definitions

```text
wimp_icon {
  extent:32,-840,164,-800
  icon_flags:wimp_ICON_TEXT | wimp_ICON_VCENTRED | wimp_ICON_RJUSTIFIED
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_only:"Author"
}

wimp_icon {
  extent:164,-846,640,-794
  icon_flags:wimp_ICON_TEXT | wimp_ICON_BORDER | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_FILLED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK_DRAG
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text.text:"\u00A9 Acorn Computers Ltd, 1993"
  text.size:28
  text.validation:"R2"
}
```
