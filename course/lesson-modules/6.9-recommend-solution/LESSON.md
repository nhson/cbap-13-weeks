# Lesson 6.9: 7.6 Analyze Potential Value and Recommend Solution

*Module 6 · Week 8 · ~85 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Analyze Potential Value and Recommend Solution](CBAP%20Knowledge%20Graph/03%20Tasks/Analyze%20Potential%20Value%20and%20Recommend%20Solution.md)
- [Solution Recommendation](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Solution%20Recommendation.md)
- [Decision Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Decision%20Analysis.md)
- [Acceptance and Evaluation Criteria](CBAP%20Knowledge%20Graph/05%20Techniques/Acceptance%20and%20Evaluation%20Criteria.md)
- [Financial Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Financial%20Analysis.md)

---

Decision day. Elena likes ShelfWise; the evidence may not. **7.6 Analyze Potential Value and Recommend Solution**, where BAs earn their credibility.

By the end of this session you will be able to:
- Know the 4 elements of 7.6
- Weigh expected benefits and costs to determine value
- Recommend, including "none" or "do nothing" when that's right

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Analyze Potential Value and Recommend Solution

ACTION: Re-read [Analyze Potential Value and Recommend Solution](CBAP%20Knowledge%20Graph/03%20Tasks/Analyze%20Potential%20Value%20and%20Recommend%20Solution.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Compare the value of each design option and recommend the most suitable one, or none.
- Elements: Expected Benefits, Expected Costs (acquisition, operation, opportunity cost…), Determine Value, Assess Design Options and Recommend Solution (considering available resources, constraints, dependencies).
- The recommendation may be that no option delivers enough value, so do nothing or re-scope.
- Inputs: Potential Value, Design Options. Output: Solution Recommendation.

STOP: What if every option costs more than the value it delivers?

USER: Recommend none / do nothing / reconsider

ACTION: Give feedback. A strong answer includes: recommend not proceeding (or re-scoping). It's a valid BABOK recommendation.

---

## Apply it at GreenBasket: Solution recommendation

Weighted scoring plus value, then a recommendation Elena can take to the board.

ACTION: Open and skim [56-design-options](workspace/56-design-options.md), [44-business-case](workspace/44-business-case.md), [13-vendor-proposals](case-files/13-vendor-proposals.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Build a weighted evaluation matrix (criteria from your validated requirements and risks: fit to Musts, time to pilot, 3-year TCO, integration, compliance, scalability and references, lock-in), score each option, and make a recommendation with conditions.

USER: Drafts their analysis in the chat

ACTION: Coach and save. The evidence usually favours OmniGrocer (fit, compliance, references at scale, integration layer) despite a higher one-off cost than ShelfWise. Include the conditions: coupons module decision, inventory-accuracy programme, security review in parallel. Save the result to `workspace/57-solution-recommendation.md` and link it: [57-solution-recommendation.md](workspace/57-solution-recommendation.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `elena-sponsor`, giving it the path `workspace/57-solution-recommendation.md` and present the recommendation; she preferred ShelfWise. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 7.6 elements, benefits and costs incl. opportunity cost, determining value, recommendation options incl. none.
Build distractors from these traps: recommend the cheapest; must always recommend an option; Solution Recommendation vs Change Strategy; Potential Value produced in 7.6 (it comes from 6.2).
Log to scores.csv with ka=`RADD` and topic=`7.6`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Value = expected benefits − expected costs (incl. opportunity cost), in context.
2. Recommending "none" is legitimate.
3. Output: Solution Recommendation.

> **Exam rule of thumb:** The BA recommends the option with the best value for the *need*, not the sponsor's favourite or the cheapest.

**Reading before the next session:**
- BABOK 7.6 (pp.157–162)
- Lessing pp.259–275 (incl. knowledge quiz)
- Jonasson 8.3.6 (p.218)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 7.6 elements? :: Expected Benefits; Expected Costs; Determine Value; Assess Design Options & Recommend Solution
- 7.6 inputs? :: Potential Value; Design Options

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.9`) to `completed` with today's date and minutes ≈ 85, set `current` to `6.10`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.10: RADD techniques lab I: NFRs, acceptance criteria, prototyping, interface analysis. Qualities, interfaces and prototypes.

STOP: Ready for 6.10? Type `/next` (or `/start 6.10`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/57-solution-recommendation.md created and sponsor-reviewed
- [ ] Drill logged; task card added
