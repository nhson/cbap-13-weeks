# Lesson 6.8: 7.5 Define Design Options

*Module 6 · Week 8 · ~80 min in session + ~15 min reading*

## Prepare (instructor: read silently before teaching)
- [Define Design Options](CBAP%20Knowledge%20Graph/03%20Tasks/Define%20Design%20Options.md)
- [Design Options](CBAP%20Knowledge%20Graph/04%20Inputs%20%26%20Outputs/Design%20Options.md)
- [Vendor Assessment](CBAP%20Knowledge%20Graph/05%20Techniques/Vendor%20Assessment.md)
- [13-vendor-proposals](case-files/13-vendor-proposals.md)

---

Three vendors are circling. Elena liked ShelfWise's demo. Before anyone chooses, you define the **design options** properly: **7.5 Define Design Options**.

By the end of this session you will be able to:
- Know the 4 elements of 7.5
- Describe solution approaches (create, purchase, combination)
- Allocate requirements to solution components and releases

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Define Design Options

ACTION: Re-read [Define Design Options](CBAP%20Knowledge%20Graph/03%20Tasks/Define%20Design%20Options.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Purpose (in our words): Work out the possible solution approaches, allocate requirements to components, and describe the design options.
- Elements: Define Solution Approaches (create, purchase, combination), Identify Improvement Opportunities (increase efficiencies, improve access to information, identify additional capabilities), Requirements Allocation (to solution components and releases), Describe Design Options.
- Inputs: Change Strategy, Requirements (validated, prioritized), Requirements Architecture. Output: Design Options.
- Design options are not final. Each is evaluated in 7.6.

STOP: Which RLCM and RADD states must requirements have to be input to 7.5?

USER: Validated and prioritized

ACTION: Give feedback. A strong answer includes: Requirements (validated, prioritized).

---

## Apply it at GreenBasket: Describe three design options

Turn vendor brochures into BA design options.

ACTION: Open and skim [13-vendor-proposals](case-files/13-vendor-proposals.md), [07-it-landscape](case-files/07-it-landscape.md), [54-validation-matrix](workspace/54-validation-matrix.md). Share the links and summarize the relevant facts in 3–5 bullets. Don't solve the exercise.

STOP: For ShelfWise (purchase), CodeHarbor (create) and OmniGrocer (combination): describe the design option, allocate the Must requirements (which components or releases meet them; which gaps remain), and list improvement opportunities each creates.

USER: Drafts their analysis in the chat

ACTION: Coach and save a design options document with an allocation matrix (requirement × option: meets / partial / gap / release). ShelfWise gaps: per-item substitution, temperature logging, coupons, WCAG, security review time. CodeHarbor: time, cost, PCI scope, the Harvest history. OmniGrocer: coupons need a +$40k module. Save the result to `workspace/56-design-options.md` and link it: [56-design-options.md](workspace/56-design-options.md).

ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `anil-architect`, giving it the path `workspace/56-design-options.md` and check allocation and integration assumptions. Relay the review to the student in 3–6 lines.

STOP: How would you respond to that feedback? What would you change?

USER: Responds; optionally asks you to update the file

[If the student wants changes, update the workspace file.]

---

## Exam drill

QUIZ: 10 CBAP-style questions on: 7.5 elements, solution approaches, improvement opportunities, requirements allocation, inputs and output.
Build distractors from these traps: design options chosen in 7.5 (choice happens in 7.6); input requirements merely verified; allocation only to software.
Log to scores.csv with ka=`RADD` and topic=`7.5`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Solution approaches: create, purchase, combination.
2. Allocate requirements to components and releases.
3. Input: Requirements (validated, prioritized); output: Design Options.

**Reading before the next session:**
- BABOK 7.5 (pp.152–156), 10.49 Vendor Assessment
- Jonasson 8.3.5 (pp.214–218)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- 7.5 elements? :: Define Solution Approaches; Identify Improvement Opportunities; Requirements Allocation; Describe Design Options
- Solution approaches (7.5)? :: Create, purchase, combination of both

ACTION: Update [progress.json](progress/progress.json): add this lesson (`6.8`) to `completed` with today's date and minutes ≈ 80, set `current` to `6.9`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 6.9: 7.6 Analyze Potential Value and Recommend Solution. Score the options and make the call, even if it isn't the sponsor's favourite.

STOP: Ready for 6.9? Type `/next` (or `/start 6.9`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] workspace/56-design-options.md created and architect-reviewed
- [ ] Drill logged; task card added
