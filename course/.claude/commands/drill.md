---
description: Quick exam drill — `/drill` (adaptive on weak areas), `/drill RADD 12`, `/drill "verify vs validate" 8`
argument-hint: "[KA short name or topic] [number of questions]"
---
Run an exam drill outside a lesson.

1. Read `.claude/rules/teaching-rules.md` (section 6 applies), `progress/error-log.md` and `progress/scores.csv`.
2. Parse "$ARGUMENTS": an optional KA (BAPM, E&C, RLCM, SA, RADD, SE, TECH, COMP, PERSP) or quoted topic, and an optional count (default 8, max 20).
   - If there is no KA or topic, weight the questions towards the weakest KAs and the most frequent error-log topics, while keeping about 30% for exam-weighted coverage (RADD 30%, RLCM 15%, SA 15%, BAPM 14%, SE 14%, E&C 12%).
3. Before writing the questions, read the relevant knowledge-graph notes in `CBAP Knowledge Graph/` so every fact is BABOK-exact.
4. Run the drill with AskUserQuestion, 4 questions per call. Then give explanations, log to scores.csv (lesson = `drill`) and error-log.md, and finish with a one-line verdict and the next best action.
