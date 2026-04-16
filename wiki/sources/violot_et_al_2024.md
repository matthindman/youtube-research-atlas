---
source_id: violot_et_al_2024
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Shorts vs. Regular Videos on YouTube: A Comparative Analysis of User Engagement and Content Creation Trends"
authors:
  - "Violot, Caroline"
  - "Elmas, Tuğrulcan"
  - "Bilogrevic, Igor"
  - "Humbert, Mathias"
year: 2024
venue: "Proceedings of the 16th ACM Web Science Conference (WEBSCI '24)"
doi: "10.1145/3614419.3644023"
temporal_scope: "January 2021-December 2022 channel-level comparison across the first two years of YouTube Shorts"
themes:
  - descriptive-deficit
project_modules:
  - shorts
  - discovery-completeness
census_papers:
  - methods-companion
  - study10-shorts-vs-long-form
census_relevance: high
verification:
  machine_extracted: 17
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Violot et al. (2024) - Shorts vs. Regular Videos

## Full Citation

Violot, Caroline, Tuğrulcan Elmas, Igor Bilogrevic, and Mathias
Humbert. 2024. "Shorts vs. Regular Videos on YouTube: A
Comparative Analysis of User Engagement and Content Creation
Trends." In *Proceedings of the 16th ACM Web Science
Conference (WEBSCI '24)*. https://doi.org/10.1145/3614419.3644023.

## One-Sentence Contribution

The paper provides the first large-scale comparative study of YouTube
Shorts and regular videos, showing that channels adopting Shorts shift
substantially toward the format and that Shorts generate distinct
engagement patterns which descriptive work cannot ignore without
missing a large share of current platform activity (pp. 1-4, 9-11).
[🤖]

## Research Question

How did the introduction of YouTube Shorts change channel upload
behavior and engagement patterns relative to regular videos, and what
does that imply for understanding the contemporary platform? (pp. 1-4,
9-11) [🤖]

## Data, Sample, Geography, and Period

- **Data:** The study collects public YouTube metadata for channels that posted at least one Short and compares their Shorts and regular-video uploads, views, likes, comments, categories, and durations (pp. 1-4). [🤖]
- **Sample:** The final dataset covers 70,712 channels, 9,883,770 Shorts, and 6,862,321 regular videos uploaded between January 2021 and December 2022 (pp. 1, 4). [🤖]
- **Geography:** The paper is platform-level rather than nationally bounded, but the sample is limited to publicly discoverable channels and videos recovered through the data-collection procedure (pp. 2-4). [🤖]
- **Period:** The analysis spans YouTube's first two years of Shorts, from January 2021 through December 2022, which makes it an early Shorts-era baseline rather than a current post-2023 census (pp. 1-4, 11). [🤖]

## Methods

The authors first collect seed short videos using keyword-based API
queries, identify which returned videos are true Shorts using the
`/shorts/<videoId>` redirect behavior because the YouTube API does not
label Shorts directly, then expand from those seeds to the full upload
histories of channels that posted at least one Short and compare Shorts
to regular videos across categories, durations, and engagement metrics
(pp. 2-4). [🤖]

## Main Findings

1. Channels that adopt Shorts increasingly upload more Shorts over time, and newly created channels move toward the format even faster than older channels do (pp. 1-4, 9-11). [🤖]
2. Shorts and regular videos are not evenly distributed across content types: Shorts cluster disproportionately in light entertainment categories, while regular videos cover a broader range including educational and political material (pp. 1, 9-10). [🤖]
3. Shorts generally receive more views and more likes per view than regular videos, but fewer comments per view, which suggests a different interaction mode from longer-form YouTube content (pp. 1, 9-11). [🤖]
4. Within the same channel, Shorts average roughly 110 times more views than regular videos, although that advantage is much weaker in education, art, and some longer-duration niches where regular videos remain comparatively strong (pp. 1, 9-11). [🤖]

## Limitations / Scope Conditions

The study includes only channels that posted at least one Short, so it
does not directly describe the full platform or channels that ignored
the format altogether (pp. 2-4, 11). [🤖]

Because the YouTube API does not natively label Shorts, the data
collection depends on a redirect-based identification strategy, which is
innovative but also illustrates how current public infrastructure makes
basic descriptive classification harder than it should be (pp. 2-4).
[🤖]

The evidence covers 2021-2022, so it predates later changes to Shorts
distribution, monetization, and recommendation systems and should not be
read as a final current-state account (pp. 1-4, 11). [🤖]

## Temporal Scope

This source is an early Shorts-era baseline. In the atlas, it matters
less as a settled current-platform measurement than as proof that
descriptive work which ignores Shorts is now missing a major, behaviorally
distinct segment of YouTube activity, especially because the public API
still does not expose a clean Shorts label (pp. 2-4, 9-11). [🤖]

## Key Quotes

> "This paper presents the first comparative analysis of YouTube Shorts versus regular videos" (p. 1) [🤖]

> "Shorts getting 110 times more views (on average) than their RVs counterparts." (p. 1) [🤖]

## Relation to This Project

- **Methods companion:** Important reminder that current platform description has to account for format heterogeneity, not just topic or channel heterogeneity. [PROJECT]
- **Paper 1 (attention economy):** Relevant because format choice changes how attention is allocated and what public traces overstate or understate. [PROJECT]
- **Paper 2 (mobility):** Indirectly relevant insofar as creator strategy and upload mix can shift sharply after platform-format innovations. [PROJECT]
- **Later studies:** Directly relevant to `study10-shorts-vs-long-form` and to any descriptive manuscript language about "YouTube" that still silently assumes long-form regular videos. [PROJECT]

## Linked Claims

- `claim_descriptive_deficit_shorts_reshape_supply_and_engagement_patterns`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** _(none yet)_
- **Debates:** _(none yet)_
- **Related sources:** [[mcgrady_2023]], [[munger_et_al_2025]], [[van_es_2020]]
