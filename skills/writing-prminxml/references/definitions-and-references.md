# Definitions and references

## SWI definitions

### Basic structure

SWI definitions require the `name` attribute and may also include `number`:

```xml
<swi-definition name='Example_SWI' number='12345'>
  <entry>...</entry>
  <exit>...</exit>
  <use><p>Description</p></use>
  <example><p><userinput>SWI "Example"</userinput></p></example>
  <related>
   <reference type='sysvar' name='Example$Var'/>
  </related>
</swi-definition>
```

SWI numbers are hexadecimal but must not include `&` or `0x` prefixes.

### Per-reason SWI definitions

SWIs that use a reason code in a register may be documented as separate
`swi-definition` entries, one per reason code, using `reason` and `reasonname`:

```xml
<swi-definition name='Example_SWI' number='5AC01'
                reason='0' reasonname='Create'
                description='Creates a new object'>
  <entry>
   <register-use number='0'>Reason code</register-use>
  </entry>
</swi-definition>
```

The top-level entry with no `reason` attribute acts as the overview entry,
documenting common registers and summarising the reason codes with a
`value-table`.

### Reason-code overview pattern

The recommended pattern is:

1. One top-level `swi-definition` with no `reason` attribute.
2. One `swi-definition` per reason code.

```xml
<swi-definition name='Example_SWI' number='5AC01'
                description='Performs operations on objects'>
  <entry>
   <register-use number='0'>
    <p>Reason code:</p>
    <p>
    <value-table head-number="Reason" head-value="Action">
     <value number="0"><reference type='swi' name='Example_SWI' reason="0" use-description='yes'/></value>
     <value number="1"><reference type='swi' name='Example_SWI' reason="1" use-description='yes'/></value>
    </value-table>
    </p>
   </register-use>
   <register-use number='1'>Handle ID</register-use>
   <register-use number='2-5'>Dependent on reason code</register-use>
  </entry>
</swi-definition>
```

### Register documentation

Use `<register-use>` with a numeric `number` attribute:

```xml
<register-use number='0'>
  Description of R0
</register-use>
```

The attribute value must not include `R`, `X`, or `W`. In visible text within
the element, use the normal register names such as `R0`.

### Referencing a specific reason code

To link directly to a per-reason entry, add `reason='N'` to the `<reference>`:

```xml
<reference type='swi' name='Example_SWI' reason='0'/>
```

Use this in related blocks of per-reason entries to cross-link them.

## Service definitions

Do not include the `Service_` prefix in the `service-definition` `name`
attribute. The stylesheet adds it automatically.

```xml
<service-definition name="ReportError" ...>
```

## Error definitions

* Error numbers should be hexadecimal and include the error base.
* Error names in the documentation should use the module prefix, not `Err_`.
* Error names must not contain spaces.

## Bit fields

For registers containing flags, prefer `<bitfield-table>`:

```xml
<register-use number='0'>
  Flags:
  <bitfield-table>
   <bit number='0-1' name='Mode'>
    <list type='unordered'>
     <item><p>0: Mode A</p></item>
     <item><p>1: Mode B</p></item>
     <item><p>2: Mode C</p></item>
     <item><p>3: Mode D</p></item>
    </list>
   </bit>
   <bit number='2' name='Enable'>
    Enable flag
   </bit>
   <bit number='3-31' state='reserved'>
    Reserved
   </bit>
  </bitfield-table>
</register-use>
```

The `state` attribute may be `reserved`, `content`, `set`, or `clear`.

## System variable definitions

System variables require both `name` and `description` attributes:

```xml
<sysvar-definition name='Example$Var' description='Controls behaviour'>
  <use>
   <p>Detailed description...</p>
  </use>
  <example>
   <p><userinput>Example$Var = value</userinput></p>
  </example>
</sysvar-definition>
```

## VDU definitions

VDU definitions use `<vdu-definition>`.

* The `name` is auto-prefixed with `VDU`.
* The `number` is hexadecimal.
* In PRM-in-XML 1.03, the `<syntax>` block should only document the additional
  parameters following the VDU number.

## Star command definitions

For CLI tools and module star commands, use `<command-definition>`:

```xml
<command-definition name="CommandName" description="One line description">
  <syntax>
    <!-- Syntax elements -->
  </syntax>
  <parameter name="param_name" switch="s" switch-alias="a">
    Description of the parameter.
  </parameter>
  <use>
    <p>Detailed usage information.</p>
  </use>
  <example>
    <command>*CommandName -s value</command>
  </example>
  <related>
    <reference type="command" name="OtherCommand"/>
  </related>
</command-definition>
```

The `*` prefix must be included in the content of `<command>` elements.
`<command>` is only valid inside `<example>` blocks. For inline references to
commands, use `<reference type="command" .../>`.

### Syntax elements

The `<syntax>` block uses:

* `<switch name="n">`
* `<optional>`
* `<alternates>`
* `<userreplace>`
* `<text>`

### Parameters

Use `<parameter>` to define arguments or switches:

* `name`: matches `<userreplace>` or a positional argument
* `switch`: matches `<switch name="...">`
* `switch-alias`: alternate spelling
* `label`: alternate visible label

For switch parameters, do not repeat the rendered switch text in `label` when
`switch` already identifies it. Use `switch-alias` when a parameter has
multiple spellings such as `-h` and `-help`.

## References

Cross-reference other elements using `<reference>`:

```xml
<reference type="service" name="ReportError"/>
<reference type="swi" name="OS_Byte"/>
<reference type="document" href="OtherDoc" name="Other Document"/>
<reference type="link" href="https://example.com" name="Example Site"/>
```

Valid types include: `swi`, `sysvar`, `command`, `vector`, `upcall`,
`service`, `message`, `entry`, `error`, `document`, `chapter`, `section`,
`subsection`, `subsubsection`, `category`, `tboxmethod`, `tboxmessage`.

For `type="document"` references, omit the `.xml` extension in `href`.
Use `href='?'` for documents that do not exist yet if a placeholder link is
still useful.

The stylesheet automatically adds prefixes such as `Service_` or `SWI_` based
on the reference type.

For `type="message"` references and `<message-definition>` names, do not
include the `Message_` prefix in the `name` attribute. The stylesheet adds it
automatically.

Correct:

```xml
<message-definition name="EditReturn" number="45D82" description="...">
  <use><p>...</p></use>
</message-definition>

<reference type="message" name="EditReturn"/>
```

Wrong:

```xml
<message-definition name="Message_EditReturn" number="45D82" description="...">
  <use><p>...</p></use>
</message-definition>
```

### `use-description`

The `use-description='yes'` attribute on a `<reference>` element causes the
target description to be used as the link text. This is especially useful
inside `value-table` entries:

```xml
<value-table head-number="Reason" head-value="Action">
 <value number="0"><reference type='swi' name='Example_SWI' reason="0" use-description='yes'/></value>
 <value number="1"><reference type='swi' name='Example_SWI' reason="1" use-description='yes'/></value>
</value-table>
```
