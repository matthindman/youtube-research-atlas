# YouTube Channel Census: Project Memo (v4)

**From:** IDDP Research Team
**Date:** March 2026
**Re:** Data architecture, denominator estimation, and study designs for full-platform YouTube measurement

---

## 1. Project Purpose and Scholarly Framing

This project is a full-platform measurement program for YouTube, not only a census of large channels. Its design has three linked inferential components:

1. **Validated near-exhaustive discovery** above explicit subscriber thresholds, supported by saturation curves, declining discovery rates, and search/trending audits.
2. **Formal estimation of the residual unseen tail**, using binwise missing-mass estimators for channel counts and curvature-corrected rank-size models for public activity.
3. **Probability-proportional-to-size (PPS) sampling** below the full-collection threshold, producing design-based estimates for the lower-subscriber universe.

The scholarly motivation is direct. The literature reviewed in our companion report identifies the descriptive deficit as the foundational obstacle to YouTube scholarship. McGrady et al. (2023, p. 4) articulate the problem precisely: "Among these fundamental unknowns are the number of videos YouTube hosts, how many views those videos typically receive, how much the site has grown over time, and how frequently various languages are represented in videos. Missing data like this creates 'denominator problems' and 'distribution problems' which limit the kinds of claims we can make." Munger (2024, p. 24) argues that "qualitative description must be complemented by rigorous quantitative description" and that "we are still allocating insufficient efforts" to this task. Norton and Shapiro (2024) document that YouTube receives approximately 0.1 published papers per 100 million active users, compared to 22.4 for Twitter -- a 200-fold disparity in scholarly attention per user.

This project's central claim is that the platform-wide denominator for public YouTube activity is not intractable. It cannot be known by naive enumeration alone, but it can be bounded and estimated by combining threshold-specific completeness diagnostics, missing-mass estimators for channel counts, curvature-corrected tail estimation for public activity, and weighted sampling below the take-all threshold. That claim directly addresses one of the major deficiencies identified in the literature.

The project's inferential language should remain disciplined. Every public claim should distinguish among three kinds of statements:

- **Near-exact claims** about observed channels above validated thresholds.
- **Design-based estimates** for lower-subscriber channels collected through weighted sampling.
- **Bounded estimates** for residual unseen mass, expressed as intervals under explicit modeling assumptions.

### Paper Sequence

**Companion methods output:** *Estimating the YouTube Denominator: Exhaustive Discovery, Missing Mass, Curvature-Corrected Tail Extrapolation, and Weighted Below-Threshold Sampling.*

**Paper 1:** *Mapping the YouTube Attention Economy: Concentration, Coverage, Institutional Form, and Public Affairs from a Near-Exhaustive Channel Census.*

**Paper 2:** *Contestability, Precarity, and Threshold Crossing in the YouTube Channel Hierarchy.*

The companion methods output should not be treated as an appendix or afterthought. It is one of the few parts of this project that is genuinely field-moving on method, not only on scale. The literature review makes clear that a major obstacle in YouTube research is not only lack of theory but lack of shared infrastructure and denominator clarity. This project is unusually well positioned to change that.

---

## 2. Three Denominator Problems

The v3 memo treated the denominator as a single problem: what fraction of total platform views does the 10k+ universe capture? The revised design separates three distinct inferential targets, each requiring its own method.

### 2.1 Channel-Count Coverage

How many channels remain undiscovered in a given subscriber bin? This is a discovery-rate problem. Within narrow subscriber bins, the project estimates remaining unseen channels using:

- **Saturation curves:** cumulative distinct channels discovered over crawl iterations, plotted by source type. Diminishing marginal returns signal approaching exhaustion.
- **Discovery-rate decline:** the share of newly encountered channels per crawl wave that were not in any prior wave.
- **Missing-mass estimators:** Good-Turing or related estimators applied to the frequency distribution of discovery-source multiplicity within subscriber bins.
- **Trending and search audits:** recurring probes of YouTube's trending feeds (all regions, all categories) and targeted `search.list` calls across subcategories, keywords, and regions. These serve as independent audits of whether the registry is missing fast-rising or niche channels.

Claims should be threshold-specific: effectively complete above 1M subscribers, above 100k, above 10k, and eventually above 1k, each supported by its own diagnostics. Completeness should also be reported by language, region, and public-affairs relevance, since those are precisely the domains where blind spots are most consequential.

### 2.2 Activity Coverage

How much public activity -- especially views -- lies below the observation boundary? This is a rank-size estimation problem, distinct from channel counting. Even if many small channels remain unseen, their collective share of public activity may be modest because the view distribution is extremely heavy-tailed.

The right framework is curvature-corrected tail estimation. Rather than fitting a naive power law to the entire tail, the project models the local Pareto exponent and allows the log-log rank-size curve to steepen. The degree-0 case (constant exponent) is the familiar Pareto benchmark and should be treated as the loosest extrapolation. Higher-degree cases incorporate observed curvature and yield tighter, lower tail estimates when -- as is typical -- the tail continues to steepen below the observation boundary.

