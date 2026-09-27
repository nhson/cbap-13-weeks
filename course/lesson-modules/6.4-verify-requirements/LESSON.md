# Lesson 6.4: 7.2 Verify Requirements

*Module 6 · Week 7 · ~80 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Verify Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Verify%20Requirements.md)
- [Requirements (verified)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20%28verified%29.md)
- [Reviews](CBAP%20Knowledge%20Graph/05%20Techniques/Reviews.md)
- [Commonly Confused Concepts](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Commonly%20Confused%20Concepts.md)
- [11-draft-requirements-v0](case-files/11-draft-requirements-v0.md)

---

Priyanka says half of Tom's requirements are untestable. She's being generous. Today: **7.2 Verify Requirements**, the quality check before approval.

By the end of this session you will be able to:
- Name the 9 characteristics of requirements quality
- Run verification activities with checklists
- Rewrite flawed requirements

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Verify Requirements

ACTION: Re-read [Verify Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Verify%20Requirements.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Check that requirement and design specifications are of good quality and fit for their purpose.
- Elements: Characteristics of Requirements and Designs Quality, Verification Activities, Checklists.
- Quality characteristics: **atomic, complete, consistent, concise, feasible, unambiguous, testable, prioritized, understandable**.
- Verification activities: check compliance with standards, correct use of modelling notation, completeness within each model, consistency across models, terminology is understood.
- Input: Requirements (specified and modelled). Output: Requirements (verified). Techniques: acceptance and evaluation criteria, item tracking, metrics and KPIs, reviews.

STOP: R-06 packs 4 requirements into one sentence. Which characteristic does it violate?

USER: Atomic

ACTION: Give feedback. A strong answer includes: atomic (and arguably testable and unambiguous for "fast"). Split it into 4.

**Exam trap to call out:** Verify ≠ validate. "Does it align with business objectives?" is validation (7.3).

---

## Apply it at GreenBasket: Verify and rewrite the draft requirements

Run a verification review on R-01..R-20.

ACTION: Open and skim [11-draft-requirements-v0](case-files/11-draft-requirements-v0.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: For at least 10 requirements: name the violated characteristic(s) and rewrite them. Start with R-01, R-02, R-04, R-06, R-07, R-08, R-13/R-14 (conflict!), R-18, R-20.

USER: Drafts their analysis in the chat

ACTION: Coach and save a verification log (ID, issue, characteristic, rewrite), plus a reusable checklist. Examples: R-01 "fast and user-friendly" → unambiguous/testable; R-02 real-time stock → feasible; R-13 vs R-14 → consistent; R-18 availability → needs context (hours, measurement window). Save the result to `workspace/53-verification-log.md` and link it: [53-verification-log.md](workspace/53-verification-log.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `priyanka-qa`, giving it the path `workspace/53-verification-log.md` and review the rewrites. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 7.2 quality characteristics, verification activities, checklists, verify vs validate, input and output states.
Build distractors from these traps: verify vs validate; verified vs validated as Approve input; complete vs consistent; feasible vs testable.
Log to scores.csv with ka=`RADD` and topic=`7.2`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 9 characteristics: atomic, complete, consistent, concise, feasible, unambiguous, testable, prioritized, understandable.
2. Verify = quality of the specification; output Requirements (verified) → 5.5.

> **Exam rule of thumb:** Verify = "built right" (quality). Validate = "right thing" (value and alignment).

**Reading before the next session:**
- BABOK 7.2 (pp.141–143), 10.37 Reviews
- Lessing pp.242–246

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Requirements quality characteristics (7.2)? :: Atomic, complete, consistent, concise, feasible, unambiguous, testable, prioritized, understandable
- 7.2 elements? :: Characteristics of Quality; Verification Activities; Checklists

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.4`) to `completed` with today's date and minutes ≈ 80, set `current` to `6.5`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.5: 7.3 Validate Requirements. Do these requirements actually deliver the business objectives?

STOP: Ready for 6.5? Type `/next` (or `/start 6.5`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/53-verification-log.md created and QA-reviewed
- [ ] Student names all 9 characteristics
- [ ] Drill logged; task card added
