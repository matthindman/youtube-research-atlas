# YouTube Scholarship Atlas — Agent Instructions

This repo is an evidence-first scholarship atlas, not a freeform
knowledge dump. Everything you do here should leave the repo more
cumulative: fewer isolated facts, clearer disagreements, better routing
from literature to project papers, more reusable writing support.

## Before any operation

Read these files in order:

1. This file
2. `data/project-taxonomy.yaml` — controlled vocabulary
3. `wiki/index.md` — current page catalog
4. `docs/review-policy.md` — if you are creating or modifying pages
5. `docs/evidence-tiers.md` — if you are writing synthesis

## Non-negotiable rules

1. **Raw sources are immutable.** Never modify anything under
   `sources/`. The symlinked PDFs in `sources/papers/` are read-only.
2. **No direct quote without a page number.** Ever.
3. **No synthesis that hides disagreement.** Record disagreements
   explicitly with both sides cited.
4. **Every new claim gets a `[🤖]` marker.** Only humans upgrade to
   `[✓]` or `[✓✓]`.
5. **Never cite a `project_internal` source as evidence about YouTube
   or the broader literature.** Project memos can support project
   context only.
6. **Check `project-taxonomy.yaml` aliases before creating any page.**
   If an alias matches, update the existing page instead of creating a
   duplicate. If genuinely new, add to the taxonomy file first.
7. **No direct commits to `main`.** Work on a branch named after the
   operation (e.g., `ingest/mcgrady_2023`, `refresh/descriptive_deficit`).
8. **Distinguish `[LIT]`, `[PROJECT]`, and `[DRAFT]`** in paper dossier
   pages. These labels are load-bearing — they determine what's
   citable, what's project reasoning, and what's draft manuscript
   language.
9. **`sources/papers/model_papers/`** is excluded from the corpus. Those
   are structural exemplars for drafting, not empirical evidence about
   YouTube. Never ingest them as source cards.

## Page status model

Every wiki page carries a `status` field in frontmatter:

- `machine-draft` — agent-generated, not yet checked.
- `citation-checked` — source references and page numbers verified.
- `human-reviewed` — substance and framing reviewed by a human.
- `stable` — safe to treat as reliable internal reference.

Do not upgrade above `machine-draft` without completing the checks in
`docs/review-policy.md`. Page-level status and claim-level markers are
complementary — see the policy doc for how they interact.

## Workflows

Use the named skills in `.agents/skills/` (or `.claude/skills/`) for
all repeatable operations:

- `ingest-source` — add a new paper/report to the atlas
- `ingest-from-review` — bootstrap from the existing literature review
- `refresh-theme` — update a theme page after new sources arrive
- `build-paper-dossier` — create/refresh manuscript support pages
- `lint-atlas` — health-check the entire atlas

## Directory routing

| Path | Contains |
|------|----------|
| `sources/papers/` | Gitignored symlink to external PDF archive (read-only) |
| `sources/internal/` | Committed project memos and literature review |
| `wiki/sources/` | Literature source cards (other people's work) |
| `wiki/themes/` | Cross-source theme syntheses |
| `wiki/methods/` | Methodological approach pages |
| `wiki/debates/` | Structured controversy tracking |
| `wiki/papers/` | Manuscript dossiers (OUR papers) |
| `data/` | Mutable registries and metadata |
| `ops/` | Chronological log and lint outputs |
| `docs/` | Durable policy documents |
| `templates/` | Page templates |
| `tools/` | CLI utilities |

## What good work looks like

A strong update:

- Advances the synthesis without flattening disagreement.
- Cites page numbers.
- Tags the right themes, claims, and paper targets.
- Updates registries (`source-registry.yaml`, `claim-registry.yaml`)
  when new cross-cutting information appears.
- Leaves behind a clear commit message and an entry in `ops/log.md`.
- Does not silently promote claim or page maturity beyond what was
  verified.

When in doubt, err toward the conservative option: leave a `[🤖]`
marker, leave `status: machine-draft`, flag the uncertainty in the
log, and let a human adjudicate.
