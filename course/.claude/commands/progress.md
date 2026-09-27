---
description: Show your CBAP study dashboard — lessons done, schedule, scores by knowledge area, weak topics
---
Read `course-structure.json`, `progress/progress.json`, `progress/scores.csv`, and `progress/error-log.md`. Then show a compact dashboard:

1. **Where you are:** current phase, week and lesson; lessons completed out of the total; completion %.
2. **Schedule check:** compare `start_date` in progress.json with today. Each week in course-structure.json has about 10 hours. Say whether they are ahead, on track, or behind, and by how many lessons.
3. **Scores by knowledge area:** aggregate scores.csv by `ka` (correct/total, %), compared against the exam weight and the 75% target. Flag any KA under 70%.
4. **Top 5 weak topics:** from error-log.md, the most frequent tags or concepts.
5. **Recommendation:** one concrete next step (for example `/next`, or `/drill RADD 10` if a KA is weak).

Keep it short and scannable with a small table. Don't modify any files.
