# Lesson 5.3: 6.3 Assess Risks

*Module 5 · Week 6 · ~70 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Assess Risks](CBAP%20Knowledge%20Graph/03%20Tasks/Assess%20Risks.md)
- [Risk Analysis Results](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Risk%20Analysis%20Results.md)
- [Risk Analysis and Management](CBAP%20Knowledge%20Graph/05%20Techniques/Risk%20Analysis%20and%20Management.md)

---

Inventory accuracy of 74% in fresh. A union consultation that nobody has started. A security review that could add 8 weeks. **6.3 Assess Risks** makes these visible *before* the change strategy is chosen.

By the end of this session you will be able to:
- Know the 5 elements of 6.3
- Build a risk register with likelihood, impact and responses
- Explain risk tolerance (averse, neutral, seeking)

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Assess Risks

ACTION: Re-read [Assess Risks](CBAP%20Knowledge%20Graph/03%20Tasks/Assess%20Risks.md), [Risk Analysis and Management](CBAP%20Knowledge%20Graph/05%20Techniques/Risk%20Analysis%20and%20Management.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Identify and weigh the uncertainties that could reduce value during the transition or in the future state, and recommend how to proceed.
- Elements: Unknowns; Constraints, Assumptions and Dependencies; Negative Impact to Value; Risk Tolerance (risk-aversion, neutrality, risk-seeking); Recommendation.
- Recommendation: pursue the benefits regardless of risk, pursue while investing in reducing risk, seek ways to increase benefits to outweigh risk, find ways to realize benefits while reducing risk, or do not pursue.
- Risk responses (technique): avoid, transfer, mitigate, accept, and for opportunities increase. Risk level = likelihood × impact.
- Inputs: Business Objectives, Elicitation Results (confirmed), Influences, Potential Value, Requirements (prioritized). Output: Risk Analysis Results.

STOP: Buying insurance or contracting the courier to carry delivery liability is which response?

USER: Transfer

ACTION: Give feedback. A strong answer includes: transfer (sharing): moving the impact to a third party.

**Exam trap to call out:** Assess the risks of *not* changing too. Doing nothing has risks (continued share loss).

---

## Apply it at GreenBasket: Risk register and recommendation

Give Elena and David an honest risk picture.

ACTION: Open and skim [07-it-landscape](case-files/07-it-landscape.md), [08-compliance-memo](case-files/08-compliance-memo.md), [02-harvest-postmortem](case-files/02-harvest-postmortem.md), [41-future-state-description](workspace/41-future-state-description.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Build a risk register of at least 8 risks (including one risk of NOT changing): cause → risk → consequence, likelihood (1–5), impact (1–5), score, response type, owner. What is the organization's risk tolerance, and what's your recommendation?

USER: Drafts their analysis in the chat

ACTION: Coach and save with a heat-map table. Key risks: inventory data quality (mitigate: cycle counts and a stock-confidence indicator); union consultation delay (mitigate: start now); security review adds 6–8 weeks (mitigate: start in parallel); store adoption (mitigate: central picker funding, pilot store choice); vendor lock-in; alcohol compliance incident; handheld failure; risk of not changing (share keeps falling). Save the result to `workspace/42-risk-analysis-results.md` and link it: [42-risk-analysis-results.md](workspace/42-risk-analysis-results.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 6.3 elements, risk tolerance types, recommendation options, risk responses, inputs and output.
Build distractors from these traps: ignore risk of not changing; transfer vs mitigate; Risk Analysis Results produced by 6.4; risk-neutral vs risk-seeking.
Log to scores.csv with ka=`SA` and topic=`6.3`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 5 elements, ending in a recommendation.
2. Risk tolerance: averse, neutral, seeking.
3. Consider the risk of doing nothing.

**Reading before the next session:**
- BABOK 6.3 (pp.120–123), 10.38
- Jonasson 4.5.1 (pp.64–67) and 7.4 (p.157)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 6.3 elements? :: Unknowns; Constraints, Assumptions & Dependencies; Negative Impact to Value; Risk Tolerance; Recommendation
- Risk responses? :: Avoid, transfer, mitigate, accept (+ increase for opportunities)
- 6.3 output? :: Risk Analysis Results

ACTION: Update [progress.json](progress/progress.json): add this lesson (`5.3`) to `completed` with today's date and minutes ≈ 70, set `current` to `5.4`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 5.4: 6.4 Define Change Strategy. Gap analysis, readiness, transition states, and the solution scope.

STOP: Ready for 5.4? Type `/next` (or `/start 5.4`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/42-risk-analysis-results.md created
- [ ] Drill logged; task card added
