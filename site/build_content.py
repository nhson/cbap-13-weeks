"""Assemble the Quartz `content/` folder from the course.

Usage: python3 site/build_content.py <output content dir>
Run from the repository root.
"""
import csv, json, os, re, shutil, sys
from urllib.parse import unquote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
COURSE = os.path.join(ROOT, 'course')
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'content'))
REPO_URL = 'https://github.com/nhson/cbap-13-weeks'

if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)

def write(rel, text):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as f:
        f.write(text)

def stem(path):
    return os.path.splitext(os.path.basename(path))[0]

structure = json.load(open(os.path.join(COURSE, 'course-structure.json')))
lessons = [l for m in structure['modules'] for l in m['lessons']]
LESSON_PAGE = {l['id']: f"{l['id']}-{l['path'].split('/')[1].split('-', 1)[1]}" for l in lessons}  # e.g. 1.2-baccm

# ---------- link rewriting ----------
def rewrite_links(text):
    def repl(m):
        label, target = m.group(1), unquote(m.group(2))
        if target.startswith('http'):
            return m.group(0)
        if target.startswith(('CBAP Knowledge Graph/', 'case-files/', 'company-context/')) or target == '../CBAP-Roadmap.md':
            name = stem(target) if target != '../CBAP-Roadmap.md' else 'CBAP Roadmap'
            return f'[[{name}]]' if name == label else f'[[{name}|{label}]]'
        if target.startswith('lesson-modules/'):
            lid = target.split('/')[1].split('-', 1)[0]
            return f'[[{LESSON_PAGE.get(lid, lid)}|{label}]]'
        # workspace/, progress/, exams/, .claude/ ... only exist in a learner's local copy
        return f'`{target}`'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', repl, text)

# ---------- lessons ----------
def lesson_page(l, module):
    raw = open(os.path.join(COURSE, l['path'])).read()
    raw = rewrite_links(raw)
    out = []
    lines = raw.split('\n')
    i = 0
    title = lines[0].lstrip('# ').strip()
    for line in lines[1:]:
        s = line.rstrip()
        if s.startswith('## Prepare (instructor'):
            out.append('## Knowledge graph notes for this lesson')
            continue
        if s.startswith('STOP: '):
            out += ['> [!question] Your turn', '> ' + s[6:], '']
            continue
        if s.startswith('USER: '):
            continue
        if s.startswith('ACTION: '):
            out += ['> [!note]- What the instructor does', '> ' + s[8:], '']
            continue
        if s.startswith('QUIZ: '):
            out += ['> [!example] Exam drill', '> ' + s[6:]]
            continue
        if s.startswith('Teach these points conversationally'):
            out.append('**Key points**')
            continue
        if s.startswith('**Exam trap to call out:**'):
            out += ['> [!warning] Exam trap', '> ' + s.replace('**Exam trap to call out:**', '').strip(), '']
            continue
        if s.startswith('**Discovery:**'):
            out += ['> [!success] Discovery', '> ' + s.replace('**Discovery:**', '').strip(), '']
            continue
        if s.startswith('A model answer should cover'):
            out.append('> [!tip]- Model answer (try it yourself first)')
            continue
        if s.startswith('- [ ] '):
            out.append(s)
            continue
        out.append(s)
    body = '\n'.join(out)
    # model-answer bullet lists belong inside the collapsed callout
    body = re.sub(r'(> \[!tip\]- Model answer \(try it yourself first\)\n)((?:- .*\n)+)', lambda m: m.group(1) + ''.join('> ' + x + '\n' for x in m.group(2).splitlines()), body)
    nav_prev = lessons[lessons.index(l) - 1] if lessons.index(l) > 0 else None
    nav_next = lessons[lessons.index(l) + 1] if lessons.index(l) + 1 < len(lessons) else None
    nav = ' · '.join(x for x in [
        f"← [[{LESSON_PAGE[nav_prev['id']]}|{nav_prev['id']} {nav_prev['name']}]]" if nav_prev else '',
        '[[course/index|Course plan]]',
        f"[[{LESSON_PAGE[nav_next['id']]}|{nav_next['id']} {nav_next['name']}]] →" if nav_next else ''] if x)
    fm = f"""---
title: "{title.replace('"', "'")}"
tags:
  - lesson
  - module-{module['id']}
---
"""
    banner = f"""> [!tip] Learn this lesson interactively
> This page is the readable version. To be **taught** it by Claude (Socratic questions, GreenBasket exercises, stakeholder reviews, graded exam drills), clone the [repository]({REPO_URL}), open `course/` in a terminal, run `claude`, and type `/start {l['id']}`.

{nav}
"""
    return fm + '\n' + banner + '\n' + body.strip() + '\n\n---\n' + nav + '\n'

