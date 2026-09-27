# Lesson 6.7: 7.4 Define Requirements Architecture

*Module 6 · Week 8 · ~75 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Define Requirements Architecture](CBAP%20Knowledge%20Graph/03%20Tasks/Define%20Requirements%20Architecture.md)
- [Requirements Architecture](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20Architecture.md)
- [Information Management Approach](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Information%20Management%20Approach.md)

---

You now have process models, data models, user stories, rules and NFRs. Do they fit together, with no gaps and no contradictions? **7.4 Define Requirements Architecture**.

By the end of this session you will be able to:
- Know the 5 elements of 7.4
- Explain viewpoints vs views
- Check completeness across views

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Define Requirements Architecture

ACTION: Re-read [Define Requirements Architecture](CBAP%20Knowledge%20Graph/03%20Tasks/Define%20Requirements%20Architecture.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Make sure the requirements fit together as a coherent, complete whole that achieves the objectives.
- Elements: Requirements Viewpoints and Views, Template Architectures, Completeness, Relate and Verify Requirements Relationships, Business Analysis Information Architecture.
- Viewpoint = the conventions for a type of view (model types, notation, stakeholders served). View = an actual set of requirements and models seen from that viewpoint (e.g. "pick process view").
- Relationships to verify: defined, necessary, correct, unambiguous, consistent.
- Inputs: Information Management Approach, Requirements (any state), Solution Scope. Output: Requirements Architecture, a guideline for 5.3, 5.4, 7.1 and an input to 7.5.

STOP: Is "BPMN process models for store staff" a viewpoint or a view? And "the Riverton picking process model"?

USER: Viewpoint; view

ACTION: Give feedback. A strong answer includes: viewpoint (convention and template); view (a specific instance).

**Exam trap to call out:** 7.4 (how requirements fit together) vs 3.4 (how information is stored and managed).

---

## Apply it at GreenBasket: Requirements architecture for release 1

Show how the pieces fit together, and find the gaps.

ACTION: Open and skim [50-model-plan](workspace/50-model-plan.md), [51-pick-handover-models](workspace/51-pick-handover-models.md), [52-data-models](workspace/52-data-models.md), [54-validation-matrix](workspace/54-validation-matrix.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Define 4 viewpoints (e.g. customer journey, store operations, data/integration, compliance), map existing views to them, and run a completeness check: what is missing (e.g. NFRs, customer service, refunds, reporting)? Any conflicts across views?

USER: Drafts their analysis in the chat

ACTION: Coach and save with a Mermaid diagram of viewpoints → views → requirements, plus a gap list. Save the result to `workspace/55-requirements-architecture.md` and link it: [55-requirements-architecture.md](workspace/55-requirements-architecture.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 7.4 elements, viewpoints vs views, template architectures, completeness, relationship verification, 3.4 vs 7.4.
Build distractors from these traps: viewpoint vs view; 3.4 vs 7.4; Requirements Architecture as input to Approve.
Log to scores.csv with ka=`RADD` and topic=`7.4`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Viewpoint = convention; view = instance.
2. Architecture ensures requirements collectively achieve the objectives (completeness, consistency).

**Reading before the next session:**
- BABOK 7.4 (pp.148–151)
- Lessing pp.250–254
- Jonasson 8.3.4 (pp.202–214)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Viewpoint vs view? :: Viewpoint = conventions/templates for a type of view; view = an actual set of requirements seen through a viewpoint
- 7.4 elements? :: Viewpoints & Views; Template Architectures; Completeness; Relate & Verify Relationships; BA Information Architecture

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.7`) to `completed` with today's date and minutes ≈ 75, set `current` to `6.8`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.8: 7.5 Define Design Options. Build, buy or hybrid? Allocate requirements to components.

STOP: Ready for 6.8? Type `/next` (or `/start 6.8`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/55-requirements-architecture.md created
- [ ] Drill logged; task card added
