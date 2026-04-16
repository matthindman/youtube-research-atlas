---
source_id: ribeiro_west_2021
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "YouNiverse: Large-Scale Channel and Video Metadata from English-Speaking YouTube"
authors:
  - "Ribeiro, Manoel Horta"
  - "West, Robert"
year: 2021
venue: "Proceedings of the 15th International AAAI Conference on Web and Social Media"
doi: null
temporal_scope: "English-language channels and videos collected September-November 2019, covering uploads from May 2005 through October 2019"
themes:
  - descriptive-deficit
  - cross-linguistic-variation
project_modules:
  - denominator
  - discovery-completeness
census_papers:
  - methods-companion
  - paper1-attention-economy
  - study5-cross-language
census_relevance: high
verification:
  machine_extracted: 18
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Ribeiro and West (2021) - YouNiverse

## Full Citation

Ribeiro, Manoel Horta, and Robert West. 2021. "YouNiverse: Large-Scale Channel and Video Metadata from English-Speaking YouTube." In *Proceedings of the 15th International AAAI Conference on Web and Social Media*, 1016-1024.

## One-Sentence Contribution

The paper releases a very large public metadata corpus for English-speaking YouTube and shows that even unusually large open infrastructure can remain structurally English-centric and subscriber-biased, leaving multilingual platform coverage unresolved (pp. 1, 6-7). [🤖]

## Research Question

How can researchers build and characterize a large-scale public dataset of channel and video metadata from English-speaking YouTube, and how representative is that dataset of the wider platform? (pp. 1-2, 6-7) [🤖]

## Data, Sample, Geography, and Period

- **Data:** Channel metadata, video metadata, weekly subscriber/view time series, and an anonymized comment table built from channelcrawler.com, socialblade.com, and YouTube itself (pp. 1-3). [🤖]
- **Sample:** After filtering, YouNiverse contains 136,470 English-language channels, 72,924,794 videos, weekly time-series data for 97% of channels, and a comment table built from 8.6B comments by 449M users on 20.5M videos (pp. 1-4). [🤖]
- **Geography:** The dataset is English-language rather than country-specific, so it captures a global anglophone slice of YouTube rather than a cross-national platform census (pp. 1-2, 6-7). [🤖]
- **Period:** Core channel metadata were collected in September 2019, video metadata in October-November 2019, and the corpus covers uploads from May 2005 through October 2019 (pp. 1-4). [🤖]

## Methods

The authors crawl English-language channels with more than 10,000 subscribers and at least 10 videos from channelcrawler.com, enrich those channels with Social Blade ranks and time series, pull full video metadata and comments from YouTube, filter channels again with `langdetect`, and construct subscriber-rank weights to partially correct sampling bias (pp. 2-7). [🤖]

## Main Findings

1. YouNiverse was, at the time of publication, the largest publicly released YouTube metadata corpus the authors knew of, covering 136,470 channels and 72.9M videos plus long-run time series and commenter-linkage data (pp. 1-4). [🤖]
2. The dataset provides unusually rich infrastructure for English-speaking YouTube, but it is not a platform-wide random sample: it begins from English channels with more than 10,000 subscribers and relies on third-party repositories rather than direct coverage of all YouTube content (pp. 2-3, 6-7). [🤖]
3. Weighting channels by Social Blade subscriber ranks can partially adjust for sampling bias among ranked channels, but the authors explicitly warn that the dataset is likely to over-emphasize English-language characteristics when used to infer YouTube overall (pp. 6-7). [🤖]
4. Even within this large corpus, views, comments, subscriber gains, and other activity measures are highly concentrated, underscoring how unequal platform activity is across channels and videos (pp. 4-5). [🤖]

## Limitations / Scope Conditions

The dataset focuses on English-language channels with more than 10,000 subscribers and at least 10 videos, so it excludes most small channels and does not solve the multilingual coverage problem (pp. 2-3, 6-7). [🤖]

The weighting scheme depends on Social Blade rankings, but the authors state that they do not know how representative Social Blade's channel repository is of YouTube overall (pp. 6-7). [🤖]

Older videos and channels may have been deleted or removed because of copyright complaints, which can induce recency bias in the observed corpus (p. 5). [🤖]

Not every channel has full time-series coverage, with roughly 4,000 channels lacking such data altogether (pp. 3, 5). [🤖]

## Temporal Scope

This paper is a pre-2020 snapshot of YouTube infrastructure. It predates Shorts, later API-policy shifts, and the current post-2022 governance environment, so it should be used as historical baseline infrastructure rather than as a current map of the platform (pp. 1-3, 5-7). [🤖]

## Key Quotes

> "this dataset represents the largest collection of YouTube metadata made publicly available to date." (p. 1) [🤖]

> "our dataset focuses on English-language YouTube channels ... we are likely to over-emphasize features associated with English-language channels." (p. 7) [🤖]

## Relation to This Project

- **Methods companion:** Directly useful as a precedent for large-scale YouTube metadata release, weighting for sampling bias, and explicit statement of what big public datasets still miss. [PROJECT]
- **Paper 1 (attention economy):** Useful as infrastructure context for why large-scale English-language metadata should not be confused with a full platform denominator. [PROJECT]
- **Paper 2 (mobility):** Minimal direct relevance. [PROJECT]
- **Later studies:** Important bridge between the descriptive-deficit and cross-linguistic themes because it shows that dataset scale does not by itself solve multilingual coverage. [PROJECT]

## Linked Claims

- `claim_cross_linguistic_english_centric_public_infrastructure`

## Cross-References

- **Themes:** [[descriptive_deficit]], [[cross_linguistic_variation]]
- **Methods:** _(none yet)_
- **Debates:** _(none yet)_
- **Related sources:** [[mcgrady_2023]], [[mcgrady_2025]], [[munger_et_al_2025]]
