# Evidence Tiers

Every source in the atlas is assigned exactly one evidence tier. The
tier controls what kinds of claims the source can support in wiki
synthesis.

## Tier definitions

| Tier | Source Types | Can Support |
|------|--------------|-------------|
| `primary_empirical` | Peer-reviewed journal articles, published working papers with original data, preregistered reports. | Any empirical, methodological, or theoretical claim. |
| `secondary_analytical` | Systematic reviews, meta-analyses, book chapters, handbooks. | Synthesis claims. Must trace specific empirical findings back to the underlying primary source. |
| `industry_report` | Reuters Digital News Report, Pew Research, Ofcom, platform transparency reports, Oxford Economics reports. | Usage statistics, descriptive trends, platform policy facts. **Cannot** support causal claims or scholarly consensus. |
| `project_internal` | Census project memos, internal methods notes, draft literature reviews authored by project members. | Project-context claims **only** — what the project plans, believes, or needs. Never cited as evidence about YouTube or the broader literature. |
| `platform_documentation` | YouTube API docs, help pages, policy announcements, Terms of Service versions. | Technical facts about the platform (what an endpoint returns, what a policy says). Not evidence about behavior or effects. |
| `news_commentary` | Journalism, trade-press coverage, opinion pieces. | Context and framing only. Rarely cited in wiki synthesis; when cited, the tier must be explicit. |

## Agent enforcement rules

These rules are load-bearing. Agents must honor them when drafting any
synthesis page.

### 1. Tier transparency in weak-evidence contexts

When a wiki claim is supported only by `industry_report` sources, add
an explicit note:

> *[Note: supported only by non-peer-reviewed sources.]*

This applies to usage statistics, share-of-attention numbers, and
trend claims sourced from Reuters DNR, Pew, Ofcom, and similar outlets.

### 2. Project-internal firewall

Never cite a `project_internal` source as evidence **about YouTube**
or **about the broader literature**. `project_internal` sources can
only support claims of the form:

- "The Census project plans to …"
- "The Census memo identifies … as a core methodological goal."
- "The project's literature review flags … as an open question."

If you catch yourself writing "McGrady et al. show that … (Census
memo, p. 4)" — stop. That is a category error.

### 3. Secondary synthesis must trace

When citing a `secondary_analytical` source (e.g., Yesilada &
Lewandowsky 2022), do not stop at the review's summary statement.
Identify the specific primary sources the review cites for the claim
and add them to the source registry (if not already present) and the
relevant source cards. A synthesis claim that cannot be traced to
primary sources is not yet a wiki-ready claim.

### 4. Temporal scope is mandatory for recommendation/radicalization claims

Claims about YouTube's recommendation system's behavior or effects
must state the time period the underlying data covers. YouTube's
algorithm and policies changed meaningfully in 2019 and again after
2022. Do not flatten findings from different periods into a single
present-tense consensus. See `data/project-taxonomy.yaml` for the
full list of themes where temporal scoping is required.

### 5. Conflict preservation

If two sources at the same tier disagree, the disagreement must
appear in synthesis — either in the consensus-vs-disagreement
structure of a theme page or as its own debate page. Do not silently
pick a side.

### 6. Mixed-tier claims

If a claim is supported by both `primary_empirical` and
`industry_report` sources, the citation list can include both, but
the strength of the claim is anchored by the primary sources. Never
use an industry report as a "second opinion" that boosts confidence
in a weakly-supported primary finding — tiering is a floor on
credibility, not a quorum system.

## Tier assignment at ingest time

When a new source is ingested, the `ingest-source` skill assigns a
tier based on venue and provenance:

- Appears in a peer-reviewed journal or conference proceedings →
  `primary_empirical`.
- Published working paper with original data (e.g., NBER, SSRN with
  clear author affiliations and methods section) → `primary_empirical`.
- A review that does not introduce new data → `secondary_analytical`.
- Authored by a research-adjacent industry org (Reuters Institute,
  Pew, Ofcom, Oxford Economics) → `industry_report`.
- Authored by the Census project or its collaborators, internal use
  → `project_internal`.
- Issued by YouTube/Google itself as platform-of-record documentation
  → `platform_documentation`.
- Journalism or op-ed → `news_commentary`.

Edge cases (e.g., a Pew report that presents novel survey methodology;
a preprint that has not yet been peer reviewed) should be flagged in
`ops/log.md` with a tier proposal and resolved by a human.
