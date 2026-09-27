# Lesson 6.5: 7.3 Validate Requirements

*Module 6 · Week 7 · ~75 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Validate Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Validate%20Requirements.md)
- [Requirements (validated)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20%28validated%29.md)
- [Business Objectives](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Business%20Objectives.md)
- [Potential Value](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Potential%20Value.md)

---

Your requirements are now well-formed. But does "recipes and meal plans" help reach 5% online share or 97% accuracy? **7.3 Validate Requirements** checks alignment with business value.

By the end of this session you will be able to:
- Know the 3 elements of 7.3
- Define measurable evaluation criteria
- Evaluate alignment with the solution scope

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Validate Requirements

ACTION: Re-read [Validate Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Validate%20Requirements.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Check that requirements and designs support the business requirements and will deliver the value that is needed.
- Elements: Identify Assumptions, Define Measurable Evaluation Criteria, Evaluate Alignment with Solution Scope.
- Input: Requirements (specified and modelled). Guidelines: Business Objectives, Future State Description, Potential Value, Solution Scope. Output: Requirements (validated).
- A requirement that is valid but outside the solution scope → change the scope or remove the requirement.
- Validation is ongoing and involves the customer, end users and sponsor.

STOP: R-11 (recipes) is well-written but supports no business objective. Verify issue or validate issue, and what happens to it?

USER: Validation issue; out of scope, removed or deferred

ACTION: Give feedback. A strong answer includes: validation: it doesn't align with the objectives or the solution scope. Remove it or move it to a future backlog (a scope change would need governance).

---

## Apply it at GreenBasket: Validation matrix

Validate the verified requirements against objectives and scope.

ACTION: Open and skim [53-verification-log](workspace/53-verification-log.md), [41-future-state-description](workspace/41-future-state-description.md), [43-change-strategy-and-solution-scope](workspace/43-change-strategy-and-solution-scope.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: For each verified requirement: which business objective it supports, the assumption it relies on, a measurable evaluation criterion, and in-scope yes/no. Which ones fail validation?

USER: Drafts their analysis in the chat

ACTION: Coach and save the validation matrix. Flag failing requirements (recipes, React Native, same-day delivery) and assumptions (e.g. coupons via API is FALSE, so R-10 needs a design option or deferral). Save the result to `workspace/54-validation-matrix.md` and link it: [54-validation-matrix.md](workspace/54-validation-matrix.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `cbap-examiner`, giving it the path `workspace/54-validation-matrix.md` and check that validation (not verification) logic is used. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 7.3 elements, validation vs verification, evaluation criteria, alignment with solution scope, guidelines used.
Build distractors from these traps: validate = check quality; validated requirements go to Approve; validation only at the end.
Log to scores.csv with ka=`RADD` and topic=`7.3`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Validate = aligns with business requirements and delivers value.
2. Elements: assumptions, measurable evaluation criteria, alignment with solution scope.
3. Output: Requirements (validated) → Define Design Options.

**Reading before the next session:**
- BABOK 7.3 (pp.144–147)
- Lessing pp.246–250
- Jonasson 9.5.1 Validation vs Verification (p.224)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 7.3 elements? :: Identify Assumptions; Define Measurable Evaluation Criteria; Evaluate Alignment with Solution Scope
- Validated requirements feed… :: 7.5 Define Design Options (with prioritization)

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.5`) to `completed` with today's date and minutes ≈ 75, set `current` to `6.6`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.6: RADD mid-point drill (40 questions). Half of RADD done. Check it sticks.

STOP: Ready for 6.6? Type `/next` (or `/start 6.6`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/54-validation-matrix.md created and examiner-reviewed
- [ ] Drill logged; task card added
