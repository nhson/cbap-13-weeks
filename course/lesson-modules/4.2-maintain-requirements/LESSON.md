# Lesson 4.2: 5.2 Maintain Requirements

*Module 4 · Week 5 · ~60 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Maintain Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Maintain%20Requirements.md)
- [Requirements (maintained)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20%28maintained%29.md)
- [Plan Business Analysis Information Management](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Information%20Management.md)

---

The Harvest TillMaster adapter worked. Its requirements could save GreenBasket months, if anyone had maintained them. **5.2 Maintain Requirements** is about accuracy, consistency and reuse.

By the end of this session you will be able to:
- Know the 3 elements of 5.2
- Explain requirements reuse and levels of abstraction for reuse
- Link 5.2 back to 3.4

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Maintain Requirements

ACTION: Re-read [Maintain Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Maintain%20Requirements.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Keep requirements correct, consistent and well-attributed over their whole life, and make them reusable.
- Elements: Maintain Requirements, Maintain Attributes, Reusing Requirements.
- Reuse works best at higher abstraction and requires maintained, clearly named and stored requirements, including requirements of existing solutions still in use.
- Inputs: Requirements, Designs. Guideline: Information Management Approach. Outputs: Requirements (maintained), Designs (maintained).

STOP: Which BAPM task planned what you are now executing in 5.2?

USER: 3.4 Plan BA Information Management

ACTION: Give feedback. A strong answer includes: 3.4 planned the attributes, reuse and storage; 5.2 executes that plan.

---

## Apply it at GreenBasket: Reuse inventory from Harvest

Salvage what is reusable, and maintain it properly.

ACTION: Open and skim [02-harvest-postmortem](case-files/02-harvest-postmortem.md), [07-it-landscape](case-files/07-it-landscape.md), [13-information-management-approach](workspace/13-information-management-approach.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: List Harvest assets with reusable requirements (e.g. TillMaster adapter, customer prototype findings, Kim's picker issues). For each, state the reuse level (enterprise, domain, initiative), what must be updated, and the attributes to maintain.

USER: Drafts their analysis in the chat

ACTION: Coach and save a reuse inventory. Note the TillMaster v9.4 firmware dependency and the stale assumption about inventory accuracy that must be corrected before reuse. Save the result to `workspace/31-requirements-reuse-inventory.md` and link it: [31-requirements-reuse-inventory.md](workspace/31-requirements-reuse-inventory.md).

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 5.2 elements, reuse, maintaining attributes, relation to 3.4.
Build distractors from these traps: maintain only during the project; 5.2 vs 5.4 (changes); reuse only at detailed level.
Log to scores.csv with ka=`RLCM` and topic=`5.2`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 5.2 keeps requirements accurate beyond the change and enables reuse.
2. Executes the Information Management Approach from 3.4.

**Reading before the next session:**
- BABOK 5.2 (pp.83–85)
- Lessing pp.158–161

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 5.2 elements? :: Maintain Requirements; Maintain Attributes; Reusing Requirements

ACTION: Update [progress.json](progress/progress.json): add this lesson (`4.2`) to `completed` with today's date and minutes ≈ 60, set `current` to `4.3`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 4.3: 5.3 Prioritize Requirements. Everyone says "High". Run a prioritization that holds up.

STOP: Ready for 4.3? Type `/next` (or `/start 4.3`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/31-requirements-reuse-inventory.md created
- [ ] Drill logged; task card added
