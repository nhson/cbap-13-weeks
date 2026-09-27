# Lesson 6.10: RADD techniques lab I: NFRs, acceptance criteria, prototyping, interface analysis

*Module 6 · Week 8 · ~75 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Non-Functional Requirements Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Non-Functional%20Requirements%20Analysis.md)
- [Acceptance and Evaluation Criteria](CBAP%20Knowledge%20Graph/05%20Techniques/Acceptance%20and%20Evaluation%20Criteria.md)
- [Prototyping](CBAP%20Knowledge%20Graph/05%20Techniques/Prototyping.md)
- [Interface Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Interface%20Analysis.md)

---

Harvest never defined how fast, how available or how secure. Today: **NFR analysis**, **acceptance vs evaluation criteria**, **prototyping** and **interface analysis**.

By the end of this session you will be able to:
- Write measurable NFRs with context
- Distinguish acceptance and evaluation criteria
- Choose a prototype type
- List the interfaces

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Qualities and interfaces

ACTION: Re-read [Non-Functional Requirements Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Non-Functional%20Requirements%20Analysis.md), [Interface Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Interface%20Analysis.md), [Acceptance and Evaluation Criteria](CBAP%20Knowledge%20Graph/05%20Techniques/Acceptance%20and%20Evaluation%20Criteria.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- NFR categories: availability, compatibility, functionality, maintainability, performance efficiency, portability, reliability, scalability, security, usability, certification, compliance, localization, service level agreements, extensibility. Each needs measures and context.
- Acceptance criteria: minimum conditions to accept ONE solution (pass/fail). Evaluation criteria: measures used to rank SEVERAL options.
- Prototypes: throw-away vs evolutionary/functional; purposes: proof of principle/concept, form study, usability, visual, functional. Types: storyboards, wireframes, mock-ups, simulations.
- Interface analysis: user, system and business interfaces. Identify each one, then pin down what crosses it, how, when, and who owns it.

STOP: Rewrite R-18 "99.9% availability" as a proper NFR.

USER: Measurable with context

ACTION: Give feedback. A strong answer includes: e.g. "Customer ordering is available 99.9% of the time 6:00–23:00 local time, measured monthly, excluding announced maintenance under 2 h/month".

---

## Apply it at GreenBasket: NFR set + interface list

Complete the non-functional and interface requirements for release 1.

ACTION: Open and skim [07-it-landscape](case-files/07-it-landscape.md), [08-compliance-memo](case-files/08-compliance-memo.md), [55-requirements-architecture](workspace/55-requirements-architecture.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Write 6 measurable NFRs (performance, availability, security/PCI, accessibility, scalability, usability for pickers) and an interface list (StockPoint, TillMaster, Basket Rewards, PayRail, RosterPro, handhelds) with what is exchanged, frequency and owner.

USER: Drafts their analysis in the chat

ACTION: Coach and save. Save the result to `workspace/58-nfrs-and-interfaces.md` and link it: [58-nfrs-and-interfaces.md](workspace/58-nfrs-and-interfaces.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `anil-architect`, giving it the path `workspace/58-nfrs-and-interfaces.md`. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: NFR analysis, acceptance vs evaluation criteria, prototyping types and purposes, interface analysis.
Build distractors from these traps: acceptance vs evaluation; NFR without measure; throw-away vs evolutionary; interface analysis only system-to-system.
Log to scores.csv with ka=`TECH` and topic=`radd-techniques-1`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. NFRs need measures and context.
2. Acceptance = one solution, pass/fail; evaluation = rank several.
3. Interfaces: user, system, business.

**Reading before the next session:**
- BABOK 10.1, 10.24, 10.30, 10.36

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Acceptance vs evaluation criteria? :: Acceptance = minimum conditions to accept one solution (pass/fail); evaluation = measures to compare/rank options

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.10`) to `completed` with today's date and minutes ≈ 75, set `current` to `6.11`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.11: RADD techniques lab II: decision modelling, roles & permissions, functional decomposition, scope models. Decision tables, access rights and decomposition.

STOP: Ready for 6.11? Type `/next` (or `/start 6.11`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/58-nfrs-and-interfaces.md created
- [ ] Drill logged
