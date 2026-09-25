# 2026-09-25 — Network-access scope diagnosis + Barthel/Guy citation refinement (Claude)

**Sidequest:** `config/sidequests.md` SQ-1 — corpus canonicalization (blocking); also
responds to Steering Committee Meeting #1's Historian action item ("get at
least one Barthel(1958)/Fischer(1997)-sourced claim onto a primary or
strong-single-authoritative citation... before it informs SQ-2 schema
design").
**Method:** live web search (working) and direct HTTPS probes of several
scholarly-source domains (`curl` through this session's own network egress
proxy, plus the `WebFetch` tool) to test domain reachability. No corpus,
image set, or dataset was downloaded or committed.

## 1. Corrected diagnosis: this is an environment-wide policy, not a
kohaumotu.org-specific block

The prior cycle (`logs/2026-09-23-sq1-kohaumotu-access-followup.md`)
diagnosed `kohaumotu.org` as blocked by "this specific agent environment's
own network egress proxy," distinct from a site-level expired-certificate
problem. This cycle tested whether that block is specific to
`kohaumotu.org` or broader, by probing several unrelated, well-known
scholarly/reference domains directly:

| Domain | Result |
|---|---|
| `en.wikipedia.org` | `CONNECT tunnel failed, response 403` (proxy: `connect_rejected` / "organization policy") |
| `www.persee.fr` (hosts Guy 1990 open access) | same |
| `journals.openedition.org` | same |
| `archive.org` | same |
| `books.google.com`, `www.google.com` | same |
| `www.jstor.org` | same |
| `doi.org`, `scholar.google.com`, `tandfonline.com`, `academic.oup.com`, `researchgate.net` | same |
| `github.com`, `raw.githubusercontent.com` | reachable (200/301/400, i.e. not egress-blocked) |

**Conclusion:** this session's network egress policy allowlists GitHub and
package-registry/Anthropic infrastructure (see the proxy's own `noProxy`
list) and blocks essentially all other external domains by default,
including basic reference sites like Wikipedia — not a targeted block on
`kohaumotu.org` specifically. This supersedes the prior cycle's narrower
diagnosis: kohaumotu.org's inaccessibility from this environment is a
special case of a much broader default-deny policy, not a site-specific
rule. A further "different access path" attempt at kohaumotu.org from
*this* environment would not produce new information — the constraint is
structural, not a path-specific quirk. Per `mcp__Claude_Code_Remote`'s own
environment documentation, the remedy is for the environment operator to
widen the network access level or add specific domains to an allowlist in
the environment's settings; that's outside what this session can do
itself, so it's recorded here as a concrete, disclosed ask rather than
something silently worked around.

**Practical effect on this project:** every citation-verification cycle so
far (this one included) has been limited to `WebSearch`-tool result
snippets — which still function, evidently served through different
infrastructure than direct page fetches — rather than a full primary-text
read. That is the actual reason no claim has cleared the Confirmed
Findings bar yet, more precisely stated than "no one has checked it yet."
If a future cycle runs in an environment with broader network access (or
the user adds `persee.fr`, `journals.openedition.org`, `en.wikipedia.org`,
`jstor.org`, `academic.oup.com` to this environment's allowed domains),
primary-source reads become possible for the first time.

## 2. Citation refinement (still WebSearch-summary tier — disclosed, not a primary read)

Working within that constraint, `WebSearch` turned up more precise detail
than previously recorded on both flagged citations:

**Guy (1990).** Full citation now specific rather than approximate: Guy,
Jacques B. M. 1990. "On the Lunar Calendar of Tablet Mamari." *Journal de
la Société des Océanistes* 91(2): 135–149. Hosted open-access at
Persée (`persee.fr`, currently unreachable from this environment per §1).
Search-result summaries (not the paper itself) describe the sequence
identified as a lunar calendar as starting "near the end of line 6 of side
A of Tablet Mamari and continu[ing] onto lines 7 and 8, with the beginning
of line 9 perhaps also being part of it." This is more specific than this
project's prior framing ("the sequence commonly discussed as a
lunar-calendar-like run on the Mamari tablet") and, if later confirmed by
an actual read of Guy (1990) or a citing secondary source that quotes it
directly, would give SQ-2's atlas schema an exact object/line locus to
encode against. **Not yet confirmed** — this is still a search-engine
summary of the paper, not the paper read directly, and is recorded here
precisely so it is not mistaken for more than that.

**Barthel (1958) sign-catalog size.** A new, previously unrecorded
discrepancy: this cycle's searches returned **three different** figures
for the size of Barthel's sign catalog across secondary sources — "632,"
"599," and "638 (of 800 possible three-digit codes)." This is analogous
to, and compounds, the already-logged 26-vs-27 surviving-object-count
disagreement (`knowledge-base/state.md` Open Questions). It is added there
as a new open question rather than silently resolved to any one number,
per this repository's own falsification standard's emphasis that
"commonly cited" rongorongo figures are frequently imprecise even in
serious secondary literature.

## Confirmed Findings bar — still not cleared this cycle

Everything in §2 remains search-engine-summary evidence, explicitly
disclosed as such, not a primary text read in full or a reproducible
script. `knowledge-base/state.md`'s Confirmed Findings section is
unchanged. Only the Open Questions section gets a new, disclosed entry
(the sign-count discrepancy) — consistent with how the object-count
discrepancy was already recorded there without being promoted further.

## Net effect on SQ-1 and the Historian action item

- The Historian action item ("primary or strong-single-authoritative
  citation, not repeated secondary corroboration") is **not fully
  satisfied this cycle** — it cannot be, from this specific environment,
  until either network access is broadened or the work moves to an
  environment/party that can reach `persee.fr` directly. What *is* now
  true: the target citation is fully specific (journal, volume, issue,
  page range) and the open-access host is identified, so the very next
  capable session can attempt the primary read directly with no further
  discovery work needed.
- SQ-1's source-selection question (kohaumotu.org vs. rongopy) is
  unchanged from the prior log: kohaumotu.org direct access is confirmed
  blocked from this environment for structural, not path-specific,
  reasons (no further benefit to retrying it here); rongopy's
  ambiguity-preservation check still needs explicit user authorization to
  pull its data files, which remains unrecorded anywhere in this repo.

## Next step

1. If the user or environment operator can broaden this environment's
   network allowlist (see `mcp__Claude_Code_Remote` environment docs,
   "Network access" in the environment settings) to include
   `persee.fr`, `journals.openedition.org`, `en.wikipedia.org`, and
   similar reference/journal domains, the next cycle should attempt a
   direct primary-source read of Guy (1990) before anything else in
   SQ-1/SQ-2 — this is now the single highest-leverage unblock across
   both SQ-1 and the Historian's standing action item.
2. Otherwise, treat kohaumotu.org direct access as closed for this
   environment (not "retry later") and keep pursuing the rongopy
   data-file-pull authorization question with the user, per the prior
   log's still-open ask.
3. Do not begin SQ-2 schema design using either the lunar-calendar locus
   or the Barthel sign-count until one of these resolves to an actual
   primary-source check, per the falsification standard and Meeting #1's
   Skeptic note.
