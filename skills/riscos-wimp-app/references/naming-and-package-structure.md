# Naming and package structure

This reference is about the build-application structure around a desktop
application, not the Wimp protocol itself.

## Application naming

RISC OS desktop application names should normally be:

* capitalised
* free of hyphens unless there is a strong reason not to

For example, prefer `WimpClicks` over `wimp-clicks` for the built application
name and package directory.

## What must change when the application name changes

Changing only `COMPONENT` in the makefile is usually not enough.

Review at least:

* `Makefile,fe1` application/component name
* `Resources/!Run` references to `<AppName$Dir>`
* other obey files under `Resources/` such as `!Boot` if they mention the
  application name
* help and message files that present the application name to the user
* `VersionNum` component name
* application source code task names, title strings, and system-variable use
* sprite names if they are application-specific

If the name is exposed through `AppName$Dir`, task names, or filenames, update
every path that depends on it together rather than one at a time.

## Build verification

For `CApp` and similar install-oriented components, verify the packaging with
an explicit install destination:

```bash
riscos-amu install INSTDIR=install
```

This checks the packaged application layout rather than only compiling the
binary.
