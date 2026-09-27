# Lesson 1.7: Diagnostic review & your personal focus plan

*Module 1 · Week 2 · ~75 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [error-log](progress/error-log.md)
- [scores](progress/scores.csv)
- [Commonly Confused Concepts](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Commonly%20Confused%20Concepts.md)
- Also read `exams/diagnostic-report.md` if it exists.

---

Your diagnostic misses are the most valuable data you have. Today we sort them into **knowledge gaps**, **confusions** and **misreads**, because each needs a different fix.

By the end of this session you will be able to:
- Classify errors by root cause
- Learn the 14 most commonly confused BABOK pairs
- Adjust the study plan to your weak spots

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Three kinds of wrong

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Knowledge gap: you didn't know the fact (e.g. which task outputs Solution Scope). Fix: study plus flashcards.
- Confusion: you mixed up two similar concepts (verify/validate, solution/enterprise limitation). Fix: contrast tables.
- Misread or over-thinking: you knew it but answered from "real life" or missed a word like FIRST, BEST, NOT. Fix: exam technique.
- BABOK answers beat real-life answers. The exam asks what the BABOK says a BA should do.

STOP: Look at your error log: which of the three types dominates for you?

USER: Names a type

---

## Part 2: The confusion hit-list

ACTION: Re-read [Commonly Confused Concepts](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Commonly%20Confused%20Concepts.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Walk through the pairs most relevant to the student's misses (verify vs validate, confirm vs verify, solution vs enterprise limitation, change strategy vs solution scope, business requirements vs business objectives, focus groups vs workshops…).
- For each pair: a one-line distinction and a GreenBasket example.

STOP: Quick-fire: I describe a situation and you name which side of the pair it is. Ready?

USER: Ready

ACTION: Give feedback. A strong answer includes: run 5 rapid quick-fire items drawn from the student's confused pairs, answered in chat.

---

## Apply it at GreenBasket: Your personal focus plan

Combine the diagnostic data with the 13-week plan.

ACTION: Open and skim [error-log](progress/error-log.md), [CBAP-Roadmap](../CBAP-Roadmap.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Tell me: your 2 weakest KAs, your top 3 confusions, and how many extra minutes per week you could give those areas.

USER: Drafts their analysis in the chat

ACTION: Write a focus plan: baseline table, target by week 9 (≥75% per KA) and week 12 (≥80% on a mock), the extra drills to add (e.g. `/drill RADD 10` every Sunday), and which lessons deserve extra time. Update `weak_topics` in progress.json. Save the result to `workspace/04-personal-focus-plan.md` and link it: [04-personal-focus-plan.md](workspace/04-personal-focus-plan.md).

---

## Exam drill

QUIZ: 8 CBAP-style questions on: re-test of the student's diagnostic misses with fresh questions on the same concepts.
Log to scores.csv with ka=`ALL` and topic=`diagnostic-retest`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Diagnose *why* you missed, not just *what*.
2. Contrast pairs kill confusion errors.
3. BABOK logic beats real-life habit in exam answers.

> **Exam rule of thumb:** Underline FIRST / BEST / MOST / NOT / EXCEPT in every question stem.

**Reading before the next session:**
- Lessing ch.4 What to Expect From the Exam (pp.41–45)
- Review the Commonly Confused Concepts note once more

ACTION: Update [progress.json](progress/progress.json): add this lesson (`1.7`) to `completed` with today's date and minutes ≈ 75, set `current` to `1.8`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 1.8: The big map: how the 30 tasks hand off to each other. The input/output backbone that answers "what comes next?" questions.

STOP: Ready for 1.8? Type `/next` (or `/start 1.8`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Errors classified by type
- [ ] workspace/04-personal-focus-plan.md created
- [ ] weak_topics updated
- [ ] Re-test drill logged
