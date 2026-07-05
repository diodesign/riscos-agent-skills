#!/usr/bin/env python3
"""Generate per-header Markdown references for using-libtoolbox."""

from __future__ import annotations

import re
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = SKILL_DIR / "references"

HEADER_SPECS = [
    {
        "name": "toolbox",
        "path": Path("/riscos-resources/Export/Export/Lib/tboxlibs/h/toolbox"),
        "category": "core",
        "manual": "http://www.riscos.com/support/developers/toolbox/toolintro.html",
        "use": "Read first for Toolbox object ids, resource file structures, core SWIs, and generic event/layout types.",
    },
    {
        "name": "wimp",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/wimp"),
        "category": "support",
        "manual": "",
        "use": "Read when Toolbox code drops to raw Wimp handles, events, icons, windows, or message blocks.",
    },
    {
        "name": "wimplib",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/wimplib"),
        "category": "support",
        "manual": "",
        "use": "Read when code uses the older helper structures and colour/icon convenience definitions from `wimplib`.",
    },
    {
        "name": "flex",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/flex"),
        "category": "support",
        "manual": "",
        "use": "Read when Toolbox support code relies on the flex heap helper rather than standard allocation.",
    },
    {
        "name": "drawfile",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/drawfile"),
        "category": "support",
        "manual": "http://www.riscos.com/support/developers/toolbox/render.html",
        "use": "Read when redraw code renders Draw files inside Toolbox windows or prints Draw content.",
    },
    {
        "name": "window",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/window"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/windows.html",
        "use": "Read for Toolbox windows, toolbars, pointer/help/menu attachment, keyboard shortcuts, and Wimp bridging.",
    },
    {
        "name": "gadgets",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/gadgets"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/windows.html",
        "use": "Read for generic gadget methods and the built-in gadget families hosted by Toolbox windows.",
    },
    {
        "name": "menu",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/menu"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/menus.html",
        "use": "Read for shared menus, per-entry state, submenu wiring, and selection dispatch.",
    },
    {
        "name": "iconbar",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/iconbar"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/iconbar.html",
        "use": "Read for iconbar object templates, Select/Adjust behaviour, menus, help, and icon presentation.",
    },
    {
        "name": "colourdbox",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/colourdbox"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/colourdbox.html",
        "use": "Read for the standard colour selection dialogue.",
    },
    {
        "name": "colourmenu",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/colourmenu"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/colmenu.html",
        "use": "Read for menu-based colour selection.",
    },
    {
        "name": "dcs",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/dcs"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/dcs.html",
        "use": "Read for Discard/Cancel/Save confirmation flows.",
    },
    {
        "name": "fileinfo",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/fileinfo"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/fileinfo.html",
        "use": "Read for the standard file metadata dialogue.",
    },
    {
        "name": "fontdbox",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/fontdbox"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/fontdbox.html",
        "use": "Read for the standard font chooser dialogue.",
    },
    {
        "name": "fontmenu",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/fontmenu"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/fontmenu.html",
        "use": "Read for menu-based font selection.",
    },
    {
        "name": "printdbox",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/printdbox"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/print.html",
        "use": "Read for standard print dialogue flows.",
    },
    {
        "name": "proginfo",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/proginfo"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/proginfo.html",
        "use": "Read for About/Program Info dialogues.",
    },
    {
        "name": "quit",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/quit"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/quit.html",
        "use": "Read for quit-confirmation dialogues.",
    },
    {
        "name": "saveas",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/saveas"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/saveas.html",
        "use": "Read for SaveAs dialogues and the Toolbox-managed save protocol.",
    },
    {
        "name": "scale",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/scale"),
        "category": "class",
        "manual": "http://www.riscos.com/support/developers/toolbox/scale.html",
        "use": "Read for scale-factor dialogues.",
    },
    {
        "name": "optionswindow",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/optionswindow"),
        "category": "extension",
        "manual": "",
        "use": "Read for the extra OptionsWindow object module and pane-management API.",
    },
    {
        "name": "ToolAction",
        "filename": "toolaction-ref.md",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/ToolAction"),
        "category": "extension",
        "manual": "",
        "use": "Read for the ToolAction gadget extension used for toolbar-like controls with separate Select/Adjust behaviour.",
    },
    {
        "name": "amplayercontrol",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/amplayercontrol"),
        "category": "extension",
        "manual": "",
        "use": "Read for the GAMPlayer gadget extension used by media-player style UIs.",
    },
    {
        "name": "colourswatch",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/colourswatch"),
        "category": "extension",
        "manual": "",
        "use": "Read for the ColourSwatch gadget extension.",
    },
    {
        "name": "divider",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/divider"),
        "category": "extension",
        "manual": "",
        "use": "Read for the Divider gadget extension.",
    },
    {
        "name": "imagefilegadget",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/imagefilegadget"),
        "category": "extension",
        "manual": "",
        "use": "Read for the ImageFileGadget extension used to present converted image content in windows.",
    },
    {
        "name": "mdnsservice",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/mdnsservice"),
        "category": "extension",
        "manual": "",
        "use": "Read for the mDNS service gadget extension.",
    },
    {
        "name": "scrollbar",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/scrollbar"),
        "category": "extension",
        "manual": "",
        "use": "Read for the Scrollbar gadget extension.",
    },
    {
        "name": "scrolllist",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/scrolllist"),
        "category": "extension",
        "manual": "",
        "use": "Read for the ScrollList gadget extension, including selection and database-query helpers.",
    },
    {
        "name": "textarea",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/textarea"),
        "category": "extension",
        "manual": "",
        "use": "Read for the TextArea gadget extension and its text-editing API.",
    },
    {
        "name": "urlimage",
        "path": Path("/riscos-resources/Export/Lib/tboxlibs/h/urlimage"),
        "category": "extension",
        "manual": "",
        "use": "Read for the URLImage gadget extension that fetches and displays images from URLs.",
    },
]


