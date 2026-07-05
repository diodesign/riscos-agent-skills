# Designing A Filer-Like View

Use this file when implementing or reviewing a Wimp window that behaves like a Filer object view.

## Scope

This applies to views such as:

* file or directory browsers
* media pickers
* launchers
* icon grids
* object lists with selectable tiles

The common shape is a window containing repeated object cells whose layout depends on the chosen view.

## Data model

Represent each object with:

* stable identity
* primary label
* icon or sprite identity
* optional secondary metadata fields
* visual flags such as selected, highlighted, or shaded

Keep display format separate from object data. The same object should be drawable in multiple views without mutating the stored metadata just to suit one layout.

## Geometry model

Define these explicitly:

* object width
* object height
* horizontal spacing
* vertical spacing
* window border or inset used by the object area
* number of columns for the current open width

From those derive:

* object cell width and height
* row count from item count and column count
* window extent from columns, rows, and borders
* the bounding box of object `n`

Use the same formulas everywhere. Hit-testing, redraw, scrolling, and selection traversal should all rely on the same object-box calculation.

## Window extent and resizing

A filer-like window usually wants its extent to match the total object area, not an arbitrary large canvas.

Useful pattern:

* compute columns from the current visible width
* clamp columns to at least one and at most the number of objects that can sensibly fit on screen
* derive rows from item count and columns
* update the window extent from the resulting total content width and height

Support at least these resize cases distinctly:

* user-driven window open or resize
* programmatic relayout because item count changed
* programmatic relayout because object size, spacing, or view format changed

If relayout forces window recreation, preserve:

* open state
* caret or focused object
* nested-window or parent linkage if present

## Object views and formats

Treat view format as a first-class state value.

Typical variations include:

* small icon with one line of text
* large icon with caption below
* detailed row with multiple metadata columns
* compact and expanded views of the same object set

For each format define:

* object cell size
* which metadata fields are visible
* whether fields are stacked, split across rows, or appended horizontally

Do not hard-code one view and bolt others on with per-field exceptions. Make the drawing path read the active format and render accordingly.

If some formats are only valid when data exists, choose the nearest simpler format deterministically rather than allowing partially broken layouts.

## Width calculation

For text-heavy object views, calculate the base width from the widest visible primary field, then add the widths of optional metadata fields enabled by the current format.

Guidance:

* measure text using the active Wimp or font metrics, not guessed character counts
* recompute widths when the visible labels or view format change
* cache width results if the object set is large, but invalidate that cache when labels or fonts change

## Redraw strategy

Use the Wimp redraw protocol correctly, then draw only objects that intersect the current rectangle.

Good pattern:

* start the redraw loop
* convert the redraw rectangle into candidate row and column ranges
* visit only the objects whose cells intersect that range
* render the object background, icon, text, and overlays from object state

Support a focused redraw path for a single object. Selection changes, highlight movement, and metadata updates should not require a full visible redraw.

## Hit-testing

Hit-testing should convert pointer coordinates to:

* the object grid position
* then the object index
* then optional subregions within that object

Reject clicks that land in spacing or outside the live object region. Returning the nearest object is usually wrong for Filer-like behaviour.

If the UI needs different actions for icon, text, or auxiliary fields, test subregions after the main object hit has succeeded.

## Selection and highlight state

Keep these states distinct:

* selected
* keyboard focus or current object
* temporary highlight or attention border
* shaded or unavailable

Users notice when these collapse into one visual state.

Design the redraw path so each state can affect appearance independently:

* selected may change foreground and background
* highlight may add a border
* shaded may suppress normal colours or interaction

## Keyboard and pointer navigation

Provide movement in terms of object topology, not raw indices.

Typical movements are:

* up, down, left, right
* next and previous object
* page up and page down
* first object matching a typed prefix

When moving the focused object:

* update the visual state
* redraw old and new objects
* scroll the focused object into view if necessary

Pointer actions should usually map to:

* select or focus object
* open or activate object
* alternate action on Adjust
* menu over object or background

## Scroll-to-view

A filer-like interface should be able to ensure an object is visible.

Useful rule:

* if the object's top is above the visible area, scroll upward until it appears
* if the object's bottom is below the visible area, scroll downward until it appears

Do this in object coordinates derived from the same box calculation used by redraw and hit-testing.

Support page-based navigation by computing the visible height in whole objects, not just raw OS units.

## Background and colours

Allow the view background to be configured independently from object colours.

When backgrounds are configurable:

* keep default colours for the "unset" case
* redraw with selected and unselected palettes consistently
* make sure selected text remains legible against selected backgrounds

If the window definition must be recreated to change background behaviour, treat that as a relayout path and preserve state accordingly.

## Performance

Filer-like views can grow large quickly.

Prefer:

* visible-region redraw instead of full-extent redraw
* single-object redraw for flag changes
* cached layout metrics when the data set is stable
* redraw by row and column ranges rather than scanning every object during every rectangle callback

If the object set is cached while the backing store changes externally, make that policy explicit. A stale-but-fast cache is acceptable only when the UI contract is clear.

## Review traps

Look for these problems:

* box calculations use one origin in redraw and another in hit-testing
* object spacing is applied in one axis but forgotten in the other
* relayout changes the item count or size without updating window extent
* changing view format loses scroll position or current selection unexpectedly
* selection redraw paints the object correctly but leaves stale borders behind
* dynamic width calculation only considers currently visible items and causes width churn while scrolling
* toggling between compact and detailed views reuses geometry from the previous format
