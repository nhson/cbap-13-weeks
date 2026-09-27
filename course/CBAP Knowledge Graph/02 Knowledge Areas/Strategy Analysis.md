---
type: "knowledge-area"
babok: "Chapter 6"
exam_weight: 15
short: "SA"
tags:
  - "cbap/ka"
  - "cbap/ka/SA"
aliases:
  - "SA"
---

# Strategy Analysis (SA)

> [!info] Exam weight: **15%** of CBAP questions (≈18 of 120)
> Define the business need, current state, future state, risks, and the change strategy that bridges them.

## Tasks
| Task | Purpose | Outputs |
|---|---|---|
| [[Analyze Current State|6.1 Analyze Current State]] | Understand why the enterprise needs to change and what the change would affect, starting from how things work today. | [[Current State Description]], [[Business Requirements]] |
| [[Define Future State|6.2 Define Future State]] | Describe the target conditions that would satisfy the business need, including measurable objectives and the value expected. | [[Business Objectives]], [[Future State Description]], [[Potential Value]] |
| [[Assess Risks|6.3 Assess Risks]] | Identify and weigh the uncertainties that could reduce value during the transition or in the future state, and recommend how to proceed. | [[Risk Analysis Results]] |
| [[Define Change Strategy|6.4 Define Change Strategy]] | Compare ways of getting from the current to the future state, pick one, and define the solution scope and transition path. | [[Change Strategy]], [[Solution Scope]] |

## Input → task → output flow
```mermaid
graph LR
  T6_1["6.1 Analyze Current State"]:::task
  T6_2["6.2 Define Future State"]:::task
  T6_3["6.3 Assess Risks"]:::task
  T6_4["6.4 Define Change Strategy"]:::task
  N0(["Elicitation Results"]) --> T6_1
  N1(["Needs"]) --> T6_1
  T6_1 --> N2(["Current State Description"])
  T6_1 --> N3(["Business Requirements"])
  N3(["Business Requirements"]) --> T6_2
  T6_2 --> N4(["Business Objectives"])
  T6_2 --> N5(["Future State Description"])
  T6_2 --> N6(["Potential Value"])
  N4(["Business Objectives"]) --> T6_3
  N7(["Elicitation Results (confirmed)"]) --> T6_3
  N8(["Influences"]) --> T6_3
  N6(["Potential Value"]) --> T6_3
  N9(["Requirements (prioritized)"]) --> T6_3
  T6_3 --> N10(["Risk Analysis Results"])
  N2(["Current State Description"]) --> T6_4
  N5(["Future State Description"]) --> T6_4
  N10(["Risk Analysis Results"]) --> T6_4
  N11(["Stakeholder Engagement Approach"]) --> T6_4
  T6_4 --> N12(["Change Strategy"])
  T6_4 --> N13(["Solution Scope"])
  classDef task fill:#e8f0fe,stroke:#4a6fa5;
```

**Inputs from outside this KA:** [[Elicitation Results]], [[Elicitation Results (confirmed)]], [[Influences]], [[Needs]], [[Requirements (prioritized)]], [[Stakeholder Engagement Approach]]


## Most-used techniques in this KA
- [[Business Cases]] — used in 4 of 4 tasks
- [[Financial Analysis]] — used in 4 of 4 tasks
- [[Interviews]] — used in 4 of 4 tasks
- [[Lessons Learned]] — used in 4 of 4 tasks
- [[Mind Mapping]] — used in 4 of 4 tasks
- [[Workshops]] — used in 4 of 4 tasks
- [[Benchmarking and Market Analysis]] — used in 3 of 4 tasks
- [[Brainstorming]] — used in 3 of 4 tasks
- [[Business Capability Analysis]] — used in 3 of 4 tasks
- [[Business Model Canvas]] — used in 3 of 4 tasks
- [[Decision Analysis]] — used in 3 of 4 tasks
- [[Functional Decomposition]] — used in 3 of 4 tasks

> [!tip] Exam lens
> - Flow to memorize: Current State → Future State → Assess Risks → Change Strategy.
> - Business Requirements are born in Analyze Current State (6.1) — the "why" of the change.
> - Define Change Strategy outputs BOTH Change Strategy and Solution Scope.
> - Transition states and release planning live in 6.4, not in RADD.

## Study guides
- **BABOK v3** chapter 6
- **Lessing** ch.9 *Strategy Analysis*, pp.185–228 (incl. knowledge quiz)
- **Jonasson** Ch 7 Strategy Analysis, from p.141

Up: [[00 CBAP Knowledge Graph]]
