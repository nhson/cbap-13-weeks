# Lesson 4.5: 5.5 Approve Requirements

*Module 4 · Week 5 · ~70 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Approve Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Approve%20Requirements.md)
- [Requirements (approved)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20%28approved%29.md)
- [Requirements (verified)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20%28verified%29.md)
- [Acceptance and Evaluation Criteria](CBAP%20Knowledge%20Graph/05%20Techniques/Acceptance%20and%20Evaluation%20Criteria.md)

---

In Harvest, requirements were "signed off" by a delegate while stores never saw them. Now Marcus and Lily disagree on substitutions, and Janet must approve compliance items. **5.5 Approve Requirements**.

By the end of this session you will be able to:
- Know the 4 elements of 5.5
- Handle conflict and gain consensus
- Know that approval takes Requirements (verified)

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Approve Requirements

ACTION: Re-read [Approve Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Approve%20Requirements.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Reach agreement and approval on requirements and designs so that work can continue.
- Elements: Understand Stakeholder Roles (who has authority), Conflict and Issue Management, Gain Consensus, Track and Communicate Approval.
- Inputs: **Requirements (verified)**, Designs. Guidelines: Change Strategy, Governance Approach, Legal/Regulatory Information, Requirements Management Tools/Repository, Solution Scope. Outputs: Requirements (approved), Designs (approved).
- Approval can be formal sign-off (predictive) or ongoing acceptance, e.g. in backlog reviews (adaptive).
- Techniques: acceptance and evaluation criteria, decision analysis, item tracking, reviews, workshops.

STOP: Marcus (store ops) and Lily (marketing) disagree about per-item substitutions. What does the BA do under "Conflict and Issue Management"?

USER: Facilitate resolution, use data or decision analysis, escalate per governance if needed

ACTION: Give feedback. A strong answer includes: facilitate communication, use evidence (survey: accuracy 82% top factor; the oat milk complaint) and decision analysis, track the issue, and escalate to the decision maker defined in governance if unresolved.

---

## Apply it at GreenBasket: Approval plan for release 1 requirements

Make approval real this time.

ACTION: Open and skim [12-governance-approach](workspace/12-governance-approach.md), [32-prioritized-requirements-r1](workspace/32-prioritized-requirements-r1.md), [11-stakeholder-engagement-approach](workspace/11-stakeholder-engagement-approach.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Create an approval plan: requirement groups → approver (authority) → reviewers → approval method (formal sign-off vs backlog acceptance) → evidence of verification. Then write how you'll resolve the substitution conflict and how approvals will be tracked and communicated.

USER: Drafts their analysis in the chat

ACTION: Coach and save. Ensure: Janet approves compliance items; Marcus approves store process items (with Rosa and Kim reviewing); Elena approves scope; approvals are recorded in the repository with date and version; the conflict is resolved with a decision-analysis table and evidence. Save the result to `workspace/34-approval-plan-r1.md` and link it: [34-approval-plan-r1.md](workspace/34-approval-plan-r1.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 5.5 elements, approval inputs (verified), consensus and conflict handling, formal vs adaptive approval, tracking approvals.
Build distractors from these traps: validated as approval input; approval only by sponsor; conflict escalated before facilitation; approval = sign-off only (no adaptive form).
Log to scores.csv with ka=`RLCM` and topic=`5.5`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Approve takes **verified** requirements.
2. Know who has authority, manage conflict, gain consensus, track and communicate.
3. Approval can be formal or continuous (adaptive).

> **Exam rule of thumb:** Conflict at approval → the BA facilitates resolution with evidence first, and escalates per governance only if needed.

**Reading before the next session:**
- BABOK 5.5 (pp.95–98)
- Lessing pp.171–184 (incl. knowledge quiz)
- Jonasson 6.3.5 (p.138)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 5.5 elements? :: Understand Stakeholder Roles; Conflict & Issue Management; Gain Consensus; Track & Communicate Approval
- 5.5 input requirement state? :: Requirements (verified)

ACTION: Update [progress.json](progress/progress.json): add this lesson (`4.5`) to `completed` with today's date and minutes ≈ 70, set `current` to `4.6`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 4.6: RLCM techniques lab: decision analysis, backlog management, business rules. Decision matrices, backlogs and business rules in practice.

STOP: Ready for 4.6? Type `/next` (or `/start 4.6`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/34-approval-plan-r1.md created
- [ ] Student states that approval takes verified requirements
- [ ] Drill logged; task card added
