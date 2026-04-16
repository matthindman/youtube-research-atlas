---
source_id: marchal_et_al_2025
type: source-card
status: machine-draft
evidence_tier: primary_empirical
title: "How Negative Media Coverage Impacts Platform Governance: Evidence from Facebook, Twitter, and YouTube"
authors:
  - "Marchal, Nahema"
  - "Hoes, Emma"
  - "Kluser, K. Jonathan"
  - "Hamborg, Felix"
  - "Alizadeh, Meysam"
  - "Kubli, Mael"
  - "Katzenbach, Christian"
year: 2025
venue: "Political Communication"
doi: "10.1080/10584609.2024.2377992"
temporal_scope: "Cross-platform English-language news coverage from 2005-2021 and platform policy changes from 2007-2021, with the sharpest negative-coverage shift after 2018"
themes:
  - governance-data-access
project_modules:
  - api-compliance
census_papers:
  - methods-companion
  - study3-media-system
census_relevance: medium
verification:
  machine_extracted: 18
  human_checked: 0
  publication_ready: 0
  needs_citation: 0
last_updated: 2026-04-16
---

# Marchal et al. (2025) - Negative Media Coverage and Platform Governance

## Full Citation

Marchal, Nahema, Emma Hoes, K. Jonathan Kluser, Felix Hamborg, Meysam Alizadeh, Mael Kubli, and Christian Katzenbach. 2025. "How Negative Media Coverage Impacts Platform Governance: Evidence from Facebook, Twitter, and YouTube." *Political Communication* 42(2): 215-233. https://doi.org/10.1080/10584609.2024.2377992

## One-Sentence Contribution

Using 19,560 English-language news articles and a Platform Governance Archive dataset of policy changes, the paper finds that sustained negative media coverage is associated with more subsequent user-policy change at Facebook, Twitter, and YouTube, highlighting public pressure as part of platform governance (pp. 1-2, 11-14). [🤖]

## Research Question

To what extent is policy change at Facebook, Twitter, and YouTube responsive to negative news coverage, and does that relationship vary by financial performance or by policy-specific criticism? (pp. 1-2, 5-7) [🤖]

## Data, Sample, Geography, and Period

- **Data:** Mainstream English-language newspaper coverage from LexisNexis plus platform policy-change records from the Platform Governance Archive (pp. 1, 6-8). [🤖]
- **Sample:** The final dataset contains 19,560 relevant news articles from 26 US- and UK-based outlets and 252 policy changes across Facebook, Twitter, and YouTube, including 1,997 YouTube articles and 36 YouTube policy changes (pp. 6-8, 11-13). [🤖]
- **Geography:** The media sample comes from influential English-language outlets in the United States and United Kingdom, while the platform evidence covers Facebook, Twitter, and YouTube as global companies (pp. 6-8, 14). [🤖]
- **Period:** News coverage runs from January 1, 2005 through January 1, 2021, and policy-change records run from 2007 through Q1 2021 (pp. 1, 6-8). [🤖]

## Methods

The authors classify and filter platform-governance news coverage with supervised text models, identify negative coverage through targeted sentiment analysis, merge those data with recurrent platform-policy events from the Platform Governance Archive, and estimate the relationship between cumulative negative coverage and future policy changes with a PWP-Gap survival model that includes several controls (pp. 7-13). [🤖]

## Main Findings

1. Sustained negative media coverage is significantly associated with a higher hazard of future platform policy change: in the main model, each unit increase in cumulative negative coverage corresponds to a 6% increase in the likelihood of a new policy change (pp. 11-13). [🤖]
2. Negative media coverage of Facebook, Twitter, and YouTube rises sharply after 2018, consistent with the broader "techlash" period in which platform power became a sustained public and journalistic concern (pp. 1-2, 10-11, 13-14). [🤖]
3. The authors do not find evidence that financial performance significantly moderates the relationship between negative coverage and subsequent policy change (pp. 13-14). [🤖]
4. Policy-specific negative coverage is also associated with policy change, but not more strongly than negative coverage in general, and the strongest estimated effect is concentrated in roughly the first three months after a policy change (pp. 12-15). [🤖]

## Limitations / Scope Conditions

The study is restricted to influential English-language mainstream outlets, so it may miss how platform-policy pressure works in other media systems, languages, or secondary markets (pp. 14-15). [🤖]

The analysis is comparative across Facebook, Twitter, and YouTube, which makes it useful for platform-governance context but less precise for claims about YouTube specifically (pp. 1-2, 6-8, 14-15). [🤖]

The policy-change data come from public-facing policy documents rather than internal governance practices, so the study observes visible policy revision rather than the full internal decision process (pp. 7-8, 14-15). [🤖]

The authors explicitly treat the design as observational and caution that it does not permit causal conclusions about whether negative reporting itself causes policy change (pp. 14-15). [🤖]

## Temporal Scope

This paper is most informative about a pre-DSA, mostly pre-2022 governance environment. It captures the rise of the post-2018 techlash and ends in early 2021, so it should not be read as direct evidence about how YouTube responds to later post-API-restriction, post-2022, or post-October-2025 governance pressures (pp. 1-2, 6-8, 13-15). [🤖]

## Key Quotes

> "We find that sustained negative coverage significantly predicts changes to platforms' user policies..." (p. 1) [🤖]

> "our observational study ... does not permit us to draw causal conclusions about the role of negative media reporting" (p. 15) [🤖]

## Relation to This Project

- **Methods companion:** Useful for showing that governance changes can respond to public scrutiny outside the platform, but also for flagging the limits of observational evidence when internal policy processes remain opaque. [PROJECT]
- **Paper 1 (attention economy):** Minimal direct relevance to attention distributions or creator outcomes. [PROJECT]
- **Paper 2 (mobility):** No direct relevance. [PROJECT]
- **Later studies:** Important comparative context for the governance theme because it shifts attention from creator complaints to external media pressure as a possible driver of policy change. [PROJECT]

## Linked Claims

- `claim_governance_data_access_media_pressure_policy_change`

## Cross-References

- **Themes:** [[governance_data_access]]
- **Methods:** _(none yet)_
- **Debates:** _(none yet)_
- **Related sources:** [[norton_shapiro_2024]], [[hallinan_et_al_2025]]
