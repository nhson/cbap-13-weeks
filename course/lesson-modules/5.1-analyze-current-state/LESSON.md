# Lesson 5.1: SA overview + 6.1 Analyze Current State

*Module 5 · Week 6 · ~80 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Strategy Analysis](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Strategy%20Analysis.md)
- [Analyze Current State](CBAP%20Knowledge%20Graph/03%20Tasks/Analyze%20Current%20State.md)
- [Current State Description](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Current%20State%20Description.md)
- [Business Requirements](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Business%20Requirements.md)
- [Root Cause Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Root%20Cause%20Analysis.md)
- [SWOT Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/SWOT%20Analysis.md)

---

David Chen, the CFO, won't fund anything until you can explain *why* GreenBasket must change, in evidence, not adjectives. Strategy Analysis (15%) starts with **6.1 Analyze Current State**, the most technique-heavy task in the BABOK (26 techniques).

By the end of this session you will be able to:
- Explain SA's 4 tasks and flow
- Know the 8 elements of 6.1 and its two outputs
- Use root cause analysis and SWOT on real data

STOP: Ready to dive in?

USER: Ready

---

## Part 1: SA at a glance

ACTION: Re-read [Strategy Analysis](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Strategy%20Analysis.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Four tasks: 6.1 Analyze Current State → 6.2 Define Future State → 6.3 Assess Risks → 6.4 Define Change Strategy.
- SA can happen before, during or after a project. It covers the need, the context, and the strategy to get from current to future state.
- SA outputs guide RADD and SE: Business Objectives, Future State Description, Potential Value, Risk Analysis Results, Change Strategy, Solution Scope.

STOP: Put the 4 SA tasks in their logical order.

USER: 6.1 → 6.2 → 6.3 → 6.4

ACTION: Give feedback. A strong answer includes: current → future → risks → change strategy (and it iterates).

---

## Part 2: Analyze Current State

ACTION: Re-read [Analyze Current State](CBAP%20Knowledge%20Graph/03%20Tasks/Analyze%20Current%20State.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Understand why the enterprise needs to change and what the change would affect, starting from how things work today.
- Elements: Business Needs, Organizational Structure and Culture, Capabilities and Processes, Technology and Infrastructure, Policies, Business Architecture, Internal Assets, External Influencers (industry structure, competitors, customers, suppliers, political and regulatory, technology, macroeconomic).
- Business needs can come from the top down, bottom up, middle management, or external drivers. Understand the problem or opportunity, not just the symptom.
- Inputs: Elicitation Results, Needs. Outputs: **Current State Description** and **Business Requirements**.

STOP: Which task outputs Business Requirements?

USER: 6.1 Analyze Current State

ACTION: Give feedback. A strong answer includes: 6.1, together with the Current State Description.

**Exam trap to call out:** Business Requirements do NOT come from Define Future State.

---

## Apply it at GreenBasket: Current State Description + Business Requirements

Build the "why change" case from evidence.

ACTION: Open and skim [05-market-and-sales-data](case-files/05-market-and-sales-data.csv), [04-customer-feedback-q2](case-files/04-customer-feedback-q2.md), [06-competitor-benchmark](case-files/06-competitor-benchmark.md), [07-it-landscape](case-files/07-it-landscape.md), [22-elicitation-results-confirmed](workspace/22-elicitation-results-confirmed.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Draft (1) a fishbone or 5-whys for "visit frequency down 11%", (2) a SWOT, and (3) a current-state summary using the 8 elements (one line each). Then write 3 business requirements (goals and outcomes) that follow from it.

USER: Drafts their analysis in the chat

ACTION: Coach, check SWOT internal/external placement, and save the Current State Description with its business requirements. Include a small table computed from the CSV (share trend, visit frequency trend, competitor online share). Save the result to `workspace/40-current-state-description.md` and link it: [40-current-state-description.md](workspace/40-current-state-description.md).

A model answer should cover (use it to coach, don't just paste it):
- Root causes: no online channel (convenience gap), competitor online share 4.1→11.2%, low digital capability, inventory accuracy 82%
- SWOT: S = loyal members (410k), store footprint, trusted brand; W = no e-commerce, legacy stock system, data quality; O = 71% would use C&C, pickup preference 44%; T = FreshWay/QuickCart, union constraints (external? internal HR policy vs external law: discuss)
- Business requirements: stop share decline; restore visit frequency; achieve an online channel reaching 5% of sales within 2 years of launch

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `cbap-examiner`, giving it the path `workspace/40-current-state-description.md` and check the 8 elements and SWOT placement. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: SA overview and 6.1 elements, business need sources, outputs, root cause analysis, SWOT.
Build distractors from these traps: business requirements from 6.2; SWOT threats as internal; symptom treated as root cause; SA only before projects.
Log to scores.csv with ka=`SA` and topic=`6.1`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 6.1 answers "why change?" with 8 elements.
2. Outputs: Current State Description AND Business Requirements.
3. Find root causes, not symptoms.

> **Exam rule of thumb:** When a stakeholder describes a symptom, the BA first investigates the root cause and the business need.

**Reading before the next session:**
- BABOK 6.0–6.1 (pp.99–109)
- Lessing ch.9 pp.185–198
- Jonasson 7.3.1 (pp.145–150) and 7.6 (p.159)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 6.1 outputs? :: Current State Description; Business Requirements
- 6.1 elements? :: Business Needs; Org Structure & Culture; Capabilities & Processes; Technology & Infrastructure; Policies; Business Architecture; Internal Assets; External Influencers
- SWOT internal vs external? :: Strengths/Weaknesses internal; Opportunities/Threats external

ACTION: Update [progress.json](progress/progress.json): add this lesson (`5.1`) to `completed` with today's date and minutes ≈ 80, set `current` to `5.2`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 5.2: 6.2 Define Future State. Goals, SMART objectives, constraints, assumptions and potential value.

STOP: Ready for 5.2? Type `/next` (or `/start 5.2`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/40-current-state-description.md created and examiner-reviewed
- [ ] Student states 6.1 outputs correctly
- [ ] Drill logged; task card added