for m in structure['modules']:
    for l in m['lessons']:
        write(f"course/module-{m['id']}/{LESSON_PAGE[l['id']]}.md", lesson_page(l, m))

# course index (plan)
plan = ['---', 'title: "Course: CBAP in 13 Weeks"', '---', '',
        'Seventy-five interactive lessons across 9 modules and 13 weeks at about 10 hours a week. Each lesson follows **teach → apply at GreenBasket → exam drill → wrap-up**.', '',
        '> [!info] Two ways to use it', '> - **Read** every lesson on this site.', f'> - **Be taught** by Claude: clone the [repository]({REPO_URL}), `cd course`, run `claude`, type `/start 1.1`, and then use `/next`, `/progress`, `/drill` and `/grade`.', '']
for m in structure['modules']:
    plan += [f"## Module {m['id']}: {m['name']}", f"*Weeks {m['weeks']}*. {m['description']}", '', '| Lesson | Week | Type | Time |', '|---|---|---|---|']
    for l in m['lessons']:
        plan.append(f"| [[{LESSON_PAGE[l['id']]}\\|{l['id']} {l['name']}]] | {l['week']} | {l['type']} | {l['minutes']}+{l['reading_min']} min |")
    plan.append('')
write('course/index.md', '\n'.join(plan) + '\n')
for m in structure['modules']:
    write(f"course/module-{m['id']}/index.md", f"---\ntitle: \"Module {m['id']}: {m['name']}\"\n---\n\n*Weeks {m['weeks']}*. {m['description']}\n\n" +
          '\n'.join(f"- [[{LESSON_PAGE[l['id']]}|{l['id']} {l['name']}]]" for l in m['lessons']) + '\n')

# ---------- knowledge graph ----------
shutil.copytree(os.path.join(COURSE, 'CBAP Knowledge Graph'), os.path.join(OUT, 'knowledge-graph'))
# a folder and a note with the same name collide in Quartz URLs
os.rename(os.path.join(OUT, 'knowledge-graph', '01 Foundations', 'Stakeholder Roles'), os.path.join(OUT, 'knowledge-graph', '01 Foundations', 'Roles'))
moc = open(os.path.join(OUT, 'knowledge-graph', '00 CBAP Knowledge Graph.md')).read()
write('knowledge-graph/index.md', re.sub(r'^---\n.*?\n---\n', '---\ntitle: "CBAP Knowledge Graph"\n---\n', moc, flags=re.S).replace('Open **Graph view**, and filter by tag or folder (for example `tag:#cbap/task`) to see one layer at a time.', 'Use the **graph** panel (top right) and the explorer on the left.') +
      '\n> [!warning] Public edition\n> This graph maps the *structure* of the BABOK® Guide v3: names, relationships, input/output flow and page references. Summaries are in our own words. It does not reproduce BABOK text. Read the official guide for exact definitions.\n')

# ---------- scenario ----------
def md_from_csv(path):
    rows = list(csv.reader(open(path)))
    head, body = rows[0], rows[1:]
    return '| ' + ' | '.join(head) + ' |\n|' + '---|' * len(head) + '\n' + '\n'.join('| ' + ' | '.join(r) + ' |' for r in body) + '\n'
for sub in ['company-context', 'case-files']:
    for d, _, fs in os.walk(os.path.join(COURSE, sub)):
        for f in fs:
            src = os.path.join(d, f)
            rel = os.path.relpath(src, COURSE)
            if f.endswith('.md'):
                write(os.path.join('scenario', os.path.relpath(src, COURSE)), rewrite_links(open(src).read()))
            elif f.endswith('.csv'):
                write(os.path.join('scenario', rel[:-4] + '.md'), f"---\ntitle: \"{stem(f)}\"\n---\n\nData file `{f}` (also in the repository as CSV).\n\n" + md_from_csv(src))
case_list = sorted(os.listdir(os.path.join(COURSE, 'case-files')))
write('scenario/index.md', f"""---
title: "The GreenBasket Scenario"
---

You are the new Senior Business Analyst at **GreenBasket Markets**, a 42-store regional grocer. For 13 weeks you take its **Click & Collect** initiative from a messy idea to an evaluated pilot, applying every BABOK® knowledge area on the way. GreenBasket, its people and its data are fictional.

## Company context
- [[SCENARIO|The scenario and the 13-week arc]]
- [[COMPANY|Company profile]]
- [[STAKEHOLDERS|Stakeholder profiles]]

## Case files
The documents you inherit or receive along the way. They are deliberately messy, contradictory and incomplete.

""" + '\n'.join(f"- [[{stem(f)}]]" for f in case_list) + '\n')

