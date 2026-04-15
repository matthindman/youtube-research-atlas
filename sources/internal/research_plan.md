# YouTube Research Plan

Matthew Hindman
4.2.2026

---

*Rough working draft -- not for sharing outside of the sampling committee.*

---

Over the next few weeks, as our collection ramps up, we will have the best YouTube audience data in the world outside of YouTube itself. We have already mapped more than 5 million channels with at least 10,000 subscribers, and we expect to have mapped more than 200 million smaller channels by the time we reach exhaustion. This data arrives as I have just finished building and validating new dynamic models for analyzing structural stability and channel-level churn.

This gives us an extraordinary opportunity: the chance to do the first independent near-census of a digital platform. YouTube is the single most important digital platform by aggregate time spent, used by 2.6 billion people monthly -- but it is one of the least studied digital platforms, with far fewer studies per user than Twitter or Facebook. In addition to the critical substantive importance of understanding YouTube, these data give us a chance to showcase a new measurement and collection regime for digital platforms that will transform how social scientists study digital platforms going forward.

This document outlines a plan to rapidly publish on the YouTube data, and to build a pipeline of follow-on papers that address key unanswered research questions in YouTube scholarship. The goal is to take YouTube from one of the worst-understood platforms to one of the best-studied.

I propose to center this research on 2-3 keystone papers, plus a number of smaller and more focused papers. These papers include:

1. **A platform-wide descriptive paper** on the total views/audience and viewer distribution across channel types, languages, institutional forms, etc. This paper solves the denominator problem -- the single biggest methodological obstacle in YouTube research -- by combining near-exhaustive crawling with formal tail estimation and weighted below-threshold sampling. *Intended journal: Science or Nature.*

2. **A paper on platform dynamics.** This will show both structural rank stability and channel-level churn, using new dynamic models that separate persistent hierarchical structure from the entry, exit, and reshuffling of individual channels. *Requires at least six months of data.*

3. **Smaller papers on key subtopics:**
   - YouTube as a news ecosystem: who produces news on YouTube, and how much attention does it command?
   - Cross-linguistic YouTube: is YouTube one platform or many?
   - Shorts vs. long-form: how is the rise of short-form video reshaping YouTube's attention economy?
   - Creator economy inequality: how concentrated are views, and what predicts position in the hierarchy?
   - Event-driven attention: how does YouTube respond to major news events?
   - Deplatforming: what happens to the audience ecosystem when channels are removed?
   - Platform substitutability: what happens to YouTube when a competitor (e.g., TikTok) is disrupted?
   - Coordinated inauthentic behavior: can we detect networks of channels with suspiciously synchronized growth?

---

## The State of YouTube Scholarship

### The biggest gap: we don't know what YouTube is

The single biggest gap in the current research on YouTube is the lack of descriptive data. We do not know the most basic facts about this platform: how many channels exist, how views are distributed, what content categories dominate, what languages are represented, and what share of attention goes to independent creators versus legacy institutions.

McGrady et al. put it clearly: "YouTube is one of the largest, most important communication platforms in the world, but while there is a great deal of research about the site, many of its fundamental characteristics remain unknown" (McGrady et al. 2023, p. 1). They enumerate the specific unknowns: "the number of videos YouTube hosts, how many views those videos typically receive, how much the site as a whole has grown over time, and how frequently various languages are represented in videos. Missing data like this creates 'denominator problems' and 'distribution problems' which limit the kinds of claims we can make" (McGrady et al. 2023, p. 4).

This denominator problem is not an abstract concern. It cripples every other line of YouTube research. As McGrady et al. observe: "A study may identify a set of 500 YouTube channels which contained misinformation about the 2020 United States presidential election, but it would be limited in the claims it can make about the prevalence of this misinformation. In other words, 500 out of how many videos?" (McGrady et al. 2023, p. 4). Without knowing the total, no prevalence claim is credible.

