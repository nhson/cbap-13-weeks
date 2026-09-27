# Lesson 2.4: 3.4 Plan Business Analysis Information Management

*Module 2 · Week 3 · ~70 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Plan Business Analysis Information Management](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Information%20Management.md)
- [Information Management Approach](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Information%20Management%20Approach.md)
- [02-harvest-postmortem](case-files/02-harvest-postmortem.md)

---

Harvest's spec mixed business needs with screen designs, and nobody could tell *why* a feature existed. That's an information management failure. Today: **3.4 Plan BA Information Management**.

By the end of this session you will be able to:
- Explain the 6 elements of 3.4
- Choose the level of abstraction per audience
- Plan traceability, reuse, storage and requirements attributes

STOP: Ready to dive in?

USER: Ready

---

## Part 1: The task

ACTION: Re-read [Plan Business Analysis Information Management](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Information%20Management.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Decide how business analysis information will be organized, detailed, traced, reused, stored and described with attributes.
- Elements: Organization of BA Information, Level of Abstraction (by audience and complexity), Plan Traceability Approach, Plan for Requirements Reuse, Storage and Access, Requirements Attributes.
- Attributes: absolute reference, author, complexity, ownership, priority, risks, source, stability, status, urgency.
- Inputs: BA Approach, Governance Approach, Stakeholder Engagement Approach. Output: Information Management Approach, a guideline for 4.4, 5.1, 5.2 and an input to 7.4.

STOP: Which attribute would have answered "why does this feature exist?" in Harvest?

USER: Source (and traceability to business objectives)

ACTION: Give feedback. A strong answer includes: source (and the traceability approach linking requirements to business objectives).

**Exam trap to call out:** Information *management* (3.4, planning storage, traceability and attributes) vs requirements *architecture* (7.4, how requirements fit together).

---

## Apply it at GreenBasket: Information Management Approach

Decide how Click & Collect's BA information will be organized so nothing gets lost like in Harvest.

ACTION: Open and skim [11-draft-requirements-v0](case-files/11-draft-requirements-v0.md), [02-harvest-postmortem](case-files/02-harvest-postmortem.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Decide: how information is organized (by what structure?), levels of abstraction for Elena, stores and vendors, the traceability approach (what traces to what, at what formality), what will be reused (hint: Harvest adapter, the prototype), storage and access (tool, permissions), and the attribute set you will capture for every requirement.

USER: Drafts their analysis in the chat

ACTION: Coach and save the approach, including an attribute table with an example requirement (R-17 pick path) fully attributed. Save the result to `workspace/13-information-management-approach.md` and link it: [13-information-management-approach.md](workspace/13-information-management-approach.md).

A model answer should cover (use it to coach, don't just paste it):
- Organize by business objective → capability (ordering, picking, staging, handover, loyalty, compliance) → requirements and designs
- Abstraction: one-page views for Elena; process models and user stories for stores and vendors
- Trace business objectives → stakeholder requirements → solution requirements → test cases; formality higher for compliance
- Reuse: Harvest TillMaster adapter requirements, customer prototype insights
- Storage: one repository with role-based access; the vendor gets read access to relevant sections

**Discovery:** Reuse is an explicit BABOK element: Harvest's adapter and prototype findings are assets, not waste.

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 3.4 elements, requirements attributes, levels of abstraction, traceability planning, reuse, storage and access.
Build distractors from these traps: 3.4 vs 7.4 requirements architecture; attributes list confused with quality characteristics (atomic, complete…); Information Management Approach as input to 5.1 (it is a guideline for 5.1).
Log to scores.csv with ka=`BAPM` and topic=`3.4`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 6 elements: organization, abstraction, traceability approach, reuse, storage and access, attributes.
2. Attributes are metadata (source, priority, status…), not quality characteristics.
3. Output guides Trace, Maintain, Communicate and Requirements Architecture.

> **Exam rule of thumb:** If the question is about *where and how BA information is stored, accessed, attributed or reused*, think 3.4.

**Reading before the next session:**
- BABOK 3.4 (pp.42–46)
- Lessing pp.92–97

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 3.4 elements? :: Organization of BA Info; Level of Abstraction; Plan Traceability Approach; Plan for Requirements Reuse; Storage & Access; Requirements Attributes
- Common requirements attributes? :: absolute reference, author, complexity, ownership, priority, risks, source, stability, status, urgency

ACTION: Update [progress.json](progress/progress.json): add this lesson (`2.4`) to `completed` with today's date and minutes ≈ 70, set `current` to `2.5`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 2.5: 3.5 Identify Business Analysis Performance Improvements. Measuring and improving the BA work itself.

STOP: Ready for 2.5? Type `/next` (or `/start 2.5`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/13-information-management-approach.md created
- [ ] Student distinguishes attributes from quality characteristics
- [ ] Drill logged; task card added
