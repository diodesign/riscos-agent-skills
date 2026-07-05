# Claiming vectors

Vector claims are usually done in the module initialisation code. They must be released on module finalisation.

## Example ReadLineV vector claim

In these examples the vector example is `ReadLineV`.

In the Module initialisation function add a call to the vector claims, like this:

```c
_kernel_oserror *err;
err = vector_claims(pw);
if (err)
    goto failed;
```

In the Module finalisation function release the vector claims, like this:

```c
vector_releases(pw);
```

All vector management should be performed in the C file `c/vector`.

Vector numbers are defined in the include file `riscos/Vectors.h`.

Implement the claims in the `vector_claims` function, and the releases in `vector_releases` with code like this:

```c
#include "riscos/Vectors.h"

_kernel_oserror *vector_claims(void *pw)
{
    _kernel_oserror *err;

    err = os_claim(ReadLineV, ReadLineV_Entry, pw);
    return err;
}
_kernel_oserror *vector_releases(void *pw)
{
    _kernel_oserror *err;
    err = os_release(ReadLineV, ReadLineV_Entry, pw);
    return err;
}
```

### Claim/Release functions

The `os_claim` and `os_release` functions should be defined in the `c/os` file, like this:

```c
#include "swis.h"

_kernel_oserror *os_claim(int vector, void (*func)(void), void *pw)
{
    _kernel_oserror *err;
    err = _swix(OS_Claim, _INR(0,2),
                          vector, func, pw);
    return err;
}

_kernel_oserror *os_release(int vector, void (*func)(void), void *pw)
{
    _kernel_oserror *err;
    err = _swix(OS_Release, _INR(0,2),
                           vector, func, pw);
    return err;
}
```

### CMHG vector-handlers

Update the CMHG header file to add a `vector-handler` entry:

```
vector-handlers: ReadLineV_Entry/ReadLineV_Handler(error-capable:)
```

The handler for the vector should be implemented in a separate file, and has a prototype that looks like this:

```
int ReadLineV_Handler(_kernel_swi_regs *regs, void *pw)
{
    /* Decode registers into typed values, validate and call implementation function */
    return VECTOR_PASSON;
}
```

Watch out for recursion. For example, using `OS_Write*` or `printf` within `WrchV` will create a recursive loop.
