# `urlimage`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/urlimage`

Category: `extension`

Purpose: Client-visible information for the URLImage gadget

Use it when: Read for the URLImage gadget extension that fetches and displays images from URLs.

## Main Types

- `URLImage`
- `URLImageClickedEvent`
- `URLImageCompleteEvent`

## Public Constants And Method Codes

- `URLImage_RetainSourceImage` = `(1<<0)`
- `URLImage_DirectRender` = `(1<<1)`
- `URLImage_Border` = `(1<<2)`
- `URLImage_DeliverClick` = `(1<<3)`
- `URLImage_DeliverComplete` = `(1<<4)`
- `URLImage_ProgressPercentage` = `(1<<5)`
- `URLImageValidFlags` = `0xC000003F`
- `URLImage_SWIBase` = `0x140540 /* Allocated */`
- `URLImage_MethodBase` = `(URLImage_SWIBase<<4)`
- `URLImage_EventBase` = `(URLImage_SWIBase)`
- `URLImage_Type` = `( (sizeof(URLImage)) << 16 | \`
- `URLImage_SetURL` = `(URLImage_MethodBase + 0)`
- `URLImage_Clicked` = `(URLImage_EventBase + 0)`
- `URLImage_Complete` = `(URLImage_EventBase + 1)`
- `URLImage_Clicked_Adjust` = `0x00000001`
- `URLImage_Clicked_Select` = `0x00000004`
- `URLImage_Clicked_Drag` = `0x00000020`
- `URLImage_Clicked_Double` = `0x00000040`
- `URLImage_Complete_Success` = `(1<<0)`

## Notes

- This header is constant/type-oriented and does not publish C veneer functions.
