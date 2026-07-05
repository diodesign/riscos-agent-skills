# Updating the skill

Use this reference when adding another bundled window template or another supporting icon/layout reference to `riscos-wimp-templates`.

## Goal

Keep the main `SKILL.md` short, keep one reference file per window type or reusable icon/layout pattern, and keep reusable template text in `assets/`.

## Process

1. Decide whether the new material is:
   - a single reusable window template,
   - a grouped set of window templates that only make sense together, or
   - a supporting icon/layout pattern that should be documented as a reference rather than stored as a full window asset.
2. Identify the source template or resource file that contains the window or pattern to copy.
3. Convert that file to text with `riscos-ccres <infile> <outfile>` when the source is a binary template file.
4. Extract the required `wimp_window` block or blocks.
5. Store each reusable window block in `assets/window_<window-type>.txt`.
6. Rename `template_name` in each asset if the skill needs a clearer reusable name than the original source template name.
7. Create `references/<window-type>.md` for that window type or grouped set.
8. If the work is really a reusable icon/layout pattern, create a focused reference such as `references/icons_<pattern>.md`.
9. Add a short entry in `SKILL.md` pointing to the new reference file and any related assets.

## Information to record for each window type

- The source file and original template name.
- The asset path that should be copied into the destination `TemplateText`.
- A short note about what the window is for.
- The icon numbers and their purposes, recorded in a table.
- Any validation strings, drag behaviour, writable fields, or other details that an agent must preserve.
- Any required placeholder substitutions, such as filetype-specific validation strings like `Sfile_fff` changing to `Sfile_xxx`.
- The `riscos-ccres` commands needed both to extract from an `&FEC` file and to rebuild an `&FEC` file from `TemplateText`.
- Whether the window is meant to be used on its own or as part of a composite set.
- Any associated companion panes or controller windows that must be copied together.
- Any supporting icon-construction references that should be read with the window, such as grouped boxes, grouped radios, or colour selectors.
- Any standard runtime-populated fields, title substitutions, or geometry adjustments that the application is expected to make.
- Whether related icons in the same set should be normalised to the same width and height, which should usually be done using the largest required hit area in that set, except where different control styles are intentionally signalling different actions.

## Structure rules

- Put documentation in `references/`.
- Put reusable template blocks in `assets/`.
- Keep each reference limited to one window type so the skill uses progressive disclosure cleanly.
- If multiple window assets only make sense together, describe them together in one reference and state clearly that they must be copied together.
- Keep supporting icon/layout guidance in dedicated references such as `icons_grouped.md`, `icons_groupedradios.md`, and `icons_colourselector.md`.
- Keep related clickable icons the same width and height where practical so users get consistent hit areas across a set of radios or chooser controls, but do not force this when differing button styles are intentional, such as mixed `R6` default buttons and `R5` action buttons.
- Wherever `R5` and `R6` icons are paired, do not make them the same size by default; check the relevant sizing rules in the style guide before adjusting their geometry.
- Do not bundle unrelated windows into the same asset file.
- Do not create an asset when a short reference with example icon definitions is the better fit.

## Validation

- Re-read the asset and confirm it is a complete `wimp_window` block.
- Re-read the reference file and confirm every icon number matches the icon order in the asset.
- If multiple assets belong together, re-read the reference and confirm it explains the relationship between them.
- If the addition introduces a reusable icon/layout pattern, confirm the geometry and validation examples match the example window assets.
- Check that related clickable icons within one logical set have matching widths and heights unless there is a clear reason not to, such as intentionally different default/action button styles.
- Where a set includes paired `R5`/`R6` buttons, confirm that their sizes follow the style-guide rules rather than a generic equal-size rule.
- If the window follows a recognised desktop pattern, note that and route style-sensitive work through `riscos-style`.
