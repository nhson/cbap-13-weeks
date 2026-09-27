# Lesson 7.1: SE overview + 8.1 Measure Solution Performance

*Module 7 · Week 9 · ~80 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [Solution Evaluation](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Solution%20Evaluation.md)
- [Measure Solution Performance](CBAP%20Knowledge%20Graph/03%20Tasks/Measure%20Solution%20Performance.md)
- [Solution Performance Measures](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Solution%20Performance%20Measures.md)
- [Implemented Solution (external)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Implemented%20Solution%20%28external%29.md)
- [Metrics and Key Performance Indicators (KPIs)](CBAP%20Knowledge%20Graph/05%20Techniques/Metrics%20and%20Key%20Performance%20Indicators%20%28KPIs%29.md)
- [14-pilot-results](case-files/14-pilot-results.md)

---

Fast-forward: OmniGrocer has been live in 6 pilot stores for 10 weeks. Two stores shine, two struggle. Elena asks: *"Is it working?"* Solution Evaluation (14%) starts with **8.1 Measure Solution Performance**.

By the end of this session you will be able to:
- Explain SE's 5 tasks and chain
- Know the 3 elements of 8.1
- Define and validate quantitative and qualitative measures

STOP: Ready to dive in?

USER: Ready

---

## Part 1: SE at a glance

ACTION: Re-read [Solution Evaluation](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Solution%20Evaluation.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Five tasks: 8.1 Measure Solution Performance → 8.2 Analyze Performance Measures → 8.3 Assess Solution Limitations and 8.4 Assess Enterprise Limitations → 8.5 Recommend Actions to Increase Solution Value.
- SE evaluates solutions in any state: prototypes, proofs of concept, pilots, beta releases, operational releases.
- Chain: Solution Performance Measures → Solution Performance Analysis → Solution Limitation and Enterprise Limitation → Recommended Actions.

STOP: Can you do Solution Evaluation on a prototype that isn't live yet?

USER: Yes

ACTION: Give feedback. A strong answer includes: yes: SE applies to prototypes, PoCs, pilots, betas and operational solutions.

---

## Part 2: Measure Solution Performance

ACTION: Re-read [Measure Solution Performance](CBAP%20Knowledge%20Graph/03%20Tasks/Measure%20Solution%20Performance.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Define, validate and collect the measures that show how a solution is performing.
- Elements: Define Solution Performance Measures (quantitative and qualitative; may already exist), Validate Performance Measures (with stakeholders, aligned with business objectives), Collect Performance Measures (volume or sample size, frequency and timing, currency).
- Inputs: Business Objectives, Implemented Solution (external). Output: Solution Performance Measures.

STOP: Name one quantitative and one qualitative measure for the pilot.

USER: e.g. order accuracy %; staff or customer sentiment

ACTION: Give feedback. A strong answer includes: quantitative, e.g. accuracy %, ready-in-2h %; qualitative, e.g. CSAT verbatims, staff survey attitudes.

---

## Apply it at GreenBasket: Measures framework for the pilot

Validate that the measures actually reflect the business objectives.

ACTION: Open and skim [14-pilot-results](case-files/14-pilot-results.md), [15-pilot-metrics](case-files/15-pilot-metrics.csv), [41-future-state-description](workspace/41-future-state-description.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: List the pilot measures, map each to a business objective, state whether it is quantitative or qualitative, and assess collection (sample size, frequency, currency). Which important measure is missing?

USER: Drafts their analysis in the chat

ACTION: Coach and save. Missing measures: inventory accuracy per store (the root driver), picker hours scheduled vs actual (it IS in the CSV, so highlight it), repeat-order rate, cost per order. Save the result to `workspace/60-solution-performance-measures.md` and link it: [60-solution-performance-measures.md](workspace/60-solution-performance-measures.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: SE overview, solution states evaluated, 8.1 elements, quantitative vs qualitative measures, validation of measures, inputs and output.
Build distractors from these traps: SE only after full rollout; BA performance measures vs solution measures; measures not validated with stakeholders.
Log to scores.csv with ka=`SE` and topic=`8.1`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. SE works on solutions in any state.
2. 8.1: define, validate, collect measures.
3. Measures must tie to business objectives.

**Reading before the next session:**
- BABOK 8.0–8.1 (pp.163–169)
- Lessing ch.11 pp.276–286
- Jonasson ch.9 (pp.221–231)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- SE task chain outputs? :: Solution Performance Measures → Solution Performance Analysis → Solution Limitation / Enterprise Limitation → Recommended Actions
- 8.1 elements? :: Define Solution Performance Measures; Validate Performance Measures; Collect Performance Measures

ACTION: Update [progress.json](progress/progress.json): add this lesson (`7.1`) to `completed` with today's date and minutes ≈ 80, set `current` to `7.2`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 7.2: 8.2 Analyze Performance Measures. Trends, variances and accuracy in the pilot data.

STOP: Ready for 7.2? Type `/next` (or `/start 7.2`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/60-solution-performance-measures.md created
- [ ] Drill logged; task card added
