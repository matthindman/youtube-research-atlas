---
source_id: ribeiro_veselovsky_west_2023
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "The Amplification Paradox in Recommender Systems"
authors:
  - "Ribeiro, Manoel Horta"
  - "Veselovsky, Veniamin"
  - "West, Robert"
year: 2023
venue: "Proceedings of the Seventeenth International AAAI Conference on Web and Social Media (ICWSM 2023)"
doi: null
temporal_scope: "A stylized agent-based model published in 2023; motivated by pre-2023 YouTube audit and navigation-log findings rather than tied to a single observation window"
themes:
  - recommendation-radicalization
project_modules:
  - public-affairs
census_papers:
  - methods-companion
  - study3-media-system
census_relevance: medium
verification:
  machine_extracted: 16
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Ribeiro, Veselovsky, and West (2023) - The Amplification Paradox

## Full Citation

Ribeiro, Manoel Horta, Veniamin Veselovsky, and Robert
West. 2023. "The Amplification Paradox in Recommender
Systems." In *Proceedings of the Seventeenth International
AAAI Conference on Web and Social Media*.

## One-Sentence Contribution

The paper offers a stylized agent-based explanation for why
blind-following audits can make recommenders look
radicalizing while real-user traces do not: extreme content
may be surfaced by collaborative filtering but still be
deamplified in actual consumption because its utility is low
for most users (pp. 1, 4-5). [🤖]

## Research Question

How can recommender systems appear to amplify extreme
content in audit studies while seeming not to drive the
consumption of that content in studies based on real user
behavior? (p. 1) [🤖]

## Data, Sample, Geography, and Period

- **Data:** The paper does not use new platform-trace data; instead it analyzes outputs from a stylized collaborative-filtering model with a user-preference matrix and simulated recommendation interactions across ideological topics (pp. 1-3). [🤖]
- **Sample:** The baseline simulation uses 600 users, 600 items, five ideological topics, 20 recommendations per round, and repeated burn-in plus measurement interactions under fixed parameter settings (pp. 2-3). [🤖]
- **Geography:** The model is abstract rather than geographically bounded, though it is motivated by the contemporary YouTube radicalization literature and uses a left-to-right political-content framing common in U.S.-focused audit work (pp. 1-2). [🤖]
- **Period:** The intervention is conceptual rather than period-specific; it responds to the state of the YouTube audit and navigation-log literature available by 2023 (pp. 1, 4-5). [🤖]

## Methods

The authors build a simple collaborative-filtering recommender
in which users differ in their utility for items from five
political topics: Far Left, Left, Center, Right, and Far Right
(pp. 2-3). More extreme topics are modeled as more niche,
meaning high utility is concentrated among fewer users
(p. 2). After a burn-in phase with utility-informed choices,
the paper runs two simulations: one where users blindly
follow recommendations, mirroring audit studies, and one
where users choose recommended items proportional to their
utility, approximating real-user behavior (pp. 3-4). The
comparison asks whether topics are amplified or deamplified
relative to the share users would consume absent the
recommender (pp. 2-4). [🤖]

## Main Findings

1. In the blind-following simulation, users become increasingly exposed to the most niche and extreme topics over repeated recommendation rounds, reproducing the kind of escalation pattern that audit studies often report (pp. 3-4). [🤖]
2. In the utility-informed simulation, extreme topics are never consumed above their relative utility and are deamplified on average, which matches the general pattern in real-user YouTube trace studies that do not find recommendations to be the main driver of extreme-content consumption (pp. 4-5). [🤖]
3. The proposed mechanism depends on nicheness rather than ideological extremity per se: any low-utility niche content could show the same pattern, so apparent "amplification" in recommendation lists does not automatically imply amplified consumption or persuasion (pp. 4-5). [🤖]
4. The paper concludes that audits which ignore user preferences are limited for diagnosing rabbit holes, radicalization, or filter bubbles because those phenomena emerge from repeated human-algorithm interaction rather than from recommendation outputs alone (pp. 1, 4-5). [🤖]

## Limitations / Scope Conditions

The model is intentionally simple and should be read as an
"existence proof" rather than as a realistic reconstruction of
the YouTube recommender system or of any specific empirical
population (pp. 4-5). [🤖]

The results do not directly measure YouTube recommendations,
real users, or attitudinal outcomes; they instead show one
plausible mechanism that could reconcile conflicting prior
findings (pp. 1, 4-5). [🤖]

Because user preferences are assumed rather than observed,
the conclusions depend on the plausibility of the utility
matrix and the nicheness assumptions built into the
simulation (pp. 2-5). [🤖]

The model also brackets other processes that may matter on
YouTube, including how recommendations shape preferences
over time or how platform incentives alter what creators
choose to upload (p. 5). [🤖]

## Temporal Scope

This source is best understood as a 2023 theoretical
intervention into how the atlas interprets pre-2023
recommendation evidence. It is not itself a pre-2019 or
post-2019 observation of YouTube behavior, but it matters for
how we read the disagreement between audit studies and
real-user navigation studies. [🤖]

## Key Quotes

> "users rarely consume niche content when given the option because it is of low utility to them" (p. 1) [🤖]

> "extreme topics are deamplified by the recommender system" (p. 4) [🤖]

## Relation to This Project

- **Methods companion:** Directly relevant because it warns that recommendation audits without user-choice modeling can misstate downstream amplification. [PROJECT]
- **Paper 1 (attention economy):** Indirectly relevant as a conceptual bridge between recommendation lists and realized consumption in political media systems. [PROJECT]
- **Paper 2 (mobility):** Relevant as a reminder that observed movement into fringe content depends on user demand and utility, not only on what the recommender surfaces. [PROJECT]
- **Later studies:** Important theoretical complement for the rabbit-hole and filter-bubble debates because it explains why audit outputs and browsing-trace studies can diverge without one side being simply wrong. [PROJECT]

## Linked Claims

- `claim_recommendation_radicalization_extreme_content_can_be_deamplified_in_consumption`
- `claim_recommendation_radicalization_audits_need_user_preference_models`

## Cross-References

- **Themes:** [[recommendation_radicalization]]
- **Methods:** [[recommendation_audit]]
- **Debates:** [[rabbit_hole_debate]], [[filter_bubble_evidence]]
- **Related sources:** [[haroon_et_al_2023]], [[brown_et_al_2022]], [[chen_et_al_2023]]
