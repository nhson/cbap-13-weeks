# Lesson 7.5: 8.5 Recommend Actions to Increase Solution Value

*Module 7 · Week 9 · ~75 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Recommend Actions to Increase Solution Value](CBAP%20Knowledge%20Graph/03%20Tasks/Recommend%20Actions%20to%20Increase%20Solution%20Value.md)
- [Recommended Actions](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Recommended%20Actions.md)
- [Prioritization](CBAP%20Knowledge%20Graph/05%20Techniques/Prioritization.md)

---

Elena must decide: roll out chain-wide on schedule, pause, or fix first. **8.5 Recommend Actions to Increase Solution Value**, the task that closes the loop back to strategy.

By the end of this session you will be able to:
- Know the elements and recommendation types of 8.5
- Recommend actions across solution and enterprise
- Adjust the performance measures themselves when needed

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Recommend Actions

ACTION: Re-read [Recommend Actions to Increase Solution Value](CBAP%20Knowledge%20Graph/03%20Tasks/Recommend%20Actions%20to%20Increase%20Solution%20Value.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Recommend actions that close the gap between the potential and actual value of the solution.
- Elements: Adjust Solution Performance Measures (if the measures themselves are wrong), and Recommendations: **do nothing, organizational change, reduce complexity of interfaces, eliminate redundancy, avoid waste, identify additional capabilities, retire the solution**.
- Inputs: Enterprise Limitation, Solution Limitation. Output: Recommended Actions, which feed back as a guideline to 4.5 and beyond.

STOP: Hillcrest's problem is the aisle-data process and incentives. Which recommendation category fits best?

USER: Organizational change

ACTION: Give feedback. A strong answer includes: organizational change (incentives, procedures), not more software.

---

## Apply it at GreenBasket: Pilot recommendation to Elena

A decision-ready recommendation for the rollout gate.

ACTION: Open and skim [62-solution-limitations](workspace/62-solution-limitations.md), [63-enterprise-limitations](workspace/63-enterprise-limitations.md), [61-solution-performance-analysis](workspace/61-solution-performance-analysis.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Recommend actions with category (from the BABOK list), owner, expected impact, and priority. Should measures be adjusted? What is your go / conditional-go / no-go for wave-1 rollout?

USER: Drafts their analysis in the chat

ACTION: Coach and save. Likely: conditional go. Organizational change: picking in store targets and centrally funded picker hours; aisle-data update procedure tied to resets. Additional capability: coupon module. Reduce interface complexity: the substitution chat UX. Handheld replacement brought forward. Adjust measures: add inventory accuracy per store and picker-hours adherence. Save the result to `workspace/64-recommended-actions.md` and link it: [64-recommended-actions.md](workspace/64-recommended-actions.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `elena-sponsor`, giving it the path `workspace/64-recommended-actions.md` and present the go/no-go recommendation. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 8.5 elements and recommendation types, adjusting measures, inputs and output, loop back to strategy.
Build distractors from these traps: always recommend more features; do nothing never valid; retire the solution not an option.
Log to scores.csv with ka=`SE` and topic=`8.5`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Recommendations include do nothing, organizational change, reduce interface complexity, eliminate redundancy, avoid waste, add capabilities, retire.
2. Sometimes the measures themselves need adjusting.

**Reading before the next session:**
- BABOK 8.5 (pp.182–184)
- Lessing pp.300–315 (incl. knowledge quiz)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 8.5 recommendation types? :: Do nothing; organizational change; reduce complexity of interfaces; eliminate redundancy; avoid waste; identify additional capabilities; retire the solution
- 8.5 inputs? :: Enterprise Limitation; Solution Limitation

ACTION: Update [progress.json](progress/progress.json): add this lesson (`7.5`) to `completed` with today's date and minutes ≈ 75, set `current` to `7.6`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 7.6: SE techniques lab: metrics & KPIs, data mining, vendor assessment, root cause. The measurement toolkit.

STOP: Ready for 7.6? Type `/next` (or `/start 7.6`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/64-recommended-actions.md created and sponsor-reviewed
- [ ] Drill logged; task card added
