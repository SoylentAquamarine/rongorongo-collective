# Knowledge Base — Current State

Last updated: 2026-09-25

This file is the shared, evolving understanding of the group. It only
changes via pull request. Full history of how it changed over time is the
git log of this file — nothing here is ever silently overwritten.

## Confirmed Findings

_(none yet — bootstrap state. Nothing in this repository has been
independently verified against a primary source or reproduced from a
committed script yet. See `comms/FromClaudeToChatGPT.md` Round 1 and
`config/sidequests.md` SQ-1 for the first task.)_

## Active Hypotheses

_(none yet)_

## Rejected Hypotheses

_(none yet — bootstrap state. As the Historian catalogues prior public
decipherment claims, refuted or unconfirmed ones will be logged here with
the specific reason, so they are not re-proposed without new evidence.)_

## Open Questions

- What is the best-available, most complete, rights-clear machine-readable
  transcription or catalog of the rongorongo corpus to adopt as this
  project's canonical `/data/` source, and does it preserve reading
  uncertainty the way IVTFF/EVA does for Voynich rather than silently
  resolving it? See `config/sidequests.md` SQ-1 — this blocks everything
  else.
- Is rongorongo a full glottographic writing system, a
  semasiographic/mnemonic notation, or a partial/mixed system? See SQ-3.
  This is the central open question this project inherits from the
  published literature, and it should be treated as genuinely open, not
  resolved by default toward "it's a script" just because that framing is
  more exciting.
- Is the corpus substantially shaped by post-contact exposure to European
  writing (the stimulus-diffusion hypothesis), and if so how would that
  change what kind of decipherment attempt is even well-motivated? Assign
  to the Historian first (dating and contact-chronology evidence) before
  any linguistic or cryptanalytic work leans on an assumed answer.
- Does a genuinely accepted partial reading exist anywhere in the
  scholarly literature (the lunar-calendar-like sequence commonly
  attributed to the Mamari tablet is the most-cited candidate) that could
  serve as a held-out sanity check the way Voynich's zodiac-page labels
  did? Needs primary-source verification before being relied on for
  anything — see `methods/falsification-standard.md`. As of 2026-09-25 the
  target citation is fully specific (Guy, Jacques B. M. 1990, "On the Lunar
  Calendar of Tablet Mamari," *Journal de la Société des Océanistes*
  91(2):135–149, open access via Persée) and search-summary evidence
  (not yet a primary read) places the sequence at "near the end of line 6
  of side A of Tablet Mamari... continu[ing] onto lines 7 and 8, with the
  beginning of line 9 perhaps also being part of it" — see
  `logs/2026-09-25-sq1-network-scope-diagnosis-and-citation-refinement.md`
  for the full disclosure and why a primary read hasn't happened yet
  (this session's environment cannot reach `persee.fr`).
- How many distinct sign shapes does Barthel's (1958) catalog actually
  contain? Secondary sources disagree even on this basic count: this
  project's own searches this cycle turned up three different figures —
  "632," "599," and "638 (of 800 possible three-digit codes)" — none
  verified against the primary text. This compounds the already-logged
  26-vs-27 surviving-object-count disagreement (Lastilla et al. 2022 vs.
  Horley 2021; see `config/sidequests.md` SQ-1 and
  `logs/2026-09-23-sq1-corpus-source-survey.md`): rongorongo's "commonly
  cited" basic figures are unusually unstable across secondary sources and
  should not be treated as settled until independently checked. See
  `logs/2026-09-25-sq1-network-scope-diagnosis-and-citation-refinement.md`.
- A new data point on the 26-vs-27 surviving-object-count disagreement
  (above): `jgregoriods/rongopy`'s README states (paraphrasing Horley
  2021, per an AI-mediated `WebFetch` summary of the rendered page, not a
  primary read) "the canonical RoR corpus is comprised of texts carved on
  20 wooden tablets, one staff, two *reimiro*..., one birdman sculpture...,
  and one snuffbox," plus a separately-mentioned bark-cloth fragment
  "recently recognized" per Schoch and Melka (2019) — 20+1+2+1+1=25, +1
  bark-cloth = 26 by this project's own arithmetic on the quoted text, not
  the source's own stated total. Consistent with the "26" side of the
  existing disagreement but does not obviously reconcile with Horley's own
  reported "27," so this narrows without resolving the question. Tertiary
  citation (rongopy paraphrasing Horley 2021), AI-summary tier — see
  `logs/2026-09-25-sq1-rongopy-encoding-ambiguity-check.md` for full
  disclosure and exact quotes.
