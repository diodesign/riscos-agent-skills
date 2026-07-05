# Internationalisation

## Use this reference for

- Localisable text
- Character-set handling
- Locale-sensitive display and parsing

## Language rules

- Assume English is not the user's first language.
- Keep text simple enough to translate.
- Avoid culture-specific jokes, puns, and icon metaphors.
- Translate mnemonic shortcuts when the target language requires different initial letters.

## Character-set rules

- Support the active territory and character-set choices made by the user.
- Handle accented and non-British characters correctly in text entry, display, and storage.
- Avoid hard-coding assumptions about the British character set.

## Format rules

- Use system services for date and time conversion.
- Respect local conventions for dates, times, and decimal formats.
- Parse and display formatted information in a way that follows the current locale rather than British defaults.
