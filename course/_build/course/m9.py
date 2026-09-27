from render import T, TE, KA, IO, F, CC, R, UC, P, EX, CF

def mock(n):
    return f"""## Generate Mock Exam {n}

ACTION: Silently read `CBAP Knowledge Graph/08 Exam Lens/Exam Blueprint.md`, `Commonly Confused Concepts.md`, `BABOK Input-Output Flow.md`, `progress/error-log.md` and the 6 KA notes. Then write **Mock Exam {n}: 120 original CBAP-style questions** to `exams/mock-{n}.md`, in 4 batches of 30 (append each batch; check facts against task and technique notes as you go):
- Blueprint: RADD 36, RLCM 18, SA 18, BAPM 17, SE 17, E&C 14. Techniques, perspectives and competencies are embedded inside KA questions.
- Types: ~65% scenario, including **3 case studies** (a 1–2 paragraph scenario followed by 4–5 questions each, all in fresh contexts, not GreenBasket); ~20% input/output/technique selection; ~15% definitions and concepts.
- Difficulty: real-exam level. Several plausible options, one most BABOK-correct. {"Weight ~25% of the questions towards the student's error-log weak topics." if n > 1 else ""}
- Don't reuse questions from earlier drills or mocks (check `exams/` for previous mocks).
- Key → `exams/.keys/mock-{n}-key.md`: number | answer | KA | task/technique | type | rationale (2 lines) | knowledge-graph note.
- Answer sheet → `exams/mock-{n}-answers.md` with `1: ` … `120: ` lines.

Link [mock-{n}.md](exams/mock-{n}.md) and [mock-{n}-answers.md](exams/mock-{n}-answers.md). Never reveal the key.

STOP: Exam conditions: **210 minutes**, one sitting, no notes, phone away. Mark guesses with `?`. Flag and move on after 2 minutes on any question. Tell me "done" when finished (or "pause" if you must stop, and note the time used).

USER: done

ACTION: Grade exactly as the `/grade mock-{n}` command does (score, per-KA and per-type breakdown, error log, scores.csv, report in `exams/mock-{n}-report.md`). Also compute the time used per question if the student reports the total time."""

