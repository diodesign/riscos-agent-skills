# Application Structure And Lifecycle

## Use this reference for

- Application directory layout
- Startup and shutdown behaviour
- Editor/file-handling behaviour
- Saved user choices
- Shared resources, network use, and CD-ROM distribution

## Application directory rules

- Put each application in a directory whose name begins with `!`.
- Omit the leading `!` when referring to the application in documentation or help text.
- Use standard resource filenames when the resource exists.
- Expect the standard resource set to include `!Boot`, `!Run`, `!Sprites`, `!Sprites22`, optional `!Sprites23`, `Messages`, optional `!Help`, and optional `Choices`.
- Keep text resources in a `Messages` file so they can be replaced for localisation.
- Provide `!Help` text if the application benefits from quick Filer help.
- Store user-settable persistent choices in `Choices`.

## Boot and run behaviour

- Use `!Boot` for setup performed when the application directory is first seen by the Filer.
- Use `!Run` for the action performed when the user opens the application.
- Only claim filetypes on startup when they are not already claimed.
- Avoid crashing if more than one copy of the application exists or if resources cannot be found.
- Load textual resources at startup rather than repeatedly reading them from removable media.

## Sprite and shared-resource rules

- Provide `!Sprites` and `!Sprites22`; include `!Sprites23` when useful for high-resolution monochrome support.
- Keep private sprites in the application's own sprite area.
- Do not redefine global pool sprites automatically.
- Use standard file icons for standard filetypes rather than replacing them.
- Name the application sprites and small sprites consistently with the application's canonical lower-case sprite names.
- Minimise dependency on shared external resources because it complicates installation.

## Standard lifecycle behaviour

- Start the application when the user double-clicks its directory icon with `Select` or `Adjust`.
- Support file opening by dragging a document to the icon bar icon.
- Provide `Info` at the top of the icon bar menu and `Quit` as the last item.
- On quit, close windows safely and prompt about unsaved data before any loss occurs.
- Handle system pre-quit messages and shutdown safely.

## Editor-specific expectations

- Create a new document from the icon bar icon or a dedicated `New` action.
- Load, save, print, and close documents using standard RISC OS patterns.
- Preserve unsaved work until the user explicitly saves or discards it.
- Match documents to editors by filetype and integrate with normal drag-and-drop file loading.

## Configuration and choices

- Respect the user's hardware, monitor, printer, screen-mode, palette, mouse, and sound settings.
- Handle screen-mode changes while running.
- If a mode is unsupported, report it clearly instead of silently changing system settings.
- Offer a `Choices` item in the icon bar menu when the application has persistent options.
- Grey out unavailable choices rather than hiding them.
- Apply relevant saved choices consistently across documents.

## Network and removable-media concerns

- Avoid assumptions about the underlying filing system.
- Keep startup lightweight over network filesystems.
- Separate writable files from the application itself when the application may be run read-only.
- On CD-ROM, expect slower access and use system variables for disc and directory locations.