The estimator should be run at several trusted censoring boundaries. The preferred boundary should be one where:
- The observed data are reliable (sufficient channels, stable daily views).
- The local Pareto exponent is comfortably above 1 (finite expected total).
- The curvature parameters are relatively stable across nearby boundaries.

The project should report: a lower bound given by observed activity alone; a preferred estimate with stated tail specification; and a sensitivity envelope across admissible boundaries and tail models. External platform totals from earnings calls or public statements become secondary plausibility checks, not the primary denominator.

### 2.3 Composition Below the Threshold

What kinds of channels occupy the observed, sampled, and unseen portions of the system? This requires the below-threshold sample described in Section 4.

---

## 3. Core Data Assets: Five Layers

### Layer 0 -- Discovery and Coverage Registry

A permanent registry of channel discovery. Every channel carries:

| Field | Description |
|-------|-------------|
| `channel_id` | YouTube channel ID |
| `first_seen` | Date first encountered by any source |
| `last_seen` | Most recent observation |
| `discovery_source` | Primary source (core feed, API crawl, trending, search audit, cross-reference) |
| `source_multiplicity` | Number of distinct discovery sources |
| `trending_hits` | Count of appearances in trending feeds, by region and category |
| `search_audit_hits` | Count of appearances in search-audit probes |
| `threshold_status` | Current subscriber tier (1k, 10k, 100k, 1M) |
| `threshold_crossing_dates` | Timestamps for each threshold crossing |
| `sample_stratum` | Below-threshold sampling stratum assignment |
| `inclusion_probability` | Sampling weight for below-threshold channels |

This layer is not a minor operational convenience. It is the empirical basis for claiming that the crawl is approaching exhaustion above specified thresholds.

### Layer 1 -- Core Audience Panel (non-API, permanent)

The primary data backbone: `channel_id`, `date`, total views, and exact subscriber counts if available.

**Critical note on subscriber counts:** YouTube's public Data API rounds `subscriberCount` to three significant figures. Do not build flagship analyses on public API subscriber counts if exact counts exist in the core feed. If exact subscribers are unavailable, treat public counts as coarse bins and document this limitation.

### Layer 2 -- Public API Enrichment (rolling cache)

Channel metadata, upload-frontier discovery, and selective video metadata from the YouTube Data API v3. Used for taxonomy inputs, format detection, and video-level enrichment -- not as the long-run historical backbone.

**API data retention compliance:** The YouTube API Developer Policies require that non-authorized statistics data not be stored for more than 30 days without refresh. Treat the raw API layer as a rolling operational cache. Refresh public metadata inside the 30-day window. Keep the non-API core panel (Layer 1) as the permanent historical backbone. Conduct a formal compliance review before operationalizing any long-term API data warehouse.

### Layer 3 -- Human-Labeled Taxonomy and Channel Dossiers

Versioned label table for topic, public-affairs relevance, ownership, editorial mode, language, and format profile. Includes adjudication logs, coder-pair agreement records, taxonomy version metadata, and multilingual evaluation.

### Layer 4 -- Estimation and Paper-Ready Tables

Saturation curves, missing-mass outputs, tail-estimation outputs, sampling weights, spike flags, rank tables, concentration summaries, and gold analytic tables.

### Namespace Layout

```
yt_raw.core.channel_views_daily          # Layer 1: non-API panel (permanent)
yt_raw.api.channel_json_raw              # Layer 2: API responses (rolling 30-day cache)
yt_raw.api.playlistitems_json_raw
yt_raw.api.videos_json_raw

yt_silver.dim_channel                    # Typed, deduplicated channel dimension
yt_silver.fact_channel_views_daily       # Daily views derived from Layer 1
yt_silver.fact_upload_frontier           # New uploads per channel per day
yt_silver.dim_video_selected             # Video-level metadata for hydrated videos
yt_silver.channel_dossier                # Composite per-channel text for taxonomy

yt_ml.channel_labels                     # Taxonomy labels (versioned)
yt_ml.channel_label_review               # Adjudication + audit trail
yt_ml.channel_embedding_index            # Vector embeddings for neighbor review

yt_gold.paper1_attention                 # Paper 1 analytic tables
yt_gold.paper2_mobility                  # Paper 2 analytic tables
yt_gold.denominator_estimates            # Tail estimation, coverage, missing mass

yt_ops.channel_registry                  # Layer 0: discovery registry
yt_ops.discovery_log                     # Per-source discovery events
yt_ops.api_run_log                       # Per-run collection metadata
yt_ops.quota_usage                       # Daily quota consumption tracking
yt_ops.data_quality                      # Expectation failures, anomaly flags
```

---

## 4. Coverage, Denominator, and Below-Threshold Sampling

### 4.1 Coverage and Completeness Diagnostics

For each major subscriber threshold -- 1k, 10k, 100k, 1M -- the project reports:

- Saturation curves (cumulative distinct channels over crawl iterations).
- Declining discovery rates (share of new channels per wave).
- Estimated remaining mass within narrow subscriber bins (missing-mass estimators).
- Miss rates from trending and search audits.

These diagnostics must be stratified. A single global saturation curve is insufficient. Report separately by language, region, topical area, and public-affairs relevance. Trending channels in every region and category serve as recurring audits of whether the registry is missing fast-rising channels.

