# Lesson 6.3: 7.1 Specify & Model III: data & information models

*Module 6 · Week 7 · ~85 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Data Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Data%20Modelling.md)
- [Data Dictionary](CBAP%20Knowledge%20Graph/05%20Techniques/Data%20Dictionary.md)
- [Glossary](CBAP%20Knowledge%20Graph/05%20Techniques/Glossary.md)
- [Data Flow Diagrams](CBAP%20Knowledge%20Graph/05%20Techniques/Data%20Flow%20Diagrams.md)
- [Concept Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Concept%20Modelling.md)
- [State Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/State%20Modelling.md)

---

"Order", "substitution", "collectable", "staged": if stores, marketing and the vendor each define these differently, the pilot fails. Today: the **data and information** models.

By the end of this session you will be able to:
- Build a conceptual data model with cardinality
- Write data dictionary and glossary entries
- Draw a DFD and a state model
- Distinguish concept model / data model / glossary / data dictionary

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Data and information models

ACTION: Re-read [Data Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Data%20Modelling.md), [Data Flow Diagrams](CBAP%20Knowledge%20Graph/05%20Techniques/Data%20Flow%20Diagrams.md), [State Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/State%20Modelling.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Data models: conceptual, logical, physical. Entities, attributes, relationships, cardinality (e.g. one Order has many Order Lines). ERD or class diagram.
- Data dictionary: primitive elements (name, aliases, values/meanings, description) and composite elements (sequence, repetition, optional).
- Glossary: business terms and definitions. Concept model: business vocabulary (noun and verb concepts), independent of data design.
- DFD: external entities, processes, data stores, data flows. Levels: context (level 0), level 1, level 2. No direct flow between external entities or data stores.
- State model: entity life cycle as states, transitions and events.

STOP: Draw (in words) the states of an Order from placement to completion.

USER: e.g. Placed → Picking → Staged → Ready → Collected / Cancelled

ACTION: Give feedback. A strong answer includes: e.g. Placed → Picking → Picked → Staged → Ready for Collection → Collected; plus Cancelled and Partially Refused (alcohol ID failure) with the triggering events.

---

## Apply it at GreenBasket: Order data and life cycle

Define the data the vendor must support.

ACTION: Open and skim [07-it-landscape](case-files/07-it-landscape.md), [08-compliance-memo](case-files/08-compliance-memo.md), [51-pick-handover-models](workspace/51-pick-handover-models.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Produce: a conceptual data model (Customer, Order, Order Line, Product, Store, Pickup Slot, Substitution Preference, Tote, Temperature Log, ID Check), 5 glossary terms, 4 data dictionary entries (incl. one composite), a level-0 DFD, and an Order state model.

USER: Drafts their analysis in the chat

ACTION: Coach and save with Mermaid (erDiagram and stateDiagram). Note privacy constraints: no ID storage; retention 24 months. Save the result to `workspace/52-data-models.md` and link it: [52-data-models.md](workspace/52-data-models.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `anil-architect`, giving it the path `workspace/52-data-models.md` and check integration and data feasibility. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: data models, data dictionary (primitive/composite), glossary vs data dictionary, concept model, DFD rules and levels, state models.
Build distractors from these traps: glossary vs data dictionary; concept model vs data model; DFD shows sequence/decisions; direct flow between two data stores.
Log to scores.csv with ka=`TECH` and topic=`data-models`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Glossary = business terms; data dictionary = data elements.
2. DFD = data movement, not sequence.
3. State model = life cycle of one entity.

**Reading before the next session:**
- BABOK 10.11–10.15, 10.23, 10.44
- Jonasson 8.3.1.2–8.3.1.3 (pp.177–184)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- DFD components? :: External entities, processes, data stores, data flows
- Glossary vs data dictionary? :: Glossary defines business terms; data dictionary defines data elements (values, composition)

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.3`) to `completed` with today's date and minutes ≈ 85, set `current` to `6.4`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.4: 7.2 Verify Requirements. Tom's list, torn apart by quality characteristics.

STOP: Ready for 6.4? Type `/next` (or `/start 6.4`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/52-data-models.md created and architect-reviewed
- [ ] Drill logged
