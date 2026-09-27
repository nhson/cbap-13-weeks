# Lesson 1.2: The BACCM: six lenses on every change

*Module 1 · Week 1 · ~75 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [BACCM](CBAP%20Knowledge%20Graph/01%20Foundations/BACCM.md)
- [Change](CBAP%20Knowledge%20Graph/01%20Foundations/Core%20Concepts/Change.md)
- [Need](CBAP%20Knowledge%20Graph/01%20Foundations/Core%20Concepts/Need.md)
- [Solution](CBAP%20Knowledge%20Graph/01%20Foundations/Core%20Concepts/Solution.md)
- [Stakeholder](CBAP%20Knowledge%20Graph/01%20Foundations/Core%20Concepts/Stakeholder.md)
- [Value](CBAP%20Knowledge%20Graph/01%20Foundations/Core%20Concepts/Value.md)
- [Context](CBAP%20Knowledge%20Graph/01%20Foundations/Core%20Concepts/Context.md)
- [Key Terms](CBAP%20Knowledge%20Graph/01%20Foundations/Key%20Terms.md)

---

Every BABOK task, technique and exam scenario can be read through six words: **Change, Need, Solution, Stakeholder, Value, Context**. That's the Business Analysis Core Concept Model (BACCM).

If you can hold those six in your head, you can dissect any case study question in seconds.

By the end of this session you will be able to:
- Define all six core concepts in BABOK terms
- Explain why no concept is more important than another
- Apply the BACCM to a real situation
- Use the key terms (business analysis, BA information, design, enterprise, organization, plan, requirement, risk)

STOP: Ready to dive in?

USER: Ready

---

## Part 1: The six concepts

ACTION: Re-read [BACCM](CBAP%20Knowledge%20Graph/01%20Foundations/BACCM.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Change: a transformation made in response to a need. Need: a problem to solve or an opportunity to pursue. Solution: a particular way of meeting one or more needs within a context.
- Stakeholder: anyone (individual or group) connected to the change, the need or the solution. Value: how much something is worth, or how important or useful it is, to a stakeholder in a given context. Context: the surrounding circumstances that shape the change, are shaped by it, and help explain it.
- All six are **equal**, and each is defined by the others. If one changes, re-evaluate the rest.
- Value can be tangible or intangible, potential or realized, and absolute or relative. Losses, risks and costs are negative value.
- Questions to ask: what kinds of changes? what needs? what solutions? who are the stakeholders? what do they value? what contexts?

STOP: Without looking: which core concept means "how much something is worth or matters to a stakeholder in a given context", and which one means "a problem to solve or an opportunity to pursue"?

USER: Value; Need

ACTION: Give feedback. A strong answer includes: exact matches. Note "within a context": value is always relative to a stakeholder and a context.

**Exam trap to call out:** Distractors often claim one concept (usually Value or Need) is "the most important". The BABOK says they are all equal.

---

## Part 2: Key terms that the exam uses precisely

ACTION: Re-read [Key Terms](CBAP%20Knowledge%20Graph/01%20Foundations/Key%20Terms.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Business analysis: the practice of making change happen in an enterprise by clarifying needs and proposing solutions that create value for stakeholders.
- Requirement = a usable representation of a **need**. Design = a usable representation of a **solution**.
- Business analysis information = any information, at any level of detail, used as input to or output of BA work. That is why the BABOK says "information", not just "requirements".
- Enterprise ≠ organization. An enterprise is one or more organizations plus the solutions they use, bounded around the change rather than around a legal entity.
- Risk = the effect of uncertainty on the value of a change, a solution, or the enterprise.

STOP: Is "a screen mock-up of the pickup check-in page" a requirement or a design? And "customers must be able to tell the store they have arrived"?

USER: Mock-up = design; tell store they arrived = requirement

ACTION: Give feedback. A strong answer includes: the mock-up represents a solution (design); the arrival need is a requirement (it represents a need).

---

## Apply it at GreenBasket: BACCM analysis of the Click & Collect initiative

Elena wants a one-page view of the initiative. Use the BACCM as your structure.

ACTION: Open and skim [01-sponsor-kickoff-email](case-files/01-sponsor-kickoff-email.md), [04-customer-feedback-q2](case-files/04-customer-feedback-q2.md), [05-market-and-sales-data](case-files/05-market-and-sales-data.csv), [02-harvest-postmortem](case-files/02-harvest-postmortem.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Draft a BACCM table for Click & Collect: one or two lines per concept (Change, Need, Solution, Stakeholder, Value, Context). Try it yourself first. Rough is fine.

USER: Drafts their analysis in the chat

ACTION: Give specific feedback per concept, then write the polished table plus 3 "questions the BACCM raised" (e.g. whose value? which context constraints?). Save the result to `workspace/01-baccm-click-and-collect.md` and link it: [01-baccm-click-and-collect.md](workspace/01-baccm-click-and-collect.md).

A model answer should cover (use it to coach, don't just paste it):
- Change: introduce online ordering with in-store pickup; transform store operations to support picking
- Need: stop share loss (18.2→14.1%) and visit-frequency decline (−11%) caused by a convenience gap
- Solution: Click & Collect capability (app/web ordering, picking, staging, handover), not yet a specific vendor
- Stakeholders: customers (personas), store ops, pickers, sponsor, CFO, IT, compliance, union, vendors
- Value: tangible (5% online share, basket retention) and intangible (reputation, convenience); negative value = cost, store burden, risk
- Context: Harvest failure, 82% inventory accuracy, union rules, alcohol and cold-chain regulation, competitor moves

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `elena-sponsor`, giving it the path `workspace/01-baccm-click-and-collect.md` and ask for a sponsor reaction to the BACCM one-pager. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

**Discovery:** The BACCM exposed that the "solution" in Elena's email (ShelfWise) was chosen before the context (inventory accuracy, union) was understood. That is exactly what killed Harvest.

---

## Exam drill

QUIZ: 8 CBAP-style questions on: BACCM definitions and application, key terms (requirement vs design, enterprise vs organization, BA information, risk).
Mix: 5 scenario, 3 definition.
Build distractors from these traps: claiming one core concept is most important; confusing need with solution; confusing enterprise with organization; value only tangible.
Log to scores.csv with ka=`FND` and topic=`baccm`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Six equal core concepts: Change, Need, Solution, Stakeholder, Value, Context.
2. Requirement ↔ need; design ↔ solution.
3. Value is always *to a stakeholder, within a context*, and can be negative.

> **Exam rule of thumb:** If an answer option says one core concept matters more than the others, it is wrong.

**Reading before the next session:**
- BABOK ch.1 (pp.1–10) and 2.1–2.2 (pp.12–16)
- Lessing ch.5, pp.46–55

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- BACCM six concepts? :: Change, Need, Solution, Stakeholder, Value, Context
- Requirement vs design? :: Requirement = usable representation of a need; design = usable representation of a solution
- Define risk (BABOK) :: The effect of uncertainty on the value of a change, a solution, or the enterprise

ACTION: Update [progress.json](progress/progress.json): add this lesson (`1.2`) to `completed` with today's date and minutes ≈ 75, set `current` to `1.3`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 1.3: Requirements classification & requirements vs designs. Business, stakeholder, solution (functional and non-functional), and transition requirements.

STOP: Ready for 1.3? Type `/next` (or `/start 1.3`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student can define all six concepts
- [ ] Student can classify a statement as requirement vs design
- [ ] workspace/01-baccm-click-and-collect.md created and reviewed by the sponsor agent
- [ ] Drill completed and logged