`search.list` should be framed carefully in the memo and in publications. It is not the primary discovery backbone (it costs 100 quota units per call and cannot be sustained at scale). It is a targeted audit and supplementary discovery instrument used to probe for systematic blind spots.

### 4.2 Channel-Count Estimation

Within narrow subscriber bins, estimate remaining unseen channels using discovery-rate decline and missing-mass estimators. The objective is not a single coarse total. It is a set of thresholded and binwise completeness statements that accumulate into a credible platform-wide count estimate.

This is important because channel count and activity are not the same thing. There may be many undiscovered small channels while the share of unseen public activity is negligible.

### 4.3 Activity-Tail Estimation

Model the local Pareto exponent of the rank-size distribution and allow curvature. The degree-0 (constant exponent) case is the loosest extrapolation. Curvature-corrected cases yield tighter estimates under the empirically typical pattern where the tail steepens. Report:

- Lower bound: observed activity only.
- Preferred estimate: curvature-corrected tail at the best-performing censoring boundary.
- Sensitivity envelope: across admissible boundaries and tail specifications.

External platform totals from earnings calls become plausibility checks, not the primary denominator.

### 4.4 Below-Threshold PPS-Style Sample

Below the take-all threshold, use a formal weighted sample. The design:

**Certainty strata** (inclusion probability = 1):
- Channels repeatedly appearing in trending feeds.
- Channels classified as public-affairs relevant.
- Channels with unusually high activity relative to subscribers.
- Channels recently crossing into the observation window from below.

**PPS strata** (inclusion probability proportional to predicted activity):

Inclusion probabilities are set as pi_i proportional to m-hat_i, where m-hat_i is the predicted mean weekly views given subscribers, language, topic proxies, channel age, recent growth, upload frequency, region, discovery source, and trending hits. The subscriber-to-activity relationship should be estimated flexibly, with interactions and nonlinearity, rather than imposed as a single global law.

Estimation uses Horvitz-Thompson or Hajek weighting, calibrated within subscriber-language-topic bins and adjusted for estimated frame missingness in those bins.

**Why this design is statistically superior:** In a highly skewed rank-size system, simple random samples spend too much sample budget on extremely low-mass channels and do a poor job recovering aggregate public activity. Taking the head with certainty and sampling the remainder PPS-style makes the residual problem far better behaved and produces stable design-based estimators with much better precision. The companion methods paper should include an empirical or simulation appendix comparing SRS with the hybrid design.

### 4.5 Internal Validation and Backtesting

The project can validate its own estimators using ranges that are already observed. This is the strongest possible response to reviewer skepticism about tail estimation.

Required backtests:

| Backtest | Observed | Target |
|----------|----------|--------|
| 100k counterfactual | Channels > 100k only | Recover known 10k-100k mass |
| 1M counterfactual | Channels > 1M only | Recover known 100k-1M mass |
| Temporal holdout | Earlier crawl state | Recover channels discovered in later crawl waves |
| Activity holdback | Views of top decile only | Recover known aggregate of deciles 2-10 |

These backtests should appear in the companion methods output and be summarized in each flagship paper.

---

## 5. Taxonomy Pipeline

The taxonomy remains the single most important methodological investment and the critical path for both flagship papers.

### 5.1 Taxonomy Axes

The v3 memo collapsed ownership and editorial form into a single "institutional form" variable. This should be split. A channel can be creator-owned but podcast-style, or legacy-affiliated but personality-led. The literature repeatedly emphasizes that such hybridity matters (Newman et al. 2025: "in practice the dividing lines are extremely fuzzy. Many creators defy categorisation," p. 10).

**Axis 1 -- Topic/genre** (primary + secondary):
```
music | gaming | entertainment | kids_family | news_public_affairs |
education_howto | sports | lifestyle | technology | business_finance |
religion | health | comedy | commentary_opinion | autos_vehicles |
travel | diy | podcasts_talk | other
```

**Axis 2 -- Ownership/affiliation:**
```
independent_creator | legacy_media | local_news | national_broadcaster |
music_label_artist | brand_corporate | government_public_agency |
nonprofit_advocacy | state_affiliated_media | multichannel_network |
educational_institution | religious_institution | political_party |
aggregator_compilation | other
```

**Axis 3 -- Editorial/presentation mode:**
```
personality_led | institutional_voice | ensemble_hosted |
automated_compilation | user_generated_compilation | other
```

This separation allows the project to distinguish, for example, a legacy-media channel with personality-led presentation from an independent creator using institutional voice -- a distinction that connects directly to the Reuters Institute findings about creator-driven displacement of institutional journalism.

**Axis 4 -- Language/geography:**
Primary language (from API `defaultAudioLanguage` + LLM inference on title/description for missing values) + coarse regional marker.

**Axis 5 -- Format profile:**
```
mainly_longform | shorts_heavy | live_podcast_heavy |
clip_archive_heavy | mixed
```
Deterministic from video durations once frontier data accumulates.

**Axis 6 -- Public-affairs relevance** (binary gate + second-stage labels):

All channels receive a binary flag: `public_affairs_relevant` (yes/no). Channels flagged yes receive richer second-stage labels:

