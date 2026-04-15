# Operations Log

Chronological record of significant operations on the atlas. Every
ingest, refresh, dossier build, lint pass, and scaffold change gets
an entry here. Entries are append-only in chronological order.

Format:

```
## YYYY-MM-DD — <short title>
**Operation:** <ingest-source | refresh-theme | build-paper-dossier | lint-atlas | scaffold | fix>
**Branch:** <branch name or "main" for direct scaffold commits>
**By:** <agent or human name>

<brief summary of what happened, what pages were touched, what
decisions were made, and anything that needs human attention>
```

---

## 2026-04-15 — Phase 0 scaffold
**Operation:** scaffold
**Branch:** main
**By:** Claude Code (Opus 4.6)

Initial scaffold of the YouTube Scholarship Atlas. Created the full
directory structure, root instruction files (`AGENTS.md`, `CLAUDE.md`,
`README.md`), policy documents under `docs/`, registries under
`data/`, templates under `templates/`, skills under `.agents/skills/`
and mirrored to `.claude/skills/`, tool scripts under `tools/`, and
seed wiki pages: index, overview, six theme stubs, and three paper
dossier directories (methods companion, Paper 1 attention economy,
Paper 2 mobility).

Key placement decisions:

- Atlas lives at `/Users/hindman/youtube-scholarship-atlas/` — a
  top-level directory, sibling to `paper archive/`. This keeps the
  shareable, versioned atlas cleanly separated from the unstructured
  PDF archive.
- `sources/papers/` is a gitignored symlink to
  `/Users/hindman/paper archive/YouTube/`. PDFs are never committed
  to GitHub. Collaborators need their own copy of the paper archive.
- `sources/internal/` holds committed copies of the literature review,
  both project memos, the research plan, and the research questions
  report. These are markdown, shareable, and safe for Git.
- `sources/papers/model_papers/` is excluded from ingest by explicit
  rule in `AGENTS.md`. Those are structural exemplars for our own
  drafting, not YouTube evidence.

**Status:** Phase 0 complete. Phase 1 (seed corpus ingest) has not
yet started. The first ingest should use the `ingest-from-review`
skill on Batch 1: McGrady et al. 2023, Munger 2024, Munger et al.
2025, Norton & Shapiro 2024, and McGrady et al. 2025. Pause for
quality calibration after Batch 1 before continuing.

**Human action items:**

1. Create the private GitHub repo and push the initial scaffold.
2. Set branch protection on `main` (require PR, one approval).
3. Add collaborators: Philip Waggoner, Josh Tucker, and others as
   needed.
4. Trigger Batch 1 ingest, either via Codex or via an interactive
   Claude Code session using the `ingest-from-review` skill.

## 2026-04-15 — Ingest newman_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/newman_et_al_2025
**By:** Codex (GPT-5)

Ingested `newman_et_al_2025` via the `ingest-from-review`
workflow. Created `wiki/sources/newman_et_al_2025.md` and
updated `data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/news_ecosystem.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material discrepancy found. The literature review's
  discussion of commentary dominance, fuzzy category boundaries,
  cross-border export of right-leaning US commentators, and the
  85% male figure matches the report's own findings (pp. 10,
  13-14).

Tier and taxonomy decisions:

- Assigned `industry_report` rather than `policy_research`, per
  the updated Batch 2 instruction. This is the canonical
  `industry_report` case: original data and analysis housed in a
  research-adjacent institute rather than a peer-reviewed venue.
- Tagged to both `news-ecosystem` and `creator-economy`, but
  limited this branch's theme update to `wiki/themes/news_ecosystem.md`.

Claims not fully verifiable from this source alone:

- The report maps audience-reported attention and creator
  categories, but it does not directly measure actual exposure,
  reliability, or business sustainability.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/newman_et_al_2025?quick_pull=1&title=%5Bingest-from-review%5D%20Newman%20et%20al.%202025%20%28Mapping%20News%20Creators%20and%20Influencers%29&body=%23%23%20Summary%0A-%20Ingested%20%60newman_et_al_2025%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20news-ecosystem%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/newman_et_al_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/news_ecosystem.md%0A-%20wiki/index.md%0A-%20ops/log.md
