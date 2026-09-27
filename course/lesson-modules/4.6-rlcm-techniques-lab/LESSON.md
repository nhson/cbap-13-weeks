# Lesson 4.6: RLCM techniques lab: decision analysis, backlog management, business rules

*Module 4 · Week 5 · ~75 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Decision Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Decision%20Analysis.md)
- [Backlog Management](CBAP%20Knowledge%20Graph/05%20Techniques/Backlog%20Management.md)
- [Business Rules Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Business%20Rules%20Analysis.md)
- [Prioritization](CBAP%20Knowledge%20Graph/05%20Techniques/Prioritization.md)

---

Three techniques that show up in RLCM questions and far beyond: **decision analysis**, **backlog management** and **business rules analysis**.

By the end of this session you will be able to:
- Build a weighted decision matrix
- Explain how a backlog is managed
- Separate definitional and behavioural business rules

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Decision analysis and backlog management

ACTION: Re-read [Decision Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Decision%20Analysis.md), [Backlog Management](CBAP%20Knowledge%20Graph/05%20Techniques/Backlog%20Management.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Decision analysis: frame the problem, alternatives, criteria and weights, and uncertainty. Tools: decision matrices (weighted), decision trees (expected value = probability × outcome), pros and cons, trade-offs.
- Backlog management: items are prioritized; higher-priority items are elaborated in more detail; the backlog is refined continually; items leave it when implemented or removed.

STOP: Option A: a 60% chance of +$500k and a 40% chance of −$100k. What is the expected value?

USER: $260k

ACTION: Give feedback. A strong answer includes: 0.6×500 − 0.4×100 = 300 − 40 = $260k.

---

## Part 2: Business rules analysis

ACTION: Re-read [Business Rules Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Business%20Rules%20Analysis.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Definitional rules: shape concepts and knowledge; they can't be violated, only misapplied (e.g. "an order is *collectable* when all items are picked and staged").
- Behavioural rules: shape conduct; they can be violated, so a response is needed (e.g. "alcohol must not be handed to anyone without verified ID").
- Rules are separated from processes so they can change independently. Express them atomically, in business vocabulary, with a single owner.

STOP: Classify: "Staff under 18 must not hand over alcohol." Definitional or behavioural?

USER: Behavioural

ACTION: Give feedback. A strong answer includes: behavioural: it can be violated, so enforcement or response is needed (the pilot logged 2 attempts).

---

## Apply it at GreenBasket: Substitution policy decision + rulebook

Resolve the substitution debate with a decision matrix and capture the rules.

ACTION: Open and skim [10-workshop-notes-raw](case-files/10-workshop-notes-raw.md), [04-customer-feedback-q2](case-files/04-customer-feedback-q2.md), [06-competitor-benchmark](case-files/06-competitor-benchmark.md), [08-compliance-memo](case-files/08-compliance-memo.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Build a weighted decision matrix for substitution options (per-order allow/deny; per-item preference; per-item plus live chat) using 4–5 weighted criteria. Then write 6 business rules (substitutions and alcohol), each tagged definitional or behavioural.

USER: Drafts their analysis in the chat

ACTION: Coach it and check the weights sum to 100% and that rules are atomic. Save both. Save the result to `workspace/35-substitution-decision-and-rules.md` and link it: [35-substitution-decision-and-rules.md](workspace/35-substitution-decision-and-rules.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: decision analysis (matrices, expected value, trees), backlog management, business rules analysis (definitional vs behavioural), prioritization techniques.
Build distractors from these traps: definitional vs behavioural; business rules embedded in process models; backlog items all equally detailed; decision analysis vs decision modelling.
Log to scores.csv with ka=`TECH` and topic=`rlcm-techniques`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Decision matrices weight criteria; decision trees use expected value.
2. Backlog: prioritized, progressively elaborated, continually refined.
3. Definitional rules can't be violated; behavioural rules can.

**Reading before the next session:**
- BABOK 10.2, 10.9, 10.16

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Definitional vs behavioural rule? :: Definitional shapes knowledge (can't be violated); behavioural shapes conduct (can be violated)
- Expected value? :: Sum of (probability × outcome)

ACTION: Update [progress.json](progress/progress.json): add this lesson (`4.6`) to `completed` with today's date and minutes ≈ 75, set `current` to `4.7`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 4.7: RLCM exam drill (40 questions). Prove RLCM mastery.

STOP: Ready for 4.7? Type `/next` (or `/start 4.7`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/35-substitution-decision-and-rules.md created
- [ ] Drill logged