```
institutional_journalism | creator_commentary | talk_interview_podcast |
advocacy_movement_media | alternative_partisan_media |
state_affiliated_public_service | satire_comedy | explanatory_educational |
other_public_affairs
```

This second stage is essential for engaging with the news-ecosystem questions foregrounded in the literature review. Newman et al. (2025) find that political commentary dominates YouTube's news creator space and is overwhelmingly male (85% of top individuals across 24 countries). Reveilhac (2024) argues that "the line between traditional news channels and alternative news channels is blurring." Munger (2024) frames the institutional-form distinction as the key to moving beyond a genre map. Without the public-affairs second stage, the project cannot speak to these questions.

### 5.2 Channel Dossier

One composite text block per channel, assembled from:

- Channel title, handle, and description (from `channels.list`)
- `topicDetails.topicCategories` (Freebase/Wikipedia topic IDs)
- `brandingSettings` keywords
- Titles and descriptions of 5-10 most recent uploads (from `playlistItems.list`)
- Extracted external domains from description text (monetization and affiliation signals)
- Simple format signals (median video duration, Shorts fraction)
- Channel age and growth trajectory summary

Stored in `yt_silver.channel_dossier`.

### 5.3 The Hybrid Classification Pipeline

The approach from v3 remains correct: rules engine, human-coded seed set, bulk machine scoring, LLM adjudication, embedding-based neighbor review, and evaluation. Key refinements:

**Step 1 -- Rules engine (high precision, low cost).** Pattern-match obvious cases: VEVO channels, official government agencies, recognizable broadcaster handles, children's brands, major sports leagues, major record labels. Cheap and near-perfect.

**Step 2 -- Human-coded seed set (10,000 channels, two rounds).** Stratified by language, public-affairs relevance, and size tier -- including the below-threshold sample.

- **Round 1 (5,000 channels):** Roughly half probability-proportional-to-views from the take-all head, half stratified by suspected topic/language bins including below-threshold sampled channels.
- **Round 2 (5,000 channels):** Active-learning selection using uncertainty x attention weighting, plus uncertainty x public-affairs weighting.
- **Dual-code** the top 1,500-2,000 channels (by attention share) plus the most ambiguous cases. Adjudicate disagreements. Freeze taxonomy v1.
- **Keep primary human coders blind to model suggestions.** Model output for adjudication and active-learning selection only.

**Step 3 -- Bulk machine scoring.** Train on the 10,000 human-labeled dossiers. Options: fine-tuned encoder model, Databricks `ai_classify()` with few-shot examples, or gradient-boosted classifier on embeddings. Outputs confidence scores per axis.

**Step 4 -- LLM adjudication for hard cases.** For channels where the bulk scorer's confidence is below threshold: `ai_query()` with structured output against Llama 3.3 70B or equivalent. Use `ai_extract()` where extraction is more natural than classification (e.g., country of origin, stated institutional affiliation).

**Step 5 -- Embedding-based neighbor review.** Mosaic AI Vector Search over channel dossiers. Reviewers inspect nearest neighbors for uncertain channels and propagate labels within clusters.

**Step 6 -- Evaluation and release.** Score on three metrics:
- **Channel-weighted** macro/micro F1 (standard).
- **Attention-weighted** F1 (weight each channel by its share of total views).
- **Design-weighted** F1 (appropriate weights for the below-threshold sampled portion).

Target: >= 85% attention-weighted accuracy on ownership/affiliation; >= 80% on topic; >= 80% on public-affairs relevance.

### 5.4 Taxonomy Maintenance

- Incremental: new channels crossing thresholds get dossiers built weekly, rules applied, bulk scorer applied, flagged for human review if uncertain + high-attention.
- Quarterly: re-run bulk scorer with any updated seed labels; version the taxonomy.

---

## 6. Databricks Architecture

Standard medallion lakehouse design. The implementation choices from v3 remain sound:

- **UC managed Delta tables** for all bronze/silver/gold/ML tables.
- **UC volumes** for raw JSON payloads, logs, prompts, wheel files, and operational artifacts.
- **Workspace files / Git folders** for notebooks, SQL, and source-controlled code.
- **Lakeflow Declarative Pipelines** to ingest raw JSON from volumes into bronze/silver with expectations and schema evolution.
- **Lakeflow Jobs** to fan out collection tasks by shard.
- **Asset Bundles** for CI/CD.
- **Service principal + Databricks secrets** for API key management.
- **Serverless compute** by default if outbound network policy allows Google API calls; otherwise standard-access job cluster.
- **DBR 15.4 LTS or later** for `ai_classify()`, `ai_extract()`, and other AI Functions.
- **MLflow 3** for taxonomy experiments, prompt versions, model versions, and evaluation runs.

**Note on Analytics/Reporting APIs:** These are owner/content-owner authorization systems, not general solutions for third-party data. All third-party data comes through the Data API v3.

### Data Quality Expectations

- One row per `channel_id`-`date` in core panel.
- Non-negative daily views (negative diffs flagged as anomalies).
- Valid YouTube IDs (regex check).
- No duplicate `channel_id`-`video_id` in upload frontier.
- Monotonic `seen_at` for repeated frontier sightings.
- No null `uploads_playlist_id` for active channels.

