# Assembly test workflow for Pyromaniac

This reference describes the pattern used by small assembly exercisers in
`testcode/s/`.

## Source layout

The usual structure is:

```asm
        AREA    |Test$$Code|, CODE

        GET     hdr.swis
        GET     hdr.printmacros
        GET     hdr.macros

toolname ROUT
        Push    "lr"
        MOV     r8, r1
```

`R1` contains the command tail. Most tools move it to `R8` and keep `R8` as the
current parse pointer.

## Argument parsing

For simple tools, dispatch on one-character verbs:

```asm
10
        ADR     lr, %BT10
        LDRB    r0, [r8], #1

        TEQ     r0, #'r'
        BEQ     do_register
```

When you need structured values, pull in routines from `_args_common.s`:

- `get_string`
- `get_spaced_string`
- `get_number`
- `get_signed`
- `get_hex`
- `get_dimensions`

Those helpers assume:

- `R8` points at the current argument text
- they update `R8` on return
- they only corrupt the documented result registers and `R14`

## Printing and diagnostics

Use `hdr.printmacros` for deterministic textual output:

- `PrintMessage`
- `PrintLine`
- `PrintInteger`
- `PrintSigned`
- `PrintHex`
- `PrintString`
- `PrintStringN`

Keep the output stable and compact. The tests compare exact text.

## SWI calls

Use `XSWI` from `hdr-macros.s` when loading literal pointers or immediate
values into argument registers would otherwise be noisy. Use plain `SWI` when
the registers are already prepared.

## Building

`testcode/Makefile` assembles every `testcode/s/*` file except names beginning
with `_` and links them into `testcode/bin/<name>`.

Useful commands:

```bash
make testcode
make -C testcode bin/urlfetcher
```

When you change or add an assembly test tool, rebuild the corresponding
`testcode/bin/<name>` binary and commit it with the source. CI for these suites
executes the checked-in test binaries; it does not verify that they can be
rebuilt first.

## Running

Manual run:

```bash
./pyro.py --load-internal-modules testcode/bin/urlfetcher rgsdx
```

Suite run:

```bash
make tests TEST=pymodules-urlfetcher
```

## Suite layout

The usual suite file keeps a shared `Command:` and `Expect:` at group scope and
uses `Args:` to select scenarios. See `example-tests-pymodules-urlfetcher.txt`.
