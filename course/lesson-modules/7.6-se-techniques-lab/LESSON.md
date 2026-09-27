# Lesson 7.6: SE techniques lab: metrics & KPIs, data mining, vendor assessment, root cause

*Module 7 · Week 9 · ~60 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Metrics and Key Performance Indicators (KPIs)](CBAP%20Knowledge%20Graph/05%20Techniques/Metrics%20and%20Key%20Performance%20Indicators%20%28KPIs%29.md)
- [Data Mining](CBAP%20Knowledge%20Graph/05%20Techniques/Data%20Mining.md)
- [Vendor Assessment](CBAP%20Knowledge%20Graph/05%20Techniques/Vendor%20Assessment.md)
- [Root Cause Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Root%20Cause%20Analysis.md)
- [Survey or Questionnaire](CBAP%20Knowledge%20Graph/05%20Techniques/Survey%20or%20Questionnaire.md)

---

SE questions often hinge on *measurement* techniques. Today: metrics and KPIs (indicator vs metric vs KPI), data mining (descriptive, diagnostic, predictive), vendor assessment, and root cause analysis revisited.

By the end of this session you will be able to:
- Distinguish indicator, metric, KPI
- Know data mining types
- Know vendor assessment criteria

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Measurement toolkit

ACTION: Re-read [Metrics and Key Performance Indicators (KPIs)](CBAP%20Knowledge%20Graph/05%20Techniques/Metrics%20and%20Key%20Performance%20Indicators%20%28KPIs%29.md), [Data Mining](CBAP%20Knowledge%20Graph/05%20Techniques/Data%20Mining.md), [Vendor Assessment](CBAP%20Knowledge%20Graph/05%20Techniques/Vendor%20Assessment.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Indicator: a specific numerical measure of progress. Metric: a quantifiable level of an indicator, e.g. a target. KPI: an indicator of progress towards a strategic goal. Good indicators are clear, relevant, economical, adequate and quantifiable. Consider the data source, collection method and reporting.
- Data mining: descriptive (patterns, clustering), diagnostic (why: decision trees, association), predictive (forecast). Supports decision making; needs quality data.
- Vendor assessment: knowledge and expertise, licensing and pricing models, product or vendor market position, terms and conditions, experience, reputation and stability.
- Root cause analysis: fishbone (Ishikawa) categories, five whys.

STOP: Is "ready within 2 hours ≥ 95%" an indicator, a metric, or a KPI?

USER: The indicator is "% ready within 2h"; ≥95% is the target metric; it is a KPI if tied to the strategic goal

ACTION: Give feedback. A strong answer includes: indicator = % ready in 2h; metric/target = 95%; it is a KPI because it measures progress towards the convenience goal.

---

## Apply it at GreenBasket: Five whys on Hillcrest

Quick root cause practice.

ACTION: Open and skim [14-pilot-results](case-files/14-pilot-results.md), [16-store-staff-survey](case-files/16-store-staff-survey.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Run a five-whys on "Hillcrest order accuracy fell from 90.2% to 86.4%".

USER: Drafts their analysis in the chat

ACTION: Coach it (why → OOS at pick up → aisle data stale → no update after the reset → no procedure or owner → head office never assigned aisle-data ownership) and save. Save the result to `workspace/65-five-whys-hillcrest.md` and link it: [65-five-whys-hillcrest.md](workspace/65-five-whys-hillcrest.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: metrics/indicators/KPIs, data mining types, vendor assessment criteria, root cause analysis, surveys for measurement.
Build distractors from these traps: metric vs indicator; predictive vs diagnostic mining; vendor assessment only price.
Log to scores.csv with ka=`TECH` and topic=`se-techniques`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Indicator ≠ metric ≠ KPI.
2. Data mining: descriptive, diagnostic, predictive.
3. Vendor assessment looks well beyond price.

**Reading before the next session:**
- BABOK 10.14, 10.28, 10.40, 10.49

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Indicator vs metric vs KPI? :: Indicator = numerical measure of progress; metric = quantifiable level/target; KPI = indicator tied to a strategic goal
- Data mining types? :: Descriptive, diagnostic, predictive

ACTION: Update [progress.json](progress/progress.json): add this lesson (`7.6`) to `completed` with today's date and minutes ≈ 60, set `current` to `7.7`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 7.7: SE exam drill + Phase 2 milestone. Finish Phase 2: all 30 tasks done.

STOP: Ready for 7.7? Type `/next` (or `/start 7.7`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/65-five-whys-hillcrest.md created
- [ ] Drill logged