---

## 7. YouTube API Collection Design

### Endpoints (production)

```
GET /youtube/v3/channels
  ?part=snippet,statistics,contentDetails,topicDetails,brandingSettings,status
  &id=<up to 50 comma-delimited IDs>
  Quota: 1 unit per call. Batch of 50.

GET /youtube/v3/playlistItems
  ?part=snippet,contentDetails
  &playlistId=<uploads playlist ID>
  &maxResults=50
  Quota: 1 unit per page.

GET /youtube/v3/videos
  ?part=snippet,statistics,contentDetails,status,liveStreamingDetails,topicDetails
  &id=<up to 50 comma-delimited IDs>
  Quota: 1 unit per call. Batch of 50.
```

`search.list` (100 units/call) is excluded from routine production but used for periodic audit probes.

### Collector Architecture

Shard-based Python wheel job.

- **Channel registry** (`yt_ops.channel_registry`): `channel_id`, threshold status, shard assignment, discovery metadata, last channel refresh, last uploads scan, last video hydration.
- **Three Lakeflow Jobs** fanning out across shard tasks:
  - Weekly channel refresh (all channels in take-all universe + sampled below-threshold channels)
  - Daily uploads frontier scan
  - Daily selected-video hydration
- Each job writes NDJSON payloads to UC volumes, appends run metadata to `yt_ops.api_run_log`.
- Lakeflow Declarative Pipeline ingests JSON into bronze, promotes to silver with typed normalization, deduplication, and expectations.

### Quota Budget (10M units/day)

| Job | Frequency | Coverage | Est. cost/day | % of quota |
|-----|-----------|----------|--------------|------------|
| Channel refresh | Weekly (amortized) | All take-all + sampled channels | ~12,000 | 0.1% |
| Uploads frontier | Daily | TBD by pilot | TBD | TBD |
| Video hydration | Daily | TBD by pilot | TBD | TBD |
| Search audits | Weekly (amortized) | Targeted probes | ~5,000 | 0.05% |
| **Reserve** | | | **~8M+** | **80%+** |

### The Two-Week Pilot (Decision Point 1)

**Do not fix the video-hydration threshold until you have empirical data.** Before committing:

1. Run the uploads-frontier scan (`playlistItems.list`) for all channels >= 10k subscribers for two weeks.
2. Measure: daily new-video count by channel tier, overflow-page frequency, total quota consumed.
3. Set the long-run video-hydration threshold using a **view-coverage rule**: hydrate all new videos for channels that together account for 85-90% of total views (from the core panel), plus any channel flagged by spike detector.

Expected outcome: hydrating new videos for channels covering 85% of views requires only a fraction of available quota. But let the data decide.

**Shorts caveat:** YouTube changed Shorts view counting on March 31, 2025 so that a view counts when a Short starts to play or replay, with no minimum watch time. Do not compare Shorts and long-form raw view counts as identical attention units. Restrict any cross-format analysis to the post-change period and document this limitation.

---

## 8. Flagship Paper 1: *Mapping the YouTube Attention Economy*

### 8.1 Questions

Paper 1 should now ask five linked questions rather than describing only the 10k+ universe:

1. How concentrated is public activity within the observed and effectively complete portions of YouTube?
2. What share of channels and activity lie above subscriber thresholds of 1k, 10k, 100k, and 1M?
3. How does composition -- by topic, public-affairs relevance, ownership, editorial mode, and language -- change as the threshold drops?
4. What does the combined census-plus-sample-plus-tail design imply about total platform-wide public activity?
5. How different is public-affairs YouTube from the rest of the platform?

That is a stronger paper than a large-channel map alone. It answers the literature's descriptive deficit more directly.

### 8.2 Design

Cross-sectional descriptive analysis with stability checks across weeks. Observation window: 8-12 weeks of daily data. Three clearly distinguished result types:

- **Observed exact or near-exact results** for the take-all head.
- **Design-based estimates** for the sampled below-threshold range.
- **Bounded platform-wide totals** after incorporating the residual tail.

### 8.3 Outcome Measures

| Measure | Level |
|---------|-------|
| Gini coefficient | Platform-wide (estimated); by category; by language |
| Top-k attention share | Top 0.1%, 1%, 5%, 10% of channels |
| HHI | By content domain; by ownership type |
| Rank-size exponent + curvature | Full observed distribution |
| Threshold-capture curves | Channels and views above 1k, 10k, 100k, 1M |
| Category attention share | Each topic's % of total views |
| Ownership attention share | Each ownership form's % of total views |
| Public-affairs ecology | Share of activity, internal split by sub-type, by language |
| Within-category Gini | Concentration inside each topic domain |
| Coverage ratio | Observed views / tail-estimated platform total |
| Format split | Shorts vs. long-form share by category |

A major section should show how much substantive conclusions change -- or do not change -- as one moves from the largest channels to the broader platform. That is one of the most important descriptive questions in the field, and this design is uniquely suited to answer it.

### 8.4 The Public-Affairs Module

