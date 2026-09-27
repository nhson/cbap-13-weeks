# Lesson 9.2: Full Mock Exam #1 (120 questions, 210 minutes)

*Module 9 · Week 11 · ~225 min in session + ~0 min reading*

## Prepare (instructor: read silently before teaching)
- [Exam Blueprint](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Exam%20Blueprint.md)
- [Commonly Confused Concepts](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Commonly%20Confused%20Concepts.md)
- [BABOK Input-Output Flow](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/BABOK%20Input-Output%20Flow.md)

---

Mock #1. Full length, full time, exam conditions. The score matters less than the data it gives us.

STOP: Do you have about 3 hours 45 minutes free now (210 min exam + setup)? If not, I'll prepare the exam and you start when ready.

USER: Ready

---

## Generate Mock Exam 1

ACTION: Silently read `CBAP Knowledge Graph/08 Exam Lens/Exam Blueprint.md`, `Commonly Confused Concepts.md`, `BABOK Input-Output Flow.md`, `progress/error-log.md` and the 6 KA notes. Then write **Mock Exam 1: 120 original CBAP-style questions** to `exams/mock-1.md`, in 4 batches of 30 (append each batch; check facts against task and technique notes as you go):
- Blueprint: RADD 36, RLCM 18, SA 18, BAPM 17, SE 17, E&C 14. Techniques, perspectives and competencies are embedded inside KA questions.
- Types: ~65% scenario, including **3 case studies** (a 1–2 paragraph scenario followed by 4–5 questions each, all in fresh contexts, not GreenBasket); ~20% input/output/technique selection; ~15% definitions and concepts.
- Difficulty: real-exam level. Several plausible options, one most BABOK-correct. 
- Don't reuse questions from earlier drills or mocks (check `exams/` for previous mocks).
- Key → `exams/.keys/mock-1-key.md`: number | answer | KA | task/technique | type | rationale (2 lines) | knowledge-graph note.
- Answer sheet → `exams/mock-1-answers.md` with `1: ` … `120: ` lines.

Link [mock-1.md](exams/mock-1.md) and [mock-1-answers.md](exams/mock-1-answers.md). Never reveal the key.

STOP: Exam conditions: **210 minutes**, one sitting, no notes, phone away. Mark guesses with `?`. Flag and move on after 2 minutes on any question. Tell me "done" when finished (or "pause" if you must stop, and note the time used).

USER: done

ACTION: Grade exactly as the `/grade mock-1` command does (score, per-KA and per-type breakdown, error log, scores.csv, report in `exams/mock-1-report.md`). Also compute the time used per question if the student reports the total time.

---

## Immediate debrief

Share the total %, the per-KA table vs the 75% target, and time per question.

STOP: How did the pacing feel, and where did you get stuck?

USER: Responds

ACTION: Note the pacing issues in progress.json `notes`.

---

## Wrap-up

**Key takeaways:**
1. First full mock done. Your stamina and pacing are now measured.
2. Target: 75% or more on mocks by week 12.

ACTION: Update [progress.json](progress/progress.json): add this lesson (`9.2`) to `completed` with today's date and minutes ≈ 225, set `current` to `9.3`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 9.3: Mock #1 deep review & gap plan. Every wrong AND every guessed answer, reviewed against the BABOK.

STOP: Ready for 9.3? Type `/next` (or `/start 9.3`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Mock 1 generated, taken and graded
- [ ] Report written; error log updated
