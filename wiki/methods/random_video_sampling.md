---
type: method-page
canonical_name: random_video_sampling
title: "Random Video Sampling (ID-Space Methods)"
status: machine-draft
method_family: sampling
themes_touched:
  - descriptive-deficit
  - cross-linguistic-variation
project_modules:
  - denominator
  - discovery-completeness
  - activity-tail
last_refreshed: 2026-04-24
verification:
  machine_extracted: 0
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
---

# Random Video Sampling (ID-Space Methods)

## What This Method Is

[LIT] Random video sampling on YouTube is the family of methods that
attempts to draw videos directly from the space of YouTube's 11-character
video IDs rather than from channels, keywords, recommendation traces, or
the public search interface. The goal is a sampling frame with known
inclusion probabilities so that platform-level prevalence, count, and
distribution claims can be defended (McGrady et al. 2023, pp. 4-7). [🤖]

[LIT] The method exists because YouTube does not publish a random-video
endpoint and because keyword- and channel-based samples inherit whatever
bias is baked into search ranking, channel connectivity, and language
distribution (McGrady et al. 2023, pp. 4-7; McGrady et al. 2025, pp.
2-3; Rieder et al. 2020, § 2.1). [🤖]

[LIT] Two operational variants currently exist in the atlas corpus:
**Random Prefix Sampling (RPS)** and **Dialing for Videos (DFV)**.
Both target the same population — public searchable YouTube videos —
and both rely on YouTube's search engine as the lookup mechanism
(McGrady et al. 2023, pp. 9-11). [🤖]

## How the Two Variants Work

[LIT] **Random Prefix Sampling** (originally proposed by Zhou et al.
2011 and not yet a source card in this atlas) exploits a YouTube search
behavior: a query for `watch?v=xy...z`, where `xy...z` is a 5-character
prefix that does not contain a dash, returns up to about 20 videos
whose IDs begin with that prefix followed by a dash. McGrady et al.
speculate this happens because the search indexer treats dashes as
token separators (McGrady et al. 2025, p. 3). [🤖]

[LIT] **Dialing for Videos** generates batches of 32 random 11-character
IDs and joins them with OR into a single query submitted via YouTube's
internal InnerTube API. Two shortcuts make the approach computationally
tractable: OR-query batching gives a ×32 multiplier, and case-insensitive
search gives another ×1,024 multiplier for the 10 alphabetical positions.
A single DFV query therefore effectively tests 32 × 1,024 = 32,768
case-sensitive IDs (McGrady et al. 2023, pp. 9-11). [🤖]

[LIT] The 2023 run collected 10,016 hits from 18,260,259,669
case-insensitive IDs tested, equivalent to 18,698,505,901,056
case-sensitive guesses and about 1.87 billion case-sensitive guesses per
hit (McGrady et al. 2023, p. 15). [🤖]

## Where It Has Been Used

| Source | Method | Sample | Key Design Choice | Verified |
|--------|--------|--------|-------------------|----------|
| [[mcgrady_2023]] | DFV (primary) + RPS (validation) | 10,016 public videos via DFV; 10k-scale RPS comparison | Introduces DFV; compares it to RPS on upload year, views, comments, likes, subscribers, categories, and top-20 languages | [🤖] |
| [[mcgrady_2025]] | RPS at scale with Whisper language detection | 246,381 random videos, yielding 33,772 English, 10,446 Spanish, 17,142 Hindi, 7,031 Russian high-confidence language samples | Uses RPS (not DFV) as the primary frame; treats language classification as part of the estimator via per-language calibrated confidence thresholds | [🤖] |
| [[bartl_2018]] | Random letter-string search (ancestor method, not ID-space) | 19,025 channels across four batches | Draws randomness from *query strings*, not IDs; explicitly evaluates sampling bias from popularity-sorted search returns | [🤖] |
| [[zhou_et_al_2011]] | Random Prefix Sampling | Length-5 random prefixes in the 2011 YouTube Search API | Introduces the RPS estimator `N_hat = (1 / (m p_L)) * sum_i X_i^L`, its variance, and sample-size guidance | [🤖] |

