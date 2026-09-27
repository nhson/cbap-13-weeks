---
description: Grade a written exam (diagnostic or mock) — `/grade mock-1`
argument-hint: "<exam id: diagnostic | mock-1 | mock-2 | mock-3>"
---
Grade the exam "$ARGUMENTS".

1. Read the answer sheet `exams/$ARGUMENTS-answers.md` (the student's answers) and the key `exams/.keys/$ARGUMENTS-key.md`. If either is missing, say which file is missing and stop.
2. Score it: total and %, plus a breakdown by knowledge area and by question type (scenario, definition, I/O-flow, technique), compared with the pass target (75% for mocks, just a baseline for the diagnostic).
3. For every wrong or blank answer, append an entry to `progress/error-log.md` using its template, with the key's explanation and knowledge-graph link. Append one line per KA to `progress/scores.csv` (lesson = the exam id).
4. Write `exams/$ARGUMENTS-report.md`: score table, top weak tasks and techniques, confusions detected (use `CBAP Knowledge Graph/08 Exam Lens/Commonly Confused Concepts.md`), and a gap-closing plan of 3–5 bullets.
5. Show the student the headline results and link the report. Read `.claude/rules/teaching-rules.md` for tone.
