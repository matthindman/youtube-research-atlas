---
name: ingest-from-review
description: Bootstrap ingest using the existing literature review as
  a verification scaffold. Used during Phase 1 seed corpus only.
---

# Ingest From Review

## When to use

Phase 1 seed corpus only. The existing literature review at
`sources/internal/literature_review_2022_2026.md` provides
pre-synthesized summaries written by a human project member. For
papers covered by the literature review, the agent can use it as a
verification scaffold — cross-checking its claims against the
original paper before ingest.

After Phase 1 is complete, switch to the standard `ingest-source`
skill for new arrivals.

## Before starting

Same as `ingest-source`.

## Procedure

1. **Read the literature review section** for the target paper.
   Identify the specific claims the review attributes to this source.
2. **Read the original paper**, focusing on claims, methods, and
   findings. Locate the passages the literature review cites.
3. **Cross-check.** For each claim the literature review makes about
   this source:
   - Does the original support it at the cited page?
   - Is the language accurate, or has it been compressed or shaded?
   - Does the scope of the original claim match the scope the review
     gives it?
4. **Flag any mismatches in `ops/log.md`.** Do not silently correct
   them without noting the discrepancy — the literature review itself
   may need an update, and the project lead needs to see those cases.
5. **Proceed with steps 2–12 of the standard `ingest-source`
   workflow** (determine tier, update registries, create source card,
   update theme/method/dossier pages, commit).
6. **Verification markers:** Claims that you cross-checked against
   the original in step 3 and verified as accurate can start at
   `[✓]` rather than `[🤖]`, because a human authored the literature
   review and you have now verified the original. Claims that the
   literature review did not cover, or that you introduce beyond
   what the review states, still start at `[🤖]`.
7. **Record verification counts honestly** in the source card's
   frontmatter. Do not mark claims `[✓]` unless you actually
   cross-checked them.

## Constraints

- All constraints from `ingest-source` apply.
- If the literature review and the original disagree, trust the
  original and record the discrepancy.
- If the literature review covers the source but you cannot locate
  the original PDF in `sources/papers/`, abort and add the missing
  source to `ops/log.md` for acquisition.

## Expected output

Same as `ingest-source`, with:
- Higher baseline verification coverage on the new source card
  (a meaningful fraction of claims at `[✓]` rather than `[🤖]`).
- Any literature-review discrepancies recorded in `ops/log.md`.
