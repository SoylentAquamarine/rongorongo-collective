# Independent scope audit — CEIPP parity script
Date: 2026-11-26.

## Pinned source
- Repository: ipezygj/rongorongo-catalogue-audit
- Commit: ea8c95a4837a22cc2d959f548c728f91ec824636
- File: verify_ceipp.py
- Git blob: 7ca6973e468e55544942a4d4b084fc9fdf0174b4

## Inspection
The parser's regular expression is hard-coded to the object identifier Aa01. It sorts those rows by the three-digit position, reconstructs a string, then loads rongopy's JSON entry at A/Aa1 and compares only the prefix with the reconstructed length. This is a single-object, single-line prefix check, not a full object/side/line corpus reconciliation.

The third-party README reports 15/15 matches. I did not run the script, fetch its data files, access any rongorongo corpus bytes, or reproduce the 15 signs. This audit independently confirms the code's narrow scope only.

## Interpretation
A 15/15 match on one line cannot establish that all CEIPP inscriptions, sides, lines, variants or omissions match the downstream dataset. It also cannot establish a data license. GPL-3.0 for the audit/code does not by itself license any underlying CEIPP transcription.

## Decision
Keep the canonical-corpus gate closed. Obtain itemized written permission naming exact Barthel/CEIPP files and allowed research, storage, derivative and publication uses before retrieving data or attempting full parity.
