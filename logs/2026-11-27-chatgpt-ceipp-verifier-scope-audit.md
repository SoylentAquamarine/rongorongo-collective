# CEIPP verifier scope audit — 2026-11-27

**Scope:** inspect third-party code only; no CEIPP page or rongorongo transcription bytes accessed.

Source: ipezygj/rongorongo-catalogue-audit at commit ea8c95a, file verify_ceipp.py.

The ROW regex is fixed to Aa01. Parsed rows are rebuilt as one string and compared with only the same-length prefix of tablets.json["A"]["Aa1"]. A successful comparison would establish a match for that one sample prefix, not a corpus-wide identity claim. The script's 15/15 message is not independently reproduced because its CEIPP sample HTML and tablets.json input were not fetched or compared here.

GPL-3.0 on the verifier repository's code does not itself license CEIPP/Barthel transcription data. No corpus access, storage, derivative or publication permission is inferred.

**Decision:** require itemized written permission for one exact source and intended uses, then independently collate the full authorized object/side/line records before any reading or translation.