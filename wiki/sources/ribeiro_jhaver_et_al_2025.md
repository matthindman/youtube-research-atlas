---
source_id: ribeiro_jhaver_et_al_2025
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Deplatforming Norm-Violating Influencers on Social Media Reduces Overall Online Attention Toward Them"
authors:
  - "Ribeiro, Manoel Horta"
  - "Jhaver, Shagun"
  - "Cluet-i-Martinell, Jordi"
  - "Reignier-Tayar, Marie"
  - "West, Robert"
year: 2025
venue: "Proceedings of the ACM on Human-Computer Interaction 9(2), Article CSCW062"
doi: "10.1145/3710960"
temporal_scope: "Deplatforming events from January 2016-September 2021 with online-attention traces observed from April 2015-September 2022"
themes:
  - governance-data-access
  - recommendation-radicalization
project_modules:
  - public-affairs
census_papers:
  - methods-companion
  - study3-media-system
  - study8-deplatforming-spillovers
census_relevance: high
verification:
  machine_extracted: 18
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Ribeiro, Jhaver, Cluet-i-Martinell, Reignier-Tayar, and West (2025) - Deplatforming and Online Attention

## Full Citation

Ribeiro, Manoel Horta, Shagun Jhaver, Jordi Cluet-i-Martinell,
Marie Reignier-Tayar, and Robert West. 2025. "Deplatforming
Norm-Violating Influencers on Social Media Reduces Overall Online
Attention Toward Them." *Proceedings of the ACM on Human-Computer
Interaction* 9(2), Article CSCW062. https://doi.org/10.1145/3710960.

## One-Sentence Contribution

Across 165 deplatforming events targeting 101 influencers, the paper
finds that cross-platform bans reduce overall online attention and that
the largest drops occur for misinformation-linked cases and coordinated
multi-platform bans (pp. 1-3, 15-17). [🤖]

## Research Question

Does deplatforming influential norm-violating social-media figures
reduce their overall online attention, and under what conditions is the
intervention more or less effective? (pp. 1-3) [🤖]

## Data, Sample, Geography, and Period

- **Data:** A semi-supervised Reddit collection of deplatforming news,
  manual event verification, Media Cloud, Google Knowledge Graph and
  Wikidata linking, Google Trends Anchor Bank, and Wikipedia pageview
  traces (pp. 2-4, 8-10). [🤖]
- **Sample:** The final analytic dataset contains 165 deplatforming
  events targeting 101 influencers, filtered from a broader set of 275
  events involving 171 entities (pp. 8-11). [🤖]
- **Geography:** The design is cross-platform rather than single-country
  but is biased toward notable English-speaking or Anglosphere-visible
  influencers because it depends on English-language Reddit/news
  coverage and Wikipedia/Google Knowledge Graph presence (pp. 3-4,
  8-10). [🤖]
- **Period:** The bans run from January 2016 through September 2021,
  while the attention traces span April 2015 through September 2022 and
  the causal models use 12-month pre/post event windows (pp. 8-10,
  14-17). [🤖]

## Methods

The authors build the event dataset through pattern-based extraction
from Reddit post titles, then manually validate deplatforming dates and
reasons, group temporally adjacent bans into "ban groups," and label
entities and events by type, reason, and permanence (pp. 2-4, 8-11).
[🤖]

For outcomes, they use Google Trends and Wikipedia pageviews as
platform-agnostic attention traces and estimate effects with a stacked
difference-in-differences design that compares treated influencers to
yet-to-be-treated controls, followed by heterogeneity models for
temporary bans, misinformation cases, entity types, and multi-platform
ban groups (pp. 14-17). [🤖]

## Main Findings

1. After 12 months, deplatforming reduces online attention toward the
   targeted influencers by an estimated 63% on Google Trends and 43% on
   Wikipedia pageviews (pp. 1-3, 15). [🤖]
2. The study does not find a statistically meaningful difference
   between temporary and permanent bans in how much they reduce online
   attention at the 0.05 level (pp. 15-17). [🤖]
3. Deplatforming tied to misinformation produces larger drops than
   other ban reasons, and coordinated multi-platform ban groups also
   reduce attention more sharply than isolated bans (pp. 16-17). [🤖]
4. The paper does not find systematic effect differences across the
   entity labels it codes, such as politician, media personality,
   internet personality, or fringe-movement association (pp. 16-17).
   [🤖]

## Limitations / Scope Conditions

The outcome measures are Google and Wikipedia attention, not direct
exposure logs, on-platform watch histories, or alt-tech audience
measurements, so the study is best read as a cross-platform attention
analysis rather than a direct YouTube feed audit (pp. 18-19). [🤖]

The sample is selective: the paper focuses on notable influencers with
Wikipedia pages and sufficient Reddit/news visibility, which skews the
evidence toward prominent English-language cases rather than all
deplatformed accounts or communities (pp. 3-4, 8-10, 19). [🤖]

The authors argue that confounding events likely bias the estimated
effect toward zero because the incidents that trigger bans often raise
attention on their own, so the causal estimates should be treated as a
lower bound on the true effect of deplatforming (pp. 14-15, 18). [🤖]

## Temporal Scope

This source belongs to the late-2010s and early-2020s governance era:
it captures mainstream-platform deplatforming before the later Twitter
replatforming wave and before the current post-2022/2023 platform
regime fully settled. In the atlas, it should be used as historical
causal evidence about governance interventions rather than as a direct
statement about today's YouTube recommendation system (pp. 8-10, 17-19).
[🤖]

## Key Quotes

> "After 12 months, we estimate that online attention toward
> deplatformed influencers is reduced by −63% ... on Google and by −43%
> ... on Wikipedia." (p. 1) [🤖]

> "temporary deplatforming was similar to permanent deplatforming in
> how it reduced online attention toward influencers." (p. 17) [🤖]

## Relation to This Project

- **Methods companion:** Strong governance-methods source because it
  links moderation interventions to platform-agnostic attention
  outcomes using a transparent quasi-experimental design. [PROJECT]
- **Paper 1 (attention economy):** Useful mainly as evidence that
  coordinated platform sanctions can shrink the attention supply
  available to high-profile rule-violating figures. [PROJECT]
- **Paper 2 (mobility):** No direct creator-labor relevance. [PROJECT]
- **Later studies:** Especially relevant to `study8-deplatforming-
  spillovers`; it also overlaps substantively with the late-2010s
  radicalization corpus because the coded influencers include figures
  such as Alex Jones, David Duke, Gavin McInnes, and Nicholas Fuentes
  (pp. 9-10, 16-19). [PROJECT]

## Linked Claims

- `claim_governance_data_access_deplatforming_reduces_overall_online_attention`

## Cross-References

- **Themes:** [[governance_data_access]], [[recommendation_radicalization]]
- **Methods:** _(none yet)_
- **Debates:** _(none yet)_
- **Related sources:** [[lewis_2018]], [[ribeiro_et_al_2020]], [[hallinan_et_al_2025]], [[ozturan_et_al_2025]]
