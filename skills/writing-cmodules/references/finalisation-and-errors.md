# Module finalisation, private word, errors, and time

## Mod_Final Function

The `Mod_Final()` function is called when the module is killed (unloaded). Ensure all resources are cleaned up:

```c
_kernel_oserror *Mod_Final(int fatal, int podule_base, void *pw)
{
    dprintf("Module JUnitXML dying\n");

    /* Finalise the state manager - closes files, frees memory. */
    junit_state_final();

    return NULL;
}
```

Only report errors if shutdown is being prevented, and never leave the module in an inconsistent state. If an error is returned, the finalisation code will be called again and must never crash.

## State Finaliser Pattern

The state finaliser should clean up in reverse order of creation:

```c
int junit_state_final(void)
{
    junit_handle_t *h, *next_h;

    for (h = junit_global.handles; h != NULL; h = next_h) {
        next_h = h->next;
        free_handle(h);
    }

    junit_global.handles = NULL;
    junit_global.next_handle_id = 0;

    return 0;
}
```

Key points:

1. Close open files with `fclose()`.
2. Free all allocated memory.
3. Reset global state to a safe empty state.
4. Keep finalisation safe after partial cleanup.

## Private memory and private word

Memory for the module is managed by standard `malloc`, `free`, `realloc`, and `calloc` calls.

If the user requires code to function on RISC OS 3.1, `realloc` was not functional and must not be used. Modules should not target RISC OS 3.1 unless explicitly directed to do so.

Rules for `pw`:

* The `pw` parameter in init/final/handler is a module-private workspace pointer.
* Pass it to interfaces that require a private word.
* Never dereference it.
* Never overwrite it when using the Shared C Library.

Common failure mode:

* Overwriting the private word destroys the SCL workspace and can cause data aborts in functions such as `fopen` or `printf`.
* Use ordinary C globals for module state instead.

## Error Handling

RISC OS error blocks have a fixed structure:

```c
typedef struct _kernel_oserror_s {
    int errnum;
    char errmess[252];
} _kernel_oserror;
```

Define static error blocks in `cmhg/modhead` with `error-identifiers`:

```cmhg
error-base: &840000

error-identifiers: \
    Err_CreateFailed("Failed to create JUnitXML handle"),
    Err_CreateSuiteFailed("Failed to create test suite"),
    Err_CloseSuiteFailed("Failed to close test suite"),
    Err_BadOp(&12e, "Unknown operation")
```

Use generated error-block pointers directly from `h/modhead`:

```c
if (handle < 0) {
    return Err_CreateFailed;
}
```

When a lower layer returns its own status codes, map them to module-defined error blocks through a conversion function.

If you get undefined symbols such as `__err_Err_NotRegistered` at link time, check that `o.modhead` is present in the `OBJS` list.

## Time Handling

RISC OS time is stored as either a quin or a 5-byte time: a 40-bit little-endian centisecond count since 1900-01-01 00:00:00 UTC.

Useful SWIs:

* `Territory_ConvertDateAndTime`
* `Territory_ConvertTimeToOrdinals`