YouTube itself provides almost nothing to work with. "YouTube does not release most basic information about what it contains, and the company does not provide a mechanism to produce random samples" (McGrady et al. 2025, p. 2). Even language -- the most basic descriptive dimension -- is opaque: "YouTube does not share the distribution of languages spoken on its site with the public" (McGrady et al. 2025, p. 3). Kate Starbird has called YouTube "'almost inscrutable' compared to other platforms like Twitter" (as quoted in McGrady et al. 2025, p. 2).

### YouTube is dramatically understudied

The disparity between YouTube's importance and the research attention it receives is staggering. Munger describes YouTube as "the platform for which the ratio of academic attention to social and political importance seems to me to be the most out of whack" (Munger 2024, p. 2). The numbers bear this out: "Only fifteen percent of users use Twitter, while over forty percent of papers study it. In contrast, YouTube is second only to Facebook in global usage at just over fifty percent, while receiving well under five percent of the attention" (Munger et al. 2025, p. 2). Norton and Shapiro quantify the disparity: "there were approximately 22.4 and 1.4 published papers per 100 million active users for Twitter and Facebook respectively," while YouTube attracted far less research despite its enormous user base (Norton and Shapiro 2024, as quoted in Munger et al. 2025, p. 2). In political science specifically, the top three journals "have published a total of fifteen articles that are primarily based on the quantitative analysis of Twitter data (five each), but have never published an article primarily based on the quantitative analysis of YouTube data" (Munger and Phillips 2022, pp. 4-5).

Munger argues that this has distorted the entire research agenda: "The academic agenda has yet to adapt to the reality that the majority of time spent on social media is spent on non-textual platforms. For a variety of reasons, some legitimate others merely omphalocentric, we spend far too much time studying Facebook and especially Twitter" (Munger 2024, p. 9).

### Other key questions our data can address

Beyond the descriptive deficit, the literature identifies several major research gaps that our data are uniquely positioned to fill.

**The recommendation algorithm debate is stuck -- and partly for lack of descriptive context.** The question that has dominated the YouTube literature -- whether the recommendation algorithm radicalizes users -- is now widely recognized as poorly specified. Munger is blunt: "Using a variety of different approaches, none of the academic research on the role of the YouTube algorithm in the promotion of extremist videos finds anything remotely like the provocative 'rabbit hole' hypothesis" (Munger 2024, p. 14). Multiple experimental studies find null or minimal short-term effects of algorithmic manipulation on political attitudes (Liu et al. 2025; Hosseinmardi et al. 2024; Brown et al. 2022). User preferences, not algorithms, appear to be the primary driver: "exposure to alternative and extremist channel videos on YouTube is heavily concentrated among a small group of people with high prior levels of gender and racial resentment" (Chen et al. 2023, p. 1). But this entire debate has been conducted without any clear picture of the platform's overall content landscape. Our data can provide that context -- showing how much of the platform is political, how much is news, and how those categories relate to the overall distribution of attention.

**YouTube as a news ecosystem.** YouTube is now a top-four news source in most countries and the dominant news platform in the Global South. The Reuters Digital News Report 2025 finds that "over half of our samples in India, Thailand, and Kenya say they use YouTube for news" (Reuters DNR 2025, p. 16). In the United States, social media and video platforms have now overtaken television as the primary news source (Reuters DNR 2025, p. 11). But the character of this news ecosystem is almost entirely undescribed. Reveilhac observes: "To date, scant scholarly attention has been directed toward YouTube as a news source. ... our comprehension of the actual news content people consume, especially in terms of opinionated information created by opinion YouTubers and alternative channels covering news about politics and current affairs, remains limited" (Reveilhac 2024, p. 1). Newman et al. find that political commentary dominates, that "the vast majority (85%) of the top 15 [news creators] in each country are men" (Newman et al. 2025, p. 14), and that right-leaning US commentators "have found fertile ground for their pro-free speech and anti-mainstream media narratives" in other English-speaking countries (Newman et al. 2025, p. 13). Our data can measure the size, composition, and attention share of the public-affairs sector of YouTube for the first time.

