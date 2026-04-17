---
source_id: figueiredo_et_al_2011
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "The tube over time: characterizing popularity growth of YouTube videos"
authors:
  - "Figueiredo, Flavio"
  - "Benevenuto, Fabrício"
  - "Almeida, Jussara M."
year: 2011
venue: "Proceedings of the Fourth ACM International Conference on Web Search and Data Mining (WSDM '11)"
doi: "10.1145/1935826.1935925"
temporal_scope: "Popularity histories and referrer traces collected in April 2010 for videos already uploaded to YouTube by that date"
themes:
  - descriptive-deficit
project_modules:
  - activity-tail
  - discovery-completeness
  - shorts
census_papers:
  - methods-companion
  - paper1-attention-economy
  - study10-shorts-vs-long-form
census_relevance: high
verification:
  machine_extracted: 16
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-17
---

# Figueiredo, Benevenuto, and Almeida (2011) - The Tube over Time

## Full Citation

Figueiredo, Flavio, Fabrício Benevenuto, and Jussara M. Almeida. 2011.
"The tube over time: characterizing popularity growth of YouTube
videos." In *Proceedings of the Fourth ACM International Conference on
Web Search and Data Mining (WSDM '11)*, 745-754.
https://doi.org/10.1145/1935826.1935925

## One-Sentence Contribution

The paper shows that YouTube videos reach cumulative-view milestones at
very different points in their lifetimes depending on video class,
which makes early-attention measurement and lookback calibration a
dataset-specific problem rather than a single universal rule (pp.
747-748). [🤖]

## Research Question

How do YouTube videos accumulate popularity over their full lifetimes,
how do those growth patterns differ across video classes, and what do
referrer pathways reveal about the mechanisms that drive popularity
growth on the platform? (pp. 745-747) [🤖]

## Data, Sample, Geography, and Period

- **Data:** YouTube popularity-history curves and top-referrer traces
  extracted from then-public YouTube statistics pages, including 100
  cumulative points for views, comments, and favorites plus referrer
  categories and first-access dates (pp. 746-747). [🤖]
- **Sample:** Three datasets collected in a single crawl day in April
  2010: 17,127 Top-list videos, 73,257 YouTomb copyright-removed
  videos, and 18,095 videos sampled from random-topic queries
  (pp. 746-748). [🤖]
- **Geography:** Platform-wide YouTube data rather than a
  country-bounded sample, though the YouTube service environment is the
  pre-2010 platform and not a later national subsystem study
  (pp. 745-747). [🤖]
- **Period:** The crawl occurred in April 2010 and reconstructs
  lifetime-normalized popularity trajectories up to that point for
  videos of varying ages already on YouTube (pp. 746-748). [🤖]

## Methods

The authors analyze cumulative-view growth by measuring the fraction of
each video's lifetime required to reach 10%, 50%, and 90% of total
observed views, then compare those distributions across Top, YouTomb,
and random-topic samples (pp. 747-748). [🤖]

They complement the lifetime-normalized analysis with burst-pattern
classification and referrer-category analysis, using interpolated daily
view curves and grouped referrer types such as Search, Internal,
Featured, Social, and External to characterize how users reached videos
(pp. 747-754). [🤖]

## Main Findings

1. View accumulation differs sharply across video classes: for half of
   the videos, Top videos take at most 65% of lifetime to reach 90% of
   total views, YouTomb videos 21%, and Random videos 87%
   (p. 748). [🤖]
2. YouTomb videos tend to receive most of their views much earlier in
   life than Top or random-topic videos, while Top videos more often
   exhibit sudden bursts and random-topic videos show slower, more
   diffuse growth (pp. 748-750, 754). [🤖]
3. Search and internal YouTube mechanisms both matter for discovery:
   search is important across datasets, but related-video and other
   internal YouTube pathways also account for large shares of access
   (pp. 751-754). [🤖]
4. Because popularity-growth patterns vary across datasets and ages,
   the paper implies that early-view observation windows should be
   calibrated to content class rather than treated as automatically
   transferable across YouTube use cases (pp. 747-750). [🤖]

## Limitations / Scope Conditions

The popularity-history curves contain at most 100 points per video, so
the authors interpolate between points to estimate daily values; that
introduces approximation error that grows with video age (p. 748). [🤖]

The referrer data only covers the top ten referrers per video, and for
64-75% of views across the datasets no referrer is registered in the
available statistics, which limits any strong claim about complete
traffic provenance (p. 748). [🤖]

The paper studies a pre-2010 YouTube environment, before later
algorithm changes, mobile-first usage, and Shorts, so its calibrated
lifetimes are methodological precedent rather than present-tense
descriptions of today's platform (pp. 745-748, 754). [🤖]

## Temporal Scope

This source is most useful as a historical methods precedent. It shows
how cumulative-view measurement behaved in the pre-2010 YouTube
environment and why lookback windows need calibration, but it should
not be projected directly onto post-2019 or Shorts-era viewing without
additional evidence (pp. 747-748, 754). [🤖]

## Key Quotes

> "We address this question by plotting…the amount of time it takes for
> a video to receive at least 10%, at least 50% and at least 90% of
> their total views…" (p. 748) [🤖]

> "Figure 2 shows that, for half of the videos…it takes at most 65%,
> 21% and 87%, respectively, of their total lifetimes…" (p. 748) [🤖]

## Relation to This Project

- **Methods companion:** Direct precedent for treating lookback windows
  as an explicit methodological choice rather than a hidden default.
  [PROJECT]
- **Paper 1 (attention economy):** Useful for defending calibrated
  observation windows when the manuscript estimates cumulative
  attention rather than same-day traffic. [PROJECT]
- **Paper 2 (mobility):** Limited direct relevance because the source is
  about view trajectories rather than creator transitions. [PROJECT]
- **Later studies:** Especially relevant to `study10-shorts-vs-long-form`
  because it motivates separate calibration logic when formats may have
  different attention lifecycles. [PROJECT]

## Linked Claims

- `claim_descriptive_deficit_lookback_windows_require_calibration`

## Cross-References

- **Themes:** [[descriptive_deficit]]
- **Methods:** [[lookback_calibration]]
- **Debates:** _(none yet)_
- **Related sources:** _(none yet)_
