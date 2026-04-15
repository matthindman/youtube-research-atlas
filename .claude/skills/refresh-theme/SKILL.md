---
name: refresh-theme
description: Refresh a theme page after new sources are ingested.
  Preserves consensus/disagreement structure and updates project
  links.
---

# Refresh Theme

## When to use

- After ingesting 3+ sources touching the same theme.
- When a collaborator asks a broad question the current theme page
  does not answer well.
- When a paper draft needs refreshed positioning in a specific area.
- As part of the Phase 1 batch ingest: after each batch, refresh
  every theme the batch touched.

## Before starting

1. Read `AGENTS.md`.
2. Read `data/project-taxonomy.yaml` (especially the entry for this
   theme and its `split_candidates`).
3. Read `docs/review-policy.md`.

## Inputs

- The `canonical_name` (slug) of the theme to refresh.

## Procedure

1. **Read the current theme page** at
   `wiki/themes/<canonical_name>.md`. Note its current consensus,
   disagreements, and evidence inventory.
2. **Read all linked source cards** — every source currently cited in
   the theme page, plus any source card whose frontmatter tags this
   theme.
3. **Read recent `claim-registry.yaml` entries** tagged with this
   theme.
4. **Rewrite the consensus section** to reflect the full source set.
   - What does the evidence base actually agree on?
   - Distinguish replicated findings from widely-held assumptions
     from theoretical convergence.
5. **Rewrite the disagreement section.** Do not flatten. For each
   contested claim, name both sides and cite the sources driving
   each.
6. **Rebuild the evidence inventory table** so that every current
   source appears with its claim, evidence, strength, period, and
   verification status.
7. **Update the "methodological reasons for disagreement" section.**
   Often this is the most useful part of the page for our own methods
   work — when sources disagree, is it driven by method, sample, or
   period differences?
8. **Update the "what this means for our project" section** with
   explicit links to relevant paper dossiers and methods pages.
9. **Add missing cross-links** to method pages, debate pages, and
   paper dossiers.
10. **Evaluate split rules.** If the refreshed page now exceeds 400
    lines, or covers distinct debates with different evidence bases
    and conclusions, consult `split_candidates` in the taxonomy and
    propose a debate page split on a separate PR. Do not perform the
    split in the same PR as the refresh.
11. **Update YAML frontmatter:** `last_refreshed`, `source_count`,
    `key_sources`, verification counts.
12. **Keep every claim grounded.** Do not infer beyond cited sources.
    If the refresh surfaces a claim nothing cites, mark it
    `[NEEDS CITATION]`.
13. **Append to `ops/log.md`** and commit to branch
    `refresh/<canonical_name>`.

## Constraints

- Preserve disagreement. No silent collapse to consensus.
- Do not upgrade any claims beyond `[🤖]` — verification is a human
  action.
- Do not change page status above `machine-draft`.
- If the refresh changes a claim that appears in
  `data/claim-registry.yaml`, also update the registry entry.

## Expected output

- Refreshed `wiki/themes/<canonical_name>.md`.
- Updated `data/claim-registry.yaml` if cross-cutting claims changed.
- New entry in `ops/log.md`.
- Possibly a follow-up PR proposing a debate page split.
- One PR on branch `refresh/<canonical_name>`.
