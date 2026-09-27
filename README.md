# CBAP in 13 Weeks

**A free, interactive study path for the IIBA® CBAP® exam.** It has 75 lessons across 13 weeks at about 10 hours a week. The lessons are built around a single realistic case, backed by a linked BABOK® v3 knowledge graph, and taught by Claude as your instructor.

🌐 **Website:** https://nhson.github.io/cbap-13-weeks

## What's inside
| | |
|---|---|
| **Course** (`course/lesson-modules/`) | 75 lessons in 9 modules: foundations, the six knowledge areas (RADD gets two weeks), consolidation, and three full mock exams |
| **Knowledge graph** (`course/CBAP Knowledge Graph/`) | 228 Obsidian notes: 6 KAs, 30 tasks, 71 inputs and outputs, 50 techniques, competencies, perspectives, and an exam lens (blueprint, I/O flow, confused pairs, technique matrix) |
| **Scenario** (`course/company-context/`, `course/case-files/`) | GreenBasket Markets: you are the Senior BA on a grocery chain's Click & Collect initiative, from kickoff to pilot evaluation |
| **Roadmap** (`CBAP-Roadmap.md`) | The 13-week plan and milestones |

## Two ways to use it
**1. Read it** on the website, or open `course/` as an Obsidian vault.

**2. Be taught it interactively** (recommended) with [Claude Code](https://claude.com/claude-code):
```bash
git clone https://github.com/nhson/cbap-13-weeks.git
cd cbap-13-weeks/course
claude
# then type:  /start 1.1
```
Claude teaches each lesson Socratically. It has you produce real BA work products for GreenBasket and reviews them as the stakeholders (sponsor, sceptical store-ops head, architect, QA, or a strict CBAP examiner). It also runs exam drills, logs your scores and error log, and generates and grades full 120-question mocks.

| Command | |
|---|---|
| `/start 2.3` | jump to a lesson |
| `/next` | resume where you left off |
| `/progress` | dashboard: schedule, scores by KA, weak topics |
| `/drill RADD 10` | quick drill (adaptive with no arguments) |
| `/grade mock-1` | grade a written diagnostic or mock |

Optional: put your own BABOK® PDF in a `Reading/` folder at the repo root (it is git-ignored). The instructor can then quote exact definitions to you from your personal copy.

## Build the website
```bash
./scripts/build_site.sh   # builds ./public with Quartz v4
./scripts/publish.sh      # builds and pushes to the gh-pages branch
```
Lesson content is authored as structured specs in `course/_build/course/m1.py`–`m9.py`. Run `python3 course/_build/course/render.py` from `course/` to regenerate the lesson scripts.

## Disclaimer
IIBA®, BABOK®, CBAP® and CCBA® are registered trademarks of the International Institute of Business Analysis. This project is **not affiliated with or endorsed by IIBA**. It does **not** reproduce the BABOK® Guide: the knowledge graph maps the Guide's structure (names, relationships, page references) and summarizes ideas in original wording. Page references also point to Esta Lessing's *CCBA® and CBAP® Certifications Study Guide* and Hans Jonasson's *CBAP Certification and BABOK Study Guide*, with no text reproduced. Practice questions are original and are not real exam items. GreenBasket and all its people and data are fictional.

The course format is inspired by Carl Vellotti's [free-ai-courses](https://github.com/carlvellotti/free-ai-courses). No content is copied from them.

## License
- Course content, knowledge graph and scenario: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- Scripts (`scripts/`, `site/`, `course/_build/`): MIT