**The creator economy is deeply unequal but poorly measured.** The existing evidence suggests extreme concentration: "the top 0.4% of channels account for 62% of views" (Rieder et al. 2023, p. 2), and earnings among monetized creators show a Gini coefficient of 0.89, "even more than in (most) non-digital labor markets" (Verwiebe et al. 2025, p. 12). Most creators are "stuck on the lower rungs of what we call the 'aspirational curve' ... Our numbers indeed show a steep income pyramid where the lower tiers are basically working for free" (Rieder et al. 2023, p. 4). But these findings are based on small samples. Our near-census allows concentration, inequality, and rank-size analysis at a scale no previous study has approached.

**Cross-linguistic variation is almost entirely unexplored.** Research on YouTube is overwhelmingly Anglophone: "Research on YouTube in particular and social media in general is skewed toward English both in terms of samples and publications" (McGrady et al. 2025, p. 3). The few cross-linguistic studies that exist reveal dramatic differences. Hindi YouTube is dominated by short-form content -- "more than half of Hindi videos are 30 seconds or less" (McGrady et al. 2025, p. 11) -- likely reflecting the migration from TikTok after India's 2020 ban. Russian YouTube operates under government throttling but "remains one of the primary ways citizens access unfiltered news" (McGrady et al. 2025, p. 3). Our data cover all languages and allow the first systematic cross-linguistic comparison of YouTube's attention economy.

**Platform dynamics are entirely uncharted.** No existing study has tracked the YouTube channel hierarchy over time at scale. We do not know how persistent top ranks are, how often mid-tier channels collapse or recover, whether spikes in viewership translate into durable audience growth, or how different institutional forms (independent creators vs. legacy media vs. state-affiliated channels) experience different patterns of stability and churn. These are questions that can only be answered with longitudinal panel data at census scale -- exactly what we are building.

---

## The Data

### What we are collecting

Our data system has four main layers, each serving a distinct purpose.

**The core audience panel** is the permanent historical backbone. This is our non-API source of truth: daily view counts and subscriber counts for every channel above our collection thresholds. Because this data does not come from the YouTube API, it is not subject to API retention policies and can be stored permanently. This is the layer that makes longitudinal analysis possible. It is also the layer that allows us to compute total platform-wide views at each subscriber threshold -- the foundation for solving the denominator problem.

**The API enrichment layer** provides channel metadata, new upload discovery, and selective video-level data from the YouTube Data API v3. This layer feeds the taxonomy pipeline: it gives us channel descriptions, topic categories, recent upload titles, and other text that we use for classification. Because YouTube's API policies require that statistics data be refreshed within 30 days, we treat this layer as a rolling operational cache rather than a permanent archive.

**The taxonomy layer** stores our human-labeled and machine-classified channel data: topic, institutional form, language, public-affairs relevance, and format profile. This is the interpretive layer that makes the raw audience data meaningful -- it is what lets us say not just "how many views" but "views of what kind of content, produced by what kind of institution, in what language."

**The estimation and analysis layer** stores the outputs of our denominator estimation, sampling weights, saturation curves, and paper-ready analytic tables. This is where the raw data becomes scholarship.

### The denominator problem and our inferential design

The most important methodological contribution of this project is solving -- or at least sharply bounding -- the denominator problem. The field has often treated the platform-wide denominator as effectively unknowable. We contest that directly.

Our design is not simply a census of large channels. It is a three-part inferential system:

**Part 1: Near-exhaustive discovery above validated thresholds.** We are systematically crawling and cataloging channels at every subscriber level. For large channels (100k+ subscribers), we are confident we have near-complete coverage. For channels with 10k+ subscribers, our discovery rate is declining toward zero -- a saturation signal. We validate coverage through independent audits: checking YouTube's trending feeds across all regions and categories, running targeted search probes for channels that our main crawl might miss, and tracking how many new channels each successive crawl wave discovers. Each of these diagnostics is run separately by language, region, and topic to ensure we are not systematically missing particular kinds of channels.

