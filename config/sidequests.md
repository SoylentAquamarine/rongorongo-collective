# Translation-oriented sidequest queue

Sidequests are bounded, achievable pieces of work. Each must produce a
reusable artifact, answer a decision, or remove a named blocker. The lead
agent may reprioritize them, but should record why.

## SQ-1 — Corpus canonicalization (blocking, start here)

**Purpose:** unlike the Voynich manuscript, rongorongo has no single
already-agreed, machine-readable transcription this project can simply
adopt on day one. This sidequest is not optional groundwork — it blocks
every other sidequest and the entire Statistician/Linguist/Cryptanalyst
track.

**Scope:** identify and evaluate candidate digital transcriptions or
catalogs of the rongorongo corpus (glyph-by-glyph, using a documented
reference numbering such as Barthel's 1958 catalog or a successor), the same
way `comms/` Round 1 of the Voynich project evaluated and selected ZL3b over
alternative EVA files. Record, for each candidate: source, license/rights,
retrieval method, coverage (how many of the ~25ish surviving inscribed
objects it transcribes, at what completeness), whether it preserves reading
uncertainty/damage the way IVTFF/EVA does for Voynich rather than silently
resolving it, and a checksum once pulled. Do not bulk-download anything
without explicit user authorization — this is a standing rule across both
sibling projects.

**Deliverables:** a source-comparison writeup (mirroring
`sq3-source-discovery-candidates.md`'s format in the sibling project),
a provenance file once a source is selected, and a normalization script with
a full ambiguity-audit trail once normalization begins.

**Stepping-stone value:** nothing downstream (glyph frequency, sequence
structure, held-out tests) is reproducible or falsifiable without this.

**Laptop/worker-node work:** none yet — this stage is source discovery and
licensing/provenance research, not computation.

**Status (2026-09-23, Claude):** first real source survey done — see
`logs/2026-09-23-sq1-corpus-source-survey.md` for full detail and citations.
Live web search/fetch (not simulated), no data downloaded or committed, per
this sidequest's own standing rule.

Two concrete, rights-clear digital candidates identified, neither yet
selected:
- `jgregoriods/rongopy` (GitHub, GPL-3.0) — a digital transcription using
  Horley's (2021) simplified ~130-basic-glyph encoding, plus comparison
  Rapa Nui recitation texts and a cross-tablet parallel-sequence catalog.
  Most immediately actionable candidate, but its glyph encoding is
  *simplified* (collapses ligature variation), which needs to be weighed
  against this sidequest's requirement to preserve reading uncertainty
  rather than silently resolve it.
- The INSCRIBE project (University of Bologna, ERC 771127) — highest-rigor
  methodology found (structured-light scanning + photogrammetry), with a
  peer-reviewed open-access new transcription of the Échancrée tablet
  (Lastilla, Ravanelli, Valério & Ferrara 2022, *Digital Scholarship in the
  Humanities* 37(2)). Covers 1 of the ~26–27 known objects so far, not a
  full-corpus candidate yet — worth tracking, not selecting.

A third, previously-unverified lead — a CEIPP-derived XML transliteration
apparently hosted at `kohaumotu.org/rongorongo_org/` — is real (a third-party
GitHub research repo, `ipezygj/rongorongo-catalogue-audit`, actively cites
and uses it) but I could not access it myself: both fetch attempts failed
with an expired TLS certificate. This is the most promising lead and also
the most concretely blocked one — needs a follow-up access attempt from a
different network/browser or the Wayback Machine before being ruled in or
out.

Fact-check side quest also resolved partially: Barthel (1958) as the
standard glyph-numbering system is confirmed by consistent secondary-source
agreement (not primary-read). The "mid-20s surviving objects" scaffold
language is directionally right but the precise count is a genuine,
citable disagreement between sources (26 per Lastilla et al. 2022 vs. 27
per Horley 2021's A–Z+#A labelling) — left as an open question rather than
silently rounded to one number.

No source has been selected yet. SQ-2 remains blocked. Next concrete step:
resolve the kohaumotu.org access question, then evaluate `rongopy`'s
encoding against the ambiguity-preservation requirement.

**Status update (2026-09-23, later same day, Claude):** attempted two
genuinely different kohaumotu.org access paths (Wayback Machine; direct
HTTP) instead of repeating the same HTTPS fetch — see
`logs/2026-09-23-sq1-kohaumotu-access-followup.md`. Both failed, but more
informatively than before: this specific agent environment's network
egress proxy blocks the `kohaumotu.org` domain outright (not the
previously-assumed expired-certificate issue, which may or may not still
be true of the site itself). Via citation-checking only (web search plus
reading a third-party GitHub repo that already uses this source, not
fetching kohaumotu.org itself), learned it is maintained by Philip Spaelti,
covers ~25 inscriptions across three CEIPP sign-inventory variants, and —
new, disclosed concern — has **no clearly stated open license**, only a
"cite CEIPP" attribution request. This weakens its "rights-clear" framing
from the first survey; it is real and substantial but its rights status is
now an open question, not an assumption in its favor.

Per the standing fallback (evaluate `rongopy` if kohaumotu.org stays
blocked), fetched `rongopy`'s own README: confirmed **GPL-3.0** (clear,
unlike kohaumotu.org) and confirmed the self-disclosed simplification
(Barthel catalogue converted to Horley 2021's ~130-basic-glyph scheme). Its
ambiguity/damage-marker preservation is still unconfirmed — the README
doesn't say, and checking would require reading its actual data files,
which were **not** pulled: no explicit user authorization for that is
recorded anywhere in this repo. This is now the single named blocker on
completing SQ-1's source-comparison writeup; see the log's "Next step" for
the two concrete asks (rongopy data-file pull authorization; independent
kohaumotu.org access check from a different environment).

**Status update (2026-09-25, Claude):** ran the "independent access check"
ask above, but from *this same* agent environment rather than a different
one — with a corrected result. Direct HTTPS probes of several unrelated
scholarly domains (`en.wikipedia.org`, `persee.fr`, `journals.openedition.org`,
`archive.org`, `jstor.org`, `academic.oup.com`, `researchgate.net`,
`books.google.com`) all failed identically to kohaumotu.org
("`CONNECT tunnel failed, response 403`" / organization policy), while
`github.com` and package registries remain reachable. See
`logs/2026-09-25-sq1-network-scope-diagnosis-and-citation-refinement.md`
for the full test. **This means kohaumotu.org's inaccessibility here is a
general environment network policy, not a site-specific block** —
superseding the prior cycle's diagnosis. Retrying kohaumotu.org again from
this same environment would not help; the real unblock is the environment
operator widening the network allowlist (or the auditor agent/user
checking from an environment that already has broader access).

Separately, used the still-functional `WebSearch` tool (search-summary
tier only) to sharpen two citations relevant to SQ-1/SQ-2: Guy (1990)'s
exact venue and page range for the Mamari lunar-calendar reading, and a
newly surfaced three-way disagreement across secondary sources on Barthel
(1958)'s total sign-catalog size ("632" / "599" / "638 of 800"). Neither
is a primary-source read; both are now recorded, disclosed as such, in
`knowledge-base/state.md` Open Questions and the same log above.

SQ-1 source selection is still not made. Next concrete step unchanged from
before: obtain user authorization to inspect `rongopy`'s actual data files
(GPL-3.0, code-hosted, not raw tablet imagery) for ambiguity-preservation,
since kohaumotu.org access is not going to resolve from within this kind
of environment without a network-policy change.

**Status update (2026-09-25, later same day, Claude) — provisional source
selection: rongopy.** Without cloning the repository or pulling its
corpus-content data files (the open authorization question below is still
unresolved), inspected two public GitHub pages via the `WebFetch` tool
(AI-mediated summary tier, disclosed as such — not a direct byte read or a
reproducible script): the `horley_encoding.py` source file (the
Barthel-to-Horley code-mapping table, i.e. the encoding *scheme*, not a
transcribed text) and the rendered README. Full detail, exact quotes, and
disclosure in
`logs/2026-09-25-sq1-rongopy-encoding-ambiguity-check.md`.

Result: `horley_encoding.py` appears to mark uncertain/illegible glyphs
explicitly (`'?'` for one unknown glyph, `'? ?'` for a run of two, at least
one embedded partial-uncertainty case, at least one empty entry) rather
than silently resolving them — this directly answers the
ambiguity-preservation question that has blocked source selection since
Round 2. One apparent internal inconsistency the summarization tool
flagged (`'470'`) still needs a direct, non-AI-mediated confirmation. The
README also newly gives a specific object-count breakdown (20 tablets + 1
staff + 2 reimiro + 1 birdman sculpture + 1 snuffbox = 25, + a recently
recognized bark-cloth fragment = 26, per Horley 2021 as cited there) — a
new data point on the existing 26-vs-27 count disagreement, added to
`knowledge-base/state.md` Open Questions rather than resolving it.

Given this, plus `kohaumotu.org`'s continued unreachability, unclear
license, and unconfirmed ambiguity-handling, **`rongopy` is now the
provisionally selected SQ-1 source** — provisional because (a) Finding 1
above is AI-summary tier, not yet independently confirmed byte-for-byte,
and (b) actual corpus-content data has still not been inspected pending
the unresolved authorization question (see immediately below). This
unblocks SQ-2 *schema* design (e.g., deciding how to represent a
`?`-marked uncertain glyph in the atlas) without yet requiring corpus
content itself.

**Still-open blocker, unchanged:** whether pulling `rongopy`'s actual
corpus-content data files (as opposed to the single encoding-scheme file
inspected this cycle) needs explicit user authorization under the
standing "no bulk download of corpus datasets" rule, or is a reasonable
exception for a small, already GPL-3.0-licensed, non-image dataset. This
remains unrecorded anywhere in this repo and is the single named blocker
on moving from "provisionally selected" to "selected, with provenance
recorded" per this sidequest's own deliverable checklist.

## SQ-2 — Glyph and compound-sign atlas

**Purpose:** build the smallest data layer needed to test structural
hypotheses: which glyphs exist, which compound/ligature signs recur, and
where they occur (object, line, position within line, relative to the
reverse-boustrophedon rotation).

**Scope:** using SQ-1's canonicalized corpus, inventory distinct glyph types
against their reference catalog numbers, tag known recurring compound
sequences (e.g. the sequence commonly discussed as a lunar-calendar-like run
on the Mamari tablet — verify this specific claim against a primary source
before relying on it, per the falsification standard), and record per-line
and per-object metadata (object identifier, estimated carver/hand if
documented, orientation).

**Deliverables:** checksummed glyph inventory table, extraction/validation
script, a missing-data report, and a small number of manually verified
examples cross-checked against published catalog images. Per ChatGPT's
direct byte-level read of `rongopy`'s `horley_encoding.py` (Round 1,
`comms/FromChatGPTToClaude.md`, GitHub blob SHA `9bbabb626f44251d42545faa72adbb9cf01cf421`
— 638 mapping entries, 57 with `?`, 118 many-to-one Barthel→Horley
collapses, one empty case `'199': ''`), the atlas table's schema must
include, per glyph row: `original_glyph_id` (the source Barthel ID,
preserved even where Horley collapses multiple Barthel IDs to one output),
`mapped_value` (the Horley-scheme output), `uncertain_flag` (true for any
`?`-marked entry), and `empty_mapping_flag` (true for the `'199'` case and
any other empty-output entry) — so the many-to-one Barthel→Horley collapse
is never silently lossy in the atlas itself, even if Horley is ultimately
selected as the working representation for other purposes. A losslessness
spot check against explicitly permitted rows is required before selecting
`rongopy`'s encoding as canonical for this sidequest, not just provisional.

**Update (2026-09-26):** a synthetic round-trip check of this four-field schema (per ChatGPT's
proposed next step, Round 2, `comms/FromClaudeToChatGPT.md`) confirms it is lossless for the two
pinned cases from `horley_encoding.py`: the `'17'`/`'18'` many-to-one collapse and the `'199'`
empty mapping both round-trip correctly — every `original_glyph_id` is uniquely recoverable even
where `mapped_value` collapses two different originals to one value. Script:
`data/scripts/sq2_schema_roundtrip_check.py`. This is a synthetic-data schema check only — it does
not touch any actual corpus content and does not resolve the still-open corpus-content
authorization blocker above.

**Stepping-stone value:** the direct analog of the Voynich project's label
atlas — the smallest layer needed to test whether recurring signs track
repeated concepts, objects, or positions, one of the cleanest available
paths to meaning.

**Laptop/worker-node work:** parsing, glyph/compound clustering,
duplicate and near-duplicate sequence calculations.

## SQ-3 — Writing-system-type discriminant tests

**Purpose:** rongorongo's central open question is not "which language" but
"what kind of system is this at all" — full glottographic writing,
mnemonic/semasiographic notation (recording content without encoding
language word-for-word, as proposed for some other early notation systems),
or some mixture. This sidequest designs falsifiable, held-out tests that
could discriminate between these before any specific-language decipherment
attempt is warranted.

**Scope:** using SQ-2's atlas, test predictions that differ between a full
writing system (expects roughly natural-language-like entropy, productive
recombination, a large semi-open sign inventory used compositionally) and a
mnemonic/notation system (expects a smaller closed repertoire, heavy
formulaic repetition, structure tied to recitation/performance rather than
word-for-word encoding). Freeze each test's design and decision rule before
looking at results, the same discipline the sibling project uses for its
own mechanism tests.

**Deliverables:** preregistration per test, held-out scores, comparison
against typologically appropriate baselines (a genuine written language
corpus at matched scale, and a known non-linguistic mnemonic/tally system
if a suitable digitized comparator exists), and a plain-English
interpretation.

**Stepping-stone value:** answers a genuinely prior question — attempting a
language-decipherment pipeline before this is settled risks repeating the
documented failure mode in rongorongo's own research history (pattern-
matching a handful of signs to a story without corpus-wide validation).

**Laptop/worker-node work:** entropy/n-gram analysis, permutation controls,
comparison-corpus assembly and sensitivity runs.

## SQ-4 — Historical recovery benchmark

**Purpose:** learn which analysis methods can actually recover meaning from
plausible comparator systems (other early or non-standard writing/notation
systems with an independently known reading) before trusting any method on
rongorongo, which has no known answer key. Directly modeled on the sibling
project's SQ-3.

**Scope:** assemble a small checksummed panel of comparator material with
documented, independently verifiable readings — candidates to evaluate
include other proto-writing or early notational systems with scholarly
consensus readings, and, if a genuinely accepted partial rongorongo reading
exists and can be verified against a primary source (e.g. the lunar-calendar
claim named in SQ-2), that reading itself as a held-out internal
recovery benchmark. Hide the reading from the recovery stage and measure
how much can be recovered blind.

**Deliverables:** source manifest and licenses, reproducible recovery
methodology, blind recovery tasks, accuracy measures, and a record of
methods that fail.

**Stepping-stone value:** validates or eliminates decipherment techniques
before they are trusted on a corpus with no known answer key — exactly the
role the sibling project's SQ-3 (Naibbe cipher, historical recovery panel)
played for Voynich mechanism candidates.

**Laptop/worker-node work:** corpus preprocessing, transform sweeps,
candidate scoring, robustness tests.

## Initial priority

Start SQ-1 first — it is a hard blocker, unlike the Voynich project where a
canonical corpus already existed at launch. Do not begin SQ-2 until a
source is selected and provenance is recorded. SQ-3 (writing-system-type
tests) should begin as soon as SQ-2's atlas exists, since it is the most
consequential open question and gates whether any subsequent
language-specific decipherment attempt is well-motivated at all. SQ-4 can
begin in parallel with SQ-1/SQ-2 (comparator-source discovery does not
depend on the rongorongo corpus itself being ready) without competing with
the primary task.
