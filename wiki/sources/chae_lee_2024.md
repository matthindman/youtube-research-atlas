---
source_id: chae_lee_2024
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Where do cross-cutting discussions happen?: Identifying cross-cutting comments on YouTube videos of political vloggers and mainstream news outlets"
authors:
  - "Chae, Seung Woo"
  - "Lee, Sung Hyun"
year: 2024
venue: "PLoS ONE 19(5): e0302030"
doi: "10.1371/journal.pone.0302030"
temporal_scope: "Comment data on Mueller-report YouTube videos from March 22-April 18, 2019"
themes:
  - news-ecosystem
project_modules:
  - public-affairs
census_papers:
  - paper1-attention-economy
  - study3-media-system
census_relevance: medium
verification:
  machine_extracted: 17
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Chae and Lee (2024) - Cross-Cutting Discussions on YouTube

## Full Citation

Chae, Seung Woo, and Sung Hyun Lee. 2024. "Where do
cross-cutting discussions happen?: Identifying cross-cutting
comments on YouTube videos of political vloggers and
mainstream news outlets." *PLoS ONE* 19(5): e0302030.
https://doi.org/10.1371/journal.pone.0302030.

## One-Sentence Contribution

Comparing comment threads on political-vlogger and mainstream-news
Mueller-report videos, the paper finds that cross-cutting discussion is
more common on mainstream news outlet videos, with neutral outlets such
as C-SPAN appearing more conducive than partisan vloggers, even though
many such interactions remain conflictual rather than deliberative (pp.
1, 15-17). [🤖]

## Research Question

Where on YouTube do cross-cutting political discussions happen, and how
do channel type and political leaning shape the prevalence of
cross-partisan comments on political-vlogger versus mainstream-news
videos? (pp. 1, 6-8, 15-17) [🤖]

## Data, Sample, Geography, and Period

- **Data:** The study analyzes top-level comments on YouTube videos about the Mueller report using a mix of manual coding for vlogger comments and NLP classification for mainstream-news comments (pp. 1, 6-8). [🤖]
- **Sample:** For political vloggers, the authors build a 1,000-comment labeled set from 10 vlogger videos with 100 top-level comments each; the mainstream-news sample includes videos from Fox News, LiveNOW from FOX, CNN, MSNBC, and C-SPAN and is classified with logistic regression, SVM, and random-forest models (pp. 6-8). [🤖]
- **Geography:** The study concerns U.S. political YouTube and U.S. media brands rather than a cross-national news sample (pp. 1, 6-8). [🤖]
- **Period:** The analyzed videos were posted between March 22 and April 18, 2019, anchoring the evidence in the late-2010s transition period around the Mueller report (pp. 6-8). [🤖]

## Methods

Chae and Lee first manually code the political leanings of comments on
videos by prominent political vloggers, then train NLP classifiers on
that labeled set and apply the models to mainstream-news comment
threads so they can compare the proportion of cross-cutting comments by
channel ideology and media type across a shared issue window (pp. 6-8,
9-15). [🤖]

## Main Findings

1. The share of cross-cutting comments varies by channel ideology: liberal political-vlogger videos receive more cross-cutting comments than conservative political-vlogger videos (pp. 1, 9-15). [🤖]
2. Mainstream news outlet videos host substantially more cross-cutting discussion than political-vlogger videos, which suggests that vlogger-centered political YouTube is not the only or best venue for cross-partisan interaction (pp. 1, 15-17). [🤖]
3. Neutral or less overtly partisan outlets, especially C-SPAN in this sample, appear more promising as venues for cross-cutting discussion than strongly partisan mainstream or vlogger channels (pp. 1, 15-17). [🤖]
4. The paper cautions that cross-cutting discussion is not automatically healthy deliberation, because many cross-cutting comments include ridicule, trolling, or otherwise low-quality interaction (pp. 15-17). [🤖]

## Limitations / Scope Conditions

The paper studies a single U.S. political event window and a bounded
set of channels, so it should not be treated as a platform-wide estimate
of all political discussion on YouTube (pp. 6-8, 17-18). [🤖]

The mainstream-news results depend on classifier performance trained on
the vlogger comment set, which is a reasonable design for comparison but
still introduces model error into the larger-scale classification step
(pp. 8-15, 17-18). [🤖]

The study is about visible top-level comments rather than the full
audience, recommendation exposure, or realized news consumption, so it
speaks most directly to interaction structure rather than to total
viewing behavior (pp. 6-8, 17-18). [🤖]

## Temporal Scope

This source is transition-period interaction evidence rather than a
current-platform census. It helps the atlas's news-ecosystem theme by
showing that cross-partisan discussion depends on media type and channel
ideology, but it should be read as a 2019 benchmark rather than as a
direct description of today's comment system or Shorts-era politics (pp.
6-8, 15-18). [🤖]

## Key Quotes

> "the proportion of cross-cutting discussions significantly varies by both the channel's political leaning and media type." (p. 1) [🤖]

> "our results suggest the possibility of neutral news outlets as a place for cross-cutting discussions." (p. 1) [🤖]

## Relation to This Project

- **Methods companion:** Useful as a comment-classification example showing how labeled political leanings can be compared across different channel types. [PROJECT]
- **Paper 1 (attention economy):** Relevant because it suggests that public-affairs interaction on YouTube depends on where users meet, not just on whether they meet across ideological lines at all. [PROJECT]
- **Paper 2 (mobility):** Limited direct relevance; it studies comment-layer interaction rather than creator or audience mobility over time. [PROJECT]
- **Later studies:** Complements [[wu_resnick_2021]] by shifting attention from active commenters on partisan-media channels to media-type differences between vlogger and mainstream-news contexts. [PROJECT]

## Linked Claims

- `claim_news_ecosystem_mainstream_news_comment_threads_more_cross_cutting_than_vloggers`

## Cross-References

- **Themes:** [[news_ecosystem]]
- **Methods:** [[ideology_estimation]]
- **Debates:** [[filter_bubble_evidence]]
- **Related sources:** [[wu_resnick_2021]], [[reveilhac_2024]], [[newman_et_al_2025]]
