# Tables, grammar, and troubleshooting

## BNF

For complex syntax definitions, use the BNF namespace
`http://gerph.org/dtd/bnf/100/bnf.dtd`. BNF elements are typically used within
a `<bnf>` block.

### Elements

* `<bnf>`: root element for a BNF grammar
* `<rule-def>`: defines a new rule
* `<rule-use>`: invokes an existing rule
* `<literal>`: a case-insensitive US-ASCII string
* `<character>`: terminal symbol or range
* `<group>`: groups elements for repetition or alternation
* `<comment>`: descriptive text within the BNF block

### Repetition attributes

Available on `<rule-use>`, `<literal>`, `<character>`, and `<group>`:

* `repeat`
* `repeat-min`
* `repeat-max`

Standard upper-case ABNF rules from RFC2234 such as `ALPHA`, `DIGIT`,
`HEXDIG`, `SP`, `WSP`, and `CRLF` are implicitly available.

## Table placement rule

All table elements are only valid as children of `<p>`. They cannot appear
directly as children of `section`, `subsection`, `subsubsection`, or
`category`.

```xml
<p>
<definition-table ...>
  ...
</definition-table>
</p>
```

The same placement rule applies to:

* `definition-table`
* `value-table`
* `offset-table`
* `bitfield-table`
* `message-table`
* `version-table`

## `definition-table` and `definition`

Use `definition-table` for named values such as options, parameters, variables,
or configuration keys where the key is a string rather than a number.

Attributes:

* `definition-table head-name`
* `definition-table head-extra`
* `definition-table head-value`
* `definition name`
* `definition extra`

```xml
<p>
<definition-table head-name="Variable" head-extra="Default" head-value="Description">
 <definition name="OPTIMISE" extra="yes">Optimisation level.</definition>
 <definition name="ASD" extra="(unset)">Set to yes to produce a debug build.</definition>
</definition-table>
</p>
```

`definition` is declared `ANY`, so it may contain rich content, including
nested tables or lists.

## `value-table`

Use `value-table` when keys are numeric values such as reason codes, flag
values, or error numbers.

```xml
<p>
<value-table head-number="Value" head-value="Meaning">
 <value number="0">Success.</value>
 <value number="1">Error occurred.</value>
</value-table>
</p>
```

## `offset-table`

Use `offset-table` to document memory layouts such as control blocks or data
buffers. Offsets are automatically prefixed with `+` in the output.

Attributes:

* `offset-table head-number`
* `offset-table head-name`
* `offset-table head-data-size`
* `offset-table head-value`
* `offset number`
* `offset name`
* `offset data-size`
* `offset state`

```xml
<p>
<offset-table head-number="Offset" head-name="Name" head-data-size="Size" head-value="Contents">
 <offset number="0" name="flags" data-size="4">Flags word</offset>
 <offset number="4" name="length" data-size="4">Length in bytes</offset>
 <offset number="8" name="data" state="content">Variable-length data</offset>
 <offset number="12-15" state="reserved">Reserved; must be zero</offset>
</offset-table>
</p>
```

## `message-table`

Use `message-table` to document Wimp message blocks. Offsets are rendered
relative to `R1+`.

`message` attributes match those of `offset`, but use `offset` instead of
`number`.

```xml
<p>
<message-table>
 <message offset="0" name="size" data-size="4">Total size in bytes</message>
 <message offset="16" name="action" data-size="4">Message action code</message>
 <message offset="24-27" state="reserved">Reserved; must be zero</message>
</message-table>
</p>
```

## `version-table`

Use `version-table` to describe compatibility differences across module or OS
versions.

Useful attributes include:

* `module-name`
* `module-lt`, `module-eq`, `module-ge`
* `riscos-lt`, `riscos-eq`, `riscos-ge`
* `supplier`
* `hardware`
* `architecture`
* `state`

```xml
<p>
<version-table>
 <version module-ge="1.00" module-lt="2.00">Original implementation.</version>
 <version module-ge="2.00">Extended interface added.</version>
 <version riscos-lt="5.00" state="unsupported"/>
</version-table>
</p>
```

## Conversion guidance

When converting another document into PRM-in-XML, the PRM-in-XML file should
become the canonical source rather than a cheat-sheet summary.

When converting structure definitions, prefer `offset-table` as the primary
reference format. If the document uses many specialised terms, introduce a
`Terminology` section.

Structures, value lists, and bitfield tables that are referenced repeatedly are
good candidates for a `category` element plus later `<reference>` links.

## Common errors and fixes

### List not allowed directly in section

If lint reports that section content does not follow the DTD, wrap lists in
`<p>` elements when they appear as direct children of sections or subsections.

### `userinput` not allowed in `item`

Wrap the item body in a paragraph:

```xml
<item><p>Text <userinput>code</userinput></p></item>
```

### Double-encoded entities

Use `&lt;` in XML, not `&amp;lt;`.

For hexadecimal prefixes, use `&hex;` directly in text and attribute values,
not `&amp;hex;`.

### Invalid register prefix

Use `number='0'`, not `number='R0'`, in attributes. Use `R0` only in visible
text.

### SWI number with prefix

Use `number='58B00'`, not `number='&58B00'`.

### Extended example in category

Wrap `<extended-example>` in `<p>` tags inside `category`:

```xml
<category title="YAML structure">
  <p>
    <extended-example type="format">
      content here
    </extended-example>
  </p>
</category>
```

### Message names rendered as `Message_Message_*`

For `<message-definition>` and `type="message"` references, omit the
`Message_` prefix from the `name` attribute. The stylesheet adds that prefix
automatically.

### HTML build output directory missing

If `riscos-prminxml -f html5+xml -O <directory> ...` reports that the output
directory does not exist, create it first with `mkdir -p <directory>`.

## Quick reference

| Element | Use for | Notes |
|---------|---------|-------|
| `<chapter>` | Top-level document | Must have `title` |
| `<section>` | Major divisions | |
| `<subsection>` | Subdivisions | |
| `<subsubsection>` | Further subdivisions | |
| `<category>` | Topic breaks within text | Not a heading level |
| `<p>` | Paragraphs | Required wrapper for lists and tables |
| `<list>` | Bulleted or numbered lists | `unordered` or `ordered` |
| `<extended-example>` | Code blocks | Wrap in `<p>` inside `category` |
| `<userinput>` | Inline code or commands | |
| `<command>` | Star commands in examples | Include `*` prefix |
| `<systemoutput>` | System responses | |
| `<service-definition>` | Service calls handled | Omit `Service_` in `name` |
| `<swi-definition>` | SWIs implemented | Omit `&` in `number` |
| `<reference>` | Cross-references | Use the correct `type` |
| `<fixme>` | Marking incomplete text | Put the deficiency in the element |

Common commands:

* `riscos-prminxml -f skeleton -o doc.xml`
* `riscos-prminxml -f lint doc.xml`
* `riscos-prminxml -f html5+xml -O html doc.xml`
* `host-open html/doc.html`

Related documents:

* `/riscos-resources/Install/Tools/Linux/riscos-prminxml-resources/docs/PRMinXML.txt`
* `/riscos-resources/Install/Tools/Linux/riscos-prminxml-resources/docs/BNF.txt`
* `/riscos-resources/Install/Tools/Linux/riscos-prminxml-resources/docs/HowTo.md`
