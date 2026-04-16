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
- The paper is a document analysis of platform communication,
  not a behavioral or payout study, so claims about direct creator
  outcomes remain inferential rather than measured here.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/ormen_gregersen_2023_engagement?quick_pull=1&title=%5Bingest-from-review%5D%20%C3%98rmen%20and%20Gregersen%202023%20%28Towards%20the%20Engagement%20Economy%29&body=%23%23%20Summary%0A-%20Ingested%20%60ormen_gregersen_2023_engagement%60%20via%20%60ingest-from-review%60%20with%20all%20source-card%20claims%20left%20at%20%60%5B%F0%9F%A4%96%5D%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20creator-economy%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/ormen_gregersen_2023_engagement.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/creator_economy.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-15 — Ingest newman_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/newman_et_al_2025
**By:** Codex (GPT-5)

Ingested `newman_et_al_2025` via the `ingest-from-review`
workflow. Created `wiki/sources/newman_et_al_2025.md` and
## 2026-04-15 — Ingest reuters_dnr_2025
**Operation:** ingest-source
**Branch:** ingest/reuters_dnr_2025
**By:** Codex (GPT-5)

Ingested `reuters_dnr_2025` via the `ingest-from-review`
workflow. Created `wiki/sources/reuters_dnr_2025.md` and
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
- No material discrepancy found. The literature review's account
  of YouTube's 30% weekly news use, especially heavy use in India,
  Thailand, and Kenya, creator-led pressure on institutional
  journalism, and YouTube's role in video-podcast distribution is
  consistent with the report itself (pp. 10, 16-21).

Tier and taxonomy decisions:

- Assigned `industry_report`, not `policy_research`. The Digital
  News Report is a Reuters Institute annual survey report and is
  the canonical `industry_report` case for this atlas.
- Scoped the source card to the report's YouTube, video-news,
  creator-attention, podcast, and verification sections rather
  than attempting to summarize the entire annual report.

Claims not fully verifiable from this source alone:

- The report does not show what users actually watched on YouTube
  or whether recommendation systems causally amplified creator-led
  news attention.
- It also cannot determine the epistemic quality of the creator-
  led news ecosystem it describes.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/reuters_dnr_2025?quick_pull=1&title=%5Bingest-from-review%5D%20Reuters%20Institute%202025%20%28Digital%20News%20Report%202025%29&body=%23%23%20Summary%0A-%20Ingested%20%60reuters_dnr_2025%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20news-ecosystem%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/reuters_dnr_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/news_ecosystem.md%0A-%20wiki/index.md%0A-%20ops/log.md
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
## 2026-04-15 — Refresh news_ecosystem
**Operation:** refresh-theme
**Branch:** refresh/news_ecosystem
**By:** Codex (GPT-5)

Refreshed `wiki/themes/news_ecosystem.md` after the Batch 2
ingests. This synthesis was built from pushed source cards on
`ingest/newman_et_al_2025` and `ingest/reuters_dnr_2025`.

Key synthesis decisions:

- Kept the page explicitly marked as supported only by non-peer-
  reviewed sources, because the current evidence base here is two
  Reuters Institute reports rather than peer-reviewed research.
- Preserved the core tension between creator-led attention gains
  and the continuing role of traditional news brands in some
  markets and in verification behavior.
- Kept all claims at `[🤖]` and limited this branch to the theme
  page plus log entry, per the Batch 2 refresh instruction.

Split evaluation:

- No split proposed yet. The page remains comfortably below the
  400-line threshold and the disagreements still cohere within a
  single creator-economy synthesis.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/creator_economy?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20creator_economy&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/creator_economy.md%60%20from%20the%20Batch%202%20source%20cards.%0A-%20Preserved%20disagreement%20between%20diversification%20and%20engagement-market%20standardization.%0A-%20Kept%20this%20branch%20limited%20to%20the%20theme%20page%20and%20ops%20log.%0A%0A%23%23%20Sources%0A-%20rieder_et_al_2023%0A-%20verwiebe_et_al_2025%0A-%20ormen_gregersen_2023_polymorphism%0A-%20ormen_gregersen_2023_engagement%0A-%20newman_et_al_2025%0A%0A%23%23%20Pages%0A-%20wiki/themes/creator_economy.md%0A-%20ops/log.md
- No split proposed yet. The page remains compact and the current
  disagreements still fit inside a single news-ecosystem theme.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/news_ecosystem?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20news_ecosystem&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/news_ecosystem.md%60%20from%20the%20Batch%202%20source%20cards.%0A-%20Preserved%20tension%20between%20creator-led%20attention%20gains%20and%20the%20continued%20role%20of%20traditional%20news%20brands.%0A-%20Kept%20this%20branch%20limited%20to%20the%20theme%20page%20and%20ops%20log.%0A%0A%23%23%20Sources%0A-%20newman_et_al_2025%0A-%20reuters_dnr_2025%0A%0A%23%23%20Pages%0A-%20wiki/themes/news_ecosystem.md%0A-%20ops/log.md

## 2026-04-15 — Ingest lai_et_al_2024
**Operation:** ingest-source
**Branch:** ingest/lai_et_al_2024
**By:** Codex (GPT-5)

Ingested `lai_et_al_2024` via the `ingest-from-review` workflow.
Created `wiki/sources/lai_et_al_2024.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/recommendation_radicalization.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced between the review summary and
  the article. The review's emphasis on video-level scaling,
  validation against human labels, ideological congruence in watch
  histories, and higher engagement around ideological extremes
  matches the original article (pp. 346-359).
- Minor metadata discrepancy: the literature review section header
  labels this source "(2022)," but the full citation and published
  article are 2024.
## 2026-04-15 — Ingest haroon_et_al_2023
**Operation:** ingest-source
**Branch:** ingest/haroon_et_al_2023
**By:** Codex (GPT-5)

Ingested `haroon_et_al_2023` via the `ingest-from-review`
workflow. Created `wiki/sources/haroon_et_al_2023.md` and
updated `data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/recommendation_radicalization.md`, and
`wiki/index.md`.
## 2026-04-15 — Ingest munger_phillips_2022
**Operation:** ingest-source
**Branch:** ingest/munger_phillips_2022
**By:** Codex (GPT-5)

Ingested `munger_phillips_2022` via the `ingest-from-review`
workflow. Created `wiki/sources/munger_phillips_2022.md` and
updated `data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/recommendation_radicalization.md`,
`wiki/themes/creator_economy.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced. The review's emphasis on
  100,000 trained sock puppets, congenial recommendations, limited
  extremization, and low-rate/high-reach problematic exposure
  matches the article (pp. 1-8).
  YouTube's political-science blind spot, the supply-and-demand
  framework, creator-centered community formation, and the 2017
  far-right peak matches the article (pp. 3-6, 28-34).

Tier and taxonomy decisions:

- Assigned `primary_empirical` and `journal_article`.
- Reused existing theme tag `recommendation-radicalization`; no
  taxonomy addition proposed.
- Registry notes explicitly record Josh Tucker's coauthorship as
  collaborator-linked but external scholarship, matching the
  existing `munger_et_al_2025` pattern.

Claims not fully verifiable from this source alone:

- The watch-history application is descriptive and does not isolate
  recommendations from search, subscriptions, or prior preference.
- The ideology estimator is validated most clearly for U.S.
  political videos with strong Reddit-link and text-metadata
  footprints, so cross-national transport should remain provisional.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/lai_et_al_2024?quick_pull=1&title=%5Bingest-from-review%5D%20Lai%20et%20al.%202024%20%28Estimating%20the%20Ideology%20of%20Political%20YouTube%20Videos%29&body=%23%23%20Summary%0A-%20Ingested%20%60lai_et_al_2024%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20recommendation-radicalization%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/lai_et_al_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md

Claims not fully verifiable from this source alone:

- The audit does not observe what real users click, search for, or
  ignore after seeing recommendations.
- The main text is clear that the evidence is post-2019, but it does
  not foreground an exact collection window with the same clarity.
- The problematic-channel share depends on prior labeled lists and
  likely understates exposure deeper in the trail where more channels
  are uncategorized.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/haroon_et_al_2023?quick_pull=1&title=%5Bingest-from-review%5D%20Haroon%20et%20al.%202023%20%28Auditing%20YouTube%27s%20Recommendation%20System%29&body=%23%23%20Summary%0A-%20Ingested%20%60haroon_et_al_2023%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20recommendation-radicalization%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/haroon_et_al_2023.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
- Reused existing theme tags `recommendation-radicalization`,
  `creator-economy`, and `news-ecosystem`; no taxonomy addition
  proposed.
- Updated the existing `claim_descriptive_deficit_understudied_platform`
  registry entry to add this paper as supporting evidence.

Theme-scope decisions:

- Added a single evidence-inventory row to
  `wiki/themes/creator_economy.md` because the paper contributes a
  useful creator-community mechanism without requiring a rewrite.
- I did **not** make a parallel incremental edit to
  `wiki/themes/news_ecosystem.md`. That page currently frames its
  evidence base as non-peer-reviewed Reuters-only material; changing
  that framing responsibly would require a deliberate future refresh,
  not a one-row Batch 3 drive-by.

Claims not fully verifiable from this source alone:

- The paper is descriptive and theoretical, not a direct
  recommendation audit, so it cannot isolate the algorithm's causal
  role.
- The evidence is about a right-wing political subsystem rather than
  platform-wide political YouTube.
- The May 2020 update cannot fully reconstruct when later views were
  accrued and is affected by nonrandom missingness in removed videos.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/munger_phillips_2022?quick_pull=1&title=%5Bingest-from-review%5D%20Munger%20and%20Phillips%202022%20%28Right-Wing%20YouTube%29&body=%23%23%20Summary%0A-%20Ingested%20%60munger_phillips_2022%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20recommendation-radicalization%20theme%2C%20registries%2C%20creator-economy%20theme%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/munger_phillips_2022.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/themes/creator_economy.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-15 — Refresh recommendation_radicalization
**Operation:** refresh-theme
**Branch:** refresh/recommendation_radicalization
**By:** Codex (GPT-5)

Refreshed `wiki/themes/recommendation_radicalization.md` after the
Batch 3 ingests. This synthesis was built from the pushed source
cards on `ingest/lai_et_al_2024`, `ingest/haroon_et_al_2023`, and
`ingest/munger_phillips_2022`, plus the already-merged
`munger_2024` source card as canon for the field's agenda-setting
critique.

Key synthesis decisions:

- Explicitly separated the page into pre-2019, post-2019, and
  post-2022 evidence buckets. The post-2022 bucket remains thin and
  is called out as such.
- Preserved the tension between limited post-2019 extremization in
  audit work and continuing concerns about problematic-channel reach.
- Treated Lai et al. primarily as measurement infrastructure for the
  debate rather than as a direct recommendation test.

Split evaluation:

- Proposed `rabbit_hole_debate`, `filter_bubble_evidence`, and
  `pre_2019_vs_post_2019_algorithm` as split candidates in the page
  frontmatter.
- Did not create the debate pages in this branch.

Human attention requested:

- This branch correctly starts from `origin/main`, so the refreshed
  theme references Batch 3 source cards that live on separate ingest
  PRs. Merge order or conflict resolution will matter in review.
- If reviewers want a stronger post-2022 section, the atlas needs
  additional sources; the current evidence base should not be
  stretched forward.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/recommendation_radicalization?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20recommendation_radicalization&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/recommendation_radicalization.md%60%20from%20the%20Batch%203%20source%20cards.%0A-%20Explicitly%20separated%20pre-2019%2C%20post-2019%2C%20and%20post-2022%20evidence%20regimes.%0A-%20Proposed%20split%20candidates%20without%20creating%20debate%20pages%20in%20this%20PR.%0A%0A%23%23%20Sources%0A-%20munger_phillips_2022%0A-%20haroon_et_al_2023%0A-%20lai_et_al_2024%0A-%20munger_2024%0A%0A%23%23%20Pages%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20ops/log.md
## 2026-04-15 — Create ideology_estimation method page
**Operation:** scaffold
**Branch:** method/ideology_estimation
**By:** Codex (GPT-5)

Created `wiki/methods/ideology_estimation.md` as the first
atlas method page for ideology-scaling designs. The page treats
`lai_et_al_2024` as the canonical exemplar and places
`munger_2024` plus `munger_et_al_2025` in the "Where It Has Been
Used" table to clarify how they rely on channel-level rather than
video-level ideology choices.
## 2026-04-15 — Create recommendation_audit method page
**Operation:** scaffold
**Branch:** method/recommendation_audit
**By:** Codex (GPT-5)

Created `wiki/methods/recommendation_audit.md` as the first atlas
method page for trained-sock-puppet and related recommender-audit
designs. The page uses `haroon_et_al_2023` as the canonical exemplar
and includes `lai_et_al_2024` only as a measurement building block,
not as an audit paper in its own right.

Structural choices:

