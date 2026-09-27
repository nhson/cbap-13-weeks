from render import T, TE, KA, IO, F, CC, R, UC, P, EX, CF

KAN = 'Elicitation and Collaboration'
MODULE = {'id': '3', 'name': 'Elicitation & Collaboration (12%)', 'weeks': '4',
          'description': 'Prepare, conduct and confirm elicitation; communicate BA information; manage stakeholder collaboration. Includes a live interview role-play with a GreenBasket picker.',
          'lessons': [
{
 'id': '3.1', 'slug': 'prepare-for-elicitation', 'title': 'E&C overview + 4.1 Prepare for Elicitation', 'week': 4, 'minutes': 75, 'reading_min': 30, 'ka': 'E&C',
 'teaser': 'Plan an elicitation activity: scope, techniques, logistics, materials, people.',
 'prepare': [KA(KAN), T('Prepare for Elicitation'), IO('Elicitation Activity Plan'), TE('Document Analysis'), TE('Data Mining')],
 'hook': """Rosa said it plainly in 2024: *"Don't let head office design this alone again. Talk to Kim."* This week you do elicitation properly. First: **4.1 Prepare for Elicitation**.""",
 'objectives': ['Explain E&C\'s five tasks and the elicitation-results states', 'Know the 5 elements of 4.1 and its output', 'Name the three types of elicitation (collaborative, research, experiments)'],
 'teach': [
  {'title': 'E&C at a glance',
   'read': [KA(KAN)],
   'points': ['Five tasks: 4.1 Prepare for Elicitation, 4.2 Conduct Elicitation, 4.3 Confirm Elicitation Results, 4.4 Communicate BA Information, 4.5 Manage Stakeholder Collaboration.',
              'Elicitation is iterative and ongoing. It isn\'t a phase. It draws out, explores and identifies information, which is more than "gathering".',
              'State flow: Elicitation Activity Plan → Elicitation Results (unconfirmed) → Elicitation Results (confirmed).',
              'Three types of elicitation (4.2): collaborative (direct interaction), research (documents and data), experiments (observation, proofs of concept, prototypes to find unknowns).'],
   'check': 'Studying the Harvest post-mortem: collaborative, research, or experiment?',
   'expect': 'Research',
   'feedback': 'research: systematically discovering and studying information from materials or sources not directly known by stakeholders involved in the change.'},
  {'title': 'Prepare for Elicitation',
   'read': [T('Prepare for Elicitation')],
   'points': ['Purpose (in our words): Get ready for an elicitation activity: its scope, the techniques, the logistics, the materials, and the people taking part.',
              'Elements: Understand the Scope of Elicitation, Select Elicitation Techniques, Set Up Logistics, Secure Supporting Material, Prepare Stakeholders.',
              'Inputs: Needs, Stakeholder Engagement Approach. Guidelines: BA Approach, Business Objectives, Existing BA Information, Potential Value. Output: Elicitation Activity Plan.',
              'Techniques include document analysis, data mining, interviews, brainstorming, estimation, mind mapping, risk analysis, and stakeholder list, map or personas.'],
   'check': 'Why would you do Document Analysis and Data Mining *during preparation*, before meeting anyone?',
   'expect': 'To understand background, form questions, avoid wasting stakeholder time',
   'feedback': 'to build background knowledge, identify gaps and good questions, and respect stakeholder time. Here that means the Harvest post-mortem, SO-12 data and survey stats.'}
 ],
 'apply': [
  {'title': 'Elicitation Activity Plan: picker and store discovery',
   'brief': 'Plan elicitation with Riverton Central (Rosa, Kim, pickers) for next Tuesday morning (the retro told you: not Fridays).',
   'files': [CF('03-store-ops-process-notes.md'), CF('09-interview-transcript-rosa.md'), CF('02-harvest-postmortem.md')],
   'ask': 'Draft the Elicitation Activity Plan for each of the 5 elements: scope and goals, techniques (and why: interviews, observation, a small workshop?), logistics (time, place, duration), supporting materials, and how you\'ll prepare the stakeholders.',
   'action': 'Coach and save. Emphasize observation for tacit knowledge, interviewing Kim separately so it feels safe to speak (low power), avoiding peak times, bringing the SO-12 form and Kim\'s 2024 issue list, and sending an agenda in advance.',
   'output': '20-elicitation-activity-plan.md',
   'discovery': 'Rosa\'s 2024 interview said picking takes "about 15 minutes", but the store\'s own table shows 18–41 minutes. Preparation reveals the questions you must ask.'}
 ],
 'quiz': {'n': 8, 'focus': 'E&C overview, types of elicitation, 4.1 elements, inputs, guidelines and output', 'ka': 'E&C', 'topic': '4.1',
          'traps': ['elicitation = requirements gathering only once', 'Elicitation Activity Plan vs Stakeholder Engagement Approach', 'research vs experiment type']},
 'takeaways': ['E&C is iterative; results move from unconfirmed to confirmed.', '4.1 elements: scope, techniques, logistics, supporting material, prepare stakeholders.', 'Three elicitation types: collaborative, research, experiments.'],
 'exam_rule': 'Before engaging stakeholders, the BA prepares (4.1), including reviewing existing information.',
 'reading': ['BABOK 4.0–4.1 (pp.53–60)', 'Lessing ch.7 pp.110–121', 'Jonasson 5.3–5.4 (pp.74–78): selecting techniques'],
 'flashcards': ['4.1 elements? :: Understand Scope of Elicitation; Select Elicitation Techniques; Set Up Logistics; Secure Supporting Material; Prepare Stakeholders', '3 types of elicitation? :: Collaborative, research, experiments', '4.1 output? :: Elicitation Activity Plan'],
 'success': ['Student knows the 5 E&C tasks and the state flow', 'workspace/20-elicitation-activity-plan.md created', 'Drill logged; task card added'],
},
{
 'id': '3.2', 'slug': 'conduct-elicitation', 'title': '4.2 Conduct Elicitation: live interview with Kim', 'week': 4, 'minutes': 90, 'reading_min': 20, 'ka': 'E&C',
 'teaser': 'You interview Kim Tran, the picker who knows why Harvest failed.',
 'prepare': [T('Conduct Elicitation'), TE('Interviews'), TE('Observation'), IO('Elicitation Results (unconfirmed)'), 'company-context/stakeholders/STAKEHOLDERS.md', CF('02-harvest-postmortem.md')],
 'hook': """Today you don't just read about elicitation. You do it. I'll play **Kim Tran**, a picker at Riverton Central. Kim knows exactly why picking failed in Harvest, but only shares it with an interviewer who earns trust and asks good questions.""",
 'objectives': ['Explain the elements of 4.2 (guide the activity, capture outcomes)', 'Run a structured interview with open and closed questions', 'Produce Elicitation Results (unconfirmed)'],
 'teach': [
  {'title': 'Conduct Elicitation',
   'read': [T('Conduct Elicitation'), TE('Interviews')],
   'points': ['Purpose (in our words): Run the elicitation activity: draw out and explore information with stakeholders or from sources, and record what comes out of it.',
              'Elements: Guide Elicitation Activity (keep to scope, probe, watch for new information) and Capture Elicitation Outcomes.',
              'Input: Elicitation Activity Plan. Output: Elicitation Results (unconfirmed). 18 techniques are listed, the most of any E&C task.',
              'Interview tips: prepare goals and questions; open questions to explore and closed questions to confirm; build rapport; don\'t lead; summarize and confirm at the end.',
              'Observation: active/noticeable (asking questions) vs passive/unnoticeable (just watching). It reveals tacit knowledge and workarounds.'],
   'check': 'Give me one open question and one closed question you might ask Kim.',
   'expect': 'Two example questions',
   'feedback': 'open, e.g. "Walk me through picking a big order on a Saturday". Closed, e.g. "Did the handhelds last a full shift?". Avoid leading questions like "The scanners were the main problem, right?".'}
 ],
 'apply': [
  {'title': 'The interview (role-play)',
   'brief': """ACTION: Role-play as **Kim Tran** (picker, 4 years, low power, high interest, did Harvest trial picks) for the next exchange. Rules for playing Kim:
- Start friendly but guarded: "Is this another head-office thing? Last time nobody read my list."
- Share information in proportion to question quality. Open, non-leading questions earn detail; leading or closed-only questions get short answers.
- Facts Kim knows (reveal only when asked well): aisle locations wrong after resets; no substitution guidance; handheld battery ~2 h; chilled items warm by the end; Saturday rush; unclear whether picking counts in productivity targets; totes by temperature zone would help; a dedicated early-morning picker schedule works best; 17-year-old evening staff can't hand over alcohol; a staging cooler is needed; one-lap picking is impossible for orders over 40 items in big stores.
- If the student confirms and summarizes at the end, Kim warms up and offers to show them on the shop floor (observation).
Stay in character until the student says "end interview".""",
   'ask': 'You\'re sitting with Kim in the break room with 30 minutes. Start the interview. Type "end interview" when you\'re done.',
   'expect': 'Conducts a multi-turn interview',
   'action': 'Step out of character. Debrief: what went well (rapport, open questions, probing, summarizing) and what was missed (list the facts not uncovered). Then write the elicitation results as **unconfirmed** notes: source, date, technique, verbatim quotes, observations, open questions.',
   'output': '21-elicitation-results-kim-unconfirmed.md',
   'model': ['Rapport first; acknowledge the ignored 2024 list', 'Open questions on the end-to-end picking flow; probing on "why" for delays', 'Captured facts about data, devices, temperature, peaks and incentives', 'Summarized at the end and asked to observe a pick (experiment/observation)'],
   'discovery': 'The unconfirmed results already contradict Rosa\'s 2024 interview ("15 minutes", "stock mostly fine"). Next lesson you confirm which is right.'}
 ],
 'quiz': {'n': 8, 'focus': '4.2 Conduct Elicitation, interview technique (question types, structured vs unstructured), observation types, capturing outcomes', 'ka': 'E&C', 'topic': '4.2',
          'traps': ['results from 4.2 labelled confirmed', 'leading questions', 'passive observation when you need to understand reasons', 'interviews for large dispersed populations (survey is better)']},
 'takeaways': ['4.2 = guide the activity plus capture outcomes; the output is **unconfirmed**.', 'Open questions explore; closed questions confirm; never lead.', 'Observation uncovers tacit knowledge that interviews miss.'],
 'exam_rule': 'Large, dispersed group → survey. Tacit, hands-on work → observation. Deep individual view → interview. Group consensus → workshop.',
 'reading': ['BABOK 4.2 (pp.61–64), 10.25 Interviews, 10.31 Observation', 'Jonasson 5.5–5.6 (pp.79–89)'],
 'flashcards': ['4.2 output? :: Elicitation Results (unconfirmed)', 'Active vs passive observation? :: Active/noticeable: observer asks questions during work; passive/unnoticeable: observer watches without interrupting', '4.2 elements? :: Guide Elicitation Activity; Capture Elicitation Outcomes'],
 'success': ['Student conducted a multi-turn interview', 'Debrief given with missed facts', 'workspace/21-elicitation-results-kim-unconfirmed.md created', 'Drill logged; task card added'],
},
{
 'id': '3.3', 'slug': 'confirm-elicitation-results', 'title': '4.3 Confirm Elicitation Results', 'week': 4, 'minutes': 70, 'reading_min': 20, 'ka': 'E&C',
 'teaser': 'Compare against sources and other results. Who was right about pick time?',
 'prepare': [T('Confirm Elicitation Results'), IO('Elicitation Results (confirmed)'), EX('Commonly Confused Concepts'), CF('09-interview-transcript-rosa.md'), CF('03-store-ops-process-notes.md')],
 'hook': """Rosa said picking takes 15 minutes. The store's own data says 18–41. Kim says it's worse on Saturdays. The Harvest contractor wrote "confirmed". Confirming is exactly what they failed to do. Today: **4.3 Confirm Elicitation Results**.""",
 'objectives': ['Explain the two elements of 4.3', 'Distinguish confirm vs verify vs validate', 'Resolve contradictions between sources'],
 'teach': [
  {'title': 'Confirm Elicitation Results',
   'read': [T('Confirm Elicitation Results')],
   'points': ['Purpose (in our words): Check that what was elicited is accurate and consistent, by comparing it with sources and with other results.',
              'Elements: Compare Elicitation Results Against Source Information, and Compare Elicitation Results Against Other Elicitation Results.',
              'Input: Elicitation Results (unconfirmed). Guidelines: Elicitation Activity Plan, Existing BA Information. Output: Elicitation Results (confirmed).',
              'Techniques: document analysis, interviews, reviews, workshops.'],
   'check': 'How is confirming different from verifying requirements (7.2)?',
   'expect': 'Confirm = accurate understanding of what stakeholders said; verify = requirement quality',
   'feedback': 'confirm checks the BA captured information accurately and consistently. Verify checks that specified requirements are well-formed (quality characteristics).',
   'trap': 'Answers saying "validate the elicitation results" are usually wrong. Confirm is the BABOK word here.'}
 ],
 'apply': [
  {'title': 'Reconcile the sources',
   'brief': 'Three sources disagree about the current process.',
   'files': [CF('09-interview-transcript-rosa.md'), CF('03-store-ops-process-notes.md'), 'workspace/21-elicitation-results-kim-unconfirmed.md'],
   'ask': 'Build a comparison: for pick time, stock accuracy, where chilled/frozen go, which till is used, alcohol on phone orders, and who picks and when, note what each source says, the contradiction, and how you would confirm it (which technique, with whom).',
   'action': 'Coach it and save a confirmation matrix, then a "confirmed results" section for the items that the data or documents settle (e.g. pick times are 18–41 min per the store table; the manual is outdated per Rosa\'s own notes). Mark items still needing confirmation with owners.',
   'output': '22-elicitation-results-confirmed.md',
   'model': ['Pick time: manual silent, Rosa said 15, the table shows 18–41 → confirmed as 18–41, driven by day of week', 'Stock accuracy "mostly fine" vs IT 82% (74% fresh) → confirmed not fine for fresh', 'Frozen goes to the front ice-cream freezer, not the back cooler (margin note) → cold-chain risk to confirm by observation', 'Alcohol: unwritten head-office rule → confirm with Janet'],
   'discovery': 'The Harvest contractor wrote "confirmed" after a single interview. Confirmation means comparing against source information and other results.'}
 ],
 'quiz': {'n': 8, 'focus': '4.3 Confirm Elicitation Results and the confirm vs verify vs validate distinction', 'ka': 'E&C', 'topic': '4.3',
          'traps': ['confirm = validate', 'confirmed results produced by 4.2', 'confirmation requires formal sign-off']},
 'takeaways': ['Confirm = accuracy and consistency against sources and other results.', 'Output: Elicitation Results (confirmed).', 'Confirm ≠ verify ≠ validate.'],
 'exam_rule': 'Contradictions between stakeholders → compare against sources and other results (4.3) before specifying anything.',
 'reading': ['BABOK 4.3 (pp.65–66)', 'Lessing pp.125–128'],
 'flashcards': ['4.3 elements? :: Compare against Source Information; Compare against Other Elicitation Results', 'Confirm vs verify? :: Confirm = captured information accurate and consistent (4.3); verify = requirement quality (7.2)'],
 'success': ['Confirmation matrix built', 'workspace/22-elicitation-results-confirmed.md created', 'Student distinguishes confirm, verify and validate', 'Drill logged; task card added'],
},
{
 'id': '3.4', 'slug': 'communicate-ba-information', 'title': '4.4 Communicate Business Analysis Information', 'week': 4, 'minutes': 70, 'reading_min': 20, 'ka': 'E&C',
 'teaser': 'Same findings, three audiences: Elena, Marcus, the vendors.',
 'prepare': [T('Communicate Business Analysis Information'), IO('Business Analysis Information (communicated)'), IO('Information Management Approach')],
 'hook': """Your discovery findings are solid. Now you have to land them with a COO who wants one page, a store head who hates slide decks, and vendors who need detail. **4.4 Communicate BA Information**.""",
 'objectives': ['Know the elements of 4.4', 'Choose format by audience (formal, informal, presentation)', 'Recognize communication as bi-directional and iterative'],
 'teach': [
  {'title': 'Communicate BA Information',
   'read': [T('Communicate Business Analysis Information')],
   'points': ['Purpose (in our words): Make sure stakeholders share the same understanding of business analysis information, using the right format and channel for each audience.',
              'Elements: Determine Objectives and Format of Communication (formal documentation, informal documentation, presentations), and Communicate Business Analysis Package.',
              'Package: prepare, review and approve. Delivery via group collaboration, individual collaboration, or e-mail and other non-verbal methods.',
              'Inputs: Business Analysis Information, Stakeholder Engagement Approach. Guidelines: BA Approach, Information Management Approach. Output: Business Analysis Information (communicated).',
              'Communication is bi-directional: check understanding, don\'t just transmit.'],
   'check': 'For Marcus (distrusts slides, prefers face-to-face), what format and delivery would you choose?',
   'expect': 'Informal / walkthrough in person',
   'feedback': 'informal documentation or a short walkthrough, delivered through individual collaboration face-to-face, per his communication needs from 3.2.'}
 ],
 'apply': [
  {'title': 'One finding set, three packages',
   'brief': 'Package your confirmed discovery findings for three audiences.',
   'files': ['workspace/22-elicitation-results-confirmed.md', 'workspace/11-stakeholder-engagement-approach.md'],
   'ask': 'For Elena, Marcus and the vendors, define: objective, format (formal, informal, presentation), level of detail, delivery method, and how you\'ll check understanding. Then draft Elena\'s version (at most 10 lines).',
   'action': 'Coach and save all three package definitions plus the drafted executive summary for Elena.',
   'output': '23-communication-packages.md',
   'review': 'elena-sponsor', 'review_focus': 'ask whether the executive summary tells her what she needs to decide'}
 ],
 'quiz': {'n': 8, 'focus': '4.4 elements, package formats, delivery methods, audience tailoring', 'ka': 'E&C', 'topic': '4.4',
          'traps': ['one format for all', 'communication as one-way', 'confusing 4.4 with 3.2 communication *needs* planning']},
 'takeaways': ['3.2 plans communication needs; 4.4 performs the communication.', 'Formats: formal documentation, informal documentation, presentations.', 'Communication is bi-directional: confirm shared understanding.'],
 'reading': ['BABOK 4.4 (pp.67–70)', 'Jonasson 5.19–5.20 (pp.126–132)'],
 'flashcards': ['4.4 elements? :: Determine Objectives and Format of Communication; Communicate BA Package', '4.4 output? :: Business Analysis Information (communicated)'],
 'success': ['workspace/23-communication-packages.md created and sponsor-reviewed', 'Drill logged; task card added'],
},
{
 'id': '3.5', 'slug': 'manage-stakeholder-collaboration', 'title': '4.5 Manage Stakeholder Collaboration', 'week': 4, 'minutes': 70, 'reading_min': 20, 'ka': 'E&C',
 'teaser': 'Marcus cancels again. Keep collaboration alive.',
 'prepare': [T('Manage Stakeholder Collaboration'), IO('Stakeholder Engagement'), TE('Collaborative Games'), CF('17-ba-team-retro-notes.md')],
 'hook': """Store ops cancelled 5 of 7 rescheduled sessions. Lily feels "shut down". Collaboration is slipping. **4.5 Manage Stakeholder Collaboration** is how the BA keeps people engaged throughout the change, not only at the start.""",
 'objectives': ['Know the 3 elements of 4.5', 'Respond to disengagement and conflict', 'Distinguish Stakeholder Engagement Approach (plan) from Stakeholder Engagement (result)'],
 'teach': [
  {'title': 'Manage Stakeholder Collaboration',
   'read': [T('Manage Stakeholder Collaboration')],
   'points': ['Purpose (in our words): Keep stakeholders engaged and working together towards the shared goal for the whole initiative.',
              'Elements: Gain Agreement on Commitments (time and resources), Monitor Stakeholder Engagement (participation, performance, risks such as diverted attention or delays), Collaboration (open communication, sharing, trust).',
              'Inputs: Stakeholder Engagement Approach, BA Performance Assessment. Guidelines: BA Approach, Business Objectives, Future State Description, Recommended Actions, Risk Analysis Results. Output: Stakeholder Engagement.',
              'Techniques: collaborative games, lessons learned, risk analysis and management, and stakeholder list, map or personas.'],
   'check': 'Marcus keeps cancelling. What does the BABOK say the BA should do first?',
   'expect': 'Monitor engagement, understand the cause, re-secure commitment',
   'feedback': 'monitor engagement, identify the risk, understand the reason (e.g. Friday scheduling, funding concern) and gain agreement on commitments. Escalate to the sponsor only if that fails.',
   'trap': 'Escalating to the sponsor as the *first* step is usually the wrong answer.'}
 ],
 'apply': [
  {'title': 'Rescue the collaboration',
   'brief': 'Two collaboration problems: store ops disengagement and marketing frustration.',
   'files': [CF('17-ba-team-retro-notes.md'), CF('10-workshop-notes-raw.md')],
   'ask': 'For Marcus and for Lily: what signals are you monitoring, what\'s the likely cause, what commitment will you seek, and what collaboration tactic will you use? When would you escalate?',
   'action': 'Coach and save a collaboration plan, and propose a collaborative game (e.g. Product Box with marketing, to channel Lily\'s ideas into a parked "future features" backlog).',
   'output': '24-stakeholder-collaboration-plan.md',
   'review': 'marcus-store-ops', 'review_focus': 'ask whether this plan would bring him back to the table'}
 ],
 'quiz': {'n': 8, 'focus': '4.5 elements, handling disengagement and conflict, escalation timing, collaborative games', 'ka': 'E&C', 'topic': '4.5',
          'traps': ['escalate first', 'Stakeholder Engagement Approach as 4.5 output', 'collaborative games need no facilitator']},
 'takeaways': ['Gain commitments, monitor engagement, collaborate: continuously.', 'Output: Stakeholder Engagement (the state of the relationship).', 'Understand causes before escalating.'],
 'reading': ['BABOK 4.5 (pp.71–74), 10.10 Collaborative Games', 'Lessing pp.132–147 (incl. knowledge quiz)'],
 'flashcards': ['4.5 elements? :: Gain Agreement on Commitments; Monitor Stakeholder Engagement; Collaboration', '4.5 output? :: Stakeholder Engagement'],
 'success': ['workspace/24-stakeholder-collaboration-plan.md created and Marcus-reviewed', 'Drill logged; task card added'],
},
{
 'id': '3.6', 'slug': 'elicitation-techniques-lab', 'title': 'Elicitation techniques lab: choosing the right technique', 'week': 4, 'minutes': 80, 'reading_min': 20, 'ka': 'TECH', 'type': 'lab',
 'teaser': 'Workshops, focus groups, surveys, observation, brainstorming, prototyping: when to use each.',
 'prepare': [TE('Workshops'), TE('Focus Groups'), TE('Survey or Questionnaire'), TE('Observation'), TE('Brainstorming'), TE('Prototyping'), TE('Interface Analysis'), TE('Benchmarking and Market Analysis')],
 'hook': """"Which technique should the BA use?" is one of the most common exam question types. Today you learn the *selection logic*, the strengths and limitations that decide between look-alike techniques.""",
 'objectives': ['Select elicitation techniques by situation', 'Know key strengths and limitations of each', 'Design a workshop and a survey'],
 'teach': [
  {'title': 'Selection logic',
   'read': [TE('Workshops'), TE('Focus Groups'), TE('Survey or Questionnaire')],
   'points': ['Workshops: a structured, facilitated event to reach decisions or consensus; roles are sponsor, facilitator, scribe, timekeeper and participants. Can be dominated by strong voices.',
              'Focus groups: 6–12 pre-qualified participants with a moderator; qualitative opinions and attitudes. Not for decisions or consensus.',
              'Surveys: many or dispersed respondents, quick and cheap; closed questions for statistics, open questions for depth. Low response rate and no follow-up probing.',
              'Observation: tacit knowledge and real workflow; people may behave differently when watched.',
              'Brainstorming: many ideas fast, no evaluation during generation. Prototyping: elicit and validate via a model (throw-away vs evolutionary; by purpose: proof of concept, form study, usability, visual).',
              'Benchmarking and market analysis: compare with best practice and competitors. Interface analysis: for each interface, what information crosses it, how, how often, why, and who owns it.'],
   'check': 'You need opinions from 400 Basket Rewards members in 3 states within a week. Technique?',
   'expect': 'Survey',
   'feedback': 'survey or questionnaire: many respondents, geographically dispersed, time-boxed.'}
 ],
 'apply': [
  {'title': 'Design Workshop #2 (the one that works)',
   'brief': 'Workshop #1 had no owners, the sponsor left after 30 minutes, and marketing felt shut down.',
   'files': [CF('10-workshop-notes-raw.md'), TE('Workshops')],
   'ask': 'Design Workshop #2 on "substitutions and pickup experience": objective, participants, roles, agenda with timings, techniques inside the workshop (e.g. brainstorming, dot voting, collaborative game), ground rules, and expected outputs. Also write 5 survey questions to test substitution preferences with members.',
   'action': 'Coach it and save the design. Check: a neutral facilitator (not the BA if the BA needs to contribute), decisions captured with owners, Kim and Rosa included, and the customer voice brought in (survey data or personas).',
   'output': '25-workshop-2-and-survey-design.md'}
 ],
 'quiz': {'n': 12, 'focus': 'choosing elicitation techniques in scenarios; strengths and limitations of interviews, workshops, focus groups, surveys, observation, brainstorming, prototyping, document analysis, benchmarking, interface analysis', 'ka': 'TECH', 'topic': 'elicitation-techniques',
          'traps': ['focus group for decisions', 'workshop for large dispersed groups', 'observation when behaviour is cognitive and not visible', 'prototype type mix-ups (throw-away vs evolutionary)']},
 'takeaways': ['Decision or consensus → workshop; opinions → focus group; many or dispersed → survey; tacit → observation.', 'Know one strength and one limitation per technique.'],
 'exam_rule': 'Read the scenario constraints (group size, geography, time, decision vs opinion). They pick the technique for you.',
 'reading': ['BABOK 10.5, 10.21, 10.31, 10.36, 10.45, 10.50', 'Jonasson 5.9–5.16 (pp.92–121)'],
 'flashcards': ['Focus group size and purpose? :: 6–12 pre-qualified participants; qualitative opinions and attitudes; not for decisions', 'Throw-away vs evolutionary prototype? :: Throw-away is discarded after eliciting; evolutionary grows into the final solution'],
 'success': ['workspace/25-workshop-2-and-survey-design.md created', 'Student chose techniques correctly in drills', 'Drill logged'],
},
{
 'id': '3.7', 'slug': 'ec-exam-drill', 'title': 'E&C exam drill (40 questions)', 'week': 4, 'minutes': 60, 'reading_min': 0, 'ka': 'E&C', 'type': 'drill',
 'teaser': 'Prove E&C mastery.',
 'prepare': [KA(KAN), T('Prepare for Elicitation'), T('Conduct Elicitation'), T('Confirm Elicitation Results'), T('Communicate Business Analysis Information'), T('Manage Stakeholder Collaboration')],
 'hook': """End of E&C week. 40 questions. E&C is only 12%, but its techniques appear in every KA. Target 75%.""",
 'quiz': {'n': 40, 'focus': 'all of E&C 4.1–4.5 plus elicitation technique selection; include a 5-question case study', 'ka': 'E&C', 'topic': 'ec-40', 'mix': '26 scenario, 8 I/O and technique, 6 definition'},
 'extra': ["""## Week 4 review

ACTION: Summarize: E&C score vs diagnostic, trend across BAPM and E&C, error-log themes, and task cards 4.1–4.5 done.

STOP: Which elicitation technique do you still hesitate on?

USER: Responds

ACTION: Give a 3-line contrast of that technique against its closest look-alike, and add it to weak_topics if needed."""],
 'takeaways': ['E&C: prepare → conduct → confirm, plus ongoing communicate and collaborate.', 'Technique choice follows scenario constraints.'],
 'reading': ['BABOK 5.0 intro (pp.75–78) before lesson 4.1'],
 'success': ['40-question drill completed and logged', 'Week review done'],
},
]}
