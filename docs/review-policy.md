# Review Policy

This document specifies how pages and claims move from agent-generated
drafts to publication-ready material. Two verification systems work
together: **page-level status** for overall manuscript safety and
**claim-level markers** for inline trust.

## Dual verification system

### Page-level status

Every wiki page carries a `status` field in its YAML frontmatter.

| Status | Meaning | Safe to cite in manuscripts? |
|--------|---------|------------------------------|
| `machine-draft` | Agent-generated, not yet checked. | No. |
| `citation-checked` | Source references and page numbers verified against originals. | Generally yes, with care — check claim-level markers. |
| `human-reviewed` | Substance and framing reviewed by a human collaborator. | Yes. |
| `stable` | Safe to treat as reliable internal reference. | Yes, including as a source for manuscript prose. |

Promotion is monotonic: pages move forward, not backward, except when
a new ingest genuinely invalidates prior synthesis — in which case the
page is demoted with an explicit note in `ops/log.md`.

### Claim-level markers

Every substantive claim inside a page carries an inline marker:

| Marker | Meaning |
|--------|---------|
| `[🤖]` | **machine_extracted** — agent-generated, citation exists but has not been verified against the source. |
| `[✓]` | **human_checked** — a human verified the cited passage supports the claim as stated. |
| `[✓✓]` | **publication_ready** — verified, and the language is suitable for manuscript use without further editing. |
| `[NEEDS CITATION]` | No source yet identified. Hard block on any upgrade. |

These systems are complementary. A page can be `citation-checked`
while still containing some `[🤖]` claims — it means the *references*
were verified but some individual claims haven't had the cited passage
re-read line by line. A page **cannot** be `stable` unless every
substantive claim is `[✓]` or `[✓✓]`.

## Verification summary in frontmatter

Every page must include a verification counter:

```yaml
status: machine-draft
verification:
  machine_extracted: 12
  human_checked: 8
  publication_ready: 3
  needs_citation: 1
```

Agents update these counts whenever they add or modify claims.
`tools/lint.sh` will flag pages where counts are stale or inconsistent
with the page body.

## PR review protocol

- **Spot-check at minimum 30%** of claims in new source cards against
  the actual source. For high-relevance papers (flagged
  `census_relevance: high` in the source registry), spot-check at
  least 50%.
- **Upgrade verified claims** from `[🤖]` to `[✓]` in the PR itself,
  not in a follow-up commit. This keeps the verification trail in the
  review record.
- **Flag incorrect claims** with a PR comment and either fix them in
  the PR or open a follow-up issue.
- **Merge thresholds:**
  - Source cards for high-relevance papers: do not merge if more than
    50% of substantive claims remain `[🤖]` after review.
  - Theme syntheses touching multiple papers: do not merge if any
    cited paper is absent from `data/source-registry.yaml`.
  - Paper dossier changes: require PI or designated coauthor review
    before merge. No exceptions.
- **PR title format:** `[skill-name] short description` — e.g.,
  `[ingest-source] McGrady 2023 (Dialing for Videos)`.
- **Branch naming:** `ingest/<source_id>`, `refresh/<theme_slug>`,
  `dossier/<paper_target>`, `lint/<YYYY-MM-DD>`.

## Section labels in paper dossiers

Paper dossier pages mix three kinds of writing that must never be
confused. Label every section with one of:

- **`[LIT]`** — Literature synthesis. Citable in manuscripts as
  evidence about the field. Claims must be traceable to source cards.
- **`[PROJECT]`** — Internal project reasoning. Not citable as
  evidence about YouTube. Captures what the Census project believes or
  plans, which is different from what the literature has established.
- **`[DRAFT]`** — Manuscript-candidate language. Needs final editing
  before submission but is explicitly authored with a target paper in
  mind. Only produce `[DRAFT]` content in pages whose status is at
  least `citation-checked`.

These labels are not decoration. They are the mechanism that keeps
literature synthesis, project inference, and draft prose from
collapsing into a mixed zone where nobody can tell what the field has
established versus what we are trying to argue.

## Separation rules

- **No mixing** of literature claims and internal project inference
  within a paragraph without labels.
- **No manuscript-facing prose** (`[DRAFT]`) from pages below
  `citation-checked`.
- **No silent collapse of disagreement into consensus.** If two
  sources disagree, the disagreement must survive synthesis —
  typically as a row in an evidence inventory or as its own entry in
  a debate page.
- **No promotion without checks.** Agents never move a page from
  `citation-checked` to `human-reviewed`. That is a human action
  recorded by a human-authored commit.

## When things go wrong

If you discover that an already-merged page contains an incorrect
claim:

1. Fix the claim on a branch named `fix/<page-or-claim-id>`.
2. Note the original error and the correction in `ops/log.md`.
3. If the claim appears in `data/claim-registry.yaml`, update every
   page listed under `appears_in`.
4. If the claim was cited in a paper dossier section marked `[DRAFT]`,
   flag the dossier page for re-review and mention the PI.

Errors are expected. The system is designed to catch and correct
them, not to prevent them from ever occurring.
