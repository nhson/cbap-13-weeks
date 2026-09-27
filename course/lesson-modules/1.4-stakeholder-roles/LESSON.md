# Lesson 1.4: Stakeholders: the 11 generic roles

*Module 1 · Week 1 · ~60 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [Stakeholder Roles](CBAP%20Knowledge%20Graph/01%20Foundations/Stakeholder%20Roles.md)
- [Sponsor](CBAP%20Knowledge%20Graph/01%20Foundations/Stakeholder%20Roles/Sponsor.md)
- [Domain Subject Matter Expert](CBAP%20Knowledge%20Graph/01%20Foundations/Stakeholder%20Roles/Domain%20Subject%20Matter%20Expert.md)
- [Implementation Subject Matter Expert](CBAP%20Knowledge%20Graph/01%20Foundations/Stakeholder%20Roles/Implementation%20Subject%20Matter%20Expert.md)
- [Regulator](CBAP%20Knowledge%20Graph/01%20Foundations/Stakeholder%20Roles/Regulator.md)
- [End User](CBAP%20Knowledge%20Graph/01%20Foundations/Stakeholder%20Roles/End%20User.md)
- [STAKEHOLDERS](company-context/stakeholders/STAKEHOLDERS.md)

---

The BABOK lists 11 generic stakeholder roles. The exam loves questions like "who should approve…?" or "which stakeholder is most likely to…?". Get the roles crisp, and a lot of questions become easy.

By the end of this session you will be able to:
- Name and define the 11 generic stakeholder roles
- Map real people to roles (one person, many roles)
- Distinguish domain SME and implementation SME, and sponsor and project manager

STOP: Ready to dive in?

USER: Ready

---

## Part 1: The 11 roles

ACTION: Re-read [Stakeholder Roles](CBAP%20Knowledge%20Graph/01%20Foundations/Stakeholder%20Roles.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Business analyst, customer, domain SME, end user, implementation SME, operational support, project manager, regulator, sponsor, supplier, tester.
- Sponsor: initiates the effort, authorizes the work, controls budget and scope. Project manager: manages the work, balancing scope, budget, schedule, resources, quality and risk.
- Domain SME = in-depth knowledge of the business topic or need. Implementation SME = specialized knowledge of building or implementing solution components (architect, developer, DBA, trainer, change manager…).
- Regulator: defines and enforces standards (legislation, governance, audit). This can be internal (e.g. compliance or audit) or external.
- Supplier: outside the organization, provides products or services. Operational support: day-to-day running (help desk, release manager). Tester: verifies the solution meets requirements (QA).
- One individual can fill several roles, and any stakeholder can be a source of requirements, assumptions or constraints.

STOP: A trainer who will teach pickers the new handheld process: which role? And the internal auditor who checks alcohol-sale logs?

USER: Implementation SME; Regulator

ACTION: Give feedback. A strong answer includes: trainer = implementation SME (BABOK lists trainers and organizational change consultants there); internal auditor = regulator.

**Exam trap to call out:** The exam often swaps sponsor and project manager. Budget and scope authority = **sponsor**.

---

## Apply it at GreenBasket: Map GreenBasket's people to BABOK roles

Before you can plan stakeholder engagement (week 3), you need to know who plays which role.

ACTION: Open and skim [STAKEHOLDERS](company-context/stakeholders/STAKEHOLDERS.md), [COMPANY](company-context/COMPANY.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Build a table: person/group → BABOK role(s) → why. Include at least: Elena, David, Marcus, Rosa, Kim, Anil, Helen, Janet, the union, Tom, Priyanka, Dev, Lily, Ben, the customer personas, and the three vendors. Who plays more than one role?

USER: Drafts their analysis in the chat

ACTION: Validate the mapping, challenge any mistakes (e.g. Janet = regulator (internal); Rosa = domain SME and end-user representative; the union = not a generic BABOK role, but a stakeholder with influence, relevant to the regulator/HR context). Save the table. Save the result to `workspace/03-stakeholder-roles.md` and link it: [03-stakeholder-roles.md](workspace/03-stakeholder-roles.md).

A model answer should cover (use it to coach, don't just paste it):
- Elena = sponsor; David = sponsor-adjacent decision maker (budget approval)
- Marcus, Rosa, Ben, Owen, Lily, Nadia = domain SMEs; Rosa and Kim also end users
- Anil, Helen = implementation SMEs; vendors = suppliers (and implementation SMEs during build)
- Janet + state agencies + PCI = regulators
- Tom = project manager; Priyanka = tester; Dev = operational support; personas = customers

---

## Exam drill

QUIZ: 8 CBAP-style questions on: the 11 generic stakeholder roles and their responsibilities.
Mix: scenario "which role" questions.
Build distractors from these traps: sponsor vs project manager; domain SME vs implementation SME; supplier vs customer; regulator only external.
Log to scores.csv with ka=`FND` and topic=`stakeholder-roles`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 11 generic roles. One person can hold several.
2. Sponsor authorizes and funds; PM manages the work.
3. Domain SME knows the business; implementation SME knows how to build it.

> **Exam rule of thumb:** Budget or scope authority → sponsor. Standards enforcement (even internal) → regulator.

**Reading before the next session:**
- BABOK 2.4, pp.16–19
- Lessing ch.5 pp.55–58

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Who authorizes work and controls budget/scope? :: Sponsor
- Trainer, solution architect, DBA are… :: Implementation SMEs
- Help desk, release manager are… :: Operational support

ACTION: Update [progress.json](progress/progress.json): add this lesson (`1.4`) to `completed` with today's date and minutes ≈ 60, set `current` to `1.5`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 1.5: Anatomy of a BABOK task & how to study the Guide. The 8-part structure behind all 30 tasks, and how to read the BABOK efficiently.

STOP: Ready for 1.5? Type `/next` (or `/start 1.5`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student can name all 11 roles
- [ ] workspace/03-stakeholder-roles.md created
- [ ] Student correctly separated sponsor/PM and domain/implementation SME
- [ ] Drill completed and logged
