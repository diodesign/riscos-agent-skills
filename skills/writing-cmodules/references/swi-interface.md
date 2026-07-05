# SWI interface details

## SWI Decoding Table

The `swi-decoding-table` in `cmhg/modhead` maps SWI names to handler functions.

Format:

```cmhg
swi-decoding-table: <prefix> <name1>/<handler1> <name2>/<handler2> ...
```

Example:

```cmhg
swi-decoding-table: JUnitXML Create/SWI_Create TestSuite/SWI_TestSuite TestCase/SWI_TestCase Close/SWI_Close
```

This creates:

* `JUnitXML_Create` -> `SWI_Create()`
* `JUnitXML_TestSuite` -> `SWI_TestSuite()`
* `JUnitXML_TestCase` -> `SWI_TestCase()`
* `JUnitXML_Close` -> `SWI_Close()`

## Centralised handler

When using a centralised `Mod_SWI` dispatcher, list SWIs without the `/handler` suffix so CMHG routes all calls to the main dispatcher.

Avoid this pattern unless all SWIs share a common register contract.

## Handling unknown SWIs

If `Mod_SWI()` receives a SWI number it does not recognise, return `error_BAD_SWI` from the generated CMHG header.

## Common mistake: name duplication

Wrong:

```cmhg
swi-decoding-table: JUnitXML JUnitXML_Create/SWI_Create
```

Correct:

```cmhg
swi-decoding-table: JUnitXML Create/SWI_Create
```

## Handler signature

All SWI handlers take this form:

```c
_kernel_oserror *SWI_Handler(int swi, _kernel_swi_regs *r, void *pw)
{
    ...
}
```

Decode parameters from registers into typed values before calling deeper implementation functions.

## X-SWI Convention

Standard convention:

* Standard SWI: raises an error.
* XSWI: sets V on error and returns an error block pointer in `R0`.

Within modules, prefer calling SWIs with the X-prefix and handling the returned error explicitly.

## SWI Names

* SWI names follow `<Module>_<Function>` in PascalCase.
* X-prefixed forms are handled automatically by the kernel and do not need separate registration.
* Common SWI names are declared in `swis.h`.
