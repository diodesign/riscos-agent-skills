# Perl 5.001 checklist for RISC OS

Use this checklist when a Perl script must run under the RISC OS interpreter reported by:

```text
riscos-build-run --command 'perl -v'
```

At the time this skill was created, that reports Perl `5.001`.

## Prefer these forms

* `open(IN, "< file")` not 3-argument `open`
* `open(OUT, "> file")` followed by `binmode(OUT)` for binary output
* `open(IN, "< file")` followed by `binmode(IN)` for binary input
* `while (<IN>)` and `close(IN)` using classic filehandles
* `mkdir $dir, 0755`
* String repetition with `x`, for example `"\x00" x 12`

## Avoid these forms

* `open($fh, ...)`
* `open(..., ..., ...)`
* `open(..., '<:raw', ...)` or `open(..., '>:raw', ...)`
* Assuming modern parser features, modules, or regex support are available

## Known failure patterns

### Binary I/O

The older interpreter may mishandle or reject modern layer syntax.
For binary templates and sprite files:

1. Open with classic 2-argument `open`.
2. Call `binmode`.
3. Read the whole file with `local $/;`.

### Filehandles

Lexical filehandles are a common portability trap.
If a script must run on RISC OS Perl, use bareword handles consistently.

### String repetition

Use `x` for repeating strings.
Do not use `*` when you intend repeated bytes:

```perl
("\x00" x 12)   # correct
("\x00" * 12)   # numeric multiplication, not string repetition
```

### Modern-host false confidence

A script can pass on Linux or macOS Perl and still fail on RISC OS.
Always run the RISC OS path before concluding that a Perl change is safe.

### Build-run concurrency

When validating with `riscos-build-run`, keep concurrency low.
Do not start more than 2 concurrent `riscos-build-run` jobs from one investigation, because higher concurrency can overload the server and confuse tool failures with script failures.

## Suggested review pass

Search the edited script for these patterns:

* `open(`
* `:raw`
* `my $fh`
* `mkdir `
* regex features that might depend on newer Perl behaviour

If you find a compatibility issue, prefer the simpler older form unless there is a strong reason not to.
