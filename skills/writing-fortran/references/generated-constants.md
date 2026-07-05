# Generated Constants

Fortran has modules rather than C-style headers. Generated constants should
usually be emitted as a module:

```fortran
module riscos_wimpspace
  use, intrinsic :: iso_fortran_env, only : int64
  implicit none
  public

  integer(int64), parameter :: Null_Reason = int(z'0', int64)
end module riscos_wimpspace
```

Use it with:

```fortran
use riscos_wimpspace
```

Fortran module names are flat. There is no path syntax equivalent to:

```c
#include "riscos/WimpSpace.h"
```

Prefer namespaced module names such as:

```fortran
module riscos_wimpspace
```

Use `integer(int64), parameter` for generated RISC OS constants so values such
as `&80000000` can be represented without overflowing a default signed
integer.

Convert hex values to BOZ form:

```fortran
integer(int64), parameter :: wf_newformat = int(z'80000000', int64)
```

String constants can be generated as:

```fortran
character(*), parameter :: ErrorString_Demo = "Demo error"
```

When generating labels, ensure they are valid Fortran identifiers:

* Replace non-alphanumeric characters with `_`.
* Prefix labels that do not begin with a letter.
* Preserve names where possible so they remain recognisable from the RISC OS
  header.
