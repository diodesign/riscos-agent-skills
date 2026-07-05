# Reviewing existing PRM-in-XML documentation

Use this when checking previously-written PRM-in-XML chapters for accuracy
or for readiness to publish, rather than when authoring new content.

## Verifying a claim against real behaviour

Prefer a real, live check over a plausible-sounding justification. If an
example or claim looks unverifiable only because no sample file or fixture
exists:

* Check whether the format is reconstructable from the tool's own parsing
  source (its source code, a worked example elsewhere in the manual, or its
  own self-tests). Building a minimal valid fixture by hand from this is
  often enough to turn an "unverifiable" example into a verified one with
  real captured output.
* If the format is complex, ambiguous, or risky to reconstruct by hand (so a
  hand-built fixture might itself be wrong), ask the user for a genuine
  sample file rather than guessing at the format. This is also worth doing
  even for simpler formats if a real-world example would materially improve
  the manual (not just verify it) — a real file often makes a better worked
  example than a synthetic one.

## When verification genuinely fails

If a documented claim cannot be substantiated despite trying the realistic
verification angles available (direct invocation, alternate code paths,
debug tracing), do not retain a hedged, plausible-sounding claim "confirmed
indirectly" — and do not silently rewrite the claim into something weaker
just to make it pass. Ask the user. A persistent mismatch between the
documentation and observed behaviour can mean the documentation is wrong,
but it can equally mean the tool or its current build has a real bug — both
are findings that need a decision from the user, not a guess.

## Citing sources responsibly

When writing or reviewing a bibliography, source list, or any reference to
where information came from:

* Local-only material — paths inside the build environment, installed
  resource trees, or files private to this repository — must not appear as
  visible reader-facing text. Move them into an XML comment immediately
  before the list or paragraph they support, so the information stays
  available to maintainers without being shown to readers. See the
  authorial-voice rule in `SKILL.md` for the same comment-placement
  convention applied to verification narration.
* Before citing material as if it were public, confirm a genuine public
  equivalent actually exists and corresponds to the local material — check
  the author's published repositories (if relevant) and read each candidate
  repository's stated purpose rather than assuming a plausible-sounding name
  is the right one.
* If no public equivalent exists, say so in the comment rather than citing
  the closest available public page as if it were equivalent.
