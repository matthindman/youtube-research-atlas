---
source_id: liu_et_al_2015
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "A Quantitative Study of Video Duplicate Levels in YouTube"
authors:
  - "Liu, Yao"
  - "Blasiak, Sam"
  - "Xiao, Weijun"
  - "Li, Zhenhua"
  - "Chen, Songqing"
year: 2015
venue: "Passive and Active Measurement - 16th International Conference, PAM 2015"
doi: "10.1007/978-3-319-15509-8_18"
temporal_scope: "Random Prefix Sampling collection conducted July 2013"
themes:
  - descriptive-deficit
project_modules:
  - denominator
  - discovery-completeness
census_papers:
  - methods-companion
census_relevance: low
verification:
  machine_extracted: 27
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-24
---

# Liu et al. (2015) - Video Duplicate Levels in YouTube

## Full Citation

Liu, Yao, Sam Blasiak, Weijun Xiao, Zhenhua Li, and Songqing Chen. 2015. "A Quantitative Study of Video Duplicate Levels in YouTube." In *Passive and Active Measurement - 16th International Conference, PAM 2015, Proceedings*, Lecture Notes in Computer Science 8995, 235-248. https://doi.org/10.1007/978-3-319-15509-8_18

## One-Sentence Contribution

This paper combines Random Prefix Sampling, title-based YouTube search, modified Dynamic Time Warping, and manual validation to estimate near-duplicate video levels in YouTube's 2013 public-video corpus (pp. 1, 4-8, 10-11). [🤖]

## Research Question

How common are duplicate or near-duplicate videos on YouTube, and how much storage do those duplicates appear to occupy? (pp. 1-2, 7-11). [🤖]

## Data, Sample, Geography, and Period

- **Data:** Random Prefix Sampling video IDs, YouTube title-search results for sampled videos, downloaded H.264 Baseline/AAC/MP4/360p video files, frame-level image histograms, DTW similarity scores, and manual duplicate validation (pp. 4-7, 10-11). [🤖]
- **Sample:** 1,000 randomly generated prefixes produced 6,365 sampled videos; title searches for those videos produced 512,314 associated searched videos used as duplicate candidates (p. 7). [🤖]
- **Geography:** The study is platform-level and not country-bounded; it does not stratify by language or geography (pp. 4-8). [🤖]
- **Period:** The RPS sample was collected in July 2013, when the authors estimate YouTube contained approximately 849 million videos (p. 10). [🤖]

## Methods

The authors use Random Prefix Sampling from Zhou et al. to draw sampled videos uniformly at random from the YouTube video-ID space, generating 1,000 five-character prefixes and retrieving matching videos (p. 4). [🤖]

The duplicate search is a second stage rather than an all-pairs comparison: for each sampled video, the authors query YouTube's text search engine with the sampled video's title and retain the top 100 results, averaging 82 searched videos per sampled video (p. 5). [🤖]

For each sampled/searched pair, the authors download the 360p MP4 version, extract frames at one-second intervals with FFmpeg, and use a modified Dynamic Time Warping algorithm over color-histogram distances to score visual similarity (pp. 5-6). [🤖]

They set the DTW duplicate threshold for perfect recall on a 100-pair calibration set, then manually validate the lower-distance candidate pairs to reduce false positives; a searched video can count as a duplicate if it contains the same content, is part of the sampled video, or contains the sampled video (pp. 6-7). [🤖]

## Main Findings

1. The authors estimate a 31.7% duplicate ratio across YouTube videos and estimate that duplicates occupy 24.0% of YouTube's video storage under their 360p-file measurement approach (pp. 1, 8, 11). [🤖]
2. Of 6,365 sampled videos, 631, or 10.0%, have at least one duplicate; the reported 95% confidence interval for this probability is 0.0912-0.1065 (pp. 7-8). [🤖]
3. The manually augmented evaluation finds 2,960 duplicate videos associated with the 6,365 sampled videos, averaging 4.69 duplicates for sampled videos that have at least one duplicate (pp. 7-8). [🤖]
4. Only 327 of the 2,960 duplicate videos, or 11%, have the same byte-level content as the sampled video, meaning cryptographic hash-based exact-duplicate detection would miss most near-duplicates in this design (p. 8). [🤖]
5. The sampled-video distribution is strongly low-view: 5,529 of 6,365 sampled videos, or 87%, have fewer than 1,000 views, consistent with Zhou et al.'s finding that only about 14% of randomly sampled videos exceed 1,000 views (p. 8). [🤖]
6. Duplicate copies do not necessarily have the same attention profile: about 55% of searched-video duplicates have more views than the sampled video they duplicate (p. 9). [🤖]

## Limitations / Scope Conditions

The paper estimates near-duplicate levels through title-based candidate retrieval, so duplicates that do not share searchable title metadata or that fall outside the top 100 search results can be missed (p. 5). [🤖]

The storage estimate is based on downloaded 360p MP4 versions rather than YouTube's full internal encoding ladder, so it should be treated as an external measurement approximation rather than a direct audit of Google's storage system (pp. 5, 10-11). [🤖]

The paper assumes the 6,365 RPS sampled videos are unique originals for the purpose of duplicate-set estimation, then supports that assumption with a birthday-paradox calculation, searched-VID comparison, DTW checks, and manual confirmation (pp. 9-10). [🤖]

This is a July 2013 pre-Shorts measurement. It is useful for duplicate-level and two-stage-method precedent, not for current duplicate prevalence on YouTube (p. 10). [🤖]

## Temporal Scope

The empirical platform snapshot is July 2013, with the paper appearing at PAM 2015. It captures a pre-Shorts, pre-current-search-interface YouTube environment and should be treated as historical method evidence for the atlas (p. 10). [🤖]

## Key Quotes

> "sample YouTube videos uniformly and at random" (p. 4). [🤖]

> "roughly 1/3 of videos on YouTube are duplicates" (p. 8). [🤖]

## Relation to This Project

- **Methods companion:** Useful precedent for a two-stage design that starts with a probability sample and then uses targeted search, automated scoring, and manual validation to estimate a latent video property. [PROJECT] [🤖]
- **Paper 1 (attention economy):** Low direct relevance, but duplicate copies matter for interpreting video-count denominators because repeated visual content can inflate video-level counts relative to unique-content counts. [PROJECT] [🤖]
- **Paper 2 (mobility):** Minimal direct relevance. [PROJECT] [🤖]
- **Later studies:** Relevant to `discovery-completeness` because the candidate stage depends on YouTube title search, making search recall a scope condition for duplicate estimates. [PROJECT] [🤖]

## Linked Claims

- `claim_descriptive_deficit_video_denominators_can_include_near_duplicates`
- `claim_descriptive_deficit_two_stage_rps_can_estimate_latent_video_properties`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** [[random_video_sampling]]
- **Debates:** _(none yet)_
- **Related sources:** [[mcgrady_2023]]
