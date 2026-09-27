# Lesson 1.6: Diagnostic exam (50 questions)

*Module 1 · Week 2 · ~100 min in session + ~0 min reading*

## Prepare (instructor: read silently before teaching)
- [Exam Blueprint](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Exam%20Blueprint.md)
- [Commonly Confused Concepts](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Commonly%20Confused%20Concepts.md)
- [BABOK Input-Output Flow](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/BABOK%20Input-Output%20Flow.md)

---

Today is about data, not ego. A 50-question diagnostic across all KAs shows where you start. Most people score 45–60% before studying, and that's normal.

Treat it like the real thing: timed (75 minutes), no notes, and honest guesses marked with a "?".

By the end of this session you will be able to:
- Establish a baseline score by KA
- Practise exam pacing (about 1.5 min per question)
- Start the error log with real data

STOP: Do you have 75 uninterrupted minutes now? If not, we can generate the exam and you take it later.

USER: Ready

---

## Generate the exam

ACTION: Read the knowledge-graph notes you need (KA notes, the Commonly Confused Concepts note, and the I/O Flow note), then write **50 original CBAP-style questions** to `exams/diagnostic.md`:
- Distribution by blueprint: RADD 15, RLCM 8, SA 7, BAPM 7, SE 7, E&C 6.
- Mix: about 60% scenario-based (including one mini case study with 4 linked questions), 20% "which input/output/technique", 20% definitions and concepts.
- Each question: number, KA tag hidden (don't show the KA to the student), 4 options A–D, exactly one best answer.
- Write the key to `exams/.keys/diagnostic-key.md`: number | answer | KA | task/technique | type | 2-line rationale | knowledge-graph note path.
- Create `exams/diagnostic-answers.md` with lines `1: ` … `50: ` for the student to fill in (letter, plus `?` if guessing).

Tell the student the exam is ready and link [diagnostic.md](exams/diagnostic.md) and [diagnostic-answers.md](exams/diagnostic-answers.md). **Don't open the key file or reveal answers.**

STOP: Start your 75-minute timer. Answer in diagnostic-answers.md, add `?` to guesses, and tell me when you're done.

USER: Done

ACTION: Run the same procedure as the `/grade diagnostic` command: score it, write `exams/diagnostic-report.md`, and append misses to the error log and per-KA rows to scores.csv.

---

## Debrief

Share the headline: total %, by-KA table, and time used. Normalize the result: a baseline is a starting point, not a verdict.

STOP: Looking at your by-KA scores, which result surprised you most?

USER: Responds

ACTION: Point out the two weakest KAs and the most common confusion pattern. Note them in progress.json `weak_topics`. Tell them lesson 1.7 will turn this into a personal focus plan.

---

## Wrap-up

**Key takeaways:**
1. You now have a baseline by KA.
2. Guesses count as misses in the error log. That's where learning happens.
3. Pacing target: about 1:45 per question on the real exam.

> **Exam rule of thumb:** On test day, flag and move on after 2 minutes. Never burn 5 minutes on one question.

ACTION: Update [progress.json](progress/progress.json): add this lesson (`1.6`) to `completed` with today's date and minutes ≈ 100, set `current` to `1.7`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 1.7: Diagnostic review & your personal focus plan. Turn your diagnostic into a personal plan.

STOP: Ready for 1.7? Type `/next` (or `/start 1.7`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] exams/diagnostic.md and answers exist
- [ ] Diagnostic graded; report written
- [ ] Error log and scores.csv populated
- [ ] Weak KAs recorded in progress.json
