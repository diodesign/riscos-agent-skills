# DCI4 statistics reference

This reference covers the general DCI4 statistics interface for RISC OS.
Use it for both supplier and gatherer work.

## Primary specification

Read the formal specification first:

* https://gerph.github.io/riscos-prm-dci4/prm/html/networking/dci4/dcistatistics.html

## Core model

The interface has two roles:

* supplier: software that owns and exports statistics
* gatherer: software that enumerates suppliers and presents or consumes the
  statistics

The protocol has two phases:

1. enumerate suppliers through `Service_StatisticEnumerate`
2. use each supplier's SWI to describe statistics with `SA_DESCRIBE` and read
   their values with `SA_READ`

The interface is polled, not event driven, and is explicitly not re-entrant.
Use it from callbacks or user mode code rather than assuming arbitrary
re-entrancy.

## Supplier enumeration

Enumeration is performed with `Service_StatisticEnumerate` (`&A1`).

Each supplier allocates a `dci4_spctl` block in the RMA, fills it in, links it
to the list headed by `R0`, and returns the new head pointer. The service
must not be claimed.

Important `dci4_spctl` fields:

* `next`: linked-list pointer
* `i_version`: DCI statistics interface version implemented by the supplier
* `features`: must currently be 0
* `swinumber`: supplier SWI used for later `SA_DESCRIBE` and `SA_READ` calls
* `max_stat`: highest statistic number, inclusive
* `type`: supplier class such as `SPT_GENERAL_SUPPLIER`,
  `SPT_NETWORK_PROTOCOL`, or `SPT_NETWORK_DRIVER`
* `s_version`: supplier module version
* `module`: module title string
* `title`: short user-facing title
* `description`: longer user-facing description
* `reset[8]`: unique per initialisation, so gatherers can detect supplier
  restart

The gatherer is expected to free the RMA blocks after use.

Do not cache the supplier SWI number across separate enumerations. The
specification explicitly allows dynamic SWI assignment, especially for modules
that expose multiple effective suppliers.

## Supplier SWI contract

After enumeration, all further interaction uses the supplier's SWI:

* `R0 = SA_DESCRIBE (0)` or `SA_READ (1)`
* `R1 = first statistic number`, inclusive
* `R2 = last statistic number`, inclusive
* `R3 = output buffer pointer`
* `R4 = output buffer size in bytes`
* `R5 = number of statistics processed` on exit
* `R6 = number of bytes written` on exit

`R0` to `R4` are preserved. The buffer must be word aligned.

The SWI may return only a prefix of the requested range if the buffer is too
small. In that case `R5` and `R6` tell the gatherer how much was actually
processed.

## Descriptions before values

A gatherer should describe statistics before reading them.

`SA_DESCRIBE` returns one fixed-size `dci4_stdesc` per statistic:

* `type`: `ST_...`
* `format`: `SxF_...`
* `presentation`: `SxP_...`
* `size`: bytes reserved for the value on `SA_READ`; always a multiple of 4
* `volatility`: `SV_STATIC`, `SV_VARIABLE`, or `SV_VOLATILE`
* `name`: static string pointer
* `name_tag`: currently must be 0
* `spare`: must be 0

`ST_UNUSED` is special:

* it reserves a statistic number
* it occupies zero bytes when read
* only the type and size fields are meaningful
* gatherers should skip it when presenting results

## Types, formats, and presentation

The specification defines these main value types:

* `ST_BOOLEAN`
* `ST_STRING`
* `ST_INTEGER8`
* `ST_INTEGER16`
* `ST_INTEGER32`
* `ST_INTEGER64`
* `ST_ADDRESS`
* `ST_TIME`

Important format and presentation families:

* booleans: `SBF_NORMAL` or `SBF_INVERTED`, with presentations such as
  `SBP_ON_OFF` and `SBP_YES_NO`
* strings: `SSF_ZEROTERM` and usually `SSP_LITERAL`
* integers: `SIF_UNSIGNED`, optional `SIF_BIGENDIAN`, with presentations such
  as `SIP_HEXADECIMAL`, `SIP_DECIMAL`, and `SIP_DOTTED`
