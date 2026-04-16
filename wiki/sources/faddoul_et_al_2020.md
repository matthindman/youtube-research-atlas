---
source_id: faddoul_et_al_2020
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "A Longitudinal Analysis of YouTube's Promotion of Conspiracy Videos"
authors:
  - "Faddoul, Marc"
  - "Chaslot, Guillaume"
  - "Farid, Hany"
year: 2020
venue: "arXiv preprint arXiv:2003.03318"
doi: null
temporal_scope: "Default U.S. watch-next recommendations collected daily from October 2018 through February 2020"
themes:
  - recommendation-radicalization
project_modules:
  - public-affairs
census_papers:
  - methods-companion
  - study3-media-system
census_relevance: high
verification:
  machine_extracted: 17
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Faddoul et al. (2020) - Conspiracy Promotion on YouTube

## Full Citation

Faddoul, Marc, Guillaume Chaslot, and Hany Farid. 2020.
"A Longitudinal Analysis of YouTube's Promotion of
Conspiracy Videos." *arXiv* preprint arXiv:2003.03318.

## One-Sentence Contribution

Using a year-plus nonpersonalized audit of watch-next
recommendations from popular U.S. informational channels,
the paper argues that YouTube sharply reduced default
conspiracy recommendations after its January 2019 policy
change, but did not eliminate them and still preserved a
declining conspiracy filter-bubble dynamic for users who
started from conspiratorial videos (pp. 1, 4-7). [🤖]

## Research Question

Did YouTube's 2019 effort to demote borderline and
conspiratorial content actually reduce the default promotion
of conspiracy videos, and how strongly did watch-next
recommendations continue to reinforce conspiracy exposure
over time? (pp. 1, 4-7) [🤖]

## Data, Sample, Geography, and Period

- **Data:** The study collects more than 8 million watch-next recommendations and classifies the recommended videos using a custom conspiracy detector built from titles, snippets, transcripts, comments, and Perspective API signals (pp. 1-4). [🤖]
- **Sample:** Recommendations were gathered daily from the most recent uploads of a recursively expanded set of 1,000-plus, and later 1,146, popular informational channels; the top 1,000 recommended videos per day were retained for analysis (pp. 2-4, 6). [🤖]
- **Geography:** Requests were made from U.S.-based IP addresses without identifying cookies and the channel pool centered on English-language U.S. informational YouTube (pp. 2, 4). [🤖]
- **Period:** Recommendations were collected from October 2018 through February 2020, spanning the January, June, and December 2019 YouTube announcements about borderline-content demotion (pp. 1, 4). [🤖]

## Methods

The authors emulate YouTube's default watch-next system
without personalization by starting from seed channels,
collecting the first 20 recommendations from the latest upload
of each channel each day, and iteratively expanding the pool
of informational channels surfaced by those recommendations
(pp. 2-3). To identify conspiratorial videos, they train a
two-layer classifier on 1,095 labeled videos; the final model
combines text features from snippets, captions, and comments
with comment-quality features and reaches reported precision
of 78% and recall of 86% at a 0.5 threshold (pp. 2-4). They
then track both raw recommendation frequency and a
view-weighted version that accounts for the popularity of the
source video, and estimate a conspiracy "filter bubble" by
conditioning recommendations on the conspiracy likelihood of
the previously watched video (pp. 4-6). [🤖]

## Main Findings

1. Conspiratorial recommendations from informational channels peaked in late 2018 at nearly 10% of raw recommendations and about 6% of weighted recommendations, then fell sharply after YouTube's January 25, 2019 announcement and reached a low point around 3% in early June 2019 (pp. 4-5). [🤖]
2. The decline was incomplete and partly reversed: by late 2019 the weighted share of conspiratorial recommendations had rebounded enough that it was only about 40% lower than at the start of YouTube's policy intervention, which the authors read as evidence that high-impact pathways persisted (pp. 4, 6). [🤖]
3. Watch-next recommendations displayed a clear conspiracy filter-bubble pattern, with conspiratorial source videos much more likely to yield conspiratorial recommendations, although that relationship weakened over the study period as overall conspiracy promotion fell (pp. 5-6). [🤖]
4. YouTube's demotion policy appeared selective at the channel level: some previously dominant conspiracy channels were nearly removed from default recommendations, while a smaller set of mixed legitimate-and-borderline channels captured a much larger share of the remaining conspiratorial recommendations (pp. 5-6). [🤖]

## Limitations / Scope Conditions

The recommendation tree covers a recursively constructed set
of informational channels rather than the full platform, so
the study is best read as a structured audit of a particular
news-and-information slice of YouTube rather than a census of
all recommendations (p. 6). [🤖]

The conspiracy classifier involves judgment calls about what
counts as conspiratorial and likely understates prevalence
because the authors adjust for false positives but not false
negatives; removed videos and videos with comments disabled
are also missing from the audit (p. 6). [🤖]

The audit is nonpersonalized, so it cannot tell us how watch
histories, subscriptions, or logged-in behavior changed the
recommendation experience for users who were already deep in
conspiracy content (pp. 2, 6-7). [🤖]

Because the design follows watch-next recommendations from
popular informational channels, it speaks more directly to
default discoverability than to realized user pathways that
also include search, external links, or repeated channel
subscriptions (pp. 1-2, 7). [🤖]

## Temporal Scope

This paper is most useful as transition-period evidence.
Its audit begins before YouTube's January 2019 demotion
announcement and continues through February 2020, so it helps
separate late-2018 and early-2019 recommendation dynamics
from the later post-2021 and post-2022 studies already in the
atlas. It should not be read as evidence about the current
system. [🤖]

## Key Quotes

> "The raw and weighted frequency of conspiratorial recommendations reached a maximum of almost 10% and 6%." (p. 4) [🤖]

> "The reduction of borderline policy is in fact implemented selectively." (p. 6) [🤖]

## Relation to This Project

- **Methods companion:** Useful as a template for longitudinal, nonpersonalized watch-next auditing paired with automated content classification. [PROJECT]
- **Paper 1 (attention economy):** Relevant because it shows how recommendation policy changes can reshape the visibility of fringe informational content without eliminating it. [PROJECT]
- **Paper 2 (mobility):** Indirectly relevant because it measures selective exposure dynamics, but it does not track individual user movement across channels over time. [PROJECT]
- **Later studies:** Important bridge source for the pre-2019 vs. post-2019 algorithm debate because it directly spans the 2019 demotion intervention. [PROJECT]

## Linked Claims

- `claim_recommendation_radicalization_conspiracy_recommendations_declined_after_2019_demotions`
- `claim_recommendation_radicalization_conspiracy_filter_bubble_persisted_in_2019_audit`

## Cross-References

- **Themes:** [[recommendation_radicalization]]
- **Methods:** [[recommendation_audit]]
- **Debates:** [[rabbit_hole_debate]], [[pre_2019_vs_post_2019_algorithm]]
- **Related sources:** [[ledwich_zaitsev_2020]], [[ribeiro_et_al_2020]], [[haroon_et_al_2023]]
