---
source_id: golnari_et_al_2014
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "What Drives the Growth of YouTube? Measuring and Analyzing the Evolution Dynamics of YouTube Video Uploads"
authors:
  - "Golnari, Golshan"
  - "Li, Yanhua"
  - "Zhang, Zhi-Li"
year: 2014
venue: "SocialCom 2014"
doi: null
temporal_scope: "Random Prefix Sampling crawl from June 30-July 25, 2013 estimating YouTube uploads and uploaders from June 15, 2005 through June 2013"
themes:
  - descriptive-deficit
project_modules:
  - denominator
  - activity-tail
census_papers:
  - methods-companion
  - paper1-attention-economy
census_relevance: medium
verification:
  machine_extracted: 25
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-24
---

# Golnari et al. (2014) - What Drives the Growth of YouTube?

## Full Citation

Golnari, Golshan, Yanhua Li, and Zhi-Li Zhang. 2014. "What Drives the Growth of YouTube? Measuring and Analyzing the Evolution Dynamics of YouTube Video Uploads." *SocialCom 2014*.

## One-Sentence Contribution

This paper extends Random Prefix Sampling from stock-size estimation to temporal flow estimation, using sampled video labels to estimate daily uploads, uploader counts, category growth, and uploader activeness from YouTube's 2005 inception through mid-2013 (pp. 1-4). [🤖]

## Research Question

How did YouTube video uploads and uploaders grow over time, and was growth driven primarily by new uploaders, changing uploader activeness, mobile uploading, policy shocks, or heavier/professionalized uploaders? (pp. 1-2, 6-9). [🤖]

## Data, Sample, Geography, and Period

- **Data:** Random Prefix Sampling query samples from YouTube video IDs, enriched with video profile fields such as upload time, category, length, uploader, and uploader history (pp. 2-3). [🤖]
- **Sample:** The authors crawled 7,752,384 length-5 prefix query samples from June 30 to July 25, 2013, containing 7,977,651 videos in total (p. 3). [🤖]
- **Geography:** The study estimates global YouTube uploader location from user profiles; the top 20 countries account for 80% of uploaders and 82% of uploads in the estimates (p. 6). [🤖]
- **Period:** The estimates cover YouTube uploads and uploaders from June 15, 2005 through June 2013, with the crawl itself conducted June 30-July 25, 2013 (pp. 3-4, 7). [🤖]

## Methods

The paper generalizes RPS by treating video metadata fields as labels: for a label `l`, such as a category or upload date, the estimator is `N_hat_l = (1 / (m p_L)) * sum_i X_i,l^L`, where `X_i,l^L` is the number of videos with that label in the `i`-th query sample (p. 3). [🤖]

The authors also derive an uploader estimator by grouping uploaders according to how many videos they have uploaded; because videos are sampled, the number of uploaders with `k` uploads is estimated by dividing the estimated number of sampled videos from that group by `k` (p. 3). [🤖]

They use multiplicative time-series decomposition to separate upload trends, seasonality, and residual variation, and they model the main upload trend as quadratic growth followed by exponential growth with an interruption in early 2012 (pp. 4-5). [🤖]

## Main Findings

1. Estimated daily uploads rose from roughly 2 x 10^4 per day around June 2006 to about 10^6 videos per day seven years later, with an estimated cumulative total of about 1.1 x 10^9 uploaded videos by July 2013 (p. 4). [🤖]
2. The growth curve has multiple phases: an initial quadratic phase, an exponential phase beginning around late 2009/early 2010, a sudden drop for a few months in early 2012, and a resumed rapid growth phase afterward (pp. 4-5). [🤖]
3. Daily new uploaders followed similar phases until early 2012, but unlike daily video uploads, the growth rate of new uploaders did not fully recover after the 2012 disruption (p. 5). [🤖]
4. The exponential growth phase coincided with the rise of videos captured or uploaded via mobile devices, based on 77,000 videos in the unbiased sample carrying mobile-device default signatures (pp. 6-7). [🤖]
5. By June 2013, the average uploader had uploaded about eight videos, up from about two by the end of 2005; the authors attribute growth more to increasingly active recent uploaders than to older uploaders becoming more active (pp. 7-8). [🤖]
6. Uploads were concentrated among heavier uploaders: about 82% of uploaders had fewer than 7.7 uploads and contributed 24% of videos, while the remaining 18% contributed about 76% of uploads (p. 9). [🤖]

## Limitations / Scope Conditions

The findings rely on the RPS search behavior and ID-generation assumptions inherited from the 2011 method, so they share the same exposure to search-interface fragility and dash-prefix frame restrictions (pp. 2-3). [🤖]

The mobile-upload analysis is a lower-bound style inference from default signatures in video descriptions; the authors note that not all mobile uploads necessarily carry those signatures (p. 6). [🤖]

The paper's causal language around Google's early-2012 privacy-policy change is explicitly framed as speculation supported by circumstantial evidence, not as a causal identification design (pp. 6-7). [🤖]

## Temporal Scope

This is a historical pre-Shorts study of YouTube uploads and uploaders through June 2013. It is useful for temporal-flow estimation and early platform growth dynamics, but not for current upload rates or current uploader composition (pp. 3-5, 9). [🤖]

## Key Quotes

> "we have generalized and extended [RPS] to estimate the number of daily video uploads, the number of uploaders and other statistics" (p. 1). [🤖]

> "the cumulative number of uploaded YouTube videos is about 1.1 x 10^9 by July 2013" (p. 4). [🤖]

## Relation to This Project

- **Methods companion:** Important extension from stock-size estimation to flow estimation, including labeled-video and uploader estimators. [PROJECT] [🤖]
- **Paper 1 (attention economy):** Useful historical evidence that YouTube supply growth and uploader concentration are dynamic, with heavier uploaders contributing most uploads by 2013. [PROJECT] [🤖]
- **Paper 2 (mobility):** Indirect relevance only; the paper studies uploader cohorts and upload activeness rather than audience or channel mobility. [PROJECT] [🤖]
- **Later studies:** Useful as a pre-Shorts baseline for activity-tail and flow-estimator arguments, especially when distinguishing video stock from upload rate. [PROJECT] [🤖]

## Linked Claims

- `claim_descriptive_deficit_id_space_sampling_public_video_denominators`
- `claim_descriptive_deficit_upload_flow_requires_temporal_estimators`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** [[random_video_sampling]]
- **Debates:** _(none yet)_
- **Related sources:** [[mcgrady_2023]]
