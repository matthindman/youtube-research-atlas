# Workflows

This document describes the five canonical workflows in more detail
than the SKILL.md files. The skills are the operational specs; this
is the narrative explanation for humans getting oriented.

## 1. `ingest-source` — adding a paper or report

**Trigger:** A new source needs to enter the atlas.

**Flow:**

1. The agent reads the full source (PDF or markdown conversion).
2. It assigns an evidence tier per `docs/evidence-tiers.md`.
3. It creates or updates an entry in `data/source-registry.yaml` with
   metadata, census relevance, and provisional theme tags.
4. It creates a source card in `wiki/sources/<source_id>.md` using
   `templates/source-card.md`. Every claim is marked `[🤖]`.
5. It checks `data/project-taxonomy.yaml` aliases for each concept in
   the source and maps to existing theme/method pages where possible.
6. It extracts reusable cross-cutting claims. For claims already in
   `data/claim-registry.yaml`, it updates the existing entry (adding
   the new source to `supporting_sources` or `conflicting_sources`).
   For genuinely new cross-cutting claims, it adds new registry
   entries.
7. It updates the minimum necessary theme and method pages. New
   information carries inline citations and `[🤖]` markers.
   Contradictions with existing content are recorded explicitly with
   both citations — never silently replaced.
8. If a theme page exceeds 400 lines or now covers distinct debates,
   the agent consults `split_candidates` in the taxonomy and proposes
   a debate page split.
9. It updates `wiki/index.md` and appends a dated entry to
   `ops/log.md`.
10. It commits to a branch named `ingest/<source_id>` and opens a PR.

**Output:** one source card, registry updates, theme/method page
updates as needed, one PR.

## 2. `ingest-from-review` — bootstrap from the literature review

**Trigger:** Phase 1 seed corpus ingest only. The existing literature
review at `sources/internal/literature_review_2022_2026.md` provides
pre-synthesized summaries we can cross-check against originals.

**Flow:**

1. Read the literature review section for the target paper.
2. Read the original paper, focusing on claims, methods, and findings.
3. Cross-check: verify that the literature review's key claims match
   the original at the cited pages.
4. Proceed with the normal `ingest-source` steps 2–10.
5. Because a human authored the literature review and the agent has
   verified the original, cross-checked claims can start at `[✓]`
   instead of `[🤖]`. Claims introduced by the agent beyond what the
   literature review covered still start at `[🤖]`.

**Output:** same as `ingest-source`, but with a higher baseline
verification coverage.

## 3. `refresh-theme` — updating a theme page

**Trigger:** A theme has accumulated 3+ new sources since its last
refresh, or a collaborator has asked a broad question the current
theme page does not answer well, or a paper draft needs refreshed
positioning in a specific area.

**Flow:**

1. Read the current theme page.
2. Read all linked source cards and recent `claim-registry.yaml`
   entries tagged with this theme.
3. Rewrite consensus and disagreement sections to reflect the full
   source set. Disagreement must survive — no flattening.
4. Update the "what this means for our project" section explicitly
   with paper target links.
5. Add missing cross-links to method pages, debate pages, and paper
   dossiers.
6. Evaluate split rules (>400 lines, or distinct evidence bases with
   different conclusions). If the page should split, consult
   `split_candidates` in `project-taxonomy.yaml` and create debate
   pages on a separate PR.
7. Update frontmatter including verification counts.
8. Commit to `refresh/<theme_slug>` and open a PR.

**Output:** refreshed theme page, possibly new debate pages, one PR.

## 4. `build-paper-dossier` — manuscript support pages

**Trigger:** A target paper is entering active drafting, or its
evidence base has shifted enough that the dossier is stale.

**Flow:**

1. Read the current dossier directory under `wiki/papers/<paper>/`.
2. Read all theme pages, method pages, and source cards tagged with
   this `paper_target`.
3. Update or create:
   - `dossier.md` — contribution claim, literature gap, supporting
     citations, limiting citations, open holes.
   - `reviewer_defense.md` — anticipated objections with
     pre-assembled responses.
   - `claims_we_cannot_test.md` — explicit limitations and what the
     data does not support.
   - (Paper 1 only) `lit_review_assembly.md` — pre-drafted paragraphs.
   - (Paper 1 only) `methods_positioning.md` — comparison table.
4. Label every section with `[LIT]`, `[PROJECT]`, or `[DRAFT]`.
5. Keep manuscript-like prose separate from evidence notes.
6. Flag any hole requiring acquisition (missing source) or human
   judgment (interpretive question).
7. Ensure all claims cited in the dossier appear in
   `data/claim-registry.yaml`.
8. Commit to `dossier/<paper_target>` and open a PR. PI or designated
   coauthor review is required before merge.

**Output:** refreshed dossier directory, one PR.

## 5. `lint-atlas` — periodic health check

**Trigger:** Weekly during Phase 1; monthly afterward; on demand
before a manuscript milestone.

**Flow:**

The agent runs a sequence of checks (see
`.agents/skills/lint-atlas/SKILL.md` for the full list) and writes a
dated markdown report to `ops/lint-reports/lint-YYYY-MM-DD.md` with
critical issues, warnings, suggested fixes, and verification coverage
statistics.

**Output:** one lint report. No automatic fixes — the report informs
the next round of ingests and refreshes.

## Quality calibration pause

After the first batch of ingests (Batch 1: descriptive-deficit
papers), stop for a 2–3 hour human review:

- Are source cards accurate where spot-checked?
- Do theme page updates correctly synthesize across sources?
- Are evidence inventory tables well-structured?
- Are cross-references sensible?
- Is the taxonomy capturing the right concepts?

Adjust templates, skills, and `project-taxonomy.yaml` as needed
**before** continuing to Batch 2. This pause is the cheapest
intervention available — do not skip it.
