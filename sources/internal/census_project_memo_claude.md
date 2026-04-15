# YouTube Channel Census: Project Memo (v3)

**From:** IDDP Research Team
**Date:** March 2026
**Re:** Data architecture, infrastructure, and study designs for the first two flagship papers

---

## 1. Paper Sequence

**Paper 1: *Mapping the 10k+ YouTube Attention Economy***
How concentrated is attention? What kinds of channels capture it? How does concentration vary across topic, institutional form, and language? This paper is mostly cross-sectional and can be drafted from 8-12 weeks of data.

**Paper 2: *Contestability and Precarity in the YouTube Channel Hierarchy***
How stable is the ranking? How often do mid-tier channels collapse or recover? Which spikes convert into durable audience growth? This paper requires 6 months minimum; 12 months for the full version.

This sequence matches the data's actual strengths: a near-census panel is immediately powerful for concentration and composition, and becomes powerful for mobility and hazard only after months of accumulation.

---

## 2. Core Data Assets: Four Layers

### Layer 1 — Core Audience Census (non-API)

The primary data backbone. This is the non-API source of truth: `channel_id`, `date`, total views, and exact subscriber counts if available in this feed.

**Critical note on subscriber counts:** YouTube's public Data API rounds `subscriberCount` to three significant figures (e.g., a channel with 123,456 subscribers returns 123,000). Do not build flagship analyses on public API subscriber counts if exact counts exist in the core feed. If exact subscribers are unavailable, treat public counts as coarse bins only and document this limitation.

### Layer 2 — Public API Enrichment

Channel metadata, upload-frontier discovery, and selective video metadata from the YouTube Data API v3. Used for taxonomy inputs, format detection, and video-level enrichment — not as the long-run historical backbone.

**API data retention compliance:** The YouTube API Developer Policies require that non-authorized statistics data not be stored for more than 30 days without refresh. This means:
- Treat the raw API layer as a **rolling operational cache**, not a permanent archive.
- Refresh public metadata inside the 30-day window.
- Keep the **non-API core panel (Layer 1)** as the permanent historical backbone.
- Use the API layer to create current dossiers, current taxonomies, and prospective video enrichments.
- Conduct a formal compliance review before operationalizing any long-term API data warehouse.

### Layer 3 — Human-Labeled Taxonomy Data

Versioned label table for topic, institutional form, language, and confidence. Includes adjudication logs, coder-pair agreement records, and taxonomy version metadata.

### Layer 4 — Derived and Paper-Specific Tables

Event calendars, spike flags, rank tables, concentration summaries, and paper-ready gold tables.

---

## 3. Databricks Architecture

Standard medallion lakehouse design. Implementation choices:

- **UC managed Delta tables** for all bronze/silver/gold/ML tables.
- **UC volumes** for raw JSON payloads, logs, prompts, wheel files, and operational artifacts.
- **Workspace files / Git folders** for notebooks, SQL, and source-controlled code.
- **Lakeflow Declarative Pipelines** to ingest raw JSON from volumes into bronze/silver with expectations and schema evolution.
- **Lakeflow Jobs** to fan out collection tasks by shard.
- **Asset Bundles** for CI/CD.
- **Service principal + Databricks secrets** for API key management and automated authentication. Do not store API keys in notebooks or environment variables.
- **Serverless compute** by default, but only if outbound network policy allows Google API calls. Databricks exposes serverless egress control and network policies for outbound connections. If serverless egress is blocked, run collectors on a standard-access job cluster.
- **DBR 15.4 LTS or later** required for `ai_classify()`, `ai_extract()`, and other AI Functions used in the taxonomy pipeline.

**Note on Analytics/Reporting APIs:** The YouTube Analytics and Reporting APIs are owner/content-owner authorization systems, not general solutions for third-party channel data. They cannot be used to pull analytics for channels you do not own. All third-party data comes through the Data API v3.

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

