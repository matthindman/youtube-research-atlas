---
type: method-page
canonical_name: recommendation_audit
title: "Recommendation Audit"
status: machine-draft
method_family: audit
themes_touched:
  - recommendation-radicalization
project_modules:
  - public-affairs
last_refreshed: 2026-04-15
verification:
  machine_extracted: 18
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
---

# Recommendation Audit

## What This Method Is

[LIT] Recommendation-audit methods try to observe what the platform
would recommend under specified user conditions, usually by
constructing controlled accounts, scripted histories, or other
repeatable exposure states. In the current atlas, Haroon et al.
(2023) is the canonical exemplar because it uses 100,000 trained sock
puppets to isolate recommendation behavior at scale and then
separates congeniality, extremity, and problematic-channel exposure
as distinct outcomes (Haroon et al. 2023, pp. 1-8). [🤖]

## Where It Has Been Used

[LIT] The method appears directly in Haroon et al. and in
Hosseinmardi et al., where logged-in counterfactual bots are trained
on real user histories so recommendation-following paths can be
compared against matched browsing trajectories; Lai et al.
contributes measurement infrastructure rather than an audit design
(Haroon et al. 2023, pp. 1-8; Hosseinmardi et al. 2024, pp. 1-3).
[🤖]
[LIT] The method appears directly in Haroon et al. and Brown et al.;
the latter uses real users with randomized traversal rules on their
own accounts, while Lai et al. supplies ideology measurement
infrastructure rather than an audit design (Haroon et al. 2023, pp.
1-8; Brown et al. 2022, pp. 12-14, 26-29). [🤖]

| Source | Data | Sample | Key Design Choice | Verified |
|--------|------|--------|-------------------|----------|
| haroon_et_al_2023 | Sock-puppet watch histories, homepage captures, up-next trails, and video slant scores | 100,000 sock puppets; 15,323,930 watched or recommended videos in total; 120,073 channels | Trains five ideological user profiles, distinguishes homepage from up-next recommendations, and tracks problematic-channel exposure separately from ideological extremity | [🤖] |
| hosseinmardi_et_al_2024 | Nielsen desktop panel histories, logged-in counterfactual bots, and YouTube API metadata | 87,988 panelists in source panel; 4,583 heavy YouTube users; 125 focal users generating 1,304 bot trajectories | Trains bots on exact real-user histories, then compares user-following and rule-based paths to estimate the recommender's causal marginal effect and forgetting time | [🤖] |
| brown_et_al_2022 | Browser-plugin captures of recommendation lists, survey responses, randomized seed videos, and traversal rules | 527 U.S.-based YouTube users following 20 recommendation traversals on their real accounts | Preserves personalization by using real users, then experimentally constrains navigation so recommendation effects can be isolated from unconstrained user choice | [🤖] |
| lai_et_al_2024 | Reddit-YouTube links, video metadata, and 2020 watch histories | 61,883 videos with metadata; 345 respondents and 6,012 political videos in the application | Not an audit by itself, but provides reusable video-level ideology estimates that later audits can plug into exposure measures | [🤖] |

## Strengths and Assumptions

[LIT] Recommendation audits isolate the platform's output more cleanly
than studies that only observe what real users ended up watching,
because they can hold the training history constant and compare
outputs across user profiles. [🤖]

[LIT] They are also highly reproducible within a given platform
regime: a researcher can re-run the same training design, depth, and
capture rules after a policy or product change to see whether outputs
shift. [🤖]

[LIT] The method assumes that the simulated user state is meaningful.
Sock-puppet audits are only as good as the training regimen,
login-state choice, and content categories used to stand in for real
users. [🤖]

## Known Weaknesses

[LIT] Audit outputs are exposure opportunities, not realized user
behavior. They usually do not tell us what users clicked, searched
for, skipped, or believed after seeing the recommendation set. [🤖]

[LIT] Many audits are highly sensitive to the period and product
environment they capture. A design that is informative in one
algorithm regime can age quickly after platform changes. [🤖]

[LIT] Training choices, language, geography, device state, and login
status can all shift the results. Haroon et al., for instance, do not
sign the sock puppets into Google accounts because phone
verification at that scale is infeasible (Haroon et al. 2023, pp.
3-4). [🤖]

## Variants in the Literature

[LIT] The core variants are untrained audits, trained sock puppets,
and real-user or browser-history designs. The current atlas's Haroon
paper is strongest as a trained-sock-puppet middle ground between
construct validity and algorithm isolation. [🤖]

[LIT] Another important variant is whether ideology is measured at
the channel or video level. Lai et al.'s video-level estimator
suggests one path for making future audits more fine-grained. [🤖]

## What the Census Project Does Differently

[PROJECT] The Census project can potentially pair audit outputs with
platform-wide composition data, which would make it easier to judge
whether a low-rate audit finding still has large platform-wide reach.
[🤖]

[PROJECT] The research plan also points toward a richer public-affairs
taxonomy than the standard left-right audit setup, which could let
future audits distinguish journalism, commentary, advocacy, and other
content types rather than treating all political content as one pool.
[🤖]

[PROJECT] If the project runs audits, it should combine them with
direct evidence about observed attention or behavior instead of
treating simulated exposure alone as a full account of user
experience. [🤖]

## Open Methodological Questions

- How should recommendation audits model logged-in states,
  subscriptions, and user choice without losing reproducibility?
  [🤖]
- What is the right audit design for post-2022 and Shorts-era
  discovery environments, where homepage, feed, and autoplay
  pathways may have shifted meaningfully? [🤖]

## Cross-References

- **Themes:** [[recommendation_radicalization]]
- **Related methods:** [[ideology_estimation]]
- **Papers that use this method:** [[haroon_et_al_2023]], [[hosseinmardi_et_al_2024]], [[lai_et_al_2024]]
- **Papers that use this method:** [[haroon_et_al_2023]], [[brown_et_al_2022]], [[lai_et_al_2024]]
