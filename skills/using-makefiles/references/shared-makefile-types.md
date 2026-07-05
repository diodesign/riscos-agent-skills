# Shared makefile types and variables

## Shared Makefile Types

| Makefile | Use for |
|---|---|
| `LibraryCommand` | Command-line tools and standalone executables (C or assembly) |
| `CModule` | RISC OS relocatable modules written in C (uses CMHG) |
| `AsmModule` | RISC OS relocatable modules written in assembly |
| `LibExport` | Libraries exported for use by other components |
| `CApp` | Desktop applications written in C |
| `BasicApp` | Desktop applications written in BBC BASIC |
| `Documentation` | PRM-in-XML documentation only, no compiled output |
| `Resource` | Resource files only, no compilation |

## Common Build Targets

| Target | Effect |
|---|---|
| `all` | Build the component (default for most types) |
| `ram` | Build as a standalone loadable module (default for module types) |
| `rom` | Build as a partially-linked object for ROM inclusion |
| `install` | Copy output to `INSTDIR` for disc use |
| `install_rom` | Copy ROM object to ROM build staging area |
| `export` | Export headers and libraries (`export_hdrs` + `export_libs`) |
| `export_hdrs` | Export headers only |
| `export_libs` | Export compiled libraries only |
| `resources` | Copy resource files to the ResourceFS staging area |
| `clean` | Remove all generated files (not exported files) |
| `rom_link` | Final ROM link at a given base address (used by ROM build system) |

## Build Architecture

| Variable | Effect |
|---|---|
| *(unset)* or `BUILD32=1` | 32-bit ARM build (default) |
| `BUILD26=1` | 26-bit ARM build (legacy hardware) |
| `BUILD64=1` | 64-bit AArch64 build (limited library support) |

Architecture determines output directories:

| Architecture | Objects | Module objects | Executables | Modules | AOF |
|---|---|---|---|---|---|
| 32-bit | `o32` | `oz32` | `aif32` | `rm32` | `aof32` |
| 26-bit | `o` | `oz` | `aif` | `rm` | `aof` |
| 64-bit | `o64` | `oz64` | `aif64` | `rm64` | `elf64` |

Only one architecture flag may be set at a time.

## Global Compilation Variables

Set before the `include` to affect compiler behaviour across all makefile types.

| Variable | Default | Description |
|---|---|---|
| `OPTIMISE` | `yes` | Optimisation level: `no`, `size`, `time`, `yes`, `max` |
| `UNALIGNED_LOADS` | `no` | Allow unaligned memory loads: `yes`, `no`, `default` |
| `ASD` | *(unset)* | Set to `yes` for a debug build; output directories gain a `d` suffix. Not supported for 64-bit. |

## C Library Selection

| Variable | Default | Description |
|---|---|---|
| `CLIBTYPE` | `noc99` | C library variant: `noc99` (StubsGS, no C99 printf/scanf), `generic` (StubsG, full C99), `static` (ANSILib, statically linked). Ignored for 64-bit builds. |
| `NOCLIB` | *(unset)* | If defined, no C library is linked at all. |

## Optional Build Features

| Variable | Default | Description |
|---|---|---|
| `FORTIFY` | *(unset)* | Memory checker: `yes` (active), `support`/`no` (headers available, not linked), unset (absent). When `yes`, source must `#include "fortify.h"` and call `Fortify_EnterScope`/`Fortify_LeaveScope`. |
| `PROFILE` | *(unset)* | ARM profiling: `yes` (full, `-px -g`), `simple` (functions only, `-p`), `support`/`no` (aware but inactive), unset (absent). Not supported for 64-bit. |

## Pre-defined Library Variables

These are set by the shared `_Libraries` include and can be used directly in `LIBS`.
`_ZM` variants are module (ROM-safe, position-independent) versions for use in modules.

### C library

| Variable | Description |
|---|---|
| `${CLIB}` | C library (selected by `CLIBTYPE`) |
| `${CLIB_ZM}` | Module C library (used automatically by module makefiles) |
| `${ROMCLIB}` | ROM C stubs (used during ROM builds) |

### Desktop / C++

| Variable | Description |
|---|---|
| `${C++LIB}`, `${C++LIB_ZM}` | C++ runtime (not available for 64-bit) |
| `${RLIB}`, `${RLIB_ZM}` | RISC_OSLib (not available for 64-bit) |
| `${TBOXLIBS}`, `${TBOXLIBS_ZM}` | All three Toolbox libraries bundled (not available for 64-bit) |
| `${TBOX_EVENTLIB}`, `${TBOX_TOOLBOXLIB}`, `${TBOX_WIMPLIB}` | Individual Toolbox libraries |
| `${DESKLIB}`, `${DESKLIB_ZM}` | DeskLib (not available for 64-bit) |

### Networking

| Variable | Description |
|---|---|
| `${TCPIPLIBS}`, `${TCPIPLIBS_ZM}` | UnixLib + InetLib + SockLib5 bundled |
| `${INETLIB}`, `${SOCKLIB}`, `${SOCKLIB5}`, `${UNIXLIB}`, `${RPCLIB}` | Individual TCP/IP libraries |

