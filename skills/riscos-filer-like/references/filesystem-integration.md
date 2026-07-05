# Integrating A Filer-Like View With A Real Filesystem

Use this file after `design.md` when the object set comes from directories and files rather than from an abstract in-memory list.

## Scope

This reference covers:

* mapping filesystem entries into filer-like item records
* refreshing and caching policy
* sort hooks
* parent and child navigation
* boundaries between filesystem state and view state

It is intentionally generic. Different filesystems and applications may expose different metadata, sorting rules, and refresh policies.

## Separate the filesystem model from the view

Keep these layers distinct:

* filesystem reader
  * enumerates entries
  * retrieves metadata
  * handles access errors
* object collection
  * stores the entries in application form
  * owns ordering, filtering, and grouping
* filer-like view
  * presents the current ordered collection
  * owns selection, focus, and window geometry

Do not let redraw code fetch directory entries directly. Enumeration should happen before or outside redraw.

## Suggested per-entry data

For a filesystem-backed item, capture at least:

* stable path or identifier
* displayed name
* type or kind
* icon identity
* size if relevant
* timestamp if relevant
* access or permission summary if relevant

Optional fields may include:

* owner
* group
* filetype text
* media metadata
* application-specific derived fields

Only store what the chosen view formats or sort modes might use.

## Enumeration policy

Decide early whether the view is:

* eager
  * read the whole directory first
* lazy
  * read entries on demand or in chunks
* cached
  * keep a snapshot and reuse it

Each is valid. The right choice depends on expected directory size and how expensive metadata lookup is.

If the collection is cached:

* document whether it is intentionally stale
* expose a refresh command or policy
* ensure refresh rebuilds the ordered sequence cleanly

## Navigation model

Filesystem-backed filer-like views usually need:

* open object
  * if directory, navigate into it
  * if file, invoke or preview it
* open parent
  * derive parent path or parent identity
* reopen existing cached directories if already loaded

Keep navigation decisions outside the low-level view code. The view should say which item was activated, not hard-code the filesystem policy for every object type.

## Sorting

Sorting should be explicit and pluggable.

Provide:

* a sort mode value
* a comparison function or key extractor for each mode
* a way to rebuild the visible order when the mode changes

Likely sort inputs for filesystem objects:

* display name
* canonical file name
* type or filetype
* size
* timestamp
* directory-first versus mixed ordering
* application-specific extra metadata

Important points:

* the most useful sort for one object domain may be wrong for another
* some views may expose metadata that is not part of the current sort
* changing sort mode may change width requirements if different labels or columns become dominant

So the skill should encourage the design of sort hooks, not dictate a single algorithm.

## Refresh behaviour

Refreshing a real filesystem view can mean:

* rebuild metadata for the current directory
* keep the current selection if the item still exists
* drop selection or focus cleanly if it does not
* preserve scroll position where that still makes sense

If the backing directory changed enough that object widths or count changed substantially, trigger the normal relayout path rather than trying to patch the geometry by hand.

## Error handling

Filesystem reads fail for ordinary reasons:

* permission denied
* object disappeared between enumeration and action
* broken links or unsupported object kinds
* transient device or network problems

Represent these cleanly:

* store enough state to show a stable placeholder item if needed
* do not let redraw paths raise fresh filesystem errors repeatedly
* report failure once through the controller or command layer

## Caching and identity

If directories or object lists are cached:

* key them by a stable identity such as canonical path
* keep the cache ownership separate from the view
* decide whether one cached collection can be shown in multiple views

This helps with:

* reopening already visited directories
* preserving alternate view formats per collection or per window
* switching between related panes or playlists without re-enumerating everything

## Design questions to answer early

Before implementation, make these choices explicit:

* is the collection a live view or a snapshot
* which metadata is required for display
* which metadata is required for sorting
* how often is refresh allowed or automatic
* are directories cached
* does selection survive refresh
* does activating a file run it, preview it, queue it, or something else
