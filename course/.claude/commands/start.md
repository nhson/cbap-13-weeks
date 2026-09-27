---
description: Start a CBAP lesson — `/start 2.3`, or `/start` alone to resume where you left off
argument-hint: "[lesson id, e.g. 2.3]"
---
Start a CBAP course lesson. Do this SILENTLY — don't announce these steps:

1. Read `course-structure.json`.
2. Read `progress/progress.json`.
3. Pick the lesson: if the argument "$ARGUMENTS" is a lesson id (like `2.3`), use it; if empty, use `current` from progress.json (default `1.1`).
4. Read `.claude/rules/teaching-rules.md` and follow it for the whole lesson.
5. Read the lesson script at the `path` given for that lesson in course-structure.json.
6. Read the knowledge-graph notes the script lists under **Prepare** before teaching.
7. Begin teaching immediately with the first line of the script — no preamble.
