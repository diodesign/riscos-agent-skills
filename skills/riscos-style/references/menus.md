# Menus

## Use this reference for

- Main menu design
- Standard menu names and ordering
- Icon bar menus
- Submenus, persistent dialogues, and Adjust behaviour

## Core behaviour

- Provide one menu tree per window type that needs menus, plus an icon bar menu.
- Display the main menu when `Menu` is pressed in the relevant window.
- Display the icon bar menu when `Menu` is pressed over the icon bar icon.
- Open the menu at the pointer position.
- Allow menus, submenus, and dialogue boxes to be moved by dragging.

## Choosing items

- Grey out unavailable items instead of omitting them.
- Let `Select`, `Adjust`, or `Menu` choose a leaf item.
- After `Select` or `Menu`, dismiss the menu tree.
- After `Adjust`, leave the menu tree open so the user can make more choices.
- If an item leads to a submenu, pressing on the parent should either do nothing or perform a sensible default from that submenu.

## Structure

- Keep the menu tree balanced and avoid hiding frequent actions deep in submenus.
- Use the standard menu families where they fit: `File`, `Edit`, `Effect`, `Style`, and `Utilities`.
- Keep `Info` and `Quit` in the icon bar menu in the standard positions.
- Put dialogue-launching items in menus where users would naturally look for them.
- Put file lifecycle actions such as load, save, save as, and print under `File` when the application supports them.
- Put selection and clipboard actions under `Edit` when the application supports them.
- Use `Effect` or `Style` for transformations and presentation choices rather than mixing them into unrelated menus.

## Ellipses and arrows

- Use an ellipsis for an item that opens a persistent dialogue box.
- Use a submenu arrow for an item that leads to a submenu.
- Never combine an ellipsis and a submenu arrow on the same item.

## Standard content guidance

- Use standard items for loading, saving, printing, selection, clipboard actions, and similar common operations where the application type supports them.
- Keep labels plain and predictable so users can transfer expectations from other RISC OS applications.
- Use keyboard shortcuts consistently with the keyboard guidance.

## Appearance

- Keep text concise and avoid over-wide menus.
- Preserve the guide's menu spacing, colours, and dimensions through the implementation rules.
- Prefer small submenu widths because they reduce pointer travel.
