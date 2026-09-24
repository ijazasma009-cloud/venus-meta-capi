# -*- coding: utf-8 -*-
"""Patch the board app for the v4 schema: nine new pillars, a declared goal per post,
the search keyword block, and the edit note on reused footage."""
import io, re

APP = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\public\app.js"
CSS = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\public\style.css"

s = io.open(APP, encoding="utf-8").read()

# ---- 1. the nine v4 pillars -------------------------------------------------
NEW_FC = """var FC = {
  'Eight Seconds':'var(--f-machine)',
  'The Decision Table':'var(--f-is)',
  'The Honest Number':'var(--f-real)',
  'Matched Frame':'var(--f-case)',
  'Asked and Answered':'var(--f-ask)',
  'The Tray':'var(--f-room)',
  "The Men's Room":'var(--f-side)',
  'Branch Desk':'var(--f-oneliner)',
  'Biology Countdown':'var(--f-irl)',
  'Smog Diary':'var(--f-off)'
};
var GOAL_LABEL = {
  save:'Built for saves', send:'Built to be forwarded', comment:'Built for replies',
  dm:'Built to start a DM', profile:'Built for profile visits'
};"""
s = re.sub(r"var FC = \{.*?\n\};", NEW_FC, s, count=1, flags=re.S)
assert "GOAL_LABEL" in s, "FC replace failed"

# ---- 2. drawer: goal pill ---------------------------------------------------
old_meta = """  meta.appendChild(el('span','pill hot', item.sourceLabel));"""
new_meta = """  meta.appendChild(el('span','pill hot', item.sourceLabel));
  if(item.goal) meta.appendChild(el('span','pill goal', GOAL_LABEL[item.goal] || item.goal));"""
assert old_meta in s, "meta anchor missing"
s = s.replace(old_meta, new_meta, 1)

# ---- 3. drawer: keyword block right after hashtags --------------------------
old_tags = """  if(item.hashtags) d.appendChild(field('Hashtags', item.hashtags));"""
new_tags = """  if(item.hashtags) d.appendChild(field('Hashtags', item.hashtags));
  if(item.keywordBlock) d.appendChild(field('Search keyword block, goes under the hashtags', item.keywordBlock));"""
assert old_tags in s, "hashtag anchor missing"
s = s.replace(old_tags, new_tags, 1)

# ---- 4. drawer: the edit note on reused footage -----------------------------
old_asset = """  af.appendChild(box); d.appendChild(af);"""
new_asset = """  af.appendChild(box); d.appendChild(af);

  if(item.editNote) d.appendChild(field('What to change in this footage', item.editNote, 'script'));"""
assert old_asset in s, "asset anchor missing"
s = s.replace(old_asset, new_asset, 1)

io.open(APP, "w", encoding="utf-8").write(s)
print("app.js patched: FC map, goal pill, keyword block, edit note")

# ---- 5. css for the goal pill ----------------------------------------------
c = io.open(CSS, encoding="utf-8").read()
if ".pill.goal" not in c:
    c += """
.pill.goal{background:var(--ink);color:#fff;border-color:var(--ink);font-weight:600}
"""
    io.open(CSS, "w", encoding="utf-8").write(c)
    print("style.css patched: .pill.goal")
else:
    print("style.css already has .pill.goal")
