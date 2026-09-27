"""Render lesson specs into interactive teaching scripts + course-structure.json + COURSE-PLAN.md.
Run: python3 _build/course/render.py   (from learn-with-ai/)
"""
import json, os, re, sys, importlib
from urllib.parse import quote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.dirname(__file__))
KG = 'CBAP Knowledge Graph'

# ---------- path helpers used by specs ----------
def T(n):  return f'{KG}/03 Tasks/{n}.md'
def TE(n): return f'{KG}/05 Techniques/{n}.md'
def KA(n): return f'{KG}/02 Knowledge Areas/{n}.md'
def IO(n): return f'{KG}/04 Inputs & Outputs/{n.replace("/", " or ")}.md'
def F(n):  return f'{KG}/01 Foundations/{n}.md'
def CC(n): return f'{KG}/01 Foundations/Core Concepts/{n}.md'
def R(n):  return f'{KG}/01 Foundations/Stakeholder Roles/{n}.md'
def UC(n): return f'{KG}/06 Underlying Competencies/{n}.md'
def P(n):  return f'{KG}/07 Perspectives/{n}.md'
def EX(n): return f'{KG}/08 Exam Lens/{n}.md'
def CF(n): return f'case-files/{n}'

def mlink(path, label=None):
    label = label or os.path.splitext(os.path.basename(path))[0]
    return f'[{label}]({quote(path)})'

def check_paths(spec):
    missing = []
    for p in spec.get('prepare', []) + [f for a in spec.get('apply', []) for f in a.get('files', [])]:
        if p.startswith(('workspace/', 'exams/')):
            continue  # created by the student during the course
        if not os.path.exists(os.path.join(ROOT, p)):
            missing.append(p)
    return missing

# ---------- renderer ----------
def render(s, nxt):
    L = []
    add = L.append
    add(f"# Lesson {s['id']}: {s['title']}\n")
    add(f"*Module {s['module']} · Week {s['week']} · ~{s['minutes']} min in session + ~{s.get('reading_min', 0)} min reading*\n")
    add('## Prepare (instructor: read silently before teaching)')
    for p in s.get('prepare', []):
        add(f'- {mlink(p)}')
    if s.get('prepare_note'):
        add(f"- {s['prepare_note']}")
    add('')
    add('---\n')
    # opening
    add(s['hook'].strip() + '\n')
    if s.get('objectives'):
        add('By the end of this session you will be able to:')
        for o in s['objectives']:
            add(f'- {o}')
        add('')
    add(f"STOP: {s.get('ready', 'Ready to dive in?')}\n")
    add('USER: Ready\n')
    add('---\n')
    # teaching segments
    for i, seg in enumerate(s.get('teach', []), 1):
        add(f"## Part {i}: {seg['title']}\n")
        if seg.get('read'):
            add('ACTION: Re-read ' + ', '.join(mlink(p) for p in seg['read']) + ' so every name you use is BABOK-exact. Share the link(s) with the student.\n')
        add('Teach these points conversationally (short, concrete, GreenBasket examples where natural):')
        for p in seg['points']:
            add(f'- {p}')
        add('')
        if seg.get('check'):
            add(f"STOP: {seg['check']}\n")
            add(f"USER: {seg.get('expect', 'Answers in their own words')}\n")
            if seg.get('feedback'):
                add(f"ACTION: Give feedback. A strong answer includes: {seg['feedback']}\n")
        if seg.get('trap'):
            add(f"**Exam trap to call out:** {seg['trap']}\n")
        add('---\n')
    # application
    for a in s.get('apply', []):
        add(f"## Apply it at GreenBasket: {a['title']}\n")
        add(a['brief'].strip() + '\n')
        if a.get('files'):
            add('ACTION: Open and skim ' + ', '.join(mlink(f) for f in a['files']) + '. Share the links and summarize the relevant facts in 3–5 bullets. Don\'t solve the exercise.\n')
        add(f"STOP: {a['ask']}\n")
        add(f"USER: {a.get('expect', 'Drafts their analysis in the chat')}\n")
        add(f"ACTION: {a['action']} Save the result to `workspace/{a['output']}` and link it: [{a['output']}](workspace/{quote(a['output'])}).\n")
        if a.get('model'):
            add('A model answer should cover (use it to coach, don\'t just paste it):')
            for m in a['model']:
                add(f'- {m}')
            add('')
        if a.get('review'):
            add(f"ACTION: Get a stakeholder review. Use the Agent tool with subagent_type `{a['review']}`, giving it the path `workspace/{a['output']}`{(' and ' + a['review_focus']) if a.get('review_focus') else ''}. Relay the review to the student in 3–6 lines.\n")
            add('STOP: How would you respond to that feedback? What would you change?\n')
            add('USER: Responds; optionally asks you to update the file\n')
            add('[If the student wants changes, update the workspace file.]\n')
        if a.get('discovery'):
            add(f"**Discovery:** {a['discovery']}\n")
        add('---\n')
    # quiz
    q = s.get('quiz')
    if q:
        add('## Exam drill\n')
        add(f"QUIZ: {q['n']} CBAP-style questions on: {q['focus']}.")
        if q.get('mix'):
            add(f"Mix: {q['mix']}.")
        if q.get('traps'):
            add('Build distractors from these traps: ' + '; '.join(q['traps']) + '.')
        add(f"Log to scores.csv with ka=`{q.get('ka', s.get('ka', 'GEN'))}` and topic=`{q.get('topic', s['slug'])}`.\n")
        add('STOP: Before we wrap up, which question felt shakiest, and why?\n')
        add('USER: Names one\n')
        add('ACTION: Re-explain that concept in a different way (analogy or GreenBasket example) in 3–4 lines.\n')
        add('---\n')
    # extra raw blocks (for exam/lab lessons)
    for blk in s.get('extra', []):
        add(blk.strip() + '\n')
        add('---\n')
    # wrap-up
    add('## Wrap-up\n')
    add('**Key takeaways:**')
    for i, k in enumerate(s['takeaways'], 1):
        add(f'{i}. {k}')
    add('')
    if s.get('exam_rule'):
        add(f"> **Exam rule of thumb:** {s['exam_rule']}\n")
    if s.get('reading'):
        add('**Reading before the next session:**')
        for r in s['reading']:
            add(f'- {r}')
        add('')
    if s.get('flashcards'):
        add('ACTION: Append these flashcards to `workspace/flashcards.md` (create it if missing; format `Q :: A`, one per line), then tell the student how many you added:')
        for fc in s['flashcards']:
            add(f'- {fc}')
        add('')
    add(f"ACTION: Update [progress.json](progress/progress.json): add this lesson (`{s['id']}`) to `completed` with today's date and minutes ≈ {s['minutes']}, set `current` to `{nxt['id'] if nxt else 'done'}`, and update `weak_topics` if the drill exposed any.\n")
    if nxt:
        add(f"**Next up:** Lesson {nxt['id']}: {nxt['title']}. {nxt.get('teaser', '')}\n")
        add(f"STOP: Ready for {nxt['id']}? Type `/next` (or `/start {nxt['id']}`) whenever you are. Short break first is a good idea.\n")
        add('USER: /next\n')
    else:
        add('STOP: That was the final lesson. How are you feeling about exam day?\n')
        add('USER: Responds\n')
    add('---\n')
    add('## Success Criteria')
    for c in s['success']:
        add(f'- [ ] {c}')
    add('')
    return '\n'.join(L)

