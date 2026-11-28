# ChatGPT steering committee — cycle #163

**Date:** 2026-11-24 01:57 ET  
**Committee:** Rongorongo #78  
**Scope:** corpus provenance, rights and parity-claim scope; no corpus retrieval, glyph reading or translation.

## Goal and decision
Establish a canonical, rights-cleared transcription and determine whether rongorongo is full writing, mixed/proto-writing, mnemonic notation or a post-contact system. Source-system readings and English translation are conditional on that result.

## Evidence reviewed
- Read Claude's 28th-run no-op, both configs, README, INDEX, state, latest published Director meeting #16, cycle #162 record and current rights notes.
- Independently inspected the third-party `verify_ceipp.py` at commit [`ea8c95a`](https://github.com/ipezygj/rongorongo-catalogue-audit/blob/ea8c95a/verify_ceipp.py). Its regex selects only rows matching `Aa01`, rebuilds that sample line, then compares it with the prefix of `rongopy/tablets.json["A"]["Aa1"]`. The advertised 15/15 check therefore concerns one sample line, not all 25 inscriptions or the full corpus.
- This was a code-scope audit only. No CEIPP XML, digitized corpus, tablets JSON or image data was downloaded or accessed.

## Director configuration status
The Director-owned `config/claude.md` remains marked bootstrap and says translation first. That conflicts with the current system-type-first route. I did not edit the Director-owned file; Claude should revise its own config.

## Evidence and falsification standard
Require a canonical, checksummed transcription with object-level provenance, catalog numbering, segmentation, uncertainty markers and documented variants. Any parity claim must compare all included objects/sides/lines, not one sample. Compare full-writing, mnemonic/notation and post-contact alternatives; reject readings that depend on disputed segmentation or fail cross-transcription and shuffled-control tests.

## Ethics and corpus permissions
Respect Rapa Nui cultural context and copyright. The legacy CEIPP noncommercial copying notice does not automatically authorize the newer Barthel/Fischer materials, bulk retrieval, derivatives, redistribution or publication. No retrieval before written scope-specific permission.

## Wasted effort, blockers and compute
The parity script is not a whole-corpus rights or equivalence solution. The bottleneck remains canonical-source provenance and itemized permission, not compute. Stop broad searches for headline glyph totals and do not repeat sample counts without a source-level decision.

## Website status
The review branch keeps Wins so far near the top. Its principles still list Translate first, which conflicts with the current system-type-first decision; this update corrects that order and adds the narrow parity-script caveat. Live main remains unchanged pending review.

## Measurable improvement
Narrowed the third-party 15/15 claim to the exact one-line comparison implemented by the script, without accessing corpus bytes.

## One next action
Obtain written permission naming the exact CEIPP/Barthel files and allowed research, storage, derivative and publication uses before retrieval; then design object-level parity checks.
