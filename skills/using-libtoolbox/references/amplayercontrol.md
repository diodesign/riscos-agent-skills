# `amplayercontrol`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/amplayercontrol`

Category: `extension`

Purpose: Client-visible information for the GAMPlayer gadget

Use it when: Read for the GAMPlayer gadget extension used by media-player style UIs.

## Includes

- `kernel.h`
- `toolbox.h`

## Main Types

- `GAMPlayer`

## Public Constants And Method Codes

- `GAMPlayer_Sprite` = `(1<<0) /* For buttons only */`
- `GAMPlayer_AlignLeft` = `(0<<1) /* For displays only */`
- `GAMPlayer_AlignCentre` = `(1<<1) /* For displays only */`
- `GAMPlayer_AlignRight` = `(2<<1) /* For displays only */`
- `GAMPlayer_AlignInvalid` = `(3<<1) /* For displays only */`
- `GAMPlayer_AlignMask` = `(3<<1) /* For displays only */`
- `GAMPlayerValidFlags` = `0xC0000007`
- `GAMPlayer_TypeStop` = `(0x00)`
- `GAMPlayer_TypePausePlay` = `(0x01)`
- `GAMPlayer_TypeRewind` = `(0x02)`
- `GAMPlayer_TypeForward` = `(0x03)`
- `GAMPlayer_TypeSkip` = `(0x04)`
- `GAMPlayer_TypePosition` = `(0x10)`
- `GAMPlayer_TypeVolume` = `(0x11)`
- `GAMPlayer_TypeElapsedTime` = `(0x20)`
- `GAMPlayer_TypeTotalTime` = `(0x21)`
- `GAMPlayer_TypeRemainTime` = `(0x22)`
- `GAMPlayer_TypeTrack` = `(0x30)`
- `GAMPlayer_TypeAlbum` = `(0x31)`
- `GAMPlayer_TypeArtist` = `(0x32)`
- `GAMPlayer_TypeTrackNum` = `(0x33)`
- `GAMPlayer_TypeYear` = `(0x34)`
- `GAMPlayer_TypeComment` = `(0x35)`
- `GAMPlayer_TypeTrackOrLeaf` = `(0x3F) /* N/I */`
- `GAMPlayer_TypeBitrate` = `(0x40)`
- `GAMPlayer_TypeFrequency` = `(0x41)`
- `GAMPlayer_TypeMPEGVersion` = `(0x42)`
- `GAMPlayer_TypeLayer` = `(0x43)`
- `GAMPlayer_TypeMode` = `(0x44)`
- `GAMPlayer_TypeChannels` = `(0x45)`
- `GAMPlayer_TypeOriginal` = `(0x50)`
- `GAMPlayer_TypeCopyright` = `(0x51)`
- `GAMPlayer_TypeCRC` = `(0x52)`
- `GAMPlayer_SWIBase` = `0x140440`
- `GAMPlayer_MethodBase` = `(GAMPlayer_SWIBase<<4)`
- `GAMPlayer_EventBase` = `(GAMPlayer_SWIBase)`
- `GAMPlayer_Type` = `( (sizeof(GAMPlayer)) << 16 | \`
- `GAMPlayer_GetFont` = `(GAMPlayer_MethodBase + 0)`
- `GAMPlayer_SetFont` = `(GAMPlayer_MethodBase + 1)`
- `GAMPlayer_GetColours` = `(GAMPlayer_MethodBase + 2)`
- `GAMPlayer_SetColours` = `(GAMPlayer_MethodBase + 3)`

## Notes

- This header is constant/type-oriented and does not publish C veneer functions.
