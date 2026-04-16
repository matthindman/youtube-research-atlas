---
type: theme-synthesis
canonical_name: recommendation_radicalization
title: "Recommendation Algorithms, Exposure, and Radicalization"
status: machine-draft
temporal_scope: "Pre-2019 and post-2019 algorithm regimes must be separated"
themes: [recommendation-radicalization]
census_papers: [methods-companion, study3-media-system]
last_refreshed: 2026-04-15
source_count: 1
key_sources:
  - haroon_et_al_2023
split_candidates:
  - rabbit_hole_debate
  - filter_bubble_evidence
  - interest_bias
  - pre_2019_vs_post_2019_algorithm
verification:
  machine_extracted: 19
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
---

# Recommendation Algorithms, Exposure, and Radicalization

> **Early Batch 3 population.** This single-source draft is anchored
> in a post-2019 recommender audit and should not be read backward
> onto pre-2019 platform conditions.

## Why This Theme Matters

Recommendation-radicalization debates often collapse three distinct
questions: whether recommendations are congenial, whether trails
become more extreme, and whether problematic channels still achieve
meaningful reach. Haroon et al. matter because they isolate the
algorithm more cleanly than either untrained sock puppets or pure
browsing-history studies, while still keeping those three outcomes
separate (Haroon et al. 2023, pp. 1-8). [🤖]

## Current Consensus

- Under post-2019 conditions, YouTube recommendations are
  ideologically congenial for partisan users, especially on the
  homepage (Haroon et al. 2023, pp. 1, 4-5). [🤖]
- Congeniality does not imply a strong rabbit-hole dynamic: the
  deepest recommendation trails become only slightly more extreme,
  and the strongest progression is concentrated among very-right
  users (Haroon et al. 2023, pp. 5-7). [🤖]
- Problematic channels remain a low average share of recommendations
  but still reach a substantial minority of users, creating a
  low-rate/high-reach tension that simple averages can hide
  (Haroon et al. 2023, pp. 1, 6-8). [🤖]

## Main Disagreements

This source cuts against the strongest rabbit-hole version of the
recommendation-radicalization story, but it does not vindicate the
platform. The same audit that finds limited extremization also finds
growing exposure to problematic channels deeper in the trail. The
disagreement therefore shifts from "does the algorithm matter?" to
"which outcome matters most: ideological extremity, problematic
content reach, or both?" (Haroon et al. 2023, pp. 6-8). [🤖]

The paper also preserves a method dispute. Trained sock puppets are
better than untrained random walks for modeling recommendation
personalization, but they still do not observe what real users would
click, skip, or search for. That means the audit isolates algorithmic
opportunity structures more clearly than realized user experience
(Haroon et al. 2023, pp. 2-3, 8). [🤖]

## Evidence Inventory

| Claim | Source | Evidence | Strength | Period | Verified |
|-------|--------|----------|----------|--------|----------|
| Partisan users receive congenial recommendations, especially on the homepage. | Haroon et al. 2023 | 100,000 trained sock puppets with homepage recommendation capture | single-source | Post-2019 regime, audit current to 2022-2023 | [🤖] |
| Recommendation trails become only slightly more extreme, with the clearest growth among very-right users. | Haroon et al. 2023 | Up-next trails to depth 20 with ideology scoring from Twitter audiences | single-source | Post-2019 regime, audit current to 2022-2023 | [🤖] |
| Problematic channels are a low share of recommendations but still reach 36.1% of sock puppets overall. | Haroon et al. 2023 | Up-next trails linked to prior lists of problematic channels | single-source | Post-2019 regime, audit current to 2022-2023 | [🤖] |

## Methodological Reasons for Disagreement

- Trained sock puppets occupy a middle ground between untrained
  automated audits and real-user browsing histories, helping isolate
  the recommender while sacrificing direct evidence about user
  clicking and search behavior (Haroon et al. 2023, pp. 2-3, 8). [🤖]
- Video ideology is measured at the video level rather than the
  channel level, but the slant scale is still anchored in a U.S.
  left-right political space inferred from Twitter audiences
  (Haroon et al. 2023, pp. 2-4). [🤖]
- Problematic exposure is measured against prior channel lists, which
  means uncategorized channels deeper in the trail can depress the
  observed share of problematic recommendations (Haroon et al. 2023,
  pp. 6-7). [🤖]

## Measures and Variables Used in the Literature

Measures here include a continuous -1 to +1 video slant score, five
ideological sock-puppet categories, slope-based congeniality of
homepage recommendations, an exposure metric across trail depth,
changes in mean slant and standard deviation, and counts or shares of
recommendations from channels labeled problematic in prior audits
(Haroon et al. 2023, pp. 2-8). [🤖]

## What This Means for Our Project

- Any refreshed synthesis on recommendation radicalization has to
  separate post-2019 audit evidence from pre-2019 pathway claims.
  [🤖]
- The project should keep low-average-rate and high-platform-reach
  claims analytically distinct, especially for problematic public-
  affairs content. [🤖]
- Later Census work that studies discovery should pair audit designs
  like this with direct evidence about what users actually watch,
  click, or search for after recommendation exposure. [🤖]

## Open Holes / Next Sources to Acquire

- No direct evidence here speaks to pre-2019 recommendation behavior
  or to long-term cumulative exposure effects. [🤖]
- The paper does not observe real-user interactions with the
  recommendations it captures. [🤖]
- The main text leaves the exact fielding window less visible than
  the regime period, which complicates fine-grained temporal
  comparisons. [🤖]

## Sources Consulted

- [[haroon_et_al_2023]]

## Cross-References

- **Methods:** [[recommendation_audit]]
- **Debates:** _(none yet; expected splits: rabbit_hole_debate, filter_bubble_evidence, interest_bias, pre_2019_vs_post_2019_algorithm)_
- **Papers:** [[methods_companion_dossier]]
