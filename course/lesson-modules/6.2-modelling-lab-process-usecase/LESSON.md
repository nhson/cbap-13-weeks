# Lesson 6.2: 7.1 Specify & Model II: process models, use cases, user stories

*Module 6 · Week 7 · ~90 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Process Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Process%20Modelling.md)
- [Use Cases and Scenarios](CBAP%20Knowledge%20Graph/05%20Techniques/Use%20Cases%20and%20Scenarios.md)
- [User Stories](CBAP%20Knowledge%20Graph/05%20Techniques/User%20Stories.md)
- [Acceptance and Evaluation Criteria](CBAP%20Knowledge%20Graph/05%20Techniques/Acceptance%20and%20Evaluation%20Criteria.md)
- [Sequence Diagrams](CBAP%20Knowledge%20Graph/05%20Techniques/Sequence%20Diagrams.md)

---

Kim and Rosa gave you the real picking flow. Today you model it three ways: a **process model**, a **use case**, and **user stories with acceptance criteria**. The exam checks when each is the right choice.

By the end of this session you will be able to:
- Draw a process model with the right elements
- Write a use case with main, alternative and exception flows
- Write INVEST user stories with acceptance criteria

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Three views of behaviour

ACTION: Re-read [Process Modelling](CBAP%20Knowledge%20Graph/05%20Techniques/Process%20Modelling.md), [Use Cases and Scenarios](CBAP%20Knowledge%20Graph/05%20Techniques/Use%20Cases%20and%20Scenarios.md), [User Stories](CBAP%20Knowledge%20Graph/05%20Techniques/User%20Stories.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Process models: activities, events, directional flow, decision points, links, roles (swimlanes). Notations: flowcharts, activity diagrams, BPMN, value stream maps.
- Use cases: actor, goal, preconditions, trigger, main success flow, alternative and exception flows, post-conditions (guarantees). Scenario = one path through a use case.
- User stories: "As a <role>, I want <goal>, so that <benefit>", plus acceptance criteria; INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable); the 3 Cs (Card, Conversation, Confirmation).
- Sequence diagrams show interactions between objects or actors over time (lifelines, messages).

STOP: Customer arrives at the store and the order isn't ready. Main flow, alternative flow, or exception flow of "Collect Order"?

USER: Alternative or exception depending on definition. Most treat it as an exception.

ACTION: Give feedback. A strong answer includes: an exception flow when the goal cannot be completed as planned (or an alternative if the goal is still met another way, e.g. wait under 5 minutes). The key is that both are documented separately from the main success scenario.

---

## Apply it at GreenBasket: Model "Pick & Hand Over Order"

Use the confirmed elicitation results.

ACTION: Open and skim [22-elicitation-results-confirmed](workspace/22-elicitation-results-confirmed.md), [35-substitution-decision-and-rules](workspace/35-substitution-decision-and-rules.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Produce: (1) a swimlane process from order released → picked (by temperature zone) → staged → customer arrives → ID check (alcohol) → handover; (2) a use case "Collect Order" with main, 2 alternative and 2 exception flows; (3) 3 user stories with Given/When/Then acceptance criteria (substitution preference, arrival notification, alcohol handover).

USER: Drafts their analysis in the chat

ACTION: Coach it, then save all three. Draw the process in Mermaid (flowchart with subgraphs as lanes). Save the result to `workspace/51-pick-handover-models.md` and link it: [51-pick-handover-models.md](workspace/51-pick-handover-models.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `priyanka-qa`, giving it the path `workspace/51-pick-handover-models.md` and review the acceptance criteria for testability. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: process modelling elements and notations, use case structure, user story format and INVEST, acceptance criteria, sequence diagrams: which to use when.
Build distractors from these traps: use case = user story; process model shows data transformation (that is DFD); acceptance criteria vs evaluation criteria; sequence diagram vs state diagram.
Log to scores.csv with ka=`TECH` and topic=`behaviour-models`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Process model = flow of activities; use case = actor-goal interaction; user story = small valuable slice.
2. Acceptance criteria make stories testable.

**Reading before the next session:**
- BABOK 10.35, 10.42, 10.47, 10.48
- Jonasson 8.3.1.1 and 8.3.1.4 (pp.173–197)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- INVEST? :: Independent, Negotiable, Valuable, Estimable, Small, Testable
- Use case components? :: Actor, goal, preconditions, trigger, main flow, alternative/exception flows, post-conditions

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.2`) to `completed` with today's date and minutes ≈ 90, set `current` to `6.3`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.3: 7.1 Specify & Model III: data & information models. Data model, data dictionary, glossary, DFD, concept and state models.

STOP: Ready for 6.3? Type `/next` (or `/start 6.3`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/51-pick-handover-models.md created and QA-reviewed
- [ ] Drill logged
