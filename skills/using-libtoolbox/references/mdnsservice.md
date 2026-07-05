# `mdnsservice`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/mdnsservice`

Category: `extension`

Purpose: Read the colour used by the MDNSService browser

Use it when: Read for the mDNS service gadget extension.

## Includes

- `kernel.h`
- `window.h`
- `toolbox.h`

## Main Types

- `MDNSService`
- `MDNSServiceSelectionEvent`

## Public Functions

- `mdnsservice_get_colour`: Read the colour used by the MDNSService browser
  Prototype: `extern _kernel_oserror *mdnsservice_get_colour ( unsigned int flags, ObjectId window, ComponentId mdnsservice, int *outflags, unsigned long *colour );`
- `mdnsservice_set_colour`: Select the colour used by the MDNSService browser
  Prototype: `extern _kernel_oserror *mdnsservice_set_colour ( unsigned int flags, ObjectId window, ComponentId mdnsservice, unsigned long colour );`
- `mdnsservice_get_font`: Read the font in use in the MDNSService browser
  Prototype: `extern _kernel_oserror *mdnsservice_get_font ( unsigned int flags, ObjectId window, ComponentId mdnsservice, char *buffer, int size, int *xsize, int *ysize, int *nbytes );`
- `mdnsservice_set_font`: Set the font to use in the MDNSService browser
  Prototype: `extern _kernel_oserror *mdnsservice_set_font ( unsigned int flags, ObjectId window, ComponentId mdnsservice, const char *font_name, unsigned int width, unsigned int height );`
- `mdnsservice_set_service`: Set the services to look for in the MDNSService browser
  Prototype: `extern _kernel_oserror *mdnsservice_set_service ( unsigned int flags, ObjectId window, ComponentId mdnsservice, const char *service_name, unsigned int width, unsigned int height );`
- `mdnsservice_get_service`: Read the services searched for in the MDNSService browser
  Prototype: `extern _kernel_oserror *mdnsservice_get_service ( unsigned int flags, ObjectId window, ComponentId mdnsservice, char *buffer, int size, int *nbytes );`
- `mdnsservice_get_domain`: Read the domain searched in the MDNSService browser
  Prototype: `extern _kernel_oserror *mdnsservice_get_domain ( unsigned int flags, ObjectId window, ComponentId mdnsservice, char *buffer, int size, int *nbytes );`
- `mdnsservice_set_domain`: Set the domain to look at in the MDNSService browser
  Prototype: `extern _kernel_oserror *mdnsservice_set_domain ( unsigned int flags, ObjectId window, ComponentId mdnsservice, const char *domain_name );`

## Public Constants And Method Codes

- `MDNSServiceValidFlags` = `0xC0000000`
- `MDNSService_SWIBase` = `0x140500 /* Allocated */`
- `MDNSService_MethodBase` = `(MDNSService_SWIBase<<4)`
- `MDNSService_EventBase` = `(MDNSService_SWIBase)`
- `MDNSService_Type` = `( (sizeof(MDNSService)) << 16 | \`
- `MDNSService_GetFont` = `(MDNSService_MethodBase + 0)`
- `MDNSService_SetFont` = `(MDNSService_MethodBase + 1)`
- `MDNSService_GetColours` = `(MDNSService_MethodBase + 2)`
- `MDNSService_SetColours` = `(MDNSService_MethodBase + 3)`
- `MDNSService_GetService` = `(MDNSService_MethodBase + 4)`
- `MDNSService_SetService` = `(MDNSService_MethodBase + 5)`
- `MDNSService_GetDomain` = `(MDNSService_MethodBase + 6)`
- `MDNSService_SetDomain` = `(MDNSService_MethodBase + 7)`
- `MDNSService_Selection` = `(MDNSService_EventBase + 0)`
- `MDNSService_Selection_Adjust` = `(1<<0)`
- `MDNSService_Selection_DoubleClick` = `(1<<1)`
- `MDNSService_Selection_LookupFailed` = `(1<<2) /* Service may have gone? */`
- `MDNSService_Selection_ServiceOmitted` = `(1<<3) /* Would not fit into the block */`
- `MDNSService_Selection_NameOmitted` = `(1<<4) /* Would not fit into the block */`
- `MDNSService_Selection_TXTOmitted` = `(1<<5) /* Must do the resolution yourself */`
