---
source_id: lee_et_al_2022
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "Whose Advantage? Measuring Attention Dynamics across YouTube and Twitter on Controversial Topics"
authors:
  - "Lee, JooYoung"
  - "Wu, Siqi"
  - "Ertugrul, Ali Mert"
  - "Lin, Yu-Ru"
  - "Xie, Lexing"
year: 2022
venue: "Proceedings of the Sixteenth International AAAI Conference on Web and Social Media (ICWSM 2022)"
doi: null
temporal_scope: "Cross-platform attention data on tweeted YouTube videos from January 1, 2017-April 30, 2018"
themes:
  - news-ecosystem
  - recommendation-radicalization
project_modules:
  - public-affairs
census_papers:
  - paper1-attention-economy
  - study3-media-system
census_relevance: medium
verification:
  machine_extracted: 17
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Lee et al. (2022) - Cross-Platform Attention Dynamics

## Full Citation

Lee, JooYoung, Siqi Wu, Ali Mert Ertugrul, Yu-Ru Lin, and
Lexing Xie. 2022. "Whose Advantage? Measuring Attention
Dynamics across YouTube and Twitter on Controversial Topics." In
*Proceedings of the Sixteenth International AAAI Conference on Web and
Social Media (ICWSM 2022)*.

## One-Sentence Contribution

Linking YouTube video attention to Twitter diffusion across abortion,
gun control, and Black Lives Matter, the paper finds a durable
cross-platform asymmetry: left-leaning videos gain more YouTube views
and engagement, while right-leaning videos receive more tweets and
longer attention tails on Twitter (pp. 1, 6-10). [🤖]

## Research Question

How do ideological groups differ in their cross-platform attention
trajectories across YouTube and Twitter, and do those asymmetries vary
across controversial political topics and over time? (pp. 1-3, 6-10)
[🤖]

## Data, Sample, Geography, and Period

- **Data:** The study links tweeted YouTube videos to their YouTube view and watch-time traces, Twitter mentions, retweet cascades, and early-adopter follower networks (pp. 1-4). [🤖]
- **Sample:** The final dataset includes 179 abortion videos, 268 gun-control videos, and 777 Black Lives Matter videos mentioned in more than 970,000 tweets, all drawn from a 16-month Twitter stream and restricted to videos with nontrivial attention (pp. 3-4). [🤖]
- **Geography:** The topics and examples are U.S.-centric controversial politics, but the paper studies cross-platform attention dynamics rather than a nationally representative news sample (pp. 1-4). [🤖]
- **Period:** The underlying Twitter stream runs from January 1, 2017 to April 30, 2018, which places the evidence in the pre-2019 YouTube regime and before later recommendation-policy shifts (pp. 3-4). [🤖]

## Methods

Lee et al. curate topical YouTube/Twitter datasets, classify YouTube
videos and early-adopter Twitter users by political leaning, then
compare ideological groups using aggregate YouTube and Twitter
attention metrics, temporal half-life measures, and network/cascade
measures such as viral potential, tweeting lifetime, and early-adopter
centrality (pp. 3-10). [🤖]

## Main Findings

1. Left-leaning videos are generally more viewed and more engaging on YouTube than right-leaning videos across the studied topics, although the strength of that advantage varies by issue (pp. 1, 6-8). [🤖]
2. Right-leaning videos are more tweeted and retweeted on Twitter, especially in abortion and BLM, indicating that ideological advantage differs by platform rather than running in one uniform direction (pp. 1, 6-8). [🤖]
3. Attention unfolds differently over time: left-leaning videos tend to accumulate views and tweets faster, while right-leaning videos often sustain attention longer and have longer tweeting lifetimes (pp. 1, 8-10). [🤖]
4. Early diffusion structures also differ, with left-leaning videos relying more on centralized high-attention early adopters and right-leaning videos showing earlier cascade starts in the attention lifecycle (pp. 1, 8-10). [🤖]

## Limitations / Scope Conditions

The paper studies tweeted YouTube videos that received substantial
attention, so it explains attention dynamics for salient controversial
videos rather than for the full universe of YouTube political content
(pp. 3-4, 10-11). [🤖]

Its Twitter stream is sampled rather than complete, and follower
networks for early adopters were collected later, which makes the
network results informative but historically noisy in ways the authors
acknowledge (pp. 10-11). [🤖]

The study is about cross-platform attention, not direct recommendation
measurement, so it should inform the atlas mainly as evidence about
ideological attention asymmetry and platform comparison rather than as
direct recommender evidence (pp. 1, 10-11). [🤖]

## Temporal Scope

This is explicitly pre-2019 evidence. In the atlas, the paper matters
because it shows that ideological advantage is platform-specific even
before the 2019 YouTube changes: what looks strong on Twitter can look
weaker on YouTube, and vice versa, which cautions against treating
cross-platform political visibility as one interchangeable object (pp.
1, 6-10). [🤖]

## Key Quotes

> "left-leaning videos are overall more viewed, more engaging, but less tweeted than right-leaning videos." (p. 1) [🤖]

> "The attention time series unfold quicker for left-leaning videos, but span a longer time for right-leaning videos." (p. 1) [🤖]

## Relation to This Project

- **Methods companion:** Useful for showing how platform-comparison work can separate attention on YouTube from attention around YouTube on other platforms. [PROJECT]
- **Paper 1 (attention economy):** Directly relevant because it treats attention as something that moves differently across platform interfaces and ideological groups. [PROJECT]
- **Paper 2 (mobility):** Indirect relevance only; it is about attention diffusion, not creator or audience migration over time. [PROJECT]
- **Later studies:** Good complement to [[wu_resnick_2021]] and [[newman_et_al_2025]] because it puts YouTube political attention into a broader cross-platform context rather than staying inside YouTube-only measures. [PROJECT]

## Linked Claims

- `claim_news_ecosystem_cross_platform_attention_asymmetry_by_ideology`

## Cross-References

- **Themes:** [[news_ecosystem]], [[recommendation_radicalization]]
- **Methods:** _(none yet)_
- **Debates:** [[filter_bubble_evidence]], [[pre_2019_vs_post_2019_algorithm]]
- **Related sources:** [[wu_resnick_2021]], [[huang_yang_2024]], [[ribeiro_et_al_2020]]
