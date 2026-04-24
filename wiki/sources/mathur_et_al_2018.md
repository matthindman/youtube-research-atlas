---
source_id: mathur_et_al_2018
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Endorsements on Social Media: An Empirical Study of Affiliate Marketing Disclosures on YouTube and Pinterest"
authors:
  - "Mathur, Arunesh"
  - "Narayanan, Arvind"
  - "Chetty, Marshini"
year: 2018
venue: "Proceedings of the ACM on Human-Computer Interaction 2(CSCW)"
doi: "10.1145/3274388"
temporal_scope: "YouTube and Pinterest content collected August-September 2017; MTurk disclosure experiments conducted March 2018"
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

# Mathur et al. (2018) - Endorsements on Social Media

## Full Citation

Mathur, Arunesh, Arvind Narayanan, and Marshini Chetty. 2018. "Endorsements on Social Media: An Empirical Study of Affiliate Marketing Disclosures on YouTube and Pinterest." *Proceedings of the ACM on Human-Computer Interaction* 2(CSCW), Article 119. https://doi.org/10.1145/3274388

## One-Sentence Contribution

This paper uses a large prefix-sampled YouTube baseline plus targeted affiliate-URL and disclosure detection to estimate affiliate marketing disclosure prevalence, then tests disclosure comprehension in randomized user experiments (pp. 1, 6-9, 13-20). [🤖]

## Research Question

How prevalent are affiliate marketing disclosures on YouTube and Pinterest, how do creators word those disclosures, and do users notice and understand the disclosure types creators actually use? (pp. 1-2, 13). [🤖]

## Data, Sample, Geography, and Period

- **Data:** Prefix-sampled YouTube videos and Pinterest pins, URLs extracted from video descriptions and pins, affiliate URL pattern detection, disclosure extraction from English descriptions, and MTurk user-study responses (pp. 6-9, 13-16). [🤖]
- **Sample:** 515,999 unique YouTube videos and 2,140,462 unique Pinterest pins; after affiliate URL detection, the paper identifies 3,472 YouTube videos and 18,237 Pinterest pins containing affiliate URLs (pp. 7, 9). [🤖]
- **Geography:** The content sample is platform-level rather than country-bounded, but the user experiments recruited U.S. MTurk participants with at least a 95% approval rating (pp. 15-16). [🤖]
- **Period:** YouTube/Pinterest content was gathered August-September 2017, and the user-study data were gathered in March 2018 (pp. 7, 15). [🤖]

## Methods

The authors reject related-graph and keyword sampling because those frames overrepresent high-engagement content or keyword choices, then use prefix sampling to gather a less biased YouTube sample by generating five-character video-ID prefixes and querying the YouTube Search API (pp. 6-7). [🤖]

After sampling, they resolve URLs from video descriptions and pins, identify affiliate URL patterns through frequency analysis plus manual validation, and compile 57 affiliate URL patterns from 33 affiliate marketing companies (pp. 7-9). [🤖]

The design is explicitly two-stage: a large random-ish platform baseline first identifies the population of candidate content, and a targeted classifier/detection pipeline then isolates affiliate URLs and disclosures for substantive analysis (pp. 6-9). [🤖]

For the user study, the authors ran separate randomized MTurk experiments for YouTube and Pinterest, varying disclosure type and position, then analyzed Likert outcomes with ordinal logistic mixed models and open-ended responses with deductive coding (pp. 13-16). [🤖]

## Main Findings

1. Affiliate URLs appeared in 0.67% of the YouTube sample, or 3,472 of 515,999 videos, and in 0.85% of the Pinterest sample, or 18,237 of 2,140,462 pins (p. 9). [🤖]
2. Only 10.49% of YouTube affiliate-marketing videos and 7.03% of Pinterest affiliate-marketing pins disclosed affiliate URLs in descriptions (pp. 11-12). [🤖]
3. Explanation disclosures were rare despite being closest to FTC guidance: they appeared in 1.82% of YouTube affiliate videos and 2.43% of Pinterest affiliate pins (pp. 11-12). [🤖]
4. Affiliate marketing was most common in YouTube Science & Technology and Howto & Style categories, with affiliate URL prevalence of 3.61% and 3.49%, respectively (p. 9). [🤖]
5. YouTube affiliate videos correlated with higher duration, views, likes, and dislikes than non-affiliate videos in Mann-Whitney U tests, which the authors interpret as making disclosure more pressing because engagement can affect recommendation visibility (p. 10). [🤖]
6. In the user experiments, participants correctly interpreted Explanation disclosures far more often than Affiliate Link disclosures: in the YouTube experiment, nearly 95% correctly interpreted Explanation disclosures versus about 65% for Affiliate Link disclosures (pp. 19-20). [🤖]

## Limitations / Scope Conditions

Affiliate URL detection is a lower-bound estimate because the authors ignored URL co-occurrences below a frequency threshold and did not include coupon-code based affiliate programs (p. 9). [🤖]

Disclosure extraction was limited to English descriptions; about 40% of affiliate marketing videos and pins had non-English descriptions, so disclosure findings may not generalize across languages (p. 9). [🤖]

The YouTube user experiment used five videos around the median affiliate-video length, so the experiment does not necessarily generalize to much shorter or longer videos (p. 16). [🤖]

## Temporal Scope

This is a 2017-2018 pre-Shorts study of YouTube affiliate marketing and user disclosure comprehension. It is most useful for method precedent and creator-economy disclosure evidence, not for current affiliate-marketing prevalence (pp. 7, 15, 22). [🤖]

## Key Quotes

> "we first measured the prevalence of and identified the types of disclosures in over 500,000 YouTube videos" (p. 1). [🤖]

> "only about 10% of affiliate marketing content on both platforms contains any disclosures at all" (p. 1). [🤖]

## Relation to This Project

- **Methods companion:** Strong precedent for a two-stage design that starts from a broad prefix-sampled baseline and then applies targeted detection/classification to a rare content type. [PROJECT] [🤖]
- **Paper 1 (attention economy):** Limited direct relevance, but useful for showing how a rare monetization practice can be estimated from a video-uniform baseline rather than only from keyword searches. [PROJECT] [🤖]
- **Paper 2 (mobility):** Minimal direct relevance. [PROJECT] [🤖]
- **Later studies:** Relevant to `creator-economy` because affiliate links are one monetization route, and to `classification-llm` because the pipeline anticipates random baseline plus automated/manual classification workflows. [PROJECT] [🤖]

## Linked Claims

- `claim_descriptive_deficit_two_stage_random_then_targeted_detection`
- `claim_creator_economy_affiliate_disclosures_are_rare`

## Cross-References

- **Themes:** [[descriptive_deficit]], [[creator_economy]]
- **Methods:** [[random_video_sampling]]
- **Debates:** _(none yet)_
- **Related sources:** [[rieder_et_al_2023]], [[youtube_2024]]
