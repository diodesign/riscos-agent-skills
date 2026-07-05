# Building Pascal

## Source Layout

Pascal source files live in `p/`:

```text
p/hello
p/main
```

Unlike the C, C++, and Fortran wrappers, `riscos-p2cc` takes the host path
directly rather than a RISC OS-style dotted path:

```sh
riscos-p2cc -32 p/hello -o hello,ff8
```

`p/hello` is passed as `p/hello`, not `p.hello` or `hello.p`.

## Direct Build: 32-bit

The `o/` directory must exist first, even for a combined
translate-compile-link command; the 32-bit compiler writes an intermediate
object file there and fails with
`Compilation aborted: couldn't write file 'o/p2c-XX...'` if it is missing:

```sh
mkdir o
riscos-p2cc -32 p/hello -o hello,ff8
```

Run it with:

```sh
riscos-build-run hello,ff8 --command hello
```

Always pass `-26`, `-32`, or `-64` explicitly. Without one of these,
`riscos-p2cc` defaults to 26-bit code, which fails with
`26 bit absolute files are not executable on this system` on a 32-bit or
64-bit system.

## Direct Build: 64-bit

Same shape, using `-64` (or the convenience wrapper `riscos64-p2cc`):

```sh
riscos-p2cc -64 p/hello -o hello,ff8
```

Run it with:

```sh
riscos-build-run --64 hello,ff8 --command hello
```

The 64-bit compiler does not need `o/` to exist first for this combined
form.

## Separate Compile and Link: 32-bit

To split translation/compilation from linking, use `-c` and link explicitly
with the P2C runtime library and stub:

```sh
mkdir o
riscos-p2cc -32 -c -o o/hello p/hello
riscos-link -aif o/hello C:o.stubsGS C:p2c.o.libp2c-32 -o hello,ff8
```

## Creating a Project: 32-bit

```sh
riscos-project create --type pcommand --name MyTool --skeleton
riscos-amu
```

This writes the skeleton to `p/main`, and the final executable into
`aif32/`.

## Creating a Project: 64-bit

```sh
riscos-project create --type pcommand --name MyTool --skeleton
riscos-amu BUILD64=1
```

This writes the final executable into `aif64/`, using the same
`riscos64-p2cc` translate-compile-link pipeline as the direct 64-bit form
above. No special variables are needed beyond `BUILD64=1`.

## Command Line Arguments

```pascal
program args;
var
    i: integer;
begin
    writeln('Argument count: ', paramCount);
    for i := 1 to paramCount do
        writeln('Arg ', i, ': ', paramStr(i));
end.
```

`paramCount` is the number of arguments supplied; `paramStr(n)` returns the
nth argument as a string.