yt_ops.channel_registry                  # Master roster + collection state
yt_ops.api_run_log                       # Per-run collection metadata
yt_ops.quota_usage                       # Daily quota consumption tracking
yt_ops.data_quality                      # Expectation failures, anomaly flags
```

### Data Quality Expectations (Lakeflow Pipelines)

- One row per `channel_id`-`date` in core panel
- Non-negative daily views (negative diffs flagged as anomalies)
- Valid YouTube IDs (regex check)
- No duplicate `channel_id`-`video_id` in upload frontier
- Monotonic `seen_at` for repeated frontier sightings
- No null `uploads_playlist_id` for active channels

Lakeflow expectations emit data-quality metrics to the pipeline event log. Use Databricks system tables (`system.billing.usage`, `system.lakeflow.pipelines`) to monitor pipeline health and cost. The billable usage table can isolate AI Functions batch inference costs from collection compute costs.

---

## 4. YouTube API Collection Design

### Endpoints (production only — no `search.list`)

```
GET /youtube/v3/channels
  ?part=snippet,statistics,contentDetails,topicDetails,brandingSettings,status
  &id=<up to 50 comma-delimited IDs>
  Quota: 1 unit per call. Batch of 50.
  Returns: uploads playlist ID, subscriber count (rounded), description, etc.

GET /youtube/v3/playlistItems
  ?part=snippet,contentDetails
  &playlistId=<uploads playlist ID>
  &maxResults=50
  Quota: 1 unit per page.
  Returns: new video IDs, titles, descriptions, publish dates.

GET /youtube/v3/videos
  ?part=snippet,statistics,contentDetails,status,liveStreamingDetails,topicDetails
  &id=<up to 50 comma-delimited IDs>
  Quota: 1 unit per call. Batch of 50.
  Returns: duration, tags, view/like/comment counts, live status, category.
