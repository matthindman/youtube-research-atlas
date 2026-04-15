---
name: lint-atlas
description: Health-check the atlas for unsupported claims, stale
  synthesis, missing links, taxonomy drift, and quality issues.
---

# Lint Atlas

## When to use

- Weekly during Phase 1.
- Monthly in steady state.
- On demand before a manuscript milestone.

## Before starting

1. Read `AGENTS.md`.
2. Read `data/project-taxonomy.yaml`.
3. Read `docs/review-policy.md`.

## Checks to run

### Structural checks

1. **Orphan pages** — pages with no inbound wikilinks from any other
   page.
2. **Broken wikilinks** — `[[...]]` references that don't resolve.
3. **`[NEEDS CITATION]` markers** — list every occurrence with
   location.
4. **Stale pages** — pages not updated in >60 days (in steady state)
   or >14 days (during active Phase 1 ingest).
5. **Duplicate concepts** — concepts appearing in multiple pages that
   lack their own canonical page or `project-taxonomy.yaml` entry.

### Registry checks

6. **Pending sources** — `source-registry.yaml` entries with
   `status: pending`.
7. **Registry/card mismatches** — source cards whose `source_id`
   has no registry entry, or registry entries with no corresponding
   card.
8. **Unindexed claims** — claims appearing in multiple pages but not
   tracked in `claim-registry.yaml`.
9. **Stale claim registry** — claim-registry entries whose
   `appears_in` list no longer matches where the claim actually
   appears in the wiki.

### Quality checks

10. **Verification coverage** — per page and overall, the share of
    claims at `[🤖]`, `[✓]`, `[✓✓]`, `[NEEDS CITATION]`. Report
    distribution.
11. **Evidence tier compliance** — any `project_internal` sources
    being cited as external evidence about YouTube? Any
    `industry_report` sources supporting causal or consensus claims?
12. **Temporal scoping** — any synthesis pages in themes flagged
    `temporal_scoping_required: true` that lack a `temporal_scope`
    field in frontmatter?
13. **Paper dossier completeness** — empty sections in any dossier;
    dossiers where `[DRAFT]` content appears in pages below
    `citation-checked`.
14. **Status consistency** — any pages marked `human-reviewed` with
    >20% `[🤖]` claims; any pages marked `stable` with any non-`[✓]`
    /`[✓✓]` claims.
15. **Taxonomy compliance** — any pages using concept names that
    aren't in `project-taxonomy.yaml` or its aliases.
16. **Theme size** — any theme pages exceeding 400 lines (split
    candidate).

## Output

A dated markdown report at `ops/lint-reports/lint-YYYY-MM-DD.md`
containing:

1. **Summary line** — counts of critical issues, warnings, info notes.
2. **Critical issues** — evidence tier violations, status/verification
   inconsistencies, broken registry integrity.
3. **Warnings** — stale pages, high `[🤖]` density, split candidates,
   missing cross-links.
4. **Suggested fixes** — for each warning, the next ingest/refresh
   that would resolve it.
5. **Verification coverage statistics** — current distribution and
   trend against the last report if available.
6. **Pages to review next** — prioritized list.

## Constraints

- Lint does not modify any wiki pages. It only reads and reports.
- The lint report is the deliverable. Downstream humans and agents
  decide what to act on.
- Do not treat lint reports as authoritative about quality — they
  catch structural issues, not substantive error. Spot-checking and
  PR review are the substantive quality gates.

## Expected output

- One new file at `ops/lint-reports/lint-YYYY-MM-DD.md`.
- A short summary entry in `ops/log.md` pointing to the report.
- No commits to wiki pages.