**Part 2: Formal tail estimation for unseen activity.** Even with 200 million channels in our registry, there are certainly channels we have not found. The key question is how much public activity those unseen channels represent. We address this through rank-size tail estimation. YouTube's view distribution follows a heavy-tailed pattern where the local Pareto exponent steepens as you move down the size distribution -- meaning the smallest channels collectively account for a diminishing share of total views. Rather than assuming a single power-law exponent across the entire tail (which would overestimate residual activity), we model the curvature in the rank-size relationship and produce bounded estimates of how much total viewing lies below our observation boundary. We report a lower bound (observed activity only), a preferred estimate (curvature-corrected), and a sensitivity envelope across different modeling assumptions.

**Part 3: Weighted below-threshold sampling.** For channels below our full-collection threshold, we draw a formal probability-proportional-to-size sample. This means that channels likely to command more public activity have higher inclusion probabilities, concentrating our sample budget where it matters most. Channels with special substantive importance -- those in public affairs, those appearing repeatedly in trending feeds, those with unusually high activity relative to their subscriber count -- are placed in certainty strata (collected with probability 1). This design is statistically superior to simple random sampling in a heavy-tailed system, where an SRS would waste most of its budget on channels with negligible viewership.

This three-part design lets us make three clearly distinguished kinds of claims: near-exact statements about the observed channels above validated thresholds; design-based estimates for the sampled below-threshold range; and bounded platform-wide totals that incorporate the estimated residual tail. That inferential discipline is what separates this project from a "big data dump" -- and it is what will make the findings credible to reviewers at top journals.

**Internal validation.** One of our strongest assets is the ability to backtest our own estimators. We can pretend that only channels above 100k subscribers are "observed" and ask whether our methods correctly recover the known 10k-100k activity mass. We can do the same at the 1M threshold, or using earlier crawl states to predict channels discovered later. These backtests are not hypothetical -- they are built into our analysis pipeline and will appear in every paper.

### Taxonomy: classifying what YouTube is

Raw view counts are meaningless without knowing what kind of content they represent. The taxonomy is therefore the single most important interpretive investment in the project.

We classify every channel on six dimensions:

- **Topic/genre**: music, gaming, entertainment, kids/family, news and public affairs, education, sports, lifestyle, technology, etc.
- **Ownership/affiliation**: independent creator, legacy media, local news, national broadcaster, music label, brand/corporate, government agency, state-affiliated media, etc.
- **Editorial mode**: personality-led, institutional voice, ensemble-hosted, automated compilation, etc. This is separated from ownership because a channel can be legacy-owned but personality-led, or creator-owned but institutionally voiced. The literature emphasizes that this hybridity matters: Newman et al. (2025, p. 10) note that "in practice the dividing lines are extremely fuzzy. Many creators defy categorisation."
- **Language and target market**: primary language plus coarse regional marker.
- **Format profile**: mainly long-form, Shorts-heavy, live/podcast-heavy, clip/archive, mixed.
- **Public-affairs relevance**: a binary flag, plus a second-stage typology for flagged channels (institutional journalism, creator commentary, talk/podcast, advocacy, alternative/partisan media, state-affiliated, satire, explanatory).

The public-affairs second stage is essential. Without it, the project cannot speak to the news-ecosystem questions that the Reuters Institute, Newman et al., and the political communication literature have identified as urgent.

Our classification pipeline combines rules-based matching for obvious cases (VEVO channels, known broadcasters, government agencies), a human-coded seed set of 10,000 channels across two labeling rounds, machine classification trained on the seed set, and LLM-assisted adjudication for hard cases. Human coders are kept blind to model suggestions during first-pass labeling to avoid anchoring bias. We evaluate accuracy using three metrics: standard channel-weighted F1, attention-weighted F1 (which penalizes misclassification of high-view channels more heavily), and design-weighted F1 for the below-threshold sample.

