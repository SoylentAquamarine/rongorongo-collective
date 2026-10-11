# SQ-4 — Steven Roger Fischer's 1995 "triad" decipherment claim catalogued

## Precommitment self-review (written before fetching)

**Known:** SQ-4's catalog has two entries so far, both relatively obscure (a priority dispute
between two independent researchers, and a self-published Zenodo working paper). Searching for
more self-published claims this cycle surfaced references to a much more prominent, widely-
discussed historical claim: Steven Roger Fischer's 1995 announcement that he had deciphered
rongorongo's Santiago Staff. This is a materially different kind of catalog entry than the
first two — a claim that drew sustained, specific, named scholarly rebuttal, exactly the "why it
remains unaccepted" detail SQ-4's own scope requires and the first two entries only partially
have.

**Not done yet:** neither the claim's specific content nor any of the named rebuttals had been
directly read by this project before this cycle.

**Design and why it's non-circular:** directly fetch Wikipedia's dedicated "Decipherment of
rongorongo" article (not a search-snippet synthesis) for the claim's specific content and every
named critic's specific objection, reporting each rebuttal's actual mechanism rather than a
generic "disputed" label.

**Honesty precommitment:** report every named critic's objection as specifically as the source
gives it, and disclose if any citation (page/count numbers, quotes) looks internally
inconsistent rather than silently smoothing it over.

## Findings

**The claim**: in 1995, independent linguist Steven R. Fischer announced he had "cracked" the
rongorongo "code." His central example, from the Santiago Staff (a 2,320-glyph text), is the
sequence "606.76 700 8," roughly halfway through line 12. He identified glyph 76 as a phallus
and read a recurring "X-phallus Y Z" pattern as "X copulated with Y, there issued forth Z,"
reading glyph 606 as "all the birds" via a claimed semantic shift from "hand" to a plural
marker — rendering his example as a creation chant about birds, fish, and the sun.

**Five specific, named rebuttals, directly fetched**:
1. **Andrew Robinson's structural count**: only 63 of the staff's sequences fully fit Fischer's
   claimed triad structure — the maximum even with generous counting (the Wikipedia article
   itself flags an internal `[sic]` on the total sequence count in Robinson's quoted figure,
   disclosed here rather than silently corrected).
2. **Pozdniakov and Pozdniakov's frequency argument**: the four glyphs in Fischer's own main
   example make up roughly 20% of the entire corpus — common enough that the same reading logic
   would produce absurd results elsewhere (e.g., "the sun copulates with the fish").
3. **Jacques Guy's linguistic objection**: the word Fischer reads as a Rapanui plural marker
   (*mau*) is actually a Tahitian grammatical element; in Polynesian languages generally it
   functions as an adjective ("true, genuine") placed after a noun, not as the plural marker
   Fischer's reading requires.
4. **Guy's second objection, on Fischer's supporting parallel text**: Fischer's corroborating
   evidence from *Atua Matariri* depends on Salmon's English translation, which does not match
   Salmon's own Rapanui transcription of the same text; a separate reading (Métraux's) mentions
   neither birds nor fish at all.
5. **Richard Sproat's computational test**: automated string-matching found the Santiago Staff
   stands apart from the rest of the corpus on its own terms; removing glyph 76 (the "phallus"
   sign central to Fischer's reading) from the analysis did not change the result, undermining
   the specific "phallus omission" assumption Fischer's method relied on.

The article also states the wider scholarly consensus is that Fischer's attempts were "not
accompanied by the least justification," and that none of his readings generalize meaningfully
to other, novel rongorongo texts.

## Outcome

A real, well-documented, multiply-corroborated historical case — five independent named critics,
each with a different, specific technical objection (structural, statistical, linguistic,
textual, and computational), converging on rejection of the same claim from five different
angles. This is a stronger evidentiary pattern than either existing catalog entry and belongs in
`data/sq4-prior-claims-catalog.md` as its own, detailed entry.

## Limitation disclosed

This is Wikipedia-article tier (a well-sourced secondary synthesis, not yet a direct read of
Fischer's own 1995/1997 publications or of Robinson's, the Pozdniakovs', Guy's, or Sproat's own
original papers). Each named rebuttal is a real, citable lead for a future primary-source
upgrade, not yet attempted this cycle.
