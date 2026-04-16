---
source_id: zaitsev_clark_2025
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Classifying YouTube Channels: Algorithmic Approach to Channel Mapping"
authors:
  - "Zaitsev, Anna"
  - "Clark, Sam"
year: 2025
venue: "First Monday 30(8)"
doi: "10.5210/fm.v30i8.13682"
temporal_scope: "Data collected in 2020 using then-visible public subscription pages; analysis maps English-language political YouTube and reports 2017-2020 view trends"
themes:
  - descriptive-deficit
project_modules:
  - discovery-completeness
  - classification-llm
  - public-affairs
census_papers:
  - methods-companion
  - study3-media-system
census_relevance: high
verification:
  machine_extracted: 18
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Zaitsev and Clark (2025) - Classifying YouTube Channels

## Full Citation

Zaitsev, Anna, and Sam Clark. 2025. "Classifying YouTube Channels:
Algorithmic Approach to Channel Mapping." *First Monday* 30(8), August.
https://doi.org/10.5210/fm.v30i8.13682

_Citation convention: this `First Monday` source is effectively an
online-only article, so citations use section headings rather than fixed
page numbers._

## One-Sentence Contribution

The paper introduces `chan2vec`, a public-subscription-based channel
discovery and classification pipeline that maps English-language
political YouTube at much larger scale than prior head-focused studies
while also showing that the underlying subscription visibility regime
has since narrowed (§ III.2; § VI; § VII). [🤖]

## Research Question

Can commenter-subscription embeddings and KNN classification discover
and classify socio-political YouTube channels at platform scale more
effectively than prior seed-based or keyword-based approaches, and what
does that larger map reveal about 2020 political YouTube (§ I; § III; §
VI)? [🤖]

## Data, Sample, Geography, and Period

- **Data:** YouTube Data API queries for recent videos and comments,
  publicly visible commenter subscription pages, labeled Recfluence and
  Laukemper datasets, Social Blade annual view counts, and an MBFC
  comparison set for political-lean prediction (§ III.2; Appendix B-E).
  [🤖]
- **Sample:** The discovery process surfaced 12.6M total channels, 1.6M
  with at least five commenter subscriptions, 600k with at least 10,000
  subscriptions, roughly 25,000 candidate socio-political channels, and
  7,224 final socio-political channels matching the paper's criteria (§
  III; § VI; Appendix C). [🤖]
- **Geography:** The mapped corpus is English-language socio-political
  YouTube, not a multilingual or platform-wide census; the appendix's
  language filter removes 362 non-English channels from the socio-
  political set (Appendix D). [🤖]
- **Period:** Collection happened in 2020, when public subscription
  pages were still widely accessible, and the substantive analysis
  treats 2020 as a snapshot while also showing 2017-2020 yearly view
  trends (§ I; § III.2; § V.4; § VII). [🤖]

## Methods

The `chan2vec` pipeline treats each commenter's subscription list like a
sentence, filters channels and sentences with too little support, learns
word2vec-style channel embeddings, and then uses K-nearest neighbors to
classify channels from labeled training data such as Recfluence and
Laukemper (§ III; Appendix B-C). [🤖]

The paper uses that embedding infrastructure for two tasks: iterative
high-recall channel discovery followed by high-precision final
prediction, and softer tag/media-type classification for the newly found
channels, with evaluation through holdout analysis, manual review,
precision/recall, and comparison to Dinkov et al.'s political-lean model
(§ IV; § VI; Appendix C-E). [🤖]

## Main Findings

1. The discovery process finds 7,224 socio-political channels matching
   the paper's criteria, nearly ten times the 758 channels in the
   original Recfluence dataset, and the authors estimate roughly 78
   percent recall for channels fitting that target definition (§ VI;
   Appendix E). [🤖]
2. Head-only political YouTube samples are materially skewed: the paper
   reports 1.8 percent of head-channel traffic going to Conspiracy
   channels versus 6.5 percent overall, and 14.6 percent of head traffic
   going to Partisan Right channels versus 19.8 percent overall (§ VI).
   [🤖]
3. `chan2vec-knn` predicts soft tags better than the average individual
   human annotator for 11 of 12 tags and outperforms Dinkov et al.'s
   model on political-lean accuracy for channels it can support (83.8
   percent versus 73.0 percent in the strongest comparison) (§ VI;
   Appendix C-E). [🤖]
4. The same method now faces a reproducibility problem because it
   depends on public subscription visibility that the paper says YouTube
   has since restricted, making the 2020 data-collection environment
   historically specific (§ III.2; § VII). [🤖]

## Limitations / Scope Conditions

The method depends on public commenter subscriptions, and the paper
states that YouTube has since made subscriptions less visible, which
directly limits exact replication (§ III.2; § VII). [🤖]

Analysis is at the channel rather than video level, so the method fits
channels with relatively coherent themes better than broad or mixed-
topic channels (§ VII). [🤖]

The discovery design is a snowball-like process seeded from known
socio-political channels, so selection bias remains possible even though
the paper argues it can be mitigated by varied seeds (§ VII). [🤖]

The mapped corpus is English-focused and requires a minimum level of
subscribers and commenter-subscription support, making very small or
non-English channels harder to discover or classify (Appendix D; §
VII). [🤖]

## Temporal Scope

This is best treated as a historical 2020 channel-mapping study rather
than a current pipeline description. It captures a moment when public
commenter subscriptions were still broadly usable, and its substantive
findings about the political channel landscape should be read as a 2020
snapshot rather than as a stable description of later YouTube (§ I; §
III.2; § VII). [🤖]

## Key Quotes

> "prior studies have significantly underestimated the prevalence of
> right-leaning and conspiracy-themed content" (Abstract) [🤖]

> "YouTube appears to be phasing out the visibility of subscriptions"
> (§ VII) [🤖]

## Relation to This Project

- **Methods companion:** Directly relevant because it turns historical
  public-subscription data into a concrete large-scale channel-discovery
  and classification pipeline with explicit evaluation and coverage
  discussion. [PROJECT]
- **Paper 1 (attention economy):** Useful mainly as a warning that
  visible head-channel samples can misstate the structure of political
  content supply. [PROJECT]
- **Paper 2 (mobility):** Limited direct relevance because the paper
  maps a 2020 snapshot rather than creator trajectories. [PROJECT]
- **Later studies:** One of the most directly usable sources for the
  planned channel-classification methods page because it combines
  discovery, classification, validation, and explicit discussion of the
  access regime that enabled the method. [PROJECT]

## Linked Claims

- `claim_descriptive_deficit_denominator_problem`
- `claim_descriptive_deficit_infrastructure_constraints`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** [[channel_classification]]
- **Debates:** _(none yet)_
- **Related sources:** [[ledwich_zaitsev_2020]], [[rieder_2020]], [[boesinger_et_al_2024]]