This section should be prominent, not buried. It reports:

- The share of total platform activity going to public-affairs channels.
- The internal split among institutional journalism, creator commentary, talk/podcast, advocacy, alternative/partisan media, state-affiliated, satire, and explanatory content.
- How that ecology varies across major language or market groupings.
- The gender composition of the most-viewed public-affairs channels.

This is where the project engages most directly with the literature on news creators (Newman et al. 2025), political information (Munger 2024; Munger & Phillips 2022), and the displacement of institutional journalism (Reuters DNR 2025).

### 8.5 Data Requirements

| Input | Source | API needed? |
|-------|--------|------------|
| 8-12 weeks of daily channel views | Layer 1 (core panel) | No |
| Channel taxonomy v1 | Layers 2 + 3 (dossiers + human labels + scorer) | Yes (one-time channel + playlistItems pulls) |
| Below-threshold sample views | Layer 1 (sampled channels) | No |
| Denominator estimates | Layer 4 (tail estimation, coverage diagnostics) | No |

### 8.6 Analysis Pipeline

```
01_weekly_aggregation.sql
  - Aggregate fact_channel_views_daily to channel-week
  - Compute mean daily views per channel over 8-12 week window
  - Join to dim_channel, channel_labels, channel_registry

02_concentration.py
  - Gini, top-k shares, rank-size distribution (full observed range)
  - Curvature-corrected tail estimation for platform-wide Gini
  - HHI by topic domain and ownership type
  - Within-category Gini for each domain
  - Robustness: weekly vs. daily aggregation, alternate taxonomy versions

03_threshold_capture.py
  - Channels and views above each threshold (1k, 10k, 100k, 1M)
  - Tail-estimated residual below lowest observed threshold
  - Sensitivity to tail specification

04_composition.py
  - Topic x ownership attention shares (cross-tabulation matrix)
  - Creator-native vs. legacy vs. state-affiliated vs. brand shares
  - Language-level decomposition
  - How composition shifts across subscriber thresholds

05_public_affairs.py
  - Binary public-affairs share of total activity
  - Second-stage type decomposition within public affairs
  - Cross-language comparison of public-affairs ecology
  - Gender composition of top public-affairs channels

06_below_threshold.py
  - PPS-weighted estimates for below-threshold composition
  - Horvitz-Thompson totals and SEs
  - Comparison of below-threshold composition to above-threshold

07_validation.py
  - LLM/scorer taxonomy vs. human gold standard
  - Cohen's kappa, channel-weighted, attention-weighted, design-weighted accuracy
  - Confusion matrices by axis
  - Denominator backtests (100k counterfactual, 1M counterfactual, temporal holdout)
  - Full documentation of dossier construction, labeling procedure, scorer, and estimators
```

### 8.7 What Matters Most Methodologically

- **Denominator estimation** is what elevates this from a large-channel description to a platform-wide measurement. It should be presented clearly and tested rigorously.
- **Taxonomy accuracy on the top attention share.** The attention-weighted validation is non-negotiable.
- **The public-affairs module** is what connects the paper to the journalism, political communication, and platform-governance literatures.
- **Threshold-capture curves** are the empirical backbone: showing how much of YouTube's total activity each subscriber threshold captures.
- **A transparent methods section** documenting the dossier, labeling procedure, scorer, tail estimator, sampling design, and backtests.

### 8.8 Timeline

| Week | Milestone |
|------|-----------|
| 1-3 | Discovery registry buildout, completeness dashboards, threshold selection, denominator backtesting design, taxonomy codebook revision |
| 3-6 | Search/trending audits, Round 1 labeling (5,000 channels), below-threshold sample design, initial completeness estimates |
| 6-9 | Round 2 labeling (5,000 channels), taxonomy v1, binwise missing-mass estimates, first tail-estimation sensitivity runs, sample-weight calibration |
| 9-12 | Paper 1 concentration, composition, threshold-coverage, and public-affairs analyses |
| 12-14 | Validation appendix, robustness checks, writing |
| 14-16 | Circulating draft; target submission by week 18 |

### 8.9 Target Outlets

- *Science* or *Nature* short report if the coverage-ratio or concentration finding is striking.
- *PNAS* for the full version.
- *Journal of Quantitative Description: Digital Media* as a strong disciplinary alternative.

---

## 9. Flagship Paper 2: *Contestability, Precarity, and Threshold Crossing in the YouTube Channel Hierarchy*

### 9.1 Questions

The revised design allows Paper 2 to study not only reshuffling within the observed hierarchy but also entry from below:

1. How persistent are top ranks?
2. How often do upper-tier positions get captured by new entrants from below the take-all threshold?
3. How long do channels remain above key thresholds once they enter?
4. Which spikes translate into durable baseline shifts?
5. Do mobility, threshold crossing, and hazard differ by topic, ownership, public-affairs status, language, and format?
6. Has the subscriber become decoupled from viewership?

### 9.2 Design

Longitudinal panel analysis. Minimum viable: 6-month panel. Full version: 12 months.

### 9.3 Outcome Measures