MODULE = {'id': '9', 'name': 'Exam simulation & final preparation', 'weeks': '11–13',
          'description': 'Exam technique, three full 120-question mocks under exam conditions, targeted gap-closing sprints, case-study clinic, final review and exam-day playbook.',
          'lessons': [
{
 'id': '9.1', 'slug': 'exam-technique', 'title': 'Exam technique: reading case studies, elimination, time management', 'week': 11, 'minutes': 60, 'reading_min': 30, 'ka': 'GEN', 'type': 'lesson',
 'teaser': 'How to think like the exam.',
 'prepare': [EX('Exam Blueprint'), EX('Commonly Confused Concepts'), 'progress/error-log.md'],
 'hook': """You know the content. Now we train the *test-taking*: how to read a long case, eliminate options, and manage 210 minutes without panic.""",
 'objectives': ['Apply a 4-step question method', 'Use elimination on "all plausible" options', 'Plan pacing checkpoints'],
 'teach': [
  {'title': 'The 4-step method',
   'points': ['1) Read the **last sentence** first: what is asked (task? technique? output? next step? FIRST/BEST/NOT?).',
              '2) Identify the **context**: which KA and task is happening, which perspective (agile? BI?), and which state the information is in (unconfirmed? verified?).',
              '3) **Eliminate**: out-of-role actions (BA approves alone, PM duties), wrong state labels, real-life-but-not-BABOK answers, absolute words (always/never).',
              '4) Choose the answer that follows the task\'s purpose, involves the right stakeholders, and serves **value**.',
              'Pacing: 120 questions / 210 min. Checkpoints: Q40 at about 65 min, Q80 at about 135 min, Q120 at about 195 min, leaving 15 min to review flags.'],
   'check': 'Why read the last sentence first on a long case study?',
   'expect': 'To know what to look for while reading',
   'feedback': 'it tells you what to extract from the scenario, which saves re-reading.'},
  {'title': 'Classic distractor patterns',
   'read': [EX('Commonly Confused Concepts')],
   'points': ['Right concept, wrong state ("validated" vs "verified").', 'Right action, wrong owner (BA decides priorities or approves changes).', 'Right action, wrong timing (escalate before trying collaboration; build before assessing).', 'Real-world shortcut vs BABOK practice (skip confirmation because the sponsor is in a hurry).', 'Plan vs perform confusion (3.3 plans prioritization; 5.3 performs it).'],
   'check': 'Which of those patterns caught you most often in your error log?',
   'expect': 'Names a pattern'}
 ],
 'quiz': {'n': 12, 'focus': 'hard, tricky questions using the classic distractor patterns across all KAs; after each batch, explicitly name the distractor pattern of each wrong option', 'ka': 'ALL', 'topic': 'exam-technique'},
 'takeaways': ['Last sentence first, context second, eliminate third, value fourth.', 'Pacing checkpoints: Q40 about 65 min, Q80 about 135 min.'],
 'reading': ['Lessing ch.4 (pp.41–45) again', 'Jonasson ch.13 Preparing for the Test (pp.301–302)'],
 'success': ['Student can state the 4-step method', 'Distractor patterns reviewed against the error log', 'Drill logged'],
},
{
 'id': '9.2', 'slug': 'mock-exam-1', 'title': 'Full Mock Exam #1 (120 questions, 210 minutes)', 'week': 11, 'minutes': 225, 'reading_min': 0, 'ka': 'ALL', 'type': 'exam',
 'teaser': 'The first full simulation.',
 'prepare': [EX('Exam Blueprint'), EX('Commonly Confused Concepts'), EX('BABOK Input-Output Flow')],
 'hook': """Mock #1. Full length, full time, exam conditions. The score matters less than the data it gives us.""",
 'ready': 'Do you have about 3 hours 45 minutes free now (210 min exam + setup)? If not, I\'ll prepare the exam and you start when ready.',
 'extra': [mock(1), """## Immediate debrief

Share the total %, the per-KA table vs the 75% target, and time per question.

STOP: How did the pacing feel, and where did you get stuck?

USER: Responds

ACTION: Note the pacing issues in progress.json `notes`."""],
 'takeaways': ['First full mock done. Your stamina and pacing are now measured.', 'Target: 75% or more on mocks by week 12.'],
 'success': ['Mock 1 generated, taken and graded', 'Report written; error log updated'],
},
{
 'id': '9.3', 'slug': 'mock-1-review', 'title': 'Mock #1 deep review & gap plan', 'week': 11, 'minutes': 120, 'reading_min': 30, 'ka': 'ALL', 'type': 'review',
 'teaser': 'Every wrong AND every guessed answer, reviewed against the BABOK.',
 'prepare': ['progress/error-log.md', EX('Commonly Confused Concepts')],
 'prepare_note': 'Also read `exams/mock-1-report.md` and `exams/.keys/mock-1-key.md` (you may now discuss answers).',
 'hook': """The review is where the points come from. We go through every miss and every guess, sort them by cause, and turn them into a gap plan.""",
 'objectives': ['Understand every miss', 'Identify top 5 gap topics', 'Plan gap sprint I'],
 'teach': [
  {'title': 'Review protocol',
   'points': ['Go through misses grouped by KA (largest weight first). For each, ask the student why they picked it *before* revealing the rationale.',
              'Tag each miss: knowledge gap / confusion / misread / pacing.',
              'For every knowledge gap, point to the exact knowledge-graph note and BABOK page.'],
   'check': 'Let\'s start with your weakest KA. Ready to go through the first 5 misses?',
   'expect': 'Ready',
   'feedback': 'run the review interactively, 5 items at a time, until all misses and guesses are covered or 90 minutes have passed.'}
 ],
 'apply': [
  {'title': 'Gap plan I',
   'brief': 'Turn the review into a targeted plan for lesson 9.4.',
   'files': ['progress/error-log.md'],
   'ask': 'What are your top 5 gap topics, and which of them are confusions rather than knowledge gaps?',
   'action': 'Write the gap plan: 5 topics, for each the fix (re-read note X / BABOK pages / contrast table / drill), and the targeted drill set for 9.4. Update weak_topics.',
   'output': '80-gap-plan-1.md'}
 ],
 'takeaways': ['Review guesses as seriously as misses.', 'Fix confusions with contrast; fix gaps with notes and BABOK pages.'],
 'reading': ['The BABOK pages listed in your gap plan'],
 'success': ['All misses and guesses reviewed', 'workspace/80-gap-plan-1.md created', 'weak_topics updated'],
},
{
 'id': '9.4', 'slug': 'gap-sprint-1', 'title': 'Gap-closing sprint I', 'week': 11, 'minutes': 90, 'reading_min': 30, 'ka': 'ALL', 'type': 'drill',
 'teaser': 'Targeted re-teach + drills on your top gaps.',
 'prepare': ['progress/error-log.md', 'CBAP Knowledge Graph/00 CBAP Knowledge Graph.md'],
 'prepare_note': 'Read `workspace/80-gap-plan-1.md` and the knowledge-graph notes for each gap topic.',
 'hook': """Sprint time. For each of your top gaps: 3-minute re-teach, a contrast or memory hook, then targeted questions.""",
 'teach': [
  {'title': 'Re-teach loop',
   'points': ['For each gap topic in the gap plan: re-teach in ≤8 lines using a new angle (analogy, GreenBasket example, mnemonic), then ask 1 check question in chat.'],
   'check': 'Ready for the first gap topic?',
   'expect': 'Ready'}
 ],
 'quiz': {'n': 20, 'focus': "the student's top 5 gap topics from workspace/80-gap-plan-1.md (4 questions each)", 'ka': 'ALL', 'topic': 'gap-sprint-1'},
 'takeaways': ['Targeted practice beats random practice.'],
 'success': ['All gap topics re-taught', '20-question targeted drill logged'],
},
{
 'id': '9.5', 'slug': 'case-study-clinic', 'title': 'Case-study clinic: long multi-KA scenarios', 'week': 12, 'minutes': 90, 'reading_min': 0, 'ka': 'ALL', 'type': 'drill',
 'teaser': 'The long cases that decide pass or fail.',
 'prepare': [EX('BABOK Input-Output Flow'), EX('Commonly Confused Concepts')],
 'hook': """Case studies are where people run out of time and nerve. Today: 3 long cases, 5 questions each, and I coach your *reasoning process*, not just your answers.""",
 'objectives': ['Apply the 4-step method under pressure', 'Track the BABOK "state" across a long scenario'],
 'extra': ["""## Case 1 (think-aloud)

ACTION: Write a 2-paragraph case in a new industry (e.g. a hospital outpatient booking system, predictive approach, regulator heavy). Present it, then 5 questions via AskUserQuestion (4 per call, then 1).

STOP: Before answering, tell me in one line which KA and task each question is really about.

USER: Responds

ACTION: Coach the reasoning (was the task identification right?), then reveal the answers with rationales.""",
 """## Cases 2 and 3 (timed)

ACTION: Two more cases (e.g. an agile fintech product team; a BPM-driven process improvement in logistics), 5 questions each, timed at 9 minutes per case. Reveal the answers after each case. Log all 15 to scores.csv (topic `case-clinic`) and misses to the error log.

STOP: Did your time per case fit within 9 minutes? What slowed you down?

USER: Responds"""],
 'takeaways': ['Name the task behind each question before choosing.', '9 minutes per 5-question case.'],
 'success': ['3 cases completed and logged', 'Reasoning coached'],
},
{
 'id': '9.6', 'slug': 'mock-exam-2', 'title': 'Full Mock Exam #2', 'week': 12, 'minutes': 225, 'reading_min': 0, 'ka': 'ALL', 'type': 'exam',
 'teaser': 'Second simulation, weighted to your weak areas.',
 'prepare': [EX('Exam Blueprint'), 'progress/error-log.md'],
 'hook': """Mock #2. The roadmap target is **75% or more**. This mock leans slightly into your weak topics, so it will feel harder than the real exam.""",
 'ready': 'Ready for 210 minutes under exam conditions?',
 'extra': [mock(2), """## Debrief

Compare mock 2 with mock 1: total, per KA, time per question.

STOP: What changed compared with mock 1?

USER: Responds"""],
 'takeaways': ['Two data points are enough to see a trend.', 'The week-12 milestone is two mocks at 75% or more.'],
 'success': ['Mock 2 generated, taken and graded', 'Comparison with mock 1 done'],
},
{
 'id': '9.7', 'slug': 'mock-2-review', 'title': 'Mock #2 review & gap plan II', 'week': 12, 'minutes': 120, 'reading_min': 30, 'ka': 'ALL', 'type': 'review',
 'teaser': 'Review, and decide whether the exam date holds.',
 'prepare': ['progress/error-log.md', 'progress/scores.csv'],
 'prepare_note': 'Also read `exams/mock-2-report.md`, `exams/.keys/mock-2-key.md` and `workspace/80-gap-plan-1.md`.',
 'hook': """Same protocol as before, plus a decision: is your exam date still right? The roadmap says reschedule if you're below 70% on mocks by week 12.""",
 'teach': [
  {'title': 'Review protocol',
   'points': ['Review misses and guesses by KA, as in 9.3; spend extra time on repeat offenders (topics wrong in both mocks).'],
   'check': 'Ready to start with the repeat offenders?',
   'expect': 'Ready'}
 ],
 'apply': [
  {'title': 'Gap plan II + go/no-go check',
   'brief': 'Decide the final 10 days.',
   'files': ['progress/scores.csv'],
   'ask': 'Where are you vs 75%? What are the top 5 remaining gaps? Are you keeping the exam date?',
   'action': 'Write gap plan II with a day-by-day plan to the exam. If mocks are under 70%, recommend rescheduling within the 6-month exam window and explain how. Update progress.json.',
   'output': '81-gap-plan-2.md'}
 ],
 'takeaways': ['Repeat offenders get priority.', 'Rescheduling is a strategy, not a failure.'],
 'success': ['Mock 2 misses reviewed', 'workspace/81-gap-plan-2.md created', 'Exam-date decision recorded'],
},
{
 'id': '9.8', 'slug': 'gap-sprint-2', 'title': 'Gap-closing sprint II', 'week': 12, 'minutes': 90, 'reading_min': 30, 'ka': 'ALL', 'type': 'drill',
 'teaser': 'Final targeted sprint.',
 'prepare': ['progress/error-log.md'],
 'prepare_note': 'Read `workspace/81-gap-plan-2.md` and the notes for each gap topic.',
 'hook': """Last targeted sprint before the final mock.""",
 'teach': [
  {'title': 'Re-teach loop',
   'points': ['For each gap topic in gap plan II: re-teach in ≤8 lines with a fresh angle, then 1 chat check question.'],
   'check': 'Ready?',
   'expect': 'Ready'}
 ],
 'quiz': {'n': 20, 'focus': "the student's remaining gap topics from workspace/81-gap-plan-2.md", 'ka': 'ALL', 'topic': 'gap-sprint-2'},
 'takeaways': ['Gaps are closing. Trust the process.'],
 'success': ['Gap topics re-taught', 'Drill logged'],
},
{
 'id': '9.9', 'slug': 'mock-exam-3-final', 'title': 'Final Mock Exam #3: go/no-go', 'week': 13, 'minutes': 225, 'reading_min': 0, 'ka': 'ALL', 'type': 'exam',
 'teaser': 'The go/no-go signal.',
 'prepare': [EX('Exam Blueprint'), 'progress/error-log.md'],
 'hook': """Final mock. The roadmap target is **80% or more** as your go signal. Treat it exactly like exam day: same time of day as your real exam if possible.""",
 'ready': 'Are you set up like exam day (time of day, quiet room, no notes)?',
 'extra': [mock(3), """## Go / no-go

ACTION: Compare all three mocks (total and per KA). Apply the rule: ≥80% = go; 75–79% = go with a focused final review; <75% = strongly consider rescheduling.

STOP: Here's the verdict. How do you feel about it?

USER: Responds"""],
 'takeaways': ['Three mocks give a reliable picture.', 'Decide calmly with data.'],
 'success': ['Mock 3 taken and graded', 'Go/no-go decision made and recorded in progress.json'],
},
{
 'id': '9.10', 'slug': 'final-review', 'title': 'Final review: I/O map, technique sheet, confusions, glossary sprint', 'week': 13, 'minutes': 120, 'reading_min': 30, 'ka': 'ALL', 'type': 'review',
 'teaser': 'Light, high-yield review. No new material.',
 'prepare': [EX('BABOK Input-Output Flow'), EX('Commonly Confused Concepts'), EX('Technique-Task Matrix')],
 'prepare_note': 'Also read `workspace/05-my-io-backbone.md`, `workspace/70-master-technique-sheet.md`, `workspace/task-cards.md`, `workspace/flashcards.md`.',
 'hook': """No new content now, only consolidation. We run four fast rounds: the I/O chain, the confusion pairs, techniques, and flashcards.""",
 'extra': ["""## Round 1: I/O chain (15 min)

STOP: Recite the main output chain from Needs to Recommended Actions, with the task numbers. Go.

USER: Recites

ACTION: Correct gaps against the I/O Flow note.""",
 """## Round 2: Confusion pairs (20 min)

ACTION: Quick-fire the 14 confusion pairs (one scenario line each; the student names the side). Log any misses to the error log.""",
 """## Round 3: Techniques (20 min)

ACTION: Give 15 scenario cues; the student names the technique. Target 13 or more correct.""",
 """## Round 4: Flashcards (20 min)

ACTION: Read [flashcards.md](workspace/flashcards.md) and quiz the 25 most important cards (prioritize ones tied to error-log topics). Report the hit rate."""],
 'takeaways': ['Consolidate, don\'t cram.', 'Sleep beats one more mock.'],
 'success': ['All four rounds completed', 'Final hit rates recorded'],
},
{
 'id': '9.11', 'slug': 'exam-day-playbook', 'title': 'Exam-day playbook & confidence', 'week': 13, 'minutes': 45, 'reading_min': 0, 'ka': 'GEN', 'type': 'lesson',
 'teaser': 'Logistics, mindset, and your personal playbook.',
 'prepare': ['../CBAP-Roadmap.md', 'progress/progress.json'],
 'hook': """You made it. Thirteen weeks, 30 tasks, 50 techniques, three mocks, and a whole Click & Collect initiative. Let's make exam day boringly well-prepared.""",
 'teach': [
  {'title': 'Logistics (from the IIBA handbook)',
   'points': ['Government-issued photo ID, original and valid, in western characters; your name must match exactly in IIBA, PSI and on the ID (fix any mismatch at least 1 week before).',
              'Online proctored: personal computer (not a company laptop), system compatibility check done in advance, quiet room and clear desk. At a test center: arrive early and expect security wanding.',
              'Schedule: sleep, a light meal, water. No new material in the last 24 hours.'],
   'check': 'Have you done the PSI system compatibility check (if online), and does your ID name match your IIBA profile exactly?',
   'expect': 'Yes / will do'}
 ],
 'apply': [
  {'title': 'Your one-page playbook',
   'brief': 'Your personal plan for the 210 minutes.',
   'files': ['progress/error-log.md'],
   'ask': 'Tell me your pacing checkpoints, your 3 personal traps (from the error log), and your reset routine if you panic.',
   'action': 'Write a one-page playbook: logistics checklist, pacing (Q40 about 65 min, Q80 about 135 min, Q120 about 195 min + 15 min flags), the 4-step method, the student\'s top 3 personal traps with their rules, a reset routine (breathe, flag, move on), and after-exam next steps (claim the digital badge; 60 CDUs over 3 years for recertification).',
   'output': '90-exam-day-playbook.md'}
 ],
 'takeaways': ['You\'re prepared: content, technique and logistics.', 'Trust the BABOK logic. Choose the answer that serves value and follows the task\'s purpose.'],
 'success': ['Logistics confirmed', 'workspace/90-exam-day-playbook.md created', 'progress.json marked complete'],
},
]}