```

**Why this design:**
- `channels.list` provides the `uploads` playlist ID, which is the stable handle for discovering new uploads. Refreshed weekly.
- `playlistItems.list` on the uploads playlist is the cheapest way to discover new videos. It also returns titles and descriptions — enough for most taxonomy work without needing `videos.list`.
- `videos.list` is reserved for selected new videos when duration, tags, statistics, and live-streaming details are needed. It is the enrichment step, not the discovery step.
- `search.list` costs 100 units per call and is unnecessary when the channel universe is already known. Excluded from production.

### Collector Architecture

Shard-based Python wheel job, not ad hoc notebooks.

- **Channel registry** (`yt_ops.channel_registry`): `channel_id`, threshold status, shard assignment (`hash(channel_id) % 256`), last channel refresh, last uploads scan, last video hydration.
- **Three Lakeflow Jobs**, each fanning out across shard tasks:
  - Weekly channel refresh (all channels)
  - Daily uploads frontier scan
  - Daily selected-video hydration
- Each job writes NDJSON payloads to UC volumes, appends run metadata to `yt_ops.api_run_log`.
- Lakeflow Declarative Pipeline ingests JSON into bronze tables, promotes to silver with typed normalization, deduplication, and expectations.

### Quota Budget (10M units/day)

| Job | Frequency | Coverage | Est. cost/day | % of quota |
|-----|-----------|----------|--------------|------------|
| Channel refresh | Weekly (amortized) | All 4.1M channels | ~12,000 | 0.1% |
| Uploads frontier | Daily | TBD by pilot | TBD | TBD |
| Video hydration | Daily | TBD by pilot | TBD | TBD |
| **Reserve** | | | **~8M+** | **80%+** |

### The Two-Week Pilot (Decision Point 1)

**Do not fix the video-hydration threshold until you have empirical data.** Before committing to a subscriber or view-coverage threshold for Tier 2/3 collection:

1. Run the uploads-frontier scan (`playlistItems.list`) for all channels with ≥10k subscribers for two weeks.
2. Measure: daily new-video count by channel tier, overflow-page frequency (channels uploading >50 videos/day), total quota consumed.
3. Set the long-run video-hydration threshold using a **view-coverage rule**: hydrate all new videos for channels that together account for 85-90% of total views (from the core panel), plus any channel flagged by spike detector. This aligns engineering cost with research value.

Expected outcome: the pilot will likely show that hydrating new videos for channels covering 85% of views requires only a fraction of available quota, confirming feasibility. But let the data decide.

---

## 5. Taxonomy Pipeline (Critical Path for Both Papers)

The taxonomy is the single most important methodological investment. The correct approach is **not** "run a zero-shot prompt over 4 million channels and trust it." Recent work on LLM annotation shows that unsupervised zero-shot classification with large label spaces performs poorly, and that model suggestions can shift human annotator distributions if coders see them during first-pass labeling.

### 5.1 Taxonomy Axes

**Axis 1 — Topic/genre** (primary + secondary):
```
music | gaming | entertainment | kids_family | news_public_affairs |
education_howto | sports | lifestyle | technology | business_finance |
religion | health | comedy | commentary_opinion | autos_vehicles |
travel | diy | podcasts_talk | other
```

**Axis 2 — Institutional form** (mutually exclusive):
```
independent_creator | legacy_media | local_news | national_broadcaster |
music_label_artist | brand_corporate | government_public_agency |
nonprofit_advocacy | state_affiliated_media | multichannel_network |
educational_institution | religious_institution | political_party |
aggregator_compilation | other
```

**Axis 3 — Language/geography:**
Primary language (from API `defaultAudioLanguage` + LLM inference on title/description for missing values) + coarse regional marker.

**Axis 4 — Format profile** (optional in Paper 1, heavier use later):
```
mainly_longform | shorts_heavy | live_podcast_heavy |
clip_archive_heavy | mixed
```
Deterministic from Tier 2 video durations once frontier data accumulates.

### 5.2 Channel Dossier

One composite text block per channel, assembled from:
- Channel title, handle, and description (from `channels.list`)
- `topicDetails.topicCategories` (Freebase/Wikipedia topic IDs)
- `brandingSettings` keywords
- Titles and descriptions of 5-10 most recent uploads (from `playlistItems.list`)
- Optional: public link/domain cues from description text

Stored in `yt_silver.channel_dossier`. This is the input to all classification steps.

### 5.3 The Hybrid Classification Pipeline

**Step 1 — Rules engine (high precision, low cost).**
Pattern-match obvious cases: VEVO channels, official government agencies, recognizable broadcaster handles, children's brands (Cocomelon, etc.), major sports leagues, major record labels. These are cheap and near-perfect.

**Step 2 — Human-coded seed set (10,000 channels, two rounds).**
- **Round 1 (5,000 channels):** Sampled to over-represent high-attention channels. Roughly half probability-proportional-to-views, half stratified by suspected topic/language bins.
- **Round 2 (5,000 channels):** Selected after the first model pass using an uncertainty × attention weighting rule (prioritize channels where the model is least confident AND that command substantial views).
- **Dual-code** the top 1,500-2,000 channels (by attention share) plus the most ambiguous cases. Adjudicate disagreements. Freeze taxonomy version 1.
- **Keep primary human coders blind to model suggestions.** Use model output for adjudication and active-learning selection only, not as a visible hint during first-pass coding.

**Step 3 — Bulk machine scoring (full universe).**
Train a supervised classifier on the 10,000 human-labeled dossiers. Options:
- Fine-tuned encoder model (e.g., via Databricks Model Training API on a smaller LLM)
- Databricks `ai_classify()` with few-shot examples drawn from the seed set
- Gradient-boosted classifier on embeddings from Mosaic AI (fast, cheap, interpretable)

The bulk scorer runs over all ~4.1M channel dossiers. Outputs confidence scores per axis.

**Step 4 — LLM adjudication for hard cases.**
For channels where the bulk scorer's confidence is below threshold, use `ai_query()` with structured output against Llama 3.3 70B (or equivalent) with the full dossier as input. Use `ai_classify()` for high-level topic and institutional-form labeling; use `ai_extract()` where extraction is more natural than flat classification — e.g., extracting country of origin, stated institutional affiliation, or self-described mission from the description text. This is the expensive step but applies only to a fraction of channels.

Track all taxonomy experiments, prompt versions, model versions, and evaluation runs in **MLflow 3**, which provides experiment tracking, evaluation metrics, and human-feedback logging natively on Databricks.

**Step 5 — Embedding-based neighbor review.**
Use Mosaic AI Vector Search over channel dossiers. Reviewers can inspect nearest neighbors for uncertain channels and propagate labels within clusters. Vector Search syncs with Delta tables automatically. **Implementation note:** standard Vector Search endpoints require Change Data Feed (CDF) to be enabled on the source Delta table (`yt_silver.channel_dossier`); enable this before creating the index.

**Step 6 — Evaluation and release.**
Score the taxonomy on two metrics:
- **Channel-weighted** macro/micro F1 (standard)
- **Attention-weighted** F1 (weight each channel's classification by its share of total views)

The attention-weighted metric is essential: misclassifying a top-0.1% channel affects Paper 1's headline findings far more than misclassifying a random low-view channel. Target: ≥85% attention-weighted accuracy on institutional form; ≥80% on topic.

### 5.4 Taxonomy Maintenance

- Incremental: new channels crossing the 10k threshold get dossiers built weekly, rules applied, bulk scorer applied, flagged for human review if uncertain + high-attention.
- Quarterly: re-run bulk scorer with any updated seed labels; version the taxonomy.

---

## 6. Flagship Paper 1: *Mapping the 10k+ YouTube Attention Economy*

### 6.1 Questions

1. How concentrated are daily/weekly views across the 10k+ universe?
2. What share of attention goes to each topic, institutional form, and language?
3. How concentrated is attention *within* categories?
4. What share goes to creator-native actors vs. legacy institutions?
5. What fraction of total platform views does the 10k+ universe capture?

### 6.2 Design

Cross-sectional descriptive analysis with stability checks across weeks. Observation window: 8-12 weeks of daily data.

### 6.3 Outcome Measures

| Measure | Level |
|---------|-------|
| Gini coefficient | Platform-wide; by category; by language |
| Top-k attention share | Top 1%, 5%, 10% of channels |
| HHI | By content domain; by institutional type |
| Rank-size exponent | OLS on log(rank) ~ log(views) |
| Category attention share | Each topic's % of total views |
| Institutional attention share | Each institutional form's % of total views |
| Coverage ratio | Total 10k+ views / YouTube-reported platform total |
| Within-category Gini | Concentration inside each topic domain |

### 6.4 Data Requirements

| Input | Source | API needed? |
|-------|--------|------------|
| 8-12 weeks of daily channel views | Layer 1 (core panel) | No |
| Channel taxonomy v1 | Layers 2 + 3 (dossiers + human labels + scorer) | Yes (one-time channel + playlistItems pulls) |
| YouTube platform-wide totals | Earnings calls, public statements | No (desk research) |

No full-census video hydration required for Paper 1.

### 6.5 Analysis Pipeline

```
01_weekly_aggregation.sql
  - Aggregate fact_channel_views_daily to channel-week
  - Compute mean daily views per channel over 8-12 week window
  - Join to dim_channel for metadata, channel_labels for taxonomy

