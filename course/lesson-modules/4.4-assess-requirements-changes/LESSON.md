# Lesson 4.4: 5.4 Assess Requirements Changes: CR-017 same-day delivery

*Module 4 · Week 5 · ~85 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Assess Requirements Changes](CBAP%20Knowledge%20Graph/03%20Tasks/Assess%20Requirements%20Changes.md)
- [Requirements Change Assessment](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20Change%20Assessment.md)
- [Proposed Change](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Proposed%20Change.md)
- [Financial Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Financial%20Analysis.md)
- [12-change-request-CR-017](case-files/12-change-request-CR-017.md)

---

CR-017 just landed: add same-day delivery to the pilot. +9 weeks, +$640k, alcohol delivery prohibited in State C, and a survey slide that hides the 9% "delivery only" figure. Elena wants a recommendation by Friday. **5.4 Assess Requirements Changes**.

By the end of this session you will be able to:
- Know the 3 elements of 5.4 and the impact analysis factors
- Assess a change against the governance approach and change strategy
- Write an impact assessment and recommendation

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Assess Requirements Changes

ACTION: Re-read [Assess Requirements Changes](CBAP%20Knowledge%20Graph/03%20Tasks/Assess%20Requirements%20Changes.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Work out what a proposed change to requirements or designs would mean (benefit, cost, impact, schedule, urgency) and resolve it through governance.
- Elements: Assessment Formality (per governance approach, predictive vs adaptive), Impact Analysis, Impact Resolution.
- Impact analysis considers: **benefit, cost, impact (on customers, business, solution), schedule, urgency**.
- Impact resolution: approve, modify, or reject (or defer), per the Governance Approach decision rights, with the outcome communicated and recorded.
- Inputs: Proposed Change, Requirements, Designs. Guidelines: Change Strategy, Domain Knowledge, Governance Approach, Legal/Regulatory Information, Requirements Architecture, Solution Scope. Outputs: Requirements Change Assessment, Designs Change Assessment.

STOP: Who decides whether CR-017 is accepted: you, Tom, or someone else?

USER: The decision maker per the governance approach (e.g. the change control board or sponsor)

ACTION: Give feedback. A strong answer includes: whoever the Governance Approach (3.3) names, e.g. the change control board chaired by Elena. The BA assesses and recommends.

**Exam trap to call out:** The BA does not approve or reject changes unilaterally.

---

## Apply it at GreenBasket: Impact assessment of CR-017

Assess the change honestly. The data is incomplete and presented selectively.

ACTION: Open and skim [12-change-request-CR-017](case-files/12-change-request-CR-017.md), [04-customer-feedback-q2](case-files/04-customer-feedback-q2.md), [08-compliance-memo](case-files/08-compliance-memo.md), [02-harvest-postmortem](case-files/02-harvest-postmortem.md), [30-traceability-matrix](workspace/30-traceability-matrix.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Write the impact analysis: benefit (use the full survey data), cost, impact (customers, stores, compliance, solution), schedule, urgency. Which requirements are affected (use traceability)? Then give a recommendation with options (e.g. reject for R1 and defer to R2 with a demand test; modify: pilot delivery in 1 store later; approve with a new date).

USER: Drafts their analysis in the chat

ACTION: Coach and save a Requirements Change Assessment with an options table and a clear recommendation for the change control board. Flag the misleading "47% either" framing (only 9% need delivery) and the State C alcohol prohibition. Save the result to `workspace/33-cr-017-change-assessment.md` and link it: [33-cr-017-change-assessment.md](workspace/33-cr-017-change-assessment.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `elena-sponsor`, giving it the path `workspace/33-cr-017-change-assessment.md` and present the recommendation for decision. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

**Discovery:** Harvest died partly of delivery complexity. The traceability matrix plus impact analysis gives you an evidence-based "not now", not a political one.

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 5.4 elements, impact analysis factors, impact resolution, role of governance, formality in predictive vs adaptive.
Build distractors from these traps: BA approves the change; implement then assess; change assessment vs change strategy; skip assessment for urgent changes.
Log to scores.csv with ka=`RLCM` and topic=`5.4`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Assess formality, analyze impact (benefit, cost, impact, schedule, urgency), resolve per governance.
2. Traceability makes impact analysis possible.
3. The BA recommends; the decision makers decide.

> **Exam rule of thumb:** Urgent change requests still go through impact analysis and the agreed change control process.

**Reading before the next session:**
- BABOK 5.4 (pp.91–94)
- Lessing pp.167–171
- Jonasson 6.3.4 (p.138)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 5.4 elements? :: Assessment Formality; Impact Analysis; Impact Resolution
- Impact analysis considers? :: Benefit, cost, impact, schedule, urgency
- 5.4 outputs? :: Requirements Change Assessment; Designs Change Assessment

ACTION: Update [progress.json](progress/progress.json): add this lesson (`4.4`) to `completed` with today's date and minutes ≈ 85, set `current` to `4.5`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 4.5: 5.5 Approve Requirements. Consensus, conflict and sign-off, without a Harvest-style rubber stamp.

STOP: Ready for 4.5? Type `/next` (or `/start 4.5`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/33-cr-017-change-assessment.md created and sponsor-reviewed
- [ ] Student used the impact factors
- [ ] Drill logged; task card added
