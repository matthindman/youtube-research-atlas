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

## 2026-04-15 — Ingest mcgrady_2023
**Operation:** ingest-source
**Branch:** ingest/mcgrady_2023
**By:** Codex (GPT-5)

Ingested `mcgrady_2023` via the `ingest-from-review` workflow. Created
`wiki/sources/mcgrady_2023.md` and updated `data/source-registry.yaml`,
`data/claim-registry.yaml`, `wiki/themes/descriptive_deficit.md`, and
`wiki/index.md`.

Literature-review cross-check note:

- The review states that recommendation-based collections are already
  shown to be systematically biased toward more popular videos. In the
  original article, the authors frame that comparison more cautiously:
  they say they believe this is true and will demonstrate it in
  forthcoming work (p. 4), rather than presenting the comparison as a
  completed result in this paper.

Tier and taxonomy decisions:

- Assigned `primary_empirical`.
- Reused existing theme tags `descriptive-deficit` and
  `cross-linguistic-variation`; no taxonomy additions proposed.

Human attention requested:

- The language-distribution discussion is useful for establishing that
  YouTube is more multilingual than many English-speaking users
  experience, but the paper itself cautions against treating the
  classifier outputs as precise language-share estimates (pp. 46-49,
  61).

## 2026-04-15 — Ingest munger_2024
**Operation:** ingest-source
**Branch:** ingest/munger_2024
**By:** Codex (GPT-5)

Ingested `munger_2024` via the `ingest-from-review` workflow. Created
`wiki/sources/munger_2024.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/descriptive_deficit.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced between the review summary and the
  book's argument. The review's emphasis on agenda-setting, reciprocal
  supply-demand feedback, and the priority of quantitative description
  matches the original text.

Tier and taxonomy decisions:

- Assigned `primary_empirical`.
- Reused existing theme tag `descriptive-deficit`; no taxonomy changes
  proposed.
- Registry `type` was set to `book_chapter` because the current schema
  has no dedicated type for a Cambridge Element / short monograph.

Human attention requested:

- The source is unusually hybrid: part agenda-setting essay, part
  original descriptive analysis of political YouTube. The evidence tier
  feels right at `primary_empirical`, but the registry schema likely
  needs a better source-type slot than `book_chapter` for future
  monographs.

## 2026-04-15 — Ingest munger_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/munger_et_al_2025
**By:** Codex (GPT-5)

Ingested `munger_et_al_2025` via the `ingest-from-review` workflow.
Created `wiki/sources/munger_et_al_2025.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/descriptive_deficit.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced. The review accurately captures
  the paper's field-level understudy claim, the priority of
  quantitative description, the extreme inequality in commenter
  activity, and the API-quota constraint.

Tier and taxonomy decisions:

- Assigned `primary_empirical`, consistent with the user's instruction
  to treat this coauthored but peer-reviewed publication as external
  scholarship rather than `project_internal`.
- Reused the existing theme tag `descriptive-deficit`; no taxonomy
  additions proposed.

Human attention requested:

- The strongest representativeness claim in this paper is about visible
  commenting behavior on anglophone US political YouTube, not about all
  viewers or all of YouTube. The theme page keeps that scope explicit.

## 2026-04-15 — Ingest norton_shapiro_2024
**Operation:** ingest-source
**Branch:** ingest/norton_shapiro_2024
**By:** Codex (GPT-5)

Ingested `norton_shapiro_2024` via the `ingest-from-review` workflow.
Created `wiki/sources/norton_shapiro_2024.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/descriptive_deficit.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced. The review accurately reports the
  article's platform, geography, and method biases, as well as the
  data-access and tooling bottlenecks it highlights.

Tier and taxonomy decisions:

- Assigned `news_commentary` rather than `secondary_analytical`
  because the venue is commentary, even though the article includes a
  useful literature audit and interview-based diagnosis.
- Reused existing theme tags `descriptive-deficit` and
  `governance-data-access`; no taxonomy additions proposed.

Human attention requested:

- The article is valuable for framing the research-infrastructure
  problem, but theme usage should stay disciplined: it supports context
  about why YouTube is understudied, not empirical claims about
  YouTube's behavior or effects.

## 2026-04-15 — Ingest mcgrady_2025
**Operation:** ingest-source
**Branch:** ingest/mcgrady_2025
**By:** Codex (GPT-5)

Ingested `mcgrady_2025` via the `ingest-from-review` workflow.
Created `wiki/sources/mcgrady_2025.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/descriptive_deficit.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced. The review accurately reports
  the Anglocentric bias claim, the Hindi/TikTok divergence, the lack
  of published language distributions, and the use of random sampling
  as a partial methodological corrective.

