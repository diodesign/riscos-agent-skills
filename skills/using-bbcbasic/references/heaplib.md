# HeapLib dynamic allocation pattern

`HeapLib` is a BBC BASIC library which wraps `OS_Heap` and `Wimp_SlotSize` to provide C-like dynamic allocation for BASIC programs. It is useful when `DIM` is too static because blocks need to be claimed, resized, or freed during the life of the program.

This pattern is most useful for desktop applications, long-running tools, or programs which manage many buffers, records, or strings. Small throwaway programs usually do not need it.

## Basic usage

Load the library and initialise it once near startup:

```basic
LIBRARY "<HeapLibrary$File>"
PROCinitheap
```

HeapLib is designed to be loaded after WimpLib so that its `FNclaim` and `PROCrelease` replace the usual WimpLib RMA claim/release calls with heap-backed ones.

`PROCinitheap`:

* Reads the page size with `OS_ReadMemMapInfo`.
* Starts the heap at `HIMEM`.
* Grows the Wimp slot by one page.
* Initialises an `OS_Heap` area.
* Creates a relocatable-block table headed by the marker `&434F4C52`.
* Starts the relocatable-block table with two handles and extends it automatically as needed.

The minimum heap size is one memory page.

## Allocation model

### Ordinary heap blocks

Use `FNclaim(size%)` to claim a fixed block:

```basic
buffer% = FNclaim(1024)
IF buffer% = -1 THEN ERROR 0, "Out of memory"
```

Release it with:

```basic
PROCrelease(buffer%)
```

`PROCrelease` writes `-1` back to the caller's variable, so passing the pointer by `RETURN` avoids stale pointers.

This call also releases blocks claimed with `FNclaimRMA`, so callers do not need separate heap and RMA release paths.

### Relocatable heap blocks

Use a negative size with `FNclaim`:

```basic
record% = FNclaim(-256)
```

This claims a block that may later be moved by `PROCheap_garbage`. HeapLib stores a 4-byte header in front of the returned pointer and records the live pointer in the relocatable-block table.

Only relocatable blocks may be resized with `FNextend`:

```basic
record% = FNextend(record%, 128)
IF record% AND 1 THEN ERROR 0, "Extend failed"
```

`FNextend` returns the new pointer. If bit 0 is set, the extend failed. The library uses this odd-pointer convention because successful heap pointers are word-aligned.

The `size%` argument may be negative, in which case the block is reduced rather than enlarged.

### RMA blocks

Use `FNclaimRMA(size%)` when you explicitly need RMA rather than the private heap:

```basic
module_workspace% = FNclaimRMA(512)
```

Release it with the same `PROCrelease` call. HeapLib distinguishes RMA and heap addresses itself.

## Heap growth and reduction

* `FNclaim` and `FNextend` call `FNenlargeheap` when the current heap cannot satisfy a request.
* `FNenlargeheap` attempts to extend the Wimp slot by one page and then grows the `OS_Heap`.
* `PROCheap_reduce` is the non-relocating shrink path: it releases free pages from the end of the heap back to the Wimp slot.
* `PROCheap_free(max%, free%)` reports total heap size and current free space.

## Garbage collection for relocatable blocks

`PROCheap_garbage` attempts to compact relocatable blocks and then calls `PROCheap_reduce`.

Only relocatable blocks may move during garbage collection; fixed heap blocks stay in place.
If possible, garbage collection also moves the relocatable-block index down the heap and reduces the Wimp slot so that only the minimum practical space remains claimed.

If a block must move, the library calls an application-supplied routine:

```basic
DEFPROCheap_relocate(block%, size%)
CASE block% OF
WHEN index%
  PROCheap_oktomove(index%, size%)
WHEN buffer%
  PROCheap_oktomove(buffer%, size%)
ENDCASE
ENDPROC
```

Rules for this callback:

* The program must update every stored pointer that may refer to the block.
* Call `PROCheap_oktomove` after deciding to move the block.
* If a block should not move, do not call `PROCheap_oktomove`.
* Call `PROClockblock(block%)` before garbage collection if a relocatable block must stay fixed temporarily.
* Call `PROCunlockblock(block%)` when it may move again.
* If pointers are stored in an array or another collection, search and update every matching entry during relocation.

If your program cannot reliably track and update all references to a relocatable block, do not use relocatable allocations for that data.

`PROCheap_garbage` is not guaranteed to fully compact the heap in one pass. Because of the way allocations are laid out, repeated calls may be needed before the heap reaches its smallest practical form.

## Linked-list helpers

HeapLib includes helpers for a simple owned chain of allocations:

* `FNclaimlinked(top%, size%)` claims `size%+4` bytes, links the new block at the head of the chain, and returns the user pointer.
* `PROCreleaselinks(top%)` frees the whole chain in one call.
* `FNstrduplinked(top%, a$)` duplicates a string into a linked block.
* `PROCreleaselinked(top%, d%)` removes one linked item.

This is useful for dynamic collections where all blocks can be released together.

## String helper

`FNstrdup(a$)` claims `LEN(a$)+1` bytes, copies the CR-terminated BASIC string into that block, and returns the pointer.

## Asset included with this skill

The non-debug library has been captured as plain text at `assets/HeapLib/HeapLib,fd1`. Use it as:

* a source reference when reading or reimplementing the allocator pattern;
* a direct starting point for BASIC programs which want this heap manager;
* a basis for deriving smaller specialised allocators.
