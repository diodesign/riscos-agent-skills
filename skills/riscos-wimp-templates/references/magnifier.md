# Magnifier

Use this reference when the user needs a simple ratio-based scaling window, usually opened from a hotkey or attached as a submenu item.

## Asset

- Copy [../assets/window_magnifier.txt](../assets/window_magnifier.txt) into the destination `TemplateText` file.
- The asset contains a single `wimp_window` block with `template_name:"magnifier"`.

## Behaviour notes

- This is a compact scaling popup for editing a ratio directly.
- It is suitable for opening from a hotkey or as a submenu window.
- The ratio is represented as two writable numeric fields separated by `:`.
- Each numeric field has matching increment and decrement repeat buttons.
- The writable fields accept digits only through `A0-9;Pptr_write`.
- The default title is `Magnifier`, which can be kept or renamed to match the application.

## Icon numbers

| Icon | Purpose | Notes |
| --- | --- | --- |
| 0 | Left ratio value | Writable numeric field, default `999`. |
| 1 | Right ratio value | Writable numeric field, default `999`. |
| 2 | Left increment | Repeat button using `sup,pup`. |
| 3 | Left decrement | Repeat button using `sdown,pdown`. |
| 4 | Right increment | Repeat button using `sup,pup`. |
| 5 | Right decrement | Repeat button using `sdown,pdown`. |
| 6 | Ratio separator | Static `:` text between the two values. |
