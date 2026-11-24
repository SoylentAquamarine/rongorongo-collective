# CEIPP parity-script scope audit — 2026-11-24

## Purpose
Assess what the third-party `verify_ceipp.py` actually tests without accessing or redistributing the underlying rongorongo corpus.

## Pinned source
- Repository: [ipezygj/rongorongo-catalogue-audit](https://github.com/ipezygj/rongorongo-catalogue-audit)
- Commit: `ea8c95a`
- Script: [`verify_ceipp.py`](https://github.com/ipezygj/rongorongo-catalogue-audit/blob/ea8c95a/verify_ceipp.py)
- README: [reproduction notes](https://github.com/ipezygj/rongorongo-catalogue-audit/blob/ea8c95a/README.md)

## Code-level result
The parser regex is anchored to the object/side/line identifier `Aa01`. It collects the matching sign rows, sorts them by numeric row index, reconstructs one line, loads `rongopy/tablets.json` at `["A"]["Aa1"]`, and compares that reconstruction to the prefix of that single string.

The script can therefore test a sample-line parity claim (the README describes 15/15 characters). It does **not** iterate across all 25 inscriptions, all sides, all lines, or all catalog variants. Its output cannot establish that the complete `tablets.json` corpus is a CEIPP reformat.

## Evidence boundary
This is inspection of the script source only. No `ceipp/digit.html`, `rongopy/tablets.json`, CEIPP XML, corpus images or other corpus bytes were fetched, opened or copied. No parity run was performed. No license or permission is inferred from the code or README.

## Decision
Treat whole-corpus equivalence as unverified. If written permission is obtained for the exact CEIPP files, preregister an object/side/line join, compare all included records, preserve variants and report unmatched rows before any statistical analysis.
