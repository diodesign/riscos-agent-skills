# Colour selector

Use this reference when creating a colour-selector row with a label, a colour swatch icon, and a menu button that opens the ColourPicker.

## Pattern

- Place a right-justified text label on the left.
- Place the colour swatch icon in the middle.
- Place a menu button icon immediately to the right of the swatch.

## Example geometry

```text
Label:       extent 64,-596,314,-548
Colour box:  extent 320,-598,532,-546
Menu button: extent 544,-598,590,-546
```

## Practical rules

- The label should be vertically centred with the swatch row.
- The swatch should be wide enough to show the selected colour clearly.
- The menu button should sit close to the swatch and use a menu-pointer validation.
- Update the swatch icon to use `C...` validation with the selected RGB values.
- The text in the swatch may be removed once the colour is shown clearly, or replaced with a short explanatory message if needed.

## Example icon definitions

```text
wimp_icon {
  extent:64,-596,314,-548
  icon_flags:wimp_ICON_TEXT | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_ICON_RJUSTIFIED
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text.text:"Mask colour"
  text.size:12
  text.validation:""
}

wimp_icon {
  extent:320,-598,532,-546
  icon_flags:wimp_ICON_TEXT | wimp_ICON_BORDER | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_FILLED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_LIGHT_BLUE
  text.text:"Meeces!!!"
  text.size:13
  text.validation:"CCC0077/4488CC"
}

wimp_icon {
  extent:544,-598,590,-546
  icon_flags:wimp_ICON_TEXT | wimp_ICON_SPRITE | wimp_ICON_HCENTRED | wimp_ICON_VCENTRED | wimp_ICON_INDIRECTED | wimp_BUTTON_CLICK
  icon_esg:0
  icon_fg:wimp_COLOUR_BLACK
  icon_bg:wimp_COLOUR_VERY_LIGHT_GREY
  text_and_sprite.text:""
  text_and_sprite.size:1
  text_and_sprite.validation:"YS;R5;sgrightc,pgrightc;pptr_menu"
}
```