- Updated `wiki/index.md` on this branch so the new page is visible
  from the atlas catalog, even though the parallel
  `method/recommendation_audit` branch will make an overlapping
  `method/ideology_estimation` branch will make an overlapping
  change.
- Referenced Batch 3 source IDs that are not present on
  `origin/main` yet because this branch correctly starts from
  `origin/main` rather than stacking on the ingest branches.

Human attention requested:

- The method-page template does not specify whether pages should
  restrict themselves to already-merged source cards. I chose to
  reference the pushed Batch 3 source IDs directly and flag the merge-
  order dependency here.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...method/ideology_estimation?quick_pull=1&title=%5Bscaffold%5D%20Create%20ideology_estimation%20method%20page&body=%23%23%20Summary%0A-%20Created%20%60wiki/methods/ideology_estimation.md%60.%0A-%20Added%20the%20new%20method%20page%20to%20%60wiki/index.md%60%20and%20documented%20the%20structural%20choices%20in%20%60ops/log.md%60.%0A%0A%23%23%20Pages%0A-%20wiki/methods/ideology_estimation.md%0A-%20wiki/index.md%0A-%20ops/log.md
- The method-page template does not say whether "Where It Has Been
  Used" can include a paper that supplies a building block rather
  than the audit itself. I included `lai_et_al_2024` with that scope
  made explicit.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...method/recommendation_audit?quick_pull=1&title=%5Bscaffold%5D%20Create%20recommendation_audit%20method%20page&body=%23%23%20Summary%0A-%20Created%20%60wiki/methods/recommendation_audit.md%60.%0A-%20Added%20the%20new%20method%20page%20to%20%60wiki/index.md%60%20and%20documented%20the%20structural%20choices%20in%20%60ops/log.md%60.%0A%0A%23%23%20Pages%0A-%20wiki/methods/recommendation_audit.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-15 — Ingest hosseinmardi_et_al_2024
**Operation:** ingest-source
**Branch:** ingest/hosseinmardi_et_al_2024
**By:** Codex (GPT-5)

Ingested `hosseinmardi_et_al_2024` via the `ingest-from-review`
workflow. Created `wiki/sources/hosseinmardi_et_al_2024.md` and
updated `data/source-registry.yaml`, `data/claim-registry.yaml`,
## 2026-04-15 — Ingest brown_et_al_2022
**Operation:** ingest-source
**Branch:** ingest/brown_et_al_2022
**By:** Codex (GPT-5)

Ingested `brown_et_al_2022` via the `ingest-from-review`
workflow. Created `wiki/sources/brown_et_al_2022.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/recommendation_radicalization.md`,
`wiki/methods/recommendation_audit.md`, and `wiki/index.md`.
## 2026-04-15 — Ingest liu_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/liu_et_al_2025
**By:** Codex (GPT-5)

Ingested `liu_et_al_2025` via the `ingest-from-review` workflow.
Created `wiki/sources/liu_et_al_2025.md` and updated
## 2026-04-15 — Ingest chen_et_al_2023
**Operation:** ingest-source
**Branch:** ingest/chen_et_al_2023
**By:** Codex (GPT-5)

Ingested `chen_et_al_2023` via the `ingest-from-review` workflow.
Created `wiki/sources/chen_et_al_2023.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/recommendation_radicalization.md`, and
`wiki/index.md`.
## 2026-04-15 — Ingest yu_et_al_2024
**Operation:** ingest-source
**Branch:** ingest/yu_et_al_2024
**By:** Codex (GPT-5)

Ingested `yu_et_al_2024` via the `ingest-from-review` workflow.
Created `wiki/sources/yu_et_al_2024.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/recommendation_radicalization.md`,
`wiki/methods/recommendation_audit.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced between the literature review
  and the article. The review's emphasis on missing causal
  counterfactuals, the post-2019 moderating effect of
  recommendations relative to user preferences, and the faster
  forgetting dynamics for sidebar than homepage recommendations
  matches the article (pp. 1-6).
- Added one source-card finding not foregrounded in the literature
  review: bursts of partisan viewing predict later partisan
  consumption because of user-preference shifts rather than
  recommender overreaction (p. 5).
  and the article. The review accurately characterizes the paper as
  a strong causal challenge to broad rabbit-hole and filter-bubble
  claims, with the main unresolved issues being long-run exposure,
  vulnerable subpopulations, and algorithm change over time (pp.
  1-2, 10).
- The article is more temporally specific than the review summary: it
  spans studies launched in June 2021, April 2022, and May 2024, so
  it should be treated as mixed post-2019 evidence rather than as a
  cleanly post-2022 study (p. 5).
  and the article. The review's emphasis on concentrated exposure
  among resentful users, subscriptions and external links as the
  main pathways, and the rarity of unsolicited recommendation-led
  rabbit holes matches the article (pp. 1-2, 6-9).
- The original paper is sharper than the review about the "lower
  bound" status of its rabbit-hole estimates and about the role of
  subscription status in structuring what recommendations are shown
  and followed (pp. 2, 6-9, 11).
  and the article. The review's emphasis on algorithmic interest
  bias, the stronger effect of nudging the algorithm than nudging
  users, and the null downstream attitude effects matches the
  original paper (pp. 1-9).
- The original article is more explicit that this is a post-2022
  study and that the key user experiment runs from November 2022
  to January 2023, which matters for the atlas's temporal buckets
  (pp. 4-9).

Tier and taxonomy decisions:

- Assigned `primary_empirical` and `journal_article`.
- Reused the existing `recommendation-radicalization` theme tag; no
  taxonomy addition was needed.
- Updated `wiki/methods/recommendation_audit.md` because the paper is
  best treated as an audit-panel hybrid built from logged-in
  counterfactual bots, not as a pure observational panel study.

Claims not fully verifiable from this source alone:

- The evidence is limited to desktop browsing and may not generalize
  to mobile recommendation surfaces.
- Partisanship is scored at the channel rather than video level, and
  the main analysis drops videos without available scores.
- The paper is explicit that its findings are post-2019 only and do
  not adjudicate pre-2019 recommendation behavior.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/hosseinmardi_et_al_2024?quick_pull=1&title=%5Bingest-from-review%5D%20Hosseinmardi%20et%20al.%202024%20%28Counterfactual%20Bots%29&body=%23%23%20Summary%0A-%20Ingested%20%60hosseinmardi_et_al_2024%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20recommendation-radicalization%20theme%2C%20recommendation_audit%20method%20page%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/hosseinmardi_et_al_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/methods/recommendation_audit.md%0A-%20wiki/index.md%0A-%20ops/log.md
  and the working paper. The review's emphasis on mild echo
  chambers, little evidence of rabbit holes for average users, and a
  modest system-wide conservative bias matches the original paper
  (pp. 1, 19-29).
- The original paper is more explicit than the review that the
  conservative nudge is small in magnitude, moving users roughly from
  a C-SPAN benchmark toward a RonPaulLibertyReport benchmark, and
  that the evidence is based on only 20 traversal steps in fall 2020
  (pp. 25, 28-29).

Tier and taxonomy decisions:

- Assigned `primary_empirical` and `working_paper` because the paper
  presents original experimental data even though the local file is
  an SSRN manuscript rather than a journal PDF.
- Reused the existing `recommendation-radicalization` theme tag; no
  taxonomy addition was needed.
- Recorded Josh Tucker's coauthorship in the source-registry notes
  field while treating the paper as external scholarship, not
  project-internal material.

Claims not fully verifiable from this source alone:

- The convenience sample recruited through Facebook ads may not
  generalize to the broader YouTube population.
- The study tracks only 20 traversal steps in one session, so it does
  not resolve long-run exposure dynamics.
- The authors isolate recommendation effects from unconstrained user
  choice, but they still cannot identify whether the conservative
  nudge reflects platform design, user demand, or the supply
  distribution of available videos.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/brown_et_al_2022?quick_pull=1&title=%5Bingest-from-review%5D%20Brown%20et%20al.%202022%20%28Echo%20Chambers%2C%20Rabbit%20Holes%2C%20and%20Algorithmic%20Bias%29&body=%23%23%20Summary%0A-%20Ingested%20%60brown_et_al_2022%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20recommendation-radicalization%20theme%2C%20recommendation_audit%20method%20page%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/brown_et_al_2022.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/methods/recommendation_audit.md%0A-%20wiki/index.md%0A-%20ops/log.md
- Did not update `wiki/methods/recommendation_audit.md` on this
  branch. The design is clearly adjacent to recommender-audit work,
  but this paper is best classified here as a naturalistic
  experiment about causal downstream effects rather than as a pure
  audit exemplar.

Claims not fully verifiable from this source alone:

- The paper does not rule out longer-run effects from repeated
  exposure over months or years.
- It cannot rule out effects concentrated in small susceptible
  subpopulations.
- The issue scope is limited to gun control and minimum wage, and
  the design holds video supply largely fixed around existing
  YouTube recommendation networks.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/liu_et_al_2025?quick_pull=1&title=%5Bingest-from-review%5D%20Liu%20et%20al.%202025%20%28Short-term%20Exposure%20to%20Filter-Bubble%20Recommendation%20Systems%20Has%20Limited%20Polarization%20Effects%29&body=%23%23%20Summary%0A-%20Ingested%20%60liu_et_al_2025%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20recommendation-radicalization%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/liu_et_al_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
- Updated the existing supply-demand claim rather than creating a
  duplicate because Chen directly strengthens the argument that
  demand-side pathways matter more than a simple recommendation
  rabbit-hole story.

Claims not fully verifiable from this source alone:

- The sample is weighted but not fully representative and excludes
  mobile consumption plus browsers outside Chrome and Firefox.
- The authors explicitly treat the rabbit-hole estimates as lower
  bounds, not complete measures of all harmful exposure.
- The evidence is U.S.-only and depends on channel-level
  classifications plus inferred subscriptions.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/chen_et_al_2023?quick_pull=1&title=%5Bingest-from-review%5D%20Chen%20et%20al.%202023%20%28Subscriptions%20and%20External%20Links%29&body=%23%23%20Summary%0A-%20Ingested%20%60chen_et_al_2023%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20recommendation-radicalization%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/chen_et_al_2023.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
- Updated `wiki/methods/recommendation_audit.md` because the paper
  extends audit logic into an interventional, extension-based
  recommender study rather than a pure observation design.

Claims not fully verifiable from this source alone:

- The final sample is restricted to frequent U.S. YouTube users who
  would install a browser extension.
- The treatment window is short, so null survey effects should not
  be overread as proof of no longer-run attitudinal consequences.
- The intervention depends on a curated list of balanced news
  outlets and therefore embeds a normative choice about which
  content should be promoted.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/yu_et_al_2024?quick_pull=1&title=%5Bingest-from-review%5D%20Yu%20et%20al.%202024%20%28Nudging%20Recommendation%20Algorithms%29&body=%23%23%20Summary%0A-%20Ingested%20%60yu_et_al_2024%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20recommendation-radicalization%20theme%2C%20recommendation_audit%20method%20page%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A%0A%23%23%20Pages%0A-%20wiki/sources/yu_et_al_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/methods/recommendation_audit.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-15 — Ingest yesilada_lewandowsky_2022
**Operation:** ingest-source
**Branch:** ingest/yesilada_lewandowsky_2022
**By:** Codex (GPT-5)

Ingested `yesilada_lewandowsky_2022` via the `ingest-from-review`
workflow. Created `wiki/sources/yesilada_lewandowsky_2022.md` and
updated `data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/recommendation_radicalization.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced between the internal literature
  review and the article. The review summary correctly captures the
  headline 14/7/2 split and the paper's main caution that restricted
  access and incomplete knowledge of the recommender limit what can
  be inferred about actual mechanisms (pp. 1, 9, 17-18).
- The article is clearer than the internal review about the exact
  coverage window: database searches were run in November-December
  2020 and the included studies range from 2013-2021, so this source
  should be treated as a synthesis of pre-2022 literature rather than
  as evidence about the current recommender state (pp. 7-9, 17-18).

Tier and taxonomy decisions:

- Assigned `secondary_analytical` and `systematic_review`.
- Reused the existing `recommendation-radicalization` theme tag; no
  taxonomy addition was needed.
- Used the review only for synthesis and methods-diagnosis claims.
  I did not use it as a substitute for missing primary evidence about
  specific rabbit-hole or filter-bubble mechanisms.

Underlying primary sources cited by the review that are not yet in
`data/source-registry.yaml` and look like future-ingest candidates:

- `ledwich_zaitsev_2019`
- `ribeiro_et_al_2020`
- `faddoul_chaslot_farid_2020`
- `ocallaghan_et_al_2015`
- `alfano_et_al_2021`
- `papadamou_et_al_2020`
- `hosseinmardi_et_al_2020`
- `chen_et_al_2021_adl_report`

Claims not fully verifiable from this source alone:

- The review's substantive 14/7/2 summary depends on a set of
  underlying primaries that are mostly not yet ingested in the atlas.
