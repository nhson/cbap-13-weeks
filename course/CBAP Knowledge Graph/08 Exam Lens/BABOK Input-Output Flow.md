---
type: "exam"
tags:
  - "cbap/exam"
  - "cbap/io"
---

# BABOK Input–Output Flow

Which task feeds which: an arrow means an **output** of one task is a formal **input** of the other. Guidelines are left out to keep it readable; see each task note for those. 38 task-to-task handoffs.

```mermaid
graph LR
  subgraph K3["BAPM"]
    T3_1["3.1 Plan Business Analysis Approach"]
    T3_2["3.2 Plan Stakeholder Engagement"]
    T3_3["3.3 Plan Business Analysis Governance"]
    T3_4["3.4 Plan Business Analysis Information Management"]
    T3_5["3.5 Identify Business Analysis Performance Improvements"]
  end
  subgraph K4["E&C"]
    T4_1["4.1 Prepare for Elicitation"]
    T4_2["4.2 Conduct Elicitation"]
    T4_3["4.3 Confirm Elicitation Results"]
    T4_4["4.4 Communicate Business Analysis Information"]
    T4_5["4.5 Manage Stakeholder Collaboration"]
  end
  subgraph K5["RLCM"]
    T5_1["5.1 Trace Requirements"]
    T5_2["5.2 Maintain Requirements"]
    T5_3["5.3 Prioritize Requirements"]
    T5_4["5.4 Assess Requirements Changes"]
    T5_5["5.5 Approve Requirements"]
  end
  subgraph K6["SA"]
    T6_1["6.1 Analyze Current State"]
    T6_2["6.2 Define Future State"]
    T6_3["6.3 Assess Risks"]
    T6_4["6.4 Define Change Strategy"]
  end
  subgraph K7["RADD"]
    T7_1["7.1 Specify and Model Requirements"]
    T7_2["7.2 Verify Requirements"]
    T7_3["7.3 Validate Requirements"]
    T7_4["7.4 Define Requirements Architecture"]
    T7_5["7.5 Define Design Options"]
    T7_6["7.6 Analyze Potential Value and Recommend Solution"]
  end
  subgraph K8["SE"]
    T8_1["8.1 Measure Solution Performance"]
    T8_2["8.2 Analyze Performance Measures"]
    T8_3["8.3 Assess Solution Limitations"]
    T8_4["8.4 Assess Enterprise Limitations"]
    T8_5["8.5 Recommend Actions to Increase Solution Value"]
  end
  T3_1 --> T3_2
  T3_1 --> T3_3
  T3_1 --> T3_4
  T3_1 --> T3_5
  T3_2 --> T3_3
  T3_2 --> T3_4
  T3_2 --> T4_1
  T3_2 --> T4_4
  T3_2 --> T4_5
  T3_2 --> T6_4
  T3_3 --> T3_4
  T3_4 --> T7_4
  T3_5 --> T4_5
  T4_1 --> T4_2
  T4_2 --> T4_3
  T4_3 --> T6_3
  T5_3 --> T6_3
  T6_1 --> T6_2
  T6_1 --> T6_4
  T6_1 --> T8_4
  T6_2 --> T6_3
  T6_2 --> T6_4
  T6_2 --> T7_6
  T6_2 --> T8_1
  T6_2 --> T8_2
  T6_3 --> T6_4
  T6_4 --> T7_4
  T6_4 --> T7_5
  T7_1 --> T7_2
  T7_1 --> T7_3
  T7_2 --> T5_5
  T7_4 --> T7_5
  T7_5 --> T7_6
  T8_1 --> T8_2
  T8_2 --> T8_3
  T8_2 --> T8_4
  T8_3 --> T8_5
  T8_4 --> T8_5
```

