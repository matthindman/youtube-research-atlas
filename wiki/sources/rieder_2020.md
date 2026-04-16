---
source_id: rieder_2020
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Mapping YouTube: A quantitative exploration of a platformed media system"
authors:
  - "Rieder, Bernhard"
  - "Coromina, Òscar"
  - "Matamoros-Fernández, Ariadna"
year: 2020
venue: "First Monday 25(8)"
doi: "10.5210/fm.v25i8.10667"
temporal_scope: "Crawler ran November 26, 2019-January 8, 2020 and describes pre-2020 YouTube data-access conditions"
themes:
  - descriptive-deficit
  - governance-data-access
project_modules:
  - discovery-completeness
  - api-compliance
  - taxonomy
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

# Rieder, Coromina, and Matamoros-Fernández (2020) - Mapping YouTube

## Full Citation

Rieder, Bernhard, Òscar Coromina, and Ariadna
Matamoros-Fernández. 2020. "Mapping YouTube: A quantitative
exploration of a platformed media system." *First Monday* 25(8),
August 3. https://doi.org/10.5210/fm.v25i8.10667

_Citation convention: this `First Monday` source is an online-only web
article archived as `.mhtml`, so citations use section headings and note
locators rather than fixed page numbers._

## One-Sentence Contribution

The paper uses a 36M+-channel crawl to map YouTube's hierarchy,
category system, and country structure while also documenting a
late-2019 research-access regime built on public subscriptions,
featured-channel links, and high-quota Data API access that later
became harder to replicate (§ 2.1; § 2.2; § 4). [🤖]

## Research Question

How can a very large crawl based on YouTube's public data interfaces map
the platformed media system of channels, topics, and country
affiliations, and what does that reveal about hierarchy and segmentation
on YouTube (§ 1; § 2.1; § 4)? [🤖]

## Data, Sample, Geography, and Period

- **Data:** Channel metadata and channel-to-channel links from featured
  channels and public channel subscriptions, plus video listings and
  video metadata gathered through the `channels`, `playlistItems`, and
  `videos` API endpoints (§ 2.1; note 11). [🤖]
- **Sample:** The crawl discovered 36,336,861 total channels, including
  4,415,180 with more than 1,000 subscribers; it then retrieved full
  video metadata for the 100k+ tier and a one-percent sample for the
  1k-10k and 10k-100k tiers (§ 2.1). [🤖]
- **Geography:** The analysis is global rather than single-country and
  uses channel country-affiliation fields to compare national and
  language-linked subsystems across 150 countries with at least 100
  channels in the transposed network (§ 3.3; § 4). [🤖]
- **Period:** Data collection ran from November 26, 2019 to January 8,
  2020, just before the new "made for kids" flag took effect, and the
  resulting measures are a late-2019 snapshot rather than a synchronized
  census of a single day (§ 2.1; § 2.2). [🤖]

## Methods

Rieder et al. implement a breadth-first crawler in Python that starts
from a seed channel, follows featured-channel and public-subscription
links, and keeps traversing when newly discovered channels exceed a
subscriber cutoff, which lets them organize both collection and analysis
around YouTube's 1k, 10k, and 100k creator tiers (§ 2.1). [🤖]

The paper then uses descriptive statistics, network analysis, and
category and country breakdowns as an explicitly exploratory mapping
exercise rather than a causal design, with a separate sample-
qualification section that estimates near-complete coverage for 10k+
channels and weaker completeness below that threshold (§ 2.2; § 2.3; §
4). [🤖]

## Main Findings

1. The crawl appears close to complete for channels above 10,000
   subscribers and especially strong for the 100k+ tier, while the
   1k-10k tier is less complete and the below-1k universe is much more
   uncertain (§ 2.2). [🤖]
2. YouTube is highly concentrated: the roughly 153,000 channels above
   100,000 subscribers make up about 0.42 percent of the sample but
   account for 69.2 percent of subscribers and 62.4 percent of views (§
   4). [🤖]
3. YouTube's own automated topic system is not a reliable political
   classification layer: many far-right "alternative influence network"
   channels were unclassified or grouped under Entertainment and
   Lifestyle rather than Politics or Society (§ 3.2; § 4). [🤖]
4. English-language countries, especially the United States, occupy the
   network core, but the platform also contains substantial secondary
   language-centered subsystems such as Brazil, Russia, India, and the
   Spanish-speaking sphere (§ 3.3; § 4). [🤖]

## Limitations / Scope Conditions

The crawler depends on public featured-channel links and public channel
subscriptions, so private subscriptions and channels without traversable
links remain systematic blind spots (§ 2.1; § 2.2). [🤖]

Coverage is strongest above 10,000 subscribers, while the paper
estimates that roughly 10-15 percent of 1k-10k channels may be missing
and treats channels below 1,000 subscribers with much greater caution (§
2.2). [🤖]

The dataset is a six-week snapshot with cumulative counts and little
historical state reconstruction, so later views may attach to older
videos and metadata fields may have changed before collection (§ 2.2).
[🤖]

Replication is historically contingent: the study used a 50M-unit/day
token from the YouTube Data Tools and states that YouTube no longer
seemed to issue similarly generous tokens for new research projects (§
2.1; note 12). [🤖]

## Temporal Scope

This source is best treated as a historical baseline for late-2019 and
early-2020 YouTube infrastructure. It predates Shorts, later governance
and API restrictions, and the post-2022 access environment, so its
strongest methodological value is in showing what large-scale channel
mapping could still do at that time and what later researchers may no
longer be able to replicate cleanly (§ 2.1; § 2.2; § 4). [🤖]

## Key Quotes

> "YouTube unfortunately no longer seems to issue similarly generous
> tokens..." (§ 2.1 note 12) [🤖]

> "the highly connected character of YouTube channels indeed makes
> crawling a viable technique." (§ 4) [🤖]

## Relation to This Project

- **Methods companion:** Directly relevant because it documents a now-
  historical but highly consequential YouTube data-access regime and
  shows how large-scale channel mapping depended on that regime.
  [PROJECT]
- **Paper 1 (attention economy):** Useful for framing concentration and
  for cautioning that platform-supplied categories are too noisy to
  serve as a public-affairs denominator by themselves. [PROJECT]
- **Paper 2 (mobility):** Indirectly useful as background on channel
  tiers and cross-channel connectivity, but it does not study creator
  trajectories directly. [PROJECT]
- **Later studies:** Strong bridge source for the planned channel-
  classification methods page because it establishes both the older API
  affordances and the weaknesses of YouTube's native category system.
  [PROJECT]

## Linked Claims

- `claim_descriptive_deficit_infrastructure_constraints`
- `claim_governance_data_access_historical_public_research_affordances`

## Cross-References

- **Themes:** [[descriptive_deficit]], [[governance_data_access]]
- **Methods:** [[channel_classification]]
- **Debates:** _(none yet)_
- **Related sources:** [[norton_shapiro_2024]], [[ribeiro_west_2021]], [[zaitsev_clark_2025]]
