# Lesson 2.5: 3.5 Identify Business Analysis Performance Improvements

*Module 2 · Week 3 · ~70 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Identify Business Analysis Performance Improvements](CBAP%20Knowledge%20Graph/03%20Tasks/Identify%20Business%20Analysis%20Performance%20Improvements.md)
- [Business Analysis Performance Assessment](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Business%20Analysis%20Performance%20Assessment.md)
- [Performance Objectives (external)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Performance%20Objectives%20%28external%29.md)
- [17-ba-team-retro-notes](case-files/17-ba-team-retro-notes.md)
- [Lessons Learned](CBAP%20Knowledge%20Graph/05%20Techniques/Lessons%20Learned.md)
- [Metrics and Key Performance Indicators (KPIs)](CBAP%20Knowledge%20Graph/05%20Techniques/Metrics%20and%20Key%20Performance%20Indicators%20%28KPIs%29.md)

---

Week 6 of the initiative: your BA team's retro data is in. 34% of requirements needed rework, approvals take 11 days, and stores rate BA engagement at 3.1/5. Time for **3.5 Identify BA Performance Improvements**. Note the target: the *BA work*, not the solution.

By the end of this session you will be able to:
- Explain the 4 elements of 3.5
- Define BA performance measures
- Recommend preventive, corrective and improvement actions

STOP: Ready to dive in?

USER: Ready

---

## Part 1: The task

ACTION: Re-read [Identify Business Analysis Performance Improvements](CBAP%20Knowledge%20Graph/03%20Tasks/Identify%20Business%20Analysis%20Performance%20Improvements.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Evaluate how well the business analysis work itself is going, and put improvements in place.
- Elements: Performance Analysis, Assessment Measures (accuracy and completeness, knowledge, effectiveness, organizational support, significance, strategic, timeliness), Analyze Results, Recommend Actions for Improvement (preventive, corrective, improvement).
- Inputs: BA Approach, Performance Objectives (external). Output: BA Performance Assessment, which feeds back as a guideline into 3.1–3.4 and 4.5.
- Techniques: lessons learned (retrospective), metrics and KPIs, root cause analysis, reviews, surveys, interviews.

STOP: Is "34% of requirements needed rework" a solution performance measure or a BA performance measure?

USER: BA performance measure

ACTION: Give feedback. A strong answer includes: BA performance (accuracy and completeness of BA deliverables). Solution performance measures belong to 8.1.

**Exam trap to call out:** BA Performance Assessment (3.5) vs Solution Performance Analysis (8.2).

---

## Apply it at GreenBasket: BA Performance Assessment from the retro

Grace wants an honest assessment and an improvement plan.

ACTION: Open and skim [17-ba-team-retro-notes](case-files/17-ba-team-retro-notes.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Analyze the retro data: which measures are off target, what are the likely root causes, and what actions would you recommend? Label each action as preventive, corrective or improvement.

USER: Drafts their analysis in the chat

ACTION: Coach it and save a BA Performance Assessment: measures table (plan, actual, variance), root causes (e.g. Friday scheduling, no peer review, unclear approval rights), and actions labelled preventive, corrective or improvement, plus which BAPM output each action updates. Save the result to `workspace/14-ba-performance-assessment.md` and link it: [14-ba-performance-assessment.md](workspace/14-ba-performance-assessment.md).

A model answer should cover (use it to coach, don't just paste it):
- Rework 34% → root cause: compound or vague requirements, no checklist → preventive: peer review with a quality checklist (link to 7.2)
- Approval 11 days → unclear decision rights → corrective: update the Governance Approach (3.3)
- Store satisfaction 3.1 → sessions on Fridays → corrective: reschedule; update the Stakeholder Engagement Approach (3.2)
- Marketing felt shut down → improvement: a structured ideas backlog for Lily

**Discovery:** The assessment loops back: it becomes a guideline for 3.1–3.4 and for 4.5. BAPM is a cycle, not a one-off.

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 3.5 elements, BA performance measures vs solution measures, preventive/corrective/improvement actions, the feedback loop.
Build distractors from these traps: BA performance vs solution performance; Performance Objectives (external) produced internally; lessons learned only at project end.
Log to scores.csv with ka=`BAPM` and topic=`3.5`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 3.5 improves BA work itself.
2. Actions are preventive, corrective or improvement.
3. Its output feeds back into the other BAPM tasks and into 4.5.

> **Exam rule of thumb:** "How well is the BA work going?" → 3.5. "How well is the solution performing?" → Solution Evaluation.

**Reading before the next session:**
- BABOK 3.5 (pp.47–52)
- Lessing pp.97–109 (incl. knowledge quiz)
- Jonasson 4.3.5 (p.57)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 3.5 elements? :: Performance Analysis; Assessment Measures; Analyze Results; Recommend Actions for Improvement
- Types of improvement actions (3.5)? :: Preventive, corrective, improvement
- 3.5 output? :: Business Analysis Performance Assessment

ACTION: Update [progress.json](progress/progress.json): add this lesson (`2.5`) to `completed` with today's date and minutes ≈ 70, set `current` to `2.6`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 2.6: BAPM techniques lab: estimation, item tracking, lessons learned, reviews. Hands-on with the techniques BAPM relies on.

STOP: Ready for 2.6? Type `/next` (or `/start 2.6`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/14-ba-performance-assessment.md created
- [ ] Actions labelled by type
- [ ] Drill logged; task card added
