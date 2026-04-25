---
source_id: rieder_et_al_2025
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Forgetful by Design? A Critical Audit of YouTube's Search API for Academic Research"
authors:
  - "Rieder, Bernhard"
  - "Padilla, Adrián"
  - "Coromina, Òscar"
year: 2025
venue: "Information, Communication & Society"
doi: "10.1080/1369118X.2025.2591767"
temporal_scope: "Weekly YouTube Data API v3 searches over six months starting April 2024; observation windows begin October 15, 2023, with a European Parliament election case covering May 9-June 9, 2024"
themes:
  - governance-data-access
  - descriptive-deficit
project_modules:
  - api-compliance
  - discovery-completeness
census_papers:
  - methods-companion
census_relevance: high
verification:
  machine_extracted: 25
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-24
---

# Rieder et al. (2025) - Forgetful by Design?

## Full Citation

Rieder, Bernhard, Adrián Padilla, and Òscar Coromina. 2025. "Forgetful by Design? A Critical Audit of YouTube's Search API for Academic Research." *Information, Communication & Society*, 1-20. https://doi.org/10.1080/1369118X.2025.2591767

## One-Sentence Contribution

This paper audits YouTube Data API v3 search and shows that search-based data collection can lose large portions of still-available videos within weeks, return different samples for identical queries, and vary substantially by ranking parameter (pp. 1, 9-21). [🤖]

## Research Question

How do YouTube Data API search ranking parameters, temporal distance from publication, and repeated extractions affect the completeness, representativeness, consistency, and research usability of search-based YouTube samples? (pp. 3, 7-9). [🤖]

## Data, Sample, Geography, and Period

- **Data:** YouTube Data API v3 search results collected with YouTube Data Tools using a one-search-per-day strategy and eleven quoted queries spanning health, politics, public affairs, and popular culture topics (pp. 7-9). [🤖]
- **Sample:** The audit repeatedly searched eleven queries, including `Andrew Tate`, `European Parliament election`, `Gaza ceasefire`, `Mukbang`, `Obesity`, and `Ukraine war`; Table 1 reports per-query returned-video counts from 4,629 to 254,098 depending on query and ranking parameter (pp. 8-10). [🤖]
- **Geography:** The study is not a country-representative YouTube sample; its queries center on globally visible public issues and a European Parliament election case study (pp. 8-9, 16-18). [🤖]
- **Period:** Searches began in April 2024, used October 15, 2023 as the starting date for publication windows, and continued weekly for six months; the election case searches were spaced five weeks apart after June 10, 2024 (pp. 8, 16). [🤖]

## Methods

The audit uses the `one-search-per-day` approach to work around the search endpoint's 500-results-per-query cap: a longer period is cut into daily intervals, and each day receives a separate API call (pp. 7-8). [🤖]

The authors compare the API's `relevance` and `date` order parameters, then operationalize precision by checking whether query text appears in video titles, descriptions, or tags (pp. 8-10). [🤖]

They evaluate temporal decay by rerunning the same queries on different search dates while holding the publication window constant, and they evaluate consistency by comparing repeated searches over the same timeframe one week apart (pp. 11-15). [🤖]

## Main Findings

1. Ranking parameters yield very different retrieval sets: in Table 1, `relevance` retrieved many more videos than `date` for most queries, but precision was lower for `relevance` in every query (pp. 9-10). [🤖]
2. The `European Parliament election` query illustrates the ranking gap sharply: `relevance` returned 72,767 videos with 17.2% precision, while `date` returned 8,933 videos with 57.6% precision before keyword filtering (pp. 9-10). [🤖]
3. Search results decayed rapidly with temporal distance: the authors identify an approximately 20-day high-retrieval head, a roughly 40-day middle phase, and a low-volume tail, even though many videos remained on YouTube (pp. 11-13). [🤖]
4. Repeated identical searches were unstable: for `Mukbang`, a relevance search found 2,407 videos in the first week, then a week later retained only 775 from the first extraction while adding 1,510 newly observed videos for the same publication window (p. 14). [🤖]
5. In the European Parliament election case, waiting five weeks after the first post-election search reduced keyword-filtered relevance results from 2,105 to 1,246, and waiting ten weeks reduced them to 500 (pp. 16-17). [🤖]
6. The case study also found that temporal loss affected high-view videos: of the top ten most-viewed videos in the first election search, only five remained findable after later searches, although all ten were still manually available on YouTube (pp. 18-19). [🤖]

## Limitations / Scope Conditions

The authors explicitly limit generalizability because the audit uses eleven queries, a six-month observation period, and metadata fields rather than unavailable content features such as transcripts (p. 19). [🤖]

The findings are strongest for research designs that use YouTube Data API search to reconstruct videos published around topics or events; studies of what search presents at a single moment may be less affected by temporal decay, though still exposed to ranking and consistency problems (pp. 19-20). [🤖]

This paper audits the official Data API search endpoint, not InnerTube/DFV directly. It is nevertheless relevant to ID-space and search-based sampling because it shows how search interfaces can introduce retrievability and temporal-stability problems that are not visible from API documentation alone (pp. 6-7, 19-21). [🤖]

## Temporal Scope

The empirical evidence is a 2024 audit of YouTube Data API v3 search behavior, published as a 2025 article. It should not be projected backward onto older API regimes without qualification, and it should be rechecked if YouTube changes search behavior or researcher-access tooling (pp. 1, 7-9, 21). [🤖]

## Key Quotes

> "the number of retrievable videos for a given period drops dramatically within just 20-60 days" (p. 1). [🤖]

> "identical queries for the same topic can yield different outputs over time" (p. 19). [🤖]

## Relation to This Project

- **Methods companion:** Central warning that official search-based collection does not guarantee temporal completeness, repeatability, or stable ranking behavior. [PROJECT] [🤖]
- **Paper 1 (attention economy):** Indirect relevance because topic/event samples collected late may understate visible supply and distort peak timing, but the paper does not measure attention shares directly. [PROJECT] [🤖]
- **Paper 2 (mobility):** Limited direct relevance unless mobility designs rely on search-based reconstruction of event or issue videos. [PROJECT] [🤖]
- **Later studies:** Directly relevant to API-compliance and DSA-facing arguments about whether YouTube's researcher program and Data API support robust independent auditing. [PROJECT] [🤖]

## Linked Claims

- `claim_descriptive_deficit_infrastructure_constraints`
- `claim_governance_data_access_youtube_search_api_temporal_decay`

## Cross-References

- **Themes:** [[governance_data_access]], [[descriptive_deficit]]
- **Methods:** [[random_video_sampling]]
- **Debates:** _(none yet)_
- **Related sources:** [[rieder_2020]], [[rieder_et_al_2023]], [[mcgrady_2023]], [[zhou_et_al_2011]]
