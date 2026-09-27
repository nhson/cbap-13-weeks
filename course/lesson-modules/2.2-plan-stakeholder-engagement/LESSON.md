# Lesson 2.2: 3.2 Plan Stakeholder Engagement

*Module 2 · Week 3 · ~75 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Plan Stakeholder Engagement](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Stakeholder%20Engagement.md)
- [Stakeholder List, Map, or Personas](CBAP%20Knowledge%20Graph/05%20Techniques/Stakeholder%20List%2C%20Map%2C%20or%20Personas.md)
- [Stakeholder Engagement Approach](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Stakeholder%20Engagement%20Approach.md)
- [STAKEHOLDERS](company-context/stakeholders/STAKEHOLDERS.md)

---

Harvest "informed" store managers by email a week before trial. Marcus hasn't forgotten. Today you plan stakeholder engagement properly: **3.2 Plan Stakeholder Engagement**.

By the end of this session you will be able to:
- Perform stakeholder analysis (roles, attitudes, decision authority, power and interest)
- Define collaboration and communication needs
- Use stakeholder lists, maps (onion, power/interest), RACI and personas

STOP: Ready to dive in?

USER: Ready

---

## Part 1: The task

ACTION: Re-read [Plan Stakeholder Engagement](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Stakeholder%20Engagement.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Work out who the stakeholders are, what they are like, and how the BA will work and communicate with each of them.
- Elements: Perform Stakeholder Analysis (identify, roles, attitudes, decision-making authority, level of power or influence), Define Stakeholder Collaboration, Stakeholder Communication Needs (what, format, frequency, level of detail, cultural and geographic considerations).
- Inputs: Needs, Business Analysis Approach. Output: Stakeholder Engagement Approach.
- Attitudes to analyze: towards the business goals, the solution approach, business analysis itself, collaboration, and the sponsor.

STOP: Which element would you use to capture "Marcus prefers face-to-face meetings and distrusts slide decks"?

USER: Stakeholder Communication Needs (and attitude in stakeholder analysis)

ACTION: Give feedback. A strong answer includes: mostly Stakeholder Communication Needs (format, delivery), with his attitude captured in Perform Stakeholder Analysis.

---

## Part 2: Signature technique: Stakeholder List, Map, or Personas

ACTION: Re-read [Stakeholder List, Map, or Personas](CBAP%20Knowledge%20Graph/05%20Techniques/Stakeholder%20List%2C%20Map%2C%20or%20Personas.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Stakeholder matrix (influence/power × impact/interest): high/high = work closely, high power/low interest = keep satisfied (ensure needs met), low power/high interest = keep informed, low/low = monitor.
- Onion diagram: solution delivery team → affected organizational units → organization/enterprise → external stakeholders (customers, suppliers, regulators).
- RACI: Responsible, Accountable (only one), Consulted, Informed.
- Personas: fictional characters representing a user type, e.g. "Busy Parent Sam".

STOP: Janet (compliance) has high power but low interest until something touches her domains. Which quadrant, and what engagement strategy?

USER: High power / low interest: keep satisfied

ACTION: Give feedback. A strong answer includes: keep satisfied: targeted involvement on the six compliance areas, early sight of related requirements, no need for every meeting.

**Exam trap to call out:** RACI allows only **one** Accountable per activity.

---

## Apply it at GreenBasket: Stakeholder Engagement Approach for Click & Collect

Build the approach that would have saved Harvest.

ACTION: Open and skim [STAKEHOLDERS](company-context/stakeholders/STAKEHOLDERS.md), [02-harvest-postmortem](case-files/02-harvest-postmortem.md), [10-workshop-notes-raw](case-files/10-workshop-notes-raw.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Produce: (1) a power/interest map of at least 12 stakeholders, (2) attitude notes for Marcus, Lily, Janet and Kim, (3) a RACI for "approve store-process requirements", and (4) communication needs for 4 key groups (format, frequency, detail).

USER: Drafts their analysis in the chat

ACTION: Coach and correct (e.g. one Accountable only; union via HR; pickers must be consulted). Save the full Stakeholder Engagement Approach including a Mermaid quadrant chart or a table. Save the result to `workspace/11-stakeholder-engagement-approach.md` and link it: [11-stakeholder-engagement-approach.md](workspace/11-stakeholder-engagement-approach.md).

A model answer should cover (use it to coach, don't just paste it):
- Manage closely: Elena, Marcus, Rosa (as store voice), Anil
- Keep satisfied: David (CFO), Janet, Helen, Nadia/union
- Keep informed: Kim and pickers (high interest; empower with a voice), Lily, Ben, Dev, customers (via panels)
- Marcus: resistant; engage face-to-face, co-design pilot selection, address funding of pickers
- RACI: Accountable = Marcus (store process owner); Responsible = BA; Consulted = Rosa, Kim, Nadia, Janet; Informed = Tom, Priyanka

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `marcus-store-ops`, giving it the path `workspace/11-stakeholder-engagement-approach.md` and ask for his honest reaction to how stores are engaged. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

**Discovery:** Marcus's resistance is about funding and respect, not the idea itself. Stakeholder analysis finds the *reason* behind an attitude.

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 3.2 Plan Stakeholder Engagement: elements, attitudes, power/interest, onion diagram, RACI, personas, communication needs.
Build distractors from these traps: more than one Accountable; keep satisfied vs keep informed; Stakeholder Engagement Approach vs Stakeholder Engagement (4.5 output); confusing stakeholder analysis with requirements elicitation.
Log to scores.csv with ka=`BAPM` and topic=`3.2`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Analyze roles, attitudes, decision authority and power/influence.
2. Plan collaboration *and* communication needs, tailored per group.
3. Output: Stakeholder Engagement Approach (the plan). 4.5 later produces Stakeholder Engagement (the result).

> **Exam rule of thumb:** A resistant, high-power stakeholder calls for early, direct engagement and understanding their concerns. Never go around them.

**Reading before the next session:**
- BABOK 3.2 (pp.31–36) and 10.43 (pp.344–347)
- Lessing pp.84–88 and 427
- Jonasson 4.3.2 (pp.49–56): user profiling

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 3.2 elements? :: Perform Stakeholder Analysis; Define Stakeholder Collaboration; Stakeholder Communication Needs
- RACI? :: Responsible, Accountable (one only), Consulted, Informed
- High power, low interest quadrant strategy? :: Keep satisfied

ACTION: Update [progress.json](progress/progress.json): add this lesson (`2.2`) to `completed` with today's date and minutes ≈ 75, set `current` to `2.3`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 2.3: 3.3 Plan Business Analysis Governance. Who decides, who approves, and how changes are controlled.

STOP: Ready for 2.3? Type `/next` (or `/start 2.3`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student built a power/interest map
- [ ] workspace/11-stakeholder-engagement-approach.md created and reviewed by the Marcus agent
- [ ] Student can explain the attitude dimensions
- [ ] Drill logged; task card added
