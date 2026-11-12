# SQ-3 normalized-distance rule: proposal v3 (answers steering #57 addendum, bootstrap pairing audit) — design only

## Precommitment self-review
- **Known:** v2 (`...amendment-v2.md`, unchanged on record) called its procedure a "joint paired bootstrap." The #57 addendum points
  out that the three corpora (rongorongo, natural-language documents, khipu records) have no defined cross-corpus matched units, so
  sharing a replicate index does not make observations paired. It also asks how the matched-token budget is met without splitting the
  cluster unit, and says "tablet-line" should not be the rongorongo unit before segmentation is frozen.
- **Not done:** no data of any kind touched (no rongorongo, OKR, NL or khipu); nothing is frozen; binds only if the Research Director
  freezes or amends it.
- **Non-circularity:** every rule below is fixed before any corpus is acquired and depends on no result.
- **Prediction:** none (no computation).
- **Honesty precommitment:** I agree with the critique. "Paired" was a mislabel in v2, not a design feature; v2 stays on record and is
  superseded only by Director freeze.

## Proposed changes (v3 over v2; everything not listed stays as in v2)
1. **Name and structure (corrected):** the procedure is a *joint analysis with independent within-corpus cluster resampling*. In each
   of B=1,000 replicates, the rongorongo, NL and khipu corpora are resampled independently of each other. The same three resampled
   sets are reused for all measures, which preserves within-corpus covariance across measures. d_m^(b) = (R-N)/(K-N) is a function of
   three independent draws; its replicate distribution is read as a bootstrap distribution, not a paired one. The word "paired" is
   reserved for a future, predeclared genuine matching scheme (none exists now).
2. **Matched-token budget without splitting clusters (new):** T = total token count of the smallest corpus. In each replicate and
   corpus, draw whole clusters with replacement until cumulative tokens first reach >= T, then stop. No cluster is split. Realized
   token counts per corpus per replicate are recorded and reported (overshoot is at most one cluster). Measures that depend on
   sample size (sign-inventory growth) are read from the growth curve at a fixed cumulative-token x declared in advance
   (x = T, using the clusters in draw order, which can only reach x at a cluster boundary or beyond; if a draw reaches x mid-cluster the
   curve is evaluated at the nearest prior boundary and the shortfall is reported). Sensitivity, reported alongside and not primary: a
   prefix truncation to exactly T tokens, disclosed as the one place a cluster may be split.
3. **Rongorongo unit (changed):** until a transcription and its segmentation are frozen, the declared default cluster is the physical
   object (tablet/side), the only unit stable across Barthel-type, Lastilla-type and other transcriptions. Line or sub-line units
   become eligible only after the Director freezes a segmentation, and must then be named in the freeze entry. NL unit = document;
   khipu unit = record, as before.
4. **Interval classification and degeneracy (unchanged from v2):** NL-side if the d interval's upper bound < 0.4; khipu-side if its
   lower bound > 0.6; otherwise ambiguous; degenerate if the K-N interval includes zero.
5. **Expected consequence (disclosed in advance):** with only about 26-27 rongorongo objects, object-level resampling yields wide
   intervals, so most measures will probably be classified ambiguous. That is the accepted honest outcome; it is not a reason to
   switch to a finer unit after seeing data.

## Open points for the Director
- Freeze v3 or amend: B, interval level, 0.4/0.6 cutoffs, object-level unit, no-split draw rule vs truncation as primary.
- Whether a genuinely matched design (e.g. length-stratified or genre-stratified matching) is wanted; if so it must be specified,
  with its matching variable, before any data access.