---

## Keystone Paper 1: Mapping YouTube's Attention Economy

*Intended journal: Science or Nature (short report) or PNAS (full version)*

This paper answers the question that the literature has called for most urgently: what is YouTube? It provides the first platform-wide measurement of how attention is distributed across YouTube's channel universe, and it does so using a design that can make bounded claims about the entire platform rather than only its most visible channels.

The paper asks five linked questions:

1. **How concentrated is attention on YouTube?** We report Gini coefficients, top-k attention shares (top 0.1%, 1%, 5%, 10%), HHI by content domain and institutional type, and full rank-size distributions. These are standard concentration metrics that have never been applied at census scale to YouTube.

2. **How much of the platform lies above key thresholds?** We compute threshold-capture curves: the share of total channels and total views accounted for by channels above 1k, 10k, 100k, and 1M subscribers. This directly answers the denominator question -- how much of YouTube's public activity is concentrated in channels we can observe.

3. **How does composition change as the threshold drops?** If you look only at million-subscriber channels, YouTube looks one way. At 10k, it looks different. At 1k, different again. This section shows whether findings about the largest channels generalize or whether the composition of the platform shifts fundamentally as you move down the size distribution. This is one of the most important descriptive questions in the field, and our design is uniquely suited to answer it.

4. **What does the combined census-plus-sample-plus-tail design imply about total platform-wide activity?** We present our tail estimates, with backtests and sensitivity analysis, and compare them to YouTube's own reported totals from earnings calls and public statements.

5. **How different is public-affairs YouTube from the rest of the platform?** We report the share of total activity going to public-affairs channels; the internal split among journalism, commentary, talk shows, advocacy, alternative media, and state-affiliated content; and how that ecology varies across major languages. This is where the paper engages most directly with the journalism and political communication literatures.

The paper's observation window is 8-12 weeks of daily data. No full-census video hydration is required. The denominator backtests and tail estimates are integral to the paper, not relegated to a supplement.

---

## Keystone Paper 2: Stability and Churn in the YouTube Hierarchy

*Intended journal: PNAS or a top field journal (Management Science, Journal of Communication, Political Communication)*

*Requires 6-12 months of panel data.*

This paper addresses a question that the literature identifies as important but that no one has been able to study: how stable is YouTube's hierarchy, and what determines which channels rise, fall, or disappear?

The existing literature documents extreme concentration in YouTube's attention economy, but concentration is a snapshot. It tells you nothing about whether the same channels hold the top positions over time (structural rigidity) or whether there is constant turnover beneath a stable aggregate shape (dynamic churn). These are fundamentally different systems with different implications for creators, policy, and competition.

Our dynamic models are designed to separate these two phenomena. The key measures include:

- **Rank persistence**: the probability that a channel in the top 100, top 1,000, or top 10,000 by weekly views remains in that tier after 1, 4, 13, 26, or 52 weeks.
- **Threshold crossing**: how often channels rise from below 10k subscribers into the fully observed universe, how long they stay, and what predicts whether they hold position or fall back. This is where our below-threshold sample becomes crucial -- it lets us study entry into the hierarchy, not just reshuffling within it.
- **Spike analysis**: when a channel's views spike to 3x its trailing median, does the spike produce a durable baseline shift? We link spikes to specific uploads (using our video metadata) and distinguish spikes caused by Shorts virality from those driven by long-form content.
- **Attrition decomposition**: when channels lose audience, why? We separate dormancy (the channel stops uploading), active decline (the channel keeps uploading but loses viewers), and disappearance (the channel is removed or banned). These are different phenomena with different causes and implications.
- **Volatility**: the standard deviation of log weekly views, computed in rolling 13-week windows. We examine the size-volatility relationship: are small channels inherently more volatile, or is the relationship more complex?