### Miscellaneous

| Variable | Description |
|---|---|
| `${ZLIB}` | zlib compression |
| `${ZIPPERLIB}`, `${ZIPPERLIB_ZM}` | Zipper archive library |
| `${MD5LIB}`, `${MD5LIB_ZM}` | MD5 hashing |
| `${REGEXLIB}` | POSIX regular expressions |
| `${GETOPTLIB}` | getopt argument parsing |
| `${THROWBACKLIB}` | DDEUtils Throwback |
| `${CONFIGLIB}`, `${CONFIGLIB_ZM}` | Configuration file library |
| `${LLLIB}`, `${LLLIB_ZM}` | LongLong 64-bit integer library |
| `${OSLIB}` | OSLib typed SWI interface library |
| `${ASMLIB}`, `${ASMLIB_ZM}` | Inline assembler support (not available for 64-bit) |
| `${RESOLVLIB}`, `${RESOLVLIB_ZM}` | DNS resolver |
| `${P2CLIB}` | Pascal-to-C translation runtime |

## LibraryCommand Variables

| Variable | Required | Description |
|---|---|---|
| `COMPONENT` | Required | Component name; default output filename |
| `TYPE` | Optional | Output type: `aif` (linked executable, default), `aof` (partial link), `util` (assembly utility binary), `basic` (BASIC program), `raw` (custom rules) |
| `OBJS` | Optional | Space-separated object files, e.g. `o.main o.utils` |
| `LIBS` | Optional | Space-separated libraries to link, e.g. `${CLIB}` |
| `CDEFINES` | Optional | Preprocessor definitions, e.g. `-DDEBUG` |
| `INCLUDES` | Optional | Comma-separated additional include paths |
| `TARGET` | Optional | Output filename; defaults to `COMPONENT` |
| `WORKSPACE` | Optional | Workspace size for relocatable AIF output |
| `VIAAOF` | Optional | Set to `yes` to link via intermediate AOF |
| `RESOURCES` | Optional | Resource files to install alongside the executable |
| `FILETYPE` | Optional | RISC OS filetype to apply (for `TYPE=aof`) |
| `DOCSRC` | Optional | PRM-in-XML documentation source files |
| `INITTARGET` | Optional | Additional target invoked at build initialisation |
| `CLEANTARGET` | Optional | Additional target invoked by `clean` |
| `TESTTARGET` | Optional | Target invoked for testing; `TESTTARGET26`/`TESTTARGET32` for architecture-specific variants |

## CModule Variables

The preprocessor symbol `BUILD_RAM` is defined during `ram` builds, not during `rom`.

| Variable | Required | Description |
|---|---|---|
| `COMPONENT` | Required | Component name |
| `OBJS` | Optional | Object files; include the CMHG object and all C objects |
| `LIBS` | Optional | Libraries to link; module C library is added automatically |
| `CDEFINES` | Optional | Preprocessor definitions |
| `INCLUDES` | Optional | Comma-separated additional include paths |
| `TARGET` | Optional | Output filename; defaults to `COMPONENT` |
| `LIBCOMPONENT` | Optional | Export subdirectory name; defaults to `COMPONENT` |
| `EXPORTS` | Optional | Files to export; commonly the generated SWI header |
| `RESOURCES` | Optional | Resource files for the `resources` target |
| `INSTALL` | Optional | Additional files for the `install` target |
| `NOCLIB` | Optional | If defined, C library is not linked |
| `NOROMLINK` | Optional | If defined, `rom_link` is not provided |
| `LINKTYPE` | Optional | Set to `bin` to produce raw binary during `install_rom` |
| `FORTIFY` | Optional | Fortify memory checker |
| `DOCSRC` | Optional | PRM-in-XML documentation source files |
| `INITTARGET` | Optional | Additional target at initialisation |
| `CLEANTARGET` | Optional | Additional target during `clean` |

## AsmModule Variables

| Variable | Required | Description |
|---|---|---|
| `COMPONENT` | Required | Component name |
| `OBJS` | Optional | Object files for ObjAsm; use with or instead of `AASM` |
| `AASM` | Optional | Single AASM source file assembled directly to a module |
| `CSOURCES` | Optional | C source files to convert to assembly before building |
| `DEFINES` | Optional | Preprocessor definitions for C-to-assembly conversion |
| `LIBS` | Optional | Libraries to link |
| `TARGET` | Optional | Output filename; defaults to `COMPONENT` |
| `EXPORTS` | Optional | Files to export |
| `RESOURCES` | Optional | Resource files for the `resources` target |
| `INSTALL` | Optional | Additional files for the `install` target |
| `ROMSAFE` | Optional | Set to `no` if the module must be squished for ROM inclusion |
| `EXTRACSEDFLAGS` | Optional | Additional flags for the C-to-assembly sed step |
| `DOCSRC` | Optional | PRM-in-XML documentation source files |
| `INITTARGET` | Optional | Additional target at initialisation |
| `CLEANTARGET` | Optional | Additional target during `clean` |
| `TESTTARGET` | Optional | Testing target; suffix variants `TESTTARGET26`/`TESTTARGET32`/`TESTTARGET64` |

