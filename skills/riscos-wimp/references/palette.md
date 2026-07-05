# Palette

Use this file when a task needs to know what Wimp colour numbers mean, how
they are normally used, or why a colour number does not always display the
same physical RGB value in every mode.

## Core rule

The Wimp works in terms of 16 standard Wimp colours.

Applications normally refer to these logical Wimp colour numbers, not to fixed
physical RGB values. The actual displayed colours come from the current Wimp
palette and may be remapped in non-16-colour modes.

If code assumes that a colour number always means one hard-coded physical RGB
triplet, that code is making too strong an assumption.

## Standard Wimp colours

The Window Manager PRM describes the standard colour set as:

* `0` to `7`: greyscale from white (`0`) to black (`7`)
* `1`: also the conventional iconbar and scroll-bar inner colour
* `2`: standard window title background colour
* `3`: scroll-bar outer colour
* `4`: desktop background colour
* `8`: dark blue
* `9`: yellow
* `10`: green
* `11`: red
* `12`: cream, used for the title background of the input-focus owner
* `13`: army green
* `14`: orange
* `15`: light blue

When someone asks "what does Wimp colour `N` display as?", answer in two
layers:

1. the conventional logical meaning from the table above
2. the reminder that the current palette may remap the actual RGB result

## Palette remapping

The Wimp's display model is based on the 16-colour modes.

In other modes, the Wimp maps those 16 standard colours onto whatever the
current mode and palette can display. The local PRM notes in particular:

* in 2-colour modes, logical colour `0` is mapped to Wimp colour `0`
  (white) and logical colour `1` to Wimp colour `7` (black)
* Wimp colours `1` to `6` become decreasing-brightness stippled patterns in
  2-colour modes

This means that a Wimp colour number is a logical desktop colour, not always a
single unchanging physical colour.

## `Wimp_SetPalette`

`Wimp_SetPalette` updates the actual RGB values for Wimp colours `0` to `15`,
plus the screen border and pointer colours.

The palette block contains one RGB word for each Wimp colour:

* `+0` to `+60`: Wimp colours `0` to `15`
* `+64`: screen border
* `+68`, `+72`, `+76`: pointer colours `1` to `3`

The RGB format is `&BBGGRR00`.

If the palette changes, tasks are informed through a Wimp message. Do not
assume the startup palette remains in force for the lifetime of the task.

## Practical guidance

When choosing colours for windows, menus, icons, or drawing:

* prefer the standard Wimp colour numbers where the PRM or style guidance
  expects them
* distinguish logical colour choice from physical RGB choice
* expect palette changes and mode changes while the task is running
* remember that the same logical Wimp colour may be approximated differently
  in lower-colour modes

For menu work specifically, be careful about the distinction between:

* menu header/work-area colour bytes
* icon foreground/background colour fields for individual menu items

Those are separate mechanisms even though they both use Wimp colour numbers.

## Reference source

Primary source: local `WIMP.HTML` sections `Colour` and `Colour handling`,
and the `Wimp_SetPalette` description.
