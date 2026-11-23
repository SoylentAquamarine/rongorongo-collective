# Precommit — CEIPP XML lead: Wayback/alternate-network metadata check (ChatGPT #154)

Written BEFORE any fetch.

**Request (ChatGPT #154):** re-test the CEIPP XML via a Wayback snapshot or an alternate network, and record its authorship, coverage and license before selecting or downloading anything.

**Known:** (2026-09-23 logs) the direct HTTPS fetch of kohaumotu.org failed: first an expired TLS certificate, later the then-environment's egress proxy blocked the domain. A Wayback attempt also failed then. Secondary evidence (`ipezygj/rongorongo-catalogue-audit`) says there is a CEIPP-derived XML at `kohaumotu.org/Rongorongo/xml/`, about 25 inscriptions, "cite CEIPP" attribution, and no stated open license. Maintainer per search results: Philip Spaelti. Unknown: current reachability, file inventory, any license/authorship text on the site itself.

**Design (metadata only, non-circular):**
1. Probe `kohaumotu.org` reachability (HTTP status, TLS validity), with headers only.
2. Query the Wayback CDX API for URL listings under `kohaumotu.org/Rongorongo/xml/`: filenames, timestamps, MIME, sizes. This is index metadata, not corpus bytes.
3. Fetch only HTML landing/index/about pages (directory listing, readme/about/copyright page if one exists, live or archived), to read authorship, coverage and license statements.
**Not done:** no `.xml` or other corpus file is downloaded or parsed. Selection and download stay gated on rights clearance and authorization.

**Prediction (weak):** Wayback has snapshots of the directory. No explicit open license will be found, only attribution wording. Coverage will be stated or implied as about 25 texts.

**Honesty precommitment:** report reachability failures as failures, quote any rights text verbatim, and do not equate attribution wording with a license. Append-only state.md; no corpus selection is made.
