# SWI to OSLib naming

OSLib wrapper names usually follow a mechanical translation from the PRM SWI
name or service/event name into a lower-case C identifier.

## Basic rule

Take the SWI name, make it lower case, and insert underscores at the original
capital transitions.

Examples:

* `OS_Write0` -> `os_write0`
* `Wimp_CreateWindow` -> `wimp_create_window`
* `DragASprite_Start` -> `dragasprite_start`
* `MessageTrans_Lookup` -> `messagetrans_lookup`

For the X form, prefix the same transformed name with `x`:

* `XOS_Write0` -> `xos_write0`
* `XWimp_CreateWindow` -> `xwimp_create_window`
* `XToolbox_CreateObject` -> `xtoolbox_create_object`

The common convention is:

* `x...` returns `os_error *` and preserves the PRM X-call behaviour
* the non-`x...` form usually exposes the same operation with a more direct C
  return type or a `void` wrapper

Always confirm the exact signature in the header because some wrappers only
exist in `x...` form, and some non-`x...` forms return status or values rather
than `void`.

## Reason code families

Where a SWI uses reason codes, OSLib usually flattens the SWI family name and
the reason name into a single lower-case function family.

Examples from the exported headers:

* `PaletteV_SetEntry` -> `palettev_set_entry`
* `ToolboxGetSysInfo_TaskName` -> `toolboxgetsysinfo_task_name`
* `ColourTransMiscOp_SetWeights` -> `colourtransmiscop_set_weights`
* `PDriverMiscOpForDriver_AddFont` -> `pdrivermiscopfordriver_add_font`
* `OSDynamicArea_Create` -> `osdynamicarea_create`
* `OSMemory_ReadSize` -> `osmemory_read_size`

The family prefix is not always split into separate words with extra
underscores. If the SWI family itself is already a compound token in the PRM,
OSLib often keeps it as one lower-case block and only inserts underscores at
the later capital boundaries.

## Services, vectors, events, and upcalls

The same lower-case transformation is used for non-SWI interfaces:

* `Service_Reset` -> `service_reset`
* `Event_VSync` -> `event_vsync`
* `UpCall_MoveMemoryRequest` -> `upcall_move_memory_request`
* `ByteV` -> `bytev`
* `TickerV` -> `tickerv`

Their X wrappers follow the same prefix rule:

* `xservice_reset`
* `xevent_vsync`
* `xupcall_move_memory_request`

## Practical use

When reading the PRMs, you can usually predict the OSLib wrapper name quickly
enough to search the inventories or the headers directly.

When reading OSLib code, you can usually reconstruct the originating SWI or
service name by reversing the transformation and looking for obvious family
names and reason codes.

Check the area references for the authoritative exported wrapper list when a
name looks ambiguous.
