# Workflow Templates

## Library export workflow

Use `assets/library-export-ci.yml` with `assets/library-export.robuild.yaml` when:

- the repository's deliverable is an exported library tree;
- the build result should be zipped and attached as an artifact or release;
- runtime execution on RISC OS is not the main validation path.

Replace these placeholders:

- `{{WORKFLOW_NAME}}`
- `{{ARCHIVE_STEM}}`
- `{{VERSION_FILE}}`
- `{{SOURCE_ARCHIVE_FILES}}`
- `{{ARTIFACT_NAME}}`

Keep the `.robuild.yaml` and workflow aligned:

- the workflow must upload the same files that `.robuild.yaml` or `.robuild.yml` needs;
- the workflow must expect the same returned archive shape that `.robuild.yaml` or `.robuild.yml` produces.
- when deriving an archive version from `VersionNum`, prefer `Module_FullVersion`.

## Binary build/test/release workflow

Use `assets/binary-build-test-release-ci.yml` when:

- the repository produces runnable AIF or RM outputs;
- you want both 32-bit and 64-bit builds;
- you want a separate test job that exercises the produced binary through build.riscos.online;
- you want a draft GitHub release for tagged builds.

Replace these placeholders:

- `{{WORKFLOW_NAME}}`
- `{{CONTAINER_IMAGE}}`
- `{{BUILD_DIR}}`
- `{{VERSION_FILE}}`
- `{{ARCHIVE_STEM}}`
- `{{ARTIFACT_NAME}}`
- `{{RISCOS_ARCHIVE_NAME}}`
- `{{BUILD_64_COMMANDS}}`
- `{{BUILD_32_COMMANDS}}`
- `{{PACKAGE_COMMANDS}}`
- `{{TEST_SOURCE_FILES}}`
- `{{TEST_ARCH}}`

Then choose one test file:

- `assets/aif-test.robuild.yaml` for AIF commands or applications;
- `assets/rm-test.robuild.yaml` for modules.

## `riscos-project create-ci`

Use `riscos-project create-ci` when the repository has no CI yet or when you want a known-good starting point for the common generated 32-bit build-service setup.

Expected use:

1. Run `riscos-project create-ci`.
2. Read the generated `.github/workflows/ci.yml`, `.gitlab-ci.yml`, and `.robuild.yaml` or `.robuild.yml` when present.
3. Decide whether the repository is a library export or a runnable binary.
4. Decide whether to keep the build-service shape or switch GitHub to direct local 32-bit and 64-bit container builds.
5. Merge in the matching asset template rather than rewriting from scratch.

Do not leave the generated workflow unreviewed:

- it may only cover 32-bit builds;
- it may not include release handling;
- it may not include build-service runtime tests;
- it may not match the repository's preferred artifact naming.
- it may parse `VersionNum` too loosely; prefer `Module_FullVersion` for archive naming.
- it may assume build-service execution when direct local GitHub container builds would be simpler.

## GitLab notes

When updating `.gitlab-ci.yml`:

- keep `script:` shell fragments POSIX-portable unless the job explicitly selects Bash;
- prefer `riscos-project create-ci` as the baseline shape when the repository does not already have a better GitLab pattern;
- if the pipeline still uses build.riscos.online, keep `.robuild.yaml` or `.robuild.yml` aligned with the files zipped into the source archive;
- if the GitLab job names archives from `VersionNum`, prefer `Module_FullVersion`.

## File naming

Prefer `.robuild.yaml` for new work.
Accept `.robuild.yml` when the repository already uses that spelling or the generated baseline produced it.

## PRM-in-XML documentation jobs

If the CI pipeline must publish documentation:

- use the `writing-prminxml` skill;
- read `/etc/agentskills/writing-prminxml/references/github-ci.md`;
- add a separate documentation job or a clearly separate documentation step.

Do not mix documentation packaging into a binary test job unless the repository already uses that shape.
