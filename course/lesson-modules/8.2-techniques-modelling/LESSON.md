# Lesson 8.2: Technique families II: modelling techniques

*Module 8 · Week 10 · ~80 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Process Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Process%20Modelling.md)
- [Use Cases and Scenarios](CBAP%20Knowledge%20Graph/05%20Techniques/Use%20Cases%20and%20Scenarios.md)
- [User Stories](CBAP%20Knowledge%20Graph/05%20Techniques/User%20Stories.md)
- [Sequence Diagrams](CBAP%20Knowledge%20Graph/05%20Techniques/Sequence%20Diagrams.md)
- [State Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/State%20Modelling.md)
- [Data Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Data%20Modelling.md)
- [Data Flow Diagrams](CBAP%20Knowledge%20Graph/05%20Techniques/Data%20Flow%20Diagrams.md)
- [Concept Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Concept%20Modelling.md)
- [Decision Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Decision%20Modelling.md)
- [Scope Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Scope%20Modelling.md)
- [Organizational Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Organizational%20Modelling.md)
- [Roles and Permissions Matrix](CBAP%20Knowledge%20Graph/05%20Techniques/Roles%20and%20Permissions%20Matrix.md)
- [Functional Decomposition](CBAP%20Knowledge%20Graph/05%20Techniques/Functional%20Decomposition.md)
- [Prototyping](CBAP%20Knowledge%20Graph/05%20Techniques/Prototyping.md)
- [Mind Mapping](CBAP%20Knowledge%20Graph/05%20Techniques/Mind%20Mapping.md)

---

Fifteen modelling techniques, five categories. Today: the fastest way to tell them apart, "what does this model *show*?".

By the end of this session you will be able to:
- Map each modelling technique to its category and what it shows
- Pick the right model for a question stem

STOP: Ready to dive in?

USER: Ready

---

## Part 1: What does it show?

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Process = sequence of activities; use case = actor-goal interaction with the system; user story = small valuable need; sequence = messages between objects over time; state = entity life cycle; data model = entities and relationships; DFD = data movement and transformation; concept model = business vocabulary; decision model = repeatable decision logic; scope model = boundaries; org model = structure and reporting; roles and permissions = who may do what; functional decomposition = breakdown of parts; prototype = early representation; mind map = non-linear idea structure.
- Categories: People & Roles, Rationale, Activity Flow, Capability, Data & Information.

STOP: Which model shows how the "Order" changes status from Placed to Collected?

USER: State model

ACTION: Give feedback. A strong answer includes: state model (Data & Information category).

---

## Apply it at GreenBasket: Master technique sheet, part 2

Add the modelling techniques.

ACTION: Open and skim [Technique-Task Matrix](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Technique-Task%20Matrix.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: For the 15 modelling techniques: what it shows, model category, and a typical exam cue.

USER: Drafts their analysis in the chat

ACTION: Check and append to the master sheet. Save the result to `workspace/70-master-technique-sheet.md` and link it: [70-master-technique-sheet.md](workspace/70-master-technique-sheet.md).

---

## Exam drill

QUIZ: 12 CBAP-style questions on: choosing the right model; model categories; distinguishing look-alike models.
Log to scores.csv with ka=`TECH` and topic=`tech-family-models`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Ask "what does it show?" to pick the model.
2. Know each model's category.

**Reading before the next session:**
- Lessing ch.14 (pp.397–441): skim

ACTION: Update [progress.json](progress/progress.json): add this lesson (`8.2`) to `completed` with today's date and minutes ≈ 80, set `current` to `8.3`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 8.3: Technique families III: analysis, decision & estimation techniques. Decision analysis, risk, financial, prioritization, estimation, business rules, NFR, interface, acceptance criteria, item tracking, backlog, glossary, data dictionary.

STOP: Ready for 8.3? Type `/next` (or `/start 8.3`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Master sheet part 2 appended
- [ ] Drill logged