[LIT] The McGrady team is the only group in the atlas corpus currently
producing ID-space random samples at research scale. Other uses of RPS
or related designs (e.g., Golnari et al. 2014, Mathur et al. 2018,
Akgul et al. 2022, Zheng et al. 2024) are referenced in the McGrady
papers but are not yet ingested into the atlas. See the Open Holes
section below. [🤖]

## Target Population (What These Methods Actually Estimate)

[LIT] Both RPS and DFV sample from **public searchable videos**, not
from all videos ever uploaded. Unlisted and private videos are outside
the frame by design: RPS relies on search-result retrieval and DFV
relies on search matching, so any video not indexed by YouTube's public
search is unreachable (McGrady et al. 2023, pp. 10-11; McGrady et al.
2025, p. 5). [🤖]

[LIT] A video-uniform random sample does *not* estimate viewer exposure,
recommendation prominence, or attention-weighted share of any content
category. It estimates the prevalence of properties *among videos*, not
*among views or viewers*. Heavy-tailed viewing distributions mean that
the video-uniform frame systematically under-represents the small minority
of videos that carry most platform attention (McGrady et al. 2023, pp.
20-21, 61). [🤖]

## Strengths and Assumptions

[LIT] The method gives a defensible denominator for platform-size claims.
McGrady et al. estimate 9.88 billion publicly searchable videos in late
2022 with a 95% confidence interval and 2% margin of error; because the
frame excludes unlisted and private videos, the full YouTube corpus is
likely larger than 10 billion (McGrady et al. 2023, pp. 15-16). [🤖]

[LIT] The original RPS estimator is explicitly a probability-sampling
estimator over ID-prefix regions: Zhou et al. define `p_L` as the match
probability for a length-`L` prefix and estimate total videos as
`N_hat = (1 / (m p_L)) * sum_i X_i^L`, where each `X_i^L` is the number
of videos returned for one sampled prefix (Zhou et al. 2011, pp. 3-4).
[🤖]

[LIT] Zhou et al. also derive the estimator variance as
`N * ((1 / (m p_L)) - 1)`, making the practical tradeoff explicit:
larger `m` lowers variance linearly, while longer prefixes make
variance grow quickly because `p_L` shrinks (Zhou et al. 2011, p. 4).
[🤖]

[LIT] Because IDs are pseudo-random strings rather than human-chosen
channel names or titles, ID-space sampling sidesteps the critique Rieder
makes of random-keyword methods: that "the distinct phonetic patterns
of human languages mean that channel names or video titles are not
spread equally over the alphabet and will cluster around particular
character patterns" (Rieder et al. 2020, § 2.1). ID-space sampling is
immune to this specific source of language bias in a way Bärtl's
random-keyword approach is not (Bärtl 2018, pp. 20-22). [🤖]

[LIT] Both methods expose biases they cannot fully correct. McGrady et
al. explicitly flag that DFV "oversamples IDs with letters, rather than
numbers or symbols, in their first ten characters" because of the
case-insensitivity shortcut, and that RPS "risks both overstudying this
part of YouTube [videos with dashes in their IDs], as well as
researchers influencing view counts" (McGrady et al. 2023, pp. 11, 49).
[🤖]

## Known Weaknesses

### Structural limits of the sampling frame

[LIT] RPS only reaches videos whose IDs contain a dash at the prefix
boundary. This is a strict-subset restriction on the frame, not a
probabilistic one. If YouTube's ID generation scheme has ever been
non-uniform over time (plausible but unverified), the dash-containing
subset is not automatically a representative slice of the full ID space
(McGrady et al. 2023, pp. 8-9; McGrady et al. 2025, p. 3). [🤖]

