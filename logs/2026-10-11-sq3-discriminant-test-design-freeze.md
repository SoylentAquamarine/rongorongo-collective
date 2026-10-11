# SQ-3 — preregistered discriminant-test design (frozen before any data is touched)

## Precommitment self-review (written before drafting)

**Known:** SQ-3's own scope calls for falsifiable, held-out tests discriminating a full
writing system from a mnemonic/notation system, using SQ-2's atlas plus a comparator corpus.
The 2026-10-10 cycle found a real comparator candidate (the Open Khipu Repository, OKR) but
explicitly left "drafting the actual preregistered test design" as a separate, not-yet-attempted
piece of work — the next unclaimed thread in this project.

**Not done yet:** no test design has been written. Separately and independently: SQ-2's own
atlas has no real corpus content yet (only a synthetic schema round-trip check, per SQ-2's own
status) — real rongorongo data is still blocked on the standing corpus-content authorization
question. OKR itself has not been downloaded (treated as subject to this project's own
no-bulk-download-without-authorization discipline).

**Design and why it's non-circular:** freeze the test's predictions and decision rule now, while
no actual data (rongorongo or khipu) is in hand to fit the design to. This is the same
discipline the sibling projects use for their own mechanism tests, and is the correct order
specifically because it prevents a later, data-informed temptation to adjust what "counts" as a
pass. This document commits to specific, falsifiable numeric predictions before any analysis
is run.

**Prediction (stated before any data is examined):** per-glyph/n-gram entropy and compositional
recombination rate for the rongorongo corpus will land closer to the mnemonic/notation baseline
than to a natural-language baseline, consistent with this project's own standing skepticism
about rongorongo being full glottographic writing — but this is explicitly a prediction, not a
precommitted conclusion, and the design below is built to falsify it if the numbers say
otherwise.

**Honesty precommitment:** this document is a design only. No test is run, no data is touched,
and no result is reported in this log — reporting a result here before the design is actually
executed against real data would violate the test's own preregistration purpose.

## Test design

### Discriminating predictions (stated in `config/sidequests.md`'s own scope, restated precisely)

| Property | Full writing system (prediction) | Mnemonic/notation system (prediction) |
|---|---|---|
| Sign-inventory size | Large, semi-open | Smaller, closed |
| Sequence entropy (per-glyph, conditional on preceding N glyphs) | Roughly natural-language-like (high, with language-typical short-range structure) | Lower; heavy formulaic repetition |
| Recombination | Productive — signs combine in many distinct, non-repeating sequences | Repetitive — same sequences recur largely verbatim across different texts/objects |
| Structural locus | Structure tracks word/clause boundaries | Structure tracks recitation/performance units (e.g., repeated formulaic blocks), not word-for-word encoding |

### Measures (to be computed once data access exists)

1. **Sign-inventory size and growth curve** — type count vs. token count (a Heaps'-law-style
   curve); a closed mnemonic repertoire should plateau faster than an open/semi-open writing
   system's inventory.
2. **Conditional entropy** of glyph sequences at orders 1–3 (unigram, bigram, trigram), computed
   per-object and corpus-wide.
3. **Sequence-repetition rate** — the fraction of N-glyph runs (N = 3, 5, 8) that recur
   verbatim elsewhere in the corpus, corpus-wide and within-object.
4. **Baseline comparison corpora** (both required, per SQ-3's own scope — neither substitutes for
   the other):
   - A genuine natural-language corpus at matched token-count scale (candidate: a segment of
     one of this project family's own already-sourced historical-language comparator texts,
     scale-matched, not the full text, so the baseline doesn't simply have more data to be
     "more entropic" with).
   - OKR (khipu) at matched scale, computed over whichever of its encoded fields (cord
     sequence, knot type/direction/turns, per the schema in
     `logs/2026-10-10-sq3-khipu-comparator-candidate-identified.md`) is the closest structural
     analog to a glyph sequence — this mapping itself must be decided and stated before
     computing anything, not chosen after seeing which mapping produces a more favorable number.

### Decision rule (frozen now, before any measurement)

For each of measures 1–3, rongorongo's statistic is scored as closer to whichever baseline
(natural-language or khipu) it falls nearer to on that measure specifically. **No single
measure decides the outcome.** The test's conclusion is reported as whichever side wins a
majority of the three measures (2 of 3), with the per-measure breakdown always shown — a 2–1
split must be reported as a 2–1 split, not rounded to a clean verdict. A tie is impossible with
three measures, but if OKR's relevant field choice turns out to be ambiguous (more than one
plausible mapping with materially different results), that ambiguity itself must be reported
rather than resolved by picking the more convenient mapping.

### Standing disclosure required in any future result that uses this design

Per the 2026-10-10 log's own finding: khipu's status as genuinely non-linguistic is itself an
open scholarly question, not settled fact. Any report of this test's results must restate this
explicitly — khipu here functions as the best available comparator for a non-glottographic
recording system, not as a certified ground-truth label.

## What remains blocked (not attempted now, by design)

- SQ-2's real corpus content (still gated on the standing corpus-content authorization
  question).
- Downloading OKR (still treated cautiously under the no-bulk-download-without-authorization
  discipline this project applies to external corpora of this size, per the 2026-10-10 log).
- Selecting the scale-matched natural-language comparator text's specific excerpt.

This document exists so that when any of those three blockers clears, the test can run
immediately against a design that was fixed beforehand — the actual point of a design freeze.
