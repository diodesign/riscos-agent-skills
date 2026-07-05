# riscos-defmod command line

```
riscos-defmod <type> [-v] [-q] [-help] [-o <output-dir>] [-byte_wide <byte-wide-file>]
              [-P] [-26bit] [-32bit] < <Def-file>
```

The Def file is always read from standard input. `<type>` is exactly one
required output selector:

| Selector | Output |
|---|---|
| `-h` | C header |
| `-h++` | C++-flavoured header (experimental) |
| `-hdr` | ObjAsm header |
| `-s` | ObjAsm source (veneers) |
| `-chelp` | SrcEdit C help file |
| `-asmhelp` | SrcEdit assembler help file |
| `-cstrong` | StrongHelp C help directory |
| `-l` | Per-SWI library-style directory tree (for `LibFile -via`) |

Most selectors write to standard output, so redirect explicitly:

```sh
mkdir -p h
riscos-defmod -h < InterfaceDef > h/interface
```

The redirection is the shell's, not `defmod`'s, so the destination directory
must exist first for every selector except the directory-producing ones.

The directory-producing selectors (`-l`, `-cstrong`) take `-o <dir>` and
create that output directory themselves:

```sh
riscos-defmod -l -o LibraryOut -26bit -32bit < InterfaceDef
```

## Other flags

| Flag | Meaning |
|---|---|
| `-v` | Verbose parser echoing and warnings. |
| `-q` | Suppress informational messages where possible. |
| `-help` | Print command help. |
| `-o <dir>` | Output directory for `-l` and `-cstrong`. |
| `-byte_wide <file>` | Whitespace-separated file listing externally-defined byte-wide type names, needed so veneer generation can tell byte-wide arguments from word-wide ones. |
| `-P` | Old-style OSLib naming: no `oslib/` path prefix, `bool` instead of `osbool`. |
| `-26bit` | Generate APCS 3/26-bit veneers. |
| `-32bit` | Generate APCS 3/32-bit veneers. Supplying both generates both forms. |

If neither `-26bit` nor `-32bit` is given, the default veneer output is
26-bit.

## Known discrepancies between help text and behaviour

* The built-in help text still mentions a Pascal output mode (`-p`), but the
  current command-line parser does not recognise it.
* `-asmstrong` is accepted by the argument parser, but the dispatch code does
  not actually produce output for it.

Follow the table above (implemented behaviour), not the tool's own `-help`
text, when either disagrees.
