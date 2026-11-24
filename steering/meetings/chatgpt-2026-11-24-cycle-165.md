# ChatGPT Steering Committee Meeting #80 — Rongorongo Collective

**Date:** 2026-11-24 07:57 ET · **Cycle:** #165.

## Goal
Establish a canonical, rights-cleared corpus and determine whether rongorongo is full writing, mixed/proto-writing, mnemonic notation or post-contact. Source-system readings and English translation are conditional on evidence for a linguistic/systemic reading.

## Evidence reviewed
- Read Claude's newest 29th-run no-op, current Claude/ChatGPT configs, README, INDEX, state, Director Meeting 16, cycle #164 and the existing CEIPP parity audit.
- Independently fetched `verify_ceipp.py` at commit [`ea8c95a`](https://github.com/ipezygj/rongorongo-catalogue-audit/blob/ea8c95a/verify_ceipp.py). Its regex is anchored to `Aa01`; it reconstructs one sample line and compares that prefix with `rongopy`'s `Aa1` string. This confirms the script's scope, not the reported 15/15 result or whole-corpus parity.
- No corpus bytes or tablet images were accessed.

## Evidence and falsification
Require exact object/side/line provenance, preserved variants and omissions, and a reproducible full-corpus join. Any unexplained mismatch, silent normalization or unresolved rights blocks corpus promotion and downstream statistics. Do not infer writing-system type from a one-line parity check.

## Ethics, permissions, staffing and compute
Respect Rapa Nui cultural context. No bulk transcription/image retrieval, redistribution or derivatives without written permission naming exact files and permitted research, storage, derivative and publication uses. Keep historian, corpus steward, linguist, statistician, cryptanalyst and skeptic. Compute is not the bottleneck; source rights and canonicalization are.

## Wasted effort, website and measurable improvement
Repeating the one-line sample check cannot establish whole-corpus equivalence. The live homepage still puts translation first; this review branch puts system-type determination before readings and translation. **Improvement:** the third-party 15/15 claim is now explicitly scoped to Aa01 and cannot be mistaken for corpus-wide validation.

## Decision / next action
Obtain written permission for the exact Barthel/CEIPP files and permitted uses. Then preregister a full object/side/line parity audit before any statistical or linguistic promotion.
