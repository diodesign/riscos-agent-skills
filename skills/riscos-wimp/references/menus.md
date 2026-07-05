# Menus

Use this file for menu construction, opening, submenu handling, menu
selection decoding, menu help, and Adjust-driven reopening.

Public references:

* Wimp menu overview and `Wimp_CreateMenu`: `http://www.riscos.com/support/developers/prm/wimp.html#27044`
* `Wimp_CreateSubMenu`: `http://www.riscos.com/support/developers/prm/wimp.html#43550`
* `Wimp_DecodeMenu`: `http://www.riscos.com/support/developers/prm/wimp.html#88368`
* `Wimp_GetMenuState`: `http://www.riscos.com/support/developers/prm/wimp.html#75062`
* `Message_MenuWarning` and `Message_MenusDeleted`: `http://www.riscos.com/support/developers/prm/wimp.html`

## Menu lifecycle

Menu handling normally has this shape:

1. construct or refresh a menu block in stable storage
2. remember which top-level menu is being opened, and where
3. call `Wimp_CreateMenu`
4. return to the normal poll loop while the Wimp owns the live menu tree
5. handle either `Menu_Selection`, `Message_MenuWarning`, or `Message_MenusDeleted`
6. on `Adjust`, rebuild if needed and reopen before the next `Wimp_Poll`

Concrete recipe for a context-sensitive menu with Adjust reopen:

1. On the initial click, identify the logical target object and remember it.
2. Build or refresh the top-level menu in stable storage.
3. Record the exact top-left coordinates passed to `Wimp_CreateMenu`.
4. Return to the poll loop and wait for `Menu_Selection`,
   `Message_MenuWarning`, or `Message_MenusDeleted`.
5. After `Menu_Selection`, perform the chosen action and inspect the current
   pointer buttons to see whether the user used `Adjust`.
6. If reopening on `Adjust`, rebuild the menu from current model state but
   reuse the remembered logical target where possible.
7. Call `Wimp_CreateMenu` again with the same top-level menu pointer and the
   same remembered coordinates before the next `Wimp_Poll`.
8. If the tree is not being reopened, clear the active-menu state.

Keep menu state explicit. Track at least:

* the top-level menu pointer or dialogue handle that was opened
* the coordinates used to open it
* the object which triggered it, especially for context menus
* whether the current action should preserve the tree for `Adjust`

If a task can open more than one menu, do not rely on the Wimp to tell you
which top-level menu the selection came from. The selection block only gives
indices. The task must already know which menu tree is active.

If the active menu depends on the object under the pointer:

* on the first open, it is reasonable to identify that object from the current
  pointer position
* on Adjust reopen, preserve the previously targeted logical object where
  possible and only fall back to pointer re-picking if that object has gone
  away

Otherwise the same menu can reopen on the wrong object just because the
pointer drifted while the tree was kept open.

## Constructing the menu block

`Wimp_CreateMenu` uses the caller's menu block in place. The Wimp does not
copy it. That means:

* the menu header and all items must remain valid while the tree is open
* indirected text, validation strings, and sprite names must remain valid too
* stack scratch space is not acceptable backing storage for a live menu

The block layout is:

* title at `menu + 0`
* title foreground and frame colour at `menu + 12`
* title background colour at `menu + 13`
* work area foreground colour at `menu + 14`
* work area background colour at `menu + 15`
* item width at `menu + 16`
* item height at `menu + 20`
* inter-item gap at `menu + 24`
* items from `menu + 28`, 24 bytes each

Be explicit about the header colour bytes:

* `menu + 12` controls the menu title foreground and frame colour
* `menu + 13` controls the menu title background colour
* `menu + 14` controls the menu work area foreground colour
* `menu + 15` controls the menu work area background colour

For a conventional menu appearance, use:

* title foreground and frame colour = `7`
* title background colour = `2`
* work area foreground colour = `7`
* work area background colour = `0`

Those work area colours are not the same thing as the menu item colours. The
work area colour bytes are normally only visible if there is a non-zero gap
between items, because the items themselves overdraw the work area.

Each item contains:

* menu flags
* submenu pointer or dialogue window handle
* icon flags
* icon data

The menu flags are the part which drives most menu behaviour:

* bit 0: tick shown
* bit 1: dotted line after item
* bit 2: writable item
* bit 3: generate `Message_MenuWarning` instead of direct submenu opening
* bit 4: allow submenu even when shaded on newer systems
* bit 7: last item in this menu

The icon flags and icon data are mostly normal icon fields, but menu items are
still constrained by the menu protocol:

* button type is effectively menu-owned; do not treat items like ordinary
  clickable icons
* menu item foreground and background colours come from the item's icon flags,
  not from the four menu-header colour bytes
* shading is done with icon flag bit 22
* writable items use menu flag bit 2 and may also use indirected icon data and
  validation strings
* sprite-only menu items must be indirected if they need a sprite area pointer

For conventional menu items:

* use icon colours that produce black text on a white filled background
* set the icon's filled-background bit so the item paints its own background
* do not expect `menu + 14` and `menu + 15` to control the item colours

If item colours are wrong, check the item icon flags first. The header colour
bytes only control the title and the bare work area behind any inter-item gap.

The PRM recommends keeping a shorthand description and expanding it into the
real block when needed. That is a good pattern for both C and BASIC code:

* encode the logical menu contents in a compact application-owned form
* regenerate the Wimp block when opening or reopening
* keep the generated block in stable memory until the Wimp deletes the tree

For static menus in C, this often ends up as permanent structures. For dynamic
menus, use a reusable heap buffer or a dedicated menu workspace rather than
mutating random structs in place.

## Conventional size values

For a conventional RISC OS menu:

* item width should be chosen explicitly and stored at `menu + 16`
* item height should normally be `44` OS units (`&2C`)
* inter-item gap is commonly `0`

Do not guess the item height from font size or from title-bar dimensions. The
menu header field at `menu + 20` is the value the Wimp uses to size every item
in that menu.

### Width calculation

For conventional text menus, calculate the top-level menu item width from the
widest top-level item text that must be displayed in that menu.

Use this pattern:

* `item_width = 16 * max_text_columns + padding`

where:

* `max_text_columns` is the number of displayed character columns needed by the
  widest top-level item in that menu
* count the actual displayed top-level item text, including any hot key text or
  other spacing that will be visible in the item
* do not use the submenu contents to size the top-level menu
* `16` OS units per character is the conventional system-font width used for
  menu sizing
* `padding` is any extra width you intentionally reserve for menu furniture and
  spacing; if your menu generator already builds this into the text columns,
  do not add it twice

Be precise about what to measure:

* use the widest top-level entry in the menu being opened
* include enough room for tick space on the left and submenu-arrow space on the
  right
* include writable-item text capacity if a writable item must visibly fit a
  longer string
* do not size from the title width alone
* do not size from the current pointer position or window width

The title also depends on this width. If the title is not indirected, its
maximum length is the smaller of `12` and `(item_width DIV 16)` characters.

## Opening menus

Open the menu with `Wimp_CreateMenu` and then return to the poll loop. Once the
call has succeeded, the Wimp owns the interactive tracking of the tree until it
is selected, replaced, or deleted.

For a normal popup menu in a window:

* derive the popup position from the click context
* if the menu belongs to a specific icon, prefer icon and window geometry over
  guessed offsets when that geometry matters
* remember the exact top-left coordinates used so the same tree can be reopened
  on `Adjust`

Many applications still apply the conventional pointer-relative offsets when
opening a menu from a click position. That is acceptable as long as the reopen
path uses the same remembered coordinates.

### Iconbar menus

Iconbar menus need special handling because there is no ordinary work-area
geometry to position against.

In practice:

* detect the iconbar click from the mouse event's window handle, typically `-2`
* use the iconbar click or current pointer position as the anchor
* choose coordinates that place the menu above the icon bar, not as if it were
  a window popup inside a work area

Real applications commonly store separate open coordinates for iconbar menus and
bias the Y position by the full menu height so that the tree grows upward from
the bar. That is different from the ordinary in-window popup case, which is
usually anchored nearer the click point.

If the same menu definition is used both on the icon bar and inside a window,
do not share one guessed popup formula between the two cases.

### Concrete positioning pattern

The Wimp wants the top-left coordinate of the top-level menu. For iconbar
menus, a practical pattern is:

* `menu_x = pointer_x - 64`
* `menu_y = iconbar_top + menu_height`

with:

* `pointer_x` from `Wimp_GetPointerInfo`
* `iconbar_top = 96` for the standard iconbar baseline used by classic
  applications
* `item_height` = the height field from the top-level menu block, not a guessed
  text height and not a submenu item height
* `item_count` = the number of entries in the top-level menu being opened on
  the icon bar, counting every item in that menu until the last-item flag, and
  not counting entries in any submenu
* `menu_height = item_height * item_count`

Be precise about which menu this refers to:

* use the top-level iconbar menu's own item height
* use the top-level iconbar menu's own item count
* do not substitute the height or count of a submenu
* do not estimate from the number of visible text lines
* do not use the menu width, the pointer Y coordinate, or a generic small
  offset in place of `menu_height`

That formula places the menu so its bottom edge sits just above the icon bar,
rather than with its top edge near the click point.

For ordinary non-iconbar popups, use a different Y-position rule:

* `menu_x = pointer_x - 64`
* `menu_y = pointer_y + 20`

Do not reuse the in-window `+20` Y offset for iconbar menus. It opens the menu
too low because iconbar menus need their full height added above the bar.

## Selection flow

When the user makes a menu selection, `Wimp_Poll` returns a `Menu_Selection`
event with a list of indices terminated by `-1`.

Treat that block as the ground truth:

* it is not an application-defined struct
* each integer is the selected item number at that depth
* the list ends with `-1`

There are two common decoding approaches:

* walk the menu tree yourself by following submenu pointers at each depth
* call `Wimp_DecodeMenu` to obtain a `.`-separated text path