- The included studies use inconsistent definitions of problematic
  content and often weak personalization controls.
- Because the coverage window ends with studies available through
  2021, the review cannot adjudicate post-2022 platform changes.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/yesilada_lewandowsky_2022?quick_pull=1&title=%5Bingest-from-review%5D%20Yesilada%20and%20Lewandowsky%202022%20%28Systematic%20Review%3A%20YouTube%20Recommendations%20and%20Problematic%20Content%29&body=%23%23%20Summary%0A-%20Ingested%20%60yesilada_lewandowsky_2022%60%20via%20%60ingest-from-review%60.%0A-%20Created%20the%20source%20card%20and%20updated%20the%20recommendation-radicalization%20theme%2C%20registries%2C%20index%2C%20and%20ops%20log.%0A-%20Registered%20it%20as%20a%20%60secondary_analytical%60%20source%20and%20used%20it%20only%20for%20synthesis/methods%20claims%2C%20not%20as%20a%20substitute%20for%20missing%20primary%20evidence.%0A%0A%23%23%20Pages%0A-%20wiki/sources/yesilada_lewandowsky_2022.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-15 — Refresh recommendation_radicalization as hub page
**Operation:** refresh-theme
**Branch:** refresh/recommendation_radicalization
**By:** Codex (GPT-5)

Refreshed `wiki/themes/recommendation_radicalization.md` as a hub
page after completing the Batch 4 corpus. The page now routes readers
to three debate pages rather than carrying the detailed point-by-point
evidence inventory itself.

Key synthesis decisions:

- Reset the page around the full 10-source corpus: four pre-Batch-4
  sources on `main` plus six newly pushed Batch 4 source cards.
- Recast the evidence inventory at the debate level rather than the
  source-row level, with one row each for rabbit holes, filter
  bubbles, and regime change.
- Cleared `split_candidates` because the split is no longer
  hypothetical on this branch; the debate pages are being created as
  separate PRs.

Structural notes:

- The hub now stays at 107 lines, which is materially leaner than the
  pre-Batch-4 monolithic page and within the intended shorter-hub
  shape.
- This branch correctly starts from `origin/main`, so it references
  pushed Batch 4 source IDs that are not yet merged on `main`.
  Reviewers will need to account for merge order or resolve those
  references manually if PRs land out of order.

Human attention requested:

- The theme template did not specify how a hub page should inventory
  debate-level evidence after a split. I chose a compact table keyed
  to debate pages rather than another source-by-source table.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/recommendation_radicalization?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20recommendation_radicalization%20as%20hub%20page&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/recommendation_radicalization.md%60%20as%20a%20hub%20page%20for%20the%20completed%2010-source%20corpus.%0A-%20Moved%20detailed%20synthesis%20pressure%20into%20three%20planned%20debate%20pages%3A%20%60rabbit_hole_debate%60%2C%20%60filter_bubble_evidence%60%2C%20and%20%60pre_2019_vs_post_2019_algorithm%60.%0A-%20Updated%20frontmatter%20to%20the%20full%2010-source%20corpus%20and%20cleared%20%60split_candidates%60%20because%20the%20split%20is%20now%20being%20executed%20in%20separate%20PRs.%0A%0A%23%23%20Pages%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20ops/log.md
## 2026-04-15 — Create rabbit_hole_debate
**Operation:** debate-page
**Branch:** debate/rabbit_hole_debate
**By:** Codex (GPT-5)

Created `wiki/debates/rabbit_hole_debate.md` and updated
## 2026-04-15 — Create filter_bubble_evidence
**Operation:** debate-page
**Branch:** debate/filter_bubble_evidence
**By:** Codex (GPT-5)

Created `wiki/debates/filter_bubble_evidence.md` and updated
`wiki/index.md` so the new debate page is visible from the atlas
catalog.

Key synthesis decisions:

- Positioned Haroon and Brown as the strongest remaining evidence
  that recommendation systems can still create algorithmic risk, but
  kept the page's center of gravity on the stronger post-2019
  counter-position from Hosseinmardi, Chen, and Munger and Phillips.
- Used Yesilada and Lewandowsky only for synthesis and methods
  diagnosis on Position B, not as a substitute for missing primary
  evidence about specific pathways.
- Treated temporal scoping as load-bearing: the page distinguishes
  pre-2019 ecosystem evidence from post-2019 audit and real-user
  evidence at the outset rather than burying that difference in
  caveats.

Human attention requested:

- The debate template did not specify whether a secondary review
  source could appear in a position table. I included
  `yesilada_lewandowsky_2022` only for the review-level claim about
  field heterogeneity and mixed older findings, not for a fresh
  empirical pathway claim.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...debate/rabbit_hole_debate?quick_pull=1&title=%5Bdebate-page%5D%20Create%20rabbit_hole_debate&body=%23%23%20Summary%0A-%20Created%20%60wiki/debates/rabbit_hole_debate.md%60.%0A-%20Split%20the%20rabbit-hole%20question%20away%20from%20the%20theme%20page%20and%20organized%20the%20evidence%20into%20algorithmic-risk%20versus%20alternative-pathway%20positions.%0A-%20Added%20the%20new%20debate%20page%20to%20%60wiki/index.md%60%20and%20documented%20the%20structural%20choices%20in%20%60ops/log.md%60.%0A%0A%23%23%20Pages%0A-%20wiki/debates/rabbit_hole_debate.md%0A-%20wiki/index.md%0A-%20ops/log.md
- Split the question into two layers that are often blurred together:
  whether recommendations sort exposure ideologically at all, and
  whether that sorting produces measurable downstream political
  effects.
- Positioned Haroon, Lai, and the older review literature on the
  exposure-sorting side, while placing Liu and Yu on the
  limited-effects side because they provide the strongest causal
  evidence in the current corpus.
- Kept post-2022 scoping explicit rather than implicit: Yu is clearly
  post-2022, Liu only partly is, and the rest of the page should not
  be read as contemporary platform evidence by default.

Human attention requested:

- The template did not say whether a single source should appear on
  both sides when it supports exposure sorting but not strong
  polarization effects. I avoided duplicating rows and instead used
  the position labels to separate exposure claims from outcome claims.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...debate/filter_bubble_evidence?quick_pull=1&title=%5Bdebate-page%5D%20Create%20filter_bubble_evidence&body=%23%23%20Summary%0A-%20Created%20%60wiki/debates/filter_bubble_evidence.md%60.%0A-%20Split%20ideological%20sorting%20from%20attitude%20effects%20and%20organized%20the%20page%20around%20exposure-sorting%20versus%20limited-effects%20positions.%0A-%20Added%20the%20new%20debate%20page%20to%20%60wiki/index.md%60%20and%20documented%20the%20structural%20choices%20in%20%60ops/log.md%60.%0A%0A%23%23%20Pages%0A-%20wiki/debates/filter_bubble_evidence.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-15 — Create pre_2019_vs_post_2019_algorithm
**Operation:** debate-page
**Branch:** debate/pre_2019_vs_post_2019_algorithm
**By:** Codex (GPT-5)

Created `wiki/debates/pre_2019_vs_post_2019_algorithm.md` and
updated `wiki/index.md` so the new debate page is visible from the
atlas catalog.

Key synthesis decisions:

- Treated this as the most temporally scoped page in the split. The
  page is organized around continuity versus regime-break positions
  rather than around rabbit-hole versus non-rabbit-hole mechanisms.
- Let the page lean toward `largely_resolved` without overstating it:
  pre-2019 evidence remains historically informative, but the newer
  corpus makes it hard to defend direct transfer of older effect
  claims into the post-2019 or post-2022 system.
- Used Munger and Phillips for the historical baseline, then anchored
  the regime-break side in Hosseinmardi and Liu because they are the
  clearest newer sources on temporal specificity and limited recent
  effects.

Human attention requested:

- The template does not spell out how strong a page marked
  `largely_resolved` should sound. I kept Position A substantive
  enough to show why the older literature still matters, but the
  Current Assessment clearly lands on regime change as the more
  defensible reading.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...debate/pre_2019_vs_post_2019_algorithm?quick_pull=1&title=%5Bdebate-page%5D%20Create%20pre_2019_vs_post_2019_algorithm&body=%23%23%20Summary%0A-%20Created%20%60wiki/debates/pre_2019_vs_post_2019_algorithm.md%60.%0A-%20Split%20the%20regime-change%20question%20away%20from%20the%20theme%20page%20and%20organized%20the%20evidence%20into%20continuity%20versus%20regime-break%20positions.%0A-%20Added%20the%20new%20debate%20page%20to%20%60wiki/index.md%60%20and%20documented%20the%20structural%20choices%20in%20%60ops/log.md%60.%0A%0A%23%23%20Pages%0A-%20wiki/debates/pre_2019_vs_post_2019_algorithm.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest hallinan_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/hallinan_et_al_2025
**By:** Codex (GPT-5)

Ingested `hallinan_et_al_2025` via the `ingest-from-review`
workflow. Created `wiki/sources/hallinan_et_al_2025.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/governance_data_access.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced. The review accurately captures
  the paper's claims about moderation opacity, the inconclusive state
  of platform-bias evidence under restricted access, and the internal
  contradictions within creator accusations of bias.

Tier and taxonomy decisions:

- Assigned `primary_empirical`.
- Reused the existing theme tag `governance-data-access`; no taxonomy
  additions proposed.
- Updated the existing infrastructure-constraints claim rather than
  creating a duplicate access-opacity claim, then added one new claim
  for informal creator accountability.

Human attention requested:

- The paper is strongest as evidence about creator-side governance
  experience under opaque moderation, not as direct evidence that
  public creator pressure changes platform policy.
- This branch correctly starts from `origin/main`, so the provisional
  governance theme update combines the already-merged
  `norton_shapiro_2024` card with this new Hallinan card; later Batch
  5 governance PRs will touch the same theme stub and may need merge
  cleanup.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/hallinan_et_al_2025?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20hallinan_et_al_2025&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/hallinan_et_al_2025.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20using%20%60norton_shapiro_2024%60%20plus%20the%20new%20Hallinan%20source%20card.%0A%0A%23%23%20Pages%0A-%20wiki/sources/hallinan_et_al_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md

## 2026-04-16 — Ingest ribeiro_west_2021
**Operation:** ingest-source
**Branch:** ingest/ribeiro_west_2021
**By:** Codex (GPT-5)

Ingested `ribeiro_west_2021` via the `ingest-source`
workflow. Created `wiki/sources/ribeiro_west_2021.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/cross_linguistic_variation.md`,
`wiki/themes/descriptive_deficit.md`, and `wiki/index.md`.

Literature-review cross-check note:

- The review does not summarize this paper directly. No contradiction
  was detectable because the review's cross-linguistic discussion is
  built around the McGrady papers rather than around YouNiverse.
## 2026-04-16 — Ingest hallinan_reynolds_2024
**Operation:** ingest-source
**Branch:** ingest/hallinan_reynolds_2024
**By:** Codex (GPT-5)

Ingested `hallinan_reynolds_2024` via the `ingest-source` workflow.
Created `wiki/sources/hallinan_reynolds_2024.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/governance_data_access.md`, and `wiki/index.md`.

Literature-review cross-check note:

- This paper is not summarized directly in the internal literature
  review, so the source card was rebuilt from the original article.

Tier and taxonomy decisions:

- Assigned `primary_empirical`.
- Reused the existing theme tags `cross-linguistic-variation` and
  `descriptive-deficit`; no taxonomy additions proposed.
- In the source registry, the paper is slotted into `journal_article`
  because the current schema lacks a conference-paper type.

Human attention requested:

- This source is crucial mainly because it reveals an infrastructural
  blind spot: a huge public YouTube dataset can still be English-only.
  It should not be treated as direct multilingual evidence in the same
  way as `mcgrady_2025`.
- The `descriptive_deficit` page received only a minimal `[🤖]`
  incremental update here. It should be fully re-refreshed in a future
  batch if the English-centric infrastructure strand becomes more
  central to the manuscript argument.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/ribeiro_west_2021?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20ribeiro_west_2021&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/ribeiro_west_2021.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/cross_linguistic_variation.md%60%2C%20%60wiki/themes/descriptive_deficit.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Populated%20the%20cross-linguistic%20theme%20stub%20from%20%60mcgrady_2023%60%2C%20%60mcgrady_2025%60%2C%20and%20the%20new%20Ribeiro/West%20source%2C%20plus%20added%20a%20minimal%20descriptive-deficit%20note%20flagged%20for%20future%20refresh.%0A%0A%23%23%20Pages%0A-%20wiki/sources/ribeiro_west_2021.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/cross_linguistic_variation.md%0A-%20wiki/themes/descriptive_deficit.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest european_commission_2025
**Operation:** ingest-source
**Branch:** ingest/european_commission_2025
**By:** Codex (GPT-5)

Ingested `european_commission_2025` via the `ingest-from-review`
workflow. Created `wiki/sources/european_commission_2025.md` and
updated `data/source-registry.yaml`, `data/claim-registry.yaml`,
- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/hallinan_et_al_2025?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20hallinan_et_al_2025&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/hallinan_et_al_2025.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%20and%20%60wiki/index.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20using%20%60norton_shapiro_2024%60%20plus%20the%20new%20Hallinan%20source%20card.%0A%0A%23%23%20Pages%0A-%20wiki/sources/hallinan_et_al_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md
- Reused the existing theme tag `governance-data-access`; no taxonomy
  additions proposed.
- Updated the existing informal creator-accountability claim rather
  than duplicating it, then added one new claim for horizontal versus
  vertical callouts.

Human attention requested:

- The paper is strongest on how creators frame and route copyright
  disputes in public, not on whether those public complaints change
  policy outcomes inside YouTube.
- This branch correctly starts from `origin/main`, so the governance
  theme update is intentionally provisional and will conflict with
  later Batch 5 governance ingests plus the parked refresh branch.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/hallinan_reynolds_2024?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20hallinan_reynolds_2024&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/hallinan_reynolds_2024.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20distinguishing%20horizontal%20copyright%20callouts%20from%20vertical%20appeals%20toward%20platforms%20and%20rights%20holders.%0A%0A%23%23%20Pages%0A-%20wiki/sources/hallinan_reynolds_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md

## 2026-04-16 — Ingest reynolds_hallinan_2024
**Operation:** ingest-source
**Branch:** ingest/reynolds_hallinan_2024
**By:** Codex (GPT-5)

Ingested `reynolds_hallinan_2024` via the `ingest-source` workflow.
Created `wiki/sources/reynolds_hallinan_2024.md` and updated
## 2026-04-16 — Ingest marchal_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/marchal_et_al_2025
**By:** Codex (GPT-5)

Ingested `marchal_et_al_2025` via the `ingest-source`
workflow. Created `wiki/sources/marchal_et_al_2025.md` and updated
## 2026-04-16 — Ingest ozturan_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/ozturan_et_al_2025
**By:** Codex (GPT-5)

Ingested `ozturan_et_al_2025` via the `ingest-source`
workflow. Created `wiki/sources/ozturan_et_al_2025.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/governance_data_access.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced. The review accurately captures
  the document's core claims about the October 29, 2025 start date, the
  role of Digital Services Coordinators, and the fact that the access
  regime is new rather than evaluated.

