# SQ-3 normalized-distance rule: Director freeze of v4 (design-only; no data, no code)

## Precommitment self-review
- **Known:** steering #58-#61 ask the Research Director to freeze or amend v4. v4 (logs/2026-11-12-sq3-normalized-distance-rule-amendment-v4.md) already fixes cluster, overshoot rule, growth-curve evaluation and disclosed sensitivities; B, interval level and cutoffs are carried from v2/v3.
- **Not done:** no corpus acquired, no canonical transcription chosen, no OKR permission, no code. This freeze does not authorize any of those.
- **Non-circularity:** every value below was fixed before any corpus access and cites no result.
- **Prediction:** none (no computation).
- **Honesty precommitment:** the freeze may be amended only by a dated append-only amendment made before data access; any change after data access is reported as a deviation. Most measures are expected to come out ambiguous (about 26-27 objects); that outcome is accepted and is not a reason to change unit afterward.

## Frozen (acting as Research Director, per config/research-department.md)
1. Primary cluster = whole physical object, all faces/sides together (#58 supersedes #59's "object/tablet-side" wording).
2. One overshoot rule for every measure: draw whole clusters with replacement until cumulative tokens >= T (T = smallest corpus), no splitting; all measures computed on that full drawn set; report min/median/max overshoot.
3. Growth-curve evaluated at x = T by deterministic interpolation in a fixed within-cluster order; no nearest-prior-boundary special case.
4. B = 1,000 replicates; the three corpora resampled independently; interval = 5th-95th percentile of d = (R-N)/(K-N), read as a bootstrap, not paired.
5. Cutoffs: NL-side if upper bound < 0.4; khipu-side if lower bound > 0.6; else ambiguous; degenerate if the K-N interval includes zero.
6. Disclosed sensitivities only (cannot change classification): prefix truncation to exactly T; side-level clusters.
7. NL unit = document; khipu unit = record. Khipu stays a comparator with contested system status, not ground truth. "Paired" is reserved for a future predeclared matching variable.

## Still gating any execution
Rights-cleared canonical rongorongo source, OKR permission, and written canonical-transcription choice. Until all three exist, nothing is run; this freeze alone moves no result.
