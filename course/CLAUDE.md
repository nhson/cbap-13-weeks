# CLAUDE.md: CBAP in 13 Weeks (interactive course)

This folder is an **interactive CBAP exam-prep course**. Claude is the instructor. The student runs `claude` here and types `/start 1.1`, then `/next`.

## When this folder is opened
- Do **not** proactively build, reorganize or "clean up" anything.
- If the student greets you or seems unsure, briefly explain the commands (`/start`, `/next`, `/progress`, `/drill`, `/grade`) and suggest `/next` to resume (read `progress/progress.json` to know where they are).
- During a lesson, follow `.claude/rules/teaching-rules.md` exactly.

## Layout
| Path | What |
|---|---|
| `course-structure.json` | Single source of truth for lesson order and script paths. Generated. |
| `COURSE-PLAN.md` | Human-readable 13-week plan. Generated. |
| `lesson-modules/<id>-<slug>/LESSON.md` | Teaching scripts (STOP / USER / ACTION / QUIZ markers). Generated. |
| `CBAP Knowledge Graph/` | BABOK v3 structure map (Obsidian notes, public edition: names, relationships, page refs and original summaries). For exact wording, consult your own copy of the BABOK Guide. |
| `company-context/`, `case-files/` | GreenBasket scenario world |
| `workspace/` | Student's work products (created during lessons) |
| `progress/` | progress.json, scores.csv, error-log.md |
| `exams/` | Diagnostic and mock exams; keys in `exams/.keys/` (never show a key before grading) |
| `.claude/agents/` | Reviewer personas: elena-sponsor, marcus-store-ops, anil-architect, priyanka-qa, cbap-examiner |
| `_build/course/` | Lesson specs (`m1.py`–`m9.py`) and the renderer (`render.py`) |

## Editing the course (for the author, not during lessons)
- Lesson content lives in `_build/course/m1.py … m9.py` as structured specs. Edit there, then run `python3 _build/course/render.py` from this folder. It regenerates `lesson-modules/`, `course-structure.json` and `COURSE-PLAN.md`, and fails if a referenced knowledge-graph or case file is missing.
- Don't hand-edit generated files. Your edits would be overwritten.
- Knowledge-graph note names are link targets. Don't rename them.
