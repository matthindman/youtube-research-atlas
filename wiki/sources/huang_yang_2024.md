---
source_id: huang_yang_2024
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Auditing Entertainment Traps on YouTube: How Do Recommendation Algorithms Pull Users Away from News?"
authors:
  - "Huang, Haoming"
  - "Yang, Tian"
year: 2024
venue: "Digital Journalism 12(10): 1367-1389"
doi: "10.1080/10584609.2024.2343769"
temporal_scope: "User-independent Up Next recommendation dyads collected in 2019 and reanalyzed as a category-transition system"
themes:
  - recommendation-radicalization
  - news-ecosystem
project_modules:
  - public-affairs
census_papers:
  - methods-companion
  - paper1-attention-economy
census_relevance: high
verification:
  machine_extracted: 18
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Huang and Yang (2024) - Entertainment Traps on YouTube

## Full Citation

Huang, Haoming, and Tian Yang. 2024. "Auditing
Entertainment Traps on YouTube: How Do Recommendation
Algorithms Pull Users Away from News?" *Digital
Journalism* 12(10): 1367-1389.
https://doi.org/10.1080/10584609.2024.2343769.

## One-Sentence Contribution

Reanalyzing 1.74 million incognito Up Next recommendation
dyads, the paper argues that YouTube's recommender does not
just personalize within topics; it also systematically
redirects attention from news toward entertainment, making
entertainment two to three times more likely than news in
steady-state recommendation flows (pp. 3, 7-15). [🤖]

## Research Question

How do YouTube recommendation algorithms shape exposure to
news versus entertainment through topical self-reinforcement,
cross-topic redirection, and the long-run balance of
recommended categories? (pp. 3-7) [🤖]

## Data, Sample, Geography, and Period

- **Data:** The study reuses Roth et al.'s open recommendation dataset and extracts 1,738,065 seed-video / Up Next dyads from user-independent YouTube recommendation crawls (pp. 3, 7-8). [🤖]
- **Sample:** The underlying audit repeatedly visited a diverse set of highly watched seed videos about 20 times each in incognito mode and categorized both seed and recommended videos using YouTube's native category labels (pp. 7-9). [🤖]
- **Geography:** The audit is platform-level rather than nationally bounded; it uses anonymous queries from over one hundred IP addresses and does not analyze recommendations for a specific country or logged-in audience segment (pp. 7-9). [🤖]
- **Period:** The recommendation dyads were collected in 2019 and analyzed as a pre-personalization benchmark for YouTube's Up Next system (pp. 1, 7-9). [🤖]

## Methods

The authors treat YouTube recommendation as a sequence of
topic transitions and analyze it in three steps. First, they
compute a transition-probability matrix for category-to-
category movement between the seed video and the first-ranked
Up Next recommendation (pp. 8-9). Second, they visualize
asymmetries between category pairs using a directed network
whose edge widths show transition gaps and whose node
centrality indicates which categories draw attention away
from others (pp. 9, 11-12). Third, they use Markov chains to
estimate the steady-state probability that a category will be
recommended after repeated transitions, which lets them ask
whether entertainment or news dominates the long-run
recommendation flow in an incognito environment (pp. 9,
12-14). [🤖]

## Main Findings

1. Topical filter bubbles exist unevenly: some entertainment-heavy categories such as automobile, sports, music, and games strongly self-reinforce, while news and politics has a much weaker self-recommendation tendency (pp. 10-11). [🤖]
2. Recommendation redirection is asymmetric between news and entertainment: after a news seed, entertainment is recommended with probability 0.18, but after an entertainment seed, news is recommended with probability only 0.03 (pp. 11-12). [🤖]
3. In Markov-chain steady-state estimates, entertainment is consistently more likely than news to be recommended; across robustness strategies, news falls between 0.05 and 0.11 while entertainment falls between 0.16 and 0.24, or even higher under a broader entertainment grouping (pp. 13-14). [🤖]
4. The paper argues that these recommendation dynamics can create "de facto news-avoided environments," because users who start with news can still be nudged toward lighter content while heavy entertainment users remain trapped in self-reinforcing entertainment flows (pp. 14-16). [🤖]

## Limitations / Scope Conditions

The study uses incognito recommendation data, so it isolates
platform-level recommendation structure at the cost of not
observing how watch history, subscriptions, or user intent
alter real recommendations (pp. 7-9, 16). [🤖]

It analyzes only the first-ranked Up Next video rather than
full recommendation panels or realized viewing sessions, so
it measures directional bias in the recommendation interface
more directly than actual user behavior (pp. 7-9, 16). [🤖]

Topic labels rely on YouTube's video categories as a proxy
for content type, which is practical but coarse and partly
dependent on uploader labeling choices (pp. 8-9, 16). [🤖]

Because the underlying dataset was collected in 2019, the
results should be treated as a late-2010s benchmark rather
than evidence about the current recommender or the Shorts
era (pp. 7-9, 16). [🤖]

## Temporal Scope

This source belongs in the regime-change discussion as
late-2010s transition evidence. It is newer than classic
pre-2019 rabbit-hole claims but still predates the more
recent user-history and experiment-heavy studies in the
atlas, which makes it useful for showing that recommendation
harm can also take the form of diversion away from public-
affairs content rather than movement toward extremity. [🤖]

## Key Quotes

> "the probability of entertainment videos to be recommended is three times higher than the probability of news videos" (p. 3) [🤖]

> "news audiences on YouTube can easily be dragged to entertainment" (p. 12) [🤖]

## Relation to This Project

- **Methods companion:** Useful as a clear example of category-transition analysis and Markov-chain modeling for recommendation flows. [PROJECT]
- **Paper 1 (attention economy):** Directly relevant because it suggests recommendation bias can lower public-affairs exposure even without ideological radicalization. [PROJECT]
- **Paper 2 (mobility):** Indirectly relevant; it tracks movement between content categories rather than movement between creator careers or audience cohorts. [PROJECT]
- **Later studies:** Bridges the recommendation-radicalization and news-ecosystem themes by showing that recommendation harms may operate through entertainment drift, not only through extremist escalation. [PROJECT]

## Linked Claims

- `claim_news_ecosystem_recommendations_redirect_news_to_entertainment`
- `claim_news_ecosystem_entertainment_bias_outweighs_news_in_up_next`

## Cross-References

- **Themes:** [[recommendation_radicalization]], [[news_ecosystem]]
- **Methods:** [[recommendation_audit]]
- **Debates:** [[filter_bubble_evidence]], [[pre_2019_vs_post_2019_algorithm]]
- **Related sources:** [[faddoul_et_al_2020]], [[haroon_et_al_2023]], [[newman_et_al_2025]]
