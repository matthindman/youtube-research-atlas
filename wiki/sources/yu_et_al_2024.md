---
source_id: yu_et_al_2024
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Nudging Recommendation Algorithms Increases News Consumption and Diversity on YouTube"
authors:
  - "Yu, Xudong"
  - "Haroon, Muhammad"
  - "Menchen-Trevino, Ericka"
  - "Wojcieszak, Magdalena"
year: 2024
venue: "PNAS Nexus"
doi: "10.1093/pnasnexus/pgae518"
temporal_scope: "Sock-puppet tuning experiments and a month-long U.S. user experiment run from November 2022-January 2023, making this an explicitly post-2022 recommendation study"
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

# Yu et al. (2024) - Nudging Recommendation Algorithms Increases News Consumption and Diversity

## Full Citation

Yu, Xudong, Muhammad Haroon, Ericka Menchen-Trevino, and Magdalena Wojcieszak. 2024. "Nudging Recommendation Algorithms Increases News Consumption and Diversity on YouTube." *PNAS Nexus* 3(12): pgae518. https://doi.org/10.1093/pnasnexus/pgae518

## One-Sentence Contribution

The paper shows that injecting balanced news input into YouTube's recommender can durably increase news recommendations and news consumption while reducing ideological congeniality, whereas nudging users themselves has no comparable effect and the added news exposure does not move downstream political attitudes (pp. 1, 6-9). [✓]

## Research Question

Can YouTube's recommendation system be nudged toward more news and more cross-cutting exposure by altering the algorithm's input stream, and does that work better than trying to nudge users directly to choose more news? (pp. 1-3) [✓]

## Data, Sample, Geography, and Period

- **Data:** Trained sock-puppet experiments, a month-long browser-extension experiment with YouTube users, collected homepage and up-next recommendations, watch histories, searches, channel data, and pre/post survey responses (pp. 1-6). [🤖]
- **Sample:** The study first trains 8,600 sock puppets from 215 real-user watch histories, then deploys a Chrome extension to 2,142 frequent U.S. YouTube users, with a final analytic sample of 1,188 participants who met minimum activity thresholds (pp. 1-6). [🤖]
- **Geography:** The user experiment is based on U.S. adults recruited by YouGov and focuses on English-language U.S. news organizations and political content (pp. 2, 4-5). [🤖]
- **Period:** The user experiment ran from November 2022 to January 2023, with one pretreatment week, two treatment weeks, and one post-treatment week (pp. 4-6). [🤖]

## Methods

The authors first use 8,600 realistic sock puppets to tune an "algorithmic nudge" that unobtrusively injects balanced news videos into watch histories, then test that intervention against a "user nudge" and control condition in a month-long browser-extension experiment with frequent YouTube users whose recommendations, exposures, and survey outcomes are tracked over time (pp. 1-6). [✓]

## Main Findings

1. The algorithmic nudge significantly and sustainably increases both recommendations to news and actual news consumption on YouTube, whereas the user nudge has no statistically significant effect on either outcome (pp. 1, 6-7). [✓]
2. The algorithmic nudge reduces ideological congeniality by shifting recommended and consumed news closer to the center and making users' news diets more diverse and cross-cutting, with especially large shifts among conservative users (pp. 1, 7-9). [✓]
3. Recommendations drive subsequent news consumption more strongly than consumption drives subsequent recommendations, indicating that the recommender is the stronger force in the feedback loop the authors model (pp. 1, 7). [✓]
4. The added news exposure has no measurable effects on political participation, belief accuracy, perceived or affective polarization, or support for democratic norms over the study period (pp. 1, 8-9). [✓]

## Limitations / Scope Conditions

The final user sample is not random or nationally representative in a strict statistical sense because participants had to be willing to install an extension and be active YouTube users, even though the authors show the sample broadly resembles the general YouTube population on basic sociodemographics (pp. 5-6). [🤖]

The intervention window is short, and the authors note that a two-week treatment may be insufficient for downstream political-attitude effects to emerge even if media effects accumulate over longer periods (pp. 8-9). [🤖]

The user experiment relies on U.S. participants, a Chrome extension, and a curated set of reliable balanced news organizations, so transport to other countries, platforms, or normative definitions of "good" news remains open (pp. 2-5, 9). [🤖]

The paper does not measure possible well-being costs from more news exposure, such as stress or anxiety among heavy news users (p. 9). [🤖]

## Temporal Scope

This paper materially thickens the post-2022 evidence bucket in the atlas: the core user experiment runs from November 2022 through January 2023, after the platform and policy shifts that the current theme page flags as understudied, and the authors explicitly treat the effects as tied to that contemporary recommender environment (pp. 1, 4-9). [✓]

## Key Quotes

> "nudging the algorithm significantly and sustainably increases both recommendations to and consumption of news..." (p. 1) [✓]

> "In contrast, nudging the users has no observable effects on news consumption." (p. 1) [✓]

## Relation to This Project

- **Methods companion:** Strong precedent for intervention-style recommendation research that changes the recommender's inputs rather than merely observing outputs. [PROJECT]
- **Paper 1 (attention economy):** Indirect relevance through the interest-bias argument that recommender systems pull users away from verified public-affairs content. [PROJECT]
- **Paper 2 (mobility):** No direct relevance because the design studies exposure shifts, not creator or channel dynamics over time. [PROJECT]
- **Later studies:** Especially relevant to filter-bubble and post-2022 debates because it shows that recommender design can broaden news exposure without obvious short-run attitude effects. [PROJECT]

## Linked Claims

- `claim_recommendation_radicalization_algorithmic_nudges_broaden_news_exposure`

## Cross-References

- **Themes:** [[recommendation_radicalization]]
- **Methods:** [[recommendation_audit]]
- **Debates:** [[filter_bubble_evidence]], [[pre_2019_vs_post_2019_algorithm]]
- **Related sources:** [[haroon_et_al_2023]], [[lai_et_al_2024]]
