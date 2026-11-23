# Result — CEIPP XML lead: Wayback/alternate-network metadata check (ChatGPT #154)

Precommit: `logs/2026-11-23-ceipp-xml-wayback-metadata-precommit.md`.

## Access: FAILED (both routes), environment-side
- `https://kohaumotu.org/Rongorongo/xml/`: the agent proxy returned `403 Forbidden (agent proxy: no rule or network setting allows this host)`. Plain HTTP failed DNS resolution in this sandbox. WebFetch failed with `ENOTFOUND`.
- Wayback CDX API (`web.archive.org/cdx/...`): proxy `CONNECT 403`. WebFetch reported "unable to fetch from web.archive.org".
- So this environment did not test the site's TLS certificate status; the failure is in the session network policy, not evidence about the site. The prediction that Wayback has snapshots is **untested**. Unblocking needs the user to allow `kohaumotu.org` and/or `web.archive.org` in the cloud environment's network settings, or someone checking from a normal browser.

## Fallback (metadata only, no corpus bytes): third-party README + one script, at a pinned commit
`ipezygj/rongorongo-catalogue-audit` HEAD = `ea8c95a4837a22cc2d959f548c728f91ec824636` (git ls-remote, 2026-11-23). README "Data (fetched, not redistributed)" table, verbatim row:
> | CEIPP transliteration, XML | kohaumotu.org/Rongorongo/xml/ (Philip Spaelti) | as published there; cite CEIPP |
- Authorship: attributed to Philip Spaelti (host/maintainer) with CEIPP as the attributed originator. This is the same as the 2026-09-23 record. Not confirmed from the site.
- Coverage: "the same 25 rongorongo inscriptions" in three readings (L = 1,897 / 633 / 125). This is the audit's working set, not necessarily the XML's full coverage. The 26-vs-27 object-count question is unaffected.
- License: still **none stated**. "Cite CEIPP" is an attribution request, not a license (prediction matched, from a secondary source only).

## New, disclosed finding (third-party claim, not reproduced)
The audit's `verify_ceipp.py` (same commit) claims that `jgregoriods/rongopy`'s `tablets.json` **is the CEIPP transliteration reformatted**. Its method: it rebuilds Aa01 line 1 from a CEIPP fixed-column sample page (`digit.html` on kohaumotu.org) and checks byte-equality with rongopy's `Aa1` prefix. The README reports 15/15 matches.
- Scope is tiny: one line of one object, about 15 signs. That makes it suggestive, not a corpus-level proof.
- **Rights implication if true:** rongopy's GPL-3.0 covers rongopy's code. It may not clear the underlying transcription data, which would then trace back to CEIPP with no stated license. Earlier notes listed rongopy's "clear GPL-3.0" as an advantage over kohaumotu.org (`config/sidequests.md` SQ-1, 2026-09-23). That advantage may not carry over to the data. This is flagged for the Director; earlier text is not edited.
- Not reproduced here. Reproducing it needs the CEIPP sample page (blocked) and rongopy's tablet data (corpus bytes, not authorized).

## Net
Nothing was selected or downloaded. The canonical-source gate is unchanged. Adoption now also needs a data-rights check on rongopy, not only on kohaumotu.org.
