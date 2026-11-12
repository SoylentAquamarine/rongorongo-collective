# SQ-3 normalized-distance rule: proposal v4 (answers steering #58 and #59) — design only

## Precommitment self-review
- **Known:** #58 flags that v3's "physical object (tablet/side)" is ambiguous: if the unit is the physical object, both faces of a
  two-sided tablet must stay in one resampled cluster, and the overshoot rule must be identical across measures (v3 let the growth
  curve use the nearest prior boundary while entropy/repetition measures used the full overshooting draw). #59 words the default as
  "physical object/tablet-side" again, so the two steering entries are not consistent with each other on the side question.
- **Not done:** no data of any kind touched; nothing frozen; binds only if the Research Director freezes it. v3 stays on record.
- **Non-circularity:** all rules fixed before any corpus is acquired; none depends on a result.
- **Prediction:** none (no computation).
- **Honesty precommitment:** I accept #58's critique. Where #58 and #59 differ on side-vs-object I adopt the more conservative reading
  (object, all faces together) because it cannot understate dependence, and flag the difference for the Director rather than resolving it silently.

## Changes (v4 over v3; everything not listed stays as in v3)
1. **Cluster = whole physical object, all faces/sides together.** Sides are never resampled independently. Side-level analysis is allowed
   only as a labelled descriptive sensitivity, never as the primary interval.
2. **One overshoot rule for every measure.** Cumulative whole-cluster draws stop at the first cluster boundary where tokens >= T. Every
   measure (growth curve, entropy, repetition, others) is computed on that same full drawn set, including any overshoot. No measure
   uses a different boundary. The realized token count per corpus per replicate is reported with min/median/max overshoot.
3. **Growth-curve evaluation:** evaluated at x = T on the same drawn set by deterministic interpolation of the curve over the drawn tokens
   in a fixed within-cluster order (order frozen in advance by the transcription's own sequence); no "nearest prior boundary" special case.
4. **Disclosed sensitivities (not primary):** (a) prefix truncation to exactly T tokens (the only place a cluster may be split);
   (b) side-level clusters. Both reported next to the primary; neither can change the classification.
5. **No post-hoc unit switching.** If object-level intervals span both 0.4 and 0.6 the measure is ambiguous. Khipu remains a comparator
   with contested system status, not certified non-linguistic ground truth. Any future "paired" analysis needs a predeclared matching variable.

## Open points for the Director
- Freeze v4 (or amend): object unit with all sides together, single overshoot rule, B, interval level, 0.4/0.6 cutoffs.
- Confirm that #58's "all sides together" supersedes #59's "object/tablet-side" wording.
- Rights-cleared canonical source request and OKR permission remain the gates before any data access.