Tier and taxonomy decisions:

- Assigned `platform_documentation`, not `policy_research`, because the
  document announces policy and procedure but contains no original
  analysis.
- Reused the existing theme tag `governance-data-access`; no taxonomy
  additions proposed.
- Added one methodological claim for the formal DSA access mechanism and
  kept its scope explicitly limited to policy facts rather than
  implementation success.

Human attention requested:

- This source can support policy facts about the DSA access route, but
  not evidence that the route materially improves YouTube research in
  practice.
- It also creates the clearest temporal breakpoint in the governance
  theme so far: `October 29, 2025` now needs to be treated as a distinct
  post-DSA access era.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/european_commission_2025?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20european_commission_2025&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/european_commission_2025.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20using%20%60norton_shapiro_2024%60%2C%20%60hallinan_et_al_2025%60%2C%20and%20the%20new%20DSA%20access-policy%20source%20card.%0A%0A%23%23%20Pages%0A-%20wiki/sources/european_commission_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest hallinan_reynolds_2024
**Operation:** ingest-source
**Branch:** ingest/hallinan_reynolds_2024
**By:** Codex (GPT-5)

Ingested `hallinan_reynolds_2024` via the `ingest-source` workflow.
Created `wiki/sources/hallinan_reynolds_2024.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/governance_data_access.md`, and `wiki/index.md`.
- This paper is not summarized directly in the internal literature
  review, so the source card was rebuilt from the original article
  rather than from review scaffolding.
- This paper is not summarized directly in the internal literature
  review. No contradiction was detectable because the review does not
  currently make any source-specific claims about it.
- This paper is not summarized directly in the internal literature
  review, so the source card was rebuilt from the original article
  rather than from review scaffolding.

Tier and taxonomy decisions:

- Assigned `primary_empirical`.
- Reused the existing theme tag `governance-data-access`; no taxonomy
  additions proposed.
- Updated the existing informal creator-accountability claim rather
  than duplicating it, then added one new claim for horizontal versus
  vertical callouts.

Human attention requested:

- The paper is strongest on how creators frame and route copyright
  disputes in public, not on whether those public complaints change
  policy outcomes inside YouTube.
- This branch correctly starts from `origin/main`, so the governance
  theme update is intentionally provisional and will conflict with
  later Batch 5 governance ingests plus the parked refresh branch.
- The source card cross-links to `reynolds_hallinan_2024`, which is a
  planned Batch 5 ingest rather than a page currently on `main`.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/hallinan_reynolds_2024?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20hallinan_reynolds_2024&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/hallinan_reynolds_2024.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20distinguishing%20horizontal%20copyright%20callouts%20from%20vertical%20appeals%20toward%20platforms%20and%20rights%20holders.%0A%0A%23%23%20Pages%0A-%20wiki/sources/hallinan_reynolds_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md
- Updated the existing informal-accountability claim and added one new
  claim for user-generated accountability so the paper's empirical and
  conceptual contributions are both represented in the registry.

Human attention requested:

- The paper's corpus spans `2015-2023`, so it should not be read as a
  pure post-2019 snapshot even though many of its governance dynamics
  are most relevant to the later period.
- This branch correctly starts from `origin/main`, so the provisional
  governance theme update combines `norton_shapiro_2024`,
  `hallinan_et_al_2025`, and this new source card; later Batch 5
  governance PRs will touch the same theme stub and may need merge
  cleanup.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/reynolds_hallinan_2024?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20reynolds_hallinan_2024&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/reynolds_hallinan_2024.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20using%20%60norton_shapiro_2024%60%2C%20%60hallinan_et_al_2025%60%2C%20and%20the%20new%20user-generated-accountability%20source%20card.%0A%0A%23%23%20Pages%0A-%20wiki/sources/reynolds_hallinan_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md

## 2026-04-16 — Ingest marchal_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/marchal_et_al_2025
**By:** Codex (GPT-5)

Ingested `marchal_et_al_2025` via the `ingest-source`
workflow. Created `wiki/sources/marchal_et_al_2025.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/governance_data_access.md`, and `wiki/index.md`.

Literature-review cross-check note:

- This paper is not summarized directly in the internal literature
  review. No contradiction was detectable because the review does not
  currently make any source-specific claims about it.

Tier and taxonomy decisions:

- Assigned `primary_empirical`.
- Reused the existing theme tag `governance-data-access`; no taxonomy
  additions proposed.
- Added one comparative claim about negative media pressure and public-
  facing policy change, keeping the claim text explicitly
  non-causal and non-YouTube-exclusive.

Human attention requested:

- This is comparative platform-governance evidence, not YouTube-only
  evidence. It should support the governance theme as contextual
  comparative evidence, not as a substitute for YouTube-specific
  process evidence.
- The study ends in early 2021, so it does not speak directly to the
  post-2022 or post-October-2025 governance environment flagged in the
  taxonomy.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/marchal_et_al_2025?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20marchal_et_al_2025&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/marchal_et_al_2025.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20using%20%60norton_shapiro_2024%60%2C%20%60hallinan_et_al_2025%60%2C%20and%20the%20new%20comparative%20media-pressure%20source%20card.%0A%0A%23%23%20Pages%0A-%20wiki/sources/marchal_et_al_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md

## 2026-04-16 — Ingest ozturan_et_al_2025
**Operation:** ingest-source
**Branch:** ingest/ozturan_et_al_2025
**By:** Codex (GPT-5)

Ingested `ozturan_et_al_2025` via the `ingest-source`
workflow. Created `wiki/sources/ozturan_et_al_2025.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/governance_data_access.md`, and `wiki/index.md`.

Literature-review cross-check note:

- This paper is not summarized directly in the internal literature
  review. No contradiction was detectable because the review does not
  currently make any source-specific claims about it.

Tier and taxonomy decisions:

- Assigned `primary_empirical`.
- Reused the existing theme tag `governance-data-access`; no taxonomy
  additions proposed.
- Marked `census_relevance` as `low` because the study is comparative
  platform-governance evidence from Twitter/X rather than direct
  YouTube evidence.

Human attention requested:

- This source should be used only as comparative evidence that
  governance changes can affect information quality. It is not direct
  evidence about YouTube.
- The paper also illustrates the access problem directly: X policy
  changes cut off the study's usable data in May 2023, so long-run
  persistence cannot be evaluated.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/ozturan_et_al_2025?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20ozturan_et_al_2025&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/ozturan_et_al_2025.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20using%20%60norton_shapiro_2024%60%2C%20%60hallinan_et_al_2025%60%2C%20and%20the%20new%20comparative%20governance-change%20source%20card.%0A%0A%23%23%20Pages%0A-%20wiki/sources/ozturan_et_al_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md

## 2026-04-16 — Refresh cross_linguistic_variation
**Operation:** refresh-theme
**Branch:** refresh/cross_linguistic_variation
**By:** Codex (GPT-5)

Refreshed `wiki/themes/cross_linguistic_variation.md` from the
three-source corpus and kept the branch self-contained by carrying the
Ribeiro source card and registry infrastructure alongside the theme.

Refresh note:

- The refreshed page is explicit about thinness: enough evidence to
  reject English-first generalization, not enough for broad
  multilingual or cross-national manuscript claims.
- Cross-language claims are stronger than cross-national claims in the
  current corpus because the available sources mostly measure language
  rather than geography directly.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/cross_linguistic_variation?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20cross_linguistic_variation&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/cross_linguistic_variation.md%60%20from%20the%20three-source%20cross-linguistic%20corpus.%0A-%20Kept%20the%20branch%20self-contained%20by%20including%20%60ribeiro_west_2021%60%20and%20its%20registry%20infrastructure%20alongside%20the%20refreshed%20theme.%0A-%20Made%20the%20page%20explicit%20about%20evidence%20thinness%3A%20enough%20to%20reject%20English-first%20generalization%2C%20not%20enough%20for%20broad%20multilingual%20or%20cross-national%20manuscript%20claims.%0A%0A%23%23%20Sources%0A-%20mcgrady_2023%0A-%20mcgrady_2025%0A-%20ribeiro_west_2021%0A%0A%23%23%20Pages%0A-%20wiki/themes/cross_linguistic_variation.md%0A-%20ops/log.md
## 2026-04-16 — Ingest european_commission_2025
**Operation:** ingest-source
**Branch:** ingest/european_commission_2025
**By:** Codex (GPT-5)

Ingested `european_commission_2025` via the `ingest-from-review`
workflow. Created `wiki/sources/european_commission_2025.md` and
updated `data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/governance_data_access.md`, and `wiki/index.md`.

Literature-review cross-check note:

- No material contradiction surfaced. The review accurately captures
  the document's core claims about the October 29, 2025 start date, the
  role of Digital Services Coordinators, and the fact that the access
  regime is new rather than evaluated.

Tier and taxonomy decisions:

- Assigned `platform_documentation`, not `policy_research`, because the
  document announces policy and procedure but contains no original
  analysis.
- Reused the existing theme tag `governance-data-access`; no taxonomy
  additions proposed.
- Added one methodological claim for the formal DSA access mechanism and
  kept its scope explicitly limited to policy facts rather than
  implementation success.

Human attention requested:

- This source can support policy facts about the DSA access route, but
  not evidence that the route materially improves YouTube research in
  practice.
- It also creates the clearest temporal breakpoint in the governance
  theme so far: `October 29, 2025` now needs to be treated as a distinct
  post-DSA access era.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/european_commission_2025?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20european_commission_2025&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/european_commission_2025.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20using%20%60norton_shapiro_2024%60%2C%20%60hallinan_et_al_2025%60%2C%20and%20the%20new%20DSA%20access-policy%20source%20card.%0A%0A%23%23%20Pages%0A-%20wiki/sources/european_commission_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md

## 2026-04-16 — Refresh governance_data_access
**Operation:** refresh-theme
**Branch:** refresh/governance_data_access
**By:** Codex (GPT-5)

Refreshed `wiki/themes/governance_data_access.md` from the full
seven-source governance corpus and kept the supporting source-card
infrastructure on-branch so the refresh remains self-contained for
verification before the ingest branches merge.

Refresh note:

- Temporal scoping remains explicit across the early-2020s opacity
  regime, the 2015-2023 creator-accountability corpus, the 2022-2023
  comparative governance-shift evidence, and the post-October-29-2025
  DSA access regime.