Tier and taxonomy decisions:

- Assigned `primary_empirical`.
- Reused existing theme tags `descriptive-deficit` and
  `cross-linguistic-variation`; no taxonomy additions proposed.
- Per the Batch 1 instruction, only `wiki/themes/descriptive_deficit.md`
  was updated here. The source is also tagged to
  `cross-linguistic-variation`, but that theme was not refreshed in
  this PR.

## 2026-04-15 — Refresh descriptive_deficit
**Operation:** refresh-theme
**Branch:** refresh/descriptive_deficit
**By:** Codex (GPT-5)

Refreshed `wiki/themes/descriptive_deficit.md` after Batch 1 ingest
using the five current source cards (`mcgrady_2023`, `munger_2024`,
`munger_et_al_2025`, `norton_shapiro_2024`, `mcgrady_2025`). Rewrote
the consensus, disagreement, evidence-inventory, methods, project
implications, and open-holes sections so the page reflects the full
current source set rather than the rolling per-paper ingest updates.

Refresh decisions:

- Kept every substantive theme-page claim at `[🤖]` per the
  `refresh-theme` rule; no refresh claim was upgraded to `[✓]`.
- Preserved the absence of a direct empirical contradiction while
  making the source-set differences in diagnosis explicit:
  denominator/sampling, agenda-setting, infrastructure, and
  multilingual heterogeneity.
- No claim-registry text changes were needed for this refresh.
- No debate-page split is proposed at this stage; the refreshed page
  remains well under the 400-line split threshold and the five sources
  still cohere as one theme.

Human attention requested:

- The page now relies on a stronger distinction between direct
  empirical evidence about platform distributions and commentary about
  why the field lacks that evidence. Reviewers should confirm that
  Norton and Shapiro remains confined to framing/infrastructure use.
- The outstanding literature-review discrepancy on `mcgrady_2023`
  still stands: the review overstates recommendation-sample bias as a
  demonstrated finding in that paper rather than a claim deferred to
  future work.

Human attention requested:

- The paper's strongest generalization is comparative, not exhaustive:
  it shows that English, Spanish, Hindi, and Russian YouTube differ
  sharply, but it does not by itself establish what all other language
  communities on the platform look like.

## 2026-04-15 — Batch 1 calibration fixes
**Operation:** fix
**Branch:** refresh/descriptive_deficit
**By:** Claude Code (Opus 4.6)

Applied two calibration fixes to the Batch 1 output before PR review,
matching durable changes made on `main` (commit 7907bb5):

1. **Norton & Shapiro 2024 retiered from `news_commentary` to
   `policy_research`.** The `policy_research` tier was added on main
   specifically for academically-authored pieces in non-peer-reviewed
   venues that present original analysis. Updated:
   - `wiki/sources/norton_shapiro_2024.md` — evidence_tier and the
     limitations section explaining the tier rationale.
   - `data/source-registry.yaml` — evidence_tier, type (`policy_essay`),
     and notes.
   - `wiki/themes/descriptive_deficit.md` — the paragraph that
     previously justified downweighting N&S now explains that the
     `policy_research` tier allows its bibliometric audit to be cited
     as the authors' own descriptive findings about the field, while
     still flagging the non-peer-reviewed venue.

2. **Claim registry verification levels demoted.** All 6 entries were
   marked `verification: human_checked` during Batch 1, but claim-
   registry entries are agent-authored synthesis and not cross-checked
   at a specific passage. The updated `ingest-from-review` skill
   clarifies that the `[✓]` starting marker applies only to inline
   source-card markers, not to claim-registry entries. All 6 entries
   now start at `machine_extracted`; a human will upgrade as part of
   PR review or the calibration pause.

