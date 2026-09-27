# CBAP in 13 Weeks: Interactive Course

An interactive CBAP course taught by Claude, modelled on the "learn by doing inside your AI tool" format of [free-ai-courses](https://github.com/carlvellotti/free-ai-courses). You spend 13 weeks as the Senior BA on **GreenBasket Markets' Click & Collect** initiative, applying every BABOK v3 knowledge area to one continuous case while training for the exam.

## Start
1. Open a terminal in this folder (`learn-with-ai/`).
2. Run `claude`.
3. Type `/start 1.1`. After that, `/next` always resumes where you left off.

| Command | What it does |
|---|---|
| `/start 2.3` | Jump to a specific lesson |
| `/next` | Continue with the next lesson |
| `/progress` | Dashboard: schedule, scores by KA, weak topics |
| `/drill RADD 10` | Quick exam drill (adaptive if no arguments) |
| `/grade mock-1` | Grade a written diagnostic or mock exam |

## What a lesson looks like
**Teach** (short, Socratic) → **Apply at GreenBasket** (you produce a real BA artifact in `workspace/`, often reviewed by a stakeholder persona) → **Exam drill** (CBAP-style questions, logged) → **Wrap-up** (takeaways, flashcards, reading, progress saved).

## Structure (75 lessons, about 10 h/week)
| Module | Weeks | Focus |
|---|---|---|
| 1 Foundations | 1–2 | BACCM, classification, roles, task anatomy, diagnostic exam, I/O backbone |
| 2 BAPM (14%) | 3 | 3.1–3.5 + techniques lab + 40-question drill |
| 3 E&C (12%) | 4 | 4.1–4.5 incl. a live interview role-play + techniques lab + drill |
| 4 RLCM (15%) | 5 | 5.1–5.5 incl. the CR-017 change request + lab + drill |
| 5 SA (15%) | 6 | 6.1–6.4 + business case (NPV/IRR) + strategy lab + drill |
| 6 RADD (30%) | 7–8 | 7.1 (3 modelling labs), 7.2–7.6, 2 technique labs, 2 drills |
| 7 SE (14%) | 9 | 8.1–8.5 on real pilot data + lab + Phase 2 milestone |
| 8 Consolidation | 10 | 50 techniques in 4 families, 5 perspectives, competencies |
| 9 Exam simulation | 11–13 | Exam technique, 3 full mocks, reviews, gap sprints, exam-day playbook |

Full plan with links: [COURSE-PLAN.md](COURSE-PLAN.md) · Roadmap: [../CBAP-Roadmap.md](../CBAP-Roadmap.md)

## Sources
BABOK® Guide v3 (the backbone, via the knowledge graph), Esta Lessing's *CCBA® and CBAP® Certifications Study Guide*, and Hans Jonasson's *CBAP Certification and BABOK Study Guide*. All exam questions are original practice questions, not real IIBA exam items. Use a commercial simulator as well for calibration.
