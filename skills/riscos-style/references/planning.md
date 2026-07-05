# Planning And Desktop Fit

## Use this reference for

- Early application design
- Desktop integration reviews
- Terminology and general wording
- Deciding whether a feature fits classic RISC OS expectations

## Core principles

- Design for consistency across the desktop so users can transfer knowledge from one application to another.
- Optimise for ease of learning, re-learning, and productive use.
- Make options and actions discoverable without forcing users to guess.
- Keep the application harmonious with the icon bar, pinboard, filer, and other desktop applications.
- Support multi-tasking well enough that the application does not degrade the rest of the machine.
- Prefer simple, reliable behaviour over feature sprawl.

## General rules

- Start considering style at specification time, not as a final polish step.
- Keep the application's look and feel aligned with established desktop conventions.
- Make file interchange and inter-application working easy where the application type permits it.
- Use standard printer drivers and other system facilities instead of custom parallel behaviour.
- Avoid jargon in user-facing text.
- Use the established names for desktop objects such as `icon bar`, `pinboard`, `window`, and `dialogue box`.
- Remember that the guide expects applications to coexist with others, not act as the whole machine unless screen takeover is genuinely justified.

## Desktop behaviour

- Provide an icon bar icon for normal desktop applications.
- Provide a sprite for iconised windows.
- Avoid resetting system-wide configuration or degrading concurrent applications.
- Keep terminology consistent in menus, help text, manuals, and dialogue boxes.
- Use `icon bar` for the bar at the foot of the screen and `pinboard` for the desktop backdrop.
- Distinguish a normal document or work window from a `dialogue box`, which is for delayed-action interaction with the user.

## Quality bar

- Favour a smaller application that behaves well over a larger one that is unreliable.
- Preserve user confidence by making behaviour predictable and familiar.
- State RISC OS version requirements clearly if the application cannot support older releases.
