# Lesson 5.2: 6.2 Define Future State

*Module 5 · Week 6 · ~80 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Define Future State](CBAP%20Knowledge%20Graph/03%20Tasks/Define%20Future%20State.md)
- [Business Objectives](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Business%20Objectives.md)
- [Future State Description](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Future%20State%20Description.md)
- [Potential Value](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Potential%20Value.md)
- [Business Model Canvas](CBAP%20Knowledge%20Graph/05%20Techniques/Business%20Model%20Canvas.md)
- [Balanced Scorecard](CBAP%20Knowledge%20Graph/05%20Techniques/Balanced%20Scorecard.md)

---

Elena's email has goals ("most convenient neighbourhood grocer") and targets ("5% online share"). Today you turn them into a proper future state: **6.2 Define Future State**.

By the end of this session you will be able to:
- Know the 11 elements of 6.2
- Write SMART business objectives
- Define constraints, assumptions and potential value

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Define Future State

ACTION: Re-read [Define Future State](CBAP%20Knowledge%20Graph/03%20Tasks/Define%20Future%20State.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Describe the target conditions that would satisfy the business need, including measurable objectives and the value expected.
- Elements: Business Goals and Objectives, Scope of Solution Space, Constraints, Organizational Structure and Culture, Capabilities and Processes, Technology and Infrastructure, Policies, Business Architecture, Internal Assets, Identify Assumptions, Potential Value.
- Goals: long-term, ongoing, qualitative. Objectives: measurable, **SMART** (Specific, Measurable, Achievable, Relevant, Time-bounded).
- Constraints: budget, time, technology, policies, regulation… Assumptions must be identified because they carry risk.
- Input: Business Requirements. Outputs: **Business Objectives, Future State Description, Potential Value**.

STOP: Make "improve pickup experience" SMART.

USER: A measurable, time-bound objective

ACTION: Give feedback. A strong answer includes: e.g. "95% of pickups completed within 5 minutes of customer arrival across pilot stores by week 10 of the pilot".

**Exam trap to call out:** Goals vs objectives: the measurable one is the *objective*.

---

## Apply it at GreenBasket: Future State Description

Describe what "good" looks like, including the parts that aren't software.

ACTION: Open and skim [01-sponsor-kickoff-email](case-files/01-sponsor-kickoff-email.md), [08-compliance-memo](case-files/08-compliance-memo.md), [07-it-landscape](case-files/07-it-landscape.md), [40-current-state-description](workspace/40-current-state-description.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Draft: 1 goal plus 4 SMART objectives; the future state across capabilities and processes, organization and culture (e.g. picker role, incentives), technology, and policies; 4 constraints; 4 assumptions; and a potential value statement (tangible and intangible).

USER: Drafts their analysis in the chat

ACTION: Coach and save. Check SMARTness, and that "real-time stock" becomes a feasible future state (near-real-time plus stock confidence plus inventory accuracy improvement). Assumptions such as "loyalty API supports coupons" should be flagged as false (it doesn't). Save the result to `workspace/41-future-state-description.md` and link it: [41-future-state-description.md](workspace/41-future-state-description.md).

A model answer should cover (use it to coach, don't just paste it):
- Objectives: online share 2% of pilot-store sales by pilot week 10; 5% chain-wide within 2 years of launch; order accuracy ≥97%; ready-in-2h ≥95%
- Future state: dedicated picker roles funded centrally, staging with temperature control, inventory accuracy ≥95% in pilot stores, pickup bays where space allows
- Constraints: $3.2M budget, 6-month pilot, union 45-day consultation, PCI, alcohol rules
- Potential value: revenue retention plus online growth (tangible); convenience and brand relevance (intangible); negative value: picker labour and platform run cost

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 6.2 elements, goals vs objectives, SMART, constraints and assumptions, outputs (business objectives, future state description, potential value).
Build distractors from these traps: goal presented as objective; assumptions ignored; potential value only financial; outputs mixed up with 6.1.
Log to scores.csv with ka=`SA` and topic=`6.2`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Goals are qualitative; objectives are SMART.
2. 11 elements; the future state covers people, process, technology and policy.
3. Outputs: Business Objectives, Future State Description, Potential Value.

**Reading before the next session:**
- BABOK 6.2 (pp.110–119), 10.3 Balanced Scorecard, 10.8 Business Model Canvas
- Lessing pp.198–206

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 6.2 outputs? :: Business Objectives; Future State Description; Potential Value
- SMART? :: Specific, Measurable, Achievable, Relevant, Time-bounded
- Goal vs objective? :: Goal = long-term qualitative; objective = measurable, SMART

ACTION: Update [progress.json](progress/progress.json): add this lesson (`5.2`) to `completed` with today's date and minutes ≈ 80, set `current` to `5.3`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 5.3: 6.3 Assess Risks. Risk of changing and of not changing, plus risk tolerance.

STOP: Ready for 5.3? Type `/next` (or `/start 5.3`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/41-future-state-description.md created
- [ ] SMART objectives written
- [ ] Drill logged; task card added
