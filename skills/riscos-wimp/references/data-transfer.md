# Data Transfer

Use this file for `DataLoad`, `DataSave`, and scrap-file based Wimp transfers.

Public references:

* Wimp PRM chapter: `http://www.riscos.com/support/developers/prm/wimp.html`
* Icon bar file drags note: `https://gerph.github.io/riscos-prminxml-staging/prm/html/select/desktop/iconbarfiledrags.html`

## General approach

For file-transfer messages:

* validate the file type first
* only acknowledge messages the task actually accepts
* keep the acknowledgement path and the real load/save action aligned

## DataLoad

Typical `DataLoad` flow:

1. inspect the offered file type and path
2. reject unsupported types
3. send `DataLoadAck`
4. perform the load action
5. clean up any tracked scrap-file state if this was a scrap-mediated transfer

## DataSave

Typical `DataSave` flow:

1. validate that the task can supply the requested data
2. inspect any required environment such as `Wimp$Scrap`
3. rewrite the destination to the scrap file if following the standard scrap-transfer pattern
4. send `DataSaveAck`
5. remember the returned reference if later cleanup depends on it

## Scrap-file flows

If the implementation uses `<Wimp$Scrap>`:

* track the reference number associated with the transfer
* delete the scrap file only when the tracked transfer completes
* do not delete unrelated scrap files just because another transfer passed through the task

## Error handling

Treat unsupported file types, missing scrap configuration, and failed acknowledgements as data-transfer errors local to this path. Do not let them turn into repeated poll-loop failures.

## Icon bar device file drags

The public icon-bar file-drags note documents a later extension used by FS Filer device icons.

That note is not directly about Display Manager, but it is useful context when a task or module interacts with icon-bar devices:

* save-box drags to icon-bar device icons can use `Message_DataSave` / `Message_DataSaveAck`
* device filers may then receive `Message_DataLoad` on completion
* filer-to-device drags can involve a follow-up `Message_FilerDevicePath`
* the destination directory may be derived from `FSFiler$DefaultPath`

Do not assume every icon-bar drag is the plain save-box protocol. If the task interacts with filing-system device icons, read that note before implementing or reviewing the message flow.