[LIT] Both methods depend on the InnerTube API accessed via `yt-dlp`.
This is an undocumented interface rather than the supported Data API.
A tightening of InnerTube access, signed requests, or anti-scraping
measures would break the pipeline, and McGrady et al. explicitly flag
the risk that brute-force query rates "may draw unwanted attention from
the company or negatively affect its normal operations" (McGrady et al.
2023, p. 9). [🤖]

[LIT] RPS additionally depends on YouTube's dash-prefix search quirk,
which McGrady et al. describe as "an unusual feature (or, more likely,
a bug)" (McGrady et al. 2025, p. 3). A one-line indexer fix on YouTube's
side would eliminate the entire method, and researchers would likely
not be told in advance. [🤖]

### Heavy-tail inference and the central-limit problem

[LIT] YouTube's engagement distributions are extremely right-skewed.
In the 2022 DFV sample, 86.93% of videos had fewer than 1,000 views,
while 3.67% of videos with more than 10,000 views accounted for 93.61%
of total sample views; the 16 most-popular videos, 0.16% of the sample,
accounted for 50.52% of total views (McGrady et al. 2023, pp. 20-21, 61).
[🤖]

[LIT] Under this degree of skew, the sample mean and total are dominated
by a small number of tail observations, and a random sample of 10,016
videos contains very few of them. Rieder et al. tested whether channel
indegree and subscriber distributions follow simple power laws and
found that log-normal fits often worked better, but the practical
consequence is the same: ordinary variance-based confidence intervals
for means and totals can be unstable in realistic samples (Rieder et
al. 2020, § 4). [🤖]

[PROJECT] Practical implication for the census project: on heavy-tail
outcomes — mean views, total views, mean likes, "top X% of videos account
for Y% of Z" statistics, exposure-weighted prevalence — ordinary
standard errors from a DFV/RPS sample should be treated with suspicion
unless the design explicitly oversamples the tail or uses
tail-sensitive estimators (trimmed means, log-scale summaries, bootstrap
resampling at the cluster level). [🤖]

### The RPS validation record is narrower than it reads

[LIT] The entire RPS validation record in the atlas corpus consists of
one comparison in McGrady et al. 2023 (pp. 49-58), conducted by the
same team that introduced DFV, across two samples collected at
different times: DFV was collected October-December 2022 and the RPS
comparison sample was collected on a single day, January 11, 2023
(McGrady et al. 2023, p. 49). [🤖]

[LIT] The comparison shows strong agreement on *central tendency and
shape*:

- Median views agree closely (37 RPS, 35 DFV) (p. 52). [🤖]
- Share of videos with fewer than 1,000 views: 86.45% RPS vs. 86.93% DFV (p. 52). [🤖]
- Log-transformed view, comment, and subscriber distributions overlap
  visually (Figures 20, 21, 23). [🤖]
- Category shares (Table 4) agree to within about 1 percentage point in
  most cells. [🤖]
- Top-20 language distribution is mostly similar (Table 5). [🤖]

[LIT] It shows meaningful *divergence at the heavy tail*:

- Mean views: 15,900 RPS vs. 5,868 DFV — RPS is 2.7× higher (p. 52). [🤖]
- Max views: 98.6M RPS vs. 4.6M DFV — RPS is ~21× higher (p. 52). [🤖]
- Share of videos with zero likes: 98.11% RPS vs. 88.71% DFV — a 9.4-point
  gap (p. 52). [🤖]
- Mean likes: 2.83 RPS vs. 16.48 DFV — DFV is ~5.8× higher (p. 52). [🤖]
- Share of 2022 uploads: 29.07% RPS vs. 25.91% DFV (p. 51). [🤖]

[LIT] McGrady et al. acknowledge "reservations about the Random Prefix
Sampling described above" but conclude it is "sufficiently similar to
our sample that it can be used as a more practical method to produce a
random sample for most purposes," with the explicit caveat of "being
mindful of its opacity and potential for overstudying the subset of
total videos available to it" (McGrady et al. 2023, pp. 58, 62). This
is the language of a pragmatic fallback, not a validated substitute.
[🤖]

