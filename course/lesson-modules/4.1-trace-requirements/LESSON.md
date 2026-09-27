# Lesson 4.1: RLCM overview + 5.1 Trace Requirements

*Module 4 · Week 5 · ~75 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [Requirements Life Cycle Management](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Requirements%20Life%20Cycle%20Management.md)
- [Trace Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Trace%20Requirements.md)
- [Requirements (traced)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements%20%28traced%29.md)
- [Requirements](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Requirements.md)
- [Designs](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Designs.md)

---

Harvest's post-mortem: "Nobody could tell *why* a feature existed." Traceability is the cure. This week is RLCM (15%): managing requirements and designs **from inception to retirement**. First, **5.1 Trace Requirements**.

By the end of this session you will be able to:
- Explain RLCM's scope (inception to retirement) and its 5 tasks
- Know the traceability relationships
- Build a traceability chain for GreenBasket

STOP: Ready to dive in?

USER: Ready

---

## Part 1: RLCM at a glance

ACTION: Re-read [Requirements Life Cycle Management](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Requirements%20Life%20Cycle%20Management.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Five tasks: 5.1 Trace, 5.2 Maintain, 5.3 Prioritize, 5.4 Assess Requirements Changes, 5.5 Approve.
- The life cycle starts with the representation of a need and ends when the solution and its requirements are **retired**, not when the project ends.
- RLCM applies to requirements *and designs*. Outputs come in pairs: Requirements (traced) and Designs (traced), and so on.
- Guidelines come from BAPM (Information Management Approach, Governance Approach) and SA/RADD (Change Strategy, Solution Scope, Requirements Architecture).

STOP: When does the requirements life cycle end?

USER: When the requirements and solution are retired

ACTION: Give feedback. A strong answer includes: when the solution and the requirements that represent it are retired. Requirements keep providing value while the solution is in use.

---

## Part 2: Trace Requirements

ACTION: Re-read [Trace Requirements](CBAP%20Knowledge%20Graph/03%20Tasks/Trace%20Requirements.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Link requirements and designs across levels so that alignment, coverage and the impact of changes are visible.
- Elements: Level of Formality, Relationships, Traceability Repository.
- Relationships: **Derive** (a child derived from a parent, e.g. solution from business requirement), **Depends** (Necessity: only makes sense if the other exists; Effort: easier if the other is implemented), **Satisfy** (implementation element to the requirement it satisfies), **Validate** (requirement to the test case that verifies it).
- Supports impact analysis, coverage (nothing missing, nothing extra) and scope control.
- Inputs: Requirements, Designs. Guidelines: Domain Knowledge, Information Management Approach, Legal/Regulatory Information, Requirements Management Tools/Repository. Outputs: Requirements (traced), Designs (traced).

STOP: "Allergen display on product pages" only makes sense if "product master data includes allergens" exists. Which relationship?

USER: Depends (necessity)

ACTION: Give feedback. A strong answer includes: depends, necessity type.

**Exam trap to call out:** Traceability formality should match the value and risk. Tracing everything at maximum detail is not the BABOK answer.

---

## Apply it at GreenBasket: Traceability chain for Click & Collect

Show Elena why each feature exists and expose orphans.

ACTION: Open and skim [11-draft-requirements-v0](case-files/11-draft-requirements-v0.md), [02-requirements-classification](workspace/02-requirements-classification.md), [01-sponsor-kickoff-email](case-files/01-sponsor-kickoff-email.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Build a traceability matrix from 2 business objectives (e.g. reach 5% online share; order accuracy ≥97%) → stakeholder requirements → solution requirements (use R-IDs) → a test idea. Label each link as derive, depends, satisfy or validate. Which requirements trace to *no* objective?

USER: Drafts their analysis in the chat

ACTION: Coach and save the matrix plus a Mermaid trace graph. List orphans (e.g. R-11 recipes, R-03 React Native) and what to do with them: park, challenge, or find their objective. Save the result to `workspace/30-traceability-matrix.md` and link it: [30-traceability-matrix.md](workspace/30-traceability-matrix.md).

**Discovery:** R-11 (recipes) traces to no business objective. Traceability just gave you a neutral, evidence-based way to push back on Lily.

---

## Exam drill

QUIZ: 8 CBAP-style questions on: RLCM scope and 5.1 Trace Requirements: relationships (derive, depends necessity/effort, satisfy, validate), formality, uses of traceability.
Build distractors from these traps: life cycle ends at project close; satisfy vs validate relationship; necessity vs effort dependency; trace everything at maximum formality.
Log to scores.csv with ka=`RLCM` and topic=`5.1`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. RLCM runs until retirement and covers requirements and designs.
2. Relationships: derive, depends (necessity, effort), satisfy, validate.
3. Traceability supports impact analysis, coverage and scope control.

> **Exam rule of thumb:** A requirement tracing to no business objective is a scope-creep candidate. Challenge it.

**Reading before the next session:**
- BABOK 5.0–5.1 (pp.75–82)
- Lessing ch.8 pp.148–158
- Jonasson 6.3.1 (p.136)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Traceability relationships? :: Derive, Depends (Necessity, Effort), Satisfy, Validate
- 5.1 elements? :: Level of Formality; Relationships; Traceability Repository
- When does the requirements life cycle end? :: When the requirements and solution are retired

ACTION: Update [progress.json](progress/progress.json): add this lesson (`4.1`) to `completed` with today's date and minutes ≈ 75, set `current` to `4.2`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 4.2: 5.2 Maintain Requirements. Keep requirements accurate, attributed and reusable.

STOP: Ready for 4.2? Type `/next` (or `/start 4.2`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/30-traceability-matrix.md created
- [ ] Student labelled relationship types correctly
- [ ] Drill logged; task card added
