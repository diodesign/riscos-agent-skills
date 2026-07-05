# Multi-page choices

Use this reference when the user needs a complex choices window made from a controller window plus one pane window per choices page.

## Assets

- Copy [../assets/window_multichoices.txt](../assets/window_multichoices.txt) into the destination `TemplateText` file.
- Copy [../assets/window_mutlichoices_pane.txt](../assets/window_mutlichoices_pane.txt) into the destination `TemplateText` file.
- The controller asset contains `template_name:"multichoices"`.
- The example pane asset contains `template_name:"mutlichoices_pane"`.

## Behaviour notes

- This is a composite window pattern for complex application choices.
- The controller window contains the action buttons and a vertical set of radio icons naming the available choices panes.
- Each radio icon corresponds to a separate pane window template.
- Opening the controller should also open the currently selected pane.
- Selecting a different radio icon should close the previously selected pane and open the new associated pane.
- There should normally be one pane window template for each controller radio icon.
- The included pane example is based on `choices_disp` and shows one possible choices page layout.
- Read [icons_grouped.md](icons_grouped.md), [icons_groupedradios.md](icons_groupedradios.md), and [icons_colourselector.md](icons_colourselector.md) when creating additional panes.
- Keep related radio-icon sets to the same width and height where practical so their click areas feel consistent across the window.

## Controller icon numbers

| Icon | Purpose | Notes |
| --- | --- | --- |
| 0 | Pane host area | Reserved area beside the divider for the associated pane window. |
| 1 | Divider | Vertical divider sprite between controller and pane area. |
| 2 | Set button | Applies the selected choices. |
| 3 | Cancel button | Closes the choices UI without applying changes. |
| 4 | Save button | Saves choices. |
| 5 | Pane selector 1 | Radio icon for the first pane. |
| 6 | Pane selector 2 | Radio icon for the second pane. |
| 7 | Pane selector 3 | Radio icon for the third pane. |
| 8 | Pane selector 4 | Radio icon for the fourth pane. |
| 9 | Pane selector 5 | Radio icon for the fifth pane. |

## Example pane icon numbers

| Icon | Purpose | Notes |
| --- | --- | --- |
| 0 | Group box 1 | Example grouped box for layout-related controls. |
| 1 | Group box 2 | Example grouped box for colour-related controls. |
| 2 | Layout option 1 | Radio icon in exclusive group `1`. |
| 3 | Layout option 2 | Radio icon in exclusive group `1`. |
| 4 | Colour option 1 | Radio icon in exclusive group `2`. |
| 5 | Colour option 2 | Radio icon in exclusive group `2`. |
| 6 | Group 1 label | Static grouped-box title `Layout`. |
| 7 | Group 2 label | Static grouped-box title `Colours`. |
| 8 | Group box 3 | Example grouped box for mask-display controls. |
| 9 | Group 3 label | Static grouped-box title `Mask display`. |
| 10 | Colour label | Static label `Mask colour`. |
| 11 | Colour swatch | Example colour display icon; update its `C` validation to the selected RGB values. |
| 12 | Colour menu button | Menu icon for opening the ColourPicker. |
