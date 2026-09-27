from render import T, TE, KA, IO, F, CC, R, UC, P, EX, CF

MODULE = {'id': '1', 'name': 'Foundations', 'weeks': '1–2',
          'description': 'Exam anatomy, the BACCM, key terms, requirements classification, stakeholder roles, how a BABOK task is built, the diagnostic exam, and the input/output backbone of the whole guide.',
          'lessons': [
{
 'id': '1.1', 'slug': 'welcome', 'title': 'Welcome to GreenBasket & your CBAP game plan', 'week': 1, 'minutes': 60, 'reading_min': 30, 'ka': 'GEN', 'type': 'lesson',
 'teaser': 'Your first day at GreenBasket, and the exam game plan.',
 'prepare': ['company-context/SCENARIO.md', 'company-context/COMPANY.md', EX('Exam Blueprint'), '../CBAP-Roadmap.md'],
 'hook': """Welcome to GreenBasket Markets. It's your first day as Senior Business Analyst, and your inbox already has a problem in it.

Over the next 13 weeks you'll do two things at once: **pass the CBAP exam**, and **take GreenBasket's "Click & Collect" initiative from messy idea to evaluated pilot**, using every BABOK knowledge area along the way. The exam tests whether you can *apply* BABOK in scenarios, and that's exactly what you'll practise here.

How this works: I teach a concept, you apply it to GreenBasket, and then I test you with exam-style questions. Your work goes in `workspace/`, your scores go in `progress/`, and the whole BABOK lives as a linked knowledge graph in `CBAP Knowledge Graph/`.""",
 'objectives': ['Explain the CBAP exam format and blueprint weights', 'Know how the course, commands and files work', 'Set your exam date and weekly study rhythm', 'Meet the GreenBasket scenario'],
 'ready': 'Before we start: what should I call you, and have you booked (or planned) your exam date yet?',
 'teach': [
  {'title': 'The exam you are training for',
   'read': [EX('Exam Blueprint')],
   'points': ['120 multiple-choice questions in 210 minutes (about 1:45 per question). Questions are scenario-based and case-study based and test application, not recall. Based on BABOK v3.',
              'Blueprint: RADD 30%, RLCM 15%, SA 15%, BAPM 14%, SE 14%, E&C 12%. Techniques (Ch 10) are woven through all of them and underpin roughly a third of question content.',
              'Case-study questions give a long scenario followed by several questions. Several answers are "good" and one is *most BABOK-correct*.',
              'Eligibility reminder: 7,500 BA hours in 10 years, 900 hours in 4 of the 6 KAs, 35 PD hours, 2 references. The application is valid for 1 year, with up to 3 attempts.'],
   'check': 'Quick gut check: based on those weights, where should most of your study hours go, and which KA is the smallest?',
   'expect': 'RADD most; E&C smallest',
   'feedback': 'RADD at 30% (≈36 questions) is more than double any other KA; E&C is 12% but its techniques appear everywhere, so it is not skippable.'},
  {'title': 'How this course works',
   'points': ['Commands: `/next` continues, `/start 2.3` jumps to a lesson, `/progress` shows the dashboard, `/drill RADD 10` runs a quick quiz, `/grade mock-1` marks a written exam.',
              'Each lesson follows teach → apply at GreenBasket → exam drill → wrap-up, and takes about 60–90 minutes. Reading assignments come from BABOK, Lessing and Jonasson.',
              'Stakeholder reviewers are available as agents: Elena (sponsor), Marcus (store ops, sceptical), Anil (architect), Priyanka (QA), and a strict CBAP examiner.',
              'The error log is your most valuable file. Every miss gets a "rule to remember".',
              'The 13-week plan: Foundations (1–2), BAPM (3), E&C (4), RLCM (5), SA (6), RADD (7–8), SE (9), Consolidation (10), Mock exams (11–13).'],
   'check': 'Which of those reviewers do you think will give you the hardest time, and why?',
   'expect': 'Any, usually Marcus or the examiner'}
 ],
 'apply': [
  {'title': 'Your first read of the situation',
   'brief': "Elena's kickoff email is waiting. Don't analyze it formally yet (that's the next lesson). Just take a BA's first look.",
   'files': [CF('01-sponsor-kickoff-email.md'), 'company-context/SCENARIO.md'],
   'ask': 'Read the email. In 3 bullets: what is the real **need** behind it, what are **solutions** being assumed, and what worries you?',
   'action': 'Coach the answer: separate need (losing share and visit frequency, convenience gap) from assumed solutions (ShelfWise, real-time stock, one-lap rule, slick app). Then create the student\'s study contract with their name, exam date, weekly rhythm (for example 5×1 h weekdays + 2×2.5 h weekend), the 3 biggest risks to their study plan, and their answers here.',
   'output': '00-study-contract.md',
   'model': ['Need: GreenBasket is losing share (18.2% → 14.1%) and visit frequency, driven by a convenience gap versus competitors', 'Assumed solutions: ShelfWise, "real-time stock", "slick app", one-lap picking rule', 'Worries: Harvest history, store resistance, unrealistic timeline, data quality'],
   'discovery': "Elena already has a vendor in mind. Spotting *solutions disguised as requirements* is one of the most tested BA instincts."}
 ],
 'extra': ["""## Set up your progress

ACTION: Update [progress.json](progress/progress.json): set `student` to the student's name, `start_date` to today, and `exam_date` to their target (or 13 weeks from today if unknown). Confirm the dates back to them.

STOP: Is the weekly rhythm in your study contract realistic for your life right now? If not, let's adjust it before week 1 gets busy.

USER: Confirms or adjusts"""],
 'takeaways': ['The CBAP tests application of BABOK v3 in scenarios. Aim for the *most BABOK-correct* answer.',
               'RADD (30%) is the biggest area. Techniques run across all KAs.',
               'Separate the **need** from the **solutions** people bring you. You did it on day one.'],
 'exam_rule': 'When a stakeholder hands you a solution, the BA move is to understand the underlying need first.',
 'reading': ['Lessing ch.1–4 (planning for success, exam format), pp.6–45: skim', 'CBAP Handbook section 6 (exam structure): already summarized in [CBAP-Roadmap.md](../CBAP-Roadmap.md)', 'Admin: join IIBA (free BABOK access), start the CBAP application, check your 35 PD hours'],
 'flashcards': ['CBAP exam length? :: 120 questions, 210 minutes', 'Largest KA by weight? :: RADD, 30%', 'CBAP eligibility hours? :: 7,500 BA hours in 10 yrs, 900 in 4 of 6 KAs, 35 PD hours, 2 references'],
 'success': ['Student knows the format and blueprint weights', 'Student knows the commands and file layout', 'progress.json has name, start date and exam date', 'workspace/00-study-contract.md exists', 'Student separated need from assumed solutions in the kickoff email'],
},
{
 'id': '1.2', 'slug': 'baccm', 'title': 'The BACCM: six lenses on every change', 'week': 1, 'minutes': 75, 'reading_min': 30, 'ka': 'FND', 'type': 'lesson',
 'teaser': 'The six core concepts that every BABOK task is built on.',
 'prepare': [F('BACCM'), CC('Change'), CC('Need'), CC('Solution'), CC('Stakeholder'), CC('Value'), CC('Context'), F('Key Terms')],
 'hook': """Every BABOK task, technique and exam scenario can be read through six words: **Change, Need, Solution, Stakeholder, Value, Context**. That's the Business Analysis Core Concept Model (BACCM).

If you can hold those six in your head, you can dissect any case study question in seconds.""",
 'objectives': ['Define all six core concepts in BABOK terms', 'Explain why no concept is more important than another', 'Apply the BACCM to a real situation', 'Use the key terms (business analysis, BA information, design, enterprise, organization, plan, requirement, risk)'],
 'teach': [
  {'title': 'The six concepts',
   'read': [F('BACCM')],
   'points': ['Change: a transformation made in response to a need. Need: a problem to solve or an opportunity to pursue. Solution: a particular way of meeting one or more needs within a context.',
              'Stakeholder: anyone (individual or group) connected to the change, the need or the solution. Value: how much something is worth, or how important or useful it is, to a stakeholder in a given context. Context: the surrounding circumstances that shape the change, are shaped by it, and help explain it.',
              'All six are **equal**, and each is defined by the others. If one changes, re-evaluate the rest.',
              'Value can be tangible or intangible, potential or realized, and absolute or relative. Losses, risks and costs are negative value.',
              'Questions to ask: what kinds of changes? what needs? what solutions? who are the stakeholders? what do they value? what contexts?'],
   'check': 'Without looking: which core concept means "how much something is worth or matters to a stakeholder in a given context", and which one means "a problem to solve or an opportunity to pursue"?',
   'expect': 'Value; Need',
   'feedback': 'exact matches. Note "within a context": value is always relative to a stakeholder and a context.',
   'trap': 'Distractors often claim one concept (usually Value or Need) is "the most important". The BABOK says they are all equal.'},
  {'title': 'Key terms that the exam uses precisely',
   'read': [F('Key Terms')],
   'points': ['Business analysis: the practice of making change happen in an enterprise by clarifying needs and proposing solutions that create value for stakeholders.',
              'Requirement = a usable representation of a **need**. Design = a usable representation of a **solution**.',
              'Business analysis information = any information, at any level of detail, used as input to or output of BA work. That is why the BABOK says "information", not just "requirements".',
              'Enterprise ≠ organization. An enterprise is one or more organizations plus the solutions they use, bounded around the change rather than around a legal entity.',
              'Risk = the effect of uncertainty on the value of a change, a solution, or the enterprise.'],
   'check': 'Is "a screen mock-up of the pickup check-in page" a requirement or a design? And "customers must be able to tell the store they have arrived"?',
   'expect': 'Mock-up = design; tell store they arrived = requirement',
   'feedback': 'the mock-up represents a solution (design); the arrival need is a requirement (it represents a need).'}
 ],
 'apply': [
  {'title': 'BACCM analysis of the Click & Collect initiative',
   'brief': 'Elena wants a one-page view of the initiative. Use the BACCM as your structure.',
   'files': [CF('01-sponsor-kickoff-email.md'), CF('04-customer-feedback-q2.md'), CF('05-market-and-sales-data.csv'), CF('02-harvest-postmortem.md')],
   'ask': 'Draft a BACCM table for Click & Collect: one or two lines per concept (Change, Need, Solution, Stakeholder, Value, Context). Try it yourself first. Rough is fine.',
   'action': 'Give specific feedback per concept, then write the polished table plus 3 "questions the BACCM raised" (e.g. whose value? which context constraints?).',
   'output': '01-baccm-click-and-collect.md',
   'model': ['Change: introduce online ordering with in-store pickup; transform store operations to support picking',
             'Need: stop share loss (18.2→14.1%) and visit-frequency decline (−11%) caused by a convenience gap',
             'Solution: Click & Collect capability (app/web ordering, picking, staging, handover), not yet a specific vendor',
             'Stakeholders: customers (personas), store ops, pickers, sponsor, CFO, IT, compliance, union, vendors',
             'Value: tangible (5% online share, basket retention) and intangible (reputation, convenience); negative value = cost, store burden, risk',
             'Context: Harvest failure, 82% inventory accuracy, union rules, alcohol and cold-chain regulation, competitor moves'],
   'review': 'elena-sponsor', 'review_focus': 'ask for a sponsor reaction to the BACCM one-pager',
   'discovery': 'The BACCM exposed that the "solution" in Elena\'s email (ShelfWise) was chosen before the context (inventory accuracy, union) was understood. That is exactly what killed Harvest.'}
 ],
 'quiz': {'n': 8, 'focus': 'BACCM definitions and application, key terms (requirement vs design, enterprise vs organization, BA information, risk)', 'ka': 'FND', 'topic': 'baccm',
          'traps': ['claiming one core concept is most important', 'confusing need with solution', 'confusing enterprise with organization', 'value only tangible'], 'mix': '5 scenario, 3 definition'},
 'takeaways': ['Six equal core concepts: Change, Need, Solution, Stakeholder, Value, Context.', 'Requirement ↔ need; design ↔ solution.', 'Value is always *to a stakeholder, within a context*, and can be negative.'],
 'exam_rule': 'If an answer option says one core concept matters more than the others, it is wrong.',
 'reading': ['BABOK ch.1 (pp.1–10) and 2.1–2.2 (pp.12–16)', 'Lessing ch.5, pp.46–55'],
 'flashcards': ['BACCM six concepts? :: Change, Need, Solution, Stakeholder, Value, Context', 'Requirement vs design? :: Requirement = usable representation of a need; design = usable representation of a solution', 'Define risk (BABOK) :: The effect of uncertainty on the value of a change, a solution, or the enterprise'],
 'success': ['Student can define all six concepts', 'Student can classify a statement as requirement vs design', 'workspace/01-baccm-click-and-collect.md created and reviewed by the sponsor agent', 'Drill completed and logged'],
},
{
 'id': '1.3', 'slug': 'requirements-classification', 'title': 'Requirements classification & requirements vs designs', 'week': 1, 'minutes': 75, 'reading_min': 30, 'ka': 'FND', 'type': 'lesson',
 'teaser': 'Business, stakeholder, solution (functional and non-functional), and transition requirements.',
 'prepare': [F('Requirements Classification Schema'), F('Requirements and Designs'), IO('Business Requirements'), TE('Non-Functional Requirements Analysis')],
 'hook': """Tom, the PM, has pasted 20 "requirements" into a spreadsheet and asked you to "sort them out". Half of them aren't requirements at all.

Today you learn the classification schema that the exam uses constantly: **business → stakeholder → solution (functional / non-functional) → transition**.""",
 'objectives': ['Classify requirements into the four BABOK types plus functional/non-functional', 'Spot designs disguised as requirements', 'Explain why transition requirements are special'],
 'teach': [
  {'title': 'The four types',
   'read': [F('Requirements Classification Schema')],
   'points': ['Business requirements: goals, objectives and outcomes. *Why* the change was initiated. They can be enterprise-wide, business-area or initiative level.',
              'Stakeholder requirements: needs of stakeholders that must be met to achieve the business requirements. The bridge between business and solution requirements.',
              'Solution requirements: capabilities and qualities of the solution. **Functional** = behaviour and information managed. **Non-functional (quality of service)** = conditions under which it must remain effective, or qualities it must have.',
              'Transition requirements: capabilities and conditions needed only to get from the current state to the future state, such as data conversion, training and business continuity. **Temporary.**'],
   'check': 'Classify these: (a) "Online sales reach 5% of total within 2 years", (b) "Store managers need to see today\'s pickup orders by slot", (c) "The pick list is sorted by aisle sequence", (d) "Pages load within 2 s for 95% of requests", (e) "Train 200 store staff before go-live".',
   'expect': 'a business, b stakeholder, c functional, d non-functional, e transition',
   'feedback': 'a = business (outcome, why); b = stakeholder (a need of a group); c = solution-functional; d = solution-non-functional; e = transition (temporary).',
   'trap': 'Training and data migration are *transition* requirements, not non-functional. And "temporary" is the tell.'},
  {'title': 'Requirements vs designs, and asking "why?"',
   'read': [F('Requirements and Designs')],
   'points': ['Requirements focus on the need; designs focus on the solution. The same techniques elicit both, and a requirement can lead to a design that uncovers more requirements.',
              'BABOK tasks that say "requirements" (e.g. Trace, Specify and Model) include designs too.',
              'Stakeholders often present a solution to an assumed need. The BA keeps asking **why** until the need is clear.',
              'Example: "Use a React Native app with ShelfWise APIs" is a design or technology choice, not a requirement.'],
   'check': 'Elena wants "real-time stock for every product". Ask "why?" twice. What need might sit underneath?',
   'expect': 'Customers must not order items that are unavailable → order accuracy / trust',
   'feedback': 'the underlying need is order accuracy and customer trust (avoid unavailable items), which could be met by other designs such as a stock-confidence indicator plus substitution preferences.'}
 ],
 'apply': [
  {'title': 'Sort Tom\'s spreadsheet',
   'brief': "Tom's draft list is a mix of goals, needs, features, designs and wishes.",
   'files': [CF('11-draft-requirements-v0.md')],
   'ask': 'Classify R-01 to R-20 by type (business / stakeholder / solution-functional / solution-NFR / transition), and mark any that are really **designs** or **not requirements at all**. Do at least 10 yourself, and I\'ll check them.',
   'action': 'Check each classification and explain disagreements. Produce a table: ID | type | design? | why | note.',
   'output': '02-requirements-classification.md',
   'model': ['R-20 "Reduce customer churn" = business requirement (too vague to be measurable yet)', 'R-03 React Native + ShelfWise = design/technology constraint, not a requirement', 'R-15 staff training and R-16 migrate phone-order customers = transition', 'R-18 availability and R-01 "fast/user-friendly" = NFR (R-01 not measurable)', 'R-05, R-09, R-10, R-12, R-14, R-17, R-19 = functional (R-19 is also a constraint from compliance)', 'R-04 one-lap rule = a design constraint from the sponsor; ask why'],
   'review': 'anil-architect', 'review_focus': 'ask which items are designs rather than requirements, and which are infeasible',
   'discovery': 'Several "High" priorities came from one person, with no link to a business objective. You will fix that properly in RLCM (prioritization) and RADD (verify and validate).'}
 ],
 'quiz': {'n': 8, 'focus': 'classifying requirements (business, stakeholder, solution-functional, solution-non-functional, transition) and requirement vs design', 'ka': 'FND', 'topic': 'req-classification',
          'traps': ['training/migration labelled non-functional', 'business requirement vs stakeholder requirement', 'design presented as requirement', 'NFR vs functional for security/audit features'], 'mix': 'mostly "classify this statement" scenarios'},
 'takeaways': ['Four types: business (why), stakeholder (needs of groups), solution (functional plus NFR), transition (temporary).', 'Requirements ↔ need; designs ↔ solution; keep asking why.', 'Designs and technology choices hide inside requirement lists. Flag them.'],
 'exam_rule': 'If it disappears once the change is complete (training, conversion, parallel run), it is a transition requirement.',
 'reading': ['BABOK 2.3 and 2.5, pp.16 and 19–20', 'Lessing ch.5 pp.59–63', 'Jonasson ch.3 pp.25–26'],
 'flashcards': ['Transition requirements? :: Temporary capabilities/conditions to move from current to future state (data conversion, training, business continuity)', 'Stakeholder requirements bridge… :: business requirements and solution requirements', 'NFR also called? :: Quality of service requirements'],
 'success': ['Student classified at least 10 of the 20 requirements correctly', 'Student identified designs inside the list', 'workspace/02-requirements-classification.md created', 'Drill completed and logged'],
},
{
 'id': '1.4', 'slug': 'stakeholder-roles', 'title': 'Stakeholders: the 11 generic roles', 'week': 1, 'minutes': 60, 'reading_min': 30, 'ka': 'FND', 'type': 'lesson',
 'teaser': 'Who is who, in BABOK terms, at GreenBasket.',
 'prepare': [F('Stakeholder Roles'), R('Sponsor'), R('Domain Subject Matter Expert'), R('Implementation Subject Matter Expert'), R('Regulator'), R('End User'), 'company-context/stakeholders/STAKEHOLDERS.md'],
 'hook': """The BABOK lists 11 generic stakeholder roles. The exam loves questions like "who should approve…?" or "which stakeholder is most likely to…?". Get the roles crisp, and a lot of questions become easy.""",
 'objectives': ['Name and define the 11 generic stakeholder roles', 'Map real people to roles (one person, many roles)', 'Distinguish domain SME and implementation SME, and sponsor and project manager'],
 'teach': [
  {'title': 'The 11 roles',
   'read': [F('Stakeholder Roles')],
   'points': ['Business analyst, customer, domain SME, end user, implementation SME, operational support, project manager, regulator, sponsor, supplier, tester.',
              'Sponsor: initiates the effort, authorizes the work, controls budget and scope. Project manager: manages the work, balancing scope, budget, schedule, resources, quality and risk.',
              'Domain SME = in-depth knowledge of the business topic or need. Implementation SME = specialized knowledge of building or implementing solution components (architect, developer, DBA, trainer, change manager…).',
              'Regulator: defines and enforces standards (legislation, governance, audit). This can be internal (e.g. compliance or audit) or external.',
              'Supplier: outside the organization, provides products or services. Operational support: day-to-day running (help desk, release manager). Tester: verifies the solution meets requirements (QA).',
              'One individual can fill several roles, and any stakeholder can be a source of requirements, assumptions or constraints.'],
   'check': 'A trainer who will teach pickers the new handheld process: which role? And the internal auditor who checks alcohol-sale logs?',
   'expect': 'Implementation SME; Regulator',
   'feedback': 'trainer = implementation SME (BABOK lists trainers and organizational change consultants there); internal auditor = regulator.',
   'trap': 'The exam often swaps sponsor and project manager. Budget and scope authority = **sponsor**.'}
 ],
 'apply': [
  {'title': 'Map GreenBasket\'s people to BABOK roles',
   'brief': 'Before you can plan stakeholder engagement (week 3), you need to know who plays which role.',
   'files': ['company-context/stakeholders/STAKEHOLDERS.md', 'company-context/COMPANY.md'],
   'ask': 'Build a table: person/group → BABOK role(s) → why. Include at least: Elena, David, Marcus, Rosa, Kim, Anil, Helen, Janet, the union, Tom, Priyanka, Dev, Lily, Ben, the customer personas, and the three vendors. Who plays more than one role?',
   'action': 'Validate the mapping, challenge any mistakes (e.g. Janet = regulator (internal); Rosa = domain SME and end-user representative; the union = not a generic BABOK role, but a stakeholder with influence, relevant to the regulator/HR context). Save the table.',
   'output': '03-stakeholder-roles.md',
   'model': ['Elena = sponsor; David = sponsor-adjacent decision maker (budget approval)', 'Marcus, Rosa, Ben, Owen, Lily, Nadia = domain SMEs; Rosa and Kim also end users', 'Anil, Helen = implementation SMEs; vendors = suppliers (and implementation SMEs during build)', 'Janet + state agencies + PCI = regulators', 'Tom = project manager; Priyanka = tester; Dev = operational support; personas = customers']}
 ],
 'quiz': {'n': 8, 'focus': 'the 11 generic stakeholder roles and their responsibilities', 'ka': 'FND', 'topic': 'stakeholder-roles',
          'traps': ['sponsor vs project manager', 'domain SME vs implementation SME', 'supplier vs customer', 'regulator only external'], 'mix': 'scenario "which role" questions'},
 'takeaways': ['11 generic roles. One person can hold several.', 'Sponsor authorizes and funds; PM manages the work.', 'Domain SME knows the business; implementation SME knows how to build it.'],
 'exam_rule': 'Budget or scope authority → sponsor. Standards enforcement (even internal) → regulator.',
 'reading': ['BABOK 2.4, pp.16–19', 'Lessing ch.5 pp.55–58'],
 'flashcards': ['Who authorizes work and controls budget/scope? :: Sponsor', 'Trainer, solution architect, DBA are… :: Implementation SMEs', 'Help desk, release manager are… :: Operational support'],
 'success': ['Student can name all 11 roles', 'workspace/03-stakeholder-roles.md created', 'Student correctly separated sponsor/PM and domain/implementation SME', 'Drill completed and logged'],
},
{
 'id': '1.5', 'slug': 'task-anatomy', 'title': 'Anatomy of a BABOK task & how to study the Guide', 'week': 1, 'minutes': 90, 'reading_min': 60, 'ka': 'FND', 'type': 'lesson',
 'teaser': 'The 8-part structure behind all 30 tasks, and how to read the BABOK efficiently.',
 'prepare': [T('Plan Business Analysis Approach'), KA('Business Analysis Planning and Monitoring'), 'CBAP Knowledge Graph/00 CBAP Knowledge Graph.md', EX('Technique-Task Matrix')],
 'hook': """All 30 BABOK tasks share one skeleton: **Purpose, Description, Inputs, Elements, Guidelines & Tools, Techniques, Stakeholders, Outputs.** Once you see it, the 500-page guide becomes a well-organized database. It's also how your knowledge graph is built.""",
 'objectives': ['Name the 8 parts of every task and what each tells you', 'Tell inputs apart from guidelines and tools', 'Navigate the knowledge graph and the BABOK efficiently', 'Know the 6 KAs, their 30 tasks and the order they are usually studied in'],
 'teach': [
  {'title': 'The task skeleton',
   'read': [T('Plan Business Analysis Approach')],
   'points': ['Purpose: why the task exists. Memorize one sentence per task; exam options paraphrase it.',
              'Inputs: information *consumed and transformed* by the task (often with a state, e.g. "Requirements (verified)"). Outputs: what the task *produces*.',
              'Guidelines and tools: information that *shapes* how the task is done but isn\'t transformed (e.g. the Business Analysis Approach guides many tasks).',
              'Elements: the key concepts or activities of the task. Techniques: *how* you might do it. Stakeholders: who typically takes part.',
              'The BABOK is not a sequential process. Tasks can be done in any order, iteratively and concurrently.'],
   'check': 'In Plan Business Analysis Approach, "Needs" is an input and "Business Analysis Performance Assessment" is a guideline. What is the difference in plain words?',
   'expect': 'Input is what the task works on; guideline influences how it is done',
   'feedback': 'inputs are transformed into outputs; guidelines and tools inform or constrain the work without being transformed.',
   'trap': 'Questions ask "which is an INPUT to task X?" and list guidelines as distractors.'},
  {'title': 'Map of the territory',
   'read': [EX('Technique-Task Matrix')],
   'points': ['6 KAs and 30 tasks: BAPM (5), E&C (5), RLCM (5), SA (4), RADD (6), SE (5).',
              'KAs are *not* phases. For example, Strategy Analysis can happen before, during and after a project.',
              '50 techniques. Some are used everywhere (Interviews, Workshops, Document Analysis, Risk Analysis and Management), others in only one or two tasks.',
              'Perspectives (Agile, BI, IT, Business Architecture, BPM) are lenses. Underlying competencies are the BA\'s skills.',
              'Study method: for each task, know the purpose, element names, inputs and outputs (with states), 3–5 signature techniques, and key stakeholders.'],
   'check': 'Which KA has only 4 tasks, and which has 6?',
   'expect': 'SA has 4, RADD has 6',
   'feedback': 'SA = 4 (Analyze Current State, Define Future State, Assess Risks, Define Change Strategy); RADD = 6.'}
 ],
 'apply': [
  {'title': 'Build your one-page task card template',
   'brief': 'You will fill one task card per task over the next weeks. They are your revision sheets for weeks 11–13.',
   'files': [T('Plan Business Analysis Approach')],
   'ask': 'Using the Plan Business Analysis Approach note, fill in a task card: purpose (in your own words), elements, inputs, guidelines, top 5 techniques, stakeholders, outputs, and "who uses my output next". What surprised you?',
   'action': 'Check the card against the note, correct any wrong names, and save it as the first card. Include a blank template at the top of the file for future cards.',
   'output': 'task-cards.md',
   'model': ['Purpose (in our words): Decide how business analysis will be carried out on this initiative: the overall method, its formality, the activities, their timing, and how the approach gets agreed.', 'Elements: planning approach, formality and level of detail, BA activities, timing, complexity and risk, acceptance', 'Input: Needs; output: Business Analysis Approach, used by 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.4, 4.5, 6.1…']}
 ],
 'quiz': {'n': 8, 'focus': 'task structure (inputs vs guidelines vs outputs), KA/task counts, BABOK as non-sequential, perspectives and competencies as concepts', 'ka': 'FND', 'topic': 'babok-structure',
          'traps': ['guideline listed as input', 'KAs treated as sequential phases', 'wrong task-to-KA mapping']},
 'takeaways': ['Every task: purpose, description, inputs, elements, guidelines and tools, techniques, stakeholders, outputs.', 'Inputs are transformed; guidelines shape the work.', 'KAs are not phases. Tasks are iterative and concurrent.'],
 'exam_rule': 'Know each output\'s *state label*. It often decides between two otherwise-good options.',
 'reading': ['BABOK 1.4 Structure (pp.3–10)', 'Lessing ch.3 Study Tools (pp.31–40)', 'Jonasson ch.2–3 (pp.11–31): skim for context'],
 'flashcards': ['Eight parts of every BABOK task? :: Purpose, Description, Inputs, Elements, Guidelines and Tools, Techniques, Stakeholders, Outputs', 'Tasks per KA? :: BAPM 5, E&C 5, RLCM 5, SA 4, RADD 6, SE 5', 'Are KAs sequential phases? :: No, tasks can be performed in any order, iteratively and concurrently'],
 'success': ['Student can name the 8 task parts', 'Student distinguishes input from guideline', 'workspace/task-cards.md created with template plus the 3.1 card', 'Drill completed and logged'],
},
{
 'id': '1.6', 'slug': 'diagnostic-exam', 'title': 'Diagnostic exam (50 questions)', 'week': 2, 'minutes': 100, 'reading_min': 0, 'ka': 'ALL', 'type': 'exam',
 'teaser': 'Find your baseline. No pressure, no studying for it.',
 'prepare': [EX('Exam Blueprint'), EX('Commonly Confused Concepts'), EX('BABOK Input-Output Flow')],
 'hook': """Today is about data, not ego. A 50-question diagnostic across all KAs shows where you start. Most people score 45–60% before studying, and that's normal.

Treat it like the real thing: timed (75 minutes), no notes, and honest guesses marked with a "?".""",
 'objectives': ['Establish a baseline score by KA', 'Practise exam pacing (about 1.5 min per question)', 'Start the error log with real data'],
 'ready': 'Do you have 75 uninterrupted minutes now? If not, we can generate the exam and you take it later.',
 'extra': ["""## Generate the exam

ACTION: Read the knowledge-graph notes you need (KA notes, the Commonly Confused Concepts note, and the I/O Flow note), then write **50 original CBAP-style questions** to `exams/diagnostic.md`:
- Distribution by blueprint: RADD 15, RLCM 8, SA 7, BAPM 7, SE 7, E&C 6.
- Mix: about 60% scenario-based (including one mini case study with 4 linked questions), 20% "which input/output/technique", 20% definitions and concepts.
- Each question: number, KA tag hidden (don't show the KA to the student), 4 options A–D, exactly one best answer.
- Write the key to `exams/.keys/diagnostic-key.md`: number | answer | KA | task/technique | type | 2-line rationale | knowledge-graph note path.
- Create `exams/diagnostic-answers.md` with lines `1: ` … `50: ` for the student to fill in (letter, plus `?` if guessing).

Tell the student the exam is ready and link [diagnostic.md](exams/diagnostic.md) and [diagnostic-answers.md](exams/diagnostic-answers.md). **Don't open the key file or reveal answers.**

STOP: Start your 75-minute timer. Answer in diagnostic-answers.md, add `?` to guesses, and tell me when you're done.

USER: Done

ACTION: Run the same procedure as the `/grade diagnostic` command: score it, write `exams/diagnostic-report.md`, and append misses to the error log and per-KA rows to scores.csv.""",
 """## Debrief

Share the headline: total %, by-KA table, and time used. Normalize the result: a baseline is a starting point, not a verdict.

STOP: Looking at your by-KA scores, which result surprised you most?

USER: Responds

ACTION: Point out the two weakest KAs and the most common confusion pattern. Note them in progress.json `weak_topics`. Tell them lesson 1.7 will turn this into a personal focus plan."""],
 'takeaways': ['You now have a baseline by KA.', 'Guesses count as misses in the error log. That\'s where learning happens.', 'Pacing target: about 1:45 per question on the real exam.'],
 'exam_rule': 'On test day, flag and move on after 2 minutes. Never burn 5 minutes on one question.',
 'success': ['exams/diagnostic.md and answers exist', 'Diagnostic graded; report written', 'Error log and scores.csv populated', 'Weak KAs recorded in progress.json'],
},
{
 'id': '1.7', 'slug': 'diagnostic-review', 'title': 'Diagnostic review & your personal focus plan', 'week': 2, 'minutes': 75, 'reading_min': 30, 'ka': 'ALL', 'type': 'review',
 'teaser': 'Turn your diagnostic into a personal plan.',
 'prepare': ['progress/error-log.md', 'progress/scores.csv', EX('Commonly Confused Concepts')],
 'prepare_note': 'Also read `exams/diagnostic-report.md` if it exists.',
 'hook': """Your diagnostic misses are the most valuable data you have. Today we sort them into **knowledge gaps**, **confusions** and **misreads**, because each needs a different fix.""",
 'objectives': ['Classify errors by root cause', 'Learn the 14 most commonly confused BABOK pairs', 'Adjust the study plan to your weak spots'],
 'teach': [
  {'title': 'Three kinds of wrong',
   'points': ['Knowledge gap: you didn\'t know the fact (e.g. which task outputs Solution Scope). Fix: study plus flashcards.',
              'Confusion: you mixed up two similar concepts (verify/validate, solution/enterprise limitation). Fix: contrast tables.',
              'Misread or over-thinking: you knew it but answered from "real life" or missed a word like FIRST, BEST, NOT. Fix: exam technique.',
              'BABOK answers beat real-life answers. The exam asks what the BABOK says a BA should do.'],
   'check': 'Look at your error log: which of the three types dominates for you?',
   'expect': 'Names a type'},
  {'title': 'The confusion hit-list',
   'read': [EX('Commonly Confused Concepts')],
   'points': ['Walk through the pairs most relevant to the student\'s misses (verify vs validate, confirm vs verify, solution vs enterprise limitation, change strategy vs solution scope, business requirements vs business objectives, focus groups vs workshops…).',
              'For each pair: a one-line distinction and a GreenBasket example.'],
   'check': 'Quick-fire: I describe a situation and you name which side of the pair it is. Ready?',
   'expect': 'Ready',
   'feedback': 'run 5 rapid quick-fire items drawn from the student\'s confused pairs, answered in chat.'}
 ],
 'apply': [
  {'title': 'Your personal focus plan',
   'brief': 'Combine the diagnostic data with the 13-week plan.',
   'files': ['progress/error-log.md', '../CBAP-Roadmap.md'],
   'ask': 'Tell me: your 2 weakest KAs, your top 3 confusions, and how many extra minutes per week you could give those areas.',
   'action': 'Write a focus plan: baseline table, target by week 9 (≥75% per KA) and week 12 (≥80% on a mock), the extra drills to add (e.g. `/drill RADD 10` every Sunday), and which lessons deserve extra time. Update `weak_topics` in progress.json.',
   'output': '04-personal-focus-plan.md'}
 ],
 'quiz': {'n': 8, 'focus': "re-test of the student's diagnostic misses with fresh questions on the same concepts", 'ka': 'ALL', 'topic': 'diagnostic-retest'},
 'takeaways': ['Diagnose *why* you missed, not just *what*.', 'Contrast pairs kill confusion errors.', 'BABOK logic beats real-life habit in exam answers.'],
 'exam_rule': 'Underline FIRST / BEST / MOST / NOT / EXCEPT in every question stem.',
 'reading': ['Lessing ch.4 What to Expect From the Exam (pp.41–45)', 'Review the Commonly Confused Concepts note once more'],
 'success': ['Errors classified by type', 'workspace/04-personal-focus-plan.md created', 'weak_topics updated', 'Re-test drill logged'],
},
{
 'id': '1.8', 'slug': 'io-backbone', 'title': 'The big map: how the 30 tasks hand off to each other', 'week': 2, 'minutes': 90, 'reading_min': 30, 'ka': 'FND', 'type': 'lesson',
 'teaser': 'The input/output backbone that answers "what comes next?" questions.',
 'prepare': [EX('BABOK Input-Output Flow'), IO('Requirements'), IO('Elicitation Results'), IO('Business Analysis Approach'), IO('Change Strategy'), IO('Solution Scope')],
 'hook': """Many exam questions are secretly asking: *"Which task produced this, and which task uses it next?"* Today you learn the backbone: the 38 formal handoffs between tasks and the "state" labels that travel with requirements.""",
 'objectives': ['Trace the main input/output chains across KAs', 'Know the requirement and elicitation-result states', 'Recognize the "hub" outputs that guide many tasks'],
 'teach': [
  {'title': 'The hub outputs',
   'read': [IO('Business Analysis Approach'), IO('Change Strategy'), IO('Solution Scope')],
   'points': ['BAPM outputs (Business Analysis Approach, Stakeholder Engagement Approach, Governance Approach, Information Management Approach, BA Performance Assessment) guide almost everything else.',
              'Strategy Analysis outputs (Current State Description, Future State Description, Business Objectives, Potential Value, Risk Analysis Results, Change Strategy, Solution Scope) guide RADD and SE.',
              'Needs enter from outside (3.1, 3.2, 4.1, 6.1). "(external)" inputs: Performance Objectives (3.5) and Implemented Solution (8.1, 8.3, 8.4).'],
   'check': 'Which task produces Solution Scope, and name two tasks that use it?',
   'expect': '6.4 Define Change Strategy; e.g. 7.1, 7.3, 7.4, 7.5…',
   'feedback': 'produced by 6.4 Define Change Strategy (together with Change Strategy); used as input by 7.4 and as a guideline by many tasks (5.3, 5.4, 5.5, 7.1, 7.3, 7.5, 7.6, 8.x).'},
  {'title': 'The state chains',
   'read': [IO('Requirements'), IO('Elicitation Results')],
   'points': ['Elicitation Results: 4.2 → **unconfirmed**, 4.3 → **confirmed**, 7.1 accepts **any state**.',
              'Requirements: 7.1 → **specified and modelled** → 7.2 **verified** → 5.5 approves **verified** requirements. 7.3 → **validated**. 7.5 uses **validated, prioritized** requirements. 5.1 → traced, 5.2 → maintained, 5.3 → prioritized, 5.5 → approved.',
              'Designs follow the same RLCM states (traced, maintained, prioritized, approved).',
              'Solution Evaluation chain: 8.1 Solution Performance Measures → 8.2 Solution Performance Analysis → 8.3 Solution Limitation and 8.4 Enterprise Limitation → 8.5 Recommended Actions.'],
   'check': 'Approve Requirements needs requirements in which state: validated or verified?',
   'expect': 'Verified',
   'feedback': 'verified: approval follows quality checking. Validated requirements feed design options.',
   'trap': 'Swapping "verified" and "validated" in the input of Approve Requirements is a classic distractor.'}
 ],
 'apply': [
  {'title': 'Draw the backbone from memory',
   'brief': 'Recall beats re-reading. Build the map without looking, then compare it with the graph note.',
   'files': [EX('BABOK Input-Output Flow')],
   'ask': 'Without opening the note: list as many "task → output → next task" handoffs as you can in 10 minutes. Aim for 15 or more.',
   'action': 'Compare with the I/O Flow note: count correct ones, list the missing and wrong ones, and save a personal "handoff map" with a Mermaid diagram of the main chain (BAPM approaches → E&C results → SA outputs → RADD states → RLCM states → SE chain). Mark the ones they missed with ⚠️.',
   'output': '05-my-io-backbone.md',
   'discovery': 'Most people forget that Business Requirements come out of **Analyze Current State**, not Define Future State. Did you?'}
 ],
 'quiz': {'n': 10, 'focus': 'input/output handoffs, state labels, which task produces or consumes a given output', 'ka': 'FND', 'topic': 'io-flow',
          'traps': ['verified vs validated as input to Approve', 'Business Requirements produced by Define Future State', 'Solution Scope produced by RADD', 'Elicitation Results (confirmed) produced by Conduct Elicitation']},
 'takeaways': ['BAPM approaches and SA outputs are hub guidelines.', 'Know the states: unconfirmed → confirmed; specified and modelled → verified / validated → prioritized → approved.', 'The SE chain: measures → analysis → limitations → recommended actions.'],
 'exam_rule': '"What should the BA do next?" means: find which task consumes the output you currently have.',
 'reading': ['BABOK input/output diagrams at the start of each KA chapter (3.0, 4.0, 5.0, 6.0, 7.0, 8.0): study the figures only', 'Appendix B Techniques to Task Mapping (p.457): skim'],
 'flashcards': ['Business Requirements are output by… :: 6.1 Analyze Current State', 'Approve Requirements input state? :: Requirements (verified)', 'Define Change Strategy outputs? :: Change Strategy and Solution Scope', 'Define Design Options input requirements state? :: Requirements (validated, prioritized)'],
 'success': ['Student recalled at least 15 handoffs', 'workspace/05-my-io-backbone.md created with a Mermaid chain', 'Student knows the requirement state chain', 'Drill logged'],
},
{
 'id': '1.9', 'slug': 'competencies-perspectives-primer', 'title': 'Underlying competencies & perspectives: a primer', 'week': 2, 'minutes': 60, 'reading_min': 45, 'ka': 'COMP', 'type': 'lesson',
 'teaser': 'The skills and lenses that frame every scenario.',
 'prepare': [UC('Underlying Competencies'), UC('Analytical Thinking and Problem Solving'), UC('Interaction Skills'), P('Perspectives'), P('The Agile Perspective')],
 'hook': """Case studies often hide a competency question ("the BA is demonstrating…") or a perspective ("in an agile context, the BA should…"). Today is a primer. We go deep in week 10.""",
 'objectives': ['Name the 6 competency groups and a few competencies in each', 'Explain what a perspective is and name the 5', 'Recognize competency and perspective cues in scenarios'],
 'teach': [
  {'title': 'Underlying competencies',
   'read': [UC('Underlying Competencies')],
   'points': ['Six groups: Analytical Thinking and Problem Solving (creative, decision making, learning, problem solving, systems, conceptual, visual thinking), Behavioural Characteristics (ethics, personal accountability, trustworthiness, organization and time management, adaptability), Business Knowledge (business acumen, industry, organization, solution, methodology), Communication Skills (verbal, non-verbal, written, listening), Interaction Skills (facilitation, leadership and influencing, teamwork, negotiation and conflict resolution, teaching), Tools and Technology (office productivity, BA tools, communication tools).',
              'Each competency has a purpose, a definition and effectiveness measures.',
              'Systems thinking = the whole and how the parts interact. Conceptual thinking = fitting details into the bigger picture and connecting seemingly unrelated information.'],
   'check': 'Rosa tells you about a workaround in her store, and you immediately see how it will affect pick accuracy, customer trust and store labour budgets. Which competency is that?',
   'expect': 'Systems thinking',
   'feedback': 'systems thinking: understanding how changing one component affects the whole system.'},
  {'title': 'Perspectives',
   'read': [P('Perspectives')],
   'points': ['A perspective is a lens for BA work in a specific context: Agile, Business Intelligence, Information Technology, Business Architecture, Business Process Management.',
              'Each describes change scope, BA scope, methodologies, underlying competencies, and impact on KAs.',
              'Agile: continuous, just-in-time elaboration, backlog, short iterations. BI: data to insight. IT: impact on systems. BA (business architecture): enterprise models. BPM: process improvement.'],
   'check': 'GreenBasket\'s pilot team works in 2-week sprints from a backlog. Which perspective frames that, and how does it change *when* requirements are elaborated?',
   'expect': 'Agile; just-in-time, when needed',
   'feedback': 'Agile perspective: requirements elaborated just in time, prioritized backlog, continuous planning.'}
 ],
 'quiz': {'n': 8, 'focus': 'identifying competencies from behaviours and matching perspectives to contexts', 'ka': 'COMP', 'topic': 'competency-perspective-primer',
          'traps': ['systems vs conceptual thinking', 'facilitation vs leadership', 'business acumen vs industry knowledge', 'BPM vs business architecture perspective']},
 'takeaways': ['6 competency groups. Know the names and one example behaviour each.', '5 perspectives are lenses, not methods.', 'Scenario verbs ("facilitated", "negotiated", "visualized") hint at the competency.'],
 'reading': ['BABOK ch.9 intro plus 9.1 (pp.185–193)', 'BABOK ch.11 intro (p.367): skim each perspective\'s first page', 'Jonasson 3.4–3.5 (pp.26–31)'],
 'flashcards': ['6 underlying competency groups? :: Analytical Thinking & Problem Solving; Behavioural Characteristics; Business Knowledge; Communication Skills; Interaction Skills; Tools & Technology', '5 perspectives? :: Agile, Business Intelligence, Information Technology, Business Architecture, Business Process Management'],
 'success': ['Student can name the 6 competency groups', 'Student can name the 5 perspectives', 'Drill logged'],
},
{
 'id': '1.10', 'slug': 'foundation-checkpoint', 'title': 'Foundation checkpoint', 'week': 2, 'minutes': 60, 'reading_min': 15, 'ka': 'FND', 'type': 'drill',
 'teaser': 'Lock in the foundations before Knowledge Area deep dives.',
 'prepare': [F('BACCM'), F('Requirements Classification Schema'), F('Stakeholder Roles'), EX('BABOK Input-Output Flow')],
 'hook': """Checkpoint time. 20 questions covering everything from weeks 1–2. Pass at 75% and you're ready for the Knowledge Areas. Below that, we patch the gaps first.""",
 'objectives': ['Confirm mastery of the foundations', 'Close any foundation gaps before week 3'],
 'quiz': {'n': 20, 'focus': 'BACCM, key terms, requirements classification, stakeholder roles, task anatomy, I/O backbone and states, competency and perspective basics', 'ka': 'FND', 'topic': 'foundation-checkpoint',
          'mix': '12 scenario, 8 definition/flow'},
 'extra': ["""## Milestone review

ACTION: Read [progress.json](progress/progress.json), [scores.csv](progress/scores.csv) and [00-study-contract.md](workspace/00-study-contract.md). Summarize weeks 1–2: lessons done, average drill score, error-log size, and whether the Phase 1 milestones are met (diagnostic done, flow map drafted, CBAP application started).

STOP: Did you start your CBAP application and IIBA membership? (Admin tasks tend to slip.)

USER: Responds

[If the checkpoint is under 75%: pick the 2 weakest foundation topics, re-teach each in 3 lines, and run 4 fresh questions before moving on.]"""],
 'takeaways': ['Foundations are in place: concepts, classification, roles, structure, flow.', 'From next week, each KA gets a full week, and RADD gets two.'],
 'exam_rule': 'Come back to the I/O backbone every week. It connects everything you will learn.',
 'reading': ['BABOK ch.3 intro (pp.21–23) before lesson 2.1'],
 'success': ['Checkpoint of 20 questions completed and logged', 'Milestone review done', 'Gaps remediated if under 75%'],
},
]}
