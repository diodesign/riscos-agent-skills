# Document structure

## DTD declaration

Use the 1.03 DTD with a public label and URL:

```xml
<!DOCTYPE riscos-prm PUBLIC "-//Gerph//DTD PRM documentation 1.03//EN"
                            "http://gerph.org/dtd/103/prm.dtd">
```

## Root element

The root element is `<riscos-prm>`, which has no attributes. It contains one
or more `<chapter>` elements followed by a single `<meta>` element:

```xml
<?xml version="1.0"?>
<!DOCTYPE riscos-prm PUBLIC "-//Gerph//DTD PRM documentation 1.03//EN"
                            "http://gerph.org/dtd/103/prm.dtd">
<riscos-prm>
 <chapter title="Component Title">
  <section title="Introduction and Overview">
   <p>...</p>
  </section>
 </chapter>
 <meta>
  ...
 </meta>
</riscos-prm>
```

## Standard component chapter pattern

For component or interface documentation, this is the normal section ordering:

* Introduction and Overview
* Technical Details
* SWI Calls
* System Variables
* Service Calls
* Vectors
* UpCalls
* Error Messages
* Wimp Messages
* Commands
* Security Issues
* Examples

Remove sections that are not relevant to the component.

For book-style manuals, treat that list as a common component-chapter pattern,
not a mandatory shape for every document. Appendix chapters may use headings
that match their subject matter directly.

If the source material has substantial rationale, historical background, or a
set of motivating examples, it is often better to split the opening into a
short `Introduction` followed by a fuller `Overview` instead of compressing
everything into `Introduction and Overview`.

## Section hierarchy

The correct nesting order is:

```text
chapter
  section
    subsection
      subsubsection
        category
```

Each level can only contain the level below it plus `<p>` elements. A
`<section>` cannot directly contain a `<category>`.

## What to document

The documentation should describe the external interfaces, data structures,
commands, services, vectors, and events used by the component. It should not
describe internal implementation details.

Where a document is intended as a manual or command reference, the reader
should be able to rely on it directly. Avoid making the reader reconstruct the
intended interface from statements about source code, wrappers, or auxiliary
help text.

For a RISC OS module, normally document:

1. `Introduction and Overview`
2. `Technical Details`
3. Service calls the module handles
4. SWIs the module implements
5. Memory usage and compatibility
6. Usage and lifecycle
7. Error messages the module generates
8. Examples

Do not create definition blocks for:

* SWIs that the module calls
* Service calls that the module issues rather than handles
* Standard RISC OS interfaces the module merely uses

SWIs used internally may be mentioned in technical details when they are
intrinsic to the purpose of the call, but they should not be given definition
blocks.

When converting an existing non-XML document into PRM-in-XML, preserve the
parts of the source that explain why the interface exists and how it is meant
to be used. Do not reduce a canonical conversion to a skeletal summary if the
original includes rationale, operational guidance, examples, or release
history that materially explain the interface.

## Authorial voice

Chapter and appendix prose must state facts about RISC OS, the format, or the
tool authoritatively. Do not narrate how the documentation was produced,
checked, or validated.

Wrong:

```xml
<p>
Local template-loading code in the build environment mirrors the Wimp loading
behaviour and shows the basic record structure clearly:
</p>
```

Right:

```xml
<!-- Field breakdown confirmed against the implementation source. -->
<p>
The template data block holds the window's in-memory definition, in the same
layout the Wimp uses internally:
</p>
```

If the verification method is worth preserving for a future maintainer, put it
in an XML comment immediately before the paragraph it supports, not in the
visible text.

This applies to revision-history `<change>` entries as well. A visible change
entry may say a claim was verified or confirmed, but it should not spell out
the verification mechanism.

For converted historic documents, the `<history>` block should normally record
the original authored releases as well as the later PRM-in-XML conversion.
Keep the original author attribution visible when the source material gives
release dates or version history.

XML comments cannot contain a literal `--` anywhere in their body. Write around
that restriction rather than quoting such text literally.

## Paragraphs and lists

Use `<p>` for paragraphs. Lists must be wrapped in paragraphs when they appear
as section content:

```xml
<p>
  <list type='unordered'>
   <item>First item</item>
   <item>Second item</item>
  </list>
</p>
```

List types are `unordered` or `ordered`.

For complex list item content, including `<userinput>`, wrap the item body in a
`<p>`:

```xml
<item><p>Text with <userinput>command</userinput></p></item>
```

## Code and user input

Use `<userinput>` for text the user types or commands. Use `<systemoutput>` for
system responses.

For extended code examples, use:

```xml
<extended-example type='asm'>
  Title text
  <br/><br/>
  Description
  <br/><br/>
  <userinput>MOV R0, #0</userinput><br/>
  <userinput>SWI "Example"</userinput>
</extended-example>
```

Valid types include: `shell`, `asm`, `c`, `basic`, `pseudo`, `format`,
`unknown`.

When a chapter has more than one worked example, prefer this structure:

* add a `<subsection title="...">` for each distinct example
* place one short descriptive `<p>` before the example block
* keep descriptive text outside the `<extended-example>` element
* wrap the `<extended-example>` in its own `<p>` inside that subsection

Do not stack multiple unrelated `<extended-example>` blocks directly under one
`Examples` section when short explanatory subsections would make them clearer.

## Cross-references

For `<reference>` elements that target definitions in the same XML file, the
local `name` is sufficient.

For `<reference>` elements that target another PRM-in-XML document in the same
set, supply `href` pointing at the target document path without the `.xml`
extension. This applies to `type="document"` references and typed references
such as commands when the definition lives in another file.

Examples:

```xml
<reference type="document" href="../part2/08-building-linking-and-outputs"
           name="Building, linking, and outputs"/>
<reference type="command" href="../part4/16-tool-reference-file-and-archive-tools"
           name="riscos-dump"/>
```

## Inline and miscellaneous elements

* `<filename>`: file paths; use `type="riscos"` by default, or `unix`,
  `windows`, or `uri`
* `<sysvar>`: inline system-variable name
* `<menuoption>`: GUI menu items
* `<actionbutton>`: GUI buttons
* `<fixme>`: visible warning marking incomplete content
* `<br/>`: forced line break; use sparingly
* `<image>`: embedded graphics; supported types are `png`, `draw`, and `svg`

```xml
<image src="path/to/img.png" type="png" width="100" height="50"
       caption="Description"/>
```

Use `&hex;` for hexadecimal prefixes to remain platform-neutral; for example
`&hex;8000`.

## Entity references

Use XML entities for special characters:

* `&lt;`
* `&gt;`
* `&amp;`
* `&nbsp;`
* `&times;`
* `&ne;`
* `&le;`
* `&ge;`
* `&micro;`
* `&implies;`
* `&ellipsis;`
* `&lsl;`
* `&lsr;`
* `&asr;`

Do not double-encode entities. Use `&lt;`, not `&amp;lt;`.
