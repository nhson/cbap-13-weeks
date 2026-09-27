# Lesson 1.3: Requirements classification & requirements vs designs

*Module 1 · Week 1 · ~75 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [Requirements Classification Schema](CBAP%20Knowledge%20Graph/01%20Foundations/Requirements%20Classification%20Schema.md)
- [Requirements and Designs](CBAP%20Knowledge%20Graph/01%20Foundations/Requirements%20and%20Designs.md)
- [Business Requirements](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Business%20Requirements.md)
- [Non-Functional Requirements Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Non-Functional%20Requirements%20Analysis.md)

---

Tom, the PM, has pasted 20 "requirements" into a spreadsheet and asked you to "sort them out". Half of them aren't requirements at all.

Today you learn the classification schema that the exam uses constantly: **business → stakeholder → solution (functional / non-functional) → transition**.

By the end of this session you will be able to:
- Classify requirements into the four BABOK types plus functional/non-functional
- Spot designs disguised as requirements
- Explain why transition requirements are special

STOP: Ready to dive in?

USER: Ready

---

## Part 1: The four types

ACTION: Re-read [Requirements Classification Schema](CBAP%20Knowledge%20Graph/01%20Foundations/Requirements%20Classification%20Schema.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Business requirements: goals, objectives and outcomes. *Why* the change was initiated. They can be enterprise-wide, business-area or initiative level.
- Stakeholder requirements: needs of stakeholders that must be met to achieve the business requirements. The bridge between business and solution requirements.
- Solution requirements: capabilities and qualities of the solution. **Functional** = behaviour and information managed. **Non-functional (quality of service)** = conditions under which it must remain effective, or qualities it must have.
- Transition requirements: capabilities and conditions needed only to get from the current state to the future state, such as data conversion, training and business continuity. **Temporary.**

STOP: Classify these: (a) "Online sales reach 5% of total within 2 years", (b) "Store managers need to see today's pickup orders by slot", (c) "The pick list is sorted by aisle sequence", (d) "Pages load within 2 s for 95% of requests", (e) "Train 200 store staff before go-live".

USER: a business, b stakeholder, c functional, d non-functional, e transition

ACTION: Give feedback. A strong answer includes: a = business (outcome, why); b = stakeholder (a need of a group); c = solution-functional; d = solution-non-functional; e = transition (temporary).

**Exam trap to call out:** Training and data migration are *transition* requirements, not non-functional. And "temporary" is the tell.

---

## Part 2: Requirements vs designs, and asking "why?"

ACTION: Re-read [Requirements and Designs](CBAP%20Knowledge%20Graph/01%20Foundations/Requirements%20and%20Designs.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Requirements focus on the need; designs focus on the solution. The same techniques elicit both, and a requirement can lead to a design that uncovers more requirements.
- BABOK tasks that say "requirements" (e.g. Trace, Specify and Model) include designs too.
- Stakeholders often present a solution to an assumed need. The BA keeps asking **why** until the need is clear.
- Example: "Use a React Native app with ShelfWise APIs" is a design or technology choice, not a requirement.

STOP: Elena wants "real-time stock for every product". Ask "why?" twice. What need might sit underneath?

USER: Customers must not order items that are unavailable → order accuracy / trust

ACTION: Give feedback. A strong answer includes: the underlying need is order accuracy and customer trust (avoid unavailable items), which could be met by other designs such as a stock-confidence indicator plus substitution preferences.

---

## Apply it at GreenBasket: Sort Tom's spreadsheet

Tom's draft list is a mix of goals, needs, features, designs and wishes.

ACTION: Open and skim [11-draft-requirements-v0](case-files/11-draft-requirements-v0.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Classify R-01 to R-20 by type (business / stakeholder / solution-functional / solution-NFR / transition), and mark any that are really **designs** or **not requirements at all**. Do at least 10 yourself, and I'll check them.

USER: Drafts their analysis in the chat

ACTION: Check each classification and explain disagreements. Produce a table: ID | type | design? | why | note. Save the result to `workspace/02-requirements-classification.md` and link it: [02-requirements-classification.md](workspace/02-requirements-classification.md).

A model answer should cover (use it to coach, don't just paste it):
- R-20 "Reduce customer churn" = business requirement (too vague to be measurable yet)
- R-03 React Native + ShelfWise = design/technology constraint, not a requirement
- R-15 staff training and R-16 migrate phone-order customers = transition
- R-18 availability and R-01 "fast/user-friendly" = NFR (R-01 not measurable)
- R-05, R-09, R-10, R-12, R-14, R-17, R-19 = functional (R-19 is also a constraint from compliance)
- R-04 one-lap rule = a design constraint from the sponsor; ask why

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `anil-architect`, giving it the path `workspace/02-requirements-classification.md` and ask which items are designs rather than requirements, and which are infeasible. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

**Discovery:** Several "High" priorities came from one person, with no link to a business objective. You will fix that properly in RLCM (prioritization) and RADD (verify and validate).

---

## Exam drill

QUIZ: 8 CBAP-style questions on: classifying requirements (business, stakeholder, solution-functional, solution-non-functional, transition) and requirement vs design.
Mix: mostly "classify this statement" scenarios.
Build distractors from these traps: training/migration labelled non-functional; business requirement vs stakeholder requirement; design presented as requirement; NFR vs functional for security/audit features.
Log to scores.csv with ka=`FND` and topic=`req-classification`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Four types: business (why), stakeholder (needs of groups), solution (functional plus NFR), transition (temporary).
2. Requirements ↔ need; designs ↔ solution; keep asking why.
3. Designs and technology choices hide inside requirement lists. Flag them.

> **Exam rule of thumb:** If it disappears once the change is complete (training, conversion, parallel run), it is a transition requirement.

**Reading before the next session:**
- BABOK 2.3 and 2.5, pp.16 and 19–20
- Lessing ch.5 pp.59–63
- Jonasson ch.3 pp.25–26

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Transition requirements? :: Temporary capabilities/conditions to move from current to future state (data conversion, training, business continuity)
- Stakeholder requirements bridge… :: business requirements and solution requirements
- NFR also called? :: Quality of service requirements

ACTION: Update [progress.json](progress/progress.json): add this lesson (`1.3`) to `completed` with today's date and minutes ≈ 75, set `current` to `1.4`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 1.4: Stakeholders: the 11 generic roles. Who is who, in BABOK terms, at GreenBasket.

STOP: Ready for 1.4? Type `/next` (or `/start 1.4`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student classified at least 10 of the 20 requirements correctly
- [ ] Student identified designs inside the list
- [ ] workspace/02-requirements-classification.md created
- [ ] Drill completed and logged
