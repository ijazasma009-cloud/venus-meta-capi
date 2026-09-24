# -*- coding: utf-8 -*-
"""Surface the v4.3 fields in the drawer: week theme, the post's shape, the source length,
the banked second cut, and the separate editing reference on every engagement day post."""
import io

APP = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\public\app.js"
CSS = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\public\style.css"

s = io.open(APP, encoding="utf-8").read()

# ---- the nine v4.3 pillars ---------------------------------------------------
old_fc_start = s.index("var FC = {")
old_fc_end = s.index("};", old_fc_start) + 2
NEW_FC = """var FC = {
  'The Full Pass':'var(--f-machine)',
  'The Decision Table':'var(--f-is)',
  'The Honest Number':'var(--f-real)',
  'Matched Frame':'var(--f-case)',
  'Asked and Answered':'var(--f-ask)',
  'The Room':'var(--f-side)',
  'Branch Desk':'var(--f-oneliner)',
  'Biology Countdown':'var(--f-irl)',
  'Smog Diary':'var(--f-off)'
};"""
s = s[:old_fc_start] + NEW_FC + s[old_fc_end:]

# ---- header line: week theme and the post's shape ----------------------------
old_head = """  hh.appendChild(el('p',null, item.dayFull+' '+item.dateLabel+'   Week '+item.week+'   '+item.block));"""
new_head = """  hh.appendChild(el('p',null, item.dayFull+' '+item.dateLabel+'   Week '+item.week+'   '+item.block));
  if(item.theme) hh.appendChild(el('p','dtheme','Week theme: '+item.theme));"""
assert old_head in s, "header anchor missing"
s = s.replace(old_head, new_head, 1)

# ---- pills: the shape, and the sub pillar ------------------------------------
old_pill = """  if(item.goal) meta.appendChild(el('span','pill goal', GOAL_LABEL[item.goal] || item.goal));"""
new_pill = """  if(item.goal) meta.appendChild(el('span','pill goal', GOAL_LABEL[item.goal] || item.goal));
  if(item.subPillar) meta.appendChild(el('span','pill hot', item.subPillar));
  if(item.variant) meta.appendChild(el('span','pill shape', item.variant));"""
assert old_pill in s, "pill anchor missing"
s = s.replace(old_pill, new_pill, 1)

# ---- source length and the banked second cut --------------------------------
old_box = """    if(item.driveUrl){
      var a=el('a','bigbtn','Open in Google Drive');"""
new_box = """    if(item.sourceSeconds){
      box.appendChild(el('div','fpath','Real length of this file: '+item.sourceSeconds+' seconds'));
    }
    if(item.bankSecondCut){
      box.appendChild(el('div','bank','Also export a second cut of 8 to 12 seconds from this same file, plus three stills. The beat is named in the edit note.'));
    }
    if(item.driveUrl){
      var a=el('a','bigbtn','Open in Google Drive');"""
assert old_box in s, "asset box anchor missing"
s = s.replace(old_box, new_box, 1)

# ---- the editing reference, required on every engagement day post ------------
old_ref = """  var cm=el('div','comments');"""
new_ref = """  if(item.editRef){
    var ef=el('div','field');
    ef.appendChild(el('label',null,'Editing reference, copy the cut and the pacing'));
    var eb=el('div','refbox');
    if(item.editRefAccount) eb.appendChild(el('div','racct', item.editRefAccount));
    eb.appendChild(el('div','rwhy', item.editRefWhy||''));
    if(item.editRefMetric) eb.appendChild(el('div','rmetric', item.editRefMetric));
    var ea=el('a','bigbtn','Open the editing reference');
    ea.href=item.editRef; ea.target='_blank'; ea.rel='noopener noreferrer';
    eb.appendChild(ea); ef.appendChild(eb); d.appendChild(ef);
  }

  var cm=el('div','comments');"""
assert old_ref in s, "comments anchor missing"
s = s.replace(old_ref, new_ref, 1)

io.open(APP, "w", encoding="utf-8").write(s)
print("app.js patched: pillars, week theme, shape pill, source length, banked cut, editing reference")

c = io.open(CSS, encoding="utf-8").read()
if ".pill.shape" not in c:
    c += """
.dtheme{margin-top:2px;font-size:.78rem;color:var(--ink-faint);letter-spacing:.01em}
.pill.shape{background:#F4F4F4;border-color:var(--rule);color:var(--ink-2);font-style:italic}
.bank{margin-top:8px;padding:8px 10px;border-left:3px solid var(--ink);background:#FAFAFA;
  font-size:.8rem;line-height:1.45;color:var(--ink-2)}
"""
    io.open(CSS, "w", encoding="utf-8").write(c)
    print("style.css patched")
else:
    print("style.css already patched")
