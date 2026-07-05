# Arbitrary input field

Use this reference when users may enter non-numeric values, so a plain writable field is more appropriate than a bumped numeric selector.

## Source

- File: `StyleGuide,fec`
- Template: `icons`
- Source icons: 18, 19

## Pattern

- Put a right-justified label on the left.
- Use a bordered writable field on the right.
- Leave the field general-purpose when the input is not constrained to numbers.

## Example geometry

```text
Label:       extent 64,-924,396,-884
Input field: extent 402,-930,544,-878
```

## Practical rules

- Use this pattern when the input might be symbolic, textual, or otherwise unsuitable for bump arrows.
- Keep the writable field wide enough for the expected input format.
- Add a stricter validation string only when the accepted syntax is well defined.

## Example icon definitions

```text
wimp_icon {
  extent:64,-924,396,-884
  icon_flags:wimp_ICON_TEXT | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_ICON_RJUSTIFIED
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_CREAM
  text.text:"Default screen mode"
  text.size:20
  text.validation:""
}

wimp_icon {
  extent:402,-930,544,-878
  icon_flags:wimp_ICON_TEXT | wimp_ICON_BORDER | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_FILLED | wimp_ICON_INDIRECTED | wimp_BUTTON_WRITE_CLICK_DRAG
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_WHITE
  text.text:"27"
  text.size:12
  text.validation:"Pptr_write"
}
```
