# Program information

Use this reference when the user needs a standard program-information window, usually opened from the iconbar menu `Info` item.

## Asset

- Copy [../assets/window_proginfo.txt](../assets/window_proginfo.txt) into the destination `TemplateText` file.
- The asset contains a single `wimp_window` block with `template_name:"proginfo"`.

## Behaviour notes

- This window is usually opened from the main iconbar menu `Info` entry.
- Applications commonly populate the displayed fields programmatically during startup.
- The default window title is `About this program`.
- The usual populated fields are Name, Purpose, Author, and Version.
- The value fields use indirected text with `R2` validation and are intended to be filled at runtime.

## Sizing guidance

- Check the expected runtime text lengths before treating the bundled asset as final.
- For ordinary system-font text, a common width rule for an icon is `16 * nchars + 16` OS units.
- If a populated value, especially `Purpose`, will not fit the existing icon width, either:
  - widen the value icon and make the window correspondingly wider
  - or shorten the runtime text so that it fits the existing layout
- Do not leave the stock proginfo template width unchanged if the application is known to populate it with longer text that will clip or look cramped.

## Icon numbers

| Icon | Purpose | Notes |
| --- | --- | --- |
| 0 | Unused filler icon | Off-window filled icon; normally leave unchanged. |
| 1 | Name value | Indirected text filled by the application at startup. |
| 2 | Purpose value | Indirected text filled by the application at startup. |
| 3 | Author value | Indirected text filled by the application at startup. |
| 4 | Version value | Indirected text filled by the application at startup. |
| 5 | Name label | Static label `Name`. |
| 6 | Purpose label | Static label `Purpose`. |
| 7 | Author label | Static label `Author`. |
| 8 | Version label | Static label `Version`. |
