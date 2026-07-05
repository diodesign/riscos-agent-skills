# `divider`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/divider`

Category: `extension`

Purpose: Client-visible information for the Divider gadget

Use it when: Read for the Divider gadget extension.

## Main Types

- `Divider`

## Public Constants And Method Codes

- `Divider_Vertical` = `(1<<0)`
- `DividerValidFlags` = `0xC0000001`
- `GDivider_SWIBase` = `0x140580`
- `GDivider_MethodBase` = `(GDivider_SWIBase<<4)`
- `GDivider_EventBase` = `(GDivider_SWIBase)`
- `GDivider_Type` = `( (sizeof(Divider)) << 16 | \`

## Notes

- This header is constant/type-oriented and does not publish C veneer functions.
