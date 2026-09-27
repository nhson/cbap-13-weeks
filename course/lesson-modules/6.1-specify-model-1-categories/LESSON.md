# Lesson 6.1: RADD overview + 7.1 Specify & Model I: model categories and abstraction

*Module 6 · Week 7 · ~85 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [Requirements Analysis and Design Definition](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Requirements%20Analysis%20and%20Design%20Definition.md)
- [Specify and Model Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Specify%20and%20Model%20Requirements.md)
- [Requirements (specified and modelled)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20%28specified%20and%20modelled%29.md)
- [Elicitation Results (any state)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Elicitation%20Results%20%28any%20state%29.md)

---

Welcome to RADD: **30% of the exam**, about 36 questions. For two weeks you'll turn GreenBasket's confirmed findings into modelled, verified, validated requirements, then recommend a vendor. First: **7.1 Specify and Model Requirements**, and the five model categories the exam loves.

By the end of this session you will be able to:
- Explain RADD's 6 tasks and their flow
- Know the 4 elements of 7.1
- Classify models into the 5 categories
- Choose the level of abstraction per audience

STOP: Ready to dive in?

USER: Ready

---

## Part 1: RADD at a glance

ACTION: Re-read [Requirements Analysis and Design Definition](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Requirements%20Analysis%20and%20Design%20Definition.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Six tasks: 7.1 Specify and Model → 7.2 Verify → 7.3 Validate → 7.4 Define Requirements Architecture → 7.5 Define Design Options → 7.6 Analyze Potential Value and Recommend Solution.
- RADD bridges strategy (SA outputs as guidelines) and delivery. It applies to requirements *and designs*.
- States: specified and modelled → verified / validated → (RLCM) prioritized, approved. 7.5 needs validated, prioritized requirements.

STOP: Which RADD output becomes the input to Approve Requirements (5.5)?

USER: Requirements (verified) from 7.2

ACTION: Give feedback. A strong answer includes: Requirements (verified), from 7.2.

---

## Part 2: Specify and Model Requirements

ACTION: Re-read [Specify and Model Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Specify%20and%20Model%20Requirements.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Turn elicitation results into structured, modelled requirements and designs at the right level of detail.
- Elements: Model Requirements, Analyze Requirements (decomposition, expansion, contraction; identify gaps), Represent Requirements and Attributes, Implement the Appropriate Levels of Abstraction.
- Model categories: **People and Roles** (org models, roles and permissions matrix, stakeholder maps/personas); **Rationale** (decision models, scope models, business model canvas, root cause, business rules); **Activity Flow** (process models, use cases and scenarios, user stories); **Capability** (business capability analysis, functional decomposition, prototypes); **Data and Information** (data dictionary, data flow diagrams, data models, glossary, state models, interface analysis).
- Models can be matrices (tables) or diagrams.
- Input: Elicitation Results (any state). 24 techniques. Output: Requirements (specified and modelled).

STOP: Classify: process model, data dictionary, decision model, roles and permissions matrix, functional decomposition.

USER: Activity flow; data & information; rationale; people & roles; capability

ACTION: Give feedback. A strong answer includes: process = activity flow; data dictionary = data and information; decision model = rationale; roles and permissions = people and roles; functional decomposition = capability.

**Exam trap to call out:** State models sit in the *Data and Information* category (entity life cycles), not Activity Flow.

---

## Apply it at GreenBasket: Model plan for Click & Collect

Decide which models you need, for whom, and at which level of abstraction.

ACTION: Open and skim [22-elicitation-results-confirmed](workspace/22-elicitation-results-confirmed.md), [43-change-strategy-and-solution-scope](workspace/43-change-strategy-and-solution-scope.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: List 8 models you'd create for release 1, tag each with its category, audience and level of abstraction (e.g. a context diagram for Elena; a pick process model for stores; a data model for vendors). Which category do you have too few of?

USER: Drafts their analysis in the chat

ACTION: Coach and save a model plan table. Make sure all 5 categories are covered. Save the result to `workspace/50-model-plan.md` and link it: [50-model-plan.md](workspace/50-model-plan.md).

---

## Exam drill

QUIZ: 10 CBAP-style questions on: RADD overview, 7.1 elements, the 5 model categories, abstraction, input and output states.
Build distractors from these traps: state model in activity flow; Elicitation Results (confirmed) only as 7.1 input (it is any state); decision model vs process model category.
Log to scores.csv with ka=`RADD` and topic=`7.1a`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 7.1 elements: model, analyze, represent (with attributes), abstraction.
2. Five categories: People & Roles, Rationale, Activity Flow, Capability, Data & Information.
3. Input: Elicitation Results (any state).

**Reading before the next session:**
- BABOK 7.0–7.1 (pp.133–140)
- Lessing ch.10 pp.229–242
- Jonasson 8.1–8.3.1 intro (pp.169–173)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 5 model categories? :: People & Roles; Rationale; Activity Flow; Capability; Data & Information
- 7.1 elements? :: Model Requirements; Analyze Requirements; Represent Requirements & Attributes; Implement Appropriate Levels of Abstraction
- 7.1 input? :: Elicitation Results (any state)

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.1`) to `completed` with today's date and minutes ≈ 85, set `current` to `6.2`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.2: 7.1 Specify & Model II: process models, use cases, user stories. Model the pick-and-handover flow three ways.

STOP: Ready for 6.2? Type `/next` (or `/start 6.2`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/50-model-plan.md created
- [ ] Student classifies models by category
- [ ] Drill logged; task card added
