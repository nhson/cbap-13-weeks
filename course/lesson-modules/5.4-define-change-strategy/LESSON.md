# Lesson 5.4: 6.4 Define Change Strategy

*Module 5 · Week 6 · ~85 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Define Change Strategy](CBAP%20Knowledge%20Graph/03%20Tasks/Define%20Change%20Strategy.md)
- [Change Strategy](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Change%20Strategy.md)
- [Solution Scope](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Solution%20Scope.md)
- [Business Cases](CBAP%20Knowledge%20Graph/05%20Techniques/Business%20Cases.md)
- [Scope Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Scope%20Modelling.md)

---

Current state: done. Future state: done. Risks: done. Now: *how do we get there?* **6.4 Define Change Strategy** produces the two outputs that frame everything in RADD: the **Change Strategy** and the **Solution Scope**.

By the end of this session you will be able to:
- Know the 5 elements of 6.4
- Perform gap analysis and an enterprise readiness assessment
- Define transition states and release planning
- Include "do nothing" and opportunity cost in the alternatives

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Define Change Strategy

ACTION: Re-read [Define Change Strategy](CBAP%20Knowledge%20Graph/03%20Tasks/Define%20Change%20Strategy.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Compare ways of getting from the current to the future state, pick one, and define the solution scope and transition path.
- Elements: Solution Scope, Gap Analysis, Enterprise Readiness Assessment, Change Strategy (alternatives including do nothing, opportunity cost, investment, timeline), Transition States and Release Planning.
- Opportunity cost: the benefits forgone by choosing one alternative over another.
- Inputs: Current State Description, Future State Description, Risk Analysis Results, Stakeholder Engagement Approach. Outputs: **Change Strategy** and **Solution Scope**.

STOP: What's the difference between the Change Strategy and the Solution Scope?

USER: Strategy = how to transition; scope = what the solution includes

ACTION: Give feedback. A strong answer includes: Change Strategy = the approach to move from current to future state (transition states, releases, readiness). Solution Scope = the boundaries of the solution (capabilities in and out).

**Exam trap to call out:** Both are outputs of 6.4. Distractors credit Solution Scope to RADD.

---

## Apply it at GreenBasket: Change strategy for Click & Collect

Compare real alternatives and design the path.

ACTION: Open and skim [40-current-state-description](workspace/40-current-state-description.md), [41-future-state-description](workspace/41-future-state-description.md), [42-risk-analysis-results](workspace/42-risk-analysis-results.md), [13-vendor-proposals](case-files/13-vendor-proposals.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Produce: (1) a gap analysis (current → future per capability), (2) an enterprise readiness assessment (cultural, operational, technical), (3) 3 change strategy alternatives including "do nothing", with opportunity cost, (4) transition states (e.g. data-fix → 6-store pilot → wave rollout), and (5) the solution scope (in and out, incl. delivery and recipes).

USER: Drafts their analysis in the chat

ACTION: Coach and save with a scope model (context diagram in Mermaid) and a transition roadmap. Readiness gaps: store incentives, union, inventory accuracy, handhelds. Save the result to `workspace/43-change-strategy-and-solution-scope.md` and link it: [43-change-strategy-and-solution-scope.md](workspace/43-change-strategy-and-solution-scope.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `marcus-store-ops`, giving it the path `workspace/43-change-strategy-and-solution-scope.md` and ask whether the readiness assessment and transition states are realistic for stores. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

**Discovery:** The readiness assessment predicts the exact problems the pilot will show in week 9 (incentives, aisle data). Keep this file. You'll compare it with the real results.

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 6.4 elements, gap analysis, enterprise readiness, alternatives incl. do nothing and opportunity cost, transition states, outputs.
Build distractors from these traps: Solution Scope from RADD; change strategy = project plan; readiness only technical; no do-nothing option.
Log to scores.csv with ka=`SA` and topic=`6.4`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 6.4 outputs: Change Strategy + Solution Scope.
2. Readiness is cultural, operational and technical.
3. Always evaluate "do nothing" and opportunity cost.

> **Exam rule of thumb:** Transition states and release planning belong to the change strategy (6.4), not to RADD.

**Reading before the next session:**
- BABOK 6.4 (pp.124–131), 10.41 Scope Modelling
- Lessing pp.211–228 (incl. knowledge quiz)
- Jonasson 7.3.3–7.3.4 (pp.152–155)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 6.4 elements? :: Solution Scope; Gap Analysis; Enterprise Readiness Assessment; Change Strategy; Transition States & Release Planning
- 6.4 outputs? :: Change Strategy; Solution Scope
- Opportunity cost? :: The benefits forgone by choosing one alternative over another

ACTION: Update [progress.json](progress/progress.json): add this lesson (`5.4`) to `completed` with today's date and minutes ≈ 85, set `current` to `5.5`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 5.5: Lab: business case & financial analysis (NPV, IRR, ROI, payback). The CFO wants numbers. You give numbers.

STOP: Ready for 5.5? Type `/next` (or `/start 5.5`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/43-change-strategy-and-solution-scope.md created and Marcus-reviewed
- [ ] Do-nothing option included
- [ ] Drill logged; task card added
