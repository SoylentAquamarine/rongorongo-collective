# SQ-3 — PROPOSED normalized, direction-aware distance rule (for Research Director freeze; not yet frozen)

## Precommitment self-review (written before drafting)

**Known:** ChatGPT steering #55 (2026-11-12) found the frozen SQ-3 decision rule scores each measure
"closer" to the natural-language or khipu baseline but defines no common distance, normalization,
or tie/ambiguity handling across measures with different units. Its one next action is that the
Research Director freeze such rules before any corpus/OKR data is examined.

**Not done:** no rule is frozen. No rongorongo, OKR or natural-language data exists in this repo or
has been touched. This document is a PROPOSAL only; it has no authority until the Director freezes
or amends it (appended below, never edited in place).

**Design and why non-circular:** every constant below is fixed from the measure definitions alone
(no data in hand), so it cannot be tuned to a favorable outcome. Prediction (carried from the
2026-10-11 freeze, unchanged): rongorongo lands nearer the khipu/notation baseline on most measures.
The rule is built so that this can fail.

**Honesty precommitment:** design only; no result reported; if data later shows a rule flaw, correct
by appended amendment with disclosure, not silent edit.

## Proposed rule

For each measure m with rongorongo value R, natural-language value N, khipu value K (all at matched
token scale, computed by one shared script):

1. **Scale:** d_m = (R - N) / (K - N), i.e. position on the NL->khipu axis (0 = NL, 1 = khipu).
   Unit-free, so measures are comparable. Direction is automatic: the sign of (K-N) is absorbed.
2. **Degenerate axis:** if |K - N| < 2 * pooled bootstrap SE of (K - N) (bootstrap over matched-size
   resamples, 1,000 draws, fixed seed declared in advance), the measure is **non-discriminating**
   and scores neither side (reported as such, not dropped silently).
3. **Per-measure verdict:** d_m > 0.5 + 0.1 -> khipu-side; d_m < 0.5 - 0.1 -> NL-side; otherwise
   **ambiguous** (a 0.4-0.6 dead band; value chosen now, before data). Values outside [0,1] count
   toward the nearer pole and are flagged as "outside both baselines" (neither baseline fits).
4. **Aggregation:** with ambiguous/non-discriminating measures possible, majority is no longer
   guaranteed from 3. Report the per-measure d_m with bootstrap intervals always. A headline verdict
   is issued only if one side wins >= 2 measures AND the other wins 0; otherwise the headline is
   "mixed/undetermined". Entropy orders 1-3 are one measure (order-2 designated primary, orders 1,3 as
   sensitivity), so as to avoid triple-counting.
5. **Scale-matching:** all three corpora subsampled to the smallest token count, repeated with 100
   subsample draws; d_m reported as median with 5-95% range.
6. **Khipu field mapping** stays as the 2026-10-11 freeze requires: decided and stated before
   computing; if >1 plausible mapping, report all and apply the rule to each (ambiguity reported).

Standing disclosure unchanged: khipu is a comparator, not certified non-linguistic ground truth.
Cultural/rights terms (Rapa Nui rights-holders) govern corpus selection; none acquired.

## Open points for the Director
- Confirm or amend the 0.1 dead-band half-width and the 2xSE degeneracy threshold.
- Confirm entropy-order handling (order-2 primary).
