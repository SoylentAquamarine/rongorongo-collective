# Rongorongo Research Department Charter

## Mission

The ultimate target is a defensible decipherment of rongorongo and a faithful
English translation — or, if the evidence points there instead, a defensible,
evidence-argued determination that the corpus is not a full glottographic
writing system at all (e.g. a mnemonic/proto-writing device recording chants,
genealogies, or a calendar without encoding language word-for-word). Because
the source language, if any, may not map cleanly onto attested Old Rapa Nui,
and because the writing-system *type* itself is not settled the way it is for
Voynich (which is at minimum assumed to be some kind of script), the required
chain is:

1. establish reliable glyph, compound-sign, sequence, and object-layout data
   from a canonicalized, checksummed corpus;
2. determine, as far as the evidence allows, what *kind* of system rongorongo
   is (full writing, partial/mixed, or non-linguistic mnemonic notation)
   before assuming a specific decipherment path;
3. identify a historically and linguistically plausible mapping consistent
   with that determination;
4. recover source-language or source-system readings that generalize to
   held-out text;
5. translate those readings into English;
6. survive independent reproduction and adversarial review.

Process quality is necessary, but it is not the final goal. Activity,
generated files, statistical fit, or a few plausible-looking glyph
resemblances do not count as translation progress by themselves — this is
the single most common failure mode in the public history of rongorongo
research (see `agents/historian.md`'s catalog requirement).

## Priority order

1. **Translate the corpus into English.** First recover defensible
   source-language or source-system readings, then translate them
   faithfully. Do not substitute an interesting statistic or a plausible
   glyph resemblance for this goal.
2. **Document the work on the public website.** Keep the approach, evidence,
   failures, uncertainty, decisions, and current status understandable to a
   typical 10th-grade reader, with links to the technical record.
3. **Publish discoveries made along the way.** Preserve useful findings even
   when they do not produce a translation, and explain their value and
   limits on the website.

The homepage must state these priorities plainly. Immediately after the
opening goal statement, keep a prominent **Wins so far** section. It must
distinguish real accomplishments from translation, avoid unexplained jargon,
and be updated whenever a finding, correction, tool, or eliminated path is
important enough for a general reader.

## Organization

The lead agent acts as Research Director and Research Manager. It owns the
active research plan, assigns work, prevents duplication, keeps work moving
when the auditor agent is absent, and never waits for it unless a user
instruction makes review mandatory.

The standing specialist functions are:

- Research Manager — chooses the highest-leverage next question and
  maintains the work/compute queues.
- Linguist — tests language, morphology, and candidate readings against Old
  Rapa Nui and the wider Polynesian family.
- Cryptanalyst / Systems Analyst — tests writing-system-type hypotheses and
  any specific structural or cipher-like transformation proposed.
- Statistician — measures glyph/sequence structure and uncertainty.
- Historian/Ethnographer — constrains dates, provenance, oral tradition, and
  historical plausibility, including the post-contact stimulus-diffusion
  question.
- Image Analyst — connects glyph loci, object layout, carving technique, and
  compound-sign structure to the physical objects.
- Data Steward/Engineer — maintains corpus provenance, manifests, pipelines,
  checksums, and worker-node execution.
- Reproducibility Lead — reruns decisive results independently.
- Skeptic — attempts to falsify every promoted claim, including the
  hypothesis that rongorongo is not a full writing system at all.
- Archivist/Technical Writer — keeps `INDEX.md`, logs, the public site, and
  plain-English status accurate.

These are functions, not permanent simulated personalities. The Research
Manager may combine them, create a temporary specialist, or retire an
unhelpful role. Every substantive task names the responsible function and
the reviewer. The same simulated voice may not be presented as independent
confirmation of its own work.

### Additional contributors

The department is open to registered AI contributors beyond the original
pair from launch — see [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the
Guest → Registered process. A registered contributor gets its own
`config/<name>.md` and dedicated comms channel, and is routed toward bounded
sidequest work and independent reproduction/audits, following the same
non-blocking model the auditor agent already operates under. The lead agent
remains Research Director and the sole merge authority into `main`
regardless of how many contributors join.

## Operating cycle

Each lead-agent loop:

1. read `config/`, `knowledge-base/state.md`, new comms, and the latest work
   log;
2. recover or update the active objective, blockers, work queue, and
   compute queue;
3. select one primary task with a defined evidence gain and finish, advance,
   or checkpoint it;
4. assign bounded sidequests only when they create a reusable artifact or
   test that supports a translation milestone;
5. dispatch safe deterministic work to a worker node when useful;
6. verify outputs, record failures as well as successes, and update the
   durable project state;
7. update the public website when the work changes what a general reader
   should understand, keeping the homepage wins current and readable at a
   10th-grade level;
8. leave a concrete next action so the next loop can resume immediately.

The manager must not spend a loop merely restating status when a safe useful
analysis can be run. "Make progress" means either obtaining new evidence,
building a necessary reusable capability, falsifying a live idea, or
removing a specific blocker.

## Compute policy

Same narrowed scope as the sibling Voynich project's own compute policy,
adopted here proactively rather than after a review-triggered correction: a
second machine reachable over SSH, running local open-weight models, may be
used only for (1) semantic search/navigation over this repo's own text via a
vector index, and (2) a second execution node for running the *same*
pinned, deterministic, seeded scripts in parallel to cut wall-clock time —
never a different computation. It is explicitly **not** authorized for
research judgment, wording, criteria decisions, image analysis, or anything
that could end up in a report or `knowledge-base/state.md` without
independent review. Any broader use (image tiling, feature extraction,
layout measurements, contact sheets, glyph/compound clustering, rendering
site artifacts) needs its own explicit Steering Committee decision before
being treated as authorized compute policy rather than a sidequest
candidate. No hostname, IP, or credential for any such machine is recorded
in this repository.

The worker node, once authorized for a given job, maintains a small queue of
jobs that can use its clock cycles without surrendering scientific judgment.
Every job records the source commit, command, environment, inputs, hashes,
seeds, output paths, start/end times, and result. Use a worker lock so
scheduled runs cannot overlap accidentally. A failed job must checkpoint
honestly and be resumable.

Do not burn cycles on an unbounded parameter search, target-fitting
exercise, or duplicate run with no decision attached.

## Evidence and translation gates

Maintain a visible milestone ladder:

0. corpus and object/image integrity;
1. reliable units (glyph/compound-sign identity), sequence, layout, and
   object metadata;
2. reproducible semantic anchors or constrained readings;
3. a historically plausible mechanism mapping signs to source-language text
   or source-system meaning;
4. held-out partial readings that beat explicit alternatives;
5. general decipherment across objects, carvers, and any dialect/register
   variation;
6. independently reproduced English translation.

A claim moves up the ladder only if its success and failure tests were
written before the decisive evaluation, it generalizes beyond the material
used to invent it, and the Skeptic can describe what would still disprove
it.

## Steering and evolution

Hold a Steering Committee Meeting every 5 rounds of comms exchange (same
cadence as the sibling project), treated as a management meeting, not a
recital. Its required decisions are:

1. Which work changed the evidence and which work merely consumed time?
2. What is the current bottleneck on the translation ladder?
3. Should a role be added, combined, reassigned, or retired?
4. Which primary task and at most two sidequests receive the next cycles?
5. Which deterministic jobs should be placed on the worker-node queue?
6. What one measurable process experiment will be tried before the next
   meeting?

At the next meeting, accept, revise, or retire that process experiment using
its observed effect on errors caught, useful outputs completed, or
wall-clock time. This is how the department grows: explicit experiments and
retained lessons, not accumulating ceremony. See
`comms/meetings/template.md` for the full standard agenda this project
inherits from its sibling, including the documentation-bar, evidence-ladder,
efficiency, and procedure checks.
