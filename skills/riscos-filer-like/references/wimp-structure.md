# Wimp Structure For A Filer-Like View

Use this file after `design.md` when turning the filer-like model into a working Wimp task.

For lower-level Wimp protocol rules, use the `riscos-wimp` skill alongside this reference.

## Scope

This reference covers:

* the window and object records a filer-like view typically needs
* the Wimp events that matter
* redraw, open, click, and key handling structure
* relayout and per-item invalidation paths

It does not prescribe a programming language.

## Suggested internal objects

Keep at least these concepts distinct:

* view record
  * window handle
  * current view format
  * item size and spacing
  * cached width metrics
  * current focused item
  * item count
  * colours and style settings
  * link to the backing object collection
* item record
  * stable identity
  * displayed label and optional metadata fields
  * icon or sprite identity
  * state flags such as selected, highlighted, shaded
* backing collection
  * ordered list or array of item identities
  * lookup from identity to item data
  * optional sort and refresh state

The view record should own Wimp-facing state. The backing collection should own the data.

## Window lifecycle

Typical lifecycle:

1. Create the view record with default geometry and style.
2. Create the Wimp window from the initial object dimensions.
3. Populate items from the backing collection.
4. Recompute width, columns, rows, and extent.
5. Open the window.
6. Enter the poll loop.

If object size, background behaviour, or title changes force window recreation:

* preserve open state
* preserve current focus or caret information
* preserve any nested-window parentage if used
* restore the window before resuming normal interaction

## Poll-loop structure

At minimum, a filer-like task usually needs structured handling for:

* redraw requests
* open window requests
* close window requests
* mouse clicks
* key presses
* menu selections or warnings if menus are used

Keep the dispatcher thin. It should identify the view from the window handle, then call a focused helper for that path.

## Open-window handling

Open-window handling should not just call `Wimp_OpenWindow` blindly for a filer-like view.

The open path is where you usually:

* read the new visible width
* derive column count
* update extent if the object geometry requires relayout
* preserve scroll offsets where possible
* then reopen the window

Distinguish:

* user-driven open or resize
* relayout because item count changed
* relayout because view format changed

Those paths often share code, but they are not identical.

## Redraw handling

A good redraw helper usually needs:

* the view record
* the redraw rectangle or redraw block
* a callback or helper to draw one item

Sequence:

1. Begin the redraw protocol.
2. Convert the current redraw rectangle into candidate rows and columns.
3. Visit only the intersecting items.
4. Draw each item from its record and current view format.
5. Continue until the Wimp says no more rectangles remain.

Support these redraw granularities explicitly:

* full visible redraw
* redraw one item
* redraw a known rectangle when a structural overlay changed

## Per-item invalidation

Single-item redraw should be a first-class path.

Use it for:

* selection changes
* highlight movement
* item metadata changes
* icon changes
* shading or availability changes

The per-item redraw path should derive the item bounds from the same box calculation used by hit-testing and full redraw.

In some detailed views it is useful to distinguish:

* the horizontal advance to the next item cell
* the actual width that needs repainting for a focused redraw

This is optional, but it can help when the first part of the cell behaves like a classic filer icon and the remainder is auxiliary metadata. If you do this, document the distinction clearly so redraw, hit-testing, and extent code do not drift apart.

## Click handling

Click handling generally follows:

1. map screen coordinates to an item index
2. reject clicks that land in spacing or outside live item bounds
3. if needed, refine to a subregion inside the item
4. apply button semantics

Common button behaviours:

* Select: focus or select object, sometimes activate on double-click
* Adjust: alternate open, add/remove selection, or move to parent
* Menu: open object or background menu

Do not let click handlers infer item geometry independently from redraw.

If menu clicks should temporarily act on the clicked object without changing the normal persistent selection, model that transient selection state explicitly and redraw only the affected item or items.

## Key handling

Key handling should be expressed in object movement terms:

* previous or next item
* left or right within the current grid
* page up or page down by visible rows
* activate current item
* return to parent or previous level
* switch view format
* jump to next item matching a typed prefix

A key move normally does three things:

* update current-item state
* redraw old and new items
* scroll the new current item into view if needed

## Menus and exposed commands

If the interface has multiple view formats or sort orders, expose them as explicit commands rather than hidden key-only state.

Useful menu groups:

* view format
* sort mode
* refresh
* open parent
* object actions on the current item

Keep command handlers separate from raw Wimp menu decoding so the same operations can be invoked from keys, clicks, or menus.

For some interfaces it is useful to distinguish:

* background menu with no current object
* object menu on a transiently selected object
* object menu on the persistent current selection

That behaviour is optional, but if used it should be deliberate and visible in the view state model.

## Sorting hooks

Sorting belongs at the backing collection layer.

The Wimp view should ask for the current ordered sequence, not invent ordering during redraw.

Suggested structure:

* keep a sort mode value on the collection or controller
* provide a comparison function that maps the chosen sort mode onto the item metadata
* rebuild or reorder the visible sequence when sort mode changes
* then trigger relayout if width or grouping may have changed

Different object domains may sort by:

* name
* filetype
* size
* timestamp
* custom metadata
* stable application-defined priority

So the skill should describe the hook points, not a universal comparison rule.

## Multi-window browsers

Some filer-like interfaces have a root window and child windows that open onto subsets of the object set.

If so:

* keep the root and child view records separate even if they share redraw code
* key child windows by stable object identity or backing-object coordinates rather than by transient display index alone
* after resort, refresh, or data replacement, rebind child windows to the new ordered sequence before relying on item numbers again
* treat empty child windows as a normal lifecycle case; either close them or move them to a clear empty-state presentation

This is an optional structure for browsers with nested object views, not a requirement for every filer-like interface.

## Width snapping

When the layout is columnar, some interfaces deliberately snap the visible width to a whole number of object cells during relayout.

This is optional. It is useful when:

* partially visible columns are visually noisy
* column widths are fixed for the current view format
* the interface should feel more like a classic fixed-cell filer view

Avoid it when fluid resizing or partial-cell exposure is a deliberate part of the UI.