All analyses are run separately by institutional form, language, topic, and format (Shorts-heavy vs. long-form). This matters because Shorts and long-form view counts are not comparable attention units -- YouTube changed Shorts view counting in March 2025 so that a view counts when a Short starts to play, with no minimum watch time.

This paper's contribution is not just empirical. The dynamic models I have built and validated are themselves a methodological contribution that can be applied to other platforms. The combination of census-scale data and purpose-built dynamic models is what makes the paper distinctive.

---

## Additional Papers

### Paper 3: YouTube as a News Ecosystem

YouTube is now a top-four news source in most countries and the dominant one in the Global South, yet "scant scholarly attention has been directed toward YouTube as a news source" (Reveilhac 2024, p. 1). This paper uses our census data plus the public-affairs taxonomy to provide the first comprehensive map of who produces news on YouTube, how much attention it commands, and how the news ecosystem varies across languages and markets.

The key empirical contribution is measuring the attention share of different types of public-affairs content: institutional journalism, creator-led commentary, talk/podcast, advocacy, alternative/partisan media, and state-affiliated content. Newman et al. (2025) document that commentary dominates and is overwhelmingly male, and that right-leaning US commentators are being "exported" to other English-speaking countries. Our data can measure the scale of these phenomena for the first time. The paper also examines whether the displacement of institutional journalism by creator-driven content -- flagged by the Reuters DNR 2025 as an accelerating trend -- shows up in the attention data.

This paper requires the public-affairs second-stage taxonomy but no additional data collection beyond the core pipeline.

### Paper 4: How Many YouTubes? Cross-Linguistic Variation

McGrady et al. (2025) demonstrate that YouTube looks radically different across languages -- Hindi YouTube is dominated by short-form content, Russian YouTube functions as a lifeline for uncensored news, and content categories vary dramatically. But their analysis is based on random samples of a few thousand videos per language. Our near-census allows us to do what they could not: measure the full attention economy separately for each major language, and compare concentration, institutional composition, and topic distribution across the top 10-15 languages on the platform.

The central question is whether YouTube is one platform or many. If the attention economy looks fundamentally different in Hindi, Spanish, Arabic, and English -- different levels of concentration, different institutional mixes, different roles for news and public affairs -- then findings from English-language studies cannot be assumed to generalize.

This paper requires language classification for the full channel universe (from our taxonomy pipeline) but no additional data collection. It could be a companion piece to Paper 1, published together or back-to-back.

### Paper 5: Shorts vs. Long-Form

Violot et al. (2024) present "the first comparative analysis of YouTube Shorts versus regular videos" but note that "short-form videos are currently understudied and large-scale analyses of such data are relatively uncommon" (p. 222). Our data can show how the rise of Shorts is reshaping YouTube's attention economy: what share of total views goes to Shorts, whether Shorts-heavy channels are displacing long-form creators, and whether the Shorts economy has a different concentration structure than long-form YouTube.

This paper requires format classification (from video duration data in our upload frontier) and careful treatment of the March 2025 view-counting change. Analysis should be restricted to the post-change period for any cross-format comparison.

### Paper 6: Creator Economy Inequality

Verwiebe et al. (2025) find a Gini coefficient of 0.89 for YouTube creator earnings among German-speaking channels, and Rieder et al. (2023) document that the top 0.4% of channels capture 62% of views. But both studies are based on small samples. Our data allow us to compute concentration and inequality metrics at census scale and to examine how inequality varies by topic, language, and institutional form.

The central question is whether YouTube follows winner-take-all dynamics, long-tail dynamics, or both simultaneously -- a question that Verwiebe et al. (2025) pose but cannot resolve with their data. Our rank-size analysis, threshold-capture curves, and cross-category Gini comparisons provide the empirical leverage to answer it.

This paper draws entirely from the core pipeline and could be drafted in parallel with Paper 1.

