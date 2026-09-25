# 2026-09-25 (later cycle) — rongopy encoding-scheme inspection: ambiguity
preservation and object-coverage detail (Claude)

**Sidequest:** `config/sidequests.md` SQ-1 — corpus canonicalization
(blocking). Directly answers the specific blocker named at the end of
`logs/2026-09-23-sq1-kohaumotu-access-followup.md` and reaffirmed in
`logs/2026-09-25-sq1-network-scope-diagnosis-and-citation-refinement.md`:
"rongopy's ambiguity-preservation check ... needs a look at its actual data
files" / "still needs explicit user authorization to pull its data files,
which remains unrecorded anywhere in this repo."

**Method, precisely stated:** this session's network egress policy is
unchanged from the immediately preceding cycle — re-tested directly
(`curl` to `www.persee.fr`, `WebFetch` on `persee.fr` and `arxiv.org`) and
got the identical `EGRESS_BLOCKED` / `403` result on every non-GitHub
scholarly domain tried, confirming (not re-diagnosing) the prior cycle's
conclusion. No further time was spent retrying blocked domains, per that
log's own "closed, not a retry candidate" instruction.

Instead of a repository clone (which is the specific action Round 3 of
`comms/FromClaudeToChatGPT.md` flagged as needing explicit user
authorization, and which is still unrecorded anywhere in this repo), this
cycle used the `WebFetch` tool — read-only, no repository added, nothing
cloned or saved to disk — to fetch and AI-summarize exactly **two** public
GitHub pages/files:

1. `https://github.com/jgregoriods/rongopy/blob/master/horley_encoding.py`
   — a single source-code file: the Python dictionary that maps Barthel-
   catalogue codes to Horley's (2021) simplified glyph codes. This is the
   *encoding scheme itself* (a codebook), not a per-tablet transcribed
   text, and is the one file that could actually answer the
   ambiguity-preservation question.
2. `https://github.com/jgregoriods/rongopy#readme` (the rendered README).

**This is explicitly narrower than "pulling rongopy's data files."** The
`data/` directory (the actual corpus content — glyph sequences per tablet
and line) was not fetched, read, or downloaded. The open authorization
question from Round 3 (whether pulling the corpus-content data files counts
as the kind of "bulk download" the standing rule is meant to prevent)
remains genuinely open and is **not** resolved by this cycle's work — it is
carried forward unchanged, see "Still open" below.

## Finding 1 — `horley_encoding.py` does mark uncertain/illegible readings

The `WebFetch`-mediated summary of the file (quoted from the tool's return,
not independently re-verified byte-for-byte) reports:

- `'?'` used as a placeholder for a single illegible/uncertain glyph, e.g.
  `'85': '?'`, `'119': '?'`.
- `'? ?'` used for a run of two uncertain glyphs, e.g. `'105': '? ?'`,
  `'112': '? ?'`, `'130': '? ?'`.
- At least one embedded partial-uncertainty case within an otherwise known
  sequence: `'162': '4 ?'`.
- At least one mixed known/unknown pair: `'233': '? 230'`.
- At least one apparently empty/absent entry: `'199': ''`.
- The tool separately flagged what it read as an inconsistency between two
  entries it labeled `'470'` (one showing `'670'`, another `'? ?'`) —
  recorded here as-returned; this specific point needs a direct,
  non-AI-mediated read to confirm it isn't a tool transcription artifact
  (e.g. two different keys formatted similarly) before being relied on.
- The tool reports the file itself has no comments or docstrings
  explaining the scheme — so this reading is inferred from the data
  values, not from an author's own stated documentation.

**Disclosure, per `methods/falsification-standard.md`:** this is a
`WebFetch`-tool AI-mediated summary of one file's contents, not a direct
byte-level read by this agent and not a reproducible script output. It is
evidence, not a Confirmed Finding. It should not be promoted to
`knowledge-base/state.md`'s Confirmed Findings section. It is, however,
materially more informative than the prior "unconfirmed, README doesn't
say" status: **rongopy's encoding does appear to have an explicit mechanism
for marking uncertain/illegible glyphs**, which was the specific open
question blocking a decision on this candidate's ambiguity-preservation
requirement. A direct verification (reading the raw file text without an
AI-summarization intermediary, e.g. once repo access is authorized, or by
the auditor from an environment that can browse it directly) is the
obvious next confirming step, not yet done.

## Finding 2 — object-coverage detail newly quoted from the README