[LIT] The validation is concurrent validity between two search-based
methods that share much of the same access pathway, not criterion
validity against an independent ground truth. YouTube does not release
a platform-wide denominator, so no external validation is currently
possible. The ~10 billion public-video estimate from DFV (McGrady et al.
2023, p. 16) and the ~15 billion estimate attributed to Zheng et al.
2024 (reported in McGrady et al. 2025, p. 7) are both in-family
estimates rather than independent cross-checks. [🤖]

### Shorts and format blind spots

[LIT] The RPS-DFV validation window straddles YouTube's 2021
introduction of a Shorts category. Table 4 of McGrady et al. 2023
(p. 57) shows 0.01% RPS and 0.00% DFV coded to Shorts — the validation
effectively covers zero Shorts. Given Violot et al.'s evidence that
Shorts changed both supply and engagement baselines by 2021-2022
([[violot_et_al_2024]]), neither method has been shown to sample Shorts
well, and neither paper addresses the March 31, 2025 change to how
Shorts views are counted ([[youtube_shorts_views_2025]]). [🤖]

## Related Approaches (Not Random Video Sampling)

[LIT] Network crawls such as Rieder et al. 2020 and Ribeiro and West
2021 produce large channel or channel-video samples but do not draw
from the video ID space and do not claim to estimate platform-wide
video prevalence. They sample from YouTube's visible relational
structure (featured channels, public subscriptions, subscriber-ranked
third-party services) and explicitly note the frame restriction —
Rieder observes that the "main problem with crawling... is to know
whether a crawl is complete and, if not, what is missing" (Rieder et
al. 2020, § 2.1), and Ribeiro and West warn that YouNiverse is "likely
to over-emphasize features associated with English-language channels"
(Ribeiro and West 2021, p. 6). [🤖]

[LIT] Crawls give relational structure that random-ID methods do not;
random-ID methods give a defensible denominator that crawls do not. The
two families are complementary, not competing, because they answer
different research questions (Rieder et al. 2020, § 2.1; McGrady et al.
2023, pp. 4-7). [🤖]

[LIT] Random-keyword methods such as Bärtl 2018 are best read as a
design ancestor of RPS rather than as an equivalent method. Bärtl
explicitly evaluated sampling bias from popularity-sorted search
returns and non-Latin-script undercoverage (Bärtl 2018, pp. 20-22), but
Rieder's critique is that the frame is intrinsically tied to language
and SEO ranking in a way ID-space methods escape (Rieder et al. 2020,
§ 2.1). [🤖]

## What the Census Project Does Differently

[PROJECT] For any Paper 1 claim about platform-wide denominators or
prevalence, the methods companion should state explicitly whether the
estimand is:
- public searchable videos (the actual RPS/DFV target),
- all videos ever uploaded (not directly observable),
- viewer-exposure-weighted content (not estimated by ID-space methods),
- or a subset conditioned on visibility, language, or channel tier.

Running these together collapses the sampling-frame distinctions the
atlas is trying to preserve. [🤖]

[PROJECT] For heavy-tail outcomes, default to medians, quantiles, and
log-scale summaries rather than means or totals; where a mean or total
is unavoidable, report a sensitivity range that reflects the 2.7× mean
and ~21× max divergence observed between RPS and DFV in the 2023
validation. [🤖]

[PROJECT] Treat the 2023 RPS-DFV comparison as evidence on *central
tendency and shape*, not on heavy-tail statistics. Explicitly re-run
the comparison on current data before relying on either method as the
primary frame for attention-economy work. [🤖]

[PROJECT] Prefer DFV over RPS when the analysis loads on the head of
the distribution; prefer RPS only when cost matters and the estimand
is robust to the observed divergences. [🤖]

## Open Methodological Questions

- Has the RPS-DFV equivalence been re-tested since late 2022? If not,
  we are leaning on a three-year-old same-team concurrent-validity
  check. [🤖]
