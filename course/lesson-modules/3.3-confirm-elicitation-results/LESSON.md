# Lesson 3.3: 4.3 Confirm Elicitation Results

*Module 3 · Week 4 · ~70 min in session + ~20 min reading*

## Prepare (instructor: read silently before teaching)
- [Confirm Elicitation Results](CBAP%20Knowledge%20Graph/03%20Tasks/Confirm%20Elicitation%20Results.md)
- [Elicitation Results (confirmed)](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Elicitation%20Results%20%28confirmed%29.md)
- [Commonly Confused Concepts](CBAP%20Knowledge%20Graph/08%20Exam%20Lens/Commonly%20Confused%20Concepts.md)
- [09-interview-transcript-rosa](case-files/09-interview-transcript-rosa.md)
- [03-store-ops-process-notes](case-files/03-store-ops-process-notes.md)

---

Rosa said picking takes 15 minutes. The store's own data says 18–41. Kim says it's worse on Saturdays. The Harvest contractor wrote "confirmed". Confirming is exactly what they failed to do. Today: **4.3 Confirm Elicitation Results**.

By the end of this session you will be able to:
- Explain the two elements of 4.3
- Distinguish confirm vs verify vs validate
- Resolve contradictions between sources

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Confirm Elicitation Results

ACTION: Re-read [Confirm Elicitation Results](CBAP%20Knowledge%20Graph/03%20Tasks/Confirm%20Elicitation%20Results.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Check that what was elicited is accurate and consistent, by comparing it with sources and with other results.
- Elements: Compare Elicitation Results Against Source Information, and Compare Elicitation Results Against Other Elicitation Results.
- Input: Elicitation Results (unconfirmed). Guidelines: Elicitation Activity Plan, Existing BA Information. Output: Elicitation Results (confirmed).
- Techniques: document analysis, interviews, reviews, workshops.

STOP: How is confirming different from verifying requirements (7.2)?

USER: Confirm = accurate understanding of what stakeholders said; verify = requirement quality

ACTION: Give feedback. A strong answer includes: confirm checks the BA captured information accurately and consistently. Verify checks that specified requirements are well-formed (quality characteristics).

**Exam trap to call out:** Answers saying "validate the elicitation results" are usually wrong. Confirm is the BABOK word here.

---

## Apply it at GreenBasket: Reconcile the sources

Three sources disagree about the current process.

ACTION: Open and skim [09-interview-transcript-rosa](case-files/09-interview-transcript-rosa.md), [03-store-ops-process-notes](case-files/03-store-ops-process-notes.md), [21-elicitation-results-kim-unconfirmed](workspace/21-elicitation-results-kim-unconfirmed.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: Build a comparison: for pick time, stock accuracy, where chilled/frozen go, which till is used, alcohol on phone orders, and who picks and when, note what each source says, the contradiction, and how you would confirm it (which technique, with whom).

USER: Drafts their analysis in the chat

ACTION: Coach it and save a confirmation matrix, then a "confirmed results" section for the items that the data or documents settle (e.g. pick times are 18–41 min per the store table; the manual is outdated per Rosa's own notes). Mark items still needing confirmation with owners. Save the result to `workspace/22-elicitation-results-confirmed.md` and link it: [22-elicitation-results-confirmed.md](workspace/22-elicitation-results-confirmed.md).

A model answer should cover (use it to coach, don't just paste it):
- Pick time: manual silent, Rosa said 15, the table shows 18–41 → confirmed as 18–41, driven by day of week
- Stock accuracy "mostly fine" vs IT 82% (74% fresh) → confirmed not fine for fresh
- Frozen goes to the front ice-cream freezer, not the back cooler (margin note) → cold-chain risk to confirm by observation
- Alcohol: unwritten head-office rule → confirm with Janet

**Discovery:** The Harvest contractor wrote "confirmed" after a single interview. Confirmation means comparing against source information and other results.

---

## Exam drill

QUIZ: 8 CBAP-style questions on: 4.3 Confirm Elicitation Results and the confirm vs verify vs validate distinction.
Build distractors from these traps: confirm = validate; confirmed results produced by 4.2; confirmation requires formal sign-off.
Log to scores.csv with ka=`E&C` and topic=`4.3`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Confirm = accuracy and consistency against sources and other results.
2. Output: Elicitation Results (confirmed).
3. Confirm ≠ verify ≠ validate.

> **Exam rule of thumb:** Contradictions between stakeholders → compare against sources and other results (4.3) before specifying anything.

**Reading before the next session:**
- BABOK 4.3 (pp.65–66)
- Lessing pp.125–128

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 4.3 elements? :: Compare against Source Information; Compare against Other Elicitation Results
- Confirm vs verify? :: Confirm = captured information accurate and consistent (4.3); verify = requirement quality (7.2)

ACTION: Update [progress.json](progress/progress.json): add this lesson (`3.3`) to `completed` with today's date and minutes ≈ 70, set `current` to `3.4`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 3.4: 4.4 Communicate Business Analysis Information. Same findings, three audiences: Elena, Marcus, the vendors.

STOP: Ready for 3.4? Type `/next` (or `/start 3.4`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Confirmation matrix built
- [ ] workspace/22-elicitation-results-confirmed.md created
- [ ] Student distinguishes confirm, verify and validate
- [ ] Drill logged; task card added
