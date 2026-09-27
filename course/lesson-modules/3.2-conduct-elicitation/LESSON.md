# Lesson 3.2: 4.2 Conduct Elicitation: live interview with Kim

*Module 3 · Week 4 · ~90 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Conduct Elicitation](CBAP%20Knowledge%20Graph/03%20Tasks/Conduct%20Elicitation.md)
- [Interviews](CBAP%20Knowledge%20Graph/05%20Techniques/Interviews.md)
- [Observation](CBAP%20Knowledge%20Graph/05%20Techniques/Observation.md)
- [Elicitation Results (unconfirmed)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Elicitation%20Results%20%28unconfirmed%29.md)
- [STAKEHOLDERS](company-context/stakeholders/STAKEHOLDERS.md)
- [02-harvest-postmortem](case-files/02-harvest-postmortem.md)

---

Today you don't just read about elicitation. You do it. I'll play **Kim Tran**, a picker at Riverton Central. Kim knows exactly why picking failed in Harvest, but only shares it with an interviewer who earns trust and asks good questions.

By the end of this session you will be able to:
- Explain the elements of 4.2 (guide the activity, capture outcomes)
- Run a structured interview with open and closed questions
- Produce Elicitation Results (unconfirmed)

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Conduct Elicitation

ACTION: Re-read [Conduct Elicitation](CBAP%20Knowledge%20Graph/03%20Tasks/Conduct%20Elicitation.md), [Interviews](CBAP%20Knowledge%20Graph/05%20Techniques/Interviews.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Run the elicitation activity: draw out and explore information with stakeholders or from sources, and record what comes out of it.
- Elements: Guide Elicitation Activity (keep to scope, probe, watch for new information) and Capture Elicitation Outcomes.
- Input: Elicitation Activity Plan. Output: Elicitation Results (unconfirmed). 18 techniques are listed, the most of any E&C task.
- Interview tips: prepare goals and questions; open questions to explore and closed questions to confirm; build rapport; don't lead; summarize and confirm at the end.
- Observation: active/noticeable (asking questions) vs passive/unnoticeable (just watching). It reveals tacit knowledge and workarounds.

STOP: Give me one open question and one closed question you might ask Kim.

USER: Two example questions

ACTION: Give feedback. A strong answer includes: open, e.g. "Walk me through picking a big order on a Saturday". Closed, e.g. "Did the handhelds last a full shift?". Avoid leading questions like "The scanners were the main problem, right?".

---

## Apply it at GreenBasket: The interview (role-play)

ACTION: Role-play as **Kim Tran** (picker, 4 years, low power, high interest, did Harvest trial picks) for the next exchange. Rules for playing Kim:
- Start friendly but guarded: "Is this another head-office thing? Last time nobody read my list."
- Share information in proportion to question quality. Open, non-leading questions earn detail; leading or closed-only questions get short answers.
- Facts Kim knows (reveal only when asked well): aisle locations wrong after resets; no substitution guidance; handheld battery ~2 h; chilled items warm by the end; Saturday rush; unclear whether picking counts in productivity targets; totes by temperature zone would help; a dedicated early-morning picker schedule works best; 17-year-old evening staff can't hand over alcohol; a staging cooler is needed; one-lap picking is impossible for orders over 40 items in big stores.
- If the student confirms and summarizes at the end, Kim warms up and offers to show them on the shop floor (observation).
Stay in character until the student says "end interview".

STOP: You're sitting with Kim in the break room with 30 minutes. Start the interview. Type "end interview" when you're done.

USER: Conducts a multi-turn interview

ACTION: Step out of character. Debrief: what went well (rapport, open questions, probing, summarizing) and what was missed (list the facts not uncovered). Then write the elicitation results as **unconfirmed** notes: source, date, technique, verbatim quotes, observations, open questions. Save the result to `workspace/21-elicitation-results-kim-unconfirmed.md` and link it: [21-elicitation-results-kim-unconfirmed.md](workspace/21-elicitation-results-kim-unconfirmed.md).

A model answer should cover (use it to coach, don't just paste it):
- Rapport first; acknowledge the ignored 2024 list
- Open questions on the end-to-end picking flow; probing on "why" for delays
- Captured facts about data, devices, temperature, peaks and incentives
- Summarized at the end and asked to observe a pick (experiment/observation)

**Discovery:** The unconfirmed results already contradict Rosa's 2024 interview ("15 minutes", "stock mostly fine"). Next lesson you confirm which is right.

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 4.2 Conduct Elicitation, interview technique (question types, structured vs unstructured), observation types, capturing outcomes.
Build distractors from these traps: results from 4.2 labelled confirmed; leading questions; passive observation when you need to understand reasons; interviews for large dispersed populations (survey is better).
Log to scores.csv with ka=`E&C` and topic=`4.2`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. 4.2 = guide the activity plus capture outcomes; the output is **unconfirmed**.
2. Open questions explore; closed questions confirm; never lead.
3. Observation uncovers tacit knowledge that interviews miss.

> **Exam rule of thumb:** Large, dispersed group → survey. Tacit, hands-on work → observation. Deep individual view → interview. Group consensus → workshop.

**Reading before the next session:**
- BABOK 4.2 (pp.61–64), 10.25 Interviews, 10.31 Observation
- Jonasson 5.5–5.6 (pp.79–89)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 4.2 output? :: Elicitation Results (unconfirmed)
- Active vs passive observation? :: Active/noticeable: observer asks questions during work; passive/unnoticeable: observer watches without interrupting
- 4.2 elements? :: Guide Elicitation Activity; Capture Elicitation Outcomes

ACTION: Update [progress.json](progress/progress.json): add this lesson (`3.2`) to `completed` with today's date and minutes ≈ 90, set `current` to `3.3`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 3.3: 4.3 Confirm Elicitation Results. Compare against sources and other results. Who was right about pick time?

STOP: Ready for 3.3? Type `/next` (or `/start 3.3`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student conducted a multi-turn interview
- [ ] Debrief given with missed facts
- [ ] workspace/21-elicitation-results-kim-unconfirmed.md created
- [ ] Drill logged; task card added
