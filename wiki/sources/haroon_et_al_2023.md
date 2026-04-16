---
source_id: haroon_et_al_2023
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Auditing YouTube's Recommendation System for Ideologically Congenial, Extreme, and Problematic Recommendations"
authors:
  - "Haroon, Muhammad"
  - "Wojcieszak, Magdalena"
  - "Chhabra, Anshuman"
  - "Liu, Xin"
  - "Mohapatra, Prasant"
  - "Shafiq, Zubair"
year: 2023
venue: "Proceedings of the National Academy of Sciences of the United States of America"
doi: "10.1073/pnas.2213020120"
temporal_scope: "Post-2019 recommendation regime audited with 100,000 trained sock puppets; the exact main-text collection window is not made prominent"
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
  human_checked: 8
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-15
---

# Haroon et al. (2023) - Auditing YouTube's Recommendation System

## Full Citation

Haroon, Muhammad, Magdalena Wojcieszak, Anshuman Chhabra, Xin Liu, Prasant Mohapatra, and Zubair Shafiq. 2023. "Auditing YouTube's Recommendation System for Ideologically Congenial, Extreme, and Problematic Recommendations." *Proceedings of the National Academy of Sciences of the United States of America* 120(50): e2213020120. https://doi.org/10.1073/pnas.2213020120

## One-Sentence Contribution

The paper uses 100,000 trained sock puppets to isolate YouTube's recommendation behavior at scale, finding ideologically congenial recommendations for partisan users, limited extremization in the trail itself, and a nontrivial reach of problematic channels despite low average rates (pp. 1-8). [✓]

## Research Question

Does YouTube's recommendation system place users in ideological filter bubbles, progressively radicalize them through the up-next trail, or route them toward problematic channels under post-2019 platform conditions? (pp. 1-3) [✓]

## Data, Sample, Geography, and Period

- **Data:** Sock-puppet training histories, homepage recommendations, up-next recommendation trails, Twitter-audience-based video slant scores, and prior lists of problematic channels (pp. 2-8). [🤖]
- **Sample:** 100,000 sock puppets watched 9,930,110 training videos and generated 5,393,820 test recommendations spanning 399,935 videos from 120,073 channels (pp. 3-4). [🤖]
- **Geography:** The audit is platform-wide in collection but operationalizes ideology through a U.S.-style left-right political scale built from partisan elites, politicians, pundits, and news sources (pp. 2-4). [🤖]
- **Period:** The paper studies a post-2019 recommendation environment, but the exact fielding window is not foregrounded in the main text; the article was received in August 2022 and published in December 2023 (pp. 1-8). [🤖]

## Methods

The authors train five classes of sock puppets from very-left to very-right by having each puppet watch 100 ideology-matched videos for 30 seconds, then collect homepage and up-next recommendations, score recommended videos on a -1 to +1 slant scale using Twitter audiences, and track whether trails grow more congenial, more extreme, or more likely to surface problematic channels (pp. 2-6). [✓]

## Main Findings

1. YouTube recommends ideologically congenial content to partisan users, with the strongest congruence on the homepage and especially pronounced congruence for very-right users (pp. 1, 4-5). [✓]
2. Congeniality does not translate into large rabbit-hole extremization: very-left and very-right trails become only slightly more extreme, and comparable progression is not detected for left, center, and right users (pp. 5-7). [✓]
3. Recommendations from problematic channels remain a small share of total recommendations, but they increase deeper in the trail and reach a substantial minority of users, including 36.1% overall and 40% of very-right users (pp. 1, 6-8). [✓]
4. The audit also points toward a rightward asymmetry, with very-right users receiving the most congenial and problematic recommendations and even moderate or heterogeneous sock puppets often seeing more right-leaning than left-leaning content (pp. 7-8). [🤖]

## Limitations / Scope Conditions

The sock puppets are not signed into Google accounts because phone verification was infeasible at the required scale, which means the audit captures personalized recommendation behavior without full account-linked histories (pp. 3-4). [🤖]

The study does not observe what real users would click, search for, or ignore after seeing recommendations, so it estimates exposure opportunities rather than realized behavior (p. 8). [🤖]

The problematic-channel analysis depends on prior labeled channel lists, and the authors note that uncategorized channels deeper in the trail likely cause some underestimation of problematic exposure (pp. 6-7). [🤖]

## Temporal Scope

This audit should be read as evidence about a post-2019 recommendation regime, not as a direct test of pre-2019 "rabbit hole" narratives. The paper documents contemporary exposure patterns under the platform state current to 2022-2023 and does not claim that the same dynamics held before YouTube's earlier moderation and ranking changes (pp. 1-8). [🤖]

## Key Quotes

> "We conduct an audit of the platform using 100,000 sock puppets..." (p. 1) [✓]

> "the proportion of these problematic recommendations is low (max of 2.5%), they are still encountered by over 36.1% of users..." (p. 1) [✓]

## Relation to This Project

- **Methods companion:** Direct precedent for large-scale recommendation auditing that isolates algorithmic exposure better than either untrained sock puppets or pure browsing-history data alone. [PROJECT]
- **Paper 1 (attention economy):** Indirect relevance only; the paper is about ideological exposure patterns rather than platform-wide attention shares. [PROJECT]
- **Paper 2 (mobility):** No direct relevance because the design is about recommendation exposure, not longitudinal channel dynamics. [PROJECT]
- **Later studies:** Highly relevant to any Census analysis of public-affairs discovery, ideological curation, or the gap between low average problematic rates and large platform-wide reach. [PROJECT]

## Linked Claims

- `claim_recommendation_radicalization_congeniality_without_extremization`
- `claim_recommendation_radicalization_problematic_low_rate_nontrivial_reach`

## Cross-References

- **Themes:** [[recommendation_radicalization]]
- **Methods:** [[recommendation_audit]]
- **Debates:** _(none yet)_
- **Related sources:** [[munger_2024]]