| Measure | Definition |
|---------|-----------|
| Rank persistence | Pr(top-k at t+tau given top-k at t) for k in {100, 1K, 10K}, tau in {1, 4, 13, 26, 52 weeks} |
| Transition matrix | Markov probabilities across view-decile bins |
| Channel volatility (sigma) | Std dev of log(weekly views), rolling 13-week windows |
| Size-volatility relationship | log(sigma) regressed on log(mean views) |
| View-to-subscriber ratio | weekly_views / subscriber_count |
| Spike detection | Channel-weeks where views > 3x trailing 8-week median |
| Post-spike baseline shift | Mean views in weeks [+5,+12] minus mean in weeks [-12,-5] relative to spike |
| **Spell duration** | Time spent continuously in top-k tiers, by entry cohort |
| **Hazard of exit** | Pr(dropping below threshold in next period, given time already above) |
| **Threshold crossing rate** | Rate of channels crossing 1k, 10k, 100k, 1M from below |
| **Entrant share** | Fraction of top-k slots held by channels that were below threshold at baseline |
| Survival / attrition | Kaplan-Meier for time to "channel death" (4 consecutive weeks < 20% of initial baseline) |
| **Attrition decomposition** | Separate dormancy (no uploads), active decline (uploading but losing views), and disappearance/removal |

### 9.4 Data Requirements

| Input | Source |
|-------|--------|
| 26-52 weeks of daily channel views | Layer 1 (core panel) |
| Exact subscriber counts (if available) | Layer 1; otherwise API with rounding caveat |
| Channel taxonomy v1 | From Paper 1 |
| New upload metadata for spike attribution | Layer 2 (upload frontier + selective video hydration) |
| Below-threshold sampled channels | Layer 0 + Layer 1 |
| Channel availability/removal status | Layer 0 (discovery registry) |

### 9.5 Supply-Side Layer

For enriched channels, spikes should be linked to changes in upload behavior, format, topic mix, and external monetization or network signals. The governance layer is critical: collapses caused by dormancy, removal, demonetization shocks, or broader policy changes are not the same phenomenon and should not be treated as interchangeable.

### 9.6 Format-Separated Analysis

Shorts-heavy and long-form-heavy channels should not be treated as if raw view counts were identical attention units, especially after the March 2025 view-counting change. All analyses should be run separately by format regime and the sensitivity documented.

### 9.7 Analysis Pipeline

```
01_rank_panel.sql
  - Weekly ranks (overall and within-category) from fact_channel_views_daily
  - Join taxonomy, subscriber counts, discovery registry

02_rank_persistence.py
  - Top-k overlap at increasing lags
  - Markov transition matrix across decile bins
  - Rank autocorrelation functions

03_threshold_crossing.py
  - Channels crossing 1k, 10k, 100k, 1M from below
  - Entrant share of top-k slots over time
  - Spell duration in each tier
  - Hazard of exit, stratified by size, category, ownership, format

04_volatility.py
  - Per-channel sigma of log(weekly views) over rolling 13-week windows
  - Size-volatility regression (binned and parametric)
  - Compare across categories, ownership types, format regimes

05_subscriber_decoupling.py
  - View-to-subscriber ratio distribution and trend
  - Panel regression: does subscriber count predict floor of weekly views?
  - Segment by ownership type

06_spike_analysis.py
  - Detect spikes (3x trailing median)
  - For hydrated channels: link spikes to specific uploads via temporal match
  - Classify spike-triggering videos by format and topic
  - Estimate post-spike baseline shift by channel type and spike type

07_survival.py
  - Define attrition: 4 consecutive weeks < 20% of initial mean weekly views
  - Decompose into dormancy, active decline, disappearance/removal
  - Kaplan-Meier stratified by size tier, category, ownership type
  - Cox proportional hazards: initial size, volatility, category, upload frequency, format

08_rank_diffusion.py  [stretch / potential standalone]
  - Stochastic portfolio theory model on weekly view shares
  - Drift, volatility, mean reversion parameters
```

### 9.8 Timeline

| Period | Milestone |
|--------|-----------|
| From day 1 | Compute weekly ranks and spike flags in parallel with Paper 1 taxonomy work |
| Months 2-3 | Define collapse, recovery, threshold-crossing, and spell rules |
| Month 4 | Preliminary volatility, rank-persistence, and threshold-crossing estimates |
| Month 6 | First working paper (6-month panel) |
| Months 6-12 | Extend with spike interpretation, survival analysis, governance-aware decomposition |
| Month 12 | Full version with 12-month panel |

### 9.9 Target Outlets

- *PNAS*
- Top field journal: *Management Science*, *Journal of Communication*, *Political Communication*
- The rank-diffusion model could be a standalone methods paper.

---

## 10. Companion Methods Output

**Title:** *Estimating the YouTube Denominator: Exhaustive Discovery, Missing Mass, Curvature-Corrected Tail Extrapolation, and Weighted Below-Threshold Sampling*

This should document:

1. The discovery architecture and threshold-specific completeness diagnostics.
2. Binwise missing-mass estimators for channel counts.
3. The curvature-corrected activity-tail estimator, with sensitivity analysis.
4. The PPS-style below-threshold sampling design.
5. Internal backtests on known ranges.
6. Taxonomy validation at channel-weighted, attention-weighted, and design-weighted levels.
7. Reproducibility materials (code, estimator specifications, diagnostic outputs) to the extent permitted by API policy.

