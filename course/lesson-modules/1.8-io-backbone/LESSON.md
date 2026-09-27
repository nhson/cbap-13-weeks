# Lesson 1.8: The big map: how the 30 tasks hand off to each other

*Module 1 · Week 2 · ~90 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [BABOK Input-Output Flow](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/BABOK%20Input-Output%20Flow.md)
- [Requirements](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements.md)
- [Elicitation Results](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Elicitation%20Results.md)
- [Business Analysis Approach](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Business%20Analysis%20Approach.md)
- [Change Strategy](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Change%20Strategy.md)
- [Solution Scope](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Solution%20Scope.md)

---

Many exam questions are secretly asking: *"Which task produced this, and which task uses it next?"* Today you learn the backbone: the 38 formal handoffs between tasks and the "state" labels that travel with requirements.

By the end of this session you will be able to:
- Trace the main input/output chains across KAs
- Know the requirement and elicitation-result states
- Recognize the "hub" outputs that guide many tasks

STOP: Ready to dive in?

USER: Ready

---

## Part 1: The hub outputs

ACTION: Re-read [Business Analysis Approach](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Business%20Analysis%20Approach.md), [Change Strategy](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Change%20Strategy.md), [Solution Scope](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Solution%20Scope.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- BAPM outputs (Business Analysis Approach, Stakeholder Engagement Approach, Governance Approach, Information Management Approach, BA Performance Assessment) guide almost everything else.
- Strategy Analysis outputs (Current State Description, Future State Description, Business Objectives, Potential Value, Risk Analysis Results, Change Strategy, Solution Scope) guide RADD and SE.
- Needs enter from outside (3.1, 3.2, 4.1, 6.1). "(external)" inputs: Performance Objectives (3.5) and Implemented Solution (8.1, 8.3, 8.4).

STOP: Which task produces Solution Scope, and name two tasks that use it?

USER: 6.4 Define Change Strategy; e.g. 7.1, 7.3, 7.4, 7.5…

ACTION: Give feedback. A strong answer includes: produced by 6.4 Define Change Strategy (together with Change Strategy); used as input by 7.4 and as a guideline by many tasks (5.3, 5.4, 5.5, 7.1, 7.3, 7.5, 7.6, 8.x).

---

## Part 2: The state chains

ACTION: Re-read [Requirements](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements.md), [Elicitation Results](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Elicitation%20Results.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Elicitation Results: 4.2 → **unconfirmed**, 4.3 → **confirmed**, 7.1 accepts **any state**.
- Requirements: 7.1 → **specified and modelled** → 7.2 **verified** → 5.5 approves **verified** requirements. 7.3 → **validated**. 7.5 uses **validated, prioritized** requirements. 5.1 → traced, 5.2 → maintained, 5.3 → prioritized, 5.5 → approved.
- Designs follow the same RLCM states (traced, maintained, prioritized, approved).
- Solution Evaluation chain: 8.1 Solution Performance Measures → 8.2 Solution Performance Analysis → 8.3 Solution Limitation and 8.4 Enterprise Limitation → 8.5 Recommended Actions.

STOP: Approve Requirements needs requirements in which state: validated or verified?

USER: Verified

ACTION: Give feedback. A strong answer includes: verified: approval follows quality checking. Validated requirements feed design options.

**Exam trap to call out:** Swapping "verified" and "validated" in the input of Approve Requirements is a classic distractor.

---

## Apply it at GreenBasket: Draw the backbone from memory

Recall beats re-reading. Build the map without looking, then compare it with the graph note.

ACTION: Open and skim [BABOK Input-Output Flow](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/BABOK%20Input-Output%20Flow.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Without opening the note: list as many "task → output → next task" handoffs as you can in 10 minutes. Aim for 15 or more.

USER: Drafts their analysis in the chat

ACTION: Compare with the I/O Flow note: count correct ones, list the missing and wrong ones, and save a personal "handoff map" with a Mermaid diagram of the main chain (BAPM approaches → E&C results → SA outputs → RADD states → RLCM states → SE chain). Mark the ones they missed with ⚠️. Save the result to `workspace/05-my-io-backbone.md` and link it: [05-my-io-backbone.md](workspace/05-my-io-backbone.md).

**Discovery:** Most people forget that Business Requirements come out of **Analyze Current State**, not Define Future State. Did you?

---

## Exam drill

QUIZ: 10 CBAP-style questions on: input/output handoffs, state labels, which task produces or consumes a given output.
Build distractors from these traps: verified vs validated as input to Approve; Business Requirements produced by Define Future State; Solution Scope produced by RADD; Elicitation Results (confirmed) produced by Conduct Elicitation.
Log to scores.csv with ka=`FND` and topic=`io-flow`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. BAPM approaches and SA outputs are hub guidelines.
2. Know the states: unconfirmed → confirmed; specified and modelled → verified / validated → prioritized → approved.
3. The SE chain: measures → analysis → limitations → recommended actions.

> **Exam rule of thumb:** "What should the BA do next?" means: find which task consumes the output you currently have.

**Reading before the next session:**
- BABOK input/output diagrams at the start of each KA chapter (3.0, 4.0, 5.0, 6.0, 7.0, 8.0): study the figures only
- Appendix B Techniques to Task Mapping (p.457): skim

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Business Requirements are output by… :: 6.1 Analyze Current State
- Approve Requirements input state? :: Requirements (verified)
- Define Change Strategy outputs? :: Change Strategy and Solution Scope
- Define Design Options input requirements state? :: Requirements (validated, prioritized)

ACTION: Update [progress.json](progress/progress.json): add this lesson (`1.8`) to `completed` with today's date and minutes ≈ 90, set `current` to `1.9`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 1.9: Underlying competencies & perspectives: a primer. The skills and lenses that frame every scenario.

STOP: Ready for 1.9? Type `/next` (or `/start 1.9`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student recalled at least 15 handoffs
- [ ] workspace/05-my-io-backbone.md created with a Mermaid chain
- [ ] Student knows the requirement state chain
- [ ] Drill logged
