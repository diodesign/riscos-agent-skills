# File information

Use this reference when the user needs a simple document or object information window.

## Asset

- Copy [../assets/window_fileinfo.txt](../assets/window_fileinfo.txt) into the destination `TemplateText` file.
- The asset contains a single `wimp_window` block with `template_name:"fileinfo"`.

## Behaviour notes

- This is a general pattern for a document or object information window.
- The name of the file or object appears at the top of the window.
- Property display fields appear beneath the name.
- Display fields should line up in a vertical column on their left and right edges.
- This example uses two columns of properties, but that depends on the information being shown.
- If there are fewer properties, or if the property values are longer, a single column may be more appropriate.
- The window size may be increased or reduced using the usual style constraints to fit the number of properties shown.
- The fields are display-only indirected text areas intended to be populated by the application.

## Icon numbers

| Icon | Purpose | Notes |
| --- | --- | --- |
| 0 | OK button | Standard dismiss button, not visible |
| 1 | Object name | Top display field for the file or object name. |
| 2 | Property value 1 | Left column value field. |
| 3 | Property value 2 | Left column value field. |
| 4 | Property value 3 | Left column value field. |
| 5 | Property value 4 | Right column value field. |
| 6 | Property value 5 | Right column value field. |
| 7 | Property value 6 | Right column value field. |
| 8 | Property label 1 | Left column label. |
| 9 | Property label 2 | Left column label. |
| 10 | Property label 3 | Left column label. |
| 11 | Property label 4 | Right column label. |
| 12 | Property label 5 | Right column label. |
| 13 | Property label 6 | Right column label. |
