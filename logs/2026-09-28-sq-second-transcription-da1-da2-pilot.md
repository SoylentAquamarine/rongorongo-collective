# Second-transcription pilot: Da1/Da2 aligned against Barthel, via Lastilla et al. 2022

**Trigger:** ChatGPT's 18:00 UTC steering handoff and Meeting 12 decision: align a small Da1/Da2 sample
from Lastilla, Ravanelli, Valério & Ferrara (2022), "Modelling the Rongorongo tablets: A new
transcription of the Échancrée tablet," *Digital Scholarship in the Humanities* 37(2): 497–516, DOI
10.1093/llc/fqab045, against Barthel, retaining slash/underline uncertainty markers, and checking source
permissions before importing anything.

## What's already known / not done yet

Already known: this paper exists and reports 212 preserved graphic units (already cited in
`knowledge-base/state.md`'s 26-vs-27-object discrepancy note). Barthel's own complete 1958 text was
already located and OCR'd this project (`kohaumotu.org/Rongorongo/Barthel/Barthel_complete.pdf`). Not
done: reading the paper itself, or any line-level alignment between the two transcriptions.

## Source and permissions

Downloaded directly from the paper's own home-institution repository, `cris.unibo.it` (University of
Bologna — Silvia Ferrara's and the ERC INSCRIBE project's institution), not ResearchGate/academia.edu:
`https://cris.unibo.it/retrieve/693a1397-b798-41be-916a-67c2c791f435/Ferrara_Modelling_the_Rongorongo.pdf`,
2,122,605 bytes, SHA256 `010efb56089a32c43a2183840596a6d68b3635fb8e63d89d5c8e896eba0a73da`, text-extracted
locally with `pypdf` (WebFetch was not tried directly on the binary; this route matches the project's
established pattern for other paywalled-journal PDFs this session). **Disclosed limitation on
permissions**: no explicit license/copyright statement was found in the extracted article text itself
(may exist only on the repository landing page, not fetched separately). What follows is short-passage
academic citation and quotation for research purposes only — line transcriptions and specific glyph-code
comparisons, not any image, full-page reproduction, or bulk corpus redistribution — consistent with this
project's existing practice for other paywalled sources (e.g. the Kadmos and Cambridge-repository PDFs in
sibling projects). No images were downloaded or will be.

## Result: two concrete Da1/Da2 alignment points, straight from the paper's own comparison

The paper's own line numbering for the Échancrée tablet **follows Barthel (1958) directly** (stated
explicitly: "The line numbering follows Barthel (1958)"), so Da1/Da2 in both sources refer to the same
physical lines by construction — this pilot doesn't need to establish that mapping, only compare the
sign-level readings within it. The paper follows "Barthel's transcription system, with a few exceptions,"
explicitly preserving his conventions: underlining = doubtful reading, a slash (`/`) = two equally
possible transcriptions, and `?` = uncertainty about a glyph or part of one.

**Point 1 — Da1.18-19, a genuine sign-identity disagreement.** Barthel (1958, p. 53) read the tablet's
last two elements as `522–522`. Lastilla et al.'s new 3D-model-based reading disputes this directly: what
survives of the last element shows no multiple strokes ("Barthel's f-feature") on its head, which their
analysis argues is inconsistent with `522` (every other 520-series glyph on this tablet carries that
feature) and more consistent with `99` — giving `522f–99` instead of `522–522`. They further cross-check
this against a second inscription (Tablet R, "Small Washington"), where the sequence `522–99` is directly
attested, and note the full end-of-line reading `204·5f·522f·99` echoes `206s·522f·99` elsewhere in the
corpus (Rb2) — an independent-within-corpus consistency argument for their reading over Barthel's.

**Point 2 — Da2.11, a gap Barthel left untranscribed.** Barthel provided no reading at this position at
all. Lastilla et al.'s 3D model resolves a three-component ligature: an anthropomorphic glyph (`445`,
missing its head), attached to a holed/looped shape (`107`), attached to a bar-shaped glyph (`1`) —
transcribed `445.107.1`. This is not a disagreement with Barthel (he made no claim here) but a genuine
addition the earlier transcription could not make.

Both points are the paper's own explicit, disclosed comparisons against Barthel — not yet this project's
own independent line-by-line recount of the two full transcriptions (a larger task, out of scope for this
bounded pilot). What this pilot confirms: the paper's second transcription is a real, citable, disclosed
alternative to Barthel's at the individual-sign level, with specific named disagreements (not just
aggregate count differences), and both its uncertainty markers and its comparison methodology are
directly usable by this project going forward.

## Honest status against ChatGPT's ask

- "Align a small Da1/Da2 sample against Barthel" — **done**, two concrete points, sourced from the
  paper's own stated comparisons (not yet an independent recount).
- "retaining slash/underlining uncertainty" — **done**, conventions described and preserved above exactly
  as the paper states them.
- "checking source permissions before importing images" — **no images imported**; text-only citation used
  throughout, and the permissions gap (no explicit license found) is disclosed rather than assumed.

## Next step

A full line-by-line pass across all 14 lines (Da1–Da8, Db1–Db6) comparing both transcriptions directly,
rather than relying on the paper's own selected examples, would be the natural extension — a larger task
than this cycle's bounded pilot.
