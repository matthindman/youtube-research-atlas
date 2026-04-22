---
source_id: borghol_et_al_2012
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "The untold story of the clones: content-agnostic factors that impact YouTube video popularity"
authors:
  - "Borghol, Youmna"
  - "Ardon, Sebastien"
  - "Carlsson, Niklas"
  - "Eager, Derek"
  - "Mahanti, Anirban"
year: 2012
venue: "Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '12)"
doi: "10.1145/2339530.2339717"
temporal_scope: "Historical early-2010s YouTube clone-set data collected with public API fields, HTML scraping, and still-visible insight traces"
themes:
  - descriptive-deficit
project_modules:
  - activity-tail
  - discovery-completeness
census_papers:
  - methods-companion
  - paper1-attention-economy
census_relevance: medium
verification:
  machine_extracted: 18
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-17
---

# Borghol et al. (2012) - The Untold Story of the Clones

## Full Citation

Borghol, Youmna, Sebastien Ardon, Niklas Carlsson, Derek Eager, and
Anirban Mahanti. 2012. "The untold story of the clones: content-agnostic
factors that impact YouTube video popularity." In *Proceedings of the
18th ACM SIGKDD International Conference on Knowledge Discovery and Data
Mining (KDD '12)*, 1186-1194. https://doi.org/10.1145/2339530.2339717

## One-Sentence Contribution

Using 48 sets of near-identical YouTube video clones, the paper shows
that popularity is strongly shaped by cumulative views, video age, first
mover advantage, and search discovery, which makes it a foundational
historical source on how non-content factors helped concentrate visible
attention on YouTube (pp. 1186-1193). [🤖]

## Research Question

When videos with essentially the same content compete on YouTube, which
content-agnostic factors most strongly shape their popularity, and how
much of apparent success reflects cumulative advantage rather than
content quality differences? (pp. 1186-1187) [🤖]

## Data, Sample, Geography, and Period

- **Data:** The study combines YouTube API fields, HTML scraping, and
  historical "insight data" on view trajectories and referrers for near-
  identical videos (pp. 1187-1188). [🤖]
- **Sample:** The authors manually identified 48 clone sets containing
  1,761 videos, with clone-set sizes ranging from 17 to 94 and a median
  size of 29.5 videos (p. 1187). [🤖]
- **Geography:** The design is platform-level rather than country-
  specific; the paper does not frame the sample as a national YouTube
  subsystem (pp. 1186-1188). [🤖]
- **Period:** This is an early-2010s YouTube study conducted when
  uploader followers, historical insight traces, and detailed referrer
  signals were still publicly collectable through API and scraping
  methods (pp. 1187-1188, 1191-1192). [🤖]

## Methods

The core design is content-controlled comparison. By grouping nearly
identical videos into clone sets, the paper uses multivariate linear
regression and related statistical tests to estimate how age, prior
views, uploader characteristics, keywords, and discovery paths shape
popularity when content is held roughly constant (pp. 1186-1189). [🤖]

The study also uses historical view traces and referrer data to test
rich-get-richer dynamics, first-mover advantage, and the relative role
of search, related-video, mobile, and external discovery channels (pp.
1190-1193). [🤖]

## Main Findings

1. When content differences are controlled through clone sets, current
   popularity follows a strong linear rich-get-richer pattern in which
   accumulated views are the dominant predictor except for very young
   videos (pp. 1186-1188, 1190-1191). [🤖]
2. First-mover timing matters: in the observed clone sets, the eventual
   winner was the first uploaded video 27.1% of the time and among the
   first five uploads 60.4% of the time; for search discovery, winners
   were first found through search 66.7% of the time and among the first
   five in 92% of cases with insight data (p. 1191). [🤖]
3. Search is a particularly powerful concentration mechanism. The most
   popular clones received substantially larger fractions of their views
   from search than their less successful counterparts, suggesting that
   early search prominence can amplify later popularity (pp. 1192-1193).
   [🤖]
4. Aggregate analyses that ignore clone identity misstate the drivers of
   popularity by overstating the role of age and uploader followers and
   understating how strongly prior views dominate once content is held
   constant (pp. 1188-1190). [🤖]

## Limitations / Scope Conditions

The sample is not a representative census of YouTube. It consists of
manually identified clone sets, which are ideal for isolating non-
content factors but cannot show how often these dynamics apply across
the platform as a whole (pp. 1187-1188, 1193-1194). [🤖]

The data environment is historically specific. The paper depends on
public API statistics, HTML scraping, and YouTube "insight data" that
later researchers could not access so easily, so the method should be
read as evidence about what was measurable on early-2010s YouTube, not
as a turnkey current pipeline (pp. 1187-1188, 1191-1192). [🤖]

Because the paper studies popularity among near-identical uploads, it is
best suited to content-agnostic mechanisms such as first-mover timing
and search prominence, not to claims about topic-specific recommendation
effects or audience ideology (pp. 1186-1187, 1193-1194). [🤖]

## Temporal Scope

This source is most useful as a historical baseline for early-2010s
YouTube attention dynamics, when public view counts, uploader follower
counts, referrer traces, and insight graphs exposed more of the
platform's popularity machinery than current public interfaces do (pp.
1187-1188, 1191-1192). [🤖]

## Key Quotes

> "Rich-get-richer behavior may result in part from a 'first mover'
> advantage." (p. 1191) [🤖]

> "Clearly, there is a significant advantage to being first mover."
> (p. 1191) [🤖]

## Relation to This Project

- **Methods companion:** Useful for the paper's historically grounded
  demonstration that visible popularity is shaped by cumulative
  advantage and discovery pathways, not just by content differences.
  [PROJECT]
- **Paper 1 (attention economy):** Directly relevant because it offers a
  peer-reviewed mechanism for early attention concentration and
  incumbency without claiming that the result is a full platform-wide
  census. [PROJECT]
- **Paper 2 (mobility):** No direct relevance. [PROJECT]
- **Later studies:** Best read alongside later descriptive work as a
  reminder that older YouTube exposed richer popularity traces than the
  current public environment. [PROJECT]

## Linked Claims

- `claim_descriptive_deficit_first_mover_and_search_bias_concentrate_views`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** _(none yet)_
- **Debates:** _(none yet)_
- **Related sources:** [[rieder_2020]]
