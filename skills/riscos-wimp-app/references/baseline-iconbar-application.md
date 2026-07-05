# Baseline iconbar application

Use this reference when the user asks for a new ordinary desktop Wimp
application and does not ask for a different structure.

This is the baseline application shape we established for future work. It
describes the required behaviour and packaging, not a specific implementation
library. The same baseline may be built with `RISC_OSLib`, bare SWI calls,
OSLib, or another suitable Wimp layer.

If the user explicitly asks for an application without an iconbar icon, do not
apply the iconbar-specific parts of this baseline.

## Required packaged structure

The application should normally be packaged with:

* `!RunImage`
* `Resources/!Run`
* `Resources/!Boot`
* `Resources/!Sprites`
* `Resources/!Sprites22`
* `Resources/UK/!Help`
* `Resources/UK/Templates,fec`

The `Templates,fec` file should contain the program information window used by
the iconbar menu `Info` entry.

## Required baseline behaviour

Unless the user asks for something else, the application should:

* install a right-side iconbar icon
* respond to `Menu` over that icon with an iconbar menu
* provide `Info` as the first iconbar menu entry
* provide `Quit` as the last iconbar menu entry
* terminate when `Quit` is selected

Do not omit `Quit` from the iconbar menu in the baseline application.

## Program information window

The `Info` item should open a standard program information window as a menu
submenu.

That window should:

* be loaded from `Resources/UK/Templates,fec`
* be created during application startup, before the iconbar menu is used
* show the usual fields `Name`, `Purpose`, `Author`, and `Version`
* have those displayed values populated by the application at runtime
* allow the normal Wimp move/open protocol so the user can drag it

If a template contains indirected text, ensure the backing storage remains
valid for as long as the created window exists.

When creating or adjusting the proginfo template itself, also use the
`riscos-wimp-templates` skill and its proginfo reference.

Do not assume the stock proginfo width is always sufficient. Check the actual
runtime string lengths, especially `Purpose`.

For ordinary system-font text, a common icon width rule is:

* `16 * nchars + 16` OS units

If the populated proginfo text is too long for the existing layout, either:

* widen the proginfo value icons and make the window correspondingly wider
* or shorten the populated text so it fits the existing template cleanly

## Startup sequence

The baseline startup sequence is:

1. initialise the Wimp task
2. load any required templates
3. create the program information window from the loaded template
4. construct the iconbar menu, including the `Info` submenu handle
5. create the iconbar icon
6. enter the poll loop

Do not leave menu construction until after the event loop has already started
if the menu depends on created windows or template-loaded resources.

## Event-handling rules

For iconbar interaction:

* filter button events by iconbar window handle `-2`
* also filter by the specific icon handle returned when the icon was created
* decode the click according to the button type actually used for the icon
* treat `Menu`, `Select`, and `Adjust` as separate semantics

Do not test the wrong event-block field when deciding whether to open the
iconbar menu.

For the proginfo window:

* handle open-window requests with the normal Wimp open protocol
* pass the returned open block back to `Wimp_OpenWindow`

Do not create a moveable proginfo window and then ignore its open-window
requests, because that prevents normal dragging and reopening behaviour.

## Menu construction rules

For the baseline iconbar menu:

* attach the `Info` entry to the created information window as a submenu
* keep `Quit` as a direct leaf item
* use the standard menu colour separation:
  title colours in the menu header
  item colours in each item's icon flags

If the menu is opened from the iconbar, use the iconbar-specific placement
rules from the `riscos-wimp` menu reference rather than a generic in-window
popup formula.

## Slot sizing

After creating the baseline application and after later feature changes:

* check the size of the built `!RunImage`
* set `WimpSlot -min` to at least the binary size plus `32K`
* round that minimum up to a whole `4K` page size
* never set the minimum below `24K`
* keep `WimpSlot -max` greater than or equal to the minimum, usually matching
  it

Do not leave the skeleton `32K` slot values in place.
