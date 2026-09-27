# Lesson 2.1: BAPM overview + 3.1 Plan Business Analysis Approach

*Module 2 · Week 3 · ~80 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [Business Analysis Planning and Monitoring](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Business%20Analysis%20Planning%20and%20Monitoring.md)
- [Plan Business Analysis Approach](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Approach.md)
- [Business Analysis Approach](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Business%20Analysis%20Approach.md)
- [Needs](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Needs.md)

---

Elena asked for "how you're going to approach this, and no 80-page documents". That's literally **3.1 Plan Business Analysis Approach**. This week is BA Planning & Monitoring (BAPM): 14% of the exam, and the KA whose outputs guide almost every other task.

By the end of this session you will be able to:
- Explain the purpose and five tasks of BAPM
- Explain the 6 elements of Plan Business Analysis Approach
- Choose between predictive and adaptive approaches with reasons
- Know the input (Needs) and output (Business Analysis Approach)

STOP: Ready to dive in?

USER: Ready

---

## Part 1: BAPM at a glance

ACTION: Re-read [Business Analysis Planning and Monitoring](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Business%20Analysis%20Planning%20and%20Monitoring.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Five tasks: 3.1 Plan BA Approach, 3.2 Plan Stakeholder Engagement, 3.3 Plan BA Governance, 3.4 Plan BA Information Management, 3.5 Identify BA Performance Improvements.
- Outputs are *approaches*: BA Approach, Stakeholder Engagement Approach, Governance Approach, Information Management Approach, plus the BA Performance Assessment. These act as guidelines for most other tasks.
- Only two inputs come from outside: Needs, and Performance Objectives (external).
- BACCM in BAPM: e.g. Change = how changes to BA results are requested and authorized; Value = performance analysis to keep BA activities producing value.

STOP: Name the five BAPM outputs.

USER: BA Approach, Stakeholder Engagement Approach, Governance Approach, Information Management Approach, BA Performance Assessment

ACTION: Give feedback. A strong answer includes: all five with exact names.

---

## Part 2: Plan Business Analysis Approach

ACTION: Re-read [Plan Business Analysis Approach](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Approach.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Decide how business analysis will be carried out on this initiative: the overall method, its formality, the activities, their timing, and how the approach gets agreed.
- Elements: Planning Approach (predictive ↔ adaptive continuum), Formality and Level of Detail of BA deliverables, BA Activities, Timing of BA Work, Complexity and Risk, Acceptance.
- Predictive: minimize upfront uncertainty, define before build; suits high risk, regulated contexts, formal sign-off, distributed or outsourced teams. Adaptive: rapid value in short iterations, accepts more uncertainty, lighter documentation, prioritized requirements list.
- Formality rises with complexity and risk, regulation, contracts, geographic distribution, outsourcing, staff turnover, formal sign-off, and long-term maintenance needs.
- Acceptance: the approach is reviewed and agreed with key stakeholders, such as the sponsor.
- Input: Needs. Guidelines include the BA Performance Assessment, business policies, expert judgment, methodologies and frameworks, and the Stakeholder Engagement Approach. Output: Business Analysis Approach.

STOP: GreenBasket has regulated areas (alcohol, cold chain, PCI) but also a tight timeline and a need for store feedback. Predictive, adaptive or a mix? Justify it using two elements.

USER: A hybrid with reasons

ACTION: Give feedback. A strong answer includes: a hybrid is defensible. Predictive formality for compliance areas and vendor contracts (formality element, complexity and risk); adaptive iterations with pilot stores for the customer and picker experience (timing element). BABOK explicitly allows different approaches within one initiative.

**Exam trap to call out:** "Adaptive means no documentation" is false. It means documentation at the team's discretion, often produced after implementation for knowledge transfer.

---

## Apply it at GreenBasket: Draft GreenBasket's Business Analysis Approach (one page)

Elena wants a short, decision-ready approach. Harvest's failures are your best input.

ACTION: Open and skim [01-sponsor-kickoff-email](case-files/01-sponsor-kickoff-email.md), [02-harvest-postmortem](case-files/02-harvest-postmortem.md), [08-compliance-memo](case-files/08-compliance-memo.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Draft a one-page BA approach covering each of the 6 elements: planning approach, formality and level of detail, BA activities (list them), timing, complexity and risk, and how you'll get acceptance. Tie at least 3 decisions to lessons from Harvest.

USER: Drafts their analysis in the chat

ACTION: Coach element by element, then save a polished one-page approach using the element names as headings, plus a "Harvest lessons applied" box. Save the result to `workspace/10-ba-approach.md` and link it: [10-ba-approach.md](workspace/10-ba-approach.md).

A model answer should cover (use it to coach, don't just paste it):
- Hybrid: predictive for compliance, vendor selection and integration; adaptive sprints for customer and picker experience
- Formality: formal sign-off only for compliance-related requirements and the vendor contract; lightweight backlog and models elsewhere
- Activities: discovery (store observation, picker interviews), strategy and business case, requirements, vendor evaluation, pilot evaluation
- Timing: BA leads the project by 1–2 sprints; strategy work before vendor selection
- Complexity and risk: data quality, union, 42 stores, regulation → more store involvement and early risk work
- Acceptance: walkthrough with Elena, Marcus and Tom; approval by Elena

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `elena-sponsor`, giving it the path `workspace/10-ba-approach.md` and ask for a sponsor reaction and whether they would accept it. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

**Discovery:** Harvest had a 212-page specification written in 6 weeks with no store input. Formality without the right stakeholders is not quality.

---

## Exam drill

QUIZ: 8 CBAP-style questions on: BAPM overview and 3.1 Plan Business Analysis Approach (elements, predictive vs adaptive, formality drivers, inputs, guidelines, outputs).
Build distractors from these traps: adaptive = no documentation; approach selected without stakeholder acceptance; Business Analysis Performance Assessment as an input (it is a guideline); confusing BA approach with project management plan.
Log to scores.csv with ka=`BAPM` and topic=`3.1`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. BAPM outputs are guidelines for nearly every other task.
2. 3.1 has 6 elements; the approach can mix predictive and adaptive.
3. Formality follows risk, regulation, distribution and sign-off needs.

> **Exam rule of thumb:** The BA plans BA work (the approach). The project manager plans the project. Don't pick answers where the BA writes the project plan.

**Reading before the next session:**
- BABOK 3.0–3.1 (pp.21–31)
- Lessing ch.6 pp.73–84
- Jonasson 4.3.1 (pp.34–48): waterfall, iterative, agile

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 3.1 elements? :: Planning Approach; Formality & Level of Detail; BA Activities; Timing of BA Work; Complexity & Risk; Acceptance
- 3.1 input? :: Needs
- Predictive approaches are preferred when… :: requirements can be defined upfront, implementation risk is high, or stakeholder engagement is difficult

ACTION: Update [progress.json](progress/progress.json): add this lesson (`2.1`) to `completed` with today's date and minutes ≈ 80, set `current` to `2.2`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 2.2: 3.2 Plan Stakeholder Engagement. Stakeholder analysis, collaboration and communication needs, with Marcus.

STOP: Ready for 2.2? Type `/next` (or `/start 2.2`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student named the five BAPM outputs
- [ ] Student explained predictive vs adaptive trade-offs
- [ ] workspace/10-ba-approach.md created and reviewed by the sponsor agent
- [ ] Drill logged; task card for 3.1 updated in workspace/task-cards.md
