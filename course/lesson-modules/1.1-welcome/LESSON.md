# Lesson 1.1: Welcome to GreenBasket & your CBAP game plan

*Module 1 · Week 1 · ~60 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [SCENARIO](company-context/SCENARIO.md)
- [COMPANY](company-context/COMPANY.md)
- [Exam Blueprint](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Exam%20Blueprint.md)
- [CBAP-Roadmap](../CBAP-Roadmap.md)

---

Welcome to GreenBasket Markets. It's your first day as Senior Business Analyst, and your inbox already has a problem in it.

Over the next 13 weeks you'll do two things at once: **pass the CBAP exam**, and **take GreenBasket's "Click & Collect" initiative from messy idea to evaluated pilot**, using every BABOK knowledge area along the way. The exam tests whether you can *apply* BABOK in scenarios, and that's exactly what you'll practise here.

How this works: I teach a concept, you apply it to GreenBasket, and then I test you with exam-style questions. Your work goes in `workspace/`, your scores go in `progress/`, and the whole BABOK lives as a linked knowledge graph in `CBAP Knowledge Graph/`.

By the end of this session you will be able to:
- Explain the CBAP exam format and blueprint weights
- Know how the course, commands and files work
- Set your exam date and weekly study rhythm
- Meet the GreenBasket scenario

STOP: Before we start: what should I call you, and have you booked (or planned) your exam date yet?

USER: Ready

---

## Part 1: The exam you are training for

ACTION: Re-read [Exam Blueprint](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Exam%20Blueprint.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- 120 multiple-choice questions in 210 minutes (about 1:45 per question). Questions are scenario-based and case-study based and test application, not recall. Based on BABOK v3.
- Blueprint: RADD 30%, RLCM 15%, SA 15%, BAPM 14%, SE 14%, E&C 12%. Techniques (Ch 10) are woven through all of them and underpin roughly a third of question content.
- Case-study questions give a long scenario followed by several questions. Several answers are "good" and one is *most BABOK-correct*.
- Eligibility reminder: 7,500 BA hours in 10 years, 900 hours in 4 of the 6 KAs, 35 PD hours, 2 references. The application is valid for 1 year, with up to 3 attempts.

STOP: Quick gut check: based on those weights, where should most of your study hours go, and which KA is the smallest?

USER: RADD most; E&C smallest

ACTION: Give feedback. A strong answer includes: RADD at 30% (≈36 questions) is more than double any other KA; E&C is 12% but its techniques appear everywhere, so it is not skippable.

---

## Part 2: How this course works

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Commands: `/next` continues, `/start 2.3` jumps to a lesson, `/progress` shows the dashboard, `/drill RADD 10` runs a quick quiz, `/grade mock-1` marks a written exam.
- Each lesson follows teach → apply at GreenBasket → exam drill → wrap-up, and takes about 60–90 minutes. Reading assignments come from BABOK, Lessing and Jonasson.
- Stakeholder reviewers are available as agents: Elena (sponsor), Marcus (store ops, sceptical), Anil (architect), Priyanka (QA), and a strict CBAP examiner.
- The error log is your most valuable file. Every miss gets a "rule to remember".
- The 13-week plan: Foundations (1–2), BAPM (3), E&C (4), RLCM (5), SA (6), RADD (7–8), SE (9), Consolidation (10), Mock exams (11–13).

STOP: Which of those reviewers do you think will give you the hardest time, and why?

USER: Any, usually Marcus or the examiner

---

## Apply it at GreenBasket: Your first read of the situation

Elena's kickoff email is waiting. Don't analyze it formally yet (that's the next lesson). Just take a BA's first look.

ACTION: Open and skim [01-sponsor-kickoff-email](case-files/01-sponsor-kickoff-email.md), [SCENARIO](company-context/SCENARIO.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Read the email. In 3 bullets: what is the real **need** behind it, what are **solutions** being assumed, and what worries you?

USER: Drafts their analysis in the chat

ACTION: Coach the answer: separate need (losing share and visit frequency, convenience gap) from assumed solutions (ShelfWise, real-time stock, one-lap rule, slick app). Then create the student's study contract with their name, exam date, weekly rhythm (for example 5×1 h weekdays + 2×2.5 h weekend), the 3 biggest risks to their study plan, and their answers here. Save the result to `workspace/00-study-contract.md` and link it: [00-study-contract.md](workspace/00-study-contract.md).

A model answer should cover (use it to coach, don't just paste it):
- Need: GreenBasket is losing share (18.2% → 14.1%) and visit frequency, driven by a convenience gap versus competitors
- Assumed solutions: ShelfWise, "real-time stock", "slick app", one-lap picking rule
- Worries: Harvest history, store resistance, unrealistic timeline, data quality

**Discovery:** Elena already has a vendor in mind. Spotting *solutions disguised as requirements* is one of the most tested BA instincts.

---

## Set up your progress

ACTION: Update [progress.json](progress/progress.json): set `student` to the student's name, `start_date` to today, and `exam_date` to their target (or 13 weeks from today if unknown). Confirm the dates back to them.

STOP: Is the weekly rhythm in your study contract realistic for your life right now? If not, let's adjust it before week 1 gets busy.

USER: Confirms or adjusts

---

## Wrap-up

**Key takeaways:**
1. The CBAP tests application of BABOK v3 in scenarios. Aim for the *most BABOK-correct* answer.
2. RADD (30%) is the biggest area. Techniques run across all KAs.
3. Separate the **need** from the **solutions** people bring you. You did it on day one.

> **Exam rule of thumb:** When a stakeholder hands you a solution, the BA move is to understand the underlying need first.

**Reading before the next session:**
- Lessing ch.1–4 (planning for success, exam format), pp.6–45: skim
- CBAP Handbook section 6 (exam structure): already summarized in [CBAP-Roadmap.md](../CBAP-Roadmap.md)
- Admin: join IIBA (free BABOK access), start the CBAP application, check your 35 PD hours

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- CBAP exam length? :: 120 questions, 210 minutes
- Largest KA by weight? :: RADD, 30%
- CBAP eligibility hours? :: 7,500 BA hours in 10 yrs, 900 in 4 of 6 KAs, 35 PD hours, 2 references

ACTION: Update [progress.json](progress/progress.json): add this lesson (`1.1`) to `completed` with today's date and minutes ≈ 60, set `current` to `1.2`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 1.2: The BACCM: six lenses on every change. The six core concepts that every BABOK task is built on.

STOP: Ready for 1.2? Type `/next` (or `/start 1.2`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student knows the format and blueprint weights
- [ ] Student knows the commands and file layout
- [ ] progress.json has name, start date and exam date
- [ ] workspace/00-study-contract.md exists
- [ ] Student separated need from assumed solutions in the kickoff email