def main():
    mods = [importlib.import_module(m) for m in ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9']]
    modules = [m.MODULE for m in mods]
    lessons = [l for m in modules for l in m['lessons']]
    problems = []
    for i, l in enumerate(lessons):
        l.setdefault('module', next(m['id'] for m in modules if l in m['lessons']))
        miss = check_paths(l)
        if miss: problems.append((l['id'], miss))
    if problems:
        for p in problems: print('MISSING', p)
        sys.exit(1)
    out = os.path.join(ROOT, 'lesson-modules')
    for f in os.listdir(out):
        pth = os.path.join(out, f)
        if os.path.isdir(pth):
            for g in os.listdir(pth): os.remove(os.path.join(pth, g))
            os.rmdir(pth)
    struct = {'course': {'name': 'CBAP in 13 Weeks: Interactive', 'code': 'cbap13', 'version': '1.0.0', 'babok': 'v3', 'hours_per_week': 10,
                         'scenario': 'GreenBasket Markets: Click & Collect'}, 'modules': []}
    for mi, m in enumerate(modules):
        sm = {'id': m['id'], 'name': m['name'], 'weeks': m['weeks'], 'description': m['description'], 'lessons': []}
        for l in m['lessons']:
            idx = lessons.index(l)
            nxt = lessons[idx + 1] if idx + 1 < len(lessons) else None
            folder = f"{l['id']}-{l['slug']}"
            os.makedirs(os.path.join(out, folder), exist_ok=True)
            path = f'lesson-modules/{folder}/LESSON.md'
            open(os.path.join(ROOT, path), 'w').write(render(l, nxt))
            sm['lessons'].append({'id': l['id'], 'name': l['title'], 'week': l['week'], 'minutes': l['minutes'], 'reading_min': l.get('reading_min', 0),
                                  'type': l.get('type', 'lesson'), 'ka': l.get('ka', ''), 'path': path, 'description': l.get('teaser', '')})
        struct['modules'].append(sm)
    json.dump(struct, open(os.path.join(ROOT, 'course-structure.json'), 'w'), indent=2)
    # plan
    P_ = ['# CBAP in 13 Weeks: Course Plan\n',
          'Interactive lessons taught by Claude inside this folder. Start with `/start 1.1`, then use `/next`. Other commands: `/progress`, `/drill`, `/grade`.\n',
          'Each lesson: **teach → apply at GreenBasket → exam drill → wrap-up**. Minutes = in-session time + reading time.\n']
    wk = {}
    for l in lessons: wk.setdefault(l['week'], []).append(l)
    for m in modules:
        P_.append(f"\n## Module {m['id']}: {m['name']} (weeks {m['weeks']})\n{m['description']}\n")
        P_.append('| Lesson | Title | Week | Type | Session | Reading |')
        P_.append('|---|---|---|---|---|---|')
        for l in m['lessons']:
            folder = f"{l['id']}-{l['slug']}"
            P_.append(f"| {l['id']} | [{l['title']}]({quote('lesson-modules/' + folder + '/LESSON.md')}) | {l['week']} | {l.get('type', 'lesson')} | {l['minutes']}m | {l.get('reading_min', 0)}m |")
    P_.append('\n## Weekly load check\n| Week | Lessons | Total hours |\n|---|---|---|')
    for w in sorted(wk):
        tot = sum(l['minutes'] + l.get('reading_min', 0) for l in wk[w])
        P_.append(f"| {w} | {', '.join(l['id'] for l in wk[w])} | {tot/60:.1f} h |")
    open(os.path.join(ROOT, 'COURSE-PLAN.md'), 'w').write('\n'.join(P_) + '\n')
    print('lessons:', len(lessons))
    for w in sorted(wk):
        print('week', w, round(sum(l['minutes'] + l.get('reading_min', 0) for l in wk[w]) / 60, 1), 'h', len(wk[w]), 'lessons')

if __name__ == '__main__':
    main()
