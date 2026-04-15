---
source_id: mcgrady_2025
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "One Platform, Four Languages: Comparing English, Spanish, Hindi, and Russian YouTube"
authors:
  - "McGrady, Ryan"
  - "Zheng, Kevin"
  - "Zuckerman, Ethan"
year: 2025
venue: "Social Media + Society"
doi: "10.1177/20563051251363216"
temporal_scope: "Random samples collected in 2023-2024 describing uploads from 2006-2023 across four language communities"
themes:
  - descriptive-deficit
  - cross-linguistic-variation
project_modules:
  - denominator
  - discovery-completeness
  - taxonomy
census_papers:
  - methods-companion
  - paper1-attention-economy
  - study5-cross-language
census_relevance: high
verification:
  machine_extracted: 9
  human_checked: 9
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-15
---

# McGrady et al. (2025) - One Platform, Four Languages

## Full Citation

McGrady, Ryan, Kevin Zheng, and Ethan Zuckerman. 2025. "One Platform, Four Languages: Comparing English, Spanish, Hindi, and Russian YouTube." *Social Media + Society* 11(3): 1-21. https://doi.org/10.1177/20563051251363216

## One-Sentence Contribution

The paper uses random samples of English, Spanish, Hindi, and Russian YouTube to show that English-centric research badly misstates platform-wide patterns and that linguistic communities may use the same platform in fundamentally different ways (pp. 1, 3-4, 17-18). [✓]

## Research Question

If researchers compare representative language-specific random samples rather than defaulting to English-language content, what different patterns of growth, duration, popularity, and categorization become visible on YouTube? (pp. 1-5) [✓]

## Data, Sample, Geography, and Period

- **Data:** Randomly sampled YouTube videos, metadata extracted with `yt-dlp`, and Whisper-based language detection calibrated separately for English, Spanish, Hindi, and Russian (pp. 1, 5-6). [🤖]
- **Sample:** 246,381 random videos collected in 2023-2024, yielding calibrated high-confidence language samples of 33,772 English, 10,446 Spanish, 17,142 Hindi, and 7,031 Russian videos (pp. 5-6). [🤖]
- **Geography:** Language-specific rather than nation-specific samples, with explicit caution that language only imperfectly proxies geography and culture (pp. 3-5). [🤖]
- **Period:** The random samples were retrieved in 2023 and 2024 and are used to describe uploads from 2006 through 2023 (pp. 5, 7-8). [🤖]

## Methods

The study uses Random Prefix Sampling to collect public YouTube videos, calibrates Whisper confidence thresholds separately by language, then compares upload dates, popularity metrics, duration, Shorts prevalence, and category metadata across the four language-specific samples (pp. 5-7). [🤖]

## Main Findings

1. YouTube research is skewed toward English in both samples and publications, and English-language content should not be assumed to represent the platform as a whole (pp. 1-4). [✓]
2. Hindi YouTube differs sharply from English, Spanish, and Russian YouTube: it is much newer, much shorter, much more Shorts-heavy, and more than half of the Hindi sample was uploaded in 2023 alone (pp. 1, 7, 12, 15, 18). [✓]
3. Cross-language metadata differences are not trivial: English has the smallest share of News & Politics videos, Spanish has the longest median duration, and Hindi has a far larger Education share than the other three languages (pp. 1, 12-17, 18). [✓]
4. Random sampling is a useful methodological corrective for cross-language platform study, but it is only a starting point for the content analysis, ethnography, and survey work needed to explain why these differences exist (pp. 3-6, 17-18). [✓]

## Limitations / Scope Conditions

YouTube does not publish platform language distributions, and video language detection is difficult because of ambient noise, code switching, singing, and dialect variation (pp. 2-4). [✓]

Language is an imperfect proxy for geography and culture because one language can span very different regions and multilingual practices, while one country can contain many language communities (pp. 4-5). [🤖]

Random Prefix Sampling covers public videos only; unlisted and private videos are excluded from the sampling frame (p. 5). [🤖]

Metadata can surface broad patterns and anomalies, but it cannot by itself establish the cultural meaning or content character of videos without follow-on qualitative and content-focused work (pp. 17-18). [🤖]

## Temporal Scope

The paper describes cross-language YouTube up to 2023 using random samples collected in 2023-2024, and many of its Hindi-specific interpretations are explicitly tied to post-2020 changes around TikTok and Shorts rather than to a timeless language difference (pp. 5-8, 15-18). [🤖]

## Key Quotes

> "Research on YouTube in particular and social media in general is skewed toward English both in terms of samples and publications" (p. 3). [✓]

> "This study underscores the necessity of multilingual and culturally specific approaches to platform research" (p. 1). [✓]

## Relation to This Project

- **Methods companion:** Direct precedent for multilingual random sampling, language calibration, and keeping uncertainty about language detection explicit. [PROJECT]
- **Paper 1 (attention economy):** Strong warning that English-language slices of YouTube should not be treated as platform-wide baselines for attention or content composition. [PROJECT]
- **Paper 2 (mobility):** Limited direct relevance. [PROJECT]
- **Later studies:** Central to `study5-cross-language` and to any claim about whether YouTube is one platform or many. [PROJECT]

## Linked Claims

- `claim_descriptive_deficit_multilingual_misrepresentation`
- `claim_cross_linguistic_youtube_not_one_platform`

## Cross-References

- **Themes:** [[descriptive_deficit]], [[cross_linguistic_variation]]
- **Methods:** _(none yet)_
- **Debates:** _(none yet)_
- **Related sources:** [[mcgrady_2023]], [[munger_et_al_2025]]
