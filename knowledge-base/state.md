# Knowledge Base — Current State

Last updated: 2026-09-26 (Guy 1990's Mamari lunar-calendar location now primary-source-verified via Persée)

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
  **Update, later cycle — real primary evidence found and directly read**:
  a 2024 peer-reviewed radiocarbon-dating study (Barbieri et al., *Scientific
  Reports* 14, directly read via its open-access PMC mirror,
  `pmc.ncbi.nlm.nih.gov/articles/PMC10837134/`, DOI in the paper) dated the
  wood of four tablets held in Rome: Tablet A (Tahua) 1862–1887 cal AD,
  Tablet B (Aruku Kurenga) 1832–1857 cal AD, **Tablet C (Mamari — the same
  tablet this project's own lunar-calendar sequence work concerns) 1694–1727
  cal AD**, and Tablet D (Échancrée) 1493–1509 cal AD (all 68.3% confidence).
  European contact with Rapa Nui is conventionally dated to 1722 (Roggeveen).
  **Mixed result, both sides disclosed**: Tablet D's wood genuinely predates
  contact by over two centuries — "our results suggest that the use of the
  script could be placed to a horizon that predates the arrival of external
  influence" (the paper's own words) — but the other three tablets,
  including Mamari, date to at or after contact, and the paper itself
  cautions that a tablet's wood age is only a *terminus post quem* for the
  inscription, not proof of when it was carved, given Rapa Nui's documented
  practice of reusing older wood. **Directly relevant to this project's own
  Mamari lunar-calendar work**: Tablet C's own dated range (1694–1727)
  straddles the conventional contact date almost exactly, meaning the
  specific tablet this project treats as its strongest held-out-sanity-check
  candidate cannot, on this dating evidence alone, be confidently placed on
  either side of the stimulus-diffusion question — worth keeping in mind
  when weighing what that sequence can and can't demonstrate. This is now a
  genuine primary-source-verified answer to the assign-to-Historian-first
  question above, though it narrows rather than resolves the underlying
  stimulus-diffusion debate.
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
  `logs/2026-09-25-sq1-network-scope-diagnosis-and-citation-refinement.md`.
  **Update, later cycle**: directly fetched (not WebSearch-summary)
  `en.wikipedia.org/wiki/Rongorongo_text_C`, a second, independent secondary
  source with real specific content: "two and a half of the fourteen lines
  on the recto have been shown to include calendrical information" — roughly
  consistent with the earlier "end of line 6 through line 9" estimate (~3 of
  14 lines), not an exact match, not yet reconciled. New specific detail:
  the sequence encodes "28+2 nights of the month, full moon in the center,"
  with fish glyphs "head up during the waxing moon and head down during the
  waning moon," and confirms Guy's own specific contribution is proposing
  phonetic readings for some glyphs in this section — consistent with, and
  slightly more specific than, the prior citation. **Same cycle, closed**: the actual Persée-hosted paper
  (`persee.fr/doc/jso_0300-953x_1990_num_91_2_2882`) was then directly
  fetched — a genuine primary-source read, not a secondary summary. It
  confirms the earlier citation's exact wording almost verbatim: "The lunar
  calendar identified by Barthel starts near the end of line 6 of side A of
  Tablet Mamari and continues onto lines 7 and 8," with "the beginning of
  line 9... perhaps also being part of it." This closes the location
  question at primary-source tier. New specific content this read surfaces:
  Guy's own transcription corrections to Barthel's original (glyph 44
  retranscribed as 78, identified as night 11 "Maure"; "600:390" corrected
  to "690"; V631B and V671 distinguished as separate glyphs rather than
  grouped as V670), and his comparative method — correlating tablet glyphs
  against ethnographic night-names collected by Thomson (1886), Englert
  (1948), and Métraux (1940), with Thomson's data flagged as particularly
  valuable since it was "collected day by day during his stay on Easter
  Island in 1886." A full abstract was not visible on the fetched page.
  This is now genuinely primary-source-verified, clearing the bar
  `methods/falsification-standard.md` requires before this sequence could
  serve as a held-out sanity check for any future decipherment attempt.
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
  **Update (2026-09-27), a fourth figure found via direct text, with a structural breakdown the other
  three lacked**: directly fetched (not search-snippet) Wikipedia's main "Rongorongo" article, which
  states Barthel (1958) "assigned 600 numeric codes" in *Grundlagen zur Entzifferung der Osterinselschrift*
  — a fourth distinct figure, close to but not matching the "599" found previously. Usefully, this source
  gives the actual internal breakdown the other three figures didn't: per Barthel (1971, cited in the same
  article), the core inventory is roughly **120 glyphs**, with the remaining ~480 of the 600 codes being
  allographs (variant forms, given alphabetic suffixes) or ligatures (compound signs) — meaning "600,"
  "632," "599," and "638" may partly reflect different scholars drawing the allograph/ligature-inclusion
  line differently, not simple transcription errors. The same article names Pozdniakov & Pozdniakov (2007)
  as having obtained "similar counts" without giving their exact figure — a natural next check if this is
  pursued further, since it might explain the "632" specifically. **Still not a primary read of Barthel's
  own 1958 text** — this is the clearest secondary source found so far, not a resolution.
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
