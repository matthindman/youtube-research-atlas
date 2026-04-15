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