02_concentration.py
  - Gini, top-k shares, rank-size distribution (platform-wide)
  - HHI by topic domain and institutional type
  - Within-category Gini for each domain
  - Robustness: weekly vs. daily aggregation, alternate taxonomy versions

03_composition.py
  - Category attention shares (topic × institutional form matrix)
  - Creator-native vs. legacy vs. state-affiliated vs. brand shares
  - Language-level decomposition

04_top_of_ocean.py
  - Total daily views across 10k+ universe
  - Coverage at 50k, 100k, 500k, 1M subscriber thresholds
  - Compare to YouTube-reported totals

05_validation_appendix.py
  - LLM/scorer taxonomy vs. human gold standard
  - Cohen's kappa, channel-weighted and attention-weighted accuracy
  - Confusion matrices by axis
  - Full documentation of dossier construction, labeling procedure, and scorer
```

### 6.6 What Matters Most Methodologically

- **Taxonomy accuracy on the top attention share**, not just the average channel. The attention-weighted validation is non-negotiable for credibility.
- **Institutional-form coding** is what makes the paper more than a genre map. The creator-vs-institution question is what connects it to the Reuters Institute, Munger, and platform-governance literatures.
- **A clear appendix** documenting the channel dossier, labeling procedure, scorer architecture, and view-weighted validation. Reviewers at top journals will scrutinize this.

### 6.7 Timeline

| Week | Milestone |
|------|-----------|
| 1-3 | Stand up core ingestion, channel registry, channel dossiers |
| 3-6 | Round 1 labeling (5,000 channels); taxonomy codebook freeze |
| 6-8 | Round 2 labeling (5,000 channels); bulk classification; review queue; taxonomy v1 |
| 8-10 | Concentration and composition analysis |
| 10-12 | Validation appendix, robustness checks, writing |
| 12-14 | Circulating draft; target submission by week 16 |

### 6.8 Target Outlets

- *Science* or *Nature* short report if the coverage-ratio or concentration finding is striking
- *PNAS* for the full version
- *Journal of Quantitative Description: Digital Media* as a strong disciplinary alternative

---

## 7. Flagship Paper 2: *Contestability and Precarity in the YouTube Channel Hierarchy*

### 7.1 Questions

1. How persistent are top ranks?
2. How often do mid-tier channels suffer sustained collapses? How often do they recover?
3. Which spikes translate into higher post-spike baselines?
4. Do mobility and hazard differ by topic, institutional form, and language?
5. Has the subscriber become decoupled from viewership?

### 7.2 Design

Longitudinal panel analysis. Minimum viable: 6-month panel. Full version: 12 months.

### 7.3 Outcome Measures

| Measure | Definition |
|---------|-----------|
| Rank persistence | Pr(top-k at t+τ given top-k at t), for k ∈ {100, 1K, 10K} and τ ∈ {1, 4, 13, 26, 52 weeks} |
| Transition matrix | Markov probabilities across view-decile bins |
| Channel volatility (σ) | Std dev of log(weekly views), rolling 13-week windows |
| Size-volatility relationship | log(σ) regressed on log(mean views) |
| View-to-subscriber ratio | weekly_views / subscriber_count (use exact subs from Layer 1 if available; note rounding if using API) |
| Spike detection | Channel-weeks where views > 3× trailing 8-week median |
| Post-spike baseline shift | Mean views in weeks [+5,+12] minus mean in weeks [-12,-5] relative to spike |
| Survival / attrition | Kaplan-Meier for time to "channel death" (4 consecutive weeks < 20% of initial baseline) |

### 7.4 Data Requirements

| Input | Source |
|-------|--------|
| 26-52 weeks of daily channel views | Layer 1 (core panel) |
| Exact subscriber counts (if available) | Layer 1 (core panel); otherwise API with rounding caveat |
| Channel taxonomy v1 | From Paper 1 |
| New upload metadata for spike attribution | Layer 2 (upload frontier + selective video hydration) |

### 7.5 Selective Video Layer

**Do not decide the video-hydration threshold now.** Instead:
1. Run the two-week uploads-frontier pilot.
2. Measure actual daily new-video counts and page-overflow frequency.
3. Choose a **view-coverage threshold**: hydrate all new videos for channels that together account for 85-90% of total views (from the core panel), plus any channel flagged by the spike detector.

This aligns engineering cost with substantive focus. It also means the video-hydration scope is empirically determined, not assumed.

**Shorts caveat:** YouTube changed Shorts view counting on March 31, 2025 so that a view counts when a Short starts to play or replay, with no minimum watch time. Do not compare Shorts and long-form raw view counts as identical attention units. Restrict any cross-format analysis to the post-change period and document this limitation.

### 7.6 Analysis Pipeline

```
01_rank_panel.sql
  - Weekly ranks (overall and within-category) from fact_channel_views_daily
  - Join taxonomy, subscriber counts

