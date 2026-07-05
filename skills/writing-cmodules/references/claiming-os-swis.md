# Claiming OS SWIs In A Module

This note describes the pattern for a RISC OS module which:

- provides its own module SWI, and
- optionally claims an existing `OS_*` SWI and routes it to the same implementation.

The common case is that the module has one internal handler, and two conditional front-ends:

- `MODULE_SWIS`: export a module SWI such as `Heap_Heap`
- `OS_SWIS`: claim an OS SWI such as `OS_Heap`

This is the pattern used in this repository for the Heap module, and is similar to the example in `examples/systemvars`.

## Overview

The clean structure is:

1. Put the real implementation behind normal C functions that do not depend on CMHG veneers.
2. Expose a module SWI handler when `MODULE_SWIS` is enabled.
3. Expose a generic veneer handler for the claimed OS SWI when `OS_SWIS` is enabled.
4. Claim or release the OS SWI from `Mod_Init()` and `Mod_Final()`.

That gives one code path for behaviour, while keeping the public interfaces separate.

## File Layout

Typical files:

- `cmhg/modhead`
- `c/module`
- `c/osswis`
- `h/osswis`
- any implementation files used by the handler

The `c/osswis` and `h/osswis` pair are a small reusable helper around `OS_ClaimOSSWI`.

## CMHG Pattern

In `cmhg/modhead`, use conditional blocks so the module SWI and claimed OS SWI can be enabled independently.

Example:

```cmhg
#ifdef MODULE_SWIS
swi-chunk-base-number: &C4A80
#endif

#ifdef MODULE_SWIS
swi-decoding-table: Heap \
                        Heap/SWI_Heap
#endif

#ifdef OS_SWIS
generic-veneers: \
        Entry_Heap/OSSWI_Heap
#endif
```

Notes:

- `swi-decoding-table` exports the module SWI name, for example `Heap_Heap`.
- `generic-veneers` creates an entry symbol such as `Entry_Heap`, which is the function pointer passed to `OS_ClaimOSSWI`.
- The veneer handler such as `OSSWI_Heap()` must take:

```c
_kernel_oserror *Handler(_kernel_swi_regs *r, void *pw)
```

## Makefile Pattern

Enable the two interfaces through options in `Makefile,fe1` or `MakefileMod,fe1`:

```make
OPTS       =
OPTS      += +MODULE_SWIS
OPTS      += +OS_SWIS
```

Include the OSSWI helper objects if the module claims OS SWIs:

```make
OBJS       = o.modhead \
             o.osswis \
             o.module
```

If the module uses extra implementation files, include them as normal.

## OSSWI Helper

A minimal helper is enough. In `h/osswis`:

```c
typedef void (*generic_veneer)(void);

_kernel_oserror *osswi_claim(bool claim, int32_t swi, generic_veneer func, void *pw);
```

In `c/osswis`:

```c
#define ClaimOSSWI_Claim   (0)
#define ClaimOSSWI_Release (1)

_kernel_oserror *osswi_claim(bool claim, int32_t swi, generic_veneer func, void *pw)
{
    return _swix(OS_ClaimOSSWI, _INR(0, 3),
                 claim ? ClaimOSSWI_Claim : ClaimOSSWI_Release,
                 swi,
                 func,
                 pw);
}
```

`OS_ClaimOSSWI` register contract:

- `R0 = 0` claims, `R0 = 1` releases.
- `R1 = OS SWI number` to claim or release.
- `R2 = CMHG-generated generic veneer entry`, not the C handler.
- `R3 = module private word`.

This keeps the claim/release code out of the main module logic.

## C Module Pattern

The usual structure in `c/module` is:

1. one shared SWI implementation function
2. one OSSWI veneer handler that forwards into it
3. one registration helper for claim/release
4. init/final hooks that call the registration helper

### Shared SWI Implementation

The module SWI handler created by CMHG has the normal signature:

```c
_kernel_oserror *SWI_Heap(int number, _kernel_swi_regs *r, void *pw)
```

This function should:

- validate the SWI number within the module chunk
- decode registers into typed values
- call the real implementation
- place results back into `r`
- return `error_BAD_SWI` for unknown module SWIs

If there is only one exported SWI in the chunk, it is common to reject any `number != 0`.

### OSSWI Veneer Handler

The claimed OS SWI veneer handler should be a thin wrapper:

```c
_kernel_oserror *OSSWI_Heap(_kernel_swi_regs *r, void *pw)
{
    return SWI_Heap(0, r, pw);
}
```