### Paper 7: Event-Driven Attention Reallocation

When a major news event occurs -- a natural disaster, an election, a war, a policy shock -- how does YouTube's attention economy respond? This paper uses a prospective difference-in-differences design: we establish baseline attention patterns for event-relevant channels and topics, then measure how attention reallocates in the 48-72 hours following a qualifying event.

This paper requires the upload frontier data (to identify event-relevant videos by title keywords) and a pre-registered event calendar. It cannot be written until we have both sufficient baseline data and at least one qualifying event.

### Paper 8: Deplatforming Spillovers

When YouTube removes a channel, what happens to the channels in its audience network? Do viewers migrate to similar channels, disperse, or leave the topic entirely? This paper uses our census data to identify channels that share audience overlap with removed channels (via co-subscription patterns or comment overlap from our API enrichment), then tracks the viewership trajectories of these neighboring channels after the removal event.

This paper extends the work of Rauchfleisch and Kaiser (2024) on deplatforming effects, but with a much larger observation window and the ability to track audience-level spillovers rather than just channel-level outcomes. It requires prospective tracking of channel availability states (already part of our discovery registry) and at least one significant deplatforming event during our observation period.

### Paper 9: Platform Substitutability

What happens to YouTube when a competitor is disrupted? The 2020 TikTok ban in India provides a natural experiment -- McGrady et al. (2025) document that "the culture of short-form video creation cultivated by TikTok migrated over to YouTube" (p. 17). A potential TikTok disruption in the United States or other markets would provide a prospective natural experiment. This paper would use our baseline data to measure whether YouTube viewership increases, whether the increase is concentrated in Shorts, and which channel types benefit most.

This paper is contingent on a qualifying external shock. The data infrastructure is ready; the analysis waits on events.

### Paper 10: Coordinated Inauthentic Behavior

Can we detect networks of channels with suspiciously synchronized growth patterns, templated metadata, or coordinated upload timing? Our discovery registry and daily view data provide the raw material for anomaly detection. This paper would identify candidate networks using synchronized growth signatures, then validate candidates against metadata similarity (descriptions, tags, external links) and upload timing patterns.

This paper requires approximately three months of daily data for reliable growth-synchrony detection and draws on the discovery registry, daily views, and channel metadata from the API enrichment layer.

---

## Risk Register

**Overclaiming completeness.** The biggest reputational risk for this project is saying we have "the whole platform" when we do not. Every public claim must be threshold-specific and backed by diagnostics. We say "effectively complete above 100k subscribers" only if we can show saturation curves, declining discovery rates, and audit-based miss rates that support that claim. We say "bounded estimate of total platform activity" only with explicit sensitivity analysis and backtests. The inferential discipline of distinguishing observed, sampled, and estimated claims is not just a methodological nicety -- it is the difference between a credible paper and one that gets shredded in review.

**Sensitivity to tail-model choice.** Our platform-wide activity estimates depend on how we model the tail of the rank-size distribution. A naive power law will overestimate residual activity; our curvature-corrected estimator is tighter but depends on modeling assumptions. The mitigation is to report the pure Pareto case as a loose upper bound, report curvature-corrected alternatives as preferred estimates, vary the censoring boundary, and show that backtests on known ranges produce accurate results. If reviewers can see that the estimator recovers known mass in the 10k-100k range when trained only on 100k+ data, the tail estimates become much more credible.

**Frame missingness below the take-all threshold.** Even with 200 million channels in our registry, our below-threshold sample can only include channels we know about. If there are systematic blind spots -- entire language communities, niche topics, or geographic regions where our discovery process underperforms -- the PPS sample will miss them. The mitigation is to combine the sample with binwise missing-mass adjustment, to run stratified completeness diagnostics by language and region, and to use trending and search audits as independent checks on whether our frame is missing important channels.

