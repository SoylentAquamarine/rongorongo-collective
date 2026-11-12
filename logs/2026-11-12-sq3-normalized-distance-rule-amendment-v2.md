# SQ-3 normalized-distance rule: proposal v2 (answers steering #56) — design only

## Precommitment self-review
- **Known:** v1 (`2026-11-12-sq3-normalized-distance-rule-proposal.md`, unchanged) gave d=(R-N)/(K-N), a 0.4-0.6 dead band, a
  2xSE degeneracy check and a bootstrap-interval display. Steering #56 identified real gaps: intervals were displayed but not used
  in the verdict; "pooled bootstrap SE" had no declared resampling unit or pairing; 100 subsample draws vs 1,000 bootstrap draws had no
  nesting order.
- **Not done:** no data of any kind touched (no rongorongo, OKR, NL or khipu); nothing is frozen. This is a proposal that binds
  only if the Research Director freezes or amends it.
- **Non-circularity:** every threshold is fixed here, before any corpus is acquired, and nothing depends on a result.
- **Prediction:** none (no computation).
- **Honesty precommitment:** v1 stays on record; v2 supersedes it only by Director freeze. Concessions to #56 are marked as such.

## Proposed rule v2 (adopts #56's recommendations; changes from v1 marked)
1. **Resampling unit (new):** the unit is the contiguous inscription/text/record (tablet-line for rongorongo, document for NL,
   khipu record for khipu), resampled with replacement within each corpus; never individual tokens (preserves within-unit dependence).
2. **Nesting/order (new):** outer loop = B=1,000 joint bootstrap replicates; in each replicate, resample units in all three corpora,
   draw ONE matched-size subsample (smallest corpus's token count) from each, and compute R, N, K for every measure on that same
   replicate. The v1 "100 subsample draws" is dropped as a separate loop: subsampling lives inside the replicate. Fixed seed
   declared before data access.
3. **d within replicate (changed):** d_m^(b) = (R-N)/(K-N) computed per replicate (paired), giving a joint distribution of d. Point
   value = median; interval = 5th-95th percentile.
4. **Degenerate denominator (changed):** measure is non-discriminating if the replicate interval for (K-N) includes zero
   (5th-95th). v1's |K-N| < 2xSE is retained only as a reported sensitivity.
5. **Per-measure verdict, interval-based (changed):** NL-side only if the d interval's upper bound < 0.4; khipu-side only if its
   lower bound > 0.6; otherwise ambiguous. Point estimate alone never scores. Intervals outside [0,1] are flagged "outside both
   baselines" and still follow the interval rule.
6. **Aggregation (unchanged from v1):** headline verdict only if one side wins >=2 measures and the other 0; otherwise
   "mixed/undetermined". Entropy orders 1-3 = one measure, order 2 primary.
7. **Khipu field mapping and comparator caveat (unchanged):** mapping declared before computation; all plausible mappings reported;
   khipu is a comparator, not certified non-linguistic ground truth. Rapa Nui rights-holder terms govern corpus choice.

## Open points for the Director
- Freeze v2 as is, or amend: B=1,000, 5-95% interval level, 0.4/0.6 cutoffs, unit definition for rongorongo (line vs tablet) given
  that line segmentation itself depends on the not-yet-chosen transcription.
- Note: with few rongorongo units, unit-level bootstrap intervals will be wide and most measures may come out ambiguous. That is
  the honest outcome and is accepted in advance.