- The refreshed page now has enough material to support a real theme
  synthesis, but it may eventually need splitting if creator
  accountability and formal access / policy-response evidence continue
  to accumulate separately.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/governance_data_access?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20governance_data_access&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/governance_data_access.md%60%20from%20the%20full%207-source%20governance%20corpus.%0A-%20Included%20the%20five%20new%20Batch%205%20governance%20source%20cards%20and%20their%20registry%20infrastructure%20on%20this%20branch%20so%20the%20refreshed%20theme%20remains%20self-contained%20for%20verification%20before%20those%20ingest%20branches%20merge.%0A-%20Kept%20temporal%20scoping%20explicit%20across%20the%20early-2020s%20opacity%20regime%2C%20the%202015-2023%20creator-accountability%20corpus%2C%20the%202022-2023%20comparative%20governance-shift%20evidence%2C%20and%20the%20post-October-29-2025%20DSA%20access%20regime.%0A%0A%23%23%20Sources%0A-%20norton_shapiro_2024%0A-%20hallinan_et_al_2025%0A-%20hallinan_reynolds_2024%0A-%20reynolds_hallinan_2024%0A-%20marchal_et_al_2025%0A-%20ozturan_et_al_2025%0A-%20european_commission_2025%0A%0A%23%23%20Pages%0A-%20wiki/themes/governance_data_access.md%0A-%20ops/log.md

## 2026-04-16 — Ingest ledwich_zaitsev_2020
**Operation:** ingest-source
**Branch:** ingest/ledwich_zaitsev_2020
**By:** Codex (GPT-5)

Ingested `ledwich_zaitsev_2020` via the `ingest-source`
workflow. Created `wiki/sources/ledwich_zaitsev_2020.md`
## 2026-04-16 — Ingest ribeiro_et_al_2020
**Operation:** ingest-source
**Branch:** ingest/ribeiro_et_al_2020
**By:** Codex (GPT-5)

Ingested `ribeiro_et_al_2020` via the `ingest-source`
workflow. Created `wiki/sources/ribeiro_et_al_2020.md`
## 2026-04-16 — Ingest faddoul_et_al_2020
**Operation:** ingest-source
**Branch:** ingest/faddoul_et_al_2020
**By:** Codex (GPT-5)

Ingested `faddoul_et_al_2020` via the `ingest-source`
workflow. Created `wiki/sources/faddoul_et_al_2020.md`
and updated `data/source-registry.yaml`,
`data/claim-registry.yaml`,
## 2026-04-16 — Ingest ribeiro_veselovsky_west_2023
**Operation:** ingest-source
**Branch:** ingest/ribeiro_veselovsky_west_2023
**By:** Codex (GPT-5)

Ingested `ribeiro_veselovsky_west_2023` via the
`ingest-source` workflow. Created
`wiki/sources/ribeiro_veselovsky_west_2023.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/recommendation_radicalization.md`,
## 2026-04-16 — Ingest abou_el_komboz_et_al_2023
**Operation:** ingest-source
**Branch:** ingest/abou_el_komboz_et_al_2023
**By:** Codex (GPT-5)

Ingested `abou_el_komboz_et_al_2023` via the `ingest-source`
workflow. Created
`wiki/sources/abou_el_komboz_et_al_2023.md` and updated
`data/source-registry.yaml`,
`data/claim-registry.yaml`, `wiki/themes/creator_economy.md`,
`wiki/index.md`, and `ops/log.md`.

Literature-review cross-check note:

- No internal literature-review summary currently exists for this
  paper, so no direct contradiction check was possible against a
  source-specific project memo.

Tier and taxonomy decisions:

- Assigned `primary_empirical` because the archived source presents
  original data collection, channel coding, and a recommendation
  audit even though the corpus PDF is a preprint rather than the
  final journal layout.
- Reused the existing theme tag
  `recommendation-radicalization`; no taxonomy additions proposed.
- Added one cross-cutting claim for the paper's core contrarian
  finding that anonymous recommendation flows mainstream rather
  than intensify extremist exposure.

Human attention requested:

- The batch prompt cites this source as a 2020 *First Monday*
  publication, but the archived PDF in the corpus is the December
  2019 preprint version submitted to *First Monday*; page citations
  on the source card follow the archived PDF.
- Temporal placement needs care: the paper is often treated as an
  older rabbit-hole source, but the measured recommendation audit is
  a 2019 anonymous-baseline snapshot rather than a clean pre-2019
  benchmark.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/ledwich_zaitsev_2020?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20ledwich_zaitsev_2020&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/ledwich_zaitsev_2020.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20recommendation-theme%20note%20positioning%20Ledwich%20and%20Zaitsev%20as%20a%202019%20anonymous%20contrarian%20audit.%0A%0A%23%23%20Pages%0A-%20wiki/sources/ledwich_zaitsev_2020.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
- No internal literature-review summary currently isolates this
  paper, so no source-specific contradiction check was possible
  against a project memo.

Tier and taxonomy decisions:

- Assigned `primary_empirical`; the paper combines original
  comment-trace analysis and recommendation auditing even though
  the archived corpus copy is the arXiv version of a published
  conference paper.
- Reused the existing theme tag
  `recommendation-radicalization`; no taxonomy additions proposed.
- Added two cross-cutting claims: one for commenter migration
  toward Alt-right channels and one for the distinction between
  channel and video recommendation reachability.

Human attention requested:

- Temporal scope needs careful handling because the paper combines
  historical commenter migration evidence through 2018 with a
  separate May-July 2019 recommendation snapshot.
- The paper is foundational for the rabbit-hole debate, but its
  migration result is based on commenters rather than full viewing
  histories and its recommendation result is nonpersonalized.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/ribeiro_et_al_2020?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20ribeiro_et_al_2020&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/ribeiro_et_al_2020.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20recommendation-theme%20note%20capturing%20commenter%20migration%20and%20channel-level%20Alt-right%20reachability.%0A%0A%23%23%20Pages%0A-%20wiki/sources/ribeiro_et_al_2020.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
- No internal literature-review memo currently isolates this
  paper, so the cross-check was against the PDF itself rather
  than against a preexisting project summary.

Tier and taxonomy decisions:

- Assigned `primary_empirical`; this is an original
  longitudinal audit with a custom classifier and repeated
  recommendation collection, even though the archived corpus
  copy is an arXiv preprint rather than a journal article.
- Reused the existing theme tag
  `recommendation-radicalization`; no taxonomy additions
  proposed.
- Added two cross-cutting claims: one for the decline and
  partial rebound of default conspiracy recommendations
  across the 2019 policy shift, and one for the declining but
  persistent conspiracy filter-bubble pattern in default
  watch-next recommendations.

Human attention requested:

- Treat this as transition-period evidence only. The audit
  spans October 2018 through February 2020 and should not be
  generalized to the current recommender.
- The study is nonpersonalized and rooted in popular
  informational channels, so it captures default
  discoverability rather than full logged-in user behavior.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/faddoul_et_al_2020?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20faddoul_et_al_2020&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/faddoul_et_al_2020.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20recommendation-theme%20note%20framing%20the%202019%20conspiracy-demotion%20period%20as%20a%20real%20but%20incomplete%20recommendation%20shift.%0A%0A%23%23%20Pages%0A-%20wiki/sources/faddoul_et_al_2020.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
- No internal literature-review memo currently isolates this
  paper, so the cross-check was against the PDF and the
  existing recommendation-theme framing rather than against
  a project summary.

Tier and taxonomy decisions:

- Assigned `primary_empirical` under current atlas rules
  because this is a peer-reviewed original research paper,
  even though its contribution is a stylized agent-based
  model rather than direct platform observation.
- Reused the existing theme tag
  `recommendation-radicalization`; no taxonomy additions
  proposed.
- Added one theoretical claim about deamplification in
  consumption and one methodological claim about the limits
  of audit studies that ignore user preferences.

Human attention requested:

- This source should not be cited as direct evidence about
  the current YouTube recommender. It is a model-based
  interpretation aid for the audit-versus-navigation-log
  disagreement.
- Its main value is conceptual: it sharpens how the atlas
  should discuss "amplification" and the inferential limits
  of blind-following audit designs.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/ribeiro_veselovsky_west_2023?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20ribeiro_veselovsky_west_2023&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/ribeiro_veselovsky_west_2023.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20recommendation-theme%20note%20explaining%20how%20audit-style%20amplification%20and%20real-user%20deamplification%20can%20coexist.%0A%0A%23%23%20Pages%0A-%20wiki/sources/ribeiro_veselovsky_west_2023.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest huang_yang_2024
**Operation:** ingest-source
**Branch:** ingest/huang_yang_2024
**By:** Codex (GPT-5)

Ingested `huang_yang_2024` via the `ingest-source`
workflow. Created `wiki/sources/huang_yang_2024.md` and
## 2026-04-16 — Ingest wu_resnick_2021
**Operation:** ingest-source
**Branch:** ingest/wu_resnick_2021
**By:** Codex (GPT-5)

Ingested `wu_resnick_2021` via the `ingest-source`
workflow. Created `wiki/sources/wu_resnick_2021.md` and
updated `data/source-registry.yaml`,
`data/claim-registry.yaml`,
`wiki/themes/recommendation_radicalization.md`,
`wiki/themes/news_ecosystem.md`, `wiki/index.md`, and
## 2026-04-16 — Ingest reveilhac_2024
**Operation:** ingest-source
**Branch:** ingest/reveilhac_2024
**By:** Codex (GPT-5)

Ingested `reveilhac_2024` via the `ingest-source`
workflow. Created `wiki/sources/reveilhac_2024.md` and
updated `data/source-registry.yaml`,
`data/claim-registry.yaml`, `wiki/themes/news_ecosystem.md`,
`wiki/themes/descriptive_deficit.md`, `wiki/index.md`, and
`ops/log.md`.

Literature-review cross-check note:

- No internal literature-review memo currently isolates this
  paper, so the cross-check was against the PDF and the
  existing theme stubs rather than against a prewritten
  project summary.

Tier and taxonomy decisions:

- Assigned `primary_empirical`; the paper reanalyzes a
  large recommendation dataset with transition-network and
  Markov-chain methods.
- Reused the existing theme tags
  `recommendation-radicalization` and `news-ecosystem`;
  no taxonomy additions proposed.
- Added two cross-cutting claims capturing
  news-to-entertainment redirection and the broader
  entertainment-over-news steady-state bias in Up Next
  recommendations.

Human attention requested:

- Treat this as a nonpersonalized 2019 benchmark, not as
  direct evidence about the current logged-in recommender.
- The paper is especially useful because it identifies a
  recommendation harm that is not primarily ideological:
  diversion away from public-affairs content.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/huang_yang_2024?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20huang_yang_2024&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/huang_yang_2024.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/themes/news_ecosystem.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20theme%20notes%20showing%20that%20recommendation%20harm%20can%20operate%20through%20news-to-entertainment%20redirection%2C%20not%20only%20through%20ideological%20escalation.%0A%0A%23%23%20Pages%0A-%20wiki/sources/huang_yang_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/themes/news_ecosystem.md%0A-%20wiki/index.md%0A-%20ops/log.md
- The prompt citation described this as an online-first Press/
  Politics article, but the archived PDF identifies the
  publication as `First Monday 29(7)` with DOI
  `10.5210/fm.v29i7.13633`.

Tier and taxonomy decisions:

- Assigned `primary_empirical`; this is an original mixed-
  methods descriptive study of a 2023 French alternative-
  news subsystem on YouTube.
- Reused the existing theme tags `news-ecosystem` and
  `descriptive-deficit`; no taxonomy additions proposed.
- Added one cross-cutting claim on clustered alternative-
  news channel types and their overlapping commenter
  publics.

Human attention requested:

- This paper is highly useful for the news theme but does not
  solve the wider descriptive-deficit problem; it remains a
  France-only, alternative-news-only, top-videos-only
  snapshot.
- The source also highlights a recurring issue in the atlas:
  much of the available descriptive work is rich within a
  subsystem but thin as a platform-wide baseline.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/reveilhac_2024?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20reveilhac_2024&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/reveilhac_2024.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/news_ecosystem.md%60%2C%20%60wiki/themes/descriptive_deficit.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20theme%20notes%20showing%20how%20a%20peer-reviewed%20country-level%20mapping%20study%20fills%20the%20news%20theme%20while%20also%20illustrating%20the%20descriptive%20literature's%20boundedness.%0A%0A%23%23%20Pages%0A-%20wiki/sources/reveilhac_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/news_ecosystem.md%0A-%20wiki/themes/descriptive_deficit.md%0A-%20wiki/index.md%0A-%20ops/log.md
- The prompt supplied a later Information Economics and
  Policy citation, but the archived corpus PDF is `CESifo
  Working Paper No. 10363` (April 2023). All page-verified
  claims here were checked against the working-paper version.

Tier and taxonomy decisions:

- Assigned `primary_empirical`; this is original causal
  analysis using a regression discontinuity design.
- Reused the existing theme tag `creator-economy`; no
  taxonomy additions proposed.
- Added one cross-cutting causal claim on the effect of
  losing YPP access on output frequency, quality, and
  diversity.

Human attention requested:

- Treat this as the strongest causal monetization-shock
  estimate in the current archive, but note that it is local
  to small German creators near the 1,000-subscriber cutoff.
- The paper also complicates simple pecuniary models by
  showing heterogeneous reactions tied to creator type and
  experience.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/abou_el_komboz_et_al_2023?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20abou_el_komboz_et_al_2023&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/abou_el_komboz_et_al_2023.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/creator_economy.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20creator-economy%20note%20showing%20that%20losing%20YPP%20access%20causally%20reduced%20small-creator%20output%2C%20quality%2C%20and%20diversity.%0A%0A%23%23%20Pages%0A-%20wiki/sources/abou_el_komboz_et_al_2023.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/creator_economy.md%0A-%20wiki/index.md%0A-%20ops/log.md
  existing debate framing rather than against a project
  summary.

Tier and taxonomy decisions:

- Assigned `primary_empirical`; this is an original
  large-scale observational study of YouTube political
  discussion using platform data and inferred user ideology.
- Reused the existing theme tags
  `recommendation-radicalization` and `news-ecosystem`;
  no taxonomy additions proposed.
- Added two cross-cutting claims: one on common but
  asymmetric cross-partisan commenting, and one on reduced
  cross-partisan visibility plus higher toxicity in reply
  threads.

Human attention requested:

- This source is crucial for the filter-bubble debate, but it
  should not be mistaken for direct recommender evidence; it
  studies comment interaction on partisan channels.
- The key takeaway is mixed: ideological isolation is weaker
  than a pure echo-chamber story implies, but cross-partisan
  contact is asymmetric and often not constructive.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/wu_resnick_2021?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20wu_resnick_2021&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/wu_resnick_2021.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/themes/news_ecosystem.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20theme%20notes%20showing%20that%20cross-partisan%20discussion%20on%20YouTube%20is%20real%20but%20asymmetric%20and%20not%20uniformly%20civil.%0A%0A%23%23%20Pages%0A-%20wiki/sources/wu_resnick_2021.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/themes/news_ecosystem.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Refresh recommendation_radicalization
**Operation:** refresh-theme
**Branch:** refresh/recommendation_radicalization
**By:** Codex (GPT-5)

Refreshed `wiki/themes/recommendation_radicalization.md` and all three
linked debate pages from the enlarged recommendation corpus, while
keeping the six new Batch 6 source cards and their registry
infrastructure on-branch so the refresh remains self-contained before
the ingest branches merge.

Refresh note:

- The refresh now treats the literature as four periods rather than
  two: pre-2018 ecosystem formation, the 2019 transition, 2020
  real-user/comment evidence, and the thinner 2022-2024 intervention
  literature.
- The debate pages now make the transition-period disagreement
  explicit: Ledwich, Ribeiro, and Faddoul no longer permit a simple
  one-line story about what the 2019 break did.
- The filter-bubble page now distinguishes ideological narrowing,
  news-to-entertainment diversion, and comment-layer hostility instead
  of treating them as one outcome.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/recommendation_radicalization?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20recommendation_radicalization&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/recommendation_radicalization.md%60%20and%20all%20three%20debate%20pages%3A%20%60wiki/debates/rabbit_hole_debate.md%60%2C%20%60wiki/debates/filter_bubble_evidence.md%60%2C%20and%20%60wiki/debates/pre_2019_vs_post_2019_algorithm.md%60.%0A-%20Included%20the%20six%20new%20radicalization-relevant%20source%20cards%20and%20registry%20infrastructure%20on-branch%20so%20the%20refresh%20remains%20self-contained%20before%20the%20ingest%20branches%20merge.%0A-%20Reframed%20the%20corpus%20around%20pre-2018%20growth%2C%202019%20transition%20audits%2C%202020%20real-user/comment%20evidence%2C%20and%20thinner%202022-2024%20intervention%20work.%0A%0A%23%23%20Sources%0A-%20ledwich_zaitsev_2020%0A-%20ribeiro_et_al_2020%0A-%20faddoul_et_al_2020%0A-%20ribeiro_veselovsky_west_2023%0A-%20huang_yang_2024%0A-%20wu_resnick_2021%0A%0A%23%23%20Pages%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/debates/rabbit_hole_debate.md%0A-%20wiki/debates/filter_bubble_evidence.md%0A-%20wiki/debates/pre_2019_vs_post_2019_algorithm.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Refresh news_ecosystem
**Operation:** refresh-theme
**Branch:** refresh/news_ecosystem
**By:** Codex (GPT-5)

Refreshed `wiki/themes/news_ecosystem.md` from a five-source corpus
spanning recommendation structure, comment interaction, channel
clustering, and audience surveys, while keeping the three new Batch 6
source cards and their registry infrastructure on-branch so the
refresh remains self-contained before those ingest branches merge.

Refresh note:

- The old two-report scaffold has been replaced with a periodized
  synthesis that separates 2019 recommendation drift, 2020 partisan
  discussion, 2023 French subsystem mapping, and 2024-2025
  cross-national survey evidence.
- The refreshed page now treats entertainment diversion, visible
  cross-partisan interaction, and creator-led news competition as
  related but distinct aspects of the YouTube news system.
- The evidence base is materially better than before, but it still
  remains uneven across platform layers and countries.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/news_ecosystem?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20news_ecosystem&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/news_ecosystem.md%60%20from%20a%20five-source%20corpus%20spanning%20recommendation%20structure%2C%20comment%20interaction%2C%20channel%20clustering%2C%20and%20audience%20surveys.%0A-%20Included%20%60huang_yang_2024%60%2C%20%60reveilhac_2024%60%2C%20and%20%60wu_resnick_2021%60%20plus%20their%20registry%20infrastructure%20on-branch%20so%20the%20refresh%20remains%20self-contained%20before%20those%20ingest%20branches%20merge.%0A-%20Replaced%20the%20old%20two-report%20scaffold%20with%20a%20periodized%20synthesis%20that%20distinguishes%202019%20recommendation%20drift%2C%202020%20partisan%20discussion%2C%202023%20French%20subsystem%20mapping%2C%20and%202024-2025%20cross-national%20survey%20evidence.%0A%0A%23%23%20Sources%0A-%20huang_yang_2024%0A-%20reveilhac_2024%0A-%20wu_resnick_2021%0A-%20newman_et_al_2025%0A-%20reuters_dnr_2025%0A%0A%23%23%20Pages%0A-%20wiki/themes/news_ecosystem.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest rieder_2020
**Operation:** ingest-source
**Branch:** ingest/rieder_2020
**By:** Codex (GPT-5)

Ingested `rieder_2020` via the `ingest-source` workflow. Created
`wiki/sources/rieder_2020.md` and updated `data/source-registry.yaml`,
`data/claim-registry.yaml`, `wiki/themes/descriptive_deficit.md`,
`wiki/themes/governance_data_access.md`, `wiki/index.md`, and
## 2026-04-16 — Ingest boesinger_et_al_2024
**Operation:** ingest-source
**Branch:** ingest/boesinger_et_al_2024
**By:** Codex (GPT-5)

Ingested `boesinger_et_al_2024` via the `ingest-source` workflow.
Created `wiki/sources/boesinger_et_al_2024.md` and updated
## 2026-04-16 — Ingest zaitsev_clark_2025
**Operation:** ingest-source
**Branch:** ingest/zaitsev_clark_2025
**By:** Codex (GPT-5)

Ingested `zaitsev_clark_2025` via the `ingest-source` workflow.
Created `wiki/sources/zaitsev_clark_2025.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/descriptive_deficit.md`, `wiki/index.md`, and
`ops/log.md`.

Literature-review cross-check note:

- No source-specific internal review memo currently isolates this paper,
  so the cross-check was against the archived `.mhtml` itself and the
  existing descriptive/governance syntheses rather than against a
  prewritten project summary.

Tier and taxonomy decisions:

- Assigned `primary_empirical` because the article presents original
  large-scale collection and descriptive analysis rather than a pure
  methodological essay.
- Reused the existing theme tags `descriptive-deficit` and
  `governance-data-access`; no taxonomy additions proposed.
- Added one new methodological claim on historically available public
  research affordances and also updated the existing infrastructure-
  constraints claim.
- Recorded `canonical_format: mhtml` because the archived corpus source
  is a web capture rather than a PDF.

Human attention requested:

- The archive filename misspells the first author's surname as
  `Reider`; the article itself clearly identifies the author as
  `Bernhard Rieder`.
- This source is unusually important for periodizing methods claims: it
  documents what large-scale channel crawling could still do in late
  2019 under public-subscription visibility and a 50M-unit/day token,
  which should not be back-projected onto the current platform.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/rieder_2020?quick_pull=1&title=%5Bingest-source%5D+Ingest+rieder_2020&body=%23%23+Summary%0A-+Created+%60wiki%2Fsources%2Frieder_2020.md%60.%0A-+Updated+%60data%2Fsource-registry.yaml%60%2C+%60data%2Fclaim-registry.yaml%60%2C+%60wiki%2Fthemes%2Fdescriptive_deficit.md%60%2C+%60wiki%2Fthemes%2Fgovernance_data_access.md%60%2C+%60wiki%2Findex.md%60%2C+and+%60ops%2Flog.md%60.%0A-+Added+provisional+theme+notes+showing+that+late-2019+large-scale+channel+mapping+depended+on+a+historical+API+and+public-profile+access+regime+that+later+became+harder+to+reproduce.%0A%0A%23%23+Pages%0A-+wiki%2Fsources%2Frieder_2020.md%0A-+data%2Fsource-registry.yaml%0A-+data%2Fclaim-registry.yaml%0A-+wiki%2Fthemes%2Fdescriptive_deficit.md%0A-+wiki%2Fthemes%2Fgovernance_data_access.md%0A-+wiki%2Findex.md%0A-+ops%2Flog.md
  so the cross-check was against the PDF itself and the existing
  descriptive theme rather than against a prewritten project summary.
  so the cross-check was against the archived PDF itself and the
  existing descriptive theme rather than against a prewritten project
  summary.

Tier and taxonomy decisions:

- Assigned `primary_empirical` because the paper presents original data
  collection, embedding construction, and empirical evaluation.
- Reused the existing theme tag `descriptive-deficit`; no taxonomy
  additions proposed.
- Added one methodological claim on scalable channel embeddings from
  public traces.

Human attention requested:

- This is strong classification infrastructure, but it is still built on
  large English-language channels shared on Reddit. It should not be
  read as a platform-wide census method.
- The recommendation embeddings are history-less and gathered over four
  days, so they are best used as reusable channel infrastructure rather
  than as a statement about stable current recommendations.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/boesinger_et_al_2024?quick_pull=1&title=%5Bingest-source%5D+Ingest+boesinger_et_al_2024&body=%23%23+Summary%0A-+Created+%60wiki%2Fsources%2Fboesinger_et_al_2024.md%60.%0A-+Updated+%60data%2Fsource-registry.yaml%60%2C+%60data%2Fclaim-registry.yaml%60%2C+%60wiki%2Fthemes%2Fdescriptive_deficit.md%60%2C+%60wiki%2Findex.md%60%2C+and+%60ops%2Flog.md%60.%0A-+Added+provisional+theme+notes+showing+that+public-trace+embeddings+can+scale+channel+mapping+without+solving+platform-wide+coverage+limits.%0A%0A%23%23+Pages%0A-+wiki%2Fsources%2Fboesinger_et_al_2024.md%0A-+data%2Fsource-registry.yaml%0A-+data%2Fclaim-registry.yaml%0A-+wiki%2Fthemes%2Fdescriptive_deficit.md%0A-+wiki%2Findex.md%0A-+ops%2Flog.md
  collection, discovery/classification methods, and empirical results.
- Reused the existing theme tag `descriptive-deficit`; no taxonomy
  additions proposed.
- Updated two existing methodological claims rather than creating a new
  registry entry: one on denominator/coverage problems and one on
  infrastructure constraints.

Human attention requested:

- The prompt named `Justin Clark`, but the archived paper credits
  `Sam Clark`; the source card and registry follow the paper itself.
- Treat the method as historically specific to 2020 public-subscription
  visibility. The paper is valuable precisely because it states that
  this access path has since narrowed.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/zaitsev_clark_2025?quick_pull=1&title=%5Bingest-source%5D+Ingest+zaitsev_clark_2025&body=%23%23+Summary%0A-+Created+%60wiki%2Fsources%2Fzaitsev_clark_2025.md%60.%0A-+Updated+%60data%2Fsource-registry.yaml%60%2C+%60data%2Fclaim-registry.yaml%60%2C+%60wiki%2Fthemes%2Fdescriptive_deficit.md%60%2C+%60wiki%2Findex.md%60%2C+and+%60ops%2Flog.md%60.%0A-+Added+provisional+theme+notes+showing+that+head-only+political+YouTube+samples+miss+substantial+small-channel+right+and+conspiracy+content+and+that+the+enabling+subscription-visibility+regime+was+historical.%0A%0A%23%23+Pages%0A-+wiki%2Fsources%2Fzaitsev_clark_2025.md%0A-+data%2Fsource-registry.yaml%0A-+data%2Fclaim-registry.yaml%0A-+wiki%2Fthemes%2Fdescriptive_deficit.md%0A-+wiki%2Findex.md%0A-+ops%2Flog.md
