# CEIPP verifier scope audit — 2026-11-28

**Scope:** code-only inspection of `ipezygj/rongorongo-catalogue-audit@ea8c95a`. No CEIPP, Barthel or rongopy transcription bytes were fetched.

- Repository: https://github.com/ipezygj/rongorongo-catalogue-audit
- Commit: `ea8c95a`
- File: `verify_ceipp.py`
- Blob SHA-1: `7ca6973e468e55544942a4d4b084fc9fdf0174b4`

## Direct code observations

1. The row regex begins with literal `Aa01`; it does not iterate over object IDs.
2. Parsed rows are sorted by the three-digit row index.
3. The reconstruction is compared with `tablets.json["A"]["Aa1"][:len(rebuilt)]`, a same-length prefix only.
4. The script's 15/15 message, if produced, therefore concerns one Aa01 sample prefix, not all tablets, objects or the complete CEIPP corpus.

## Conclusion

The code inspection confirms the verifier's narrow scope. It does **not** reproduce the 15/15 result, establish that rongopy is corpus-wide CEIPP reformatted, or resolve data rights. GPL-3.0 on the wrapper does not license underlying transcription data.

**Next:** obtain itemized written permission for one exact corpus edition/files and permitted uses before fetching or comparing any transcription bytes.
