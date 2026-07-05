# Building Fortran

## Source Layout

Fortran source files live in `f90/` and do not have a `.f90` suffix in the host
filesystem:

```text
f90/hello
f90/countlib
```

The compiler wrapper accepts RISC OS-style names:

```sh
riscos64-fortran -c -o o.hello f90.hello
```

`f90.hello` maps to host file `f90/hello`.

## Compile and Link

Compile Fortran:

```sh
riscos64-fortran -c -o o.name f90.name
```

Compile C:

```sh
riscos64-cc -c -o o.cname c.cname
```

Link a Fortran program:

```sh
riscos64-link o.name -lgfortran -o name,ff8
```

Link C and Fortran together:

```sh
riscos64-link o.cname o.fname -lgfortran -o name,ff8
```

Run an absolute:

```sh
riscos-build-run --64 name,ff8 --command name
```

Always link with `-lgfortran` when any Fortran object is present.

## Modules

For reusable code, use a module:

```fortran
module countlib
  implicit none

contains

  function count_letters(text) result(total)
    implicit none

    character(len=*), intent(in) :: text
    integer :: total
    integer :: pos

    total = 0
    do pos = 1, len_trim(text)
      if (((text(pos:pos) >= "A") .and. (text(pos:pos) <= "Z")) .or. &
          ((text(pos:pos) >= "a") .and. (text(pos:pos) <= "z"))) then
        total = total + 1
      end if
    end do
  end function count_letters

end module countlib
```

Use it from a main program:

```fortran
program countmain
  use countlib
  implicit none

  print *, count_letters("RISC OS")
end program countmain
```

Compile the module before files that `use` it:

```sh
riscos64-fortran -c -o o.countlib f90.countlib
riscos64-fortran -c -o o.countmain f90.countmain
riscos64-link o.countmain o.countlib -lgfortran -o countmain,ff8
```

The module compile produces both an object file and a compiler-generated
`.mod` interface file. Do not hand-edit `.mod` files.

## Style

Use free-form Fortran 90 or later.

Use `implicit none` everywhere.

Declare variables before executable statements.

Use `intent(in)`, `intent(out)`, and `intent(inout)` for procedure arguments
where practical.

For C-compatible interfaces, prefer `iso_c_binding` types.