02_rank_persistence.py
  - Top-k overlap at increasing lags
  - Markov transition matrix across decile bins
  - Rank autocorrelation functions

03_volatility.py
  - Per-channel σ of log(weekly views) over rolling 13-week windows
  - Size-volatility regression (binned and parametric)
  - Compare across categories and institutional types

04_subscriber_decoupling.py
  - View-to-subscriber ratio distribution and trend
  - Panel regression: does subscriber count predict floor of weekly views?
  - Segment by institutional type

05_spike_analysis.py
  - Detect spikes (3× trailing median)
  - For hydrated channels: link spikes to specific uploads via temporal match
  - Classify spike-triggering videos by format (Shorts vs. long-form) and topic
  - Estimate post-spike baseline shift by channel type and spike type

06_survival.py
  - Define attrition: 4 consecutive weeks < 20% of initial mean weekly views
  - Kaplan-Meier stratified by size tier, category, institutional type
  - Cox proportional hazards: initial size, volatility, category, upload frequency

07_rank_diffusion.py  [stretch / potential standalone paper]
  - Fit stochastic portfolio theory model to weekly view shares
  - Estimate drift, volatility, mean reversion parameters
  - Compare to Facebook engagement rank dynamics
```

### 7.7 Timeline

| Period | Milestone |
|--------|-----------|
| From day 1 | Compute weekly ranks and spike flags in parallel with Paper 1 taxonomy work |
| Months 2-3 | Define collapse, recovery, and spike persistence rules |
| Month 4 | Preliminary volatility and rank-persistence estimates |
| Month 6 | First mobility/precarity working paper (6-month panel) |
| Months 6-12 | Extend with selective video interpretation, event-study sections, survival analysis |
| Month 12 | Full version with 12-month panel |

### 7.8 Target Outlets

- *PNAS*
- Top field journal: *Management Science*, *Journal of Communication*, *Political Communication*
- The rank-diffusion model component could be a standalone methods paper

---

## 8. Studies 3-10 (Brief Designs)

Each uses shared infrastructure. Listed with minimum data accumulation needed.

| # | Title | Design | Min. data | Key addition |
|---|-------|--------|-----------|-------------|
| 3 | What kind of media system? | Cross-section + 12-month trend | 4 wks / 12 mo | Map Reuters 24-country news-creator taxonomy onto channel census |
| 4 | Event-driven attention reallocation | Prospective DiD | Baseline + event | Tier 2 title keywords identify event-relevant uploads within 48 hrs |
| 5 | How many YouTubes? | Cross-language comparison | 4-8 wks | Concentration/composition by top 10 languages |
| 6 | Subscriber loyalty | Panel analysis | 6 mo | View-to-subscriber dynamics by institutional type |
| 7 | Platform substitutability | Natural experiment | Baseline + shock | Contingent on TikTok disruption or similar |
| 8 | Deplatforming spillovers | Prospective event study | Baseline + event | Correlation-based cluster neighbors of terminated channel |
| 9 | Coordinated inauthentic networks | Anomaly detection | 3 mo | Synchronized growth, templated metadata |
| 10 | Shorts vs. long-form | Within-channel panel | 6 mo | Post-March 2025 view-counting only |

---

## 9. Immediate Decisions (This Week)

Two decisions gate almost everything downstream. Make them first.

**A. Freeze the taxonomy axes and approve the labeling budget.** Fund 10,000 human labels across two rounds with dual-coding on the high-impact slice. Keep first-pass coders blind to model suggestions. The taxonomy codebook must be started in week 1; every week of delay shifts Paper 1's timeline by a week.

**B. Launch the two-week uploads-frontier pilot.** Run `playlistItems.list` across the full 10k+ universe for two weeks. Let the empirical upload distribution determine the video-hydration threshold before committing to long-run Tier 2/3 scope.

The remaining decisions are important but not blocking:

1. **Confirm whether exact subscriber counts exist in the core feed.** If yes, use them for Paper 2. If no, treat public API counts as coarse bins and document this.

2. **Approve the Databricks architecture.** UC managed Delta tables, UC volumes, Lakeflow Jobs + Declarative Pipelines, Asset Bundles, service principal + secrets, serverless where permitted, DBR 15.4 LTS.

3. **Approve the collector design.** `channels.list` for registry refresh, `playlistItems.list` for daily frontier, `videos.list` only for selected new videos. No `search.list` in production.

4. **Conduct API data retention compliance review.** The 30-day rules for non-authorized API data need formal review before treating API snapshots as a permanent archive. Until cleared, treat the API layer as a rolling cache and rely on Layer 1 as the historical backbone.

---

## 10. Risk Register

| Risk | Mitigation |
|------|-----------|
| YouTube reduces API quota | Maintain compliance standing; keep production well under allocation; document research purpose for audit |
| YouTube changes view-count reporting | Monitor API revision history; version all derived metrics; preserve raw cumulative snapshots in Layer 1 |
| Shorts view-count methodology changes again | Track creator announcements; flag Shorts-heavy channels; sensitivity tests excluding Shorts |
| Subscriber count rounding distorts analysis | Use exact counts from core feed if available; if API-only, treat as bins and run robustness checks |
| Taxonomy LLM/scorer degrades | Pin model versions; maintain human gold standard; re-validate quarterly |
| API data retention policy violation | Treat API layer as 30-day rolling cache; keep Layer 1 as permanent backbone; formal compliance review |
| Channel universe exceeds collection capacity | Tier 1 scales linearly (~0.8% quota at 4M channels); Tier 2 threshold adjustable |
| Major event occurs before baseline established | Accept shorter baseline; still valuable vs. zero prior data |
| Human coders influenced by model suggestions | Blind first-pass coders to model output; use model only for adjudication/active-learning selection |
