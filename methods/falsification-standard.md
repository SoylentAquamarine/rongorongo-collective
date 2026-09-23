# Falsification and Promotion Standard

This is the minimum bar for moving an interpretation into **Active
Hypotheses**. It is deliberately stricter than the bar for recording a
measurement in **Confirmed Findings**. A measurement can be reliable while
supporting several incompatible explanations.

## Minimum bar for Confirmed Findings

Confirmed Findings is a much lower bar than Active Hypotheses — a
measurement or result, not an interpretation, and it doesn't need
alternatives explicitly ruled out. But every entry should still be well
documented and reproducible, not left to habit. Before a PR adds a bullet
to `knowledge-base/state.md`'s Confirmed Findings, it should have:

- a script, a manifest, or a directly-read and cited image/text protocol
  that produced the number or claim — not a description of a result
  alone, with nothing behind it a reader could rerun;
- the actual output (a summary JSON, a report, or both) committed to the
  repo, not only quoted or paraphrased inline in the bullet;
- enough provenance (source commit, checksum, seed, sample definition)
  that a third party could rerun it and reasonably expect the same
  result;
- for anything resting on an external secondary source (a search-engine
  summary, a paper or catalog not read directly), an explicit disclosure
  of that limitation in the same entry — never presented as if it were
  independently verified when it wasn't. This applies with particular force
  here: much of what is "commonly cited" about rongorongo in casual
  secondary sources is itself contested or imprecise in the primary
  scholarly literature (surviving object counts, glyph counts, and specific
  decipherment claims all vary by source), so a claim's provenance chain
  matters more than usual.

This does not require independent adversarial review the way Active
Hypotheses does — that remains the harder bar. It requires that a
Confirmed Finding always be *checkable*, even when no one has checked it
yet.

## Required hypothesis card

Before running its decisive test, the proponent must record:

1. **Claim** — one operational statement narrow enough to fail.
2. **Alternatives** — at least the strongest natural-language,
   mnemonic/notation-system, and post-contact/stimulus-diffusion
   explanations that fit the same observation, or a reason one family is
   inapplicable.
3. **Discriminating prediction** — an outcome expected under the claim and
   not equally expected under the named alternatives.
4. **Failure condition** — a numerical threshold, held-out pattern, or
   image/catalog mismatch that would count against the claim. This may not
   be invented after seeing the result.
5. **Units and controls** — the objects, sequences, glyphs, metadata
   fields, comparison corpora, exclusions, and randomization unit.
6. **Dependencies** — transcription, catalog-numbering, sequence
   segmentation, object-attribution, and carver/hand assumptions that could
   manufacture the result.

## Evidence required for promotion

A candidate can enter **Active Hypotheses** only when all of the following
are present:

- a reproducible script or a cited, inspectable image/catalog protocol;
- an effect size and uncertainty or an equally explicit qualitative
  decision rule, not only a p-value;
- a negative or shuffled control appropriate to the claim;
- sensitivity to at least the material transcription/segmentation and
  object/carver confounds identified in the hypothesis card;
- a held-out or genuinely out-of-sample test when the claim was developed
  by exploring the same data;
- independent adversarial review by the other collaborator, including
  reproduction of the headline result or a documented reason reproduction
  is impossible;
- a statement of what the result does **not** distinguish.

Promotion means "worth sustained falsification," not "probably deciphered."
Confirmation requires surviving the Skeptic's targeted test and explaining
evidence that the strongest alternative does not explain equally well.

## Automatic stop conditions

Do not promote when any of these applies:

- the observation was selected after inspecting the same test set and has
  no holdout;
- the effect disappears under one reasonable transcription or segmentation
  policy;
- the comparison changes object, carver, register, or sampling unit at the
  same time as the claimed variable;
- the proposed mechanism has enough unconstrained choices to fit arbitrary
  sequences;
- the result only restates a known corpus property (e.g. Zipf-like
  frequency) without a prediction that separates mechanisms;
- an upstream correction has not been propagated through the full dependent
  analysis chain;
- the claim rests on matching a handful of signs to a story or reading
  without corpus-wide validation — the specific, publicly documented
  failure mode of prior rongorongo decipherment attempts.

## Current consequence

At launch, the repository has no Confirmed Findings and no Active
Hypotheses — this is a genuine bootstrap state, not a placeholder awaiting
cleanup. The first substantive work is corpus canonicalization
(`config/sidequests.md`, SQ-1), which is itself infrastructure, not a
finding.