Fetched sentences (quoted by the tool from the rendered README, disclosed
as the same AI-mediated-summary tier as above):

> "The canonical RoR corpus is comprised of texts carved on 20 wooden
> tablets, one staff, two *reimiro* (pectoral adornments), one birdman
> sculpture (*tagata manu*), and one snuffbox (assembled from an earlier
> tablet)."

> "A bark-cloth fragment has recently been recognized as another genuine
> inscription (Schoch and Melka 2019)."

Arithmetic check (mine, not the source's): 20 + 1 + 2 + 1 + 1 = 25 objects
in the "canonical" set as stated, +1 for the separately-mentioned
bark-cloth fragment = 26. This is a new, more granular data point bearing
on the already-logged 26-vs-27 surviving-object-count disagreement
(Lastilla et al. 2022 "26" vs. Horley 2021 "27" A–Z+#A labelling,
`knowledge-base/state.md` Open Questions / `logs/2026-09-23-sq1-corpus-
source-survey.md`). It is **consistent with the "26" side** of that
disagreement as read here, but this is a tertiary citation (rongopy's
README paraphrasing Horley 2021) fetched via AI summary, not a primary
read of Horley (2021) itself, and the object breakdown given (20+1+2+1+1)
does not obviously reconcile with "27" under Horley's own labelling
scheme as previously reported — so this narrows but does not resolve the
discrepancy. Recorded as a new, explicitly disclosed data point in
`knowledge-base/state.md` Open Questions, not a resolution.

License: the README's footer confirms **GPL-3.0**, consistent with every
prior cycle's finding. A direct fetch of `LICENSE` at
`github.com/jgregoriods/rongopy/blob/master/LICENSE` 404'd (path/name
mismatch, not investigated further this cycle since the footer badge
already gives an unambiguous answer, and the README text itself does not
say a separate `LICENSE` file's contents differ).

## Net effect on SQ-1

Given (1) `kohaumotu.org` is confirmed unreachable from every environment
available to this project so far, has an unresolved, non-open license
("cite CEIPP" only), and no independently confirmed ambiguity-preservation
either; and (2) `rongopy` now has a clear GPL-3.0 license, a self-disclosed
encoding simplification (Barthel to Horley's ~130-basic-glyph scheme,
already logged), and — new this cycle — apparent, though not yet
independently-verified, ambiguity preservation via `?` markers, this cycle
recommends **provisionally selecting `rongopy` as SQ-1's working source**,
recorded in `config/sidequests.md` with that status label (provisional,
not final), rather than continuing to wait on `kohaumotu.org`.

This does **not** mean the corpus-content data files may now be pulled —
that authorization question is unchanged and still open (see below). It
means source *selection* (which candidate to build toward, pending that
authorization or a direct/non-AI-mediated verification) can proceed, which
unblocks writing SQ-1's comparison writeup and SQ-2's planned schema
around rongopy's structure specifically, without yet touching corpus
content.

## Still open (unchanged by this cycle)

1. Whether pulling `rongopy`'s actual corpus-content data files (as
   opposed to the encoding-scheme file inspected here) needs explicit user
   authorization, and whether that authorization is in scope of the
   standing "no bulk download of corpus datasets" rule or a reasonable
   exception for a small, already GPL-3.0-licensed, non-image dataset —
   this is a policy question for the user, not one this session can settle
   for itself. Still unrecorded anywhere in this repo as of this entry.
2. A direct, non-AI-mediated verification of `horley_encoding.py`'s exact
   contents (confirming Finding 1 above byte-for-byte, and resolving the
   flagged `'470'` inconsistency) once repo access is authorized or from
   an environment/party that can browse GitHub directly without a
   summarization intermediary.
3. `persee.fr` / Guy (1990) primary read: still blocked, unchanged, per
   the immediately preceding log.

## Next step

1. Update `config/sidequests.md` SQ-1 status to "provisionally selected:
   rongopy" with the caveats above (done, same commit as this log).
2. Add the new object-coverage data point to `knowledge-base/state.md`
   Open Questions, disclosed as tertiary/AI-summary tier (done, same
   commit).
3. Whoever runs the next cycle: raise the corpus-content-data-file
   authorization question to the user explicitly (this session has no
   interactive channel to do so this cycle) before pulling any actual
   `rongopy` transcription content; in the meantime SQ-2 schema design can
   proceed structurally (field names, how to represent a `?`-marked
   uncertain glyph) without needing the content itself yet.
