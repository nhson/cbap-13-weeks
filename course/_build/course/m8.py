from render import T, TE, KA, IO, F, CC, R, UC, P, EX, CF

MODULE = {'id': '8', 'name': 'Consolidation: techniques, perspectives, competencies', 'weeks': '10',
          'description': 'All 50 techniques compared in families, the 5 perspectives, and the underlying competencies. Plus the technique matrix you will revise from in weeks 11–13.',
          'lessons': [
{
 'id': '8.1', 'slug': 'techniques-collaboration', 'title': 'Technique families I: elicitation & collaboration techniques', 'week': 10, 'minutes': 80, 'reading_min': 15, 'ka': 'TECH', 'type': 'review',
 'teaser': 'Compare the look-alikes: interviews, workshops, focus groups, surveys, observation, brainstorming, collaborative games, document analysis, reviews, lessons learned.',
 'prepare': [EX('Technique-Task Matrix'), TE('Interviews'), TE('Workshops'), TE('Focus Groups'), TE('Survey or Questionnaire'), TE('Observation'), TE('Brainstorming'), TE('Collaborative Games'), TE('Document Analysis'), TE('Reviews'), TE('Lessons Learned')],
 'hook': """Week 10: consolidation. The exam doesn't ask "define workshops". It asks "*which* technique fits this situation?". Today we compare the people-facing techniques side by side, then build your master technique sheet.""",
 'objectives': ['Compare 10 collaboration techniques on purpose, group size, output and limitations', 'Answer "which technique" questions fast'],
 'teach': [
  {'title': 'Side-by-side',
   'points': ['Walk through each technique in 2 lines: purpose + the scenario cue that selects it + one limitation. Use the technique notes.',
              'Key cues: consensus/decision → workshop; opinions/attitudes → focus group; many/dispersed → survey; tacit/workarounds → observation; ideas volume → brainstorming; engagement/creativity → collaborative games; existing materials → document analysis; quality check → reviews; improve process → lessons learned.'],
   'check': 'Rapid-fire: I\'ll give 6 cues and you name the technique. Ready?',
   'expect': 'Ready',
   'feedback': 'run 6 quick cues in chat and correct them instantly.'}
 ],
 'apply': [
  {'title': 'Master technique sheet, part 1',
   'brief': 'Your one-page revision sheet for weeks 11–13.',
   'files': [EX('Technique-Task Matrix')],
   'ask': 'For these 10 techniques, give me purpose (≤10 words), selection cue, main limitation, and the KAs where they are used most. I\'ll check it.',
   'action': 'Check against the technique notes (esp. task usage counts from the matrix) and save as part 1 of the master sheet.',
   'output': '70-master-technique-sheet.md'}
 ],
 'quiz': {'n': 12, 'focus': 'selecting between elicitation/collaboration techniques in scenarios; strengths and limitations', 'ka': 'TECH', 'topic': 'tech-family-collab'},
 'takeaways': ['Scenario cues pick the technique.', 'Know one limitation per technique; distractors exploit them.'],
 'reading': ['Lessing ch.13 (pp.348–396): skim the "When should you apply this technique?" tables'],
 'success': ['Master sheet part 1 created', 'Drill logged'],
},
{
 'id': '8.2', 'slug': 'techniques-modelling', 'title': 'Technique families II: modelling techniques', 'week': 10, 'minutes': 80, 'reading_min': 15, 'ka': 'TECH', 'type': 'review',
 'teaser': 'Process, use case, user story, sequence, state, data, DFD, concept, decision, scope, org, roles & permissions, functional decomposition, prototyping.',
 'prepare': [TE('Process Modelling'), TE('Use Cases and Scenarios'), TE('User Stories'), TE('Sequence Diagrams'), TE('State Modelling'), TE('Data Modelling'), TE('Data Flow Diagrams'), TE('Concept Modelling'), TE('Decision Modelling'), TE('Scope Modelling'), TE('Organizational Modelling'), TE('Roles and Permissions Matrix'), TE('Functional Decomposition'), TE('Prototyping'), TE('Mind Mapping')],
 'hook': """Fifteen modelling techniques, five categories. Today: the fastest way to tell them apart, "what does this model *show*?".""",
 'objectives': ['Map each modelling technique to its category and what it shows', 'Pick the right model for a question stem'],
 'teach': [
  {'title': 'What does it show?',
   'points': ['Process = sequence of activities; use case = actor-goal interaction with the system; user story = small valuable need; sequence = messages between objects over time; state = entity life cycle; data model = entities and relationships; DFD = data movement and transformation; concept model = business vocabulary; decision model = repeatable decision logic; scope model = boundaries; org model = structure and reporting; roles and permissions = who may do what; functional decomposition = breakdown of parts; prototype = early representation; mind map = non-linear idea structure.',
              'Categories: People & Roles, Rationale, Activity Flow, Capability, Data & Information.'],
   'check': 'Which model shows how the "Order" changes status from Placed to Collected?',
   'expect': 'State model',
   'feedback': 'state model (Data & Information category).'}
 ],
 'apply': [
  {'title': 'Master technique sheet, part 2',
   'brief': 'Add the modelling techniques.',
   'files': [EX('Technique-Task Matrix')],
   'ask': 'For the 15 modelling techniques: what it shows, model category, and a typical exam cue.',
   'action': 'Check and append to the master sheet.',
   'output': '70-master-technique-sheet.md'}
 ],
 'quiz': {'n': 12, 'focus': 'choosing the right model; model categories; distinguishing look-alike models', 'ka': 'TECH', 'topic': 'tech-family-models'},
 'takeaways': ['Ask "what does it show?" to pick the model.', 'Know each model\'s category.'],
 'reading': ['Lessing ch.14 (pp.397–441): skim'],
 'success': ['Master sheet part 2 appended', 'Drill logged'],
},
{
 'id': '8.3', 'slug': 'techniques-analysis-decision', 'title': 'Technique families III: analysis, decision & estimation techniques', 'week': 10, 'minutes': 75, 'reading_min': 15, 'ka': 'TECH', 'type': 'review',
 'teaser': 'Decision analysis, risk, financial, prioritization, estimation, business rules, NFR, interface, acceptance criteria, item tracking, backlog, glossary, data dictionary.',
 'prepare': [TE('Decision Analysis'), TE('Risk Analysis and Management'), TE('Financial Analysis'), TE('Prioritization'), TE('Estimation'), TE('Business Rules Analysis'), TE('Non-Functional Requirements Analysis'), TE('Interface Analysis'), TE('Acceptance and Evaluation Criteria'), TE('Item Tracking'), TE('Backlog Management'), TE('Glossary'), TE('Data Dictionary')],
 'hook': """The analytical toolkit: how BAs decide, quantify and control. These show up across nearly every KA.""",
 'objectives': ['Compare analytical and decision techniques', 'Recall key formulas and lists (PERT, NPV, risk responses, bases of prioritization)'],
 'teach': [
  {'title': 'Toolkit review',
   'points': ['Decision analysis (alternatives under uncertainty) vs decision modelling (repeatable decisions) vs business rules analysis (individual rules).',
              'Risk: likelihood × impact; avoid, transfer, mitigate, accept, increase. Financial: ROI, payback, NPV, IRR, TCO. Estimation: PERT (O+4M+P)/6, Delphi, analogous, bottom-up, top-down, rolling wave, parametric.',
              'Prioritization: grouping, ranking, time boxing/budgeting, negotiation. Backlog: prioritized, progressively elaborated.',
              'Glossary (terms) vs data dictionary (data elements). Acceptance (one, pass/fail) vs evaluation (rank many). Item tracking (issues to closure).'],
   'check': 'Three-point estimate: O=4, M=6, P=14 days. PERT?',
   'expect': '7 days',
   'feedback': '(4 + 24 + 14) / 6 = 7.'}
 ],
 'apply': [
  {'title': 'Master technique sheet, part 3',
   'brief': 'Add the analytical techniques and formulas.',
   'files': [EX('Technique-Task Matrix')],
   'ask': 'Add these 13 techniques with purpose, cue, limitation, plus a formulas box.',
   'action': 'Check and append.',
   'output': '70-master-technique-sheet.md'}
 ],
 'quiz': {'n': 12, 'focus': 'analytical, decision and estimation techniques incl. 3 short calculations', 'ka': 'TECH', 'topic': 'tech-family-analysis'},
 'takeaways': ['Decision analysis ≠ decision modelling ≠ business rules analysis.', 'Formulas: PERT, ROI, NPV, EV.'],
 'success': ['Master sheet part 3 appended', 'Drill logged'],
},
{
 'id': '8.4', 'slug': 'techniques-strategy-measurement', 'title': 'Technique families IV: strategy & measurement techniques', 'week': 10, 'minutes': 70, 'reading_min': 10, 'ka': 'TECH', 'type': 'review',
 'teaser': 'SWOT, BMC, business capability analysis, business cases, balanced scorecard, benchmarking, metrics & KPIs, data mining, root cause, process analysis, vendor assessment, stakeholder list/map/personas.',
 'prepare': [TE('SWOT Analysis'), TE('Business Model Canvas'), TE('Business Capability Analysis'), TE('Business Cases'), TE('Balanced Scorecard'), TE('Benchmarking and Market Analysis'), TE('Metrics and Key Performance Indicators (KPIs)'), TE('Data Mining'), TE('Root Cause Analysis'), TE('Process Analysis'), TE('Vendor Assessment'), TE('Stakeholder List, Map, or Personas')],
 'hook': """The last 12 techniques: strategy and measurement. After today, your master sheet covers all 50.""",
 'objectives': ['Compare strategy and measurement techniques', 'Complete the 50-technique master sheet'],
 'teach': [
  {'title': 'Toolkit review',
   'points': ['SWOT (internal S/W, external O/T); BMC (9 blocks); capability analysis (what, not how; gaps and hot spots); business case (need, outcomes, alternatives, recommendation); balanced scorecard (4 perspectives); benchmarking vs market analysis.',
              'Metrics and KPIs (indicator, metric, KPI); data mining (descriptive, diagnostic, predictive); root cause (fishbone, 5 whys); process analysis (gaps, waste, Lean, Six Sigma, SIPOC, value stream); vendor assessment criteria; stakeholder matrix, onion, RACI, personas.'],
   'check': 'Process analysis vs process modelling: what\'s the difference?',
   'expect': 'Analysis assesses efficiency/effectiveness; modelling represents the process',
   'feedback': 'modelling *represents* the process; analysis *assesses* it for efficiency and effectiveness and finds improvement opportunities.'}
 ],
 'apply': [
  {'title': 'Master technique sheet, part 4 + self-test',
   'brief': 'Finish the sheet.',
   'files': [EX('Technique-Task Matrix')],
   'ask': 'Add the last 12 techniques. Then, without looking, name all 50 techniques. How many can you recall?',
   'action': 'Check, append, and record the recall count (target: 45 or more) in the sheet header.',
   'output': '70-master-technique-sheet.md'}
 ],
 'quiz': {'n': 12, 'focus': 'strategy and measurement techniques, process analysis vs modelling', 'ka': 'TECH', 'topic': 'tech-family-strategy'},
 'takeaways': ['All 50 techniques are on one sheet: your revision backbone.'],
 'success': ['Master sheet complete (50 techniques)', 'Recall count recorded', 'Drill logged'],
},
{
 'id': '8.5', 'slug': 'perspectives-agile-bi-it', 'title': 'Perspectives I: Agile, Business Intelligence, Information Technology', 'week': 10, 'minutes': 75, 'reading_min': 30, 'ka': 'PERSP', 'type': 'lesson',
 'teaser': 'How BA work shifts in agile, BI and IT contexts.',
 'prepare': [P('Perspectives'), P('The Agile Perspective'), P('The Business Intelligence Perspective'), P('The Information Technology Perspective')],
 'hook': """Case studies often set the scene: "an agile team…", "a data warehouse initiative…", "a legacy system replacement…". The perspective changes what the *best* answer is.""",
 'objectives': ['Explain each perspective\'s change scope, BA scope, approaches and impact on KAs', 'Adjust answers to the perspective context'],
 'teach': [
  {'title': 'Agile',
   'read': [P('The Agile Perspective')],
   'points': ['Mindset of values and principles; short iterations; continuous, just-in-time elaboration; the BA works with the product owner and team.',
              'Approaches: Crystal Clear, DAD, DSDM, Evo, XP, FDD, Kanban, SAFe, Scrum. Techniques: BDD, Kano, lightweight documentation, MoSCoW, personas, planning workshop, purpose alignment model, real options, relative estimation, retrospectives, story decomposition, story mapping, storyboarding, value stream mapping.',
              'Impact on KAs: planning is continuous; elicitation is ongoing; the backlog replaces formal requirement documents; SE is frequent.'],
   'check': 'In an agile context, when are detailed requirements elaborated?',
   'expect': 'Just in time, close to implementation',
   'feedback': 'just in time: detail is added as items near the top of the backlog.'},
  {'title': 'BI and IT',
   'read': [P('The Business Intelligence Perspective'), P('The Information Technology Perspective')],
   'points': ['BI: transform data into value-added information. Analytics types: descriptive, predictive, prescriptive; supply-driven vs demand-driven; structured vs unstructured data; the focus is on decisions supported.',
              'IT: impact of change on IT systems, from small enhancements to large implementations; methodologies (predictive/adaptive; RE, SSADM, UP); strong on NFRs, interfaces and data.'],
   'check': 'A BI project starts from "what decisions do managers need to make?". Supply-driven or demand-driven?',
   'expect': 'Demand-driven',
   'feedback': 'demand-driven: starts from information needs and decisions.'}
 ],
 'quiz': {'n': 10, 'focus': 'Agile, BI and IT perspectives: scope, methods, techniques, impact on KAs', 'ka': 'PERSP', 'topic': 'persp-1'},
 'takeaways': ['A perspective shifts the best answer: agile = just in time; BI = decisions and data; IT = systems impact.'],
 'reading': ['BABOK 11.1–11.3 (pp.368–407): read the "Impact on Knowledge Areas" sections closely'],
 'flashcards': ['BI analytics types? :: Descriptive, predictive, prescriptive', 'Supply- vs demand-driven BI? :: Supply = start from available data; demand = start from information needs/decisions'],
 'success': ['Student distinguishes the three perspectives', 'Drill logged'],
},
{
 'id': '8.6', 'slug': 'perspectives-ba-bpm', 'title': 'Perspectives II: Business Architecture & Business Process Management', 'week': 10, 'minutes': 70, 'reading_min': 25, 'ka': 'PERSP', 'type': 'lesson',
 'teaser': 'Enterprise-level models and process improvement.',
 'prepare': [P('The Business Architecture Perspective'), P('The Business Process Management Perspective')],
 'hook': """Two enterprise-level lenses: **business architecture** (how the enterprise is structured to deliver strategy) and **BPM** (continuous process improvement).""",
 'objectives': ['Explain business architecture reference models and techniques', 'Explain BPM frameworks, methodologies (Lean, Six Sigma, TOC, TQM, BPR) and techniques (SIPOC, DMAIC…)'],
 'teach': [
  {'title': 'Business Architecture',
   'read': [P('The Business Architecture Perspective')],
   'points': ['Models the enterprise to show how strategic concerns are met: capabilities, value streams, information, organization.',
              'Reference models: ACORD, Business Motivation Model, COBIT, FEA, ITIL, APQC PCF, SCOR, VRM. Techniques: capability map, value mapping, customer journey map, roadmap, TOGAF, Zachman, project portfolio analysis.'],
   'check': 'Which technique shows the end-to-end value a customer receives, stage by stage?',
   'expect': 'Value mapping / value stream',
   'feedback': 'value mapping (value streams). The customer journey map is the customer\'s experiential view.'},
  {'title': 'BPM',
   'read': [P('The Business Process Management Perspective')],
   'points': ['BPM: design, execution, monitoring and optimization of processes end to end.',
              'Methodologies: Lean (waste), Six Sigma (variation; DMAIC for existing processes, DMADV for new ones), Theory of Constraints (bottlenecks; drum-buffer-rope), TQM, BPR (radical redesign), continuous improvement, adaptive case management.',
              'Techniques: SIPOC, value stream analysis, cycle-time analysis, FMEA, Kaizen event, process simulation, 5 Whys / 5Ws.'],
   'check': 'Improving an existing picking process with measurable defects: DMAIC or DMADV?',
   'expect': 'DMAIC',
   'feedback': 'DMAIC (Define, Measure, Analyze, Improve, Control) for existing processes.'}
 ],
 'quiz': {'n': 10, 'focus': 'Business Architecture and BPM perspectives: reference models, methodologies, techniques', 'ka': 'PERSP', 'topic': 'persp-2'},
 'takeaways': ['Business architecture = enterprise blueprint; BPM = process improvement.', 'DMAIC improves existing processes; DMADV designs new ones.'],
 'reading': ['BABOK 11.4–11.5 (pp.408–440)'],
 'flashcards': ['DMAIC vs DMADV? :: DMAIC improves an existing process; DMADV designs a new process/product', 'SIPOC? :: Suppliers, Inputs, Process, Outputs, Customers'],
 'success': ['Student distinguishes BA and BPM perspectives', 'Drill logged'],
},
{
 'id': '8.7', 'slug': 'competencies-deep-dive', 'title': 'Underlying competencies deep-dive + consolidation quiz', 'week': 10, 'minutes': 80, 'reading_min': 20, 'ka': 'COMP', 'type': 'review',
 'teaser': 'Name the competency behind the behaviour, then a 30-question consolidation.',
 'prepare': [UC('Underlying Competencies'), UC('Analytical Thinking and Problem Solving'), UC('Behavioural Characteristics'), UC('Business Knowledge'), UC('Communication Skills'), UC('Interaction Skills'), UC('Tools and Technology')],
 'hook': """Competency questions describe a *behaviour* and ask which competency it shows. Today we sharpen that, then run a 30-question consolidation across techniques, perspectives and competencies.""",
 'objectives': ['Identify competencies from behaviour', 'Know effectiveness measures for key competencies'],
 'teach': [
  {'title': 'Behaviour → competency',
   'points': ['Go group by group, giving one GreenBasket behaviour per competency, e.g. "reframed the delivery debate using the full survey data" = decision making / conceptual thinking; "kept every commitment to Kim" = trustworthiness / personal accountability; "facilitated workshop #2 neutrally" = facilitation; "negotiated central picker funding" = negotiation and conflict resolution; "taught stores to read the dashboard" = teaching.',
              'Watch out: ethics (fairness, transparency, confidentiality) vs trustworthiness (consistency, honesty over time).'],
   'check': 'The BA explains to Marcus how a change to aisle data affects accuracy, customer trust and labour cost. Competency?',
   'expect': 'Systems thinking',
   'feedback': 'systems thinking.'}
 ],
 'quiz': {'n': 30, 'focus': 'consolidation: techniques (all 50, selection), perspectives (5), underlying competencies (identify from behaviour)', 'ka': 'COMP', 'topic': 'consolidation-30',
          'mix': '12 technique selection, 8 perspective context, 10 competency'},
 'extra': ["""## Phase 3 milestone

ACTION: Summarize week 10: master technique sheet complete? technique recall count? consolidation score? Then preview weeks 11–13: 3 full mocks, gap sprints, exam-day playbook.

STOP: Have you booked your exam date? The final mock in week 13 is your go/no-go signal.

USER: Responds"""],
 'takeaways': ['Behaviour words in the question stem point to the competency.', 'Consolidation done. Next: full exam simulation.'],
 'reading': ['BABOK ch.9 (pp.185–213): skim the effectiveness measures', 'Lessing ch.12 (pp.316–347)'],
 'success': ['30-question consolidation logged', 'Phase 3 milestone reviewed'],
},
]}
