# Lesson 5.5: Lab: business case & financial analysis (NPV, IRR, ROI, payback)

*Module 5 · Week 6 · ~90 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Business Cases](CBAP%20Knowledge%20Graph/05%20Techniques/Business%20Cases.md)
- [Financial Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Financial%20Analysis.md)
- [Estimation](CBAP%20Knowledge%20Graph/05%20Techniques/Estimation.md)

---

David Chen: *"I need payback within 3 years and a positive NPV, or this doesn't go to the board."* Today you build the business case and do the calculations the exam expects you to understand.

By the end of this session you will be able to:
- Structure a business case (need, outcomes, alternatives, recommendation)
- Calculate ROI, payback, NPV; interpret IRR
- Explain TCO, cost of change and sensitivity analysis

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Business cases

ACTION: Re-read [Business Cases](CBAP%20Knowledge%20Graph/05%20Techniques/Business%20Cases.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Business case sections: Need Assessment, Desired Outcomes, Assess Alternatives (including do nothing: scope, feasibility, assumptions, risks, constraints, financial analysis), Recommended Solution.
- A business case is a living document, revisited when the context changes.

---

## Part 2: Financial analysis

ACTION: Re-read [Financial Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Financial%20Analysis.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Cost of the change, total cost of ownership (acquire + operate over the life), value realization, cost-benefit analysis.
- ROI = (total benefits − total costs) / total costs. Payback period = time until cumulative benefits cover costs (no time value of money).
- Present value: future cash discounted, PV = CF / (1 + r)^t. NPV = sum of PVs minus the initial investment. Positive NPV = worth doing at that discount rate.
- IRR = the discount rate where NPV = 0. Higher is better, compared against the hurdle rate. Sensitivity analysis tests how results change when assumptions vary.

STOP: Investment $1.1M now; net benefits $500k per year for 3 years; discount rate 10%. Rough NPV?

USER: About +$143k

ACTION: Give feedback. A strong answer includes: PV = 500/1.1 + 500/1.21 + 500/1.331 ≈ 454.5 + 413.2 + 375.7 = 1,243.4; NPV ≈ 1,243 − 1,100 = +$143k. Payback ≈ 2.2 years.

---

## Apply it at GreenBasket: Business case: three alternatives + do nothing

Use the vendor proposals and your own assumptions (state them).

ACTION: Open and skim [13-vendor-proposals](case-files/13-vendor-proposals.md), [05-market-and-sales-data](case-files/05-market-and-sales-data.csv), [43-change-strategy-and-solution-scope](workspace/43-change-strategy-and-solution-scope.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Compute a 3-year view for ShelfWise, CodeHarbor and OmniGrocer (one-off + run cost + extra items such as the Connect API, coupons module, security review, pickers), with an assumed benefit ramp (state your assumptions, e.g. online sales margin). Then give ROI, payback and NPV at 10% for each, and a do-nothing line (revenue erosion).

USER: Drafts their analysis in the chat

ACTION: Do the arithmetic carefully (show a table; you may use a quick Python calculation via Bash to avoid errors), coach interpretation, add a sensitivity check (benefits −30%), and save the business case with the 4 BABOK sections. Save the result to `workspace/44-business-case.md` and link it: [44-business-case.md](workspace/44-business-case.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `elena-sponsor`, giving it the path `workspace/44-business-case.md` and ask whether this is board-ready and what the CFO will challenge. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: business case structure, ROI, payback, PV/NPV, IRR interpretation, TCO, sensitivity analysis; includes 3 small calculations.
Build distractors from these traps: payback considers time value (it doesn't); IRR vs NPV meaning; ROI formula inverted; TCO = purchase price only.
Log to scores.csv with ka=`TECH` and topic=`financial-analysis`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Business case = need, outcomes, alternatives (incl. do nothing), recommendation.
2. NPV > 0 → value-creating at that rate; IRR = rate where NPV = 0.
3. Payback ignores the time value of money.

**Reading before the next session:**
- BABOK 10.7, 10.20 (pp.234–235, 274–278)
- Lessing pp.361–363, 384–388
- Jonasson 7.3.5, 7.5 (pp.156–158)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- NPV? :: Sum of discounted future cash flows minus initial investment
- IRR? :: Discount rate at which NPV = 0
- Business case sections (BABOK)? :: Need Assessment; Desired Outcomes; Assess Alternatives; Recommended Solution

ACTION: Update [progress.json](progress/progress.json): add this lesson (`5.5`) to `completed` with today's date and minutes ≈ 90, set `current` to `5.6`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 5.6: Lab: strategy techniques (BMC, capability analysis, benchmarking, balanced scorecard). The strategy toolkit, applied.

STOP: Ready for 5.6? Type `/next` (or `/start 5.6`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/44-business-case.md created with calculations
- [ ] Student computed NPV correctly
- [ ] Drill logged