No source card body content or theme-page substantive claims were
changed. This is a tier/metadata correction only.
## 2026-04-15 — Ingest rieder_et_al_2023
**Operation:** ingest-source
**Branch:** ingest/rieder_et_al_2023
**By:** Codex (GPT-5)

Ingested `rieder_et_al_2023` via the `ingest-from-review`
workflow. Created `wiki/sources/rieder_et_al_2023.md` and
## 2026-04-15 — Ingest verwiebe_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/verwiebe_et_al_2025
**By:** Codex (GPT-5)

Ingested `verwiebe_et_al_2025` via the `ingest-from-review`
workflow. Created `wiki/sources/verwiebe_et_al_2025.md` and
## 2026-04-15 — Ingest ormen_gregersen_2023_polymorphism
**Operation:** ingest-source
**Branch:** ingest/ormen_gregersen_2023_polymorphism
**By:** Codex (GPT-5)

Ingested `ormen_gregersen_2023_polymorphism` via the
`ingest-from-review` workflow. Created
`wiki/sources/ormen_gregersen_2023_polymorphism.md` and
updated `data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/creator_economy.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material discrepancy found. The literature review's emphasis
  on extreme inequality, creator precarity, and the growth of
  external linking matches the paper's framing and findings (pp.
  1-4, 15-16).
  on extreme earnings inequality, the under-studied role of
  sociostructural variables, and the winner-take-all framing
  matches the article's results and discussion (pp. 2-3, 12-20).
- No material discrepancy found. The literature review's framing
  of diversification over convergence, the sampling challenge, and
  the weakness of YouTube's native categories matches the
  article's methods and conclusions (pp. 432-437, 444-448).

Tier and taxonomy decisions:

- Assigned `primary_empirical` and `journal_article`.
- Reused existing theme tag `creator-economy`; no taxonomy
  addition proposed on this branch.

Claims not fully verifiable from this source alone:

- The paper clearly shows visible URL-based diversification among
  elite channels, but it cannot observe sponsorships, direct brand
  deals, or other non-linked income streams. Treat any stronger
  claim about total creator income diversification as provisional.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/rieder_et_al_2023?quick_pull=1&title=%5Bingest-from-review%5D%20Rieder%20et%20al.%202023%20%28Making%20a%20Living%20in%20the%20Creator%20Economy%29&body=%23%23%20Summary%0A-%20Ingested%20%60rieder_et_al_2023%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20creator-economy%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/rieder_et_al_2023.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/creator_economy.md%0A-%20wiki/index.md%0A-%20ops/log.md
- The paper estimates YPP earnings rather than observing payout
  ledgers directly, so exact income magnitudes should be treated
  as modeled estimates rather than audited creator accounts.
- Because the sample is limited to monetized German-speaking
  channels, any broader claim about the global creator economy
  remains provisional.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/verwiebe_et_al_2025?quick_pull=1&title=%5Bingest-from-review%5D%20Verwiebe%20et%20al.%202025%20%28Unequal%20Earnings%20on%20YouTube%29&body=%23%23%20Summary%0A-%20Ingested%20%60verwiebe_et_al_2025%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20creator-economy%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/verwiebe_et_al_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/creator_economy.md%0A-%20wiki/index.md%0A-%20ops/log.md
  addition proposed on this branch, but the paper reinforces the
  need for careful institutional-form coding in later project
  taxonomy work.

Claims not fully verifiable from this source alone:

- The paper is strong on strategic heterogeneity but does not
  provide platform-wide prevalence estimates for the four
  strategic types.
- Monetization comparisons rely on visible and threshold-based
  signals rather than internal watch-time or payout records.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/ormen_gregersen_2023_polymorphism?quick_pull=1&title=%5Bingest-from-review%5D%20%C3%98rmen%20and%20Gregersen%202023%20%28Institutional%20Polymorphism%29&body=%23%23%20Summary%0A-%20Ingested%20%60ormen_gregersen_2023_polymorphism%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20creator-economy%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/ormen_gregersen_2023_polymorphism.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/creator_economy.md%0A-%20wiki/index.md%0A-%20ops/log.md
