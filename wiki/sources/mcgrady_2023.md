---
source_id: mcgrady_2023
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Dialing for Videos: A Random Sample of YouTube"
authors:
  - "McGrady, Ryan"
  - "Zheng, Kevin"
  - "Curran, Rebecca"
  - "Baumgartner, Jason"
  - "Zuckerman, Ethan"
year: 2023
venue: "Journal of Quantitative Description: Digital Media"
doi: "10.51685/jqd.2023.022"
temporal_scope: "Publicly searchable videos sampled October 5-December 13, 2022; uploads from 2005-2022"
themes:
  - descriptive-deficit
  - cross-linguistic-variation
project_modules:
  - denominator
  - discovery-completeness
  - activity-tail
  - taxonomy
census_papers:
  - methods-companion
  - paper1-attention-economy
  - study5-cross-language
census_relevance: high
verification:
  machine_extracted: 12
  human_checked: 5
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-15
---

# McGrady et al. (2023) - Dialing for Videos

## Full Citation

McGrady, Ryan, Kevin Zheng, Rebecca Curran, Jason Baumgartner, and Ethan Zuckerman. 2023. "Dialing for Videos: A Random Sample of YouTube." *Journal of Quantitative Description: Digital Media* 3: 1-85. https://doi.org/10.51685/jqd.2023.022

## One-Sentence Contribution

The paper introduces a random-video sampling method for YouTube and uses it to establish baseline facts about platform size, growth, view concentration, and linguistic diversity that more targeted studies usually cannot observe directly (pp. 1, 4-6). [✓]

## Research Question

How can researchers generate a platform-level random sample of YouTube videos, and what does such a sample reveal about denominators, distributions, and the limits of prevailing convenience samples? (pp. 4-7) [✓]

## Data, Sample, Geography, and Period

- **Data:** Metadata gathered through InnerTube and `yt-dlp`, downloaded audio tracks for language detection, and a hand-coded subsample of videos (pp. 10-13, 46). [🤖]
- **Sample:** 10,016 randomly sampled public videos, plus a randomly selected hand-coded subset of 1,000 videos coded by at least two coders each (pp. 10, 12-13). [🤖]
- **Geography:** Platform-wide public YouTube rather than a country-bounded sample, with videos in many languages and no geographic restriction built into sampling (pp. 1-2, 44-49). [🤖]
- **Period:** Sampling ran from October 5, 2022, to December 13, 2022, and the upload-year analysis spans videos uploaded from 2005 through 2022 (pp. 10, 16-17). [🤖]

## Methods

"Dialing for Videos" uses randomly generated YouTube IDs, 32-term OR queries, and search-engine case insensitivity to search 32,768 valid IDs per query; the authors then extract metadata, download audio for VoxLingua107 language detection, and hand-code a random subsample to recover content features that metadata alone cannot capture (pp. 9-13, 46). [🤖]

## Main Findings

1. Fundamental platform facts such as total video count, view distributions, growth over time, and language representation remain unknown, creating denominator and distribution problems for any study that wants to make prevalence claims about YouTube content (p. 4). [✓]
2. YouTube offers no built-in mechanism for random sampling, so most existing studies begin from known channels, known videos, or recommendation traces rather than a representative platform-wide frame (pp. 4-7). [✓]
3. The sampled data imply about 9.88 billion publicly searchable videos in late 2022, with a reported 95% confidence interval and 2% margin of error; because the method excludes unlisted and private videos, the full number of YouTube videos is likely higher than 10 billion (pp. 15-16). [🤖]
4. The platform's public-video distribution is extremely skewed: 86.93% of sampled videos have fewer than 1,000 views, while the 3.67% with at least 10,000 views account for 93.61% of total sample views (pp. 20-21, 61). [🤖]

## Limitations / Scope Conditions

The method only captures public videos because it relies on search, so unlisted and private videos are outside the sampling frame by design (pp. 10-11). [🤖]

The hand-coded estimates for linguistically dependent categories such as politics or religion are likely undercounts because coders were instructed to answer conservatively and could not understand many languages in the sample (pp. 13-14, 38-39). [🤖]

The authors explicitly caution that their language-detection pipeline is useful for showing that YouTube is more multilingual than many users assume, but not for producing precise point estimates for specific languages (pp. 46-49, 61). [🤖]

## Temporal Scope

The core descriptive estimates are a late-2022 snapshot of publicly searchable YouTube videos, with growth estimates built from upload years 2005-2022 and a notable acceleration in uploads beginning in 2020 (pp. 16-19). [🤖]

## Key Quotes

> "Missing data like this creates 'denominator problems' and 'distribution problems'" (p. 4). [✓]

> "The vast majority of YouTube videos (86.93%) are seen by fewer than 1,000 people." (p. 61). [🤖]

## Relation to This Project

- **Methods companion:** The paper is direct precedent for treating denominator estimation and sampling-frame transparency as core methodological contributions rather than background scene-setting. [PROJECT]
- **Paper 1 (attention economy):** The long-tail view distribution and public-only denominator estimate provide benchmark context for any census-based claim about attention concentration. [PROJECT]
- **Paper 2 (mobility):** Limited direct relevance because the paper is cross-sectional rather than longitudinal. [PROJECT]
- **Later studies:** Especially relevant to cross-language work and to any study tempted to generalize from English, recommendation-based, or public-affairs-heavy slices of the platform. [PROJECT]

## Linked Claims

- `claim_descriptive_deficit_denominator_problem`
- `claim_descriptive_deficit_multilingual_misrepresentation`

## Cross-References

- **Themes:** [[descriptive_deficit]], [[cross_linguistic_variation]]
- **Methods:** _(none yet)_
- **Debates:** _(none yet)_
- **Related sources:** _(none yet)_