Use `Wimp_DecodeMenu` when text-path dispatch is appropriate, but remember:

* it depends on the submenu pointers in the menu tree still matching the live
  logical structure
* it returns item text, not a typed application action ID
* writable-item text and displayed hot key text may need normalising before
  comparison

If you want to know the currently highlighted path before selection, use
`Wimp_GetMenuState`. That is especially useful for menu help and for submenu
creation driven by the current path rather than by a single top-level item.

## Adjust reopening

`Adjust` selection is a two-stage protocol, not automatic persistence.

After `Menu_Selection`:

* inspect the pointer buttons, normally via `Wimp_GetPointerInfo`
* if `Adjust` was used, rebuild or update the menu as needed
* call `Wimp_CreateMenu` again with the same top-level menu pointer and the same
  remembered coordinates before the next `Wimp_Poll`

If you do that, the Wimp recreates the tree in place and walks back down the
previous selection path while it still matches the rebuilt tree.

If you do not reopen it before the next `Wimp_Poll`, the Wimp deletes the
temporary tree.

This is why menu code should keep the top-level pointer and popup coordinates
explicitly. A common pattern is:

* open: remember `current_menu`, `menu_x`, `menu_y`
* selection: perform the action
* if `Adjust`, call `Wimp_CreateMenu(current_menu, menu_x, menu_y)`
* otherwise clear the active-menu state

## Submenus and dialogue boxes

If an item's submenu field is a submenu pointer, the Wimp can open the submenu
directly.

If that field is a window handle, the Wimp opens the window as a menu dialogue
box:

* the first writable icon gets the caret
* the user does not close it through normal window close handling
* clicks outside the tree close it automatically
* there is no `Close_Window_Request` just because the menu dialogue vanished

Use an explicit action such as `OK` or `Cancel` to convert dialogue interaction
into a menu selection or a menu close.

If you want Return to commit the dialogue, handle the key-pressed event
yourself. The Wimp will not invent the menu semantics for you.

## `Message_MenuWarning`

`Message_MenuWarning` is the delayed-submenu path. It is generated when:

* the menu item has submenu-generation bit 3 set
* the submenu pointer is non-zero
* the user moves over that item's submenu arrow

The message block contains:

* the submenu pointer copied from the item
* the X and Y coordinates to pass to `Wimp_CreateSubMenu`
* the current selected path, again as a `-1` terminated list

Use this when submenu contents are dynamic or expensive, or when the submenu is
really a dialogue which must be created at the last moment.

When handling `Message_MenuWarning`:

* derive the active path from the included selection list
* refresh any state the submenu depends on
* create or update the submenu object
* call `Wimp_CreateSubMenu` with the provided coordinates, unless the specialised
  subsystem owns that step

The submenu pointer in the message is advisory. You may replace it with a new
submenu block pointer or a newly created window handle.

If the submenu is a ColourPicker dialogue, read `references/colour-picker.md`
as well. Type-3 ColourPicker menus are opened by the ColourPicker module rather
than by a direct client `Wimp_CreateSubMenu` call.

## `Message_MenusDeleted`

`Message_MenusDeleted` is the cleanup signal for menu trees which disappear
without becoming a `Menu_Selection`.

Expect it when:

* another task replaces your menu
* your task replaces the open tree with a different top-level menu pointer
* the user clicks outside the tree

Do not expect it when:

* a normal `Menu_Selection` has just been returned
* you reopened the same tree pointer in place

Use it to clear cached menu-open state which should not survive a cancelled or
externally replaced menu.

## Writable items, warnings, and hot key display

Writable items are still menu items, not ordinary writable icons embedded in a
window. Make sure the menu flag says the item is writable and the backing text
storage remains valid while the menu is open.

For warning triangles and delayed submenus:

* the submenu arrow appears when the submenu field is present
* `Message_MenuWarning` only happens when the generate-message bit is set
* a shaded item should normally be treated as unavailable rather than as a live
  submenu entry
* on newer systems, menu flag bit 4 allows submenu following even when the
  parent item is shaded; use that only deliberately

For hot key display:

* the Wimp does not infer application shortcuts from your key handling
* display text such as `Ctrl-F3`, `F12`, or `Shift-Tab` must be included in the
  menu item text you build
* keep the displayed shortcut aligned consistently across sibling items
* when comparing decoded item text, strip any appended shortcut legend if your
  dispatcher is text-based

If the application also serves menu help from tokenised messages, keep the menu
item text, the decoded path, and the help-token naming scheme in sync. Read
`references/help.md` when menu help generation depends on the live selection
tree.

## Dynamic menu guidance

For menus whose entries depend on current mode, selection, or other runtime
state:

* rebuild from the current model rather than patching stale menu blocks ad hoc
* keep menu backing storage lifetime separate from transient scratch buffers
* update ticked, shaded, writable, and submenu state before opening or reopening
* keep submenu pointers coherent if you expect to use `Wimp_DecodeMenu`
