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

## Tooling

- **`scripts/index_corpus_qdrant.py`** — embeds this repo's own `logs/`,
  `comms/`, `steering/meetings/`, `knowledge-base/state.md`, and `methods/`
  into a Qdrant vector collection (`rongorongo-collective`) via the
  linuxbox's `nomic-embed-text` model, for semantic search/navigation over
  this project's own prior work. Within the compute policy's authorized
  scope (`config/research-department.md`): a navigation aid only, never a
  substitute for Claude/ChatGPT's own research judgment or adversarial
  review. Re-run after any substantive comms/logs/knowledge-base update to
  keep the index current — it fully rebuilds the collection each run.

## Convention

Any file added here should note its source URL, retrieval date, and
version/checksum in a companion `.source.md` (or in this README) so
provenance is never lost.