* addresses and times have their own format and presentation enums in the
  spec

When reviewing code, check that the `size` field matches the actual layout the
supplier writes during `SA_READ`, and that string maximum sizes are honest.

## Atomicity requirements

A supplier must perform each read operation atomically for the requested
range. The goal is consistency across related statistics within a single call.

The spec recommends avoiding long interrupt-disabled regions. The suggested
pattern is:

* keep accumulated totals in one buffer
* keep live deltas in another buffer
* atomically swap the live and merge pointers
* merge outside the critical section
* clear the reused delta buffer afterwards

This is especially relevant for drivers or protocol modules whose counters may
change in interrupt context.

## Volatility guidance

Volatility is part of the contract with the gatherer:

* `SV_STATIC`: constant for the supplier invocation
* `SV_VARIABLE`: unlikely to change in about 5 minutes
* `SV_VOLATILE`: may change rapidly

Suppliers should usually group statistics of similar volatility together so a
gatherer can choose sane refresh behaviour.

## Dynamic suppliers

One module may expose multiple effective suppliers. For example, a network
driver controlling multiple interfaces might export one overall supplier and
one per interface.

In that case:

* each effective supplier needs its own SWI number
* enumeration must describe each one separately
* gatherers must rely on fresh enumeration rather than cached SWI numbers

## Gatherer workflow

For a gatherer, the normal sequence is:

1. issue `Service_StatisticEnumerate`
2. walk the returned `dci4_spctl` list
3. for each supplier, call the SWI with `SA_DESCRIBE`
4. size the read buffer from the returned `dci4_stdesc` entries
5. call the SWI again with `SA_READ`
6. interpret the values using the previously returned descriptions
7. free the enumeration structures from the RMA

If the supplier only partially satisfies a request because the buffer is too
small, continue from the next statistic number.

## Simple supplier example

A small supplier might expose these statistics:

* 0: module title as `ST_STRING`, `SSF_ZEROTERM`, `SSP_LITERAL`,
  `SV_STATIC`
* 1: enabled flag as `ST_BOOLEAN`, `SBF_NORMAL`, `SBP_ON_OFF`,
  `SV_VARIABLE`
* 2: packets sent as `ST_INTEGER32`, `SIF_UNSIGNED`, `SIP_DECIMAL`,
  `SV_VOLATILE`
* 3: packets received as `ST_INTEGER32`, `SIF_UNSIGNED`, `SIP_DECIMAL`,
  `SV_VOLATILE`

In `SA_DESCRIBE`, the supplier would return one `dci4_stdesc` for each of
those statistic numbers, with sizes matching the values written later by
`SA_READ`.

In `SA_READ`, it would write:

* a zero-terminated string buffer for statistic 0
* a 32-bit word for statistic 1
* a 32-bit word for statistic 2
* a 32-bit word for statistic 3

If the caller asked for statistics 0 to 3 but the output buffer only had
enough space for the first two, the supplier would stop after statistic 1 and
report the processed count and written size through `R5` and `R6`.

## Common review points

When reviewing a DCI4 statistics implementation, check for these issues:

* enumeration block is not allocated from the RMA
* `features` is non-zero without a defined feature contract
* `name`, `module`, `title`, or `description` point to transient storage
* `reset` is not unique per initialisation
* `size` is not a multiple of 4
* `SA_READ` writes a different layout from what `SA_DESCRIBE` promises
* `name_tag` or `spare` are not zero
* `ST_UNUSED` slots are treated like ordinary statistics
* gatherer caches SWI numbers across separate enumeration passes
* read path is not atomic for logically related counters

## Output style

When answering with this reference:

* state whether you are describing supplier behaviour or gatherer behaviour
* include the exact enumeration/SWI sequence when teaching the interface
* call out whether a detail comes from the generic DCI4 spec or from a local
  repository example
* use small generic examples, and do not imply that one supplier's choices are
  mandatory for all suppliers
