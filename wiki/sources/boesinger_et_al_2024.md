---
source_id: boesinger_et_al_2024
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Tube2Vec: Social and Semantic Embeddings of YouTube Channels"
authors:
  - "Boesinger, Léopaul"
  - "Ribeiro, Manoel Horta"
  - "Veselovsky, Veniamin"
  - "West, Robert"
year: 2024
venue: "Proceedings of the Eighteenth International AAAI Conference on Web and Social Media"
doi: null
temporal_scope: "Reddit links from 2010-August 2022, plus channel metadata and history-less recommendations gathered during the study"
themes:
  - descriptive-deficit
project_modules:
  - discovery-completeness
  - classification-llm
  - public-affairs
census_papers:
  - methods-companion
  - study3-media-system
census_relevance: high
verification:
  machine_extracted: 18
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Boesinger et al. (2024) - Tube2Vec

## Full Citation

Boesinger, Léopaul, Manoel Horta Ribeiro, Veniamin Veselovsky,
and Robert West. 2024. "Tube2Vec: Social and Semantic Embeddings
of YouTube Channels." In *Proceedings of the Eighteenth
International AAAI Conference on Web and Social Media*, 2084-2090.

## One-Sentence Contribution

The paper introduces and releases three channel-embedding families
built from public traces - Reddit sharing, channel metadata, and
history-less recommendations - to scale semantic and social mapping
of YouTube channels without relying on low-recall manual channel
discovery (pp. 2084-2087). [🤖]

## Research Question

Can latent embeddings derived from public YouTube-related traces
recover channel semantics and social dimensions well enough to
support large-scale research without exhaustive manual channel
labeling or keyword-based discovery (pp. 2084-2087)? [🤖]

## Data, Sample, Geography, and Period

- **Data:** Reddit Pushshift posts and comments linking to YouTube,
  YouTube Data API channel and video metadata, video titles and
  descriptions, and recommendation lists collected from the
  InnerTube API (pp. 2084-2085). [🤖]
- **Sample:** The raw corpus contains 31.4M distinct videos from
  7.5M YouTube channels shared on Reddit; after filtering for large
  channels with 50 recent mostly English videos, the released
  embeddings cover 44,000 channels (pp. 2084-2085). [🤖]
- **Geography:** The final dataset is English-language and is biased
  toward channels shared on Reddit, so it is strongest for channels
  circulating in primarily English-speaking online environments
  rather than for YouTube globally (pp. 2084-2085, 2087). [🤖]
- **Period:** Reddit traces span January 2010 to August 2022, while
  recommendations were crawled repeatedly over four days during the
  study and do not model longer-run temporal change (pp. 2085, 2087).
  [🤖]

## Methods

Tube2Vec constructs three separate embeddings. The `t2v-soc`
embedding represents channels as weighted averages of the subreddit
embeddings where they are shared; `t2v-con` averages MiniLM vectors
from titles and descriptions of each channel's 50 most recent
videos; and `t2v-rec` uses `node2vec` over a channel graph built from
history-less recommendations between sampled recent videos (pp.
2085-2086). [🤖]

The paper evaluates these embeddings three ways: category prediction
for Music, Sports, and Gaming channels; an Amazon Mechanical Turk
"odd-channel-out" semantic-similarity task; and social-dimension
ranking against both existing partisan labels and new crowdsourced
partisan, age, and gender rankings (pp. 2085-2087). [🤖]

## Main Findings

1. Recommendation embeddings performed best on the paper's category-
   prediction benchmark, reaching F1 scores of 0.94 across Gaming,
   Music, and Sports, with content embeddings close behind and social-
   sharing embeddings weakest on that task (pp. 2085-2086). [🤖]
2. Recommendation and content embeddings both aligned well with human
   judgments of semantic similarity in the "odd-channel-out" task,
   while social-sharing embeddings lagged behind (p. 2086). [🤖]
3. Social-sharing embeddings correlated best with existing partisan
   labels, but recommendation embeddings performed best overall across
   the paper's crowdsourced partisan, gender, and age rankings (pp.
   2086-2087). [🤖]
4. The released embeddings provide reusable research infrastructure
   for 44,000 channels and show that large-scale channel mapping can
   be built from public relational and metadata traces rather than
   only from manual curation (pp. 2084, 2087). [🤖]

## Limitations / Scope Conditions

The social-sharing embeddings depend on Reddit, which means they only
cover channels shared on another platform whose users are primarily in
English-speaking countries (p. 2087). [🤖]

The released channel set is limited to channels with more than
100,000 subscribers and 50 recent mostly English videos, so the
infrastructure is not a platform-wide census and does not solve small-
channel or multilingual coverage directly (p. 2085). [🤖]

Recommendation embeddings capture what a history-less user would
receive from sampled recent videos over four days, not logged-in or
longitudinal recommendation behavior (pp. 2085, 2087). [🤖]

The content and recommendation social dimensions are partly derived
from regressors trained on social-sharing dimensions, and the paper
explicitly notes that time is not modeled in the released embeddings
(pp. 2086-2087). [🤖]

## Temporal Scope

This source is best read as early-2020s public-trace infrastructure.
Its main evidence pools together long-run Reddit sharing from 2010-2022
with recommendation captures gathered during the study, so it is useful
for reusable channel infrastructure but should not be treated as a
stable description of the current recommender or of post-2022 YouTube
more broadly (pp. 2084-2087). [🤖]

## Key Quotes

> "we let the data 'speak for itself,'" (p. 2084) [🤖]

> "recommendation embeddings excel at capturing both social dimensions
> and semantics" (p. 2084) [🤖]

## Relation to This Project

- **Methods companion:** Directly useful as a reusable precedent for
  embedding channels from public traces when full-platform crawling or
  manual labeling is infeasible. [PROJECT]
- **Paper 1 (attention economy):** Indirect relevance only; the paper
  helps with channel discovery and classification but not with
  platform-wide denominators or attention shares. [PROJECT]
- **Paper 2 (mobility):** Minimal direct relevance because the released
  embeddings do not model channel trajectories over time. [PROJECT]
- **Later studies:** Central to the planned channel-classification
  methods page because it clarifies the tradeoff between semantic
  embeddings, social-graph signals, and history-less recommendation
  traces. [PROJECT]

## Linked Claims

- `claim_descriptive_deficit_channel_embeddings_public_traces`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** [[channel_classification]], [[ideology_estimation]]
- **Debates:** _(none yet)_
- **Related sources:** [[rieder_2020]], [[lai_et_al_2024]], [[zaitsev_clark_2025]]
