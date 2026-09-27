# Lesson 7.2: 8.2 Analyze Performance Measures

*Module 7 · Week 9 · ~80 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Analyze Performance Measures](CBAP%20Knowledge%20Graph/03%20Tasks/Analyze%20Performance%20Measures.md)
- [Solution Performance Analysis](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Solution%20Performance%20Analysis.md)
- [Potential Value](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Potential%20Value.md)
- [15-pilot-metrics](case-files/15-pilot-metrics.csv)

---

The averages hide the story. Riverton hits 97.4% accuracy; Hillcrest is falling to 86%. **8.2 Analyze Performance Measures** asks: how is the solution performing against its *potential value*, and why?

By the end of this session you will be able to:
- Know the 5 elements of 8.2
- Analyze trends and variances
- Judge the accuracy and significance of data

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Analyze Performance Measures

ACTION: Re-read [Analyze Performance Measures](CBAP%20Knowledge%20Graph/03%20Tasks/Analyze%20Performance%20Measures.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Interpret the performance measures to see how the solution is delivering value compared with what was expected.
- Elements: Solution Performance versus Desired Value, Risks, Trends, Accuracy, Performance Variances.
- Inputs: Potential Value (from 6.2), Solution Performance Measures. Output: Solution Performance Analysis.
- Look at time periods long enough to reveal trends, and check that data is accurate and reproducible. Examine the root causes of variances.

STOP: Which input gives you the "benchmark" to compare actual performance against?

USER: Potential Value

ACTION: Give feedback. A strong answer includes: Potential Value (from Define Future State).

---

## Apply it at GreenBasket: Analyze the pilot data

Let the data speak. You can compute it.

ACTION: Open and skim [15-pilot-metrics](case-files/15-pilot-metrics.csv), [14-pilot-results](case-files/14-pilot-results.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Look at the CSV: per store, what are the trends from week 2 → 10 in accuracy, OOS-at-pick and picker hours actual vs scheduled? What variance patterns do you see? What correlates with poor accuracy?

USER: Drafts their analysis in the chat

ACTION: Run a quick analysis (Python via Bash on the CSV: per-store week-10 values, deltas, and the correlation between picker-hours shortfall and accuracy or OOS). Coach interpretation and save a Solution Performance Analysis with a table and 4–5 insights. Expected: Bayview and Hillcrest have large picker-hour shortfalls (~45–40% under schedule) and the highest OOS-at-pick; Hillcrest worsens after week 4 (aisle reset); the strong stores staff pickers as scheduled. Save the result to `workspace/61-solution-performance-analysis.md` and link it: [61-solution-performance-analysis.md](workspace/61-solution-performance-analysis.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 8.2 elements, performance vs desired value, trends, accuracy, variances, input Potential Value.
Build distractors from these traps: Potential Value produced in SE; one data point = trend; analysis vs limitation assessment.
Log to scores.csv with ka=`SE` and topic=`8.2`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Compare actual performance against Potential Value.
2. Elements: vs desired value, risks, trends, accuracy, variances.
3. Output: Solution Performance Analysis.

**Reading before the next session:**
- BABOK 8.2 (pp.170–172)
- Lessing pp.286–291

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 8.2 elements? :: Solution Performance vs Desired Value; Risks; Trends; Accuracy; Performance Variances
- 8.2 inputs? :: Potential Value; Solution Performance Measures

ACTION: Update [progress.json](progress/progress.json): add this lesson (`7.2`) to `completed` with today's date and minutes ≈ 80, set `current` to `7.3`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 7.3: 8.3 Assess Solution Limitations. What inside the solution is holding value back?

STOP: Ready for 7.3? Type `/next` (or `/start 7.3`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/61-solution-performance-analysis.md created with computed data
- [ ] Drill logged; task card added
