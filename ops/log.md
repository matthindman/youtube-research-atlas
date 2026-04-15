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
