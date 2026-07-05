# Icons

Use this file for icon bar icons, window icons, and icon state changes.

Public references:

* Wimp PRM chapter: `http://www.riscos.com/support/developers/prm/wimp.html`
* Icon bar priorities note: `https://gerph.github.io/riscos-prminxml-staging/prm/html/select/desktop/wimp/iconpriorities.html`
* Icon bar priorities diagram: `https://raw.githubusercontent.com/gerph/riscos-prminxml-staging/refs/heads/master/src/select/desktop/wimp/iconpriorities.ditaa`

## Icon bar creation

Be careful with `Wimp_CreateIcon` on the icon bar:

* `R1 + 0` in the create block controls the icon-bar placement mode such as `-8`
* `R0` may hold a priority value or an anchor icon handle, depending on the placement mode

Do not swap those two roles.

For icon-bar icons, the placement values are part of the block, not the returned handle. This is a common source of left/right icon-bar placement bugs.

When a placement mode anchors a new icon relative to an existing icon, keep the returned handle from the earlier `Wimp_CreateIcon` call and feed that handle back in `R0`. Do not treat that anchor handle as if it were a priority value.

For ordinary desktop applications on the icon bar, prefer the conventional
application form unless you have a reason to model some other category:

* right-side application icons should usually be sprite-only
* left-side icons should usually be sprite-plus-text
* if you do not know which sprite to use, fall back to the sprite name
  `application`

The icon block geometry differs between those common forms:

* right-side sprite-only icons are usually built with `y0 = 0`, `y1 = 68`
* left-side sprite-plus-text icons are usually built with `y0 = -16`,
  `y1 = 84`
* sprite-plus-text icons usually start with a minimum width of
  `12 + 16 * max(4, text_length)`
* after choosing the basic form, read the sprite size and enlarge the box if
  the sprite needs more width or height

If an iconbar icon appears not to show at all, check the bounding box before
assuming the sprite is wrong. A right-side application icon with inverted or
unexpected vertical co-ordinates is a common failure mode.

## Icon bar priorities

If the task creates an icon bar icon with a fixed priority, check that the chosen priority matches the intended icon-bar category.

The public icon-bar priorities note usefully separates:

* object sources and sinks
* data source / sink controllers
* user applications
* system control applications

The accompanying diagram makes an important distinction:

* object sources and sinks are prioritised
* source / sink controllers are not prioritised
* user applications are not prioritised
* system control applications are prioritised

Do not assign fixed numeric priorities to ordinary application icons just because `Wimp_CreateIcon` allows a priority-bearing form. Reserve fixed priorities for categories that the documented layout actually treats as prioritised.

For object sources and sinks, the note documents a clarified left-to-right ordering from read-only through read-write to write-only and volatile devices. The documented priorities include:

* scanners: `&76000000`
* CD-ROM: `&74000000`
* hard discs: `&70000000`
* floppies: `&68000000`
* network devices: `&60000000`
* volatile devices: `&40000000`
* printers: `&0F000000`
* accelerators: `&04000000`

That note specifically places Display Manager in the system control application area, alongside Task Manager and Help, and documents the clarified icon-bar ordering for Select-era systems. Use it as guidance when a module or application chooses a priority rather than relying only on old folklore or accidental historic values.

## Icon bar behaviour by category

The public note also gives behavioural guidance, not just positions:

* device-style icons should usually have text underneath identifying the medium, device, or drive
* device-style icons should generally not offer `Quit`
* user applications should normally offer `Quit`
* user applications should not normally show text underneath unless the state genuinely needs explanation

This guidance is especially useful when reviewing whether an icon is really modelling a device, a service/controller, or an ordinary application.

## Sprite sizing

For icon bar sprites:

1. read sprite size
2. read eig factors for the sprite mode
3. convert to OS units
4. construct the icon bounding box from those converted dimensions

For the common application icon calculations, the converted size
comes from:

* width in OS units = `(sprite_width_words + 1) << x_eig_factor`
* height in OS units = `(sprite_height_rows + 1) << y_eig_factor`

Treat these values as the sprite's minimum required size for the icon box. If
the conventional iconbar defaults are already larger, keep the larger box.

## Iconbar button types

Do not accidentally create a non-interactive iconbar icon:

* button type `0` is `Never` / ignore all mouse operations
* a normal clickable application icon should use a click-capable button type
  such as `3` (`wimp_BCLICKDEBOUNCE`)

Choose button types to match the icon's role, not just to make it clickable:

* ordinary command or action icons should generally use one of the click or
  notify styles, rather than writable or drag-oriented types
* writable icons should use button type `15` (`wimp_BWRITABLE`) so that the
  Window Manager owns text editing, caret movement, and text replacement
* radio-button and on/off style icons often suit `wimp_BCLICKSEL`
* drag operations should use one of the drag-specific button types instead of
  a plain click type

The button type affects which mouse-click values are returned later. Do not
assume that all clickable icons produce the same event values regardless of
their button type.

If the icon appears but clicks are ignored, check the icon button type before
debugging the poll loop.

For dialogue boxes specifically, choose the same button-type family that the
Window Manager expects for the icon's purpose:

* writable fields should be genuinely writable icons
* action buttons are described by the PRM as best using button type `7`
  (`Menu`) with a non-zero ESG, so that they invert while the pointer is over
  them and report a button press
* option and radio controls should use button types intended for selectable
  state changes

If a dialogue icon behaves oddly, re-check whether the button type matches the
kind of control the icon is meant to represent before blaming the poll loop.

## Window icons

When templates contain indirected icons:

* keep the backing text and validation buffers alive
* only update indirected text through stable storage
* use `Wimp_SetIconState` or the appropriate icon update path to refresh what the user sees
* remember that writable icons and indirected icons have different ownership and update expectations
* if the visible text length changes materially, check whether the icon bounding box also needs resizing before the refresh

## State changes

Be clear about what the icon-state block fields mean:

* window handle
* icon handle
* EOR word
* clear word

Do not pass an unrelated block layout to `Wimp_SetIconState`.
