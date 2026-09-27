# Lesson 6.11: RADD techniques lab II: decision modelling, roles & permissions, functional decomposition, scope models

*Module 6 · Week 8 · ~75 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Decision Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Decision%20Modelling.md)
- [Roles and Permissions Matrix](CBAP%20Knowledge%20Graph/05%20Techniques/Roles%20and%20Permissions%20Matrix.md)
- [Functional Decomposition](CBAP%20Knowledge%20Graph/05%20Techniques/Functional%20Decomposition.md)
- [Scope Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Scope%20Modelling.md)
- [Organizational Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Organizational%20Modelling.md)

---

Alcohol handover is a repeatable decision with rules. Store roles need clear permissions. The whole solution needs decomposing. Today: **decision modelling, roles and permissions, functional decomposition, scope modelling**.

By the end of this session you will be able to:
- Build a decision table
- Build a roles and permissions matrix
- Decompose the solution functionally
- Recap scope models

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Four structure techniques

ACTION: Re-read [Decision Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Decision%20Modelling.md), [Roles and Permissions Matrix](CBAP%20Knowledge%20Graph/05%20Techniques/Roles%20and%20Permissions%20Matrix.md), [Functional Decomposition](CBAP%20Knowledge%20Graph/05%20Techniques/Functional%20Decomposition.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Decision modelling: decision tables and trees, DMN; separates repeatable business decisions (and their rules) from process flow.
- Roles and permissions matrix: roles × activities, with authority levels; supports segregation of duties and security.
- Functional decomposition: break outcomes, functions, processes or products into smaller parts until they are manageable. Beware inconsistent decomposition levels.
- Scope models: context diagrams, use case diagrams, feature lists; show in/out of scope and boundaries.

STOP: Alcohol handover: which inputs would a decision table use?

USER: Store sells alcohol, State C time window, staff age ≥18, ID verified…

ACTION: Give feedback. A strong answer includes: conditions: order contains alcohol; staff member aged 18 or over; valid photo ID; State C and time 23:00–07:00; outcome: hand over / refuse and log.

---

## Apply it at GreenBasket: Alcohol handover decision + role permissions

Turn compliance rules into models the vendor can build.

ACTION: Open and skim [08-compliance-memo](case-files/08-compliance-memo.md), [14-pilot-results](case-files/14-pilot-results.md), [35-substitution-decision-and-rules](workspace/35-substitution-decision-and-rules.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Build (1) a decision table for alcohol handover, (2) a roles and permissions matrix (picker, desk associate, store manager, service desk, customer) × activities (pick, substitute, hand over alcohol, refund, override slot, view customer data), and (3) a functional decomposition of Click & Collect, two levels deep.

USER: Drafts their analysis in the chat

ACTION: Coach and save all three. Save the result to `workspace/59-decision-permissions-decomposition.md` and link it: [59-decision-permissions-decomposition.md](workspace/59-decision-permissions-decomposition.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: decision modelling vs business rules analysis vs decision analysis, roles and permissions matrix, functional decomposition, scope modelling.
Build distractors from these traps: decision modelling vs decision analysis; functional decomposition = process model; scope model shows detailed flow.
Log to scores.csv with ka=`TECH` and topic=`radd-techniques-2`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Decision modelling = repeatable decisions; decision analysis = choosing among options under uncertainty.
2. Roles and permissions support security and segregation of duties.

**Reading before the next session:**
- BABOK 10.17, 10.22, 10.39, 10.41

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Decision modelling vs decision analysis? :: Modelling = how repeatable business decisions are made (tables/trees/DMN); analysis = evaluating alternatives for one decision under uncertainty

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.11`) to `completed` with today's date and minutes ≈ 75, set `current` to `6.12`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.12: RADD final drill (40 questions). Close out the biggest KA.

STOP: Ready for 6.12? Type `/next` (or `/start 6.12`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/59-decision-permissions-decomposition.md created
- [ ] Drill logged
