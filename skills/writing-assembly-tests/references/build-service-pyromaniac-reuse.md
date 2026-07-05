# Reusing Pyromaniac assembly tests through a build service

This reference describes an optional pattern for repositories that build a
module locally but want to reuse Pyromaniac-style assembly tests without
requiring a full Pyromaniac checkout at test time.

Use it when:

- the tests are small ObjAsm command-line exercisers under `testcode/s/`
- the module under test can be copied into a self-contained test archive
- the expected output should stay close to the original Pyromaniac tests
- the repository is willing to ship a local `test.pl` copy and require
  `riscos-build-online`

Do not use it just to add ordinary assembly tests. The simpler direct
Pyromaniac workflow in `workflow.md` is still the default.

## Tree shape

The reusable layout is:

```text
testcode/
  Makefile
  test.pl
  run-on-build-service.sh
  transform-pyro-tests-to-buildservice.sh
  tests.txt
  tests-<area>-pyro.txt
  tests-<area>.txt
  hdr/
  s/
  expect/
```

`tests-<area>-pyro.txt` is the source of truth. `tests-<area>.txt` is generated
from it for the build-service environment. `tests.txt` usually just includes
the generated suite.

Repositories may also keep hand-written `tests-<name>.txt` files for local
smoke tests that were not sourced from Pyromaniac. Those should not use the
transform rule; include them directly from `tests.txt`, usually after the
assembly-based suites.

## Execution model

The flow is:

1. Build the assembly exercisers from `testcode/s/*` into `testcode/bin/*`.
2. Copy the module under test into `testcode/`.
3. Convert the Pyromaniac suite into a local suite.
4. Run the local suite through `test.pl`.
5. For each test, `test.pl` invokes `run-on-build-service.sh` with the
   Pyromaniac-style command line.
6. The runner expands `--command`, `--config`, and `--set-variable` into
   commands inside a generated `.robuild.yaml`.
7. The runner archives the selected files and submits them with
   `riscos-build-online`.
8. The returned text is compared against the expectation files, ideally with
   only small normalisation changes from the original Pyromaniac version.

## Recommended setup order

Apply the example in this sequence:

1. Copy `assets/buildservice-example/testcode/` into the repository.
2. Add any repository-specific helper headers and `s/_*.common` helper sources
   that the bundled example does not provide.
3. Set `MODULE = ...` in `testcode/Makefile`.
4. Update the `tests:` prerequisite list in `testcode/Makefile` to match the
   suites used by the repository.
5. Update `files=(...)` and `modules=(...)` near the top of
   `run-on-build-service.sh`.
6. Add the repository's `tests-<area>-pyro.txt` source suites.
7. Add any hand-written non-Pyromaniac tests separately as plain
   `tests-<name>.txt`.
8. Order `tests.txt` so the simpler assembly suites run before heavier smoke
   tests such as BASIC programs.
9. Run `make` in `testcode/` to build the assembly tools.
10. Regenerate transformed local suites after editing any
    `tests-<area>-pyro.txt` source files.
11. Run `make tests`.

If the generated target `tests-<area>.txt` does not build, verify that the
matching `tests-<area>-pyro.txt` exists and that
`transform-pyro-tests-to-buildservice.sh` is present and executable.

If the transformed suite still appears to run stale commands or expectations,
rebuild it explicitly before investigating the binary or expectation files.

The example bundle already includes a useful baseline of optional common files:

- `hdr/vdu`
- `hdr/osplot`
- `hdr/osspriteop`
- `s/_args_common`
- `s/_dump_common`
- `s/_colourtrans_common`
- `s/_screenmode_common`
- `.gitignore`

Use them when the copied assembly tools depend on those names. If a repository
does not need them, they can simply remain unused.

## What gets transformed

The build-service suite normally needs a few mechanical rewrites:

- expectation paths move from `expect/pymodules/<area>/...` to a local
  `expect/<area>/...`
- replacement-script paths are rewritten in the same way
- `--load-internal-modules` is removed because the runner loads the modules
  explicitly
- `--config messagetrans.support=...` can be removed if the remote environment
  does not need it
- `$TOOL` often gains `--quiet` so the harness emits only stable test output
- RISC OS binary paths such as `bin/<tool>` become local tooltester paths such
  as `bin.<tool>`

Keep this transformation script small and mechanical. The Pyromaniac suite
should remain readable and close to upstream.

Do not send unrelated local smoke tests through this transformation. A
hand-written BASIC or direct build-run suite should remain a normal
`tests-<name>.txt` file.

## Runner responsibilities

`run-on-build-service.sh` is the bridge. It should:

- maintain a short editable list of uploaded files
- maintain a short editable list of modules to `RMLoad`
- ignore Pyromaniac-only switches that are not needed remotely
- convert supported Pyromaniac switches into RISC OS commands inside
  `.robuild.yaml`
- upload the archive with `riscos-build-online`
- tidy line endings in the returned output so the expectations remain stable
- remove temporary files idempotently, for example with `rm -f`, so cleanup
  does not fail after interrupted or repeated runs

Keep the repository-specific configuration near the top of the script. In the
example bundle, the key customisation points are the `files=(...)` and
`modules=(...)` arrays.

Be careful when invoking the bridge directly by hand: the transformed local
suite will normally call dotted RISC OS command paths such as `bin.toolname`,
not host paths such as `bin/toolname`.

Unless you have modified the runner to use unique temporary filenames, do not
run multiple copies in parallel from the same `testcode/` directory. The
simple example uses a shared `.robuild.yaml`, which makes parallel runs race
with each other.

The runner should archive:

- the built command-line test binaries under `bin/`
- any directories needed at runtime, such as `basic/` or `testdata/`
- the module binaries named in `modules=(...)`

## Tooltester copy

This pattern keeps a local `test.pl` in the repository rather than assuming an
external installation. That makes the test harness self-contained and easier to
reuse in CI or on build servers.

When reusing the pattern:

- treat `test.pl` as part of the harness
- keep `tests.txt` as the suite entry point
- let `Makefile` call `./test.pl ... ./run-on-build-service.sh .`

## Example bundle

The skill bundles a complete sample under:

`assets/buildservice-example/testcode/`

Restore those files into a repository `testcode/` tree when you need a
starting point. The example contains:

- the `Makefile`
- the transform and runner scripts
- the local `test.pl`
- a Pyromaniac source suite and its generated local form
- assembly exercisers `s/var_read` and `s/var_set`
- helper headers under `hdr/`
- optional graphics and mode helper headers under `hdr/`
- optional shared helper sources under `s/`
- a sample `.gitignore`
- expectation files under `expect/var/`

That bundle is intentionally concrete so another repository can copy the
structure first and then replace the module-specific parts.