## Handoff table
| From task | Work product | To task |
|---|---|---|
| [[Plan Business Analysis Approach|3.1 Plan Business Analysis Approach]] | [[Business Analysis Approach]] | [[Plan Stakeholder Engagement|3.2 Plan Stakeholder Engagement]] |
| [[Plan Business Analysis Approach|3.1 Plan Business Analysis Approach]] | [[Business Analysis Approach]] | [[Plan Business Analysis Governance|3.3 Plan Business Analysis Governance]] |
| [[Plan Business Analysis Approach|3.1 Plan Business Analysis Approach]] | [[Business Analysis Approach]] | [[Plan Business Analysis Information Management|3.4 Plan Business Analysis Information Management]] |
| [[Plan Business Analysis Approach|3.1 Plan Business Analysis Approach]] | [[Business Analysis Approach]] | [[Identify Business Analysis Performance Improvements|3.5 Identify Business Analysis Performance Improvements]] |
| [[Plan Stakeholder Engagement|3.2 Plan Stakeholder Engagement]] | [[Stakeholder Engagement Approach]] | [[Plan Business Analysis Governance|3.3 Plan Business Analysis Governance]] |
| [[Plan Stakeholder Engagement|3.2 Plan Stakeholder Engagement]] | [[Stakeholder Engagement Approach]] | [[Plan Business Analysis Information Management|3.4 Plan Business Analysis Information Management]] |
| [[Plan Stakeholder Engagement|3.2 Plan Stakeholder Engagement]] | [[Stakeholder Engagement Approach]] | [[Prepare for Elicitation|4.1 Prepare for Elicitation]] |
| [[Plan Stakeholder Engagement|3.2 Plan Stakeholder Engagement]] | [[Stakeholder Engagement Approach]] | [[Communicate Business Analysis Information|4.4 Communicate Business Analysis Information]] |
| [[Plan Stakeholder Engagement|3.2 Plan Stakeholder Engagement]] | [[Stakeholder Engagement Approach]] | [[Manage Stakeholder Collaboration|4.5 Manage Stakeholder Collaboration]] |
| [[Plan Stakeholder Engagement|3.2 Plan Stakeholder Engagement]] | [[Stakeholder Engagement Approach]] | [[Define Change Strategy|6.4 Define Change Strategy]] |
| [[Plan Business Analysis Governance|3.3 Plan Business Analysis Governance]] | [[Governance Approach]] | [[Plan Business Analysis Information Management|3.4 Plan Business Analysis Information Management]] |
| [[Plan Business Analysis Information Management|3.4 Plan Business Analysis Information Management]] | [[Information Management Approach]] | [[Define Requirements Architecture|7.4 Define Requirements Architecture]] |
| [[Identify Business Analysis Performance Improvements|3.5 Identify Business Analysis Performance Improvements]] | [[Business Analysis Performance Assessment]] | [[Manage Stakeholder Collaboration|4.5 Manage Stakeholder Collaboration]] |
| [[Prepare for Elicitation|4.1 Prepare for Elicitation]] | [[Elicitation Activity Plan]] | [[Conduct Elicitation|4.2 Conduct Elicitation]] |
| [[Conduct Elicitation|4.2 Conduct Elicitation]] | [[Elicitation Results (unconfirmed)]] | [[Confirm Elicitation Results|4.3 Confirm Elicitation Results]] |
| [[Confirm Elicitation Results|4.3 Confirm Elicitation Results]] | [[Elicitation Results (confirmed)]] | [[Assess Risks|6.3 Assess Risks]] |
| [[Prioritize Requirements|5.3 Prioritize Requirements]] | [[Requirements (prioritized)]] | [[Assess Risks|6.3 Assess Risks]] |
| [[Analyze Current State|6.1 Analyze Current State]] | [[Business Requirements]] | [[Define Future State|6.2 Define Future State]] |
| [[Analyze Current State|6.1 Analyze Current State]] | [[Current State Description]] | [[Define Change Strategy|6.4 Define Change Strategy]] |
| [[Analyze Current State|6.1 Analyze Current State]] | [[Current State Description]] | [[Assess Enterprise Limitations|8.4 Assess Enterprise Limitations]] |
| [[Define Future State|6.2 Define Future State]] | [[Business Objectives]], [[Potential Value]] | [[Assess Risks|6.3 Assess Risks]] |
| [[Define Future State|6.2 Define Future State]] | [[Future State Description]] | [[Define Change Strategy|6.4 Define Change Strategy]] |
| [[Define Future State|6.2 Define Future State]] | [[Potential Value]] | [[Analyze Potential Value and Recommend Solution|7.6 Analyze Potential Value and Recommend Solution]] |
| [[Define Future State|6.2 Define Future State]] | [[Business Objectives]] | [[Measure Solution Performance|8.1 Measure Solution Performance]] |
| [[Define Future State|6.2 Define Future State]] | [[Potential Value]] | [[Analyze Performance Measures|8.2 Analyze Performance Measures]] |
| [[Assess Risks|6.3 Assess Risks]] | [[Risk Analysis Results]] | [[Define Change Strategy|6.4 Define Change Strategy]] |
| [[Define Change Strategy|6.4 Define Change Strategy]] | [[Solution Scope]] | [[Define Requirements Architecture|7.4 Define Requirements Architecture]] |
| [[Define Change Strategy|6.4 Define Change Strategy]] | [[Change Strategy]] | [[Define Design Options|7.5 Define Design Options]] |
| [[Specify and Model Requirements|7.1 Specify and Model Requirements]] | [[Requirements (specified and modelled)]] | [[Verify Requirements|7.2 Verify Requirements]] |
| [[Specify and Model Requirements|7.1 Specify and Model Requirements]] | [[Requirements (specified and modelled)]] | [[Validate Requirements|7.3 Validate Requirements]] |
| [[Verify Requirements|7.2 Verify Requirements]] | [[Requirements (verified)]] | [[Approve Requirements|5.5 Approve Requirements]] |
| [[Define Requirements Architecture|7.4 Define Requirements Architecture]] | [[Requirements Architecture]] | [[Define Design Options|7.5 Define Design Options]] |
| [[Define Design Options|7.5 Define Design Options]] | [[Design Options]] | [[Analyze Potential Value and Recommend Solution|7.6 Analyze Potential Value and Recommend Solution]] |
| [[Measure Solution Performance|8.1 Measure Solution Performance]] | [[Solution Performance Measures]] | [[Analyze Performance Measures|8.2 Analyze Performance Measures]] |
| [[Analyze Performance Measures|8.2 Analyze Performance Measures]] | [[Solution Performance Analysis]] | [[Assess Solution Limitations|8.3 Assess Solution Limitations]] |
| [[Analyze Performance Measures|8.2 Analyze Performance Measures]] | [[Solution Performance Analysis]] | [[Assess Enterprise Limitations|8.4 Assess Enterprise Limitations]] |
| [[Assess Solution Limitations|8.3 Assess Solution Limitations]] | [[Solution Limitation]] | [[Recommend Actions to Increase Solution Value|8.5 Recommend Actions to Increase Solution Value]] |
| [[Assess Enterprise Limitations|8.4 Assess Enterprise Limitations]] | [[Enterprise Limitation]] | [[Recommend Actions to Increase Solution Value|8.5 Recommend Actions to Increase Solution Value]] |

> [!tip] How to study this
> Cover the right-hand column and recall where each output goes next. "What should the BA do next?" questions are usually answered by this table.

Up: [[Exam Blueprint]]
