# Lesson 8.6: Perspectives II: Business Architecture & Business Process Management

*Module 8 · Week 10 · ~70 min in session + ~25 min reading*

## Prepare (instructor: read silently before teaching)
- [The Business Architecture Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Business%20Architecture%20Perspective.md)
- [The Business Process Management Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Business%20Process%20Management%20Perspective.md)

---

Two enterprise-level lenses: **business architecture** (how the enterprise is structured to deliver strategy) and **BPM** (continuous process improvement).

By the end of this session you will be able to:
- Explain business architecture reference models and techniques
- Explain BPM frameworks, methodologies (Lean, Six Sigma, TOC, TQM, BPR) and techniques (SIPOC, DMAIC…)

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Business Architecture

ACTION: Re-read [The Business Architecture Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Business%20Architecture%20Perspective.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Models the enterprise to show how strategic concerns are met: capabilities, value streams, information, organization.
- Reference models: ACORD, Business Motivation Model, COBIT, FEA, ITIL, APQC PCF, SCOR, VRM. Techniques: capability map, value mapping, customer journey map, roadmap, TOGAF, Zachman, project portfolio analysis.

STOP: Which technique shows the end-to-end value a customer receives, stage by stage?

USER: Value mapping / value stream

ACTION: Give feedback. A strong answer includes: value mapping (value streams). The customer journey map is the customer's experiential view.

---

## Part 2: BPM

ACTION: Re-read [The Business Process Management Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Business%20Process%20Management%20Perspective.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- BPM: design, execution, monitoring and optimization of processes end to end.
- Methodologies: Lean (waste), Six Sigma (variation; DMAIC for existing processes, DMADV for new ones), Theory of Constraints (bottlenecks; drum-buffer-rope), TQM, BPR (radical redesign), continuous improvement, adaptive case management.
- Techniques: SIPOC, value stream analysis, cycle-time analysis, FMEA, Kaizen event, process simulation, 5 Whys / 5Ws.

STOP: Improving an existing picking process with measurable defects: DMAIC or DMADV?

USER: DMAIC

ACTION: Give feedback. A strong answer includes: DMAIC (Define, Measure, Analyze, Improve, Control) for existing processes.

---

## Exam drill

QUIZ: 10 CBAP-style questions on: Business Architecture and BPM perspectives: reference models, methodologies, techniques.
Log to scores.csv with ka=`PERSP` and topic=`persp-2`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. Business architecture = enterprise blueprint; BPM = process improvement.
2. DMAIC improves existing processes; DMADV designs new ones.

**Reading before the next session:**
- BABOK 11.4–11.5 (pp.408–440)

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- DMAIC vs DMADV? :: DMAIC improves an existing process; DMADV designs a new process/product
- SIPOC? :: Suppliers, Inputs, Process, Outputs, Customers

ACTION: Update [progress.json](progress/progress.json): add this lesson (`8.6`) to `completed` with today's date and minutes ≈ 70, set `current` to `8.7`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 8.7: Underlying competencies deep-dive + consolidation quiz. Name the competency behind the behaviour, then a 30-question consolidation.

STOP: Ready for 8.7? Type `/next` (or `/start 8.7`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student distinguishes BA and BPM perspectives
- [ ] Drill logged