## 2026-04-16 — Refresh channel_classification_methods
**Operation:** refresh-theme
**Branch:** refresh/channel_classification_methods
**By:** Codex (GPT-5)

Created `wiki/methods/channel_classification.md` and kept the branch
self-contained by carrying `rieder_2020`, `boesinger_et_al_2024`, and
`zaitsev_clark_2025` plus the needed source-registry and
claim-registry infrastructure on-branch before those ingest branches
merge.

Refresh note:

- The new methods page treats channel classification as a stack:
  access regime, discovery universe, representation, classifier, and
  evaluation all need to be separated.
- Rieder anchors the historical access regime, Boesinger provides the
  embedding comparison, and Zaitsev/Clark provides the strongest
  end-to-end discovery-plus-classification pipeline in the current
  archive.
- The page explicitly cross-references `ideology_estimation` rather
  than collapsing channel classification into a one-dimensional
  partisan measurement problem.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/channel_classification_methods?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20channel_classification_methods&body=%23%23%20Summary%0A-%20Created%20%60wiki/methods/channel_classification.md%60.%0A-%20Included%20%60rieder_2020%60%2C%20%60boesinger_et_al_2024%60%2C%20and%20%60zaitsev_clark_2025%60%20plus%20the%20needed%20source-registry%20and%20claim-registry%20infrastructure%20on-branch%20so%20the%20methods%20page%20remains%20self-contained%20before%20those%20ingest%20branches%20merge.%0A-%20Synthesized%20the%20method%20family%20around%20historical%20access%20regimes%2C%20embedding-based%20versus%20metadata/subscription-based%20classification%2C%20evaluation%20choices%2C%20and%20implications%20for%20the%20project%27s%20own%20pipeline.%0A%0A%23%23%20Sources%0A-%20rieder_2020%0A-%20boesinger_et_al_2024%0A-%20zaitsev_clark_2025%0A%0A%23%23%20Pages%0A-%20wiki/methods/channel_classification.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/sources/rieder_2020.md%0A-%20wiki/sources/boesinger_et_al_2024.md%0A-%20wiki/sources/zaitsev_clark_2025.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest lewis_2018
**Operation:** ingest-source
**Branch:** ingest/lewis_2018
**By:** Codex (GPT-5)

Created `wiki/sources/lewis_2018.md` for Rebecca Lewis's *Alternative
Influence* report and updated the recommendation theme, registries,
index, and log.

Cross-check notes:

- Verified the archived source is the 2018 Data & Society Research
  Institute report, not a later journal adaptation.
- Confirmed the core empirical base is a manually assembled
  65-influencer / 81-channel guest network plus qualitative transcript
  analysis, with collaboration data spanning January 1, 2017 to April
  1, 2018.
- Added one new cross-cutting claim on pre-2019 guest-network pathways
  across reactionary political YouTube.

Tier decision:

- Assigned `policy_research`, not `primary_empirical`, because the
  report presents original analysis in a non-peer-reviewed research-
  institute format.

Human attention requested:

- Treat this as foundational pre-2019 ecosystem evidence, not as a
  direct estimate of logged recommendation behavior.
- The report is likely to matter heavily in the later recommendation
  refresh because it strengthens the pre-2019 side of the regime-change
  debate without resolving mechanism attribution by itself.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/lewis_2018?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20lewis_2018&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/lewis_2018.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20recommendation-theme%20notes%20anchoring%20pre-2019%20ecosystem%20evidence%20in%20Lewis%27s%20Alternative%20Influence%20Network%20map.%0A%0A%23%23%20Pages%0A-%20wiki/sources/lewis_2018.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest hosseinmardi_et_al_2021
**Operation:** ingest-source
**Branch:** ingest/hosseinmardi_et_al_2021
**By:** Codex (GPT-5)

Created `wiki/sources/hosseinmardi_et_al_2021.md` and updated the
## 2026-04-16 — Ingest hussein_et_al_2020
**Operation:** ingest-source
**Branch:** ingest/hussein_et_al_2020
**By:** Codex (GPT-5)

Created `wiki/sources/hussein_et_al_2020.md` and updated the
recommendation theme, registries, index, and log.

Cross-check notes:

- Verified the archived file is the 2021 *PNAS* article, not the later
  2024 counterfactual-bot paper by overlapping authors.
- Confirmed the core sample: 309,813 U.S. desktop users, 21,385,962
  watched-video pageviews, and observation from January 2016 through
  December 2019.
- Added one new cross-cutting claim on radical-content consumption
  being concentrated among a small predisposed minority rather than
  being systematically recommendation-driven for average users.

Tier decision:

- Assigned `primary_empirical` because this is a peer-reviewed *PNAS*
  article built on original browsing-panel data and original pathway
  analyses.

Human attention requested:

- The study is strong real-user evidence for the late-2010s period, but
  it is desktop-only and cannot directly observe recommendation options
  that users did not click.
- It narrows strong rabbit-hole claims without turning into a blanket
  statement about the post-2022 or mobile-first platform.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/hosseinmardi_et_al_2021?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20hosseinmardi_et_al_2021&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/hosseinmardi_et_al_2021.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20recommendation-theme%20notes%20showing%20that%202016-2019%20real-user%20evidence%20concentrated%20far-right%20consumption%20in%20a%20small%20predisposed%20minority%20rather%20than%20a%20mass%20rabbit-hole%20dynamic.%0A%0A%23%23%20Pages%0A-%20wiki/sources/hosseinmardi_et_al_2021.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
- Verified the archived file is the PACM HCI / CSCW1 article with DOI
  `10.1145/3392854`, not the WWW 2020 citation given in the prompt.
- Confirmed the audit spans five misinformation topics and separates
  search results, Up-Next, and Top 5 recommendation outputs.
- Added one new cross-cutting claim on topic-specific misinformation
  exposure across different YouTube discovery surfaces.

Tier decision:

- Assigned `primary_empirical` because the archived article is a
  peer-reviewed audit paper with original experimental data and
  platform measurements.

Human attention requested:

- This source is especially useful for the atlas because it prevents
  search and recommendation exposure from being collapsed into one
  mechanism story.
- The paper is output-surface evidence rather than realized consumption
  evidence, so it should complement rather than substitute for real-user
  behavior studies.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/hussein_et_al_2020?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20hussein_et_al_2020&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/hussein_et_al_2020.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20recommendation-theme%20notes%20showing%20that%20search%2C%20Up%20Next%2C%20and%20Top%205%20recommendation%20surfaces%20produce%20topic-specific%20misinformation%20risks.%0A%0A%23%23%20Pages%0A-%20wiki/sources/hussein_et_al_2020.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest chae_lee_2024
**Operation:** ingest-source
**Branch:** ingest/chae_lee_2024
**By:** Codex (GPT-5)

Created `wiki/sources/chae_lee_2024.md` and updated the news theme,
registries, index, and log.

Cross-check notes:

- Verified the archived article is the *PLoS ONE* paper by Seung Woo
  Chae and Sung Hyun Lee; these author-name forms differ from the
  prompt and were taken from the article itself.
- Confirmed the study window is March 22-April 18, 2019 and that the
  analysis compares political-vlogger comment threads with mainstream-
  news comment threads about the Mueller report.
- Added one new cross-cutting claim on mainstream-news comment threads
  hosting more cross-cutting discussion than vlogger videos in this
  sample.

Tier decision:

- Assigned `primary_empirical` because this is a peer-reviewed journal
  article with original manual coding and NLP classification.

Human attention requested:

- This source is comment-layer evidence, not total-audience evidence.
- Its strongest value is clarifying that cross-cutting political
  discussion on YouTube depends on media type and is not automatically
  deliberative in quality.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/chae_lee_2024?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20chae_lee_2024&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/chae_lee_2024.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/news_ecosystem.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20news-theme%20notes%20showing%20that%20mainstream-news%20videos%20hosted%20more%20cross-cutting%20discussion%20than%20political-vlogger%20videos%20in%20the%202019%20Mueller-report%20window.%0A%0A%23%23%20Pages%0A-%20wiki/sources/chae_lee_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/news_ecosystem.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest kumar_2019
**Operation:** ingest-source
**Branch:** ingest/kumar_2019
**By:** Codex (GPT-5)

Created `wiki/sources/kumar_2019.md` and updated the creator-economy
and governance themes, registries, index, and log.

Cross-check notes:

- Verified the archived article is the peer-reviewed *Internet Policy
  Review* version with DOI `10.14763/2019.2.1417`.
- Confirmed the paper centers the March 2017 Adpocalypse aftermath,
  later YPP threshold changes, and creator testimony about
  demonetization and suppressed viewership.
- Added one new cross-cutting claim on monetization policy functioning
  as cultural gatekeeping.

Tier decision:

- Assigned `primary_empirical` rather than `policy_research` because
  the paper is a peer-reviewed journal article with original
  qualitative analysis, despite its essay-like framing.

Human attention requested:

- This is not a platform-wide effect-size estimate. Its value is
  conceptual and qualitative: it explains how governance can happen
  through monetization infrastructure.
- It should pair especially well with `abou_el_komboz_et_al_2023`,
  which estimates one slice of the same Adpocalypse-era shock
  causally.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/kumar_2019?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20kumar_2019&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/kumar_2019.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/creator_economy.md%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20theme%20notes%20showing%20that%20Adpocalypse-era%20monetization%20policy%20functioned%20as%20a%20form%20of%20platform%20gatekeeping%20over%20creator%20revenue%20and%20visibility.%0A%0A%23%23%20Pages%0A-%20wiki/sources/kumar_2019.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/creator_economy.md%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest van_es_2020
**Operation:** ingest-source
**Branch:** ingest/van_es_2020
**By:** Codex (GPT-5)

Created `wiki/sources/van_es_2020.md` and updated the descriptive-
deficit theme, registries, index, and log.

Cross-check notes:

- Verified the archived article is the 2020 *Television & New Media*
  paper with DOI `10.1177/1527476418818986`.
- Confirmed the paper is not a review; it presents an original
  platform analysis of how views and watch time structure YouTube's
  information regimes, monetization, and creator behavior.
- Added one new cross-cutting claim on the platform's view / watch-time
  regime shaping what becomes legible and measurable.

Tier decision:

- Assigned `primary_empirical` rather than `secondary_analytical`
  because the paper is an original peer-reviewed platform analysis,
  even though it is conceptually framed rather than built around a
  conventional sample dataset.

Human attention requested:

- This source is most useful as a diagnosis of metric inheritance in
  YouTube research.
- It is pre-Shorts, so its direct descriptive value for today's
  platform is historical and infrastructural rather than current-state
  measurement.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/van_es_2020?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20van_es_2020&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/van_es_2020.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/descriptive_deficit.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20descriptive-theme%20notes%20showing%20that%20YouTube%27s%20visible%20metrics%20already%20encode%20what%20becomes%20measurable%20and%20valuable%20on%20the%20platform.%0A%0A%23%23%20Pages%0A-%20wiki/sources/van_es_2020.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/descriptive_deficit.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest violot_et_al_2024
**Operation:** ingest-source
**Branch:** ingest/violot_et_al_2024
**By:** Codex (GPT-5)

Created `wiki/sources/violot_et_al_2024.md` and updated the
descriptive-deficit theme, registries, index, and log.

Cross-check notes:

- Verified the archived paper is the peer-reviewed WEBSCI '24 version
  with DOI `10.1145/3614419.3644023`.
- Confirmed the main sample covers 70,712 channels, 9,883,770 Shorts,
  and 6,862,321 regular videos from January 2021 through December
  2022.
- Added one new cross-cutting claim on Shorts reshaping both supply and
  engagement patterns, making regular-video-only description
  increasingly incomplete.
## 2026-04-16 — Ingest lee_et_al_2022
**Operation:** ingest-source
**Branch:** ingest/lee_et_al_2022
**By:** Codex (GPT-5)

Created `wiki/sources/lee_et_al_2022.md` and updated the
recommendation and news themes, registries, index, and log.

Cross-check notes:

- Verified the archived paper is the ICWSM 2022 conference paper on
  cross-platform attention dynamics across YouTube and Twitter.
- Confirmed the data window is January 1, 2017 through April 30, 2018
  and that the sample includes 179 abortion videos, 268 gun-control
  videos, and 777 BLM videos.
- Added one new cross-cutting claim on ideological attention advantage
  differing between YouTube engagement and Twitter diffusion.

Tier decision:

- Assigned `primary_empirical` because this is a peer-reviewed
  conference paper with original large-scale data collection and
  conference paper with original cross-platform data collection and
  analysis.

Human attention requested:

- The public API's lack of a native Shorts label is itself a
  methodological finding and should matter for later methods writing.
