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

- https://github.com/matthindman/youtube-research-atlas/compare/main...ingest/hallinan_et_al_2025?quick_pull=1&title=%5Bingest-source%5D%20Ingest%20hallinan_et_al_2025&body=%23%23%20Summary%0A-%20Created%20%60wiki/sources/hallinan_et_al_2025.md%60.%0A-%20Updated%20%60data/source-registry.yaml%60%2C%20%60data/claim-registry.yaml%60%2C%20%60wiki/themes/governance_data_access.md%60%20and%20%60wiki/index.md%60.%0A-%20Added%20a%20provisional%20governance-theme%20update%20using%20%60norton_shapiro_2024%60%20plus%20the%20new%20Hallinan%20source%20card.%0A%0A%23%23%20Pages%0A-%20wiki/sources/hallinan_et_al_2025.md%0A-%20data/source-registry.yaml%0A-%20data/claim-registry.yaml%0A-%20wiki/themes/governance_data_access.md%0A-%20wiki/index.md%0A-%20ops/log.md

## 2026-04-16 — Ingest reynolds_hallinan_2024
**Operation:** ingest-source
**Branch:** ingest/reynolds_hallinan_2024
**By:** Codex (GPT-5)

Ingested `reynolds_hallinan_2024` via the `ingest-source` workflow.
Created `wiki/sources/reynolds_hallinan_2024.md` and updated
`data/source-registry.yaml`, `data/claim-registry.yaml`,
`wiki/themes/governance_data_access.md`, and `wiki/index.md`.

Literature-review cross-check note:

- This paper is not summarized directly in the internal literature
  review, so the source card was rebuilt from the original article
  rather than from review scaffolding.

Tier and taxonomy decisions:

- Assigned `primary_empirical`.
- Reused the existing theme tag `governance-data-access`; no taxonomy
  additions proposed.
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
