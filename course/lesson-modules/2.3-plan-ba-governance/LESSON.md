# Lesson 2.3: 3.3 Plan Business Analysis Governance

*Module 2 · Week 3 · ~70 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Plan Business Analysis Governance](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Governance.md)
- [Governance Approach](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Governance%20Approach.md)
- [02-harvest-postmortem](case-files/02-harvest-postmortem.md)

---

Harvest had 63 change requests "agreed in corridors" and no owner for approvals. Today you design the rules of the game: **3.3 Plan Business Analysis Governance**.

By the end of this session you will be able to:
- Explain the 4 elements of governance planning
- Design a change control process for BA information
- Define decision rights, the prioritization approach and approvals

STOP: Ready to dive in?

USER: Ready

---

## Part 1: The task

ACTION: Re-read [Plan Business Analysis Governance](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Governance.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Set the rules for decisions about requirements and designs: who decides, how changes are controlled, how priorities are set, and how approvals happen.
- Elements: Decision Making (who decides, escalation path), Change Control Process (how changes are requested, what a change request contains, how changes are prioritized, documented and communicated, who does impact analysis, who authorizes), Plan Prioritization Approach (formality, basis and who participates), Plan for Approvals (what is approved, when, by whom, format).
- Change request contents: cost and time estimates, benefits, risks, priority, course(s) of action.
- Inputs: BA Approach, Stakeholder Engagement Approach. Output: Governance Approach, a guideline for 5.3, 5.4 and 5.5.

STOP: Which later tasks use the Governance Approach as a guideline?

USER: Prioritize, Assess Requirements Changes, Approve Requirements

ACTION: Give feedback. A strong answer includes: 5.3 Prioritize Requirements, 5.4 Assess Requirements Changes, 5.5 Approve Requirements.

**Exam trap to call out:** BA governance covers decisions about *BA information* (requirements and designs), not the whole project governance.

---

## Apply it at GreenBasket: Governance Approach for Click & Collect

Design governance that stakeholders will actually follow.

ACTION: Open and skim [02-harvest-postmortem](case-files/02-harvest-postmortem.md), [17-ba-team-retro-notes](case-files/17-ba-team-retro-notes.md), [08-compliance-memo](case-files/08-compliance-memo.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Draft the 4 elements: decision makers and escalation (who decides store-process, customer-experience, compliance and technology requirements?), a change control process (steps plus change request fields), the prioritization approach, and a plan for approvals (what, who, format; predictive vs adaptive parts).

USER: Drafts their analysis in the chat

ACTION: Coach it: resolve the retro's "Marcus or store managers?" ambiguity, make Janet the approver for the six compliance areas, set a change control board cadence, and require impact analysis before decisions. Save it with a Mermaid flowchart of the change control process. Save the result to `workspace/12-governance-approach.md` and link it: [12-governance-approach.md](workspace/12-governance-approach.md).

A model answer should cover (use it to coach, don't just paste it):
- Decision rights by requirement domain; escalation to Elena as sponsor
- CR fields: description, requester, benefit, cost/time estimate, risk of doing and not doing, priority, affected requirements, recommendation
- Change control board weekly: Elena (chair), Tom, Marcus, Anil, BA; Janet for compliance CRs
- Prioritization: agreed basis (value, cost, risk, regulatory), workshop-based, with the sponsor as tie-breaker
- Approvals: formal sign-off for compliance and vendor contract; sprint-review acceptance for backlog items

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `cbap-examiner`, giving it the path `workspace/12-governance-approach.md` and check that all four governance elements are covered with BABOK terms. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 3.3 Plan Business Analysis Governance: decision making, change control process contents, prioritization approach, plan for approvals.
Build distractors from these traps: governance approach vs information management approach; BA implements changes without authorization; prioritization performed here (it is only *planned* here, performed in 5.3); approvals only in predictive approaches.
Log to scores.csv with ka=`BAPM` and topic=`3.3`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 4 elements: decision making, change control process, prioritization approach, plan for approvals.
2. 3.3 *plans* prioritization and approvals; 5.3 and 5.5 *do* them.
3. Governance Approach guides Prioritize, Assess Changes and Approve.

> **Exam rule of thumb:** Spot "plan" vs "perform": BAPM plans the approach, and the other KAs execute it.

**Reading before the next session:**
- BABOK 3.3 (pp.37–41)
- Lessing pp.88–92
- Jonasson 4.3.3 (p.56) and 4.4.7 Manage Changes to Requirements (p.63)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 3.3 elements? :: Decision Making; Change Control Process; Plan Prioritization Approach; Plan for Approvals
- Governance Approach is a guideline for… :: 5.3 Prioritize, 5.4 Assess Changes, 5.5 Approve

ACTION: Update [progress.json](progress/progress.json): add this lesson (`2.3`) to `completed` with today's date and minutes ≈ 70, set `current` to `2.4`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 2.4: 3.4 Plan Business Analysis Information Management. Organization, abstraction, traceability approach, reuse, storage and attributes.

STOP: Ready for 2.4? Type `/next` (or `/start 2.4`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student covered all 4 elements
- [ ] workspace/12-governance-approach.md created and examiner-reviewed
- [ ] Drill logged; task card added