- The sample is restricted to channels that posted at least one Short,
  so it is best read as a strong Shorts-era baseline rather than as a
  random full-platform census.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/violot_et_al_2024?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20violot_et_al_2024&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/violot_et_al_2024.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/descriptive_deficit.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20descriptive-theme%20notes%20showing%20that%20Shorts%20changed%20both%20upload%20behavior%20and%20engagement%20baselines%2C%20while%20remaining%20poorly%20exposed%20in%20the%20public%20API.%0A%0A%23%23%20Pages%0A-%20wiki/sources/violot_et_al_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/descriptive_deficit.md%0A-%20wiki/index.md%0A-%20ops/log.md
- The source belongs more naturally to cross-platform attention and the
  news ecosystem than to direct recommender evaluation.
- Its value for the recommendation theme is cautionary: ideological
  visibility differences should not be collapsed into a simple claim
  about the recommender itself.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/lee_et_al_2022?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20lee_et_al_2022&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/lee_et_al_2022.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/recommendation_radicalization.md%60%2C%20%60wiki/themes/news_ecosystem.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20theme%20notes%20showing%20that%20ideological%20advantage%20differs%20between%20YouTube%20engagement%20and%20Twitter%20diffusion%20in%20pre-2019%20cross-platform%20attention%20data.%0A%0A%23%23%20Pages%0A-%20wiki/sources/lee_et_al_2022.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/themes/news_ecosystem.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Refresh recommendation_radicalization
**Operation:** refresh-theme
**Branch:** refresh/recommendation_radicalization
**By:** Codex (GPT-5)

Refreshed `wiki/themes/recommendation_radicalization.md` plus the
three linked debate pages `wiki/debates/rabbit_hole_debate.md`,
`wiki/debates/filter_bubble_evidence.md`, and
`wiki/debates/pre_2019_vs_post_2019_algorithm.md`.

Branch self-containment:

- Carried `lewis_2018`, `hosseinmardi_et_al_2021`,
  `hussein_et_al_2020`, and `lee_et_al_2022` plus their source-
  registry, claim-registry, and index infrastructure on-branch so the
  refresh remains internally verifiable before those ingest branches
  merge.

Refresh notes:

- The hub page now treats the corpus as a layered exposure literature:
  guest-network pathways, search outputs, recommendation outputs,
  real-user behavior, comment interaction, and cross-platform
  attention.
- `rabbit_hole_debate` now integrates Lewis as pre-2019 ecosystem
  formation evidence and Hosseinmardi 2021 as late-2010s real-user
  behavioral evidence against a mass rabbit-hole claim.
- `filter_bubble_evidence` now includes Hussein on search and
  recommendation surface differences plus Lee on cross-platform
  ideological attention asymmetry.
- `pre_2019_vs_post_2019_algorithm` now treats the transition period as
  a mixed multi-interface regime rather than as a simple before/after
  recommendation story.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...refresh/recommendation_radicalization?quick_pull=1&title=%5Brefresh-theme%5D%20Refresh%20recommendation_radicalization&body=%23%23%20Summary%0A-%20Refreshed%20%60wiki/themes/recommendation_radicalization.md%60%20plus%20%60wiki/debates/rabbit_hole_debate.md%60%2C%20%60wiki/debates/filter_bubble_evidence.md%60%2C%20and%20%60wiki/debates/pre_2019_vs_post_2019_algorithm.md%60.%0A-%20Included%20%60lewis_2018%60%2C%20%60hosseinmardi_et_al_2021%60%2C%20%60hussein_et_al_2020%60%2C%20and%20%60lee_et_al_2022%60%20plus%20the%20needed%20source-registry%2C%20claim-registry%2C%20and%20index%20infrastructure%20on-branch%20so%20the%20refresh%20remains%20self-contained%20before%20those%20ingest%20branches%20merge.%0A-%20Reframed%20the%20recommendation%20corpus%20around%20pre-2019%20ecosystem%20formation%2C%20search%20and%20recommendation%20interface%20differences%2C%20late-2010s%20real-user%20behavior%2C%20and%20thinner%20post-2021%20intervention%20evidence.%0A%0A%23%23%20Sources%0A-%20lewis_2018%0A-%20hosseinmardi_et_al_2021%0A-%20hussein_et_al_2020%0A-%20lee_et_al_2022%0A%0A%23%23%20Pages%0A-%20wiki/themes/recommendation_radicalization.md%0A-%20wiki/debates/rabbit_hole_debate.md%0A-%20wiki/debates/filter_bubble_evidence.md%0A-%20wiki/debates/pre_2019_vs_post_2019_algorithm.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/sources/lewis_2018.md%0A-%20wiki/sources/hosseinmardi_et_al_2021.md%0A-%20wiki/sources/hussein_et_al_2020.md%0A-%20wiki/sources/lee_et_al_2022.md%0A-%20wiki/index.md%0A-%20ops/log.md

## 2026-04-16 — Ingest padilla_2026
**Operation:** ingest-source
**Branch:** ingest/padilla_2026
**By:** Codex (GPT-5)

Created `wiki/sources/padilla_2026.md` and updated the
descriptive-deficit theme, the channel-classification methods page,
registries, index, and log.

Cross-check notes:

- Verified the archived paper is Adrián Padilla's 2026 *First Monday*
  article "Networks beyond the links: Methodological challenges in
  mapping YouTube communities" with DOI `10.5210/fm.v31i1.14633`.
- Confirmed the mixed-methods design uses Search API retrieval,
  keyword-matching cleanup, and crawls of the `subscriptions:list` and
  `channelSections:list` endpoints.
- Confirmed the GNU/Linux case yields 300,649 retrieved videos,
  153,795 keyword-matching videos, 62,092 channels, and 24,773
  channels with at least one public relational trace.
- Added one new cross-cutting claim on partial relational data forcing
  channel/community mapping to combine sparse formal ties with
  qualitative boundary interpretation.

Tier decision:

- Assigned `primary_empirical` because this is a peer-reviewed *First
  Monday* article with original large-scale data collection and
  methodological analysis, not a pure methods essay or policy note.

Human attention requested:

- The paper is methodologically central for `channel_classification`,
  but the registry schema has no dedicated field for method-page
  primacy; the methods relevance is captured through touched pages and
  cross-references rather than a new taxonomy term.
- The source broadens the methods evidence base beyond political
  YouTube, which is useful, but its GNU/Linux case still depends on
  keyword-led discovery and should not be mistaken for a neutral
  platform census.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/padilla_2026?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20padilla_2026&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/padilla_2026.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/descriptive_deficit.md%60%2C%20%60wiki/methods/channel_classification.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20descriptive-theme%20and%20channel-classification%20notes%20on%20hidden%20relational%20data%2C%20search%20API%20limits%2C%20and%20community-boundary%20filtering.%0A%0A%23%23%20Pages%0A-%20wiki/sources/padilla_2026.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/descriptive_deficit.md%0A-%20wiki/methods/channel_classification.md%0A-%20wiki/index.md%0A-%20ops/log.md

## 2026-04-16 — Ingest ofcom_2025
**Operation:** ingest-source
**Branch:** ingest/ofcom_2025
**By:** Codex (GPT-5)

Created `wiki/sources/ofcom_2025.md` and updated the
descriptive-deficit and governance-data-access themes, registries,
index, and log.

Cross-check notes:

- Verified the archived report is Ofcom's *Online Nation Report 2025*,
  published December 10, 2025.
- Focused extraction on YouTube-specific usage, time-spent, child-use,
  and platform-comparison sections rather than summarizing the whole
  115-page report.
- Confirmed the adult YouTube baseline is 94% reach and 51 minutes per
  day in May 2025, and the child baseline is 96% reach among 8-14s
  with 48 minutes of daily use.
- Did not find a dedicated Shorts breakout in the YouTube sections;
  logged that absence explicitly in the source card limitations.

Tier decision:

- Assigned `industry_report` because this is a research-adjacent
  regulatory monitoring report useful for descriptive baselines, not a
  peer-reviewed study and not evidence for causal or mechanism claims.

Human attention requested:

- The governance relevance here is indirect: Ofcom provides independent
  measurement baselines, but the report does not create a researcher-
  access mechanism or open platform internals.
- The YouTube metrics exclude some viewing environments, especially TV
  set use in adult summaries, so the reported totals are substantial
  but not all-screen totals.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/ofcom_2025?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20ofcom_2025&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/ofcom_2025.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/descriptive_deficit.md%60%2C%20%60wiki/themes/governance_data_access.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20provisional%20theme%20notes%20using%20Ofcom%27s%20UK-only%20audience%20baselines%20to%20underscore%20YouTube%27s%20scale%20while%20keeping%20the%20non-peer-reviewed%20evidence%20tier%20explicit.%0A%0A%23%23%20Pages%0A-%20wiki/sources/ofcom_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/descriptive_deficit.md%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest pew_2025
**Operation:** ingest-source
**Branch:** ingest/pew_2025
**By:** Codex (GPT-5)

Created `wiki/sources/pew_2025.md` and updated the
descriptive-deficit theme, registries, index, and log.
- Verified the archived report is Pew Research Center's *Americans'
  Social Media Use 2025* by Jeffrey Gottfried and Eugenie Park.
- Focused extraction on YouTube's U.S. adoption share, age and
  demographic patterns, and the separate daily-use estimates rather
  than summarizing the full methodology appendix.
- Confirmed the report uses two 2025 surveys: the 5,022-adult NPORS
  adoption survey and the 5,123-adult ATP daily-use survey.
- Used the report as a U.S.-specific scale baseline only and kept the
  non-peer-reviewed evidence tier explicit in the theme update.
- Assigned `industry_report` because this is a descriptive research
  report from Pew Research Center, useful for current platform-use
  baselines but not for causal or mechanism claims.

Human attention requested:

- Pew explicitly warns that the 2023 mode shift complicates comparisons
  with earlier phone-only waves, so any trend language beyond the
  report's own wording should stay cautious.
- Daily-use figures come from a different survey than the adoption
  figures, so branch reviewers should keep those two measurement frames
  conceptually separate.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/pew_2025?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20pew_2025&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/pew_2025.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/descriptive_deficit.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20a%20provisional%20descriptive-theme%20note%20using%20Pew%27s%20U.S.-specific%20adoption%20and%20daily-use%20baselines%20while%20keeping%20the%20non-peer-reviewed%20evidence%20tier%20explicit.%0A%0A%23%23%20Pages%0A-%20wiki/sources/pew_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/descriptive_deficit.md%0A-%20wiki/index.md%0A-%20ops/log.md
## 2026-04-16 — Ingest youtube_2024
**Operation:** ingest-source
**Branch:** ingest/youtube_2024
**By:** Codex (GPT-5)

Created `wiki/sources/youtube_2024.md` and updated the descriptive and
creator-economy themes, registries, index, and log.
- Verified that the archived PDF is YouTube's own impact report, not an
  independent academic or industry study, and that the report itself
  says its evidence comes from a mix of Oxford Economics research and
  YouTube internal data.
- Confirmed the report's main platform-asserted figures: more than $55B
  U.S. GDP contribution and 490,000 U.S. FTE jobs in 2024, more than
  $100B paid globally from January 2021 through December 2024, a claim
  of more than half of ad and subscription revenue shared with
  creators, and a ten-route monetization menu.
- Confirmed the report's scale framing claims: 2 billion viewers
  worldwide, more than 20 million uploads per day, and more than 20
  billion videos on YouTube.

Tier and citation decisions:

- Assigned `platform_documentation` because this is YouTube's own
  self-published impact report. The source is usable for platform-
  asserted facts and self-description, not for independent empirical or
  evaluative claims.
- Kept the stable atlas identifier `youtube_2024`, while noting that
  the PDF metadata is timestamped October 2025 even though the report is
  branded as a 2024 impact report.

Human attention requested:

- Reviewers should decide how much weight to give Oxford
  Economics-produced figures once they are embedded inside a YouTube-
  framed impact report; I treated the whole document conservatively as
  `platform_documentation`.
- The source is useful for stage-setting and platform self-description,
  but it should not be allowed to harden into independent evidence about
  creator livelihoods or national economic impact without outside
  corroboration.

Prefilled compare URL:

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/youtube_2024?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20youtube_2024&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/youtube_2024.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/descriptive_deficit.md%60%2C%20%60wiki/themes/creator_economy.md%60%2C%20%60wiki/index.md%60%2C%20and%20%60ops/log.md%60.%0A-%20Added%20explicitly%20attributed%20platform-self-report%20notes%20on%20YouTube%27s%20claimed%20scale%2C%20revenue-sharing%20design%2C%20and%20multi-route%20creator%20monetization%20stack.%0A%0A%23%23%20Pages%0A-%20wiki/sources/youtube_2024.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/descriptive_deficit.md%0A-%20wiki/themes/creator_economy.md%0A-%20wiki/index.md%0A-%20ops/log.md
