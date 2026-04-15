---
name: build-paper-dossier
description: Create or refresh manuscript support pages for a target
  paper. Updates contribution framing, citations, objections, and
  writing-support artifacts.
---

# Build Paper Dossier

## When to use

- A target paper is entering active drafting.
- The evidence base underlying an existing dossier has shifted enough
  that positioning, citations, or objection framing is stale.
- Before a manuscript milestone (e.g., submission, major revision).

## Before starting

1. Read `AGENTS.md`.
2. Read `docs/review-policy.md` — pay attention to the `[LIT]`,
   `[PROJECT]`, `[DRAFT]` labeling rules.
3. Read the existing dossier directory at
   `wiki/papers/<paper_target>/`.

## Inputs

- The `paper_target` slug (e.g., `paper1_attention_economy`).
- Optionally, a specific section of the dossier to focus on.

## Procedure

1. **Read the current dossier directory.** Note what exists and what
   is empty.
2. **Gather relevant evidence.** Read:
   - Every theme page tagged with this `paper_target`.
   - Every source card tagged with this `paper_target`.
   - Every method page and debate page touching the themes this
     paper engages.
   - Every `claim-registry.yaml` entry whose `census_papers` list
     includes this target.
3. **Update or create the four or five dossier pages:**
   - `dossier.md` — contribution claim, literature gap, supporting
     citations, limiting citations, open holes.
   - `reviewer_defense.md` — anticipated objections with
     pre-assembled responses. Each objection should be framed as a
     reviewer might frame it, with the response grounded in cited
     sources and the project's own evidence.
   - `claims_we_cannot_test.md` — explicit limitations. What does
     the Census data not support, and which reviewer questions can
     only be answered by acknowledging the limitation?
   - (Paper 1 only) `lit_review_assembly.md` — pre-drafted paragraphs
     assembled from cited source cards.
   - (Paper 1 only) `methods_positioning.md` — comparison table of
     the project's methodological choices against those in the
     literature.
4. **Label every section.** `[LIT]` for literature synthesis,
   `[PROJECT]` for internal project reasoning, `[DRAFT]` for
   manuscript-candidate language. Paragraphs that mix the three
   kinds of writing must be split.
5. **Only produce `[DRAFT]` content** when the underlying source
   cards are at least `citation-checked`. If they are not, leave
   the section at `[LIT]` or `[PROJECT]` and note that drafting is
   blocked on verification.
6. **Flag every hole.** Distinguish acquisition holes (missing source)
   from judgment holes (interpretive question requiring a human).
7. **Ensure claim-registry consistency.** Every claim cited in the
   dossier must appear in `data/claim-registry.yaml` with this
   `paper_target` listed in `census_papers` and this dossier page
   listed in `appears_in`.
8. **Update YAML frontmatter** including verification counts and
   `last_refreshed`.
9. **Append to `ops/log.md`** and commit to branch
   `dossier/<paper_target>`.

## Constraints

- No manuscript-facing prose (`[DRAFT]`) from pages below
  `citation-checked`.
- No collapse of `[LIT]` and `[PROJECT]` labels within a single
  paragraph.
- All dossier page changes require PI or designated coauthor review
  before merge. The agent opens the PR; a human merges.
- Do not upgrade any claim from `[🤖]` to `[✓]` unless you are also
  cross-checking the original source as part of this operation. If
  you do cross-check, record which claims you checked.

## Expected output

- Updated or newly-created dossier pages under
  `wiki/papers/<paper_target>/`.
- Updated `data/claim-registry.yaml` entries (cross-references).
- New entry in `ops/log.md`.
- One PR on branch `dossier/<paper_target>` awaiting human review.
