# Testing PyModules

PyModule integration tests in the Pyromaniac repository live under `testcode/` and use
gold-master output matching.

Run them with:

```bash
bash run-tests <suite-name>
```

The log is written to `/tmp/pyro-tests-<suite-name>.log`. Read that file for detailed pass/fail output.

## Mixed Python/C module tests

`riscos-run` can load PyModules and native RISC OS modules together. This is useful when a PyModule must interoperate with an existing C module, or when a small native test fixture is the easiest way to exercise service calls, callbacks, or SWI registration paths.

Example:

```bash
riscos-run --load-pymodule filtermanager.py \
           --load-module test/filterreg/rm32/FilterRegTest,ffa \
           --command 'FilterRegTestStatus' \
           --command '*Filters'
```

This style of test is particularly useful for:

- checking that startup service announcements are observed by native modules
- validating SWI-compatible registration interfaces
- proving that a PyModule and a native module can coexist without crashing

## Test suite file format

Each suite is a file `testcode/tests-<name>.txt`. The master list `testcode/tests.txt` includes them via `Include:` lines.

A minimal suite file looks like this:

```text
#
# SUT:    Extension Modules: MyModule
# Area:   SWIs
# Class:  Functional
# Type:   Integration test
#

Group: MyModule: Basic operations

Test: Init and reinit
Command: $TOOL --load-internal-modules --command "RMReinit MyModule"
Expect: expect/pymodules/mymodule/reinit

Test: Help text
Command: $TOOL --load-internal-modules --help-config mymodule.implementation
Expect: expect/pymodules/mymodule/help_implementation
```

`$TOOL` is substituted with the `pyro.py` invocation.

Common options:

- `--load-internal-modules`
- `--load-internal-group core`
- `--config key=value`
- `--set-variable "Name=value"`
- `--set-variable-encoded "Name:charset=value"`
- `--command 'RISC OS command'`
- `--boot-debug <flag>`

## Parameterised tests

Groups can share a command template, with each test supplying an `Args:` substitution:

```text
Group: MyModule: Operations

Command: $TOOL --load-internal-modules bin/mymodule_test $ARG1
Expect: expect/pymodules/mymodule/$ARG1

Test: Create handle
Args: create

Test: Close handle
Args: close
```

## Replacement scripts

If the output contains timestamps or other variable content, use a `Replace:` file to normalise it:

```text
Test: Show timestamp
Command: $TOOL --load-internal-modules --command "MyMod_ShowTime"
Expect: expect/pymodules/mymodule/showtime
Replace: expect/pymodules/mymodule/replacements
```

A replacements file contains Perl-style substitutions, one per line:

```text
s/\d{4}-\d{2}-\d{2}/DATE/g
s/\d{2}:\d{2}:\d{2}/TIME/g
```

## Creating expectation files

Run the command manually and capture its output:

```bash
python3 pyro.py --load-internal-modules --command "MyCommand" > testcode/expect/pymodules/mymodule/mycommand
```

Expectation files live in `testcode/expect/<suite-subpath>/`.

## Adding a test to an existing suite

1. Open the relevant `testcode/tests-<name>.txt`.
2. Add a `Test:` block inside the appropriate `Group:`, or create a new `Group:` if needed.
3. Create the corresponding expectation file in `testcode/expect/`.
4. Run `bash run-tests <name>` and confirm the new test passes.

## Registering a new suite

Add an `Include:` line to `testcode/tests.txt` in the appropriate section, in alphabetical order:

```text
Include: tests-pymodules-mymodule.txt
```
