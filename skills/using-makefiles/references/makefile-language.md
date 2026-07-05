# AMU Makefile Language Reference

This reference is the local detailed source for the AMU makefile language used
by the `using-makefiles` skill. Keep it aligned with the `riscos-help
makefiles` topic when behaviour or conventions change.

## Makefile Format

AMU makefiles are plain ASCII text. On RISC OS the normal file type is
`0xFE1` (`Makefile`), which is why projects in this environment usually store
them as `Makefile,fe1`. Older text-typed makefiles can still be read, but the
RISC OS Make tool would not manage them in the same way.

A makefile is read as a sequence of logical lines. A logical line may continue
onto the next physical line when each continued line ends with `\`.

Comments begin with `#` and run to the end of the logical line. The one active
comment recognised by AMU is:

```makefile
# Dynamic dependencies:
```

This marks the section that tools may update automatically. Other comment lines
are ignored by AMU and may be used freely for documentation.

The non-empty logical lines in a makefile are dependency lines, command lines,
macro definition lines, and special-rule lines.

## Dependency Lines

A dependency line has the form:

```makefile
target-list : prerequisite-list
```

It must not begin with white space. Spaces before the colon are optional, but
some white space must follow the colon so that AMU can distinguish it from a
colon inside a RISC OS path.

Commands for a dependency follow immediately after it and must begin with white
space. For best compatibility, begin command lines with a tab, although spaces
also work with AMU. A single-command rule may also be written with a `;` on the
dependency line itself:

```makefile
clean:; wipe o.* ~cfq
```

If several targets appear on the left-hand side, that is shorthand for writing
the same rule separately for each target. Multiple dependency lines for the
same target accumulate prerequisites, but only one of those entries may supply
commands when `:` is used.

## Macros

Macro definition lines have the form:

```makefile
NAME = text to the end of the line
```

Macros are referenced as `${NAME}` or `$(NAME)`. Undefined macros simply expand
to nothing. This is the normal way to centralise compiler commands, flags,
target names, and lists of objects or libraries. Macro names are
case-insensitive, which differs from GNU `make` and matters when porting
makefiles.

AMU also supports the GNU-style assignment forms `:=`, `?=`, and `+=`. `:=`
expands immediately at the point of assignment. `?=` assigns only when the
macro does not already exist. `+=` appends to the existing value.

The first rule in the makefile may be written in terms of a macro definition,
so the default target can be selected indirectly. Even so, using a visible
target such as `all` is usually easier to read.

Macros can also be pre-defined on the command line:

```bash
riscos-amu COMPONENT=MyTool
```

The `override` directive can be used inside the makefile when you need to alter
or append to a macro that came from the command line. Without `override`,
command-line definitions are normally protected from later changes in the file.

The `origin` function reports where a macro came from, which is useful in
conditional logic and when debugging precedence issues.

Useful built-in and automatic macros:

* `$@` is the current target.
* `$*` is the matched stem in an inference rule.
* `$<` is the inferred source dependency.
* `$?` is the set of prerequisites newer than the target.
* `MAKE` is the AMU command to use for recursive builds.
* `MFLAGS` carries the option state passed to AMU.
* `MAKEFLAGS` is the flag-only subset of `MFLAGS`.
* `MAKECMDGOALS` contains the explicit target names from the command line.

Build-platform helper macros are also defined before the makefile is parsed:
`__riscos` for native RISC OS builds, `__crosscompile` for host-side
cross-builds, `__linux` as the older host-side name, and `MAKEFILEDIR` when
AMU can determine the active makefile's directory.

## Pattern Rules and Special Features

AMU supports suffix-based inference rules using `.SUFFIXES` and special targets
such as `.c.o`. Automatic variables are available inside commands:

* `$@` for the target being built.
* `$*` for the target name with its suffix removed.
* `$<` for the inferred prerequisite list.
* `$?` for the prerequisites that are newer than the target.

AMU uses several special targets to control behaviour:

* `.PHONY` marks synthetic targets that should always run.
* `.SILENT` suppresses command echoing globally.
* `.IGNORE` ignores command failures globally.
* `.INIT` runs before the requested targets are processed.
* `.DONE` runs after a successful build.
* `.FAILED` runs after a failed build.
* `.DEFAULT` provides a fallback rule when no explicit or inferred rule exists.
* `.SUFFIXES` controls suffix inference rules.
* `.UNIXNAMES` favours Unix-style filename handling.

At command level, a leading `@` suppresses echoing for that command and a
leading `-` ignores failures for that command only.

AMU also supports `VPATH`, which gives a search path for prerequisites that are
not found relative to the working directory or their explicit path. AMU accepts
RISC OS, UNIX-like, and MS-DOS-like filename syntaxes in makefiles, although
using one consistent style is easier to maintain.

If `::` is used instead of `:`, repeated dependency lines for the same target
are kept as separate rules, each with its own commands. This is used by some
generated makefiles.

GNU-style `include` and `.include` directives are supported. Prefix the
directive with `-` to ignore missing include files. This is the mechanism used
by many RISC OS projects to pull in shared build fragments.

Conditional directives are also available: `ifeq`, `ifneq`, `ifdef`, `ifndef`,
`else`, and `endif`. These are evaluated while the makefile is read, so they
control which rules and macro definitions AMU sees at all.

AMU implements a useful subset of GNU make functions, including:

* Text and pattern helpers such as `subst`, `patsubst`, `strip`, `sort`,
  `findstring`, `filter`, and `filter-out`.
* Word and list helpers such as `word`, `wordlist`, `words`, `firstword`,
  `lastword`, `join`, `addprefix`, and `addsuffix`.
* Filename helpers such as `dir` and `notdir`.
* Flow-control helpers such as `if`, `foreach`, `call`, `warning`, `error`,
  and `origin`.
* `wildcard` for existence checks and simple wildcard matching.
* `lc` as a non-standard extension that converts text to lower case.

The `wildcard` function should not be treated as a full GNU `make` equivalent.
It is safest as a presence test or for simple local patterns. The function
names `suffix`, `basename`, and `shell` exist in the implementation but are
still marked as needing implementation and should not be relied upon.

## Behaviour Notes

AMU executes each command through the C library `system()` call, which then
uses `OS_CLI`. On RISC OS that means the child command runs with less memory
than AMU itself, because AMU has to be moved in workspace first. Writing a
command file with `-o`, or inspecting commands with `-n`, can be useful when
memory is tight.

After a command runs, the most recent system return code is also recorded in
the `AMU$ReturnCode` system variable.

There is also a RISC OS command length limit of 255 characters. The compiler
and linker cooperate with DDEUtils for longer argument handling, but other
commands in a makefile may still need short command lines.

On systems with filename truncation disabled, non-file target names longer than
10 characters can fail when AMU tries to inspect their timestamps. Keep that in
mind for synthetic targets such as `install_rom`.

The build logic in a makefile is executable code, not passive metadata. Running
an untrusted makefile, or included fragments from untrusted paths, can execute
arbitrary commands.
