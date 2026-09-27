# Lesson 7.4: 8.4 Assess Enterprise Limitations

*Module 7 · Week 9 · ~75 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Assess Enterprise Limitations](CBAP%20Knowledge%20Graph/03%20Tasks/Assess%20Enterprise%20Limitations.md)
- [Enterprise Limitation](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Enterprise%20Limitation.md)
- [16-store-staff-survey](case-files/16-store-staff-survey.md)
- [43-change-strategy-and-solution-scope](workspace/43-change-strategy-and-solution-scope.md)

---

"Nobody's bonus includes online orders, so why would the manager care?" That isn't a software bug. **8.4 Assess Enterprise Limitations** looks at culture, structure and operations *outside* the solution.

By the end of this session you will be able to:
- Know the 4 elements of 8.4
- Assess culture, stakeholder impact, structure and operations
- Compare with your earlier readiness assessment

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Assess Enterprise Limitations

ACTION: Re-read [Assess Enterprise Limitations](CBAP%20Knowledge%20Graph/03%20Tasks/Assess%20Enterprise%20Limitations.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Find the factors in the wider enterprise (culture, structure, operations) that stop the solution from delivering value.
- Elements: Enterprise Culture Assessment (beliefs, values, norms; e.g. incentives), Stakeholder Impact Analysis (functions, locations, concerns), Organizational Structure Changes (formal and informal), Operational Assessment (policies, procedures, capabilities, tools, skills, resources).
- Inputs: Current State Description, Implemented Solution (external), Solution Performance Analysis. Output: Enterprise Limitation. 18 techniques, the most in SE.

STOP: Managers moving pickers to tills during peaks: which element?

USER: Enterprise culture assessment / operational assessment

ACTION: Give feedback. A strong answer includes: enterprise culture (incentives and norms make picking a "cost") plus operational assessment (resource policy). Either is defensible when justified.

---

## Apply it at GreenBasket: Enterprise limitations + readiness look-back

Compare what you predicted in week 6 with what happened.

ACTION: Open and skim [16-store-staff-survey](case-files/16-store-staff-survey.md), [14-pilot-results](case-files/14-pilot-results.md), [43-change-strategy-and-solution-scope](workspace/43-change-strategy-and-solution-scope.md), [61-solution-performance-analysis](workspace/61-solution-performance-analysis.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Using the 4 elements, list the enterprise limitations with evidence. Then compare with your week-6 readiness assessment: what did you predict correctly, and what did you miss?

USER: Drafts their analysis in the chat

ACTION: Coach and save. Key limitations: incentives (picking not in store targets or bonuses → culture); manager priority (Bayview 11%); no aisle-data update procedure after resets (operational); handheld replacement budget (operational resource); picker role and union status (structure). Save the result to `workspace/63-enterprise-limitations.md` and link it: [63-enterprise-limitations.md](workspace/63-enterprise-limitations.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `marcus-store-ops`, giving it the path `workspace/63-enterprise-limitations.md` and ask for his reaction, since incentives are his domain. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

**Discovery:** The best technology in the chain still underperforms where incentives work against it. Value realization is an enterprise problem as much as a software one.

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 8.4 elements, culture, stakeholder impact, structure, operational assessment; enterprise vs solution limitation.
Build distractors from these traps: enterprise limitation fixed by changing software; stakeholder impact analysis vs stakeholder analysis (3.2).
Log to scores.csv with ka=`SE` and topic=`8.4`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Enterprise limitations are OUTSIDE the solution: culture, structure, operations.
2. Elements: culture, stakeholder impact, org structure changes, operational assessment.

> **Exam rule of thumb:** Incentives, culture, policies, skills, org structure → enterprise limitation. Component defects or dependencies → solution limitation.

**Reading before the next session:**
- BABOK 8.4 (pp.177–181)
- Lessing pp.295–300

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 8.4 elements? :: Enterprise Culture Assessment; Stakeholder Impact Analysis; Organizational Structure Changes; Operational Assessment

ACTION: Update [progress.json](progress/progress.json): add this lesson (`7.4`) to `completed` with today's date and minutes ≈ 75, set `current` to `7.5`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 7.5: 8.5 Recommend Actions to Increase Solution Value. Before chain-wide rollout: what should change?

STOP: Ready for 7.5? Type `/next` (or `/start 7.5`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/63-enterprise-limitations.md created and Marcus-reviewed
- [ ] Drill logged; task card added
