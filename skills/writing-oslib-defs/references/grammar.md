# Def file grammar

This summarises the grammar consumed by `riscos-defmod`. It matches the
detailed reference in `prminxml/appendix/a19-defmod-file-format.xml`, with
extra emphasis on points that are easy to get wrong in practice.

## Overall structure

There are seven top-level declaration forms: `TITLE`, `AUTHOR`, `NEEDS`,
`NEEDSATEND`, `CONST`, `TYPE`, and `SWI`. Declarations appear in a single
stream, separated by semicolons. An empty file is valid.

**The semicolon separates declarations; it does not terminate the last one.**
If the final declaration in the file has a trailing semicolon, `defmod`
reports a syntax error at end of file. Omit the semicolon after the last
declaration only.

Identifiers may be up to 255 characters; quoted descriptions may be up to
255 characters. Keywords are matched case-insensitively.

## Metadata and dependencies

| Declaration | Meaning |
|---|---|
| `TITLE id "description"` | Sets the interface title. The identifier is also used as the generated module prefix. The description is optional. |
| `AUTHOR "text"` | Sets the author string embedded in generated files. |
| `NEEDS id, id, ...` | Names interfaces that must be included before the generated declarations. |
| `NEEDSATEND id, id, ...` | Names interfaces that must be included after the generated declarations. |

## Constants

```
CONST ReasonCode = .int: 5 "Reason code for the SWI",
      BufferType = MyType: ExternalValue;
```

The right-hand value may be a literal number or the name of a
previously-declared constant. Forward references are not supported.

## Type system

| Type | Value class | Meaning |
|---|---|---|
| `.int` | register | Signed word-sized integer. |
| `.short` | register | Short integer. |
| `.byte` | register | Unsigned byte-sized scalar. |
| `.char` | register | Character-sized scalar. |
| `.bits` | register | Bit-set or flags word. |
| `.bytes` | register | Byte count or raw size value. |
| `.bool` | register | Boolean value. |
| `.ref type` | register | Reference to another type. |
| `.string` | variable | Pointer to string data. |
| `.asm` | variable | Assembler-defined opaque data. |
| `.data` | variable | Raw opaque data. |
| `.struct ...` | fixed or variable | Structure of named members, optionally with a base type and trailing ellipsis. |
| `.union ...` | variable | Union of named members; members may use `.void`. |
| `[count] type` | fixed | Fixed-length array of a non-variable base type. |
| `TypeName` | resolved | Reference to a previously-declared or externally-provided named type. |

```
TYPE BufferHandle "Opaque handle",
     WindowBlock = .struct (.int: window, .int: icon),
     ByteArray = [16] .byte;
```

### Structured types

Structure members use `type : name`. Unions use `toid : name`, where `toid`
is a normal type or `.void`.

A structure may include an optional base type immediately after `.struct`
and before the opening parenthesis:

```
TYPE Derived = .struct :BaseType (.int: extra);
```

An ellipsis inside a structure marks it as variable-sized:

```
TYPE Variable = .struct (.int: length, ...);
```

Arrays cannot use a variable-sized base type.

## SWI declarations

```
SWI Example_Call = (NUMBER &12345 "Example call",
                    ENTRY (R0 = .int: value, R1 # ReasonCode),
                    EXIT (R0! = .int: result, R2 ?))
```

The definition begins with `NUMBER` followed by a numeric literal and an
optional description. The remainder may contain `ENTRY (...)`, `EXIT (...)`,
or `ABSENT` (a described but non-callable SWI; no veneer is generated).
Entry and exit clauses, if both present, are comma-separated.

### Entry conditions

| Form | Meaning |
|---|---|
| `Rn = type:name` | Register contains a value of the given type. |
| `Rn -> type:name` | Register contains a reference to the given type. |
| `Rn # value` | Register is loaded with the constant value before the call. |
| `Rn \| type:name` | Register is bitwise ORed with the argument before the call. |
| `Rn + type:name` | Register is added to the argument before the call. |
| `Rn ^ type:name` | Register is exclusive-ORed with the argument before the call. |
| `FLAGS` | Input PSR flags are significant. |

### Exit conditions

| Form | Meaning |
|---|---|
| `Rn = type:name` | Register returns a value of the given type. |
| `Rn! = type:name` | Register returns an output parameter and is also the function result. |
| `Rn -> type:name` | Register returns a reference result. |
| `Rn! -> type:name` | Register returns a reference result and is also the function result. |
| `Rn ?` | Register is corrupted by the SWI or veneer. |
| `Rn !` | Register is the primary result value. |
| `FLAGS` | Output PSR flags are returned. |
| `FLAGS !` | Output PSR flags are returned and are also the primary result. |

The exclamation mark has two roles: inside a typed exit condition it marks
the returned value; as a standalone suffix it selects a register or the
flags word as the primary result.

### Starred descriptions

A quoted description immediately after `NUMBER` marks the SWI as having a
named numeric constant in generated headers. A bare `*` requests the same
treatment without adding descriptive text. The same applies to
`Rn # value "description"` or `Rn # value *` on entry conditions. These are
what the C and assembler generators use to emit manifest constants for SWI
numbers and reason codes.

## Literals

Identifiers begin with a letter and may contain letters, digits, and
underscores.

| Form | Meaning |
|---|---|
| `123` | Decimal integer. |
| `-123` | Negative decimal integer. |
| `0x1234` | Hexadecimal integer. |
| `&1234` | Alternative hexadecimal form. |
| `0b1010` | Binary integer. |
| `%1010` | Alternative binary form. |
| `'AB'` | Packed character constant, up to four characters. |

Quoted descriptions support escaped `'`, `"`, `\`, `\n`, `\0`, and two-digit
hexadecimal escapes `\xHH`.
