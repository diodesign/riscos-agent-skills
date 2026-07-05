# Testing C modules

## Loading and unloading

Typical commands:

* `*RMLoad rm32.Module`
* `*RMKill Module`

## BASIC Testing

Use BBC BASIC `SYS` calls to exercise SWIs directly.

Example:

```basic
REM Standard SWI (error raises BASIC error)
SYS "Timer_ReturnNumber", 0 TO ,,,num_timers%

REM X-SWI (check flags for errors)
SYS "XTimer_Claim", 0, 0, 1000, 0 TO r0%,r1%,rate%;flags%
IF flags% AND 1 THEN
  error_num% = r0%!0
ENDIF
```

## Build Testing

Typical smoke test:

```bash
riscos-build-run rm32 test_MODULE,fd1 \
  --command "*RMLoad rm32.MODULE" \
  --command "Run test_MODULE"
```

The `--command` arguments are RISC OS commands, not BASIC statements.

## Leaf-name collision pitfall

`riscos-build-run` copies listed host files into a flat guest environment by leaf name.

Do not give the BASIC test file the same leaf name as the module. For example, `tests/inversetable,fd1` can collide with `rm32/InverseTable,ffa` and break `RMLoad`.

Prefer distinct names such as `tests/test-it,fd1`.

## Repeatable AMU test target

```makefile
.PHONY: test
test: ram
           riscos-build-run rm32/Module,ffa tests/test-module,fd1 --command "RMLoad Module" --command "Run test-module"
```

## 64-bit note

64-bit modules can be loaded for smoke testing, but BBC BASIC is not available there:

```bash
riscos-amu BUILD64=1
riscos-build-run --arch aarch64 rm64 --command "*RMLoad rm64.<module>"
```
