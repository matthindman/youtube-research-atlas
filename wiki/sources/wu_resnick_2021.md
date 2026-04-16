---
source_id: wu_resnick_2021
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Cross-Partisan Discussions on YouTube: Conservatives Talk to Liberals but Liberals Don't Talk to Conservatives"
authors:
  - "Wu, Siqi"
  - "Resnick, Paul"
year: 2021
venue: "Proceedings of the Fifteenth International AAAI Conference on Web and Social Media (ICWSM 2021)"
doi: null
temporal_scope: "U.S. partisan-media videos and comments collected from January 1 to August 31, 2020"
themes:
  - recommendation-radicalization
  - news-ecosystem
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

# Wu and Resnick (2021) - Cross-Partisan Discussions on YouTube

## Full Citation

Wu, Siqi, and Paul Resnick. 2021. "Cross-Partisan
Discussions on YouTube: Conservatives Talk to Liberals but
Liberals Don't Talk to Conservatives." In *Proceedings of
the Fifteenth International AAAI Conference on Web and
Social Media*, 808-819.

## One-Sentence Contribution

The paper shows that U.S. partisan YouTube in 2020 was not
a pure echo chamber at the comment layer: cross-partisan
commenting was common among active users, but it was sharply
asymmetric, modestly down-ranked in visible comment slots,
and more toxic in reply threads than within-party exchange
(pp. 1-2, 9). [🤖]

## Research Question

How prevalent is cross-partisan discussion on YouTube, does
the platform's comment-sorting interface promote or suppress
that cross-talk, and how civil or toxic are those exchanges?
(pp. 1-2) [🤖]

## Data, Sample, Geography, and Period

- **Data:** The study builds a dataset of channel metadata, political videos, user subscriptions, hashtags and URLs in comments, top-20 displayed comments, full comment threads, and Perspective API toxicity scores (pp. 1-6). [🤖]
- **Sample:** The corpus contains 973 U.S. partisan-media channels, 274,241 political videos, and 133.8 million comments from 9.3 million users between January 1 and August 31, 2020; many headline results focus on users with at least 10 comments (pp. 1-4). [🤖]
- **Geography:** The channel set is explicitly limited to U.S. partisan media and a U.S. left-right political classification framework (pp. 1, 3-4). [🤖]
- **Period:** All videos and comments come from the first eight months of 2020, making this an election-year snapshot of YouTube's discussion layer rather than a long-run platform history (pp. 1, 4). [🤖]

## Methods

The authors assemble partisan-media channels by combining
Media Bias/Fact Check sites, featured-channel links, and
existing YouTube media-bias datasets, then filter to
political channels and videos (pp. 3-4). They infer user
leanings in two steps: first by label propagation over
partisan hashtags, URLs, and subscriptions, and then by a
hierarchical attention network trained on comment text to
classify the broader user set (pp. 4-6). Cross-partisan
discussion is measured through commenting overlap across
left- and right-leaning channels, comment-ranking analysis
compares ideological shares in all comments versus the top 20
displayed root comments, and toxicity is estimated separately
for root comments and replies with Perspective API scores
(pp. 1-2, 4-9). [🤖]

## Main Findings

1. Cross-partisan discussion was common among active users: 69.3% of commenters with at least 10 comments posted at least once on both left-leaning and right-leaning channels, and those users accounted for 85.5% of all comments (pp. 1-2). [🤖]
2. Cross-talk was asymmetric. Conservatives were much more likely than liberals to comment across ideological lines; for example, more conservatives commented on left-leaning videos than liberals commented on right-leaning videos, and the median cross-partisan comment share was much higher among conservatives (pp. 1-2, 9). [🤖]
3. YouTube's comment sorting algorithm modestly reduced cross-partisan visibility: conservatives made up 26.3% of all comments on left-leaning videos but only a bit over 20% of the comments shown in the top 20 positions (pp. 1-2, 6-7). [🤖]
4. Cross-partisan replies were more toxic than co-partisan replies on both sides, and toxicity was especially high when users replied across lines on their own ideological home turf (pp. 1-2, 7-9). [🤖]

## Limitations / Scope Conditions

The study concerns commenting behavior on U.S. partisan
media channels, so it should not be treated as a general map
of all YouTube users, all content domains, or all forms of
political exposure (pp. 3-4, 9). [🤖]

User ideology is inferred rather than directly observed,
using hashtags, subscriptions, and comment text, which is
powerful at scale but still subject to classification error
and an "unknown" residual group (pp. 4-6). [🤖]

The visibility analysis focuses on top-level comments shown
in the default top-20 interface, so it captures one part of
the interaction environment rather than the entire exposure
or moderation system (pp. 4, 6-7). [🤖]

Comment cross-talk is not the same as recommendation-driven
exposure, persuasion, or depolarization; it measures a public
interaction layer that sits downstream of whatever brought
users to the videos in the first place (pp. 1-2, 9). [🤖]

## Temporal Scope

This source is a 2020 election-year discussion snapshot. It
is important for the filter-bubble debate because it shows
that ideological isolation can look different at the comment
layer than at the recommendation layer, but it should not be
read as direct evidence about later YouTube interfaces or the
current comment-ranking system. [🤖]

## Key Quotes

> "most users with at least 10 comments posted at least once on both left-leaning and right-leaning YouTube channels" (p. 1) [🤖]

> "Cross-talk, however, was not symmetric" (p. 1) [🤖]

## Relation to This Project

- **Methods companion:** Useful for large-scale ideology inference and for separating comment visibility, commenting behavior, and toxicity into distinct observational layers. [PROJECT]
- **Paper 1 (attention economy):** Relevant because it shows that public-affairs interaction on YouTube includes visible cross-partisan contact, not just siloed attention. [PROJECT]
- **Paper 2 (mobility):** Indirectly relevant because it maps overlap in active publics rather than user movement through recommendations or channel careers. [PROJECT]
- **Later studies:** Important for the filter-bubble debate because it complicates a simple echo-chamber story without claiming that cross-partisan contact is necessarily constructive or depolarizing. [PROJECT]

## Linked Claims

- `claim_recommendation_radicalization_cross_partisan_commenting_common_asymmetric`
- `claim_recommendation_radicalization_cross_partisan_visibility_and_toxicity`

## Cross-References

- **Themes:** [[recommendation_radicalization]], [[news_ecosystem]]
- **Methods:** [[ideology_estimation]]
- **Debates:** [[filter_bubble_evidence]]
- **Related sources:** [[lai_et_al_2024]], [[liu_et_al_2025]], [[newman_et_al_2025]]
