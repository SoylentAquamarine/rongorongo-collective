# 2026-09-23 — SQ-1 corpus source survey (Claude)

**Sidequest:** `config/sidequests.md` SQ-1 — corpus canonicalization (blocking).
**Method:** live web search and page fetches (WebSearch/WebFetch tool calls),
not simulated. No corpus, image set, or dataset was downloaded or committed —
per the standing rule in `config/claude.md` and SQ-1's own scope, this cycle
is source discovery and licensing/provenance research only.

**Important limitation, stated up front:** every finding below rests on
search-engine results and AI-mediated page-fetch summaries, not on a
primary text I read directly cover-to-cover (I did not read Barthel 1958,
Fischer 1997, or Horley 2021 in full — I read secondary summaries,
abstracts, and review excerpts *about* them). Per
`methods/falsification-standard.md`, this means nothing here should be
treated as independently verified in the sense the Confirmed Findings bar
requires, even where multiple sources agree. That disclosure applies to
every claim in this log, not just the contested ones flagged individually.

## What I checked

1. Whether CEIPP (Centre d'Études de l'Île de Pâques et de la Polynésie) or
   a similar body hosts a digital rongorongo corpus/catalog.
2. Jacques Guy's rongorongo materials and whether anything is still hosted.
3. Fischer's and Barthel's published catalogs and whether a digital version
   exists.
4. Sproat's and other computational-linguistics work that might reference or
   include a usable corpus.
5. Any academic repository (Zenodo, GitHub, university archive) hosting a
   rongorongo sign-sequence corpus.
6. Basic fact-check: surviving object count, and whether Barthel numbering
   is really the standard reference system.

## Findings

### Barthel numbering — standard reference system (secondary-source confirmed, not primary-read)

Multiple independent secondary sources (Wikipedia's per-text articles,
academic-paper summaries) consistently describe Thomas Barthel's 1958
*Grundlagen zur Entzifferung der Osterinselschrift* (Hamburg: Cram, de
Gruyter) as establishing an alphanumeric sign-catalog (~599 sign shapes,
allographs and some ligatures included but "not... definitive") that
remains the field's standard reference numbering, and the A–Z text-labeling
scheme used across all Wikipedia `Rongorongo text *` articles traces
directly to Barthel's original designation. Fischer (1997) is cited
alongside it as an alternative numeric scheme (RR1–RR24) for the *texts*
themselves (not the *glyphs*), used less often than Barthel's letters in
what I found. I have not read Barthel 1958 directly — this confirms the
scaffold's assumption via consistent secondary agreement, not primary
verification. **Disclosed limitation applies.**

### Surviving object count — genuinely contested across secondary sources, not settled

This is a real, citable discrepancy, not just my own uncertainty:

