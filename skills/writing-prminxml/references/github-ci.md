# GitHub CI integration for PRM-in-XML

Use GitHub Actions when PRM-in-XML documents should be exported as build
artifacts for review, release packaging, or publication.

## Recommended workflow step

Add a documentation job to the workflow and use
`gerph/riscos-prminxml-action@v1` to render the source documents:

```yaml
build-docs:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v7

    - name: Build modern PRM-in-XML documentation with Prince PDF
      uses: gerph/riscos-prminxml-action@v1
      with:
        files: prminxml/manual.xml prminxml/reference.xml
        output: output
        pdf-generator: prince
        style: prm
```

## Inputs to configure

Set these values for the repository being documented:

* `files`: Space-separated list of PRM-in-XML source files to build.
* `output`: Directory where generated files will be written.
* `pdf-generator`: Set to `prince` when PDF output is required.
* `style`: Select the output style. `prm` is the default house style for
  PRM-like manuals unless the repository wants a different look.

Keep the output directory separate from the source directory so generated files
do not overwrite the XML sources.

## Packaging generated documentation

If the documentation should be downloadable from the workflow, package the
output directory after rendering:

```yaml
    - name: Package documentation
      run: |
        version=$(git rev-parse --short HEAD)
        leafname="Documentation-$version.zip"
        cd output && zip -9r "../$leafname" *
        echo "leafname=$leafname" >> $GITHUB_OUTPUT
      id: docsversion

    - name: Upload documentation artifact
      uses: actions/upload-artifact@v7
      with:
        name: Documentation
        path: ${{ steps.docsversion.outputs.leafname }}
```

If the repository already has a version file or release naming convention, use
that instead of the git hash when creating the archive name.

## When updating documentation sources

Whenever PRM-in-XML documents are added, removed, or renamed:

* Update the `files:` list in the workflow.
* Keep the packaging step aligned with the chosen output directory.
* Preserve both HTML and PDF outputs if the workflow is intended to produce
  distributable documentation.

## Practical guidance for skill users

When asked to add PRM-in-XML export to GitHub CI:

* Add or update a docs job in `.github/workflows/*.yml`.
* Use `gerph/riscos-prminxml-action@v1` rather than hand-rolling the conversion
  commands.
* Ensure the resulting `output` directory is either uploaded directly or zipped
  and uploaded as an artifact.
