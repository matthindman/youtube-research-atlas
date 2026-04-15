# YouTube Scholarship Atlas

A private, Git-based, agent-maintained evidence layer for the **YouTube
Channel Census** research program. LLM agents (Codex, Claude Code)
ingest papers and reports and maintain structured markdown pages;
humans supervise promotion and interpretation; manuscript drafting
draws from paper dossiers rather than from raw PDFs or chat logs.

The raw PDFs are the archive. The atlas is the maintained evidence
layer. Manuscript prose sits above the atlas, not inside it.

## Quick start

1. Read `AGENTS.md` (or `CLAUDE.md` — mirrors). Everything an agent
   needs to route through the repo is there.
2. Read `docs/review-policy.md` and `docs/evidence-tiers.md` for the
   quality system.
3. Read `data/project-taxonomy.yaml` for the controlled vocabulary.
4. Follow one of the skills in `.agents/skills/` or `.claude/skills/`
   for any repeatable operation.

## Repository layout

```
sources/            # Raw materials (papers/ is a gitignored symlink
                    # to the external PDF archive; internal/ holds
                    # committed project memos and the literature review)
wiki/               # Agent-maintained synthesis
  sources/          # Per-paper source cards (other people's work)
  themes/           # Cross-source theme syntheses
  methods/          # Methodological approach pages
  debates/          # Structured controversy tracking
  papers/           # Manuscript dossiers (OUR papers)
data/               # Mutable registries (source, claim, taxonomy)
ops/                # Chronological log and lint reports
docs/               # Durable policy documents
templates/          # Page templates
tools/              # CLI utilities (search, lint, stats, citation check)
.agents/skills/     # Codex skills
.claude/skills/     # Claude Code skills (mirror of .agents/)
```

## What's in Git, what isn't

- **In Git:** all markdown pages, YAML registries, skills, templates,
  policy docs, tool scripts, and internal project memos (markdown).
- **Not in Git:** PDFs, MHTML captures, and any other canonical raw
  artifacts. `sources/papers/` is a gitignored symlink to
  `/Users/hindman/paper archive/YouTube/`. Collaborators need their
  own copy of the paper archive (or symlinks pointing to their own
  clone) to run ingest skills.

## Collaborators

- **Matt Hindman (PI)** — project lead, manuscript direction.
- **Philip Waggoner** — coauthor.
- **Josh Tucker** — coauthor.
- Additional consortium members (read access) as papers come online.

## Status

Scaffolded. Seed corpus ingest (Phase 1) has not yet started. See
`ops/log.md` for chronological state.
