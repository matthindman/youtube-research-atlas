---
source_id: hosseinmardi_et_al_2024
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Causally Estimating the Effect of YouTube's Recommender System Using Counterfactual Bots"
authors:
  - "Hosseinmardi, Homa"
  - "Ghasemian, Amir"
  - "Rivera-Lanas, Miguel"
  - "Ribeiro, Manoel Horta"
  - "West, Robert"
  - "Watts, Duncan J."
year: 2024
venue: "Proceedings of the National Academy of Sciences of the United States of America"
doi: "10.1073/pnas.2313377121"
temporal_scope: "Desktop browsing histories from October 2021-December 2022 with bot experiments run in early 2023; findings explicitly scoped to the post-2019 recommendation regime"
themes:
  - recommendation-radicalization
project_modules:
  - public-affairs
census_papers:
  - methods-companion
  - study3-media-system
census_relevance: high
verification:
  machine_extracted: 9
  human_checked: 9
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-15
---

# Hosseinmardi et al. (2024) - Causally Estimating the Effect of YouTube's Recommender System

## Full Citation

Hosseinmardi, Homa, Amir Ghasemian, Miguel Rivera-Lanas, Manoel Horta Ribeiro, Robert West, and Duncan J. Watts. 2024. "Causally Estimating the Effect of YouTube's Recommender System Using Counterfactual Bots." *Proceedings of the National Academy of Sciences of the United States of America* 121(8): e2313377121. https://doi.org/10.1073/pnas.2313377121

## One-Sentence Contribution

The paper introduces "counterfactual bots" to compare matched real-user browsing trajectories with recommendation-following trajectories, finding that in the post-2019 regime YouTube's recommender moderates partisan consumption on average rather than intensifying it (pp. 1, 3-6). [✓]

## Research Question

How much partisan or extreme YouTube consumption is caused by the recommender itself, as opposed to user preferences that would have produced similar viewing even without recommendations? (pp. 1-2) [✓]

## Data, Sample, Geography, and Period

- **Data:** Nielsen desktop browsing-panel traces, logged-in bot trajectories, YouTube API metadata, and channel-level partisan scores derived from prior embeddings work (pp. 2, 7-8). [🤖]
- **Sample:** The source panel covers 87,988 desktop panelists, including 48,026 users with at least one YouTube view; the experiments focus on 4,583 users with at least 140 YouTube videos, then sample 125 focal users and generate 1,304 bot trajectories totaling 201,915 watched videos (pp. 2-3, 7-8). [🤖]
- **Geography:** The empirical panel is a nationally representative U.S. desktop web panel, so the study speaks most directly to U.S. political YouTube use on desktop devices (pp. 1, 7-8). [🤖]
- **Period:** User histories run from October 2021 through December 2022, and the bot experiments were conducted in early 2023 (pp. 2, 6-8). [🤖]

## Methods

The authors train logged-in bots on the exact viewing histories of sampled real users, then compare control bots that continue following those users' trajectories with counterfactual bots that switch to "up next," random-sidebar, random-homepage, or moderate-content paths, allowing the marginal effect of recommendations and the system's "forgetting time" to be estimated against matched counterfactuals (pp. 1-3, 5-6). [✓]

## Main Findings

1. Relative to matched real-user trajectories, relying exclusively on YouTube recommendations produces less partisan consumption on average, and that moderating effect is strongest for heavy partisan consumers (pp. 1, 3-4). [✓]
2. The observed recommendation trajectories do not become more extreme over time in the observational phase; the estimated depth coefficient is indistinguishable from zero across recommendation types (p. 4). [🤖]
3. Bursts of highly partisan viewing predict later partisan consumption because users appear to have shifted their own preferences, not because the recommender overreacts by pushing especially partisan follow-on content (p. 5). [🤖]
4. When partisan users switch to moderate content, sidebar recommendations forget partisan history within roughly 30 videos, while homepage recommendations adjust more slowly and retain more history dependence when prior partisan histories are longer (pp. 1, 5-6). [✓]

## Limitations / Scope Conditions

The paper is explicit that its findings should be interpreted as post-2019 evidence because recreating the pre-2019 recommendation system is not feasible after YouTube's 2019 ranking changes (p. 6). [✓]

The empirical panel covers desktop browsing only, so the results may not generalize to mobile consumption, where recommendation surfaces and user behavior could differ (pp. 6-7). [🤖]

The experiments compress months of behavior into two or three days of bot activity, which the authors argue is operationally necessary but acknowledge could differ from a true field experiment stretched over months (pp. 6-7). [🤖]

Partisanship is scored at the channel level rather than the video level, and roughly 20% of collected videos lack partisan scores in the main-text analysis (p. 7). [🤖]

## Temporal Scope

This is a post-2019 study in the strongest possible sense: the authors tie their interpretation directly to YouTube's 2019 algorithm changes, use 2021-2022 desktop histories plus early-2023 bot experiments, and warn against treating the results as evidence about earlier YouTube regimes (p. 6). [✓]

## Key Quotes

> "relying exclusively on the YouTube recommender results in less partisan consumption..." (p. 1) [✓]

> "our findings should be interpreted as applying only to the post-2019 period." (p. 6) [✓]

## Relation to This Project

- **Methods companion:** Strong precedent for combining observational panel traces with controlled recommendation auditing, especially when the causal question is the recommender's marginal effect relative to user preference. [PROJECT]
- **Paper 1 (attention economy):** Indirect relevance only; the paper is about political exposure mechanisms rather than platform-wide denominators or attention shares. [PROJECT]
- **Paper 2 (mobility):** No direct relevance because the design studies recommendation effects, not channel-level churn or rank dynamics. [PROJECT]
- **Later studies:** Highly relevant to any Census work that wants to pair audit designs with real-user histories, compare homepage and sidebar pathways, or distinguish algorithmic exposure from self-selection and other demand-side mechanisms. [PROJECT]

## Linked Claims

- `claim_recommendation_radicalization_post2019_limited_algorithmic_effect`

## Cross-References

- **Themes:** [[recommendation_radicalization]]
- **Methods:** [[recommendation_audit]]
- **Debates:** [[rabbit_hole_debate]], [[pre_2019_vs_post_2019_algorithm]]
- **Related sources:** [[haroon_et_al_2023]], [[munger_phillips_2022]]
