# StrongHelp Manual Structure

## Inspecting a packed manual

When the source material is a packed StrongHelp file such as `Manual,3d6`:

- Start with `riscos-shextract --list Manual,3d6` to see the true page names, directories, and file types.
- Extract it with `riscos-shextract --extract-dir <dirname> Manual,3d6`.
- Read the extracted files from the filesystem.
- Do not inspect the raw `,3d6` bytes as if they were a text file. Packed manuals may contain container metadata or stale bytes that are not part of the live page set.

The extracted directory is the source of truth for structure and content.

## Container Directory
A StrongHelp manual is built from a directory containing files for each page.

- **!Root**: Required. Entry point of the manual.
- **info**: Commonly used as an overview or information page linked from `!Root`.
- **!Configure**: Optional. Custom fonts/styles for the manual.
- **!Pre**: Optional. Utility code (RISC OS machine code) for lookups.
- **!Menu**: Optional. (Main manual only) Iconbar menu.
- **NotFound_{manual}**: Optional. Page shown for missing external manual links.

## File Organization
To manage large manuals, group pages:

- **Flat**: All files in the manual's root directory.
- **Prefix Directory**: Group pages with a common prefix in a directory named with that prefix (e.g., `Wimp_Poll` and `Wimp_PollIdle` in `Wimp_`).
- **First-Letter Range**: Use `[a-z]` or similar directories to automatically group pages by their first letter.
- **!root**: In any directory, a `!root` file is the default page.
- **Topic Directories**: Manuals often group related pages into directories such as `FN` or `PROC`, which then contain leaf page files like `claim` or `initheap`. Read the extracted tree rather than guessing the page layout.

## Extracted page mapping

After extraction, each StrongHelp page becomes a normal host file in the extracted tree.

- A root page such as `$.!Root` becomes `!Root` in the extract directory, sometimes with a host filetype suffix such as `!Root,ffd`.
- A page such as `$.PROC.initheap` becomes a file like `PROC/initheap`.
- Listing output from `riscos-shextract --list` is useful for mapping manual page names onto extracted host paths before editing or quoting content.

## Redirections
Files named `OLDNAME>NEWNAME` redirect lookups for `OLDNAME` to the page `NEWNAME`.

## Naming Constraints
RISC OS filenames have restrictions. StrongHelp additionally reserves `! [ ] \ < > . $ % & ? # :`. Use `!xx` (hex) for special characters in filenames.

## Images
- **#Sprite**: References a sprite from the Wimp pool or a specified sprite file.
- **#SpriteFile**: Defines the path to a sprite file (e.g., `!Sprites`).
- **#Draw**: Places a RISC OS Drawfile.
