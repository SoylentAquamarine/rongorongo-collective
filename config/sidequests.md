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
examples cross-checked against published catalog images.

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
