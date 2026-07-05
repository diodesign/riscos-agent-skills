# Indexed manual sets

## When to use them

When creating a multi-file PRM-in-XML manual set, prefer an indexed collection
in addition to the per-chapter HTML files.

Always check whether the user actually wants a multi-document manual set before
introducing `index.xml` and indexed output.

## Recommended `index.xml` defaults

Unless the user asks for a different presentation, use:

* `page-format="html5"`
* `catalog-version="103"`
* `include-source="no"`
* `include-sections="no"`
* `chapter-contents="no"`
* `docgroup-part=""`
* `page-css-base="standard"`
* `index-css-base="standard"`
* `page-css-variant="prm body-fraunces heading-raleway webfont-fraunces webfont-raleway large-bullets"`
* `index-css-variant="prm body-fraunces heading-raleway webfont-fraunces webfont-raleway large-bullets no-edge-index"`

The footer text is not a style default. Write it for the actual manual and
normally include copyright information plus any notices about completeness or
accuracy.

Leave `docgroup-part` empty by default. It is usually only useful when the
output really is one volume of several.

Do not add `<make-index type="link" />`; `link` is not a valid generated index
type. Only add a `sysvar` index when the documents actually define system
variables.

If a section supplies an `edgeindex` and the value changes between sections,
also give that section a `docgroup-name`.

Appendix pages should normally be lettered `A`, `B`, `C`, and so on, not
treated as an extra numbered part.

## Recommended indexed `index.xml` shape

```xml
<?xml version="1.0"?>
<index>
<dirs output="../html/indexed/pages"
      index="../html/indexed"
      help="../html/indexed/help"
      header="../html/indexed/header"
      input="."
      temp="../html/indexed/tmp" />
<options
    hide-empty="no"
    include-source="no"
    make-contents="no"
    include-sections="no"
    include-sections-depth="1"
    catalog-version="103"
    page-format="html5"
    page-css-base="standard"
    page-css-variant="prm body-fraunces heading-raleway webfont-fraunces webfont-raleway large-bullets"
    page-css-file="none"
    index-css-base="standard"
    index-css-variant="prm body-fraunces heading-raleway webfont-fraunces webfont-raleway large-bullets no-edge-index"
    index-css-file="none"
    docgroup-name="Document set name"
    docgroup-part=""
    chapter-numbers="yes"
    chapter-contents="no"
    edgeindex-max="4"
    />

<make-index type="command" />
<make-indexdata/>
<make-filelist/>

<footer>
Copyright ... plus any notices about the accuracy or completeness of the
documentation.
</footer>

<front-matter type="title" href="front/title-page"/>
</index>
```

## Local `Makefile` pattern

For multi-file manual sets, prefer a small local `Makefile` that builds:

* per-chapter lint results
* per-chapter HTML output
* the indexed collection
* optionally a PDF from the indexed HTML when Prince is installed

Use explicit XML ordering if the book structure matters.

```make
XMLS = \
	part1/01-introduction.xml \
	part1/02-prerequisites.xml \
	appendix/a1-reference.xml

.PHONY: all lint html lint-indexed indexed pdf clean

all: lint html indexed

lint:
	@for file in $(XMLS); do \
		echo "Linting $$file"; \
		riscos-prminxml -f lint "$$file"; \
	done

html:
	@mkdir -p ../html
	@for file in $(XMLS); do \
		echo "Building $$file"; \
		riscos-prminxml -f html5+xml -O ../html "$$file"; \
	done

lint-indexed:
	@mkdir -p ../html/indexed/logs
	@echo "Linting indexed document set"
	@riscos-prminxml --lint -f index -L ../html/indexed/logs index.xml

indexed:
	@mkdir -p ../html/indexed/logs
	@echo "Building indexed document set"
	@riscos-prminxml -f index -L ../html/indexed/logs index.xml

pdf: indexed
	@if command -v prince >/dev/null 2>&1; then \
		cd ../html/indexed/pages && prince -l filelist.txt -o Manual.pdf; \
	else \
		echo "Prince is not installed; skipping PDF generation"; \
	fi

clean:
	rm -rf ../html
```

If the user explicitly wants Prince output, keep the `pdf` target. Do not
assume Prince is available without checking.

## Metadata

The `<meta>` section at the end of a document should include:

```xml
<meta>
  <maintainer>
   <email name="Your Name" address="you@example.com"/>
  </maintainer>
  <disclaimer>
   <p>Copyright and license information</p>
  </disclaimer>
  <history>
   <revision number="1" date="25 March 2026" author="ABC" title="Initial version">
    <change>Created documentation</change>
   </revision>
  </history>
  <related>
   <reference type='document' href='?' name='Related Document'/>
  </related>
</meta>
```

Update the visible history with each major change. The earliest change should
go first; add later revisions at the end.

The `<meta>` element must appear after all `<chapter>` elements as a direct
child of `<riscos-prm>`.

## Advanced document metadata

The `<chapter>` element supports:

* `docgroup`
* `docgroup-part`

Use those only when the chapter genuinely belongs to a grouped manual set.

## Index format

The `index` format collects multiple PRM-in-XML documents into one navigable
site.

For multiple documents, create an index file such as:

```xml
<?xml version="1.0"?>
<index>
<dirs output="output/html" index="output/index" input="." temp="tmp"/>
<options page-format="html5" catalog-version="103" ... />
<make-index type="swi"/>
<make-index type="service"/>
<section title="Section Name" dir="dir">
    <page href="Document">Document Title</page>
</section>
</index>
```

Build it with:

```bash
riscos-prminxml -f index Index.xml
```
