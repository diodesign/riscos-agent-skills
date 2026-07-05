# CI Pattern Notes

These notes describe reusable CI shapes that often appear in RISC OS repositories.
The local workspace may contain files that demonstrate these shapes, but the skill
should apply the patterns generically rather than copying project-specific names.
When a build-service configuration file is needed, `.robuild.yaml` is preferred,
but `.robuild.yml` is also valid.

## 1. GitHub 32-bit build-service pattern

Use this shape when:

- GitHub Actions should submit the build to build.riscos.online;
- the repository wants the common `riscos-project create-ci` baseline;
- the workflow should build a 32-bit result through a `.robuild.yaml` or `.robuild.yml` file.

Typical structure:

- check out the repository on Ubuntu;
- download `riscos-build-online`;
- zip the source tree together with `.robuild.yaml` or `.robuild.yml`;
- submit the archive to build.riscos.online;
- rename the returned archive using `Module_FullVersion` from `VersionNum` or the git hash;
- upload the archive as a GitHub Actions artifact;
- optionally create a draft release for `v*` tags.

This is the common generated baseline from `riscos-project create-ci`.

## 2. GitLab 32-bit build-service pattern

Use this shape when:

- GitLab CI should submit work to build.riscos.online rather than build locally;
- the repository wants the common `riscos-project create-ci` baseline;
- the artifact should be returned from the build service and then renamed by GitLab CI.

Typical structure:

- download `riscos-build-online`;
- zip the source tree with `.robuild.yaml` or `.robuild.yml`;
- submit that archive to build.riscos.online;
- rename the returned archive based on `VersionNum`;
- publish a `*.zip` archive as a GitLab artifact.

This is also part of the common generated baseline from `riscos-project create-ci`.

## 3. GitHub local 32-bit and 64-bit build pattern

Use this shape when:

- the deliverable is an exported library tree;
- there is no useful standalone runtime test;
- GitHub can build the exports directly inside a RISC OS build container.

Typical structure:

- check out the repository on Ubuntu;
- run inside a container such as `gerph/riscos-build:latest-64bit`;
- build 64-bit and 32-bit outputs locally with `riscos-amu`;
- run `export` for both build variants;
- copy the exported library tree into an `Artifacts` directory;
- create the RISC OS zip on the host side;
- rename it using `Module_FullVersion` from `VersionNum` or the git hash;
- upload the archive as a GitHub Actions artifact;
- optionally create a draft release for `v*` tags.

Why this shape fits:

- the real product is an exported library tree, not a single runnable binary;
- there is no need to round-trip the export through build.riscos.online;
- packaging the exported tree directly is simpler than inventing a runtime test.

## 4. `riscos-project create-ci` baseline

Use this shape when:

- the repository has no CI yet;
- you want the standard generated 32-bit build-service setup first;
- you intend to create both GitHub and GitLab CI definitions quickly before refining them.

Typical structure:

- generate `.github/workflows/ci.yml`;
- generate `.gitlab-ci.yml`;
- generate `.robuild.yaml` or sometimes `.robuild.yml`;
- leave the result as a working 32-bit build-service baseline to refine.

Important limitation:

- it is only the starting point;
- many repositories will then extend GitHub CI to 64-bit or switch GitHub to local container builds.

## 5. How to use these patterns

Choose based on output type:

- Standard generated 32-bit build-service CI on GitHub: use the GitHub 32-bit build-service pattern.
- Standard generated 32-bit build-service CI on GitLab: use the GitLab 32-bit build-service pattern.
- Library export on GitHub with local builds: adapt the GitHub local 32-bit and 64-bit build pattern and package only the export tree.
- Library export on GitHub or GitLab via build service: start from `riscos-project create-ci`, then adapt the generated CI file plus `assets/library-export.robuild.yaml`.
- AIF binary: start from `assets/binary-build-test-release-ci.yml` and `assets/aif-test.robuild.yaml`.
- RM/module: start from `assets/binary-build-test-release-ci.yml` and `assets/rm-test.robuild.yaml`.

If you begin with `riscos-project create-ci`, treat the generated files as the normal baseline for both GitHub and GitLab, then merge in the relevant pattern above.
