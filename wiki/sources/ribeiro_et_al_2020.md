---
source_id: ribeiro_et_al_2020
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Auditing Radicalization Pathways on YouTube"
authors:
  - "Ribeiro, Manoel Horta"
  - "Ottoni, Raphael"
  - "West, Robert"
  - "Almeida, Virgílio A. F."
  - "Meira Jr., Wagner"
year: 2020
venue: "Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency; archived corpus PDF is the arXiv v4 version"
doi: "10.1145/3351095.3372879"
temporal_scope: "Channel and comment histories through 2018 plus a nonpersonalized recommendation snapshot collected in May-July 2019"
themes:
  - recommendation-radicalization
project_modules:
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

# Ribeiro et al. (2020) - Auditing Radicalization Pathways on YouTube

## Full Citation

Ribeiro, Manoel Horta, Raphael Ottoni, Robert West, Virgílio A. F. Almeida, and Wagner Meira Jr. 2020. "Auditing Radicalization Pathways on YouTube." In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency*, 131-141. https://doi.org/10.1145/3351095.3372879. The archived corpus PDF used here is the arXiv v4 version.

## One-Sentence Contribution

The paper combines large-scale channel histories, 72 million comments, and a nonpersonalized recommendation audit to argue that users migrated from I.D.W. and Alt-lite content toward Alt-right channels over time, while Alt-right channels remained discoverable mainly through channel recommendations rather than direct video recommendations (pp. 1-2, 8-10). [🤖]

## Research Question

How have I.D.W., Alt-lite, and Alt-right YouTube channels grown, to what extent do users move from milder to more extreme contrarian communities, and do recommendation systems make that movement easier? (pp. 1-3) [🤖]

## Data, Sample, Geography, and Period

- **Data:** The study combines channel metadata, captions, more than 72 million comments, 2.47 million video recommendations, and 14,283 channel recommendations gathered with custom crawlers (pp. 1-4; p. 4 table 2). [🤖]
- **Sample:** The core corpus contains 349 channels, 330,925 videos, and 5.98 million commenting users across Alt-right, Alt-lite, I.D.W., and media categories (pp. 1-4; p. 4 table 2). [🤖]
- **Geography:** The channels and community labels are centered on U.S. political and cultural YouTube in English, even though some channels have transnational audiences (pp. 1-4). [🤖]
- **Period:** Channel, video, and comment histories span the 2008-2018 growth period, while recommendations were collected between May and July 2019, making the recommender analysis an early post-2019 snapshot layered onto pre-2019 ecosystem histories (pp. 2-4, 8-10). [🤖]

## Methods

The authors build a channel pool from seed lists, keyword searches, and featured/recommended channels; manually label channels into I.D.W., Alt-lite, Alt-right, and media groups; analyze annual growth and user-overlap patterns in comments; track cohorts of commenters over time to estimate migration into Alt-right channels; and simulate random walks on channel and video recommendation graphs built from a May-July 2019 nonpersonalized audit (pp. 3-10). [🤖]

## Main Findings

1. The three contrarian communities expanded sharply after 2015, and Alt-right channels displayed especially high comment intensity relative to their size, indicating a highly engaged audience even when their total scale remained smaller than mainstream media (pp. 5-6). [🤖]
2. Commenting user bases increasingly overlapped: by 2018, roughly half of Alt-right commenters also commented on Alt-lite and I.D.W. channels, and overlap with media channels also grew as these communities became more mainstreamed in the broader information environment (pp. 1-2, 6). [🤖]
3. Users who initially commented only on Alt-lite or I.D.W. content later commented on Alt-right channels at nontrivial rates, and these cohorts became a substantial share of the later Alt-right commenting base, especially for users starting in Alt-lite rather than only I.D.W. (pp. 7-8). [🤖]
4. In the 2019 nonpersonalized recommendation audit, Alt-lite channels were easily reachable from I.D.W. channels, while Alt-right channels were mainly reachable via channel recommendations rather than video recommendations, which the authors interpret as recommender-enabled discoverability without strong direct video promotion of Alt-right content (pp. 8-10). [🤖]

## Limitations / Scope Conditions

The study uses comments as its main user-level behavioral trace, so it treats commenting users as a proxy for radicalization and assumes comments are generally supportive rather than oppositional; the authors defend that choice, but it remains an indirect measure of viewing and persuasion (pp. 2-3, 10). [🤖]

The recommendation audit is a time slice from May-July 2019 and does not observe how the recommender behaved in earlier periods when much of the user migration may already have occurred (pp. 8-10). [🤖]

The recommendation analysis is nonpersonalized, so it cannot show how logged-in histories or strong prior watch preferences might alter reachability patterns (pp. 2, 8-10). [🤖]

Community boundaries between I.D.W., Alt-lite, and Alt-right are fuzzy and partly contested, which is why the authors adopt conservative manual labeling rules that may understate borderline cases (pp. 1-4, 10). [🤖]

## Temporal Scope

This source bridges two periods that should not be collapsed: most of its growth and commenter-migration evidence is historical and pre-2019, but its recommender audit is specifically a May-July 2019 snapshot, so it belongs in the regime-change debate as evidence from the transition rather than from either a pure pre-2019 or contemporary post-2022 system (pp. 2-4, 8-10). [🤖]

## Key Quotes

> "users consistently migrate from milder to more extreme content" (p. 1) [🤖]

> "Alt-lite content is easily reachable from I.D.W. channels" (p. 1) [🤖]

## Relation to This Project

- **Methods companion:** Useful as a combined template for channel discovery, community coding, comment-based migration analysis, and nonpersonalized recommendation audits. [PROJECT]
- **Paper 1 (attention economy):** Indirect relevance only; the paper focuses on contrarian community pathways rather than platform-wide attention shares. [PROJECT]
- **Paper 2 (mobility):** Relevant as a historical example of audience movement across linked channel communities, though the measure is commenting migration rather than full viewing mobility. [PROJECT]
- **Later studies:** Central to the rabbit-hole and pre/post-2019 debates because it provides one of the strongest historical cases for migration into more extreme right-wing YouTube communities. [PROJECT]

## Linked Claims

- `claim_recommendation_radicalization_commenter_migration_to_alt_right`
- `claim_recommendation_radicalization_channel_recommendations_reach_alt_right`

## Cross-References

- **Themes:** [[recommendation_radicalization]]
- **Methods:** [[recommendation_audit]]
- **Debates:** [[rabbit_hole_debate]], [[pre_2019_vs_post_2019_algorithm]]
- **Related sources:** [[chen_et_al_2023]], [[munger_phillips_2022]], [[yesilada_lewandowsky_2022]]
