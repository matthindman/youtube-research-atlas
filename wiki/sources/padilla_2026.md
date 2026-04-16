---
source_id: padilla_2026
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Networks beyond the links: Methodological challenges in mapping YouTube communities"
authors:
  - "Padilla, Adrián"
year: 2026
venue: "First Monday 31(1)"
doi: "10.5210/fm.v31i1.14633"
temporal_scope: "Video retrieval covers January 1, 2010-January 1, 2025; the channel-relation crawl reflects a late-2025 snapshot of public subscriptions and featured-channel visibility"
themes:
  - descriptive-deficit
project_modules:
  - discovery-completeness
  - taxonomy
  - api-compliance
census_papers:
  - methods-companion
  - study3-media-system
census_relevance: high
verification:
  machine_extracted: 19
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Padilla (2026) - Networks Beyond the Links

## Full Citation

Padilla, Adrián. 2026. "Networks beyond the links: Methodological
challenges in mapping YouTube communities." *First Monday* 31(1),
January. https://doi.org/10.5210/fm.v31i1.14633

## One-Sentence Contribution

Using the GNU/Linux creator ecosystem as a case, the paper develops a
mixed-methods framework for YouTube community mapping that shows how
search API biases and sparse public relational data force researchers to
combine partial formal traces with qualitative boundary judgments (pp.
1, 6-8, 18). [🤖]

## Research Question

How can researchers identify, size, map, and interpret a specific
YouTube creator community when the platform exposes only limited
relational data and when formal links alone may not capture meaningful
community boundaries (pp. 2, 6)? [🤖]

## Data, Sample, Geography, and Period

- **Data:** Keyword-based YouTube Search API retrieval, title/description
  keyword matching, and relational crawls through the
  `subscriptions:list` and `channelSections:list` endpoints for public
  subscriptions and featured channels (pp. 7-8). [🤖]
- **Sample:** The workflow retrieved 300,649 videos, retained 153,795
  keyword-matching videos, identified 62,092 unique channels, and then
  found 24,773 channels with at least one public subscription or
  featured-channel tie feeding a 1.32M-node graph (pp. 9-15, 18). [🤖]
- **Geography:** The case is the GNU/Linux creator ecosystem on YouTube
  rather than a single national market; the search-and-crawl design is
  platform-wide and not country-bounded in its sampling logic (pp. 2,
  7-8). [🤖]
- **Period:** Video retrieval spans January 1, 2010 through January 1,
  2025, while the relational crawl reflects the state of public channel
  fields at collection time rather than a historical tie archive (pp.
  7-8, 12). [🤖]

## Methods

Padilla proposes a five-step mixed-methods workflow: identify cultural
markers, collect videos with the Search API, clean the dataset with
keyword matching, crawl formal relations, and then compare alternative
graph-filtering strategies to delimit the community (pp. 6-8). [🤖]

The design is explicitly reflexive rather than fully automated. The
paper treats community boundaries as a research-design choice, comparing
strict, open, and productive filtering strategies instead of assuming
that one observed graph is self-evidently the community (pp. 15-18).
[🤖]

## Main Findings

1. The case study identifies 62,092 channels that published GNU/Linux-
   related content over a 15-year period, showing that YouTube
   community mapping can operate at substantial scale even outside the
   usual political domain (pp. 1, 10, 18). [🤖]
2. Search-based channel discovery is structurally noisy: only 51.15% of
   retrieved videos survived the keyword-matching filter, and the paper
   warns that older content may remain underreturned even when query
   windows stay below the API's 500-result cap (pp. 8-10). [🤖]
3. Public relational data are sparse enough to materially limit channel
   mapping. In the final dataset, 60.08% of channels exposed neither
   public subscriptions nor featured channels, and only 39.89% exposed
   at least one of those relation types (pp. 12, 18). [🤖]
4. Featured channels appear more community-internal than subscriptions:
   only 2.71% of subscription edges pointed to seed channels, versus
   11.95% of featured-channel edges, which makes strict filtering the
   paper's clearest community-isolation strategy (pp. 14-16). [🤖]

## Limitations / Scope Conditions

The discovery pipeline inherits Search API bias. The paper notes both
irrelevant results returned by algorithmic affinity and the likely
underretrieval of older videos, which means the initial channel set is
not a neutral census of GNU/Linux YouTube (pp. 8-10). [🤖]

Most detected channels contribute very little visible GNU/Linux content:
72.06% contributed only one video to the filtered dataset, which makes
community-membership thresholds analytically consequential rather than
obvious (pp. 10-11). [🤖]

Relational inference is sharply limited because most channels do not
expose subscriptions or featured channels, and because even visible
links may reflect personal media habits or visibility strategy rather
than meaningful community affiliation (pp. 3, 12-15, 18). [🤖]

The largest open graph is hard to interpret substantively: more than 1.3
million nodes and 3 million edges still do not guarantee socially
meaningful communities, because the social value of the links remains
questionable even when they are computationally tractable (pp. 15-18).
[🤖]

## Temporal Scope

This source is best read as a mid-2020s methodological snapshot of what
YouTube community mapping could still do with Search API access plus the
remaining public subscriptions and featured-channel surface. It is not a
claim that current YouTube offers rich relational visibility; the paper
instead treats hidden or unstable public links as one of the core
constraints on current research design (pp. 2-3, 7-8, 18). [🤖]

## Key Quotes

> "Results reveal structural limitations in YouTube's API —
> particularly the scarcity and opacity of relational data ..." (p. 1)
> [🤖]

> "over 60 percent of channels disclosed no formal relational data"
> (p. 18) [🤖]

## Relation to This Project

- **Methods companion:** Directly relevant because it shows how
  community and channel mapping on YouTube now depends on partial public
  traces, search-system behavior, and explicit boundary-setting
  decisions. [PROJECT]
- **Paper 1 (attention economy):** Indirectly relevant as a reminder
  that even large channel maps can be shaped by search and visibility
  biases before any substantive interpretation begins. [PROJECT]
- **Paper 2 (mobility):** Limited direct relevance because the design is
  cross-sectional and methodological rather than about creator
  trajectories. [PROJECT]
- **Later studies:** Important bridge source for the
  `channel_classification` methods page because it expands the methods
  discussion beyond political YouTube and beyond purely link-based
  classification. [PROJECT]

## Linked Claims

- `claim_descriptive_deficit_infrastructure_constraints`
- `claim_descriptive_deficit_partial_relational_data_channel_mapping`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** [[channel_classification]]
- **Debates:** _(none yet)_
- **Related sources:** [[rieder_2020]], [[boesinger_et_al_2024]], [[zaitsev_clark_2025]]