This output creates a reusable measurement framework. The literature review makes clear that a major obstacle is not only lack of theory but lack of shared denominator infrastructure. This project is unusually well positioned to provide it.

---

## 11. Studies 3-10 (Brief Designs)

Each uses shared infrastructure. Listed with minimum data accumulation needed.

| # | Title | Design | Min. data | Key addition |
|---|-------|--------|-----------|-------------|
| 3 | What kind of media system? | Cross-section + 12-month trend | 4 wks / 12 mo | Map Reuters 24-country news-creator taxonomy onto channel census |
| 4 | Event-driven attention reallocation | Prospective DiD | Baseline + event | Title keywords identify event-relevant uploads within 48 hrs |
| 5 | How many YouTubes? | Cross-language comparison | 4-8 wks | Concentration/composition by top 10 languages |
| 6 | Subscriber loyalty | Panel analysis | 6 mo | View-to-subscriber dynamics by ownership type |
| 7 | Platform substitutability | Natural experiment | Baseline + shock | Contingent on TikTok disruption or similar |
| 8 | Deplatforming spillovers | Prospective event study | Baseline + event | Correlation-based cluster neighbors of terminated channel |
| 9 | Coordinated inauthentic networks | Anomaly detection | 3 mo | Synchronized growth, templated metadata |
| 10 | Shorts vs. long-form | Within-channel panel | 6 mo | Post-March 2025 view-counting only |

These should now be tied explicitly to the new inferential architecture. The project is no longer only describing the large-channel head. It is designing a platform-wide measurement system that supports each of these downstream studies with shared denominator, taxonomy, and sampling infrastructure.

---

## 12. Immediate Decisions

Four decisions gate everything downstream:

**A. Build the discovery-and-coverage registry.** Start threshold-specific completeness dashboards immediately. This is the empirical basis for all denominator claims.

**B. Freeze the denominator strategy.** Three-part system: binwise count estimation, activity-tail estimation, and PPS-style below-threshold sampling. Design the internal backtests now.

**C. Freeze the revised taxonomy design.** Six axes including the public-affairs second stage and the ownership/editorial-mode split. Approve the labeling budget for 10,000 human labels across two rounds with dual-coding on the high-impact slice and stratification by language and size tier.

**D. Launch the two-week uploads-frontier pilot.** This still governs the supply-side layer and the later mobility paper.

Remaining decisions (important but not blocking):

1. Confirm whether exact subscriber counts exist in the core feed.
2. Approve Databricks architecture.
3. Approve collector design.
4. Conduct API data retention compliance review.

---

## 13. Risk Register

| Risk | Mitigation |
|------|-----------|
| Overclaiming completeness | Every public claim threshold-specific and backed by diagnostics. Never say "the whole platform." |
| Sensitivity to tail-model choice | Report pure Pareto as loose benchmark, curvature-corrected alternatives, varied censoring boundaries, and backtests on known ranges |
| Frame missingness below take-all threshold | Combine PPS sample with binwise missing-mass adjustment and repeated trending/search audit |
| Misspecification of subscriber-to-activity model for PPS | Estimate flexibly with richer observables; validate on channels that later cross into fully observed universe |
| Cross-language or public-affairs blind spots | Stratified completeness diagnostics, multilingual annotation, explicit public-affairs oversampling in certainty strata |
| Shorts format instability | Format-separated analysis; careful language about what view counts represent; sensitivity tests excluding Shorts |
| Platform-policy and governance shocks | Store channel availability states and policy-change calendar prospectively; decompose attrition by cause |
| YouTube reduces API quota | Maintain compliance standing; keep production well under allocation; document research purpose |
| YouTube changes view-count reporting | Version all derived metrics; preserve raw cumulative snapshots in Layer 1 |
| API data retention policy violation | Treat API layer as 30-day rolling cache; Layer 1 as permanent backbone; formal compliance review |
| Taxonomy LLM/scorer degrades | Pin model versions; maintain human gold standard; re-validate quarterly |
| Human coders influenced by model suggestions | Blind first-pass coders to model output; use model only for adjudication/active-learning selection |

---

## 14. Bottom Line

The original v3 memo had the right backbone: taxonomy first, cross-sectional description first, mobility second. Its weakness was framing: it described the project too narrowly as a 10k+ channel census with some auxiliary denominator work around the edges.

The stronger and more accurate framing is that this is a **hybrid census-estimation-sampling design for measuring YouTube at platform scale.** It combines validated near-exhaustive crawling to explicit thresholds, formal estimation of the unseen channel and activity tail, and probability-proportional-to-size sampling below the take-all threshold.

Once the memo foregrounds completeness diagnostics, count-side and activity-side denominator estimation, and the below-threshold PPS sample, the project becomes substantially more ambitious and substantially more important. It is no longer only a very large descriptive panel. It becomes one of the first credible attempts to estimate the public platform as a whole -- while still preserving the taxonomy, public-affairs, multilingual, and mobility questions that the literature most urgently needs answered.
