---
source_id: akgul_et_al_2022
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Investigating Influencer VPN Ads on YouTube"
authors:
  - "Akgul, Omer"
  - "Roberts, Richard"
  - "Namara, Moses"
  - "Levin, Dave"
  - "Mazurek, Michelle L."
year: 2022
venue: "IEEE Symposium on Security and Privacy"
doi: null
temporal_scope: "Random Prefix Sampling scrape conducted August 2020-March 2021; VPN ad videos analyzed from late 2016-mid 2020"
themes:
  - descriptive-deficit
  - creator-economy
project_modules:
  - denominator
  - classification-llm
census_papers:
  - methods-companion
census_relevance: medium
verification:
  machine_extracted: 26
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-24
---

# Akgul et al. (2022) - Investigating Influencer VPN Ads on YouTube

## Full Citation

Akgul, Omer, Richard Roberts, Moses Namara, Dave Levin, and Michelle L. Mazurek. 2022. "Investigating Influencer VPN Ads on YouTube." *IEEE Symposium on Security and Privacy*.

## One-Sentence Contribution

This paper uses an unusually large Random Prefix Sampling baseline, followed by view-thresholded subtitle retrieval and manual qualitative coding, to estimate the scale and content of influencer VPN ads on YouTube (pp. 1, 3-5). [🤖]

## Research Question

How widespread are influencer VPN ads on YouTube, where do they appear, what claims do they make about privacy and security, and how consistently are sponsorships disclosed? (pp. 1-2). [🤖]

## Data, Sample, Geography, and Period

- **Data:** YouTube video metadata from Random Prefix Sampling, detailed metadata and English subtitles for higher-view videos, manually coded VPN-ad videos, and promotional materials supplied by SurfShark for a case study (pp. 1, 3-4, 12-13). [🤖]
- **Sample:** The initial representative sample contains 86.3 million videos, about 1.4% of YouTube, with more than 603.5 billion rounded views; the deeper "10M dataset" contains 10.7 million videos with at least 800 views and 606.0 billion exact views; the final VPN-ad sample contains 243 videos with 62.7 million views (pp. 3-5). [🤖]
- **Geography:** The sampling frame is platform-level rather than country-bounded, but the content-analysis stage depends on available English subtitles and therefore is not language-universal (pp. 3-5). [🤖]
- **Period:** Data were collected from August 2020 through March 2021, and the identified VPN ad videos run from late 2016 to mid-2020 (pp. 3, 5). [🤖]

## Methods

The authors use Random Prefix Sampling by generating random five-character prefixes and querying YouTube for `watch?v=<prefix>-`, following Zhou et al.'s prefix-sampling method to retrieve videos from the ID space rather than from keywords or related-video links (pp. 3-4). [🤖]

They validate their implementation against a 2016 modified random YouTube sample by checking whether those known videos were still reachable in the prefix space; 51.7K of 54.0K videos were found, giving 95.8% coverage with an Agresti-Coull confidence interval of .956-.959 (p. 4). [🤖]

The design then narrows the estimand: the authors collect richer metadata only for videos with at least 800 views, retrieve English subtitles where available, search subtitles for "VPN", and manually code a candidate set to identify influencer VPN ads (pp. 3-5). [🤖]

For qualitative analysis, the authors construct a threat-model codebook, independently code 175 videos during reliability assessment, report Krippendorff's alpha of .852, and then analyze the 243 retained VPN-ad videos for claims, companies, categories, disclosure, and advertising techniques (pp. 4-5). [🤖]

## Main Findings

1. The study identifies 243 influencer VPN ad videos with 62.7 million views in the filtered analysis set; when scaled to YouTube, the authors estimate 17,127 VPN-ad videos with a 95% confidence interval of 15,136-19,381, and about 4.4 billion views (pp. 1, 5). [🤖]
2. The RPS baseline is very large by published YouTube-research standards: 86.3 million videos, or about 1.4% of YouTube, before the deeper view and subtitle filters are applied (pp. 1, 3-4). [🤖]
3. The content-analysis stage is not a uniform random sample of all YouTube videos because it is restricted to videos with at least 800 views and, for detection, to videos with available English subtitles; the authors frame resulting counts as lower bounds and note limited generalizability to low-view or non-English videos (pp. 3-5). [🤖]
4. VPN ads frequently make broad security guarantees and technical claims: 171 videos with 45.6 million views include broad guarantees, while 154 videos with 43.5 million views use absolute terms or overstate anonymity (pp. 6-7). [🤖]
5. Disclosure is incomplete: 188 videos with 59.4 million views have disclosures the authors treat as at least somewhat guideline-compliant, while 55 videos with 3.3 million views do not; 13 disclose only in the description and 42 include affiliate links without explicit disclosure (pp. 11-12). [🤖]
6. The company/channel pattern is heterogeneous: VirtualShield appears in right-wing or conspiratorial channels in this dataset, while SurfShark ads are especially likely to mention accessing content, showing that VPN advertising is not a single uniform creator-economy practice (pp. 10-11). [🤖]

## Limitations / Scope Conditions

The initial RPS scrape is the strongest denominator evidence, but the substantive VPN-ad analysis is conditioned on the 800-view threshold and English subtitle availability, so it should not be cited as a uniform prevalence estimate for all YouTube videos (pp. 3-5). [🤖]

The authors describe their count estimates as lower bounds because the subtitle search and filtering strategy can miss VPN ads without subtitles, without the term "VPN" in subtitles, or outside the filtered population (pp. 4-5). [🤖]

The SurfShark promotional-material analysis is a single-company case study because only SurfShark shared materials, while most other VPN providers did not respond or did not provide equivalent guidance (p. 12). [🤖]

## Temporal Scope

This is a pre-Shorts-dominance and pre-2025 Shorts-view-counting study built from an August 2020-March 2021 collection window and VPN ads posted from late 2016 through mid-2020 (pp. 3, 5). [🤖]

## Key Quotes

> "random sample of about 86 million videos" (p. 1). [🤖]

> "at least 800 views each" (p. 1). [🤖]

## Relation to This Project

- **Methods companion:** Strong precedent for high-scale RPS, but also a warning that downstream filtering can change the estimand from a uniform public-video sample to a visibility- and language-conditioned sample. [PROJECT] [🤖]
- **Paper 1 (attention economy):** Useful mainly as an example of how rare-content prevalence and attention can diverge when the substantive analysis is conditioned on higher-view videos. [PROJECT] [🤖]
- **Paper 2 (mobility):** Minimal direct relevance except as evidence that creator monetization and sponsorship practices vary across channel niches. [PROJECT] [🤖]
- **Later studies:** Relevant to `classification-llm` because it combines probability sampling, search-based candidate generation, manual coding, and explicit reliability assessment for a rare content class. [PROJECT] [🤖]

## Linked Claims

- `claim_descriptive_deficit_thresholded_rps_changes_estimand`
- `claim_creator_economy_vpn_ads_are_widespread_but_incompletely_disclosed`

## Cross-References

- **Themes:** [[descriptive_deficit]], [[creator_economy]]
- **Methods:** [[random_video_sampling]]
- **Debates:** _(none yet)_
- **Related sources:** [[mcgrady_2023]], [[mcgrady_2025]]
