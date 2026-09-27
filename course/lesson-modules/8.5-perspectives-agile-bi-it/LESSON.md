# Lesson 8.5: Perspectives I: Agile, Business Intelligence, Information Technology

*Module 8 · Week 10 · ~75 min in session + ~30 min reading*

## Prepare (instructor: read silently before teaching)
- [Perspectives](CBAP%20Knowledge%20Graph/07%20Perspectives/Perspectives.md)
- [The Agile Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Agile%20Perspective.md)
- [The Business Intelligence Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Business%20Intelligence%20Perspective.md)
- [The Information Technology Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Information%20Technology%20Perspective.md)

---

Case studies often set the scene: "an agile team…", "a data warehouse initiative…", "a legacy system replacement…". The perspective changes what the *best* answer is.

By the end of this session you will be able to:
- Explain each perspective's change scope, BA scope, approaches and impact on KAs
- Adjust answers to the perspective context

STOP: Ready to dive in?

USER: Ready

---

## Part 1: Agile

ACTION: Re-read [The Agile Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Agile%20Perspective.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- Mindset of values and principles; short iterations; continuous, just-in-time elaboration; the BA works with the product owner and team.
- Approaches: Crystal Clear, DAD, DSDM, Evo, XP, FDD, Kanban, SAFe, Scrum. Techniques: BDD, Kano, lightweight documentation, MoSCoW, personas, planning workshop, purpose alignment model, real options, relative estimation, retrospectives, story decomposition, story mapping, storyboarding, value stream mapping.
- Impact on KAs: planning is continuous; elicitation is ongoing; the backlog replaces formal requirement documents; SE is frequent.

STOP: In an agile context, when are detailed requirements elaborated?

USER: Just in time, close to implementation

ACTION: Give feedback. A strong answer includes: just in time: detail is added as items near the top of the backlog.

---

## Part 2: BI and IT

ACTION: Re-read [The Business Intelligence Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Business%20Intelligence%20Perspective.md), [The Information Technology Perspective](CBAP%20Knowledge%20Graph/07%20Perspectives/The%20Information%20Technology%20Perspective.md) so every name you use is BABOK-exact. Share the link(s) with the student.

Teach these points conversationally (short, concrete, GreenBasket examples where natural):
- BI: transform data into value-added information. Analytics types: descriptive, predictive, prescriptive; supply-driven vs demand-driven; structured vs unstructured data; the focus is on decisions supported.
- IT: impact of change on IT systems, from small enhancements to large implementations; methodologies (predictive/adaptive; RE, SSADM, UP); strong on NFRs, interfaces and data.

STOP: A BI project starts from "what decisions do managers need to make?". Supply-driven or demand-driven?

USER: Demand-driven

ACTION: Give feedback. A strong answer includes: demand-driven: starts from information needs and decisions.

---

## Exam drill

QUIZ: 10 CBAP-style questions on: Agile, BI and IT perspectives: scope, methods, techniques, impact on KAs.
Log to scores.csv with ka=`PERSP` and topic=`persp-1`.

STOP: Before we wrap up, which question felt shakiest, and why?

USER: Names one

ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.

---

## Wrap-up

**Key takeaways:**
1. A perspective shifts the best answer: agile = just in time; BI = decisions and data; IT = systems impact.

**Reading before the next session:**
- BABOK 11.1–11.3 (pp.368–407): read the "Impact on Knowledge Areas" sections closely

ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:
- BI analytics types? :: Descriptive, predictive, prescriptive
- Supply- vs demand-driven BI? :: Supply = start from available data; demand = start from information needs/decisions

ACTION: Update [progress.json](progress/progress.json): add this lesson (`8.5`) to `completed` with today's date and minutes ≈ 75, set `current` to `8.6`, and update `weak_topics` if the drill exposed any.

**Next up:** Lesson 8.6: Perspectives II: Business Architecture & Business Process Management. Enterprise-level models and process improvement.

STOP: Ready for 8.6? Type `/next` (or `/start 8.6`) whenever you are. Short break first is a good idea.

USER: /next

---

## Success Criteria
- [ ] Student distinguishes the three perspectives
- [ ] Drill logged
