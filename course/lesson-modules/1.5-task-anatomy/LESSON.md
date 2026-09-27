# Lesson 1.5: Anatomy of a BABOK task & how to study the Guide

*Module 1 · Week 1 · ~90 min in session + ~60 min reading*

## Prepare (instructor: read silently before teaching)
- [Plan Business Analysis Approach](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Approach.md)
- [Business Analysis Planning and Monitoring](CBAP%20Knowledge%20Graph/02%20Knowledge%20Areas/Business%20Analysis%20Planning%20and%20Monitoring.md)
- [00 CBAP Knowledge Graph](CBAP%20Knowledge%20Graph/00%20CBAP%20Knowledge%20Graph.md)
- [Technique-Task Matrix](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Technique-Task%20Matrix.md)

---

All 30 BABOK tasks share one skeleton: **Purpose, Description, Inputs, Elements, Guidelines & Tools, Techniques, Stakeholders, Outputs.** Once you see it, the 500-page guide becomes a well-organized database. It's also how your knowledge graph is built.

By the end of this session you will be able to:
- Name the 8 parts of every task and what each tells you
- Tell inputs apart from guidelines and tools
- Navigate the knowledge graph and the BABOK efficiently
- Know the 6 KAs, their 30 tasks and the order they are usually studied in

STOP: Ready to dive in?

USER: Ready

---

## Part 1: The task skeleton

ACTION: Re-read [Plan Business Analysis Approach](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Approach.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose: why the task exists. Memorize one sentence per task; exam options paraphrase it.
- Inputs: information *consumed and transformed* by the task (often with a state, e.g. "Requirements (verified)"). Outputs: what the task *produces*.
- Guidelines and tools: information that *shapes* how the task is done but isn't transformed (e.g. the Business Analysis Approach guides many tasks).
- Elements: the key concepts or activities of the task. Techniques: *how* you might do it. Stakeholders: who typically takes part.
- The BABOK is not a sequential process. Tasks can be done in any order, iteratively and concurrently.

STOP: In Plan Business Analysis Approach, "Needs" is an input and "Business Analysis Performance Assessment" is a guideline. What is the difference in plain words?

USER: Input is what the task works on; guideline influences how it is done

ACTION: Give feedback. A strong answer includes: inputs are transformed into outputs; guidelines and tools inform or constrain the work without being transformed.

**Exam trap to call out:** Questions ask "which is an INPUT to task X?" and list guidelines as distractors.

---

## Part 2: Map of the territory

ACTION: Re-read [Technique-Task Matrix](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Technique-Task%20Matrix.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- 6 KAs and 30 tasks: BAPM (5), E&C (5), RLCM (5), SA (4), RADD (6), SE (5).
- KAs are *not* phases. For example, Strategy Analysis can happen before, during and after a project.
- 50 techniques. Some are used everywhere (Interviews, Workshops, Document Analysis, Risk Analysis and Management), others in only one or two tasks.
- Perspectives (Agile, BI, IT, Business Architecture, BPM) are lenses. Underlying competencies are the BA's skills.
- Study method: for each task, know the purpose, element names, inputs and outputs (with states), 3–5 signature techniques, and key stakeholders.

STOP: Which KA has only 4 tasks, and which has 6?

USER: SA has 4, RADD has 6

ACTION: Give feedback. A strong answer includes: SA = 4 (Analyze Current State, Define Future State, Assess Risks, Define Change Strategy); RADD = 6.

---

## Apply it at GreenBasket: Build your one-page task card template

You will fill one task card per task over the next weeks. They are your revision sheets for weeks 11–13.

ACTION: Open and skim [Plan Business Analysis Approach](CBAP%20Knowledge%20Graph/03%20Tasks/Plan%20Business%20Analysis%20Approach.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Using the Plan Business Analysis Approach note, fill in a task card: purpose (in your own words), elements, inputs, guidelines, top 5 techniques, stakeholders, outputs, and "who uses my output next". What surprised you?

USER: Drafts their analysis in the chat

ACTION: Check the card against the note, correct any wrong names, and save it as the first card. Include a blank template at the top of the file for future cards. Save the result to `workspace/task-cards.md` and link it: [task-cards.md](workspace/task-cards.md).

A model answer should cover (use it to coach, don't just paste it):
- Purpose (in our words): Decide how business analysis will be carried out on this initiative: the overall method, its formality, the activities, their timing, and how the approach gets agreed.
- Elements: planning approach, formality and level of detail, BA activities, timing, complexity and risk, acceptance
- Input: Needs; output: Business Analysis Approach, used by 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.4, 4.5, 6.1…

---

## Exam drill

QUIZ: 8 CBAP-style questions on: task structure (inputs vs guidelines vs outputs), KA/task counts, BABOK as non-sequential, perspectives and competencies as concepts.
Build distractors from these traps: guideline listed as input; KAs treated as sequential phases; wrong task-to-KA mapping.
Log to scores.csv with ka=`FND` and topic=`babok-structure`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Every task: purpose, description, inputs, elements, guidelines and tools, techniques, stakeholders, outputs.
2. Inputs are transformed; guidelines shape the work.
3. KAs are not phases. Tasks are iterative and concurrent.

> **Exam rule of thumb:** Know each output's *state label*. It often decides between two otherwise-good options.

**Reading before the next session:**
- BABOK 1.4 Structure (pp.3–10)
- Lessing ch.3 Study Tools (pp.31–40)
- Jonasson ch.2–3 (pp.11–31): skim for context

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Eight parts of every BABOK task? :: Purpose, Description, Inputs, Elements, Guidelines and Tools, Techniques, Stakeholders, Outputs
- Tasks per KA? :: BAPM 5, E&C 5, RLCM 5, SA 4, RADD 6, SE 5
- Are KAs sequential phases? :: No, tasks can be performed in any order, iteratively and concurrently

ACTION: Update [progress.json](progress/progress.json): add this lesson (`1.5`) to `completed` with today's date and minutes ≈ 90, set `current` to `1.6`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 1.6: Diagnostic exam (50 questions). Find your baseline. No pressure, no studying for it.

STOP: Ready for 1.6? Type `/next` (or `/start 1.6`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student can name the 8 task parts
- [ ] Student distinguishes input from guideline
- [ ] workspace/task-cards.md created with template plus the 3.1 card
- [ ] Drill completed and logged
