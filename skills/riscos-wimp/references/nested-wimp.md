# Nested Wimp Extensions

Use this file when the task may rely on the Acorn nested-window-manager extensions rather than only the base PRM Wimp behaviour.

Public references:

* Nested Window Manager functional specification: `https://gerph.github.io/riscos-prminxml-staging/prm/html/acorn/nested_window_manager/nested_window_manager.html`
* Base Wimp PRM chapter: `http://www.riscos.com/support/developers/prm/wimp.html`

## Scope

The nested-window-manager note documents later Wimp extensions including:

* child and nested windows
* furniture windows
* icon bar auto-fronting
* icon bar scroll behaviour changes
* 24-bit icon colours
* border-less windows
* redraw optimisation
* additional filter-related behaviour

Do not assume these features are available just because the base Wimp APIs exist.

## Wimp_Initialise versioning

The note documents version `380` as the initialise version needed, at a sufficiently advanced Wimp version, to activate most nested-Wimp features.

Guidance:

* if code depends on nested-Wimp behaviour, check the returned Wimp version and the initialise version passed
* do not assume passing `300` or `310` is enough for features such as child-window semantics
* do not assume current limited behaviour around version gating will remain stable in future releases

## Child windows

Child windows are windows linked to a parent and displayed within that parent.

The note says each edge and both scroll offsets of a child window can be independently linked to:

* the parent work area
* the left or bottom of the parent visible area
* the right or top of the parent visible area

This is a real protocol extension, not just a UI convention.

When reviewing or writing nested-window code:

* keep parent/child ownership separate from task ownership
* do not assume child and parent belong to the same task
* verify whether clipping is against the parent visible area or the outline/furniture case

## Furniture windows

Furniture windows are child windows allowed to overlap the parent furniture area.

The note documents:

* a child-window flag for furniture-window behaviour
* scrollbar accommodation rules when a child touches the relevant outer edge and end of the scrollbar

This is specialised behaviour. Use it only when the UI genuinely needs window-furniture augmentation.

## Extended Wimp_OpenWindow

The note documents an extended `Wimp_OpenWindow` form:

* `R2 = "TASK"` magic word
* `R3 = parent handle` or `-1`
* `R4 = extended flags`

Important points:

* do not accidentally leave `R2` holding `"TASK"` in mixed old/new call paths
* in C veneers, stale registers are a real risk here
* the extended form is used by cross-task embedding protocols as well as by same-task nested UIs
* if `R4 bit 0` is set, `R1 + 32` supplies new window flags to apply at open time
* `R1 = 0` or `-1` can be used to flush pending opens in the extended form

If a task uses nested windows, document clearly whether it is using old or extended open-window calls.

## Extended Wimp_GetWindowState

The note says `Wimp_GetWindowState` mirrors the extended `Wimp_OpenWindow` behaviour when `R2 = "TASK"`.

This matters when the code expects parent or extended-flag information back from the Wimp.

## Window flag extensions

The note documents extensions and reinterpretations in the window block, including:

* a Wimp-managed status bit related to shift-toggle full-size behaviour without covering the icon bar
* a child-window furniture flag
* a special title/window-frame colour byte value of `&FF` to remove the one-pixel border while still allowing furniture
* revised minimum-width and minimum-height behaviour enabling windows to shrink further in the nested Wimp

Do not carry these meanings back into base-Wimp code without checking the active Wimp level.

## Icon extensions

The note documents:

* 24-bit icon colour specification through the validation-string colour command
* line-spacing command behaviour being honoured
* clarification that icon flags bit 20 is reserved and not part of the ESG number

This is useful when reviewing code that assumes old ESG packing or old icon-colour limits.

## Menu and icon bar behaviour

The note also documents:

* corrected submenu/dialogue positioning for reversed menus
* icon bar auto-fronting when the pointer dwells on the bottom screen row
* icon bar scrolling regulation and acceleration

If code is sensitive to icon bar visibility or reversed-menu positioning, check whether the behaviour being relied upon is base-PRM or nested-Wimp era.

## Redraw and performance

The note documents improved invalid-rectangle handling and block-copy optimisation.

For debugging:

* if a behaviour difference appears only on a nested Wimp, do not assume the redraw order or rectangle generation will match older Wimps exactly
* keep protocol correctness, but do not overfit logic to one invalid-rectangle sequence
