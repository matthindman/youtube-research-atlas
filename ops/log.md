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

## 2026-04-15 — Refresh creator_economy
**Operation:** refresh-theme
**Branch:** refresh/creator_economy
**By:** Codex (GPT-5)

Refreshed `wiki/themes/creator_economy.md` after the Batch 2
ingests. This synthesis was built from pushed source cards on
`ingest/rieder_et_al_2023`, `ingest/verwiebe_et_al_2025`,
`ingest/ormen_gregersen_2023_polymorphism`,
`ingest/ormen_gregersen_2023_engagement`, and
`ingest/newman_et_al_2025`.

Key synthesis decisions:

- Preserved the central disagreement between diversification at
  the strategic level and an overarching engagement-market logic
  at the platform level.
- Kept Newman et al. in scope because its source card explicitly
  tags `creator-economy`, but treated it as supplementary evidence
  about a news-adjacent creator niche rather than as a direct
  earnings or labor study.
- Kept all claims at `[🤖]` and limited this branch to the theme
  page plus log entry, per the Batch 2 refresh instruction.

Split evaluation:

- No split proposed yet. The page remains comfortably below the
  400-line threshold and the disagreements still cohere within a
  single creator-economy synthesis.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/creator_economy?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20creator_economy&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/creator_economy.md%60%20from%20the%20Batch%202%20source%20cards.%0A-%20Preserved%20disagreement%20between%20diversification%20and%20engagement-market%20standardization.%0A-%20Kept%20this%20branch%20limited%20to%20the%20theme%20page%20and%20ops%20log.%0A%0A%23%23%20Sources%0A-%20rieder_et_al_2023%0A-%20verwiebe_et_al_2025%0A-%20ormen_gregersen_2023_polymorphism%0A-%20ormen_gregersen_2023_engagement%0A-%20newman_et_al_2025%0A%0A%23%23%20Pages%0A-%20wiki/themes/creator_economy.md%0A-%20ops/log.md
