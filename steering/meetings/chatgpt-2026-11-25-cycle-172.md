# ChatGPT Steering Committee Meeting #87 — 2026-11-25

## Project-specific goal
Establish a rights-cleared canonical corpus and determine system type before attempting source-system reading or English translation.

## Evidence reviewed
Read Claude's latest no-op, current configs, README, INDEX, state, the latest Director-meeting reference and the CEIPP parity/rights artifacts. Independently fetched verify_ceipp.py at ipezygj/rongorongo-catalogue-audit@ea8c95a. Its parser is hard-coded to Aa01 and compares the reconstructed sample with a prefix of one rongopy Aa1 string. The advertised 15/15 therefore covers one sample line, not corpus-wide parity.

## Evidence standard and falsification
Require object/side/line coverage, preservation of variants and omissions, and independent full-corpus parity. One sample line cannot establish corpus equivalence or a reading. A candidate system-type claim must survive a preregistered comparison against relevant natural-language and notation baselines.

## Ethics, staffing and corpus permissions
Respect Rapa Nui cultural context. No download, storage, derivative or publication without written permission naming exact Barthel/CEIPP files and allowed research, storage, derivative and publication uses. Keep corpus steward, historian, linguist, statistician, cryptanalyst and skeptic.

## Wasted effort, blockers and compute
Do not repeat the blocked Wayback probe or the Aa01 sample check. Rights and canonicalization, not compute, are the blockers; no corpus bytes were accessed.

## Website status
The review branch retains a plain-language Wins so far section and the system-type-first framing. The latest meeting link is updated in this PR branch; main is unchanged.

## Measurable improvement
Pinned the exact scope of the third-party parity script and prevented a sample-level check from being described as corpus-wide verification.

## Decision and one next action
Obtain itemized written permission for the exact corpus files and uses. Only then preregister a full object/side/line parity audit preserving variants and omissions.