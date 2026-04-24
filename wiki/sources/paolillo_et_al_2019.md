---
source_id: paolillo_et_al_2019
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "A Network View of Social Media Platform History: Social Structure, Dynamics and Content on YouTube"
authors:
  - "Paolillo, John C."
  - "Ghule, Sharad"
  - "Harper, Brian P."
year: 2019
venue: "Proceedings of the 52nd Hawaii International Conference on System Sciences"
doi: null
temporal_scope: "YouTube videos and channel relations covering May 2005-December 2016; search/browse/crawl collection repeated July 2015-March 2017"
themes:
  - descriptive-deficit
project_modules:
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

# Paolillo et al. (2019) - YouTube Content History

## Full Citation

Paolillo, John C., Sharad Ghule, and Brian P. Harper. 2019. "A Network View of Social Media Platform History: Social Structure, Dynamics and Content on YouTube." *Proceedings of the 52nd Hawaii International Conference on System Sciences*. URI: https://hdl.handle.net/10125/59701

## One-Sentence Contribution

This paper builds a large historical network of YouTube channels, videos, likes, and favorites to interpret genre evolution from early YouTube through 2016, while explicitly acknowledging that the sample is a biased connected crawl rather than a representative platform frame (pp. 1-3, 9). [🤖]

## Research Question

Can liked/favorited-video relations among channels, dated by video publication time, be used to reconstruct a history of genre evolution and content structure on YouTube? (pp. 1-3). [🤖]

## Data, Sample, Geography, and Period

- **Data:** Channel IDs gathered through search and browsing, then expanded with the YouTube public Data API through channel upload, liked-video, and favorited-video playlists (p. 2). [🤖]
- **Sample:** The repeated search/browse/crawl process ended with 76,081,372 videos and 549,383 channels; the authors describe the resulting database as a small, popular, highly connected fraction of YouTube activity (p. 2). [🤖]
- **Geography:** The paper is not country-bounded and analyzes English-dominant entertainment and politics streams as well as Spanish, Brazilian Portuguese, and Russian language-market clusters (pp. 6-9). [🤖]
- **Period:** The historical network slices run from May 2005 to December 2016, while search/browse/crawl collection was repeated from July 2015 to March 2017 (pp. 1-2). [🤖]

## Methods

The sampling procedure began with channel IDs collected during a 2015 conspiracy-theory project, then broadened through additional YouTube searches, manual browsing, and API crawling of uploads, likes, and favorites (p. 2). [🤖]

The channel network treats likes and favorites as directed channel-to-channel links when one channel likes or favorites videos uploaded by another; video publication dates are used as proxies for dating those relations historically (p. 3). [🤖]

The authors construct 141 overlapping three-month network samples from April 2005 through December 2016, using a minimum threshold of 10 likes/favorites from one channel to another within a sample before including a link (p. 3). [🤖]

They cluster each sample with Louvain modularity methods, then compare clusters across adjacent samples to trace cluster continuity, splits, merges, and content streams over time (pp. 3-4). [🤖]

## Main Findings

1. The resulting network has a stable central YouTube core across the platform's history, but the composition of that core changes over time as genres and clusters shift (p. 4). [🤖]
2. The 24 largest cross-sample clusters account for 75.9% of the network's nodes, making the paper's substantive interpretation heavily oriented toward large, connected parts of the crawl (p. 3). [🤖]
3. The authors identify two major English-language streams after early YouTube: a larger, fluid entertainment stream and a more stable politics stream descending partly from earlier news/political content (pp. 6-8). [🤖]
4. Platform and external events appear to structure the timeline: examples include Vevo and Content ID changes, the shift toward watch time, the relaxation of video-length restrictions, the emergence of GoPro-style point-of-view content, and U.S. presidential-election cycles (pp. 6-9). [🤖]
5. The politics stream contains news and conspiracy-theory channels, with RT and Al Jazeera English especially integrated into that stream in the authors' network view (p. 8). [🤖]
6. The paper identifies major Spanish, Brazilian Portuguese, and Russian language-market clusters beginning around mid-2011, while noting that additional language clusters may fall below the authors' qualitative interpretation threshold (pp. 8-9). [🤖]

## Limitations / Scope Conditions

This is not a representative sample of YouTube. The authors state that search and browsing features are subject to unknown biases, that individual videos cannot be sampled in a truly random manner through those interfaces, and that crawled samples miss unconnected components (p. 2). [🤖]

The crawl requires channel-first discovery and therefore misses profiles that do not post videos; private subscriptions, private likes/favorites, and non-posting channels are structurally hard to observe through the authors' API pathway (p. 2). [🤖]

The authors explicitly describe the database as a small, popular, highly connected fraction of YouTube, which makes it stronger for historical network interpretation than for platform-wide descriptive prevalence claims (p. 2). [🤖]

The paper also notes uncertainty from seed-channel choice, possible recency effects near the end of the sample, and losses from videos or channels deleted for copyright, decay, or censorship; the authors say complete remedies would require Google/YouTube internal data unavailable to most researchers (p. 9). [🤖]

## Temporal Scope

This is a historical YouTube-network study, strongest for 2005-2016 genre evolution and for documenting pre-2019 API/crawl affordances. It should not be used as evidence about current YouTube, Shorts-era content, or platform-wide prevalence without additional support (pp. 1-3, 9). [🤖]

## Key Quotes

> "small but popular and highly connected fraction" (p. 2). [🤖]

> "incomplete picture of the platform" (p. 9). [🤖]

## Relation to This Project

- **Methods companion:** Useful as a contrast case for search/browse/crawl designs: it reconstructs historical network structure but does not provide a defensible denominator or random sampling frame. [PROJECT] [🤖]
- **Paper 1 (attention economy):** Low direct relevance; it helps identify historical genre and political-stream shifts but cannot support platform-wide attention-share estimates. [PROJECT] [🤖]
- **Paper 2 (mobility):** Minimal direct relevance. [PROJECT] [🤖]
- **Later studies:** Important mainly because Rieder et al. 2020 use this type of study as an example of why crawled/search-started YouTube histories need explicit bias accounting before they can be treated as comprehensive. [PROJECT] [🤖]

## Linked Claims

- `claim_descriptive_deficit_hybrid_crawls_are_historically_rich_but_not_representative`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** [[random_video_sampling]]
- **Debates:** _(none yet)_
- **Related sources:** [[rieder_2020]], [[mcgrady_2023]]
