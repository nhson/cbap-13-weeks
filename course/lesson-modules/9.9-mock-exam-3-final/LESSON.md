# Lesson 9.9: Final Mock Exam #3: go/no-go

*Module 9 · Week 13 · ~225 min in session + ~0 min reading*

## Prepare (instructor: read silently before teaching)
- [Exam Blueprint](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Exam%20Blueprint.md)
- [error-log](progress/error-log.md)

---

Final mock. The roadmap target is **80% or more** as your go signal. Treat it exactly like exam day: same time of day as your real exam if possible.

STOP: Are you set up like exam day (time of day, quiet room, no notes)?

USER: Ready

---

## Generate Mock Exam 3

ACTION: Silently read `CBAP Knowledge Graph/08 Exam Lens/Exam Blueprint.md`, `Commonly Confused Concepts.md`, `BABOK Input-Output Flow.md`, `progress/error-log.md` and the 6 KA notes. Then write **Mock Exam 3: 120 original CBAP-style questions** to `exams/mock-3.md`, in 4 batches of 30 (append each batch; check facts against task and technique notes as you go):
- Blueprint: RADD 36, RLCM 18, SA 18, BAPM 17, SE 17, E&C 14. Techniques, perspectives and competencies are embedded inside KA questions.
- Types: ~65% scenario, including **3 case studies** (a 1–2 paragraph scenario followed by 4–5 questions each, all in fresh contexts, not GreenBasket); ~20% input/output/technique selection; ~15% definitions and concepts.
- Difficulty: real-exam level. Several plausible options, one most BABOK-correct. Weight ~25% of the questions towards the student's error-log weak topics.
- Don't reuse questions from earlier drills or mocks (check `exams/` for previous mocks).
- Key → `exams/.keys/mock-3-key.md`: number | answer | KA | task/technique | type | rationale (2 lines) | knowledge-graph note.
- Answer sheet → `exams/mock-3-answers.md` with `1: ` … `120: ` lines.

Link [mock-3.md](exams/mock-3.md) and [mock-3-answers.md](exams/mock-3-answers.md). Never reveal the key.

STOP: Exam conditions: **210 minutes**, one sitting, no notes, phone away. Mark guesses with `?`. Flag and move on after 2 minutes on any question. Tell me "done" when finished (or "pause" if you must stop, and note the time used).

USER: done

ACTION: Grade exactly as the `/grade mock-3` command does (score, per-KA and per-type breakdown, error log, scores.csv, report in `exams/mock-3-report.md`). Also compute the time used per question if the student reports the total time.

---

## Go / no-go

ACTION: Compare all three mocks (total and per KA). Apply the rule: ≥80% = go; 75–79% = go with a focused final review; <75% = strongly consider rescheduling.

STOP: Here's the verdict. How do you feel about it?

USER: Responds

---

## Wrap-up

**Key takeaways:**
1. Three mocks give a reliable picture.
2. Decide calmly with data.

ACTION: Update [progress.json](progress/progress.json): add this lesson (`9.9`) to `completed` with today's date and minutes ≈ 225, set `current` to `9.10`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 9.10: Final review: I/O map, technique sheet, confusions, glossary sprint. Light, high-yield review. No new material.

STOP: Ready for 9.10? Type `/next` (or `/start 9.10`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Mock 3 taken and graded
- [ ] Go/no-go decision made and recorded in progress.json
