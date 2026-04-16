---
source_id: lai_et_al_2024
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Estimating the Ideology of Political YouTube Videos"
authors:
  - "Lai, Angela"
  - "Brown, Megan A."
  - "Bisbee, James"
  - "Tucker, Joshua A."
  - "Nagler, Jonathan"
  - "Bonneau, Richard"
year: 2024
venue: "Political Analysis"
doi: "10.1017/pan.2023.42"
temporal_scope: "Reddit-YouTube link data from December 31, 2011 to June 21, 2021; application to browsing histories from May 17-July 14, 2020"
themes:
  - recommendation-radicalization
project_modules:
  - public-affairs
  - classification-llm
census_papers:
  - methods-companion
  - study3-media-system
census_relevance: high
verification:
  machine_extracted: 8
  human_checked: 9
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-15
---

# Lai et al. (2024) - Estimating the Ideology of Political YouTube Videos

## Full Citation

Lai, Angela, Megan A. Brown, James Bisbee, Joshua A. Tucker, Jonathan Nagler, and Richard Bonneau. 2024. "Estimating the Ideology of Political YouTube Videos." *Political Analysis* 32: 345-360. https://doi.org/10.1017/pan.2023.42

## One-Sentence Contribution

The paper introduces a scalable video-level ideology estimator for political YouTube videos using Reddit link structure plus text metadata, then uses it to study ideological congruence in watch histories and the engagement profile of ideological extremes (pp. 345-359). [✓]

## Research Question

Can cross-platform linking data be used to estimate the ideology of individual political YouTube videos at scale, and what do those estimates reveal about ideological media diets and engagement on YouTube? (pp. 345-346, 356-359) [✓]

## Data, Sample, Geography, and Period

- **Data:** Pushshift Reddit posts linking to YouTube, YouTube video metadata, human-coded validation data, and 2020 browsing histories from Aslett et al. (2022) (pp. 349-359). [🤖]
- **Sample:** Roughly 31 million Reddit posts were filtered to build the political-subreddit universe; the core subreddit-video matrix contains 74,038 videos by 685 subreddits, reduced to 61,883 videos with metadata; validation uses 9,282 held-out videos plus 937 human-labeled videos; the application section uses 345 respondents who watched 6,012 political videos (pp. 349-357). [🤖]
- **Geography:** The ideology space is U.S.-politics-centric, anchored in political subreddits, prior U.S.-focused channel labels, and survey respondents' self-reported U.S. party identification (pp. 345-346, 353-357). [🤖]
- **Period:** Reddit-link data run from December 31, 2011 to June 21, 2021, while the browsing-history application covers May 17-July 14, 2020 (pp. 349, 356). [🤖]

## Methods

The method has two steps: correspondence analysis on a political subreddit-video matrix to scale videos posted on Reddit, followed by fine-tuning BERT on titles, descriptions, and tags so ideology can be predicted for any political video with text metadata (pp. 345-351). [✓]

## Main Findings

1. Existing YouTube ideology datasets have mostly been channel-level and hand-labeled, which makes them static and unable to capture within-channel variation across videos (pp. 346-347). [✓]
2. The two-step estimator performs well against held-out and human-labeled data, with a 0.891 correlation on the holdout test set and more than 75% pairwise agreement when compared videos are far apart ideologically (pp. 351, 354-355). [✓]
3. Applied to 2020 browsing histories, Democrats and Republicans watched clearly different ideological distributions of political videos, and respondent-level variance was much smaller than the full ideology distribution, consistent with ideologically congruent media diets (pp. 356-357). [✓]
4. Ideologically extreme videos generated more comments and more likes or dislikes per view than moderate videos, even though view counts themselves showed no clear association with ideology (pp. 358-359). [✓]

## Limitations / Scope Conditions

The estimator depends on cross-platform link structure and uploader-supplied text metadata, so it is strongest where political videos circulate through ideologically legible Reddit communities and retain informative titles, descriptions, or tags (pp. 345-346, 359). [🤖]

The strongest validation evidence is narrowed to videos judged political and relevant to U.S. politics; videos with substantial cross-aisle coder disagreement are dropped from parts of the validation analysis (pp. 355-356). [🤖]

The watch-history application is observational and cannot separate the effects of recommendations from search, subscriptions, or prior user preferences (pp. 356-359). [🤖]

## Temporal Scope

The training corpus spans 2011-2021 Reddit-to-YouTube linkages, so the scale is not tied to a single post-2019 recommendation regime; the paper's direct evidence about media diets and engagement comes from May-July 2020 browsing histories and should be read as early-post-2019 rather than timeless (pp. 349, 356-359). [🤖]

## Key Quotes

> "our method estimates the ideology of each video rather than applying channel-level labels." (p. 346) [✓]

> "users opt for ideologically congruent content rather than merely viewing a random sample of ideological YouTube content." (p. 357) [✓]

## Relation to This Project

- **Methods companion:** Directly relevant as a reusable measurement design for turning political video metadata into an ideology scale without hand-labeling each new video. [PROJECT]
- **Paper 1 (attention economy):** Indirectly relevant because ideology scores could help partition public-affairs attention, but the paper does not solve platform-wide denominators. [PROJECT]
- **Paper 2 (mobility):** Limited direct relevance because the estimator is cross-sectional and the paper does not model channel or video trajectories over time. [PROJECT]
- **Later studies:** Especially useful for recommendation audits, news-ecosystem mapping, and any public-affairs classification work that needs finer granularity than channel-level labels. [PROJECT]

## Linked Claims

- `claim_recommendation_radicalization_video_level_ideology_estimation`
- `claim_recommendation_radicalization_media_diets_congruence`

## Cross-References

- **Themes:** [[recommendation_radicalization]]
- **Methods:** [[ideology_estimation]]
- **Debates:** _(none yet)_
- **Related sources:** [[munger_2024]], [[munger_et_al_2025]]
