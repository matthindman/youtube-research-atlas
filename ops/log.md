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

## 2026-04-15 — Ingest ormen_gregersen_2023_engagement
**Operation:** ingest-source
**Branch:** ingest/ormen_gregersen_2023_engagement
**By:** Codex (GPT-5)

Ingested `ormen_gregersen_2023_engagement` using the
`ingest-from-review` workflow conservatively. Created
`wiki/sources/ormen_gregersen_2023_engagement.md` and
updated `data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/creator_economy.md`, and `wiki/index.md`.

Literature-review cross-check discrepancy:

- I could not locate a dedicated section for this paper in
  `sources/internal/literature_review_2022_2026.md`, despite the
  Batch 2 instruction that the review covers all six sources.
  Because of that mismatch, I did **not** bootstrap any inline
  source-card claims to `[✓]`.
- There is a short internal summary for this paper in
  `sources/internal/research_questions_report.md`, but per the
  updated skill I treated that as project context only, not as a
  substitute verification scaffold.

Tier and taxonomy decisions:

- Assigned `primary_empirical` and `journal_article`.
- Reused existing theme tag `creator-economy`; no taxonomy
  addition proposed on this branch.

Claims not fully verifiable from this source alone:

- The paper is a document analysis of platform communication,
  not a behavioral or payout study, so claims about direct creator
  outcomes remain inferential rather than measured here.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/ormen_gregersen_2023_engagement?quick_pull=1&title=%5Bingest-from-review%5D%20%C3%98rmen%20and%20Gregersen%202023%20%28Towards%20the%20Engagement%20Economy%29&body=%23%23%20Summary%0A-%20Ingested%20%60ormen_gregersen_2023_engagement%60%20via%20%60ingest-from-review%60%20with%20all%20source-card%20claims%20left%20at%20%60%5B%F0%9F%A4%96%5D%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20creator-economy%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/ormen_gregersen_2023_engagement.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/creator_economy.md%0A-%20wiki/index.md%0A-%20ops/log.md
