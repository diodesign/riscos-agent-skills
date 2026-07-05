# Pitfalls and Checks

## Build Pitfalls

Always pass `-26`, `-32`, or `-64` explicitly to `riscos-p2cc`. The default
(no switch) produces 26-bit code, which builds without error but fails at
run time with `26 bit absolute files are not executable on this system` on
a 32-bit or 64-bit system. This is easy to miss because translation and
compilation both succeed silently.

The `o/` directory must exist before a 32-bit build, even for a single
combined `riscos-p2cc -32 ... -o name,ff8` command with no explicit `-c`.
The 64-bit form (`riscos-p2cc -64` / `riscos64-p2cc`) does not need this.

`riscos-p2cc` takes the source file as a host path (`p/hello`), not a RISC
OS-style dotted path (`p.hello`) and not a host extension form (`hello.p`).
If a build fails with the input file "not found", check which form was
used.

When linking a 32-bit object manually (after `-c`), the P2C runtime and stub
must be given explicitly: `C:o.stubsGS C:p2c.o.libp2c-32`. The equivalent
64-bit libraries are `RO64C:o.libcrt C:p2c.o.libp2c-64`, added automatically
by `riscos64-p2cc`/`riscos-amu BUILD64=1`.

## Language Pitfalls

**Do not print a `real` value with `write`/`writeln` in a 32-bit build.**
This produces incorrect output (`0.0`, or garbage for an unformatted
`writeln(x)`) due to a variadic-double calling-convention bug in the 32-bit
toolchain. Verify by checking: does `real` arithmetic on the same value
produce the correct result when converted to an integer (eg
`trunc(x * 2)`)? If so, the value itself is fine and only the direct
`real` print path is broken. 64-bit builds print `real` values correctly;
prefer 64-bit, or convert to an integer for display, when a 32-bit program
must show a computed value.

Assignment is `:=`; `=` is comparison only. Using `=` where `:=` is meant is
a common slip carried over from other languages.

Boolean operators are the words `and`, `or`, `not`, not `&&`/`||`/`!`.

Array bounds are declared explicitly, eg `array[1..3] of integer`; unlike
some other languages there is no fixed default starting index.

Do not assume Pascal `unit`/`module` cross-file compilation works like
Turbo Pascal or Modula units. This has not been verified to work with this
environment's P2C translator; a `module ... end.` file was found to require
an undocumented `IMPLEMENT` structure that did not translate cleanly in
testing. Treat multi-file Pascal builds as unverified: prefer a single
Pascal source file per program, or test thoroughly before relying on
cross-file Pascal compilation.

Similarly, calling arbitrary C functions from Pascal (or Pascal functions
from C) has not been verified in this environment. Do not assert that a
particular interop pattern works without testing it first.

`writeln`/`write` string literals may use either single or double quotes
(the shipped `pcommand` skeleton uses double quotes); do not assume only one
form works.

## Review Checklist

Before declaring Pascal work complete:

* Source files are in `p/`, referenced as host paths (`p/name`), not `p.name`.
* Every direct `riscos-p2cc`/`riscos64-p2cc` invocation passes `-26`, `-32`,
  or `-64` explicitly.
* `o/` exists before any 32-bit build.
* No `real` value is printed directly with `write`/`writeln` in a 32-bit
  build; converted-to-integer or 64-bit output is used instead if display is
  needed.
* Manual 32-bit links include `C:o.stubsGS C:p2c.o.libp2c-32`.
* Boolean logic uses `and`/`or`/`not`, and assignment uses `:=`.
* No untested multi-file `unit`/`module` or C-interop claims were made.
* No trailing whitespace was introduced.
