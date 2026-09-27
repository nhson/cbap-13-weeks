# Lesson 2.6: BAPM techniques lab: estimation, item tracking, lessons learned, reviews

*Module 2 · Week 3 · ~75 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Estimation](CBAP%20Knowledge%20Graph/05%20Techniques/Estimation.md)
- [Item Tracking](CBAP%20Knowledge%20Graph/05%20Techniques/Item%20Tracking.md)
- [Lessons Learned](CBAP%20Knowledge%20Graph/05%20Techniques/Lessons%20Learned.md)
- [Reviews](CBAP%20Knowledge%20Graph/05%20Techniques/Reviews.md)
- [Functional Decomposition](CBAP%20Knowledge%20Graph/05%20Techniques/Functional%20Decomposition.md)
- [Risk Analysis and Management](CBAP%20Knowledge%20Graph/05%20Techniques/Risk%20Analysis%20and%20Management.md)

---

Techniques make up about a third of the exam content. Today's lab covers the ones BAPM leans on. You'll *use* them on GreenBasket, not just memorize them.

By the end of this session you will be able to:
- Apply estimation methods (incl. PERT)
- Set up item tracking
- Run a lessons-learned review
- Know the review types

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Estimation

ACTION: Re-read [Estimation](CBAP%20Knowledge%20Graph/05%20Techniques/Estimation.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Methods: top-down, bottom-up, parametric, rolling wave, Delphi, PERT (three-point: (O + 4M + P) / 6), analogous, historical analysis, expert judgment.
- Estimates are ranges with confidence levels and should be revised as information improves (rolling wave).
- BA uses: estimating BA effort (3.1), elicitation (4.1), prioritization cost (5.3), change impact (5.4), solution options (6.4, 7.6).

STOP: Estimate BA effort for store observation sessions: optimistic 6 days, most likely 9, pessimistic 18. What is the PERT estimate?

USER: 10 days

ACTION: Give feedback. A strong answer includes: (6 + 36 + 18) / 6 = 10 days.

---

## Part 2: Item tracking, lessons learned, reviews

ACTION: Re-read [Item Tracking](CBAP%20Knowledge%20Graph/05%20Techniques/Item%20Tracking.md), [Lessons Learned](CBAP%20Knowledge%20Graph/05%20Techniques/Lessons%20Learned.md), [Reviews](CBAP%20Knowledge%20Graph/05%20Techniques/Reviews.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Item tracking: capture and assign responsibility for issues, actions, assumptions, constraints, dependencies, defects, enhancements, until resolved. Attributes include ID, description, type, date identified, owner, priority, impact, resolution date, status.
- Lessons learned: compile successes, failures and recommendations. Can happen at any point (retrospectives), not only at the end.
- Review types: inspection (most formal, checklist), formal walkthrough, single-issue review, informal walkthrough, desk check, pass-around, ad hoc. Roles: author, reviewer, facilitator, scribe.

STOP: The workshop notes had "action items: nobody assigned owners". Which technique fixes that?

USER: Item tracking

ACTION: Give feedback. A strong answer includes: item tracking: every item gets an owner, status and resolution date.

---

## Apply it at GreenBasket: Issue and action log from the inherited mess

Workshop #1 and the Harvest post-mortem left many open issues with no owners.

ACTION: Open and skim [10-workshop-notes-raw](case-files/10-workshop-notes-raw.md), [02-harvest-postmortem](case-files/02-harvest-postmortem.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Create an item-tracking log of at least 8 items (issues, decisions needed, assumptions, dependencies) with type, owner (by role), priority, impact and target date. Then list 3 Harvest lessons in "keep / stop / start" form.

USER: Drafts their analysis in the chat

ACTION: Coach it (e.g. alcohol decision → owner Janet/Elena; substitution policy → owner Marcus plus the customer voice; aisle data dependency → Ben/Owen). Save both. Save the result to `workspace/15-item-log-and-lessons.md` and link it: [15-item-log-and-lessons.md](workspace/15-item-log-and-lessons.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: estimation methods and PERT, item tracking, lessons learned, review types, plus which BAPM tasks use these techniques.
Build distractors from these traps: inspection vs walkthrough formality; lessons learned only at close; Delphi vs PERT; item tracking vs backlog management.
Log to scores.csv with ka=`TECH` and topic=`bapm-techniques`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. PERT = (O + 4M + P) / 6. Estimates are ranges, refined over time.
2. Item tracking assigns owners to issues until they are resolved.
3. Reviews range from inspection (formal) to ad hoc.

**Reading before the next session:**
- BABOK 10.19, 10.26, 10.27, 10.37
- Jonasson 4.5.2 Estimating (p.68)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- PERT formula? :: (Optimistic + 4×Most likely + Pessimistic) / 6
- Most formal review type? :: Inspection
- Item tracking tracks… :: issues, actions, assumptions, constraints, dependencies, defects, enhancements

ACTION: Update [progress.json](progress/progress.json): add this lesson (`2.6`) to `completed` with today's date and minutes ≈ 75, set `current` to `2.7`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 2.7: BAPM exam drill (40 questions). Prove BAPM mastery.

STOP: Ready for 2.7? Type `/next` (or `/start 2.7`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student computed a PERT estimate
- [ ] workspace/15-item-log-and-lessons.md created
- [ ] Drill logged