def squash_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def extract_description(text: str) -> str:
    for label in ("Description", "Purpose"):
        match = re.search(rf"{label}\s*:\s*(.+)", text)
        if match:
            return squash_ws(match.group(1))
    return "Public header."


def extract_includes(text: str) -> list[str]:
    return re.findall(r'#include "([^"]+)"', text)


def extract_named_types(text: str) -> list[str]:
    seen = []
    lines = text.splitlines()
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        if line.startswith("typedef struct") or line.startswith("typedef union"):
            depth = line.count("{") - line.count("}")
            while index + 1 < len(lines):
                index += 1
                depth += lines[index].count("{") - lines[index].count("}")
                if depth <= 0 and "}" in lines[index]:
                    match = re.search(r"}\s*([A-Za-z_]\w*)\s*;", lines[index])
                    if match:
                        name = match.group(1)
                        if name not in seen:
                            seen.append(name)
                    break
        else:
            match = re.match(
                r"typedef\s+(?:unsigned\s+)?(?:int|long|short|char|bits|void|float|double)\s+([A-Za-z_]\w*)\s*;",
                line,
            )
            if match:
                name = match.group(1)
                if name not in seen:
                    seen.append(name)
        index += 1
    return seen


def extract_defines(text: str) -> list[tuple[str, str]]:
    defines = []
    for match in re.finditer(r"^#define\s+([A-Za-z_]\w*)\s+(.+)$", text, re.M):
        name = match.group(1)
        value = squash_ws(match.group(2))
        if name.startswith("__") or value.startswith("#"):
            continue
        defines.append((name, value))
    return defines


def extract_functions(text: str) -> list[tuple[str, str, str]]:
    functions = []
    lines = text.splitlines()
    index = 0

    while index < len(lines):
        line = lines[index]
        if "Name" in line and ":" in line:
            block = []
            while index < len(lines):
                block.append(lines[index])
                if "*/" in lines[index]:
                    break
                index += 1

            name = ""
            desc = ""
            for block_line in block:
                if "Name" in block_line and ":" in block_line:
                    name = squash_ws(block_line.split(":", 1)[1])
                if "Description" in block_line and ":" in block_line:
                    desc = squash_ws(block_line.split(":", 1)[1])

            index += 1
            if name:
                proto_lines = []
                while index < len(lines):
                    proto_lines.append(lines[index])
                    if ";" in lines[index]:
                        break
                    index += 1
                proto = squash_ws(" ".join(proto_lines))
                if proto.startswith("extern "):
                    functions.append((name, desc or "Public veneer.", proto))
        index += 1

    return functions


def render_reference(spec: dict[str, str]) -> str:
    text = spec["path"].read_text(encoding="latin-1")
    description = extract_description(text)
    includes = extract_includes(text)
    types = extract_named_types(text)
    defines = extract_defines(text)
    functions = extract_functions(text)

    lines = [f"# `{spec['name']}`", ""]
    lines.append(f"Installed header: `{spec['path']}`")
    lines.append("")
    lines.append(f"Category: `{spec['category']}`")
    lines.append("")
    lines.append(f"Purpose: {description}")
    lines.append("")
    lines.append(f"Use it when: {spec['use']}")
    lines.append("")
    if spec["manual"]:
        lines.append(f"Related Toolbox manual page: {spec['manual']}")
        lines.append("")
    if includes:
        lines.append("## Includes")
        lines.append("")
        for inc in includes:
            lines.append(f"- `{inc}`")
        lines.append("")
    if types:
        lines.append("## Main Types")
        lines.append("")
        for name in types:
            lines.append(f"- `{name}`")
        lines.append("")
    if functions:
        lines.append("## Public Functions")
        lines.append("")
        for name, desc, proto in functions:
            lines.append(f"- `{name}`: {desc}")
            lines.append(f"  Prototype: `{proto}`")
        lines.append("")
    if defines:
        lines.append("## Public Constants And Method Codes")
        lines.append("")
        for name, value in defines:
            lines.append(f"- `{name}` = `{value}`")
        lines.append("")
    if not functions:
        lines.append("## Notes")
        lines.append("")
        lines.append("- This header is constant/type-oriented and does not publish C veneer functions.")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for spec in HEADER_SPECS:
        out = OUT_DIR / spec.get("filename", f"{spec['name']}.md")
        out.write_text(render_reference(spec), encoding="utf-8")


if __name__ == "__main__":
    main()
