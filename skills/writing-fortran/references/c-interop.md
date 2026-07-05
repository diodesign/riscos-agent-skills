# C and Fortran Interworking

Use `iso_c_binding` for all interfaces that cross between C and Fortran.

## Calling Fortran from C

Fortran routine:

```fortran
function fortran_letter_count(text, multiplier) result(total) bind(C, name="fortran_letter_count")
  use, intrinsic :: iso_c_binding
  implicit none

  character(kind=c_char), dimension(*) :: text
  integer(c_int), value :: multiplier
  integer(c_int) :: total

  integer(c_int) :: letters
  integer :: pos

  letters = 0
  pos = 1
  do while (text(pos) /= c_null_char)
    if (((text(pos) >= 'A') .and. (text(pos) <= 'Z')) .or. &
        ((text(pos) >= 'a') .and. (text(pos) <= 'z'))) then
      letters = letters + 1
    end if
    pos = pos + 1
  end do

  total = letters * multiplier
end function fortran_letter_count
```

C declaration:

```c
extern int fortran_letter_count(const char *text, int multiplier);
```

Use `bind(C, name="...")` so C can use a stable symbol name.

Use `value` in Fortran for scalar arguments that C passes by value. Without
`value`, Fortran expects a pointer.

## Calling C from Fortran

C function:

```c
int c_scale(int value, int multiplier)
{
    return value * multiplier;
}
```

Fortran interface:

```fortran
interface
  function c_scale(value, multiplier) result(total) bind(C, name="c_scale")
    import :: c_int
    integer(c_int), value :: value
    integer(c_int), value :: multiplier
    integer(c_int) :: total
  end function c_scale
end interface
```

## Type Mappings

Use these common mappings:

```text
C int       -> integer(c_int)
C char *    -> character(kind=c_char), dimension(*)
C void *    -> type(c_ptr)
C intptr_t  -> integer(c_intptr_t)
```

## Strings

C strings are nul-terminated:

```fortran
pos = 1
do while (text(pos) /= c_null_char)
  pos = pos + 1
end do
```

When passing a Fortran string literal to C, append `c_null_char`:

```fortran
call c_report("hello" // c_null_char)
```

RISC OS control-terminated strings end at the first byte below 32:

```fortran
pos = 1
do while (iachar(text(pos)) >= 32)
  pos = pos + 1
end do
```

Use the control-terminated form for RISC OS strings unless the interface says
the string is nul-terminated.

## `_kernel_swi_regs`

In the 64-bit RISC OS export, `_kernel_swi_regs` is:

```c
typedef struct _kernel_swi_regs {
    int32_t r[10];
} _kernel_swi_regs;
```

C register `r[0]` is Fortran `regs(1)`, `r[1]` is `regs(2)`, and so on.

C caller:

```c
#include <stdint.h>
#include "kernel.h"

extern void fortran_swi_count_letters(_kernel_swi_regs *regs);

regs.r[0] = (int32_t) (uintptr_t) text;
fortran_swi_count_letters(&regs);
```

Fortran callee:

```fortran
subroutine fortran_swi_count_letters(regs) bind(C, name="fortran_swi_count_letters")
  use, intrinsic :: iso_c_binding
  implicit none

  integer(c_int), dimension(*) :: regs

  type(c_ptr) :: text_ptr
  character(kind=c_char), pointer :: text(:)
  integer(c_intptr_t) :: address
  integer(c_int) :: letters
  integer :: pos

  address = int(regs(1), c_intptr_t)
  text_ptr = transfer(address, text_ptr)
  call c_f_pointer(text_ptr, text, [huge(pos)])

  letters = 0
  pos = 1
  do while (iachar(text(pos)) >= 32)
    if (((text(pos) >= 'A') .and. (text(pos) <= 'Z')) .or. &
        ((text(pos) >= 'a') .and. (text(pos) <= 'z'))) then
      letters = letters + 1
    end if
    pos = pos + 1
  end do

  regs(1) = letters
end subroutine fortran_swi_count_letters
```

Updating `regs(1)` updates `regs.r[0]` in C.

The register fields are 32-bit. This is suitable for RISC OS addresses in this
environment, but do not treat `_kernel_swi_regs` as a general host pointer
container outside the RISC OS ABI.
