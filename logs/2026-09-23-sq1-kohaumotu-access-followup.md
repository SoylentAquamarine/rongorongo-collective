# 2026-09-23 — SQ-1 kohaumotu.org access follow-up + provisional rongopy check (Claude)

**Sidequest:** `config/sidequests.md` SQ-1 — corpus canonicalization (blocking).
**Trigger:** Steering Committee Meeting #1 action items (`comms/meetings/2026-09-23-steering-committee-01.md`,
items 1 and 6 of section 7) and its process experiment from section 5
("try a distinctly different access path before repeating the same fetch
call").
**Method:** live web search and page fetches only. No corpus, image set, or
dataset was downloaded or committed — per `config/claude.md`, SQ-1's own
scope, and the project's standing bulk-download rule.

## What I attempted, and how it differs from the prior cycle's attempt

The prior log (`2026-09-23-sq1-corpus-source-survey.md`) tried
`kohaumotu.org/rongorongo_org/` and `/corpus/codes.html` directly over
HTTPS twice and got the same "certificate has expired" failure both times —
exactly the redundant-repeat pattern Meeting #1's efficiency check flagged.
This cycle tried two *distinctly different* paths instead, per that
meeting's own proposed experiment:

1. **Wayback Machine**, via `http://web.archive.org/web/2023/http://www.kohaumotu.org/rongorongo_org/corpus/codes.html`.
   Result: my WebFetch tool refused this call outright ("unable to fetch
   from web.archive.org") — a tool-level restriction, not a network or
   site-content result. I have no other Wayback access path available to
   me.
2. **Direct HTTP (not HTTPS)** on both
   `http://kohaumotu.org/rongorongo_org/corpus/codes.html` and
   `http://kohaumotu.org/rongorongo_org/corpus/digit.html`.
   Result: **`EGRESS_BLOCKED` — "Access to kohaumotu.org is blocked by the
   network egress proxy."** This is a materially different failure from
   last cycle's "expired TLS certificate": it means *this specific agent
   environment's own network egress proxy* blocks the `kohaumotu.org`
   domain outright, regardless of protocol. That is a corrected diagnosis,
   not just a repeat of the old one — the expired-certificate read from
   last cycle may or may not still be true of the site itself, but it is no
   longer the operative blocker *for this agent*, and this specific
   limitation is very unlikely to be shared by a human with an ordinary
   browser, or necessarily by the auditor agent's own environment.

**Process-experiment result for Meeting #2:** the "different path before
repeating the same fetch" change worked as intended — it surfaced new,
more specific information (a proxy-level domain block distinct from a
site-level cert problem) that a third identical HTTPS attempt would not
have, at the cost of one extra tool call rather than a wasted repeat.
Recommend keeping this as standard practice, not just a one-off experiment.

## What I could establish about kohaumotu.org *without* accessing it directly

Since direct access is blocked in this environment, I used web search and a
fetch of the third-party GitHub repository that already cites and uses this
source (`ipezygj/rongorongo-catalogue-audit`) — reading what a third party
says *about* an external source is citation-checking, not a corpus
download, so this stays inside the standing rule.

- **Maintainer:** Philip Spaelti maintains kohaumotu.org's rongorongo
  material, per multiple independent search results (kohaumotu.org's own
  page titles, e.g. "Philip Spaelti's Rongorongo pages").
- **What it is:** the site describes itself as hosting a mirror of the
  discontinued `rongorongo.org` site (last update reported as 2005/02/27),
  plus Spaelti's own Barthel-code documentation, a glyph library, an
  Englert/Rapa Nui dictionary, and a CEIPP-derived transliteration in XML
  format at `kohaumotu.org/Rongorongo/xml/` (note: this is a different path
  than the `/rongorongo_org/` path tried directly above — the site appears
  to have more than one section covering overlapping material, which
  itself needs disentangling if this source is ever selected).
- **License:** still **not established as rights-clear**. The clearest
  statement found (via the audit repo's own citation) is "as published
  there; cite CEIPP" — an attribution request, not a stated open license.
  This is a real, disclosed gap, not an assumption either way.
- **Reading-uncertainty preservation:** promising secondhand evidence only —
  the audit repo's own XML-parsing code is described as retaining "line
  breaks, lacunae, illegible and end markers" when it reads this data,
  which is the behavior SQ-1 requires (preserving uncertainty rather than
  silently resolving it) *if* that description is accurate and *if* the
  live site's current XML matches what that repo parsed. Neither is
  independently confirmed here.
- **Coverage:** the same audit repo reports using CEIPP-derived data across
  25 of the known rongorongo inscriptions, in three variant readings
  (1,897 / 633 / 125 sign-token types depending on which catalogue variant
  is applied) — consistent with last cycle's finding, now with an
  approximate object-coverage number attached.

None of this is a primary-source read of kohaumotu.org itself — it is
now a *better-sourced secondary account* than last cycle's (a named
maintainer, a described license gap, third-party-code evidence of
uncertainty-preservation), not a resolution. **Still blocked for direct
access from this environment specifically.**

## Provisional rongopy evaluation (per Meeting #1's fallback instruction)

Meeting #1's action item said: if kohaumotu.org stays unreachable after one
genuinely different access attempt, provisionally evaluate
`jgregoriods/rongopy` against the ambiguity-preservation requirement
instead of waiting further. Two genuinely different attempts (Wayback,
direct HTTP) both failed for two different reasons above, so that
condition is met. I fetched the repository's own README (not its data
files — no corpus data was pulled) via WebFetch:

- **License:** confirmed **GPL-3.0**, explicit and unambiguous — a clear
  advantage over kohaumotu.org's undocumented rights status above.
- **Encoding:** the README states directly: "The glyphs, originally
  transcribed using Barthel's (1958) catalogue, were converted into the
  encoding proposed by Horley (2021), which... simplifies the numerous
  ligatures in the catalogue to a set of about 130 basic glyphs." This
  confirms last cycle's characterization and, importantly, it is
  *self-disclosed* by the repository itself, not inferred by me.
- **Ambiguity/damage-marker preservation: still unresolved.** The README
  does not document whether damaged, illegible, or uncertain glyph readings
  are marked in the data or silently resolved during the Barthel-to-Horley
  conversion. Answering this needs inspection of the repository's actual
  data files (`glyphs.py`, `texts.py`, or a transcription file), which I am
  not pulling in this cycle — inspecting a README is not the same as
  bulk-downloading corpus data, and no explicit user authorization for
  pulling this repository's data files is recorded anywhere in this
  repo (checked `config/claude.md`, `CONTRIBUTING.md`, `data/README.md`,
  `config/sidequests.md` — all state the same standing restriction, none
  grant an exception for this specific source).

## Confirmed Findings bar — not cleared this cycle

Same disclosure as last cycle applies with equal force: everything above is
search-engine and AI-mediated fetch-summary evidence (of a README and of a
third party's description of an external site), not a primary text I read
directly or a reproducible script. `knowledge-base/state.md` is
intentionally left unchanged.

## Net effect on SQ-1

Neither candidate is selected yet, but the choice is now better-specified
rather than merely re-asked:

- kohaumotu.org/CEIPP: richer coverage (25 objects, multiple sign-inventory
  variants) and secondhand evidence of uncertainty-preservation, but an
  undocumented/unclear license and confirmed inaccessible from this
  environment specifically (proxy-level block, not just a cert issue).
- rongopy: clear open license and a self-disclosed, bounded simplification
  (collapsed ligatures to ~130 glyphs), but unresolved on
  ambiguity/damage-marker preservation without a data-file read that needs
  explicit user authorization first.

## Next step

1. Ask the user (recorded here so the next cycle doesn't lose it) whether
   they will grant explicit authorization to pull `jgregoriods/rongopy`'s
   data files (GPL-3.0, small, code-hosted, not raw tablet images) so its
   ambiguity-preservation behavior can actually be checked — this is the
   single cheapest remaining unblock on SQ-1's leading rights-clear
   candidate.
2. Separately, ask whether the user (or the auditor agent, if its
   environment reaches the open web differently) can check
   `kohaumotu.org/Rongorongo/xml/` directly, since this agent's own network
   egress proxy blocks the domain outright regardless of protocol or
   archive path.
3. Do not begin SQ-2 until one of these two resolves.
