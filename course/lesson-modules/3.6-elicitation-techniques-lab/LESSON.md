# Lesson 3.6: Elicitation techniques lab: choosing the right technique

*Module 3 · Week 4 · ~80 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Workshops](CBAP%20Knowledge%20Graph/05%20Techniques/Workshops.md)
- [Focus Groups](CBAP%20Knowledge%20Graph/05%20Techniques/Focus%20Groups.md)
- [Survey or Questionnaire](CBAP%20Knowledge%20Graph/05%20Techniques/Survey%20or%20Questionnaire.md)
- [Observation](CBAP%20Knowledge%20Graph/05%20Techniques/Observation.md)
- [Brainstorming](CBAP%20Knowledge%20Graph/05%20Techniques/Brainstorming.md)
- [Prototyping](CBAP%20Knowledge%20Graph/05%20Techniques/Prototyping.md)
- [Interface Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Interface%20Analysis.md)
- [Benchmarking and Market Analysis](CBAP%20Knowledge%20Graph/05%20Techniques/Benchmarking%20and%20Market%20Analysis.md)

---

"Which technique should the BA use?" is one of the most common exam question types. Today you learn the *selection logic*, the strengths and limitations that decide between look-alike techniques.

By the end of this session you will be able to:
- Select elicitation techniques by situation
- Know key strengths and limitations of each
- Design a workshop and a survey

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Selection logic

ACTION: Re-read [Workshops](CBAP%20Knowledge%20Graph/05%20Techniques/Workshops.md), [Focus Groups](CBAP%20Knowledge%20Graph/05%20Techniques/Focus%20Groups.md), [Survey or Questionnaire](CBAP%20Knowledge%20Graph/05%20Techniques/Survey%20or%20Questionnaire.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Workshops: a structured, facilitated event to reach decisions or consensus; roles are sponsor, facilitator, scribe, timekeeper and participants. Can be dominated by strong voices.
- Focus groups: 6–12 pre-qualified participants with a moderator; qualitative opinions and attitudes. Not for decisions or consensus.
- Surveys: many or dispersed respondents, quick and cheap; closed questions for statistics, open questions for depth. Low response rate and no follow-up probing.
- Observation: tacit knowledge and real workflow; people may behave differently when watched.
- Brainstorming: many ideas fast, no evaluation during generation. Prototyping: elicit and validate via a model (throw-away vs evolutionary; by purpose: proof of concept, form study, usability, visual).
- Benchmarking and market analysis: compare with best practice and competitors. Interface analysis: for each interface, what information crosses it, how, how often, why, and who owns it.

STOP: You need opinions from 400 Basket Rewards members in 3 states within a week. Technique?

USER: Survey

ACTION: Give feedback. A strong answer includes: survey or questionnaire: many respondents, geographically dispersed, time-boxed.

---

## Apply it at GreenBasket: Design Workshop #2 (the one that works)

Workshop #1 had no owners, the sponsor left after 30 minutes, and marketing felt shut down.

ACTION: Open and skim [10-workshop-notes-raw](case-files/10-workshop-notes-raw.md), [Workshops](CBAP%20Knowledge%20Graph/05%20Techniques/Workshops.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Design Workshop #2 on "substitutions and pickup experience": objective, participants, roles, agenda with timings, techniques inside the workshop (e.g. brainstorming, dot voting, collaborative game), ground rules, and expected outputs. Also write 5 survey questions to test substitution preferences with members.

USER: Drafts their analysis in the chat

ACTION: Coach it and save the design. Check: a neutral facilitator (not the BA if the BA needs to contribute), decisions captured with owners, Kim and Rosa included, and the customer voice brought in (survey data or personas). Save the result to `workspace/25-workshop-2-and-survey-design.md` and link it: [25-workshop-2-and-survey-design.md](workspace/25-workshop-2-and-survey-design.md).

---

## Exam drill

QUIZ: 12 CBAP-style questions on: choosing elicitation techniques in scenarios; strengths and limitations of interviews, workshops, focus groups, surveys, observation, brainstorming, prototyping, document analysis, benchmarking, interface analysis.
Build distractors from these traps: focus group for decisions; workshop for large dispersed groups; observation when behaviour is cognitive and not visible; prototype type mix-ups (throw-away vs evolutionary).
Log to scores.csv with ka=`TECH` and topic=`elicitation-techniques`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Decision or consensus → workshop; opinions → focus group; many or dispersed → survey; tacit → observation.
2. Know one strength and one limitation per technique.

> **Exam rule of thumb:** Read the scenario constraints (group size, geography, time, decision vs opinion). They pick the technique for you.

**Reading before the next session:**
- BABOK 10.5, 10.21, 10.31, 10.36, 10.45, 10.50
- Jonasson 5.9–5.16 (pp.92–121)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- Focus group size and purpose? :: 6–12 pre-qualified participants; qualitative opinions and attitudes; not for decisions
- Throw-away vs evolutionary prototype? :: Throw-away is discarded after eliciting; evolutionary grows into the final solution

ACTION: Update [progress.json](progress/progress.json): add this lesson (`3.6`) to `completed` with today's date and minutes ≈ 80, set `current` to `3.7`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 3.7: E&C exam drill (40 questions). Prove E&C mastery.

STOP: Ready for 3.7? Type `/next` (or `/start 3.7`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/25-workshop-2-and-survey-design.md created
- [ ] Student chose techniques correctly in drills
- [ ] Drill logged