- Does YouTube's ID-generation scheme change over time? If so, the
  dash-containing subset that RPS can reach may not be temporally
  uniform. [🤖]
- How do either method's frames handle Shorts in the post-March-2025
  view-counting regime? [🤖]
- What is the variance structure of DFV under the case-insensitivity
  shortcut when estimators are reweighted to account for alphabetical
  oversampling? The 2023 paper notes the bias but does not formally
  correct for it (McGrady et al. 2023, p. 11). [🤖]
- Can the ~10B / ~15B platform-size estimates be cross-validated
  against any non-search-based denominator (e.g., internal platform
  reports, scraped sitemaps, third-party crawls)? [🤖]

## Open Holes / Next Sources to Acquire

These sources are referenced in the McGrady papers, in Rieder et al.
2020, and in the review text that motivated this page, but are not yet
ingested into the atlas. Listed roughly in order of importance for
future refresh work:

1. **Zheng, McGrady, & Zuckerman (2024), TubeStats.** Source of the
   ~15 billion public-video estimate attributed in McGrady et al. 2025,
   p. 7. Infrastructure rather than a conventional article, but the
   number is load-bearing.
2. **Rieder, Padilla, & Coromina (2025), "Forgetful by design?"** A
   critical audit of YouTube's Data API search endpoint. Directly
   relevant to whether any search-based sampling method (RPS or DFV)
   can be trusted for temporal consistency.
3. **Karkulahti & Kangasharju (2015)**, "YouTube Revisited." Makes
   sampling bias the object of study across multiple sampling methods;
   the right external reference for the atlas's validation discussion.
4. **Golnari, Li, & Zhang (2014)**, extension of RPS to estimate upload
   flow and uploader dynamics. Provides a temporal-flow estimator that
   complements stock-size estimation.
5. **Mathur, Narayanan, & Chetty (2018)**, affiliate-disclosure study
   using RPS at 515,999-video scale. Substantive application useful as
   a precedent for two-stage (random baseline + targeted detection)
   designs.
6. **Akgul, Roberts, Namara, Levin, & Mazurek (2022)**, influencer
   VPN-ad study using ~86 million video RPS. Largest published RPS
   application we have a lead on; their thresholding practices are
   directly relevant to our rare-content estimation questions.
7. **Brodersen, Scellato, & Wattenhofer (2012)**, Google-internal
   random sample of >20M videos. Not externally reproducible, but the
   only point of comparison we have for an internally-sampled
   denominator.
8. **Paolillo et al. (2019)**, hybrid search/browse/crawl of 549,383
   channels. Criticized in Rieder et al. 2020 § 2.1 for being
   "neither systematic" nor explicit about biases — ingest primarily
   to anchor the critique.
9. **Liu, Blasiak, Xiao, Li, & Chen (2015)**, duplicate-video study
    using RPS. Example of two-stage estimation (probability sample +
    targeted validation).
10. **Abu-El-Haija et al. (2016), YouTube-8M**, platform-provided
    labeled benchmark. Not a probability sample but a useful reference
    point for internal-access datasets.
11. **Cheng, Dale, & Liu (2008)**, early large-scale crawl. Historical
    anchor rather than current evidence.
12. **Wesch (2008) and Hráček (2009)**, recent-uploads feed work.
    Historical anchor; feed no longer exists.

## Cross-References

- **Themes:** [[descriptive_deficit]], [[cross_linguistic_variation]]
- **Related methods:** [[channel_classification]]
- **Papers that use this method:** [[zhou_et_al_2011]], [[mcgrady_2023]], [[mcgrady_2025]], [[bartl_2018]]
- **Papers that inform the critique:** [[rieder_2020]], [[ribeiro_west_2021]], [[violot_et_al_2024]]
- **Debates:** _(none yet — see "Known Weaknesses" for the representativeness concern that would seed one once we have an independent published critique)_
