# Pitfalls and Checks

## Build Pitfalls

Always link with `-lgfortran` if any object was produced by
`riscos64-fortran`.

Compile modules before files that `use` them.

Do not edit generated `.mod` files.

Do not read or write files in `.rotransform`; those are generated
implementation details of the wrappers.

The wrapper can accept RISC OS-style names such as `f90.name` and `o.name`.
If a host path behaves unexpectedly, check whether the wrapper is translating
the name.

## Language Pitfalls

Do not omit `implicit none`.

Do not declare variables after executable statements.

Do not use C zero-based array indexing in normal Fortran code. Fortran arrays
normally start at index 1.

Do not write C operators in Fortran:

```text
C &&    -> Fortran .and.
C ||    -> Fortran .or.
C !     -> Fortran .not.
C true  -> Fortran .true.
C false -> Fortran .false.
```

Do not assume Fortran strings are C strings. Add `c_null_char` when passing a
Fortran string to C.

Do not use a nul-terminated loop for RISC OS control-terminated strings.

Do not rely on compiler-generated Fortran symbol names for C interworking.
Use `bind(C, name="...")`.

Do not omit `value` on scalar arguments passed by value from C.

## Review Checklist

Before declaring Fortran work complete:

* Source files are in `f90/` with no `.f90` suffix.
* `implicit none` appears in every program unit.
* Modules are compiled before dependent sources.
* Link commands include `-lgfortran`.
* C interop uses `iso_c_binding`.
* C-visible Fortran routines use `bind(C, name="...")`.
* C strings and RISC OS control-terminated strings are handled distinctly.
* `_kernel_swi_regs` uses `integer(c_int), dimension(*)` on the Fortran side,
  with `regs(1)` for C `r[0]`.
* No trailing whitespace was introduced.