## LibExport Variables

Exported library files go to `${EXP_LIB}.${LIBCOMPONENT}.o.*`.

| Variable | Required | Description |
|---|---|---|
| `COMPONENT` | Required | Component name |
| `OBJS` | Optional | Object files to compile; if unset, no library object is produced |
| `TARGET` | Optional | Base library filename; defaults to `libCOMPONENT` |
| `LIBCOMPONENT` | Optional | Export subdirectory; defaults to `COMPONENT` |
| `EXPORTS` | Optional | Files to export; split automatically into header and library exports |
| `INCLUDES` | Optional | Comma-separated include paths |
| `PREINCLUDES` | Optional | Primary include path; defaults to `C:` |
| `NOLIBFILE` | Optional | Library format selector |
| `NOEXPORTS` | Optional | Set to `yes` to suppress automatic export of compiled library files |
| `NO32BITLIBS` | Optional | If defined, 32-bit variants are not built |
| `NOMODULELIBS` | Optional | If defined, module variants are not built |
| `INSTALLS` | Optional | Extra source files to copy during source distribution |
| `INITTARGET` | Optional | Additional target at initialisation |
| `CLEANTARGET` | Optional | Additional target during `clean` |

## CApp, BasicApp, Documentation, and Resource Variables

### CApp

| Variable | Required | Description |
|---|---|---|
| `COMPONENT` | Required | Component name; bundle named `!COMPONENT` by default |
| `OBJS` | Optional | Object files to compile; if unset, bundle contains resources only |
| `LIBS` | Optional | Libraries to link |
| `CDEFINES` | Optional | Preprocessor definitions |
| `INCLUDES` | Optional | Comma-separated additional include paths |
| `TARGET` | Optional | Application bundle name; defaults to `!COMPONENT` |
| `LIBCOMPONENT` | Optional | Export subdirectory for any library exports |
| `RESOURCES` | Optional | Resource files to copy during installation |
| `EXPORTS` | Optional | Files to export; split automatically into headers and libraries |
| `NOCLIB` | Optional | If defined, C library is not linked |
| `I18N` | Optional | Set to `yes` for internationalisation |
| `INITTARGET` | Optional | Additional target at initialisation |
| `CLEANTARGET` | Optional | Additional target during `clean` |

### BasicApp

| Variable | Required | Description |
|---|---|---|
| `COMPONENT` | Required | Component name; bundle named `!COMPONENT` by default |
| `TARGET` | Optional | Application bundle name; defaults to `!COMPONENT` |
| `RESOURCES` | Optional | Additional resource files to copy during installation |
| `EXPORTS` | Optional | Files to export |
| `NOSQUISH` | Optional | If defined, the `!RunImage` is not squished |
| `INITTARGET` | Optional | Additional target at initialisation |
| `CLEANTARGET` | Optional | Additional target during `clean` |

### Documentation

| Variable | Required | Description |
|---|---|---|
| `COMPONENT` | Required | Component name |
| `DOCSRC` | Optional | PRM-in-XML source files to build and install |
| `INSTALL` | Optional | Additional files to copy during `install` |
| `TARGET` | Optional | Output name; defaults to `COMPONENT` |
| `INITTARGET` | Optional | Additional target at initialisation |
| `CLEANTARGET` | Optional | Additional target during `clean` |

### Resource

| Variable | Required | Description |
|---|---|---|
| `COMPONENT` | Required | Component name |
| `TARGET` | Optional | Output name; defaults to `COMPONENT` |
| `RESOURCES` | Optional | Resource files for the `resources` target |
| `INSTALL` | Optional | Files to copy during `install` |
| `EXPORTS` | Optional | Files to export (explicit export rules required) |
| `CLEANTARGET` | Optional | Additional target during `clean` |

## Export Paths and Patterns

| Variable | Description |
|---|---|
| `${EXP_HDR}` | Assembly header export path (`Hdr:` style headers) |
| `${EXP_C_H}` | C header export path (`C:` style headers) |
| `${EXP_LIB}` | Library export root |

Common `INITTARGET`/`CLEANTARGET` pattern for a generated `h/modhead`:

```makefile
INITTARGET  = inittarget
CLEANTARGET = cleantarget

include CModule

cleantarget:
        ${DESTROY} h.modhead

inittarget:
        ${MKDIR} h
```

Common export rule patterns:

```makefile
EXPORTS = ${EXP_C_H}.${COMPONENT}SWIs

include CModule

${EXP_C_H}.${COMPONENT}SWIs: cmhg.modhead
        ${CMHG} ${CMHGFLAGS} -xh $@ cmhg.modhead
```

```makefile
EXPORTS = ${EXP_LIB}.${COMPONENT}.h.myheader

include LibExport

${EXP_LIB}.${COMPONENT}.h.myheader: h.myheader
        ${CP} $?  $@  ${CPFLAGS}
```
