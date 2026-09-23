# Data

Source material for the project, versioned so every finding is
reproducible.

## Present

Nothing yet. Unlike the sibling Voynich project, which had an
already-agreed canonical transcription to import on day one, rongorongo
has no equivalent selected in this repository yet — see
`config/sidequests.md` SQ-1.

## Needed

- **Canonical glyph transcription/catalog** — a rights-clear,
  machine-readable source covering as much of the surviving corpus as
  possible, using a documented reference numbering, that preserves reading
  uncertainty rather than silently resolving it. Not yet selected. Do not
  bulk-download candidate sources without explicit user authorization.
- **Normalization script** — once a source is selected, a documented,
  reproducible script to turn it into a form the Statistician can run
  entropy/n-gram analysis on, without losing or silently resolving
  ambiguity, mirroring `normalize_eva.py` in the sibling project.
- **Reference/comparator corpora** — for the Linguist and Cryptanalyst to
  compare against (natural-language baselines, known mnemonic/notation
  systems). To be added as specific hypotheses are tested, not bulk-loaded
  up front.

## Convention

Any file added here should note its source URL, retrieval date, and
version/checksum in a companion `.source.md` (or in this README) so
provenance is never lost.