This keeps the OS SWI behaviour identical to the module SWI behaviour.

## Claim And Release Pattern

Track which SWIs were successfully claimed so finalisation can safely release only those SWIs.

Example pattern:

```c
static uint32_t registered;

static _kernel_oserror *register_osswis(void *pw, bool reg)
{
    _kernel_oserror *error;
    uint32_t bit;

    bit = 1u;

    if (reg)
    {
        error = osswi_claim(true, OS_Heap, Entry_Heap, pw);
        if (error == NULL)
        {
            registered |= bit;
        }
        return error;
    }

    if ((registered & bit) != 0)
    {
        (void)osswi_claim(false, OS_Heap, Entry_Heap, pw);
        registered &= ~bit;
    }
    return NULL;
}
```

Use the generated veneer entry symbol from CMHG, not the C handler name:

- correct: `Entry_Heap`
- wrong: `OSSWI_Heap`

`Entry_Heap` is the SVC-mode veneer entry point.

## Initialisation And Finalisation

Claim SWIs during module initialisation:

```c
_kernel_oserror *Mod_Init(const char *tail, int podule_base, void *pw)
{
    _kernel_oserror *error;

    (void)tail;
    (void)podule_base;

    error = register_osswis(pw, true);
    if (error != NULL)
    {
        return error;
    }

    return NULL;
}
```

Release SWIs during finalisation:

```c
_kernel_oserror *Mod_Final(int fatal, int podule_base, void *pw)
{
    (void)fatal;
    (void)podule_base;

    (void)register_osswis(pw, false);
    return NULL;
}
```

If claiming fails during `Mod_Init()`, return the error immediately. Do not leave the module half-initialised.

## Why Use Paired Conditional Blocks

Using paired `MODULE_SWIS` and `OS_SWIS` conditionals is useful because it lets you build:

- a module that exports only its own SWI
- a module that claims only the OS SWI
- a module that supports both

This is helpful for:

- testing
- incremental bring-up
- avoiding accidental export of private module SWIs
- separating compatibility interfaces from native module interfaces

The pair of blocks should usually exist in both:

- `cmhg/modhead`
- `c/module`

That keeps the generated entry points and the C code in sync.

## Error Handling

For SWI handlers:

- return `NULL` on success
- return a `_kernel_oserror *` on failure
- return `error_BAD_SWI` for unknown module SWIs

If your implementation code uses a private error type, convert it at the module boundary into `_kernel_oserror`.

For claimed OS SWIs, the veneer handler should return the same error that the module SWI would return.

## Practical Rules

- Keep one behavioural implementation path; do not duplicate OS SWI logic and module SWI logic.
- Put OS SWI claiming behind `OS_SWIS`.
- Put exported module SWIs behind `MODULE_SWIS`.
- Use CMHG generic veneers for claimed OS SWIs.
- Pass the CMHG-generated `Entry_*` symbol to `OS_ClaimOSSWI`.
- Track successful claims so release is safe.
- Release claimed SWIs in `Mod_Final()`.
- Keep the SWI register decoding in `c/module`; pass typed values into lower-level code.

## Build And Test

For this repository, the module build is:

```sh
riscos-amu -f MakefileMod,fe1
```

If you have a BASIC or command-line smoke test, load the module and exercise both interfaces:

```sh
riscos-build-run rm32 tests --command "RMLoad rm32.Heap" --command "Run tests.HeapModuleSmoke"
```

That verifies:

- the module loads
- the OS SWI claim succeeded
- the exported module SWI works
- both paths reach the same implementation

## Common Mistakes

- Passing `OSSWI_*` instead of `Entry_*` to `OS_ClaimOSSWI`
- Forgetting to add the `generic-veneers` declaration in `cmhg/modhead`
- Claiming SWIs in `Mod_Init()` but never releasing them in `Mod_Final()`
- Duplicating logic between the module SWI and the claimed OS SWI
- Returning a private error structure instead of `_kernel_oserror`
- Letting `MODULE_SWIS` and `OS_SWIS` conditionals drift out of sync between CMHG and C

## Summary

The recommended pattern is:

1. implement the operation once in normal C
2. expose it as a module SWI behind `MODULE_SWIS`
3. expose it as a claimed OS SWI behind `OS_SWIS`
4. use a CMHG veneer entry for `OS_ClaimOSSWI`
5. register in `Mod_Init()` and deregister in `Mod_Final()`

That gives a maintainable module interface with minimal duplicated code and predictable behaviour across both SWI entry paths.
