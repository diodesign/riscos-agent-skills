# Pyromaniac tooltester notes

Use this alongside the main `using-tooltester` skill when the repository uses
`testcode/test.pl`.

## Entry points

The top-level `Makefile` is the normal entry point:

```bash
make tests
make tests TEST=pymodules-urlfetcher
make tests64 TEST=introspection
make testcode
```

Important details from the Makefile:

- `make tests` runs `pythontests` before integration tests
- integration tests always run with `TZ=UTC`
- JUnit XML goes to `artifacts/results.xml`
- `--show-command` is enabled, so failures print the exact command line
- `TEST=<name>` selects `testcode/tests-<name>.txt`

## Suite registration

There are two useful modes while developing a suite:

1. `make tests TEST=<name>`
   No `Include:` line is needed in `testcode/tests.txt`.
2. `make tests`
   The suite must be included from `testcode/tests.txt`.

This makes `TEST=` the faster path while iterating on a new suite.

## Common Pyromaniac command patterns

RISC OS command tests:

```text
Command: $TOOL --load-internal-modules --command '*MyCommand'
```

Assembly helper under `testcode/bin/`:

```text
Command: $TOOL --load-internal-modules bin/mytool $ARG1
```

Command-driven helper with a host file argument:

```text
Command: $TOOL --load-internal-modules --command 'Run TestThing' testcode/basic/TestThing,fd1
```

## Expectations and failures

Expectation files normally live under `testcode/expect/...`.

On a mismatch, `test.pl` writes `<expect-file>-actual`. That is the first file
to inspect, because it contains the output after any `Replace:` script has been
applied.

When a test starts failing after a deliberate output change:

1. run the suite again
2. inspect the `-actual` file
3. diff expected versus actual
4. only then decide whether the expectation or the code is wrong

## Replacement scripts

Use `Replace:` when the output contains unstable values such as:

- absolute host paths
- memory addresses
- dates and timestamps
- git SHAs or branch names

Normalise those values rather than baking machine-specific output into the
expectation file.
