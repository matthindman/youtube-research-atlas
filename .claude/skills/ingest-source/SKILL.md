---
name: ingest-source
description: Ingest a new paper, report, or internal memo into the
  YouTube Scholarship Atlas. Creates or updates source card, claim
  registry, theme pages, method pages, paper dossiers, index, and log.
---

# Ingest Source

## Before starting

1. Read `AGENTS.md` (or `CLAUDE.md`).
2. Read `data/project-taxonomy.yaml`.
3. Read `docs/evidence-tiers.md`.
4. Read `docs/review-policy.md`.

## Inputs

- Path to raw source (typically under `sources/papers/`, which is a
  symlink to the external PDF archive).
- Basic citation metadata (author, year, title, venue, DOI if known).
- Whether the source is external scholarship or internal project
  material.

## Procedure

1. **Read the full source** before editing any wiki page. Do not
   summarize from the title or abstract alone.
2. **Determine evidence tier** per `docs/evidence-tiers.md`.
3. **Create or update `data/source-registry.yaml`** with the source's
   metadata, evidence tier, canonical format, themes, census relevance,
   and initial notes. Set `status: ingested` and `date_ingested` to
   today.
4. **Create the source card** at `wiki/sources/<source_id>.md` using
   `templates/source-card.md`. Every substantive claim carries a
   `[🤖]` marker and a page citation. No quote without a page number.
5. **Check `data/project-taxonomy.yaml` aliases** for every concept
   you plan to tag. If a concept matches an existing alias, use the
   canonical name. If genuinely new, add to the taxonomy file first
   (on the same branch), then use it.
6. **Extract reusable cross-cutting claims.**
   - For claims already in `data/claim-registry.yaml`, update the
     existing entry: add this source to `supporting_sources` or
     `conflicting_sources` as appropriate, update `evidence_strength`,
     and add this source card to `appears_in`.
   - For genuinely new cross-cutting claims (ones that will appear in
     multiple future pages), add a new registry entry.
   - Do NOT create registry entries for narrow, source-specific
     findings. The registry is for cross-cutting claims only.
7. **Update the minimum necessary theme and method pages.**
   - Add new information with inline citations and `[🤖]` markers.
   - If the new source contradicts existing content, record the
     contradiction explicitly: do not silently replace prior claims.
   - Update the page's YAML frontmatter (`source_count`,
     `key_sources`, `last_refreshed`, verification counts).
8. **Evaluate theme split rules.** If a theme page now exceeds 400
   lines or covers distinct debates, consult `split_candidates` in
   `data/project-taxonomy.yaml` and propose a debate page split.
   Debate-page creation is a separate PR.
9. **Update paper dossier sections** only if the source is materially
   relevant to a target paper. Label additions with `[LIT]`,
   `[PROJECT]`, or `[DRAFT]`. Do not create `[DRAFT]` content in a
   dossier whose status is below `citation-checked`.
10. **Update `wiki/index.md`** with the new page(s).
11. **Append to `ops/log.md`** with a dated entry: what was ingested,
    what pages were touched, any tier or taxonomy decisions that
    merit human review.
12. **Create, commit, verify, and push.**

    **Branch creation (mandatory protocol):**
    ```
    git fetch origin
    git switch -c ingest/<source_id> origin/main
    ```
    Always use `git switch -c` (or `git checkout -b`) to create a
    **named branch**. **NEVER use `git switch --detach` or
    `git checkout --detach`.** Detached HEAD does not track commits
    to a branch ref — pushing from detached HEAD silently creates
    an empty branch. This has caused data loss in practice.

    **Every ingest branch must be created from the current tip of
    `main`**, not from another ingest branch. When multiple sources
    are ingested in the same batch, each branch starts fresh from
    `main`. Do not stack ingest branches on top of each other.

    **Commit (mandatory — never skip):**
    ```
    git add <files>
    git commit -m "<message>"
    ```
    Never run `git push` without a preceding `git commit`. The
    sequence is always: edit → add → commit → verify → push.

    **Pre-push verification (mandatory — run all three):**
    ```
    git log --oneline -2
    # Line 1 = YOUR new commit. Line 2 = main's tip.
    # If line 1 IS main's tip, you forgot to commit.

    git diff --stat HEAD~1
    # Must show 5+ files changed, 150+ insertions.
    # If empty or shows only 1 file, something went wrong.

    git show HEAD:wiki/sources/<source_id>.md | head -3
    # Must show YAML frontmatter. If it errors, the card
    # was never committed.
    ```
    If ANY check fails, do not push. Diagnose and fix first.

    **Push:**
    ```
    git push -u origin ingest/<source_id>
    ```

    When multiple ingests in a batch touch shared files (registries,
    index, theme pages, log), merge conflicts will surface in PR
    review. That is expected and correct — the conflicts are resolved
    in the review rather than hidden via stacking. Do not reorder or
    bundle commits to avoid them.

## Constraints

- No direct quote without a page number. Ever.
- **When truncating a direct quote, mark the omission with an
  ellipsis (…).** Never silently drop words from a quote, and never
  end a quote mid-sentence without marking it — even when the source
  card's context makes the truncation obvious. Faithful quotation is
  load-bearing for the verification system.
- Never overwrite mature synthesis unless the new source requires it
  (and then record the change explicitly in `ops/log.md`).
- Preserve disagreement.
- Leave page status at `machine-draft`. Only humans promote.
- Respect evidence tier rules: `project_internal` sources cannot be
  cited as evidence about YouTube; `industry_report` sources cannot
  support causal claims or scholarly consensus.
- Never ingest anything under `sources/papers/model_papers/`. Those
  are structural exemplars for our own drafting, not YouTube evidence.

## Expected output

- One new `wiki/sources/<source_id>.md` source card.
- Updated `data/source-registry.yaml`.
- Updated `data/claim-registry.yaml` (when cross-cutting claims
  surface).
- Updated theme/method/debate/dossier pages as relevant.
- Updated `wiki/index.md`.
- New entry in `ops/log.md`.
- One PR on branch `ingest/<source_id>`.
