---
source_id: hussein_et_al_2020
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Measuring Misinformation in Video Search Platforms: An Audit Study on YouTube"
authors:
  - "Hussein, Eslam"
  - "Juneja, Prerna"
  - "Mitra, Tanushree"
year: 2020
venue: "Proceedings of the ACM on Human-Computer Interaction 4(CSCW1), Article 48"
doi: "10.1145/3392854"
temporal_scope: "Audit experiments published in May 2020 on then-current YouTube search, Up Next, and Top 5 recommendation outputs; exact crawl dates are not emphasized in the main text"
themes:
  - recommendation-radicalization
project_modules:
  - public-affairs
census_papers:
  - methods-companion
  - paper1-attention-economy
  - study3-media-system
census_relevance: high
verification:
  machine_extracted: 17
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Hussein, Juneja, and Mitra (2020) - Misinformation in YouTube Search

## Full Citation

Hussein, Eslam, Prerna Juneja, and Tanushree Mitra. 2020.
"Measuring Misinformation in Video Search Platforms: An Audit
Study on YouTube." *Proceedings of the ACM on Human-Computer
Interaction* 4(CSCW1), Article 48.
https://doi.org/10.1145/3392854.

## One-Sentence Contribution

Auditing YouTube across five misinformation topics, the paper shows
that misinformation exposure is pathway-specific: search results,
Up-Next, and Top 5 recommendations behave differently, and
personalization effects grow once watch history develops (pp. 48:1-3,
48:21-23). [🤖]

## Research Question

How much misinformation appears in YouTube search and recommendation
outputs across different topics, and how do user demographics,
geolocation, and watch history affect that exposure? (pp. 48:1-3,
48:11-13) [🤖]

## Data, Sample, Geography, and Period

- **Data:** The audit collects search results, Up-Next, and Top 5 recommendation outputs for five misinformation topics and codes 2,943 unique videos for stance as promoting, neutral, or debunking misinformation (pp. 48:1-3, 48:11-13). [🤖]
- **Sample:** Across the experiments, the study gathers 56,475 videos, using eight demographic accounts for search audits, 24 accounts per topic for watch-history audits, and additional geolocation-specific account sets (pp. 48:1-3, 48:11-13). [🤖]
- **Geography:** The paper varies geolocation experimentally rather than focusing on a single country, but it does not present the audit as a global census of all regional recommendation regimes (pp. 48:11-13). [🤖]
- **Period:** The results describe YouTube's search and recommendation behavior as observed before the paper's May 2020 publication, making this evidence a late-2010s / early-2020 benchmark rather than a statement about later policy regimes or Shorts-era YouTube (pp. 48:1-3, 48:21-23). [🤖]

## Methods

The authors shortlist five misinformation topics, build query sets for
each, and then run four audit designs: search audits on brand-new
accounts varying age, gender, and geolocation, plus watch-history
audits in which accounts repeatedly watch promoting or debunking
content before collecting search results, Up-Next recommendations, and
Top 5 recommendation panels for comparison (pp. 48:11-13). [🤖]

## Main Findings

1. For brand-new accounts, demographic attributes and geolocation do not meaningfully change how much misinformation appears in returned search results, which suggests weak personalization effects at the search stage before history accumulates (pp. 48:1-3, 48:14-17). [🤖]
2. Once users develop watch histories, personalization matters much more for recommendations: Up-Next and Top 5 outputs often reflect filter-bubble dynamics that reinforce previously watched misinformation-promoting videos (pp. 48:1-3, 48:17-22). [🤖]
3. The effect is topic-specific rather than uniform. Vaccine-related results behave differently from several other misinformation topics, with more debunking content surfacing in recommendations even while search results still show important exposure risks (pp. 48:1-3, 48:17-22). [🤖]
4. The study therefore argues that YouTube's misinformation problem cannot be reduced to one interface or one algorithmic surface, because search, Up-Next, and Top 5 recommendations each contribute differently to exposure pathways (pp. 48:21-23). [🤖]

## Limitations / Scope Conditions

This is an audit of platform outputs rather than a study of realized
user watching, so it identifies exposure opportunities without showing
which videos people ultimately choose to click or ignore (pp. 48:11-13,
48:22-23). [🤖]

The experiments use a small number of controlled accounts and five
selected misinformation topics, which makes the design strong for
mechanism testing but weaker as a platform-wide estimate of all
misinformation on YouTube (pp. 48:11-13, 48:22-23). [🤖]

Because the archived file is the PACM HCI / CSCW1 version and not the
prompt's WWW 2020 citation, the source card is keyed to the archived
article actually in the corpus; findings should be cited from this
version's pagination and phrasing. [🤖]

## Temporal Scope

This source belongs to the late-2010s / early-2020 transition window.
It predates later post-2019 real-user and intervention studies, but it
adds an important exposure mechanism that the atlas previously lacked:
search can be a distinct route into problematic content, and search and
recommendations should not be analytically collapsed into one pathway
(pp. 48:1-3, 48:21-23). [🤖]

## Key Quotes

> "once a user develops a watch history, these attributes do affect the extent of misinformation recommended to them." (p. 48:1) [🤖]

> "Further analyses reveal a filter bubble effect, both in the Top 5 and Up-Next recommendations" (p. 48:1) [🤖]

## Relation to This Project

- **Methods companion:** Useful because it separates search, Up-Next, and Top 5 recommendation surfaces instead of treating "the algorithm" as one interface. [PROJECT]
- **Paper 1 (attention economy):** Relevant for showing that exposure to problematic content can happen through search as well as recommendations. [PROJECT]
- **Paper 2 (mobility):** No direct relevance beyond reminding us that discovery mechanisms matter before any creator or audience trajectories are observed. [PROJECT]
- **Later studies:** Important bridge into [[filter_bubble_evidence]] because it adds a search-side pathway to a literature otherwise dominated by recommendation audits and real-user behavior studies. [PROJECT]

## Linked Claims

- `claim_recommendation_radicalization_search_and_recommendation_misinformation_pathways_are_topic_specific`

## Cross-References

- **Themes:** [[recommendation_radicalization]]
- **Methods:** [[recommendation_audit]]
- **Debates:** [[filter_bubble_evidence]], [[pre_2019_vs_post_2019_algorithm]]
- **Related sources:** [[faddoul_et_al_2020]], [[haroon_et_al_2023]], [[huang_yang_2024]]
