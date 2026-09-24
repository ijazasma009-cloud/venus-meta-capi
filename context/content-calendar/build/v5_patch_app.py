# -*- coding: utf-8 -*-
"""Patch the board for v5: the seven plain formats, the four buckets, and THE IDEA panel."""
import io

APP = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\public\app.js"
CSS = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\public\style.css"

s = io.open(APP, encoding="utf-8").read()

a = s.index("var FC = {"); b = s.index("};", a) + 2
s = s[:a] + """var FC = {
  'Treatment Film':'var(--f-machine)',
  'Skin School':'var(--f-is)',
  'Ask Venus':'var(--f-ask)',
  'The Results':'var(--f-case)',
  'Real Talk':'var(--f-real)',
  'The Team':'var(--f-side)',
  'Your Glow Plan':'var(--f-irl)'
};
var BUCKET_COLOR = {
  'Treatment':'var(--f-machine)', 'Educational':'var(--f-is)',
  'Engaging':'var(--f-real)', 'Conversion':'var(--f-irl)'
};""" + s[b:]

# THE IDEA panel, straight under the header, before the pills
old = """  var meta=el('div','dmeta');"""
new = """  if(item.conceptLine){
    var ib=el('div','ideabox');
    ib.appendChild(el('div','idealabel','THE IDEA'));
    ib.appendChild(el('div','ideatext', item.conceptLine));
    d.appendChild(ib);
  }

  var meta=el('div','dmeta');"""
assert old in s, "meta anchor missing"
s = s.replace(old, new, 1)

# bucket pill first, then the concept name
old2 = """  if(item.subPillar) meta.appendChild(el('span','pill hot', item.subPillar));"""
new2 = """  if(item.bucket) meta.appendChild(el('span','pill bucket', item.bucket));"""
if old2 in s: s = s.replace(old2, new2, 1)

# the header subtitle should show the bucket and format, not a week theme
s = s.replace("""  if(item.theme) hh.appendChild(el('p','dtheme','Week theme: '+item.theme));""",
              """  if(item.theme) hh.appendChild(el('p','dtheme', item.theme));""")

io.open(APP, "w", encoding="utf-8").write(s)
print("app.js patched: seven formats, bucket pill, THE IDEA panel")

c = io.open(CSS, encoding="utf-8").read()
if ".ideabox" not in c:
    c += """
.ideabox{margin:14px 0 4px;padding:12px 14px;border:1px solid var(--ink);border-radius:4px}
.idealabel{font-size:.62rem;letter-spacing:.14em;font-weight:700;color:var(--ink-faint);margin-bottom:5px}
.ideatext{font-size:.95rem;line-height:1.5;color:var(--ink);font-weight:500}
.pill.bucket{background:var(--ink);color:#fff;border-color:var(--ink);font-weight:700;letter-spacing:.04em}
"""
    io.open(CSS, "w", encoding="utf-8").write(c)
    print("style.css patched: ideabox and bucket pill")
else:
    print("style.css already patched")
