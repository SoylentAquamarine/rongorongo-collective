# SQ-4 — comparator search: one real access block confirmed, one related tool found, no direct match

**Trigger:** following indus-script-collective's successful SQ-4 pattern this same cycle (finding IBDB).
Rongorongo's own SQ-4 is similarly untouched and independent of the SQ-1 corpus-access blocker — checked
whether an equivalent resource exists here, and whether the project's own best internal candidate (the
Mamari lunar-calendar sequence) could serve as a held-out benchmark per SQ-4's own suggested scope.

## What's already known / not done yet

Already known: Guy (1990), "On the Lunar Calendar of Tablet Mamari," is primary-source-verified as the
right citation and location (end of line 6 through line 9, Tablet Mamari side A) — but an earlier cycle's
read captured only the descriptive summary (28+2 nights, fish glyphs waxing/waning), not the actual glyph
codes needed for a computational recovery test. Not done: obtaining the actual glyph sequence, or finding
an IBDB-equivalent synthetic benchmark tool for rongorongo specifically.

## Attempt 1: get the actual glyph sequence from Guy (1990)

The HTML article page is reachable (confirmed directly, 94KB fetched) — a change from an earlier cycle's
note that this session's environment couldn't reach `persee.fr` at all. **But the PDF endpoint
(`persee.fr/docAsPDF/...pdf`) returns HTTP 403**, confirmed via both WebFetch and direct `curl` (with a
browser user-agent, and again after first visiting the HTML page to establish a session cookie — same
403 both times). The HTML page itself doesn't inline the actual figure/table content (Figure 1 and Table
1, which hold the glyph-to-calendar-night correspondence, are image-based and not extracted). **This is a
confirmed, specific access block**, narrower and more precise than the earlier cycle's general "can't
reach persee.fr" note — the site is reachable, the specific PDF download is not.

## Attempt 2: find an IBDB-equivalent tool for rongorongo

Searched for a synthetic-corpus, known-answer, calibrated decipherment-method benchmark specific to
rongorongo or proto-writing systems generally. **No direct match found.** Search results instead surfaced
several self-published "rongorongo fully deciphered" claims (academia.edu, Zenodo, a GitHub repo
describing itself as "preserving decoded research logs") — per this project's own standing discipline,
these are not independently verified and should not be treated as resolved claims; worth a future SQ-4
"catalog of claimed decipherments and why they likely fail" entry (mirroring the sibling Phaistos Disc and
Zodiac projects' own prior-claims catalogs), not attempted in this log.

**One genuinely relevant, honestly-scoped tool found**: `github.com/skolachi/rongorongo` (MIT licensed),
a BERT-style masked-language-model trained on 7,441 fully-identified inscriptions (of 14,653 total, from
kohaumotu.org) to fill in missing/uncertain signs. The author explicitly disclaims any decipherment claim:
the script "remains undeciphered although several claims of decipherment have been made." This is a
different kind of tool than SQ-4 asks for (it operates on the real undeciphered corpus directly to predict
missing signs, not a synthetic known-answer comparator for calibrating method confidence) — related
context, not a direct SQ-4 deliverable.

## Honest status

SQ-4 remains substantively unstarted. Two real, disclosed findings this cycle: (1) the Guy 1990 PDF access
block is now precisely characterized (HTML reachable, PDF specifically blocked, not a general site
block), useful for whoever attempts this next; (2) no IBDB-equivalent synthetic benchmark exists for
rongorongo as far as this search found — building one from scratch (per SQ-4's original scope) remains
the real path, not a shortcut via an existing tool the way indus-script-collective found one.

## Next step

Either a different access route for the Guy 1990 PDF (library proxy, direct author/journal contact), or
beginning SQ-4's comparator panel from scratch using a different, genuinely independently-verified short
proto-writing/notation system (not rongorongo-specific) as the known-answer calibration case — closer to
what indus-script-collective's IBDB actually does, rather than searching further for an exact match.
