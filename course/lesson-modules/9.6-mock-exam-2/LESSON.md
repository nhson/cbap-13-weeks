# Lesson 9.6: Full Mock Exam #2

*Module 9 · Week 12 · ~225 min in session + ~0 min reading*

## Prepare (instructor: read silently before teaching)
- [Exam Blueprint](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Exam%20Blueprint.md)
- [error-log](progress/error-log.md)

---

Mock #2. The roadmap target is **75% or more**. This mock leans slightly into your weak topics, so it will feel harder than the real exam.

STOP: Ready for 210 minutes under exam conditions?

USER: Ready

---

## Generate Mock Exam 2

ACTION: Silently read `CBAP Knowledge Graph/08 Exam Lens/Exam Blueprint.md`, `Commonly Confused Concepts.md`, `BABOK Input-Output Flow.md`, `progress/error-log.md` and the 6 KA notes. Then write **Mock Exam 2: 120 original CBAP-style questions** to `exams/mock-2.md`, in 4 batches of 30 (append each batch; check facts against task and technique notes as you go):
- Blueprint: RADD 36, RLCM 18, SA 18, BAPM 17, SE 17, E&C 14. Techniques, perspectives and competencies are embedded inside KA questions.
- Types: ~65% scenario, including **3 case studies** (a 1–2 paragraph scenario followed by 4–5 questions each, all in fresh contexts, not GreenBasket); ~20% input/output/technique selection; ~15% definitions and concepts.
- Difficulty: real-exam level. Several plausible options, one most BABOK-correct. Weight ~25% of the questions towards the student's error-log weak topics.
- Don't reuse questions from earlier drills or mocks (check `exams/` for previous mocks).
- Key → `exams/.keys/mock-2-key.md`: number | answer | KA | task/technique | type | rationale (2 lines) | knowledge-graph note.
- Answer sheet → `exams/mock-2-answers.md` with `1: ` … `120: ` lines.

Link [mock-2.md](exams/mock-2.md) and [mock-2-answers.md](exams/mock-2-answers.md). Never reveal the key.

STOP: Exam conditions: **210 minutes**, one sitting, no notes, phone away. Mark guesses with `?`. Flag and move on after 2 minutes on any question. Tell me "done" when finished (or "pause" if you must stop, and note the time used).

USER: done

ACTION: Grade exactly as the `/grade mock-2` command does (score, per-KA and per-type breakdown, error log, scores.csv, report in `exams/mock-2-report.md`). Also compute the time used per question if the student reports the total time.

---

## Debrief

Compare mock 2 with mock 1: total, per KA, time per question.

STOP: What changed compared with mock 1?

USER: Responds

---

## Wrap-up

**Key takeaways:**
1. Two data points are enough to see a trend.
2. The week-12 milestone is two mocks at 75% or more.

ACTION: Update [progress.json](progress/progress.json): add this lesson (`9.6`) to `completed` with today's date and minutes ≈ 225, set `current` to `9.7`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 9.7: Mock #2 review & gap plan II. Review, and decide whether the exam date holds.

STOP: Ready for 9.7? Type `/next` (or `/start 9.7`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Mock 2 generated, taken and graded
- [ ] Comparison with mock 1 done
