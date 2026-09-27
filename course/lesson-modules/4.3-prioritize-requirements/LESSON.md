# Lesson 4.3: 5.3 Prioritize Requirements

*Module 4 · Week 5 · ~85 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Prioritize Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Prioritize%20Requirements.md)
- [Prioritization](CBAP%20Knowledge%20Graph/05%20Techniques/Prioritization.md)
- [Decision Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Decision%20Analysis.md)
- [Backlog Management](CBAP%20Knowledge%20Graph/05%20Techniques/Backlog%20Management.md)
- [Requirements (prioritized)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20%28prioritized%29.md)
- [Governance Approach](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Governance%20Approach.md)

---

Tom's list has 13 "High" priorities, many from one person. Workshop #1's dot vote said accuracy beats recipes 14 to 1. Today you prioritize properly: **5.3 Prioritize Requirements**.

By the end of this session you will be able to:
- Know the 8 bases for prioritization
- Handle the challenges (non-negotiable demands, unrealistic trade-offs)
- Apply MoSCoW, ranking and time-boxing

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Prioritize Requirements

ACTION: Re-read [Prioritize Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Prioritize%20Requirements.md), [Prioritization](CBAP%20Knowledge%20Graph/05%20Techniques/Prioritization.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Rank requirements and designs by relative importance, with stakeholders, and keep doing so as things change.
- Elements: Basis for Prioritization, Challenges of Prioritization, Continual Prioritization.
- Basis: **benefit, penalty, cost, risk, dependencies, time sensitivity, stability, regulatory or policy compliance**.
- Challenges: stakeholders may deem everything high priority, try to avoid difficult trade-offs, or the solution team may influence results by exaggerating effort.
- Prioritization is continual. The basis can change as context changes.
- Technique families: grouping (MoSCoW, high/med/low), ranking, time boxing/budgeting, negotiation.
- Inputs: Requirements, Designs. Guidelines include Governance Approach, Change Strategy, Solution Scope, Requirements Architecture, Business Constraints, Domain Knowledge. Outputs: Requirements (prioritized), Designs (prioritized).

STOP: R-19 (hosted payment page) is not exciting for customers, but it is mandatory. Which basis makes it top priority?

USER: Regulatory or policy compliance (and penalty)

ACTION: Give feedback. A strong answer includes: regulatory or policy compliance, with penalty as a secondary basis (the consequence of not doing it).

**Exam trap to call out:** Penalty (the consequence of NOT implementing) is a distinct basis from benefit.

---

## Apply it at GreenBasket: Prioritize release 1 (6 pilot stores)

Run the prioritization you would facilitate with Elena, Marcus, Anil, Janet and Lily.

ACTION: Open and skim [11-draft-requirements-v0](case-files/11-draft-requirements-v0.md), [10-workshop-notes-raw](case-files/10-workshop-notes-raw.md), [04-customer-feedback-q2](case-files/04-customer-feedback-q2.md), [12-governance-approach](workspace/12-governance-approach.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Apply MoSCoW to R-01..R-20 for release 1. For each Must and each Won't, name the basis (benefit, penalty, cost, risk, dependencies, time sensitivity, stability, compliance). How will you handle Lily's "everything is High" and the one-lap rule?

USER: Drafts their analysis in the chat

ACTION: Coach and save the prioritized list with the rationale. Must: payment page (compliance), substitution preferences (benefit, accuracy), pick path sorted (benefit), temperature control (compliance), loyalty points (benefit, time). Won't this time: recipes (no objective), same-day delivery. Coupons are Could or Should depending on cost and the dependency on the loyalty API. Record the dependency R-12 → product master data. Save the result to `workspace/32-prioritized-requirements-r1.md` and link it: [32-prioritized-requirements-r1.md](workspace/32-prioritized-requirements-r1.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `elena-sponsor`, giving it the path `workspace/32-prioritized-requirements-r1.md` and ask whether she accepts what is Won't for release 1. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 5.3 bases, challenges, continual prioritization, prioritization techniques (MoSCoW, ranking, time boxing, negotiation), decision analysis support.
Build distractors from these traps: priority set once; benefit vs penalty; BA decides priority alone; prioritization approach (3.3) vs prioritizing (5.3).
Log to scores.csv with ka=`RLCM` and topic=`5.3`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 8 bases: benefit, penalty, cost, risk, dependencies, time sensitivity, stability, compliance.
2. Stakeholders decide priorities; the BA facilitates.
3. Continual: re-prioritize as the context changes.

> **Exam rule of thumb:** The BA *facilitates* prioritization with stakeholders. An answer where the BA sets priorities alone is wrong.

**Reading before the next session:**
- BABOK 5.3 (pp.86–90) and 10.33
- Jonasson 5.18 (pp.122–126): dollar, forced-pair, density dotting, AHP

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Bases for prioritization? :: Benefit, penalty, cost, risk, dependencies, time sensitivity, stability, regulatory/policy compliance
- Prioritization technique families? :: Grouping (e.g. MoSCoW), ranking, time boxing/budgeting, negotiation

ACTION: Update [progress.json](progress/progress.json): add this lesson (`4.3`) to `completed` with today's date and minutes ≈ 85, set `current` to `4.4`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 4.4: 5.4 Assess Requirements Changes: CR-017 same-day delivery. Marketing wants delivery in release 1, with media already booked.

STOP: Ready for 4.4? Type `/next` (or `/start 4.4`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/32-prioritized-requirements-r1.md created and sponsor-reviewed
- [ ] Student named bases for key items
- [ ] Drill logged; task card added