# ---------- roadmap, about, home ----------
write('CBAP Roadmap.md', rewrite_links(open(os.path.join(ROOT, 'CBAP-Roadmap.md')).read()).replace('# CBAP 3-Month Learning Roadmap', '---\ntitle: "CBAP Roadmap (13 weeks)"\n---\n\n# CBAP 3-Month Learning Roadmap', 1))
write('about.md', f"""---
title: About & Disclaimer
---

## What this is
A free, open study companion for the IIBA® **CBAP®** exam: a 13-week plan, 75 interactive lessons built around a fictional case, and a linked knowledge graph of the BABOK® Guide v3 structure.

## Not affiliated with IIBA
IIBA®, BABOK®, CBAP® and CCBA® are registered trademarks of the International Institute of Business Analysis. This project is **not** affiliated with, endorsed by, or sponsored by IIBA. It does not reproduce the BABOK® Guide. It references its structure and page numbers and summarizes ideas in original wording. Get the Guide from [iiba.org](https://www.iiba.org) (free for IIBA members).

## Study guides referenced
Page references point to: *BABOK® Guide v3* (IIBA, 2015); Esta Lessing, *CCBA® and CBAP® Certifications Study Guide* (Packt, 2020); Hans Jonasson, *CBAP Certification and BABOK Study Guide* (CRC Press, 2017). No text from these books is reproduced.

## Practice questions
All quiz and mock-exam questions are generated as original practice items. They are not real IIBA exam questions. Use a reputable commercial simulator as well to calibrate.

## Credits & license
- Course format inspired by Carl Vellotti's interactive courses ([free-ai-courses](https://github.com/carlvellotti/free-ai-courses)). No content is copied from them.
- Built with [Quartz](https://quartz.jzhao.xyz).
- Content: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Scripts: MIT. See the [repository]({REPO_URL}).
""")
n_lessons = len(lessons)
n_notes = sum(len(fs) for _, _, fs in os.walk(os.path.join(OUT, 'knowledge-graph')))
write('index.md', f"""---
title: CBAP in 13 Weeks
---

**A free, interactive path to the IIBA® CBAP® exam.** Study 10 hours a week for 13 weeks, with one realistic case, a linked BABOK® knowledge graph, and an AI instructor.

> [!abstract] What's inside
> - **[[course/index|The course]]**: {n_lessons} lessons in 9 modules. Each one follows teach → apply → exam drill → wrap-up.
> - **[[knowledge-graph/index|The knowledge graph]]**: {n_notes} linked notes covering 6 knowledge areas, 30 tasks, their inputs and outputs, 50 techniques, competencies and perspectives, plus an exam lens.
> - **[[scenario/index|The GreenBasket scenario]]**: you are the Senior BA on a grocery chain's Click & Collect initiative, from the messy kickoff to pilot evaluation.
> - **[[CBAP Roadmap|The 13-week roadmap]]**: phases, milestones, and the weekly rhythm.

## How to use it
| If you want to… | Do this |
|---|---|
| Read and self-study | Start at [[1.1-welcome\\|Lesson 1.1]] and follow the ← → links. Keep the knowledge graph open alongside. |
| Be **taught** interactively | `git clone {REPO_URL}` → `cd cbap-13-weeks/course` → `claude` → `/start 1.1`. Claude teaches, reviews your work as GreenBasket stakeholders, runs graded drills and mocks, and tracks your progress. |
| Revise before the exam | [[Exam Blueprint]] · [[BABOK Input-Output Flow]] · [[Commonly Confused Concepts]] · [[Technique-Task Matrix]] |

## The 13 weeks at a glance
```mermaid
gantt
  dateFormat  X
  axisFormat  W%s
  section Foundations
  Foundations           :0, 2
  section Knowledge Areas
  BAPM 14%              :2, 3
  E&C 12%               :3, 4
  RLCM 15%              :4, 5
  SA 15%                :5, 6
  RADD 30%              :6, 8
  SE 14%                :8, 9
  section Exam prep
  Consolidation         :9, 10
  Mocks & gap sprints   :10, 13
```

> [!warning] Not affiliated with IIBA
> Independent study material. It does not reproduce the BABOK® Guide. See [[about|About & Disclaimer]].
""")
print(f'content built: {OUT} | lessons {n_lessons} | graph notes {n_notes}')
