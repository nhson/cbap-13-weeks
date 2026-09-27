# Lesson 7.3: 8.3 Assess Solution Limitations

*Module 7 · Week 9 · ~70 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Assess Solution Limitations](CBAP%20Knowledge%20Graph/03%20Tasks/Assess%20Solution%20Limitations.md)
- [Solution Limitation](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Solution%20Limitation.md)
- [Root Cause Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Root%20Cause%20Analysis.md)
- [Commonly Confused Concepts](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Commonly%20Confused%20Concepts.md)

---

Some problems live *inside* the solution: the substitution chat nobody uses, stock status that is wrong, handhelds dying. **8.3 Assess Solution Limitations**.

By the end of this session you will be able to:
- Know the 3 elements of 8.3
- Investigate solution problems (root cause)
- Separate solution vs enterprise limitations

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Assess Solution Limitations

ACTION: Re-read [Assess Solution Limitations](CBAP%20Knowledge%20Graph/03%20Tasks/Assess%20Solution%20Limitations.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Find the factors inside the solution that stop it from delivering its full value.
- Elements: Identify Internal Solution Component Dependencies, Investigate Solution Problems (where outputs are below acceptable quality, or potential value is not realized), Impact Assessment (size and severity, likelihood, impact on operations, capacity to absorb impact).
- Inputs: Implemented Solution (external), Solution Performance Analysis. Output: Solution Limitation.

STOP: "Stock shown as available is wrong because StockPoint is wrong." Solution limitation or enterprise limitation?

USER: Debatable: data within the solution's components is a solution limitation; data governance is enterprise

ACTION: Give feedback. A strong answer includes: the stock feed is a solution component dependency (StockPoint and its integration are part of the solution), so it is a solution limitation. The *process* causing poor accuracy (cycle counts, reset updates) is an enterprise issue. Good answers separate the two.

---

## Apply it at GreenBasket: Solution limitations register

Identify the internal factors.

ACTION: Open and skim [14-pilot-results](case-files/14-pilot-results.md), [61-solution-performance-analysis](workspace/61-solution-performance-analysis.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: List the solution limitations (component dependencies, problems), each with root cause and impact assessment (size, severity, likelihood, impact on operations). Keep enterprise issues aside for the next lesson.

USER: Drafts their analysis in the chat

ACTION: Coach and save. Examples: stock-status accuracy (StockPoint dependency); aisle data not refreshed after resets; handheld battery life; substitution chat UX too slow; coupon module deferred. Save the result to `workspace/62-solution-limitations.md` and link it: [62-solution-limitations.md](workspace/62-solution-limitations.md).

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 8.3 elements, internal solution factors, impact assessment, solution vs enterprise limitation.
Build distractors from these traps: culture issue as solution limitation; Solution Limitation output from 8.4.
Log to scores.csv with ka=`SE` and topic=`8.3`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Solution limitations are INSIDE the solution.
2. Elements: dependencies, investigate problems, impact assessment.

**Reading before the next session:**
- BABOK 8.3 (pp.173–176)
- Lessing pp.291–295

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 8.3 elements? :: Identify Internal Solution Component Dependencies; Investigate Solution Problems; Impact Assessment

ACTION: Update [progress.json](progress/progress.json): add this lesson (`7.3`) to `completed` with today's date and minutes ≈ 70, set `current` to `7.4`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 7.4: 8.4 Assess Enterprise Limitations. Incentives, culture, structure: the problems outside the software.

STOP: Ready for 7.4? Type `/next` (or `/start 7.4`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/62-solution-limitations.md created
- [ ] Drill logged; task card added
