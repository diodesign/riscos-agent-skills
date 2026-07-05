# Standard window defaults

Use this reference when creating a new ordinary Wimp window that is not already covered by one of the bundled assets.

## Starting point

- Start from [../assets/window_document.txt](../assets/window_document.txt) when you need a normal `New Format` window shell with standard title colours and standard scroll/icon setup.
- For a non-user-redrawn dialogue or choices pane, change the document window's work area from transparent to grey `1` and then remove scroll bars, resize, and toggle icons if the window does not need them.
- Keep the standard title colours from the document template: black title text on light grey title background, with `text.validation:""` so the title uses the normal desktop colours.
- If the window keeps a close icon, also keep the back icon.
- Do not leave a resize icon on its own; if there are no scroll bars, remove resize and toggle as well.
- When sizing and placing dialogue content, use the visible work area as the geometry reference rather than the outer window position.

## Practical grey mapping

- Use `wimp_COLOUR_VERY_LIGHT_GREY` for Grey `1` in the work area. This mapping was confirmed locally from the exported headers (`wimp_VERY_LIGHT_GREY 1`) and by live template checks.
- In the same live checks, `wimp_COLOUR_LIGHT_GREY` rendered as Grey `2` and `wimp_COLOUR_MID_LIGHT_GREY` rendered as Grey `3`. Treat those as the next darker standard greys when matching an existing design.
- Use the symbolic colour names in `TemplateText`, but keep these numeric notes in mind when the user asks for a specific grey number.
- Keep ordinary desktop windows on standard Wimp colours rather than title-validation colour overrides.

## Grouped-box layout notes

- Read [icons_grouped.md](icons_grouped.md) and [icons_groupedradios.md](icons_groupedradios.md) together when building a labelled group box with radio choices.
- The captured grouped-box geometry already bundled in this skill is the preferred baseline:
  - Group box top/left inset: `22` OS units from the pane edge in the example pane.
  - Group label extent: `46,-66,206,-22`.
  - First radio row extent: `60,-124,488,-80`.
  - Second radio row extent: `60,-176,488,-132`.
- Keep the label near the top-left inside the group header area, but not pressed against the top border.
- A good rule from the captured templates is that the label's vertical centre sits about `4` OS units below the top of the group box.
- Leave clear space between the label and the first control row; do not let the first row rise into the label area.
- Leave visible clearance below the final control row before the bottom of the group border; do not let the border sit tight against the last radio icon.

## Style-guide cross-checks

- Re-check `/etc/agentskills/riscos-style/references/implementation.md` for control heights and spacing:
  - Keep ordinary control-to-control spacing at `8` OS units.
  - Use `44` OS units for radio control height.
  - Keep at least `12` OS units between controls and the visible window edge.
- Re-check `/etc/agentskills/riscos-style/references/visual-design.md` for standard control presentation:
  - Use standard desktop colours outside the work area.
  - Group borders are channel borders only; the label is a separate icon.
  - Radio controls should use the standard `radiooff,radioon` sprites, visible text, no border, and a non-zero ESG.