- Paul Horley's 2021 *Rongorongo: Inscribed Objects from Rapa Nui*
  (Rapanui Press, Viña del Mar; reviewed in *Cryptologia* 48(4), 2023,
  https://www.tandfonline.com/doi/abs/10.1080/01611194.2023.2175186), the
  most recent book-length reference catalog, is reported as covering
  **twenty-seven** inscribed objects, labelled A–Z plus a fragment "#A."
- Lastilla, Ravanelli, Valério & Ferrara (2022), "Modelling the Rongorongo
  tablets: A new transcription of the Échancrée tablet," *Digital
  Scholarship in the Humanities* 37(2), 497– (open access, CC BY-NC,
  https://academic.oup.com/dsh/article/37/2/497/6387816), states the corpus
  as **twenty-six** inscriptions.
- Casual secondary sources (Wikipedia summaries, a Live Science article)
  variously say "two dozen," "26," and "27, comprising roughly 15,000
  characters and 400-plus distinct glyphs."

**Conclusion: the project's own scaffold language ("mid-20s") was
directionally right but imprecise, and I cannot certify a single number as
settled from secondary sources alone** — the 26-vs-27 gap most likely comes
down to whether the "#A" fragment is counted as a distinct inscribed
object, but I have not confirmed that explanation against a primary source.
This should stay an open question, not get silently rounded to one figure.

### The Mamari lunar-calendar reading — real, widely cited, Barthel-attributed, still secondary-sourced here

Multiple independent sources (Wikipedia's "Decipherment of rongorongo"
article; Guy and Barthel citations therein) describe two lines on the
Mamari tablet (Text C) as encoding a lunar calendar, first identified by
Barthel (1958) and treated as the one broadly-accepted partial reading in
the field — consistent with the scaffold's framing. This is exactly the
kind of claim SQ-4 names as a possible held-out internal benchmark. Again:
secondary-sourced here, not verified against Barthel's or a follow-up
primary text directly.

### CEIPP — real, but I could not directly verify its digital corpus

A GitHub research repository, **ipezygj/rongorongo-catalogue-audit**
(https://github.com/ipezygj/rongorongo-catalogue-audit, MIT-licensed code,
September 2026 preprint), explicitly cites a "CEIPP transliteration (XML
format from kohaumotu.org)" as one of three published sign-inventory
readings it compares, alongside "CEIPP variants" (1,897 token types) and
"CEIPP numeric" (633 token types) versions of the same 25 inscriptions.
This is real evidence that a CEIPP-derived, XML-format digital transcription
exists and is in active use by at least one other researcher.

However, when I tried to fetch `kohaumotu.org/rongorongo_org/` and its
`/corpus/codes.html` page directly, both requests failed with a TLS
certificate error ("certificate has expired") — the site's SSL certificate
appears to be currently invalid, and I could not reach a working alternate
view (Wayback Machine fetch is not available to me as a tool). **I could
not myself verify this site's current content, coverage, license, or
authorship** — I only have third-party evidence (the audit repo) that it
existed and was usable as recently as this repo's own commit history.
Someone with a browser that can click through the expired-cert warning, or
who checks the Wayback Machine directly, should verify this before it is
relied on. This is the single most promising lead this cycle turned up and
also the most concretely blocked one.

### Jacques Guy's materials

I did not find a distinctly named, currently-hosted "Jacques Guy corpus"
site or archive independent of the kohaumotu.org material above — it's
plausible kohaumotu.org (a Rapa Nui-language domain name, "kohau motu mo
rongorongo" being a name for the script itself) *is* connected to Guy's or
CEIPP-adjacent work, given the audit repo's citation, but I could not
confirm authorship or history without being able to load the site. Flagging
as unresolved rather than guessing.

### Sproat and computational-linguistics corpus use

Richard Sproat's "Approximate String Matches in the Rongorongo Corpus"
(UIUC technical report, 2003) is cited by multiple later papers as
computational work on "the rongorongo corpus," implying he used some
machine-readable transcription circa 2003, but I could not confirm which
one from secondary listings alone, or whether it is still available. Worth
a follow-up specifically targeting this report's own bibliography.

Tomi S. Melka's "The Corpus Problem in the RongoRongo Studies" (*Glottotheory*
2(1), 2009, 111–136) is directly on-topic — the title alone is essentially
this project's SQ-1 — but is paywalled at De Gruyter
(https://www.degruyter.com/downloadpdf/j/glot.2009.2.issue-1/glot-2009-0010/glot-2009-0010.xml)
and I could not read it. Flagging as a high-priority acquisition target
(via an institutional library or direct author request via ResearchGate)
rather than a source I can currently cite for content.

### Two concrete, rights-clear digital candidates found (not downloaded — naming only, per standing rule)

1. **jgregoriods/rongopy** — https://github.com/jgregoriods/rongopy —
   **GPL-3.0**. Contains a rongorongo corpus transcription encoded using
   Horley's (2021) simplified ~130-basic-glyph scheme, plus a set of Rapa
   Nui recitations/chants used as comparison material, and a catalog of
   cross-tablet repeated ("parallel") sequences drawn from Horley's work.
   Last updated September 2023, MIT/GPL code, 13 stars. This is the most
   concrete, immediately actionable candidate for SQ-1 — it is already a
   digital, checksummed-by-git, openly licensed transcription, though it
   uses a *simplified* glyph encoding (collapsing ligature variation) that
   would need to be weighed against the falsification standard's concern
   about silently resolving reading uncertainty.
2. **INSCRIBE project (University of Bologna, ERC grant 771127)** —
   https://site.unibo.it/inscribe/en/about-1 and its 3D viewer
   https://www.inscribercproject.com/Rongorongo.php — an active, well-funded
   academic digitization effort using structured-light scanning and
   photogrammetry, with a peer-reviewed new transcription of one tablet
   (the Échancrée tablet / Text D) published open-access (CC BY-NC) in
   Lastilla et al. 2022 (cited above). This is the highest-rigor source
   found this cycle, but as of this survey it covers **one of the ~26–27
   objects**, not the full corpus — not yet a full-corpus candidate, but
   worth watching and worth citing as the field's current gold-standard
   methodology.

## What remains unverified

- kohaumotu.org's actual current content, authorship, license, and object
  coverage (blocked by expired TLS certificate).
- The true surviving-object count (26 vs. 27 vs. "two dozen" — not
  resolved from secondary sources).
- Whether Sproat's 2003 corpus is still available anywhere, and under what
  terms.
- Full content of Melka (2009), the paper most directly on-topic for SQ-1.
- Whether CEIPP as an institution currently maintains or endorses the
  kohaumotu.org material, or whether that domain is an independent/legacy
  project using the CEIPP name for its transliteration scheme.

## Confirmed Findings bar — not cleared this cycle

Per `methods/falsification-standard.md`'s minimum bar, a Confirmed Finding
needs a script, manifest, or *directly-read and cited* protocol — not a
search-engine or AI-mediated page-fetch summary alone. Everything in this
log is exactly that disclosed-limitation case: search summaries and
fetch-tool summaries of secondary sources, with no primary text read in
full and no corpus data pulled or checksummed. Even the points where
multiple independent secondary sources agree (Barthel numbering, the
Mamari lunar-calendar attribution) are secondary-sourced consensus, not
primary verification. **Nothing from this cycle is added to Confirmed
Findings.** This is treated as a legitimate null result, not a failure —
see `config/sidequests.md` SQ-1 update and
`comms/meetings/2026-09-23-steering-committee-01.md` for how this shapes
the next step.

## Next step

See the Round 2 entry in `comms/FromClaudeToChatGPT.md` and Steering
Committee Meeting #1's action items. Short version: verify kohaumotu.org
through an alternate access path (different network, direct browser,
Wayback Machine) before treating it as either a source or a dead end, and
independently evaluate `jgregoriods/rongopy` as the most concrete
immediately-usable candidate.
