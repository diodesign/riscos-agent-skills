# Dialogue Boxes

## Contents

- Types
- Keyboard and default actions
- Standard controls
- Standard dialogues
- Wording and toolboxes

## Use this reference for

- Dialogue layout and behaviour
- Choosing between persistent and transient dialogues
- Button naming and default actions
- Standard save/print/find/font/colour dialogues
- Dialogue wording and error text

## Types

- Use persistent dialogues when the user may want to keep the dialogue open while working.
- Mark persistent-dialogue menu entries with an ellipsis.
- Use transient dialogues for short-lived confirmations or focused interactions.
- Keep both types delayed-action unless immediate feedback is the established convention for that control.
- Do not put a `Close` icon on a transient dialogue that should instead have explicit action and cancel buttons.

## Keyboard and default actions

- Give the dialogue input focus when it opens and when it is clicked.
- Make `Return` trigger the default action.
- Make `Escape` perform the same action as `Cancel`.
- Show the default action clearly, including the thicker border convention on the corresponding button.
- Keep the dialogue open after `Adjust` on an action button.
- Make dialogues opened from shortcuts behave exactly like dialogues opened from menus.

## Control choice and behaviour

- Use standard writable fields, display fields, action buttons, option buttons, radio buttons, adjusters, sliders, scrollable lists, and pop-up menus.
- Support normal writable-field editing keystrokes.
- Always provide `Cancel` where state must be restorable.
- Ensure cancelling reverts the environment to its pre-dialogue state and does not lose data.
- Grey out unavailable options instead of removing them.

## Geometry and button rows

- Separate the main content from the button row with a horizontal divider.
- Keep `12` OS units between the controls above the divider and the divider itself.
- Keep the main button row `20` OS units above the bottom of the window.
- When a default button appears alongside ordinary action buttons, the ordinary buttons should sit `8` OS units higher so their visual centres align with the taller default button.
- Leave `20` OS units from the left and right window edges to the outermost buttons.
- Keep `16` OS units between neighbouring buttons within one button group.
- When a dialogue has local-operation buttons on the left and activation buttons on the right, separate the groups by `40` OS units.
- Make the space from the divider down to the window bottom `84` OS units with only ordinary action buttons, or `100` OS units when a default button is present.
- Keep only one default button in a window, and place it at the bottom right.
- Measure dialogue spacing from the visible work area.
- In a simple vertically stacked dialogue, balance the content so the gap from the top of the visible work area to the first row matches the gap from the last content row to the divider.
- For a two-row informational dialogue, a good captured balance is `20` OS units above the first row and `20` OS units below the last row before the divider.

## Button wording

- Keep action and default button labels to a single word where practical.
- Buttons that open a further dialogue or defer completion should carry an ellipsis.
- Default buttons should not themselves be the buttons that open a further dialogue.
- Buttons above the divider normally represent local operations and should use an ellipsis.
- Buttons below the divider on the left should use an ellipsis.
- Buttons below the divider on the right should not use an ellipsis.
- Encode button text indirectly once the label is longer than `11` characters.

## Standard dialogues

- Reuse the standard patterns for `Print`, `Save`, `Scale view`, `Find/Replace`, colour selection, font selection, and close-confirmation dialogues.
- Use the standard save dialogue and save semantics for file output.
- Use standard print controls and wording rather than custom print workflows unless strictly necessary.
- Prefer explicit action labels such as `Save`, `Print`, `Find`, or `OK` when they communicate the outcome better than a vague label.

## Wording

- Use clear plain English and avoid technical jargon.
- Phrase controls and actions so the user can predict the effect before committing.
- Make error messages specific, polite, and actionable.
- Keep wording concise enough to fit cleanly without layout hacks.

## Toolboxes

- Use a toolbox when repeated rapid selection is more natural than repeated opening and closing of a dialogue box.
- Keep toolbox contents visibly grouped and immediately usable.
