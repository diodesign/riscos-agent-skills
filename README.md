# Agent skills for RISC OS

When developing for RISC OS it is useful to give the AI agents sufficient
information to be able to drive the system. This repository contains an
extract from the [RISC OS Build Environment](https://hub.docker.com/r/gerph/riscos-build)
of the skills that are used there. It is intended that it be available to
others to use if they wish, or to contribute to if they create new skills
which are useful.

## Summary

Skills are definitions of how to perform certain actions which are commonly needed by AI
agents.
They don't comprise full information on a topic, but provide enough guidance to aid an AI
system to diagnose problems, follow procedures or perform certain tasks.

Within a project these skills are usually defined with the configuration directory for
the AI coding agent. For example:

* Qwen skills are held in: `.qwen/skills/`
* Claude skills are held in: `.claude/skills/`
* Gemini skills are held in: `.gemini/skills/`
* Codex skills are held in: `.agents/skills/`

Each skill is given a simple name for the directory, and contains a file `SKILL.md` which
describes the skill, with a short header. Other resources may also be stored in this directory
to help the skill with specific tasks.

More information on building these skill files can be found at [AgentSkills.io](https://agentskills.io/home).

## Skills

The following skills are provided:

### Languages

* `using-bbcbasic`: BASIC syntax, common usage and integration with RISC OS.
* `writing-c`: Coding style and guidance for writing C code.
* `writing-cplusplus`: Writing, building and testing C++ for the 64-bit build environment.
* `writing-pascal`: Writing, building and testing Pascal with `riscos-p2cc`/`riscos64-p2cc`.
* `writing-fortran`: Writing, building and testing Fortran with `riscos64-fortran`.
* `using-perl`: Writing and debugging Perl for the RISC OS Perl 5.001 interpreter.
* `writing-assembly`: Writing ARM assembly (veneers, callbacks, module entry points) with ObjAsm.
* `writing-assembly-tests`: Writing ObjAsm command-line exercisers under `testcode/s`.
* `reading-assembly`: Translating ObjAsm/ARM assembly into another language, tests, or documentation.

### Modules and build system

* `writing-cmodules`: Development, layout, building and testing of RISC OS modules in C.
* `designing-modules`: Designing module interfaces before implementation begins.
* `using-cmhg`: The CMHG file format and CMunge usage for module headers.
* `using-makefiles`: The RISC OS AMU makefile build system, its shared makefile types and variables.
* `porting-to-riscos-c`: Porting POSIX C projects to RISC OS with `riscos-cport`.
* `writing-pymodules`: Building and testing PyModules (Python modules for RISC OS Pyromaniac).
* `writing-oslib-defs`: Writing OSLib Def files and generating headers/veneers with `riscos-defmod`.
* `allocating-resources`: Registering module names, SWI chunks, filetypes and other allocations with RISC OS Open.

### RISC OS subsystems

* `riscos-filesystem`: RISC OS filesystem conventions and translating to/from host filenames.
* `riscos-commands`: Using `*Commands` in Obey files, OSCLI, `.robuild.yaml` and Pyromaniac.
* `riscos-output`: Text/graphics output, VDU, OS_Plot, Draw, Sprites, Fonts and ColourTrans.
* `riscos-wimp`: Writing, reviewing and porting Wimp code (windows, menus, events, SWIs).
* `riscos-wimp-app`: Structuring small desktop Wimp applications, especially iconbar apps.
* `riscos-wimp-templates`: Building Wimp window templates as `TemplateText` files with `riscos-ccres`.
* `riscos-filer-like`: Building filer-like windows (grid/list views, hit-testing, scrolling).
* `riscos-desktop-fileraction`: Driving desktop Filer operations via the FilerAction module.
* `riscos-graphics-converters`: Writing ImageFileConvert image converter modules.
* `riscos-network-resolver`: Using the Resolver module for DNS lookups and hostent data.
* `riscos-network-dcistatistics`: Implementing and querying DCI4 network statistics suppliers.
* `riscos-urls-fetching`: Fetching URL/URI contents with the Acorn URL_Fetcher module.
* `riscos-urls-launching`: Launching URLs/URIs via AcornURI, `*URIdispatch` or legacy ANT broadcasts.
* `riscos-throwback`: Reporting compiler/tool errors to desktop editors via LibThrowback/DDEUtils.
* `riscos-style`: Applying the Acorn RISC OS Style Guide to desktop application design.
* `riscos-re`: Reverse engineering existing RISC OS modules from their binaries.

### Libraries

* `using-libasm`: The Asm library for optimised multiply/divide, IRQ control and low-level routines.
* `using-libgcontext`: The GContext graphics library for drawing primitives and text.
* `using-liboslib`: The OSLib typed SWI interface library, headers and naming conventions.
* `using-libriscoslib`: The RISC_OSLib library for desktop applications.
* `using-libtoolbox`: The Toolbox veneer library for windows, menus, dialogues and gadgets.
* `using-toolbox-imagefilegadget`: Using the Toolbox ImageFileGadget object and its methods.

### Testing and CI

* `using-tooltester`: The `riscos-tooltester` command and `tests.txt` file format.
* `writing-pyromaniac-integration-tests`: Writing Pyromaniac `testcode/tests-*.txt` integration tests.
* `ci-testing`: Creating and repairing RISC OS CI pipelines (GitHub Actions, GitLab CI, `.robuild.yaml`).
* `using-gh`: Working with GitHub repositories, pull requests and releases via the `gh` CLI.
* `using-git`: Safe non-interactive git usage, commit preparation and handling dirty worktrees.
* `creating-pull-requests`: Writing clear, reviewer-focused pull/merge request descriptions.

### Documentation

* `writing-prminxml`: Creating interface documentation with PRM-in-XML.
* `using-stronghelp`: Creating and maintaining StrongHelp manuals.

### Skill management

* `updating-robe-skills`: Creating or updating AI skills for the RISC OS build environment.

## Installation in Claude

This repository also provide a plugin marketplace for Claude. Add the marketplace to Claude and then enable the RISC OS skills plugin.

```
/plugin marketplace add gerph/riscos-agent-skills
/plugin install riscos-skills@riscos-agent-skills
/reload-plugins
```

### Plugin updates

Auto-update can be enabled by running `/plugin` and navigating to Marketplaces > riscos-skills-plugin and enabling auto-update. Each time Claude starts, any updates to the plugin will be automatically installed.

Or update manually using:

```
/plugin marketplace update riscos-skills-plugin
/reload-plugins
```

## Installation in Codex

This repository can also be used as a Codex plugin. The skill content is the
same; Codex discovers it through the `.codex-plugin/plugin.json` manifest at
the repository root.

To install it for your user account:

```bash
mkdir -p ~/plugins ~/.agents/plugins
ln -sfn /absolute/path/to/riscos-agent-skills ~/plugins/riscos-skills
```

Create or update `~/.agents/plugins/marketplace.json`:

```json
{
  "name": "local",
  "interface": {
    "displayName": "Local Plugins"
  },
  "plugins": [
    {
      "name": "riscos-skills",
      "source": {
        "source": "local",
        "path": "./plugins/riscos-skills"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Coding"
    }
  ]
}
```

If you already have a marketplace file, append the `riscos-skills` entry instead
of replacing the whole file. Restart Codex after updating the marketplace.

## Installation in Gemini CLI

This repository is compatible with Gemini CLI's Agent Skills and Extensions system.

### As an Extension (Recommended)

Installing as an extension allows Gemini to automatically discover and use these skills whenever you are working on a RISC OS project.

```bash
gemini extensions install https://github.com/gerph/riscos-agent-skills
```

### As Agent Skills only

If you prefer to only install the individual skills without the full extension package:

```bash
gemini skills install https://github.com/gerph/riscos-agent-skills
```

Once installed, Gemini will automatically prompt to activate relevant skills (like `writing-cmodules` or `using-bbcbasic`) when it identifies a RISC OS task.

## Installation in Qwen Code

Qwen Code does not have a remote plugin installation system like Claude, Codex, or Gemini. To use these skills with Qwen Code, you need to manually copy the skill files into your local project's `.qwen/skills/` directory.

### Manual Installation

1. Clone or download this repository to your local machine:

```bash
git clone https://github.com/gerph/riscos-agent-skills.git
```

2. Copy the skill directories you want to use into your project's `.qwen/skills/` directory:

```bash
# Create the skills directory if it doesn't exist
mkdir -p .qwen/skills/

# Copy specific skills you want to use
cp -r /path/to/riscos-agent-skills/skills/using-bbcbasic .qwen/skills/
cp -r /path/to/riscos-agent-skills/skills/writing-cmodules .qwen/skills/
# Add other skills as needed
```

Alternatively, you can create symbolic links to the skills:

```bash
# Create symbolic links to the skills
ln -s /path/to/riscos-agent-skills/skills/using-bbcbasic .qwen/skills/
ln -s /path/to/riscos-agent-skills/skills/writing-cmodules .qwen/skills/
# Add other skills as needed
```

3. Restart Qwen Code or reload your project for the skills to become available.

Qwen Code will recognize and make use of the skills when you invoke them with the `skill:` command (e.g., `skill: "using-bbcbasic"`).
