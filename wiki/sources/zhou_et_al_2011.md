---
source_id: zhou_et_al_2011
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Counting YouTube Videos via Random Prefix Sampling"
authors:
  - "Zhou, Jia"
  - "Li, Yanhua"
  - "Adhikari, Vijay Kumar"
  - "Zhang, Zhi-Li"
year: 2011
venue: "Proceedings of the 2011 ACM SIGCOMM Conference on Internet Measurement Conference (IMC '11)"
doi: null
temporal_scope: "Live YouTube API sampling through May 12, 2011, with view-count and traffic estimates for April 5-18, 2011"
themes:
  - descriptive-deficit
project_modules:
  - denominator
  - discovery-completeness
census_papers:
  - methods-companion
  - paper1-attention-economy
census_relevance: high
verification:
  machine_extracted: 25
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-24
---

# Zhou et al. (2011) - Counting YouTube Videos via Random Prefix Sampling

## Full Citation

Zhou, Jia, Yanhua Li, Vijay Kumar Adhikari, and Zhi-Li Zhang. 2011. "Counting YouTube Videos via Random Prefix Sampling." *Proceedings of the 2011 ACM SIGCOMM Conference on Internet Measurement Conference (IMC '11)*, 371-380.

## One-Sentence Contribution

This paper introduces Random Prefix Sampling (RPS) as a way to estimate the number of YouTube videos from the video-ID space and derives an unbiased estimator, variance expression, and confidence-interval/sample-size guidance for that estimator (pp. 1-4). [🤖]

## Research Question

How can researchers estimate YouTube's total public video population when YouTube does not publish a denominator and brute-force random ID guessing is infeasible in the extremely large video-ID space? (pp. 1-2) [🤖]

## Data, Sample, Geography, and Period

- **Data:** YouTube video IDs returned through the YouTube Search API using randomly generated ID prefixes, plus three pre-existing ID collections used to validate prefix-search completeness and estimator behavior (pp. 2-5). [🤖]
- **Sample:** The live-system estimate uses length-5 random prefixes; for that prefix length, the paper reports that 430, 108, 48, or 27 samples are sufficient for RRMSE targets of 0.05, 0.10, 0.15, or 0.20, respectively (p. 4). [🤖]
- **Geography:** The design is not country-bounded; the authors report that prefix queries from PlanetLab nodes generally returned the same sets of results, sometimes in different orders (p. 3). [🤖]
- **Period:** The main platform-size estimate is for May 12, 2011, and the traffic estimates use daily view-count changes from April 5 through April 18, 2011 (pp. 5-6). [🤖]

## Methods

The method exploits a then-existing YouTube Search API behavior: quoted searches of the form `watch?v=<prefix>` returned videos whose IDs began with that prefix followed by a dash, allowing the authors to query small ID-space regions rather than individual 11-character IDs (pp. 1-3). [🤖]

The paper models YouTube IDs as uniformly and independently generated from an ID space whose first ten characters come from 64 symbols and whose final character comes from 16 symbols; the authors validate near-uniform character frequencies across positions in a 2-million-ID collection (p. 2). [🤖]

For a prefix of length `L`, the paper defines the match probability `p_L` as `1 / |S|^L` for `L` from 1 to 10 and `1 / (|S|^10 |T|)` for `L = 11`; with `m` sampled prefixes and returned counts `X_i^L`, the total-video estimator is `N_hat = (1 / (m p_L)) * sum_i X_i^L` (pp. 3-4). [🤖]

The estimator is unbiased under the paper's ID-generation assumptions, and its variance is `N * ((1 / (m p_L)) - 1)`, so larger samples lower variance linearly while longer prefixes raise variance sharply (p. 4). [🤖]

## Main Findings

1. Prefix searches were nearly complete in the validation checks: among IDs with a dash in the fifth position, the worst observed miss rate across three validation datasets was 0.30%, and the authors attributed misses to recent, blocked, deleted, or private videos (p. 3). [🤖]
2. With live length-5 prefix sampling, the estimated number of YouTube videos converged to roughly 5.02 x 10^8 videos by May 12, 2011 (p. 5). [🤖]
3. Breadth-first related-video crawls overstated visibility compared with the RPS sample: only 14% of RPS-sampled videos had more than 1,000 views, versus 89% and 52% in two BFS-derived datasets (pp. 5-6). [🤖]
4. The same comparison showed inflated mean views in crawl-derived datasets: 32,046 and 9,928 average views in the two BFS datasets versus 3,898 in the RPS dataset (p. 6). [🤖]
5. Using the RPS sample for daily view-count changes, the authors estimated roughly 1.7-4.6 billion YouTube views per day and 17-46 PB/day of delivery traffic during April 5-18, 2011, while explicitly describing this as a rule-of-thumb estimate (p. 6). [🤖]

## Limitations / Scope Conditions

The method depended on a specific YouTube Search API behavior and on the search engine continuing to return complete prefix-matched results, so the paper's own review documentation flagged that the method could stop working if YouTube changed its interfaces or ID assignment/search behavior (pp. 3, 8-9). [🤖]

RPS only retrieved the subset exposed by the prefix-search behavior, especially videos whose relevant position contained a dash, and its validity depends on the assumption that that subset behaves like a uniform slice of the full ID space (pp. 2-4). [🤖]

The platform-size estimate is historical evidence about public YouTube in 2011, before Shorts, major API restrictions, and later changes in YouTube search behavior; it should not be used as a current denominator (pp. 5-6). [🤖]

## Temporal Scope

This is an early-YouTube, pre-Shorts, pre-current-API-regime method paper. Its strongest current value is formal: it defines RPS, its estimator, and its variance/CI logic, not a reusable 2011 point estimate for today's platform (pp. 1-6). [🤖]

## Key Quotes

> "we develop a random prefix sampling method to estimate the total number of videos hosted by YouTube" (p. 1). [🤖]

> "the total number of YouTube videos converges to 5.02 x 10^8 (502 millions)" (p. 5). [🤖]

## Relation to This Project

- **Methods companion:** Foundational source for the RPS estimator, variance expression, and sample-size logic that later random-video sampling papers cite as method origin. [PROJECT] [🤖]
- **Paper 1 (attention economy):** Useful historical evidence that crawl-derived samples can radically undercount low-view videos and inflate average view counts. [PROJECT] [🤖]
- **Paper 2 (mobility):** Limited direct relevance because the paper estimates video stock and aggregate traffic rather than channel or audience movement. [PROJECT] [🤖]
- **Later studies:** Provides the formal ancestor for later RPS applications and for current caution that search-based random sampling inherits search-interface fragility. [PROJECT] [🤖]

## Linked Claims

- `claim_descriptive_deficit_denominator_problem`
- `claim_descriptive_deficit_id_space_sampling_public_video_denominators`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** [[random_video_sampling]]
- **Debates:** _(none yet)_
- **Related sources:** [[mcgrady_2023]], [[mcgrady_2025]]