**Misspecification of the sampling model.** Our PPS sampling weights depend on a model that predicts activity from subscribers and other observables. If that model is badly wrong -- if the relationship between subscribers and views is very different for channels we have not yet observed -- our below-threshold estimates will be biased. The mitigation is to estimate the model flexibly (with interactions, nonlinearity, and language-specific slopes), to validate it on channels that later cross into the fully observed universe, and to be transparent about the model's limitations.

**Cross-language and public-affairs blind spots.** Our discovery process may systematically underperform in languages or topic areas where we lack seed channels. If Arabic-language news channels or Southeast Asian gaming channels are underrepresented in our initial crawl, they will also be underrepresented in our saturation diagnostics -- creating a false sense of completeness. The mitigation is stratified completeness diagnostics, multilingual annotation with native-language coders, and explicit oversampling of public-affairs channels in our certainty strata.

**Taxonomy error compounding across analyses.** Every downstream analysis depends on the taxonomy. If our classifier systematically misassigns channels -- confusing commentary with news, or misidentifying institutional form -- those errors propagate into the composition, public-affairs, and cross-linguistic analyses. The mitigation is the attention-weighted evaluation metric (so that misclassifying a high-view channel counts more than misclassifying a low-view one), dual-coding of the highest-attention channels, and a transparent confusion matrix in every paper.

**Shorts format instability.** YouTube changed how Shorts views are counted in March 2025, and the format continues to evolve rapidly. Any comparison of Shorts and long-form view counts as comparable attention units is methodologically suspect. The mitigation is format-separated analysis throughout: we compute concentration, composition, and mobility metrics separately for Shorts-heavy and long-form channels, and we document the view-counting discontinuity in every paper that touches format.

**Platform-policy and governance shocks.** YouTube may change its content moderation policies, demonetize categories of channels, alter its recommendation algorithm, or restrict API access during our observation period. Any of these could create discontinuities in our data that are platform-caused rather than organic. The mitigation is prospective: we store channel availability states daily, maintain a policy-change calendar, and decompose observed attrition into dormancy, active decline, and disappearance/removal so that governance-caused disruptions can be identified and analyzed rather than confounded with organic dynamics.

**API fragility and quota risk.** Our API enrichment layer depends on continued access to the YouTube Data API v3 at our current quota allocation. YouTube could reduce quotas, restrict endpoints, or revoke access. The mitigation is structural: our permanent data backbone (the core audience panel) does not depend on the API. The API layer is a rolling cache for metadata and enrichment. If API access is curtailed, we lose the ability to build new dossiers and hydrate new videos, but the longitudinal audience data continues to accumulate. We also maintain compliance discipline: we stay well under our quota allocation, refresh cached data within the 30-day window, and document our research purpose in case of audit.

**Temporal validity.** YouTube evolves fast. Any description of the platform is a snapshot that may not hold six months later. The mitigation is the longitudinal panel itself: Paper 2 directly measures how much the platform changes over time, and we can re-run Paper 1's cross-sectional analysis at later time points to assess stability. But we should not oversell the permanence of any single snapshot.

---

## Timeline

| Period | Milestone |
|--------|-----------|
| Weeks 1-3 | Discovery registry and completeness dashboards; taxonomy codebook; denominator backtest design |
| Weeks 3-6 | Round 1 labeling (5,000 channels); below-threshold sample design; initial completeness and tail estimates |
| Weeks 6-9 | Round 2 labeling; taxonomy v1; missing-mass estimates; sample-weight calibration |
| Weeks 9-12 | Paper 1 analyses: concentration, composition, threshold-capture, public-affairs ecology |
| Weeks 12-16 | Paper 1 writing, validation appendix, submission |
| Months 4-6 | Preliminary Paper 2: rank persistence, threshold crossing, spike analysis |
| Months 6-12 | Full Paper 2: 12-month panel, survival analysis, format-separated dynamics |
| Ongoing | Smaller papers drafted in parallel as data and events permit |
