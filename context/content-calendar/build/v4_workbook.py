# -*- coding: utf-8 -*-
import json, io, openpyxl, os
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026"
SRC = os.path.join(ROOT, "venus-calendar-app", "data", "calendar.json")
OUT = os.path.join(ROOT, "Venus-Content-Calendar-Q4-2026.xlsx")

D = json.load(io.open(SRC, encoding="utf-8"))
INK = "000000"
SRC_FILL = {"Ready to post": "E8F3EC", "Edit needed": "FBF3E6", "Shoot, scripted": "EAF0F6",
            "Shoot, b-roll": "EAF0F6", "Design": "F0EDF6"}

wb = openpyxl.Workbook()
thin = Side(style="thin", color="DBDBDB"); B = Border(left=thin, right=thin, top=thin, bottom=thin)

def head(ws, freeze="C2"):
    for c in range(1, ws.max_column + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill = PatternFill("solid", fgColor=INK)
        cell.font = Font(bold=True, color="FFFFFF", size=10)
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 34
    ws.freeze_panes = freeze

def widths(ws, w):
    for i, x in enumerate(w, 1): ws.column_dimensions[get_column_letter(i)].width = x

def body(ws, h, bold=()):
    for n, row in enumerate(ws.iter_rows(min_row=2, max_row=ws.max_row)):
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True); cell.border = B; cell.font = Font(size=9)
        for bi in bold:
            if bi < len(row): row[bi].font = Font(size=9, bold=True, color=INK)
        ws.row_dimensions[n + 2].height = h

s = D["stats"]

# ------------------------------------------------------------------ START HERE
ws = wb.active; ws.title = "START HERE"
widths(ws, [4, 44, 118])
rows = [
 ("", "VENUS AESTHETICS", "Q4 2026 CONTENT CALENDAR"),
 ("", "Period", D["period"] + ". 95 posts, one a day."),
 ("", "Live board", "https://venus-content-calendar-production.up.railway.app"),
 ("", "", ""),
 ("", "THE ONE NUMBER THAT SHAPED THIS", ""),
 ("", "Organic reach is 17,546, not 511,299",
  "Across 207 reels the median was 511,299 plays and 67 likes. Across the last eight weeks, after the "
  "boosting was scaled back, the median was 17,546 plays and 41 likes. Reach fell 29x and engagement rate "
  "improved about 4x. The million play posts are bought impressions landing on people who do not care. "
  "Every post here is built to earn a response at 15,000 views."),
 ("", "", ""),
 ("", "THE WEEK, SLOT BY SLOT", ""),
 ("", "Monday, The Full Pass", "A 25 to 45 second treatment film that uses the whole arc of the footage: prep, the pass, the reaction, the finish. The 13 Monday films average 47.5 seconds of source. Each one also banks an 8 to 12 second cut and three stills, so one shoot gives three uses."),
 ("", "Tuesday, The Decision Table", "An 8 to 10 slide carousel naming a decision. Carousels out-engage reels per person reached and drive far more saves."),
 ("", "Wednesday, The Honest Number", "One number, or one refusal. Declining business is the least fakeable trust signal there is. Three of these become The Tray, sterility filmed with no patient in frame."),
 ("", "Thursday, Matched Frame", "Proof, shot with identical lighting, distance and posture. Mid-course beats final. Faceless by default."),
 ("", "Friday, Asked and Answered", "The existing Dr. Uzair FAQ library, 13 of the 20 unused questions. The question is the subject, never the doctor."),
 ("", "Saturday, THE ROOM", "The engagement day. Humour, team and clinic life, the treatment as the punchline. 13 posts, each with a content reference AND a separate editing reference. 7 re-cut from footage you have, 6 new shoots."),
 ("", "Sunday, The Forward", "Biology Countdown in October and December, Smog Diary through November. Built to be screenshotted and forwarded, not read. Sunday is Pakistan's peak wedding function day."),
 ("", "", ""),
 ("", "NO TWO WEEKS ARE THE SAME", ""),
 ("", "14 named week themes", "The season opens. How many sessions really. Before the event. Hair honestly. What is on the tray. The air changes. Barrier week. The laser window opens. Scalp and fall. Choosing a clinic. Wavelength week. The December bride. Quiet days. What next year needs."),
 ("", "A named shape on every post", "Each post carries a variant so a pillar never repeats its shape inside four weeks. The Decision Table alone runs seven: this or that after six sessions, the order to do them in, what it costs you in time, who it will not work on, what each one treats, the three questions to ask any clinic, what changes if your skin is deeper."),
 ("", "Real break weeks", "Monday 9 November, straight after Diwali, and Thursday 24 December both drop the normal slot for a pinned branch hours post. Week 14 is a four day year end run."),
 ("", "Five male-directed Mondays", "Instagram's Pakistani audience is roughly 63 percent male, male laser is your cheapest paid lead, and the account has never run a male-directed post."),
 ("", "", ""),
 ("", "THE NUMBERS", ""),
 ("", "Ready to post as is", "%d posts. Finished footage, nothing to do. 13 of these are Dr. Uzair FAQs that have never been published." % s["readyToPost"]),
 ("", "Edit needed", "%d posts. Footage exists and the exact change is written out, including which seconds carry which beat." % s["editNeeded"]),
 ("", "To shoot", "%d videos. These are the only things on the Production sheet." % s["toShoot"]),
 ("", "To design", "%d carousels and cards." % s["toDesign"]),
 ("", "Format mix", "%d reels, %d carousels, zero single images. Single image engagement fell 45.98%% year on year." % (
     s["byCreative"].get("Reel", 0), s["byCreative"].get("Carousel", 0))),
 ("", "Drive links", "%d of 95 posts carry a direct link to the exact file. The library is 45.7 minutes across 95 clips, median 28.5 seconds." % s["driveLinked"]),
 ("", "Banked second cuts", "%d. Every long Monday film also yields an 8 to 12 second cut and three stills, named in the edit note." % s["bankedCuts"]),
 ("", "", ""),
 ("", "THE RULES THIS CALENDAR FOLLOWS", ""),
 ("", "English only", "No Roman Urdu in any caption, on-screen line or script. Checked mechanically on all 95."),
 ("", "Nobody is quoted", "No caption puts words in any patient's mouth. Where a patient speaks on camera the spec says subtitle their real words."),
 ("", "Zero discounts", "No percentage off, no sale, no countdown to an offer. Urgency comes from biology and the wedding calendar instead."),
 ("", "Treatment-led", "Dr. Uzair answers questions. He is never in a hook, never in a first caption line, never in frame 1."),
 ("", "Every post declares one goal", "Save, send, comment, DM or profile visit, and the call to action is written for that goal and nothing else."),
 ("", "Nothing is claimed that cannot be cited", "Every number traces to a published source. The laser figure is a 150 patient series on Fitzpatrick IV to VI skin."),
 ("", "No banned words", "Permanent, painless, guaranteed, flawless, best, magic. The permitted term is hair reduction."),
 ("", "No drug brand names", "Pakistan's Therapeutic Goods Advertisement Rules 2025 require DRAP approval to promote therapeutic products to the public."),
 ("", "", ""),
 ("", "THE SHEETS", ""),
 ("", "Calendar", "All 95 days with hook, caption, hashtags, keyword block, goal, spec, links and reference."),
 ("", "Production", "Only the %d videos that have to be shot, numbered in the order needed." % s["toShoot"]),
 ("", "Scripts", "Every word-for-word script."),
 ("", "Shoot Guides", "Who, where, kit, the beat and the direction for each shoot."),
 ("", "Edit Notes", "Exactly what to change in each piece of existing footage."),
 ("", "Reference Library", "Every reference with its format and real engagement. A carousel only ever references a carousel."),
]
for r in rows: ws.append(list(r))
ws["B1"].font = Font(bold=True, size=19, color=INK); ws["C1"].font = Font(bold=True, size=19, color="6B6B6B")
ws.row_dimensions[1].height = 28
for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=2, max_col=3):
    for cell in row:
        cell.alignment = Alignment(vertical="top", wrap_text=True)
        if cell.column == 2 and cell.value:
            v = str(cell.value)
            cell.font = Font(bold=True, size=12, color="6B6B6B") if v.isupper() else Font(bold=True, size=10, color=INK)
for n in range(2, ws.max_row + 1):
    ws.row_dimensions[n].height = None

# ------------------------------------------------------------------- CALENDAR
ws = wb.create_sheet("Calendar")
ws.append(["#", "Date", "Day", "Wk", "WEEK THEME", "Month", "PILLAR", "THIS POST'S SHAPE", "Treatment",
           "Format", "GOAL", "STATE", "Owner",
           "HOOK, on screen", "CAPTION", "HASHTAGS", "KEYWORD BLOCK", "CTA", "Note",
           "FOOTAGE / JOB", "Source secs", "LINK", "2nd cut?", "WHAT TO CHANGE",
           "SPEC, slide by slide or shot by shot", "SCRIPT", "SHOOT GUIDE",
           "REFERENCE", "Ref account", "Ref format", "Why", "Ref result",
           "EDIT REFERENCE", "What to copy in the edit", "Status"])
for i in D["items"]:
    ws.append([i["id"], i["dateLabel"], i["dayFull"], i["week"], i.get("theme", ""), i["block"],
               i["show"] + (" / " + i["subPillar"] if i.get("subPillar") else ""), i.get("variant", ""),
               i["treatment"], i["creative"], i["goal"], i["sourceLabel"], i["owner"],
               i["hook"], i["caption"], i["hashtags"], i["keywordBlock"], i["cta"], i.get("marker", ""),
               (i["driveFolder"] + " / " + i["driveFile"]) if i["fromDrive"] else i["asset"],
               i.get("sourceSeconds") or "", i["driveUrl"] or "",
               "YES" if i.get("bankSecondCut") else "", i["editNote"], i["spec"], i["script"], i["recordGuide"],
               i["ref"] or "", i["refAccount"] or "", i["refFormat"] or "", i["refWhy"] or "", i["refMetric"] or "",
               i.get("editRef", "") or "", i.get("editRefWhy", "") or "", ""])
widths(ws, [4, 13, 10, 4, 22, 10, 22, 34, 22, 9, 9, 14, 10, 42, 70, 38, 44, 28, 20, 38, 9, 8, 8, 58, 86, 72, 68, 30, 16, 13, 44, 28, 30, 44, 10])
head(ws)
for n, row in enumerate(ws.iter_rows(min_row=2, max_row=ws.max_row)):
    i = D["items"][n]
    fill = SRC_FILL.get(i["sourceLabel"], "FFFFFF")
    for cell in row:
        cell.alignment = Alignment(vertical="top", wrap_text=True); cell.border = B
        cell.font = Font(size=9); cell.fill = PatternFill("solid", fgColor=fill)
    for c in (4, 6, 7, 10, 11): row[c].font = Font(size=9, bold=True, color=INK)
    row[13].font = Font(size=9, bold=True)
    if i["driveUrl"]:
        row[21].hyperlink = i["driveUrl"]; row[21].value = "Open"
        row[21].font = Font(size=9, color="0000EE", underline="single", bold=True)
    if i["ref"]:
        row[27].hyperlink = i["ref"]; row[27].value = i["ref"].replace("https://www.", "").replace("https://", "")
        row[27].font = Font(size=8, color="0000EE", underline="single")
    if i.get("editRef"):
        row[32].hyperlink = i["editRef"]; row[32].value = i["editRef"].replace("https://www.", "").replace("https://", "")
        row[32].font = Font(size=8, color="0000EE", underline="single")
    ws.row_dimensions[n + 2].height = 165

# ----------------------------------------------------------------- PRODUCTION
ws = wb.create_sheet("Production")
ws.append(["No", "Date", "Wk", "Kind", "Pillar", "THE SHAPE TO SHOOT", "Treatment", "Hook", "Shoot spec", "Script", "Shoot guide", "Reference", "Ref result", "EDIT REFERENCE", "What to copy in the edit"])
for p in D["production"]:
    ws.append([p["no"], p["date"], p["week"], p["kind"], p["title"], p.get("variant", ""), p["treatment"], p["hook"],
               p["spec"], p["script"], p["recordGuide"], p["ref"] or "", p["refMetric"] or "",
               p.get("editRef", "") or "", p.get("editRefWhy", "") or ""])
widths(ws, [5, 13, 4, 16, 20, 34, 20, 42, 86, 76, 76, 30, 28, 30, 44]); head(ws); body(ws, 165, bold=(4, 5))
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    row[0].font = Font(size=13, bold=True, color=INK)
    for c in (11, 13):
        if row[c].value:
            row[c].hyperlink = row[c].value
            row[c].value = str(row[c].value).replace("https://www.", "")
            row[c].font = Font(size=8, color="0000EE", underline="single")

# -------------------------------------------------------------------- SCRIPTS
ws = wb.create_sheet("Scripts")
ws.append(["Date", "Wk", "Pillar", "Treatment", "Hook", "FULL SCRIPT", "Shoot spec"])
for i in D["items"]:
    if not i["script"]: continue
    ws.append([i["dateLabel"], i["week"], i["show"], i["treatment"], i["hook"], i["script"], i["spec"]])
widths(ws, [13, 4, 22, 24, 42, 104, 80]); head(ws); body(ws, 240, bold=(2,))

# --------------------------------------------------------------- SHOOT GUIDES
ws = wb.create_sheet("Shoot Guides")
ws.append(["Date", "Wk", "Pillar", "Hook", "Caption", "HOW TO RECORD IT", "Spec", "Reference"])
for i in D["items"]:
    if not i["recordGuide"]: continue
    ws.append([i["dateLabel"], i["week"], i["show"], i["hook"], i["caption"], i["recordGuide"], i["spec"], i["ref"] or ""])
widths(ws, [13, 4, 20, 42, 60, 100, 62, 34]); head(ws); body(ws, 210, bold=(2,))

# ----------------------------------------------------------------- EDIT NOTES
ws = wb.create_sheet("Edit Notes")
ws.append(["Date", "Wk", "Pillar", "Footage in Drive", "Link", "WHAT TO CHANGE", "Spec"])
for i in D["items"]:
    if not i["editNote"]: continue
    ws.append([i["dateLabel"], i["week"], i["show"], i["driveFolder"] + " / " + i["driveFile"],
               i["driveUrl"] or "", i["editNote"], i["spec"]])
widths(ws, [13, 4, 20, 44, 10, 84, 76]); head(ws); body(ws, 180, bold=(2,))
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    if row[4].value:
        row[4].hyperlink = row[4].value; row[4].value = "Open"
        row[4].font = Font(size=9, color="0000EE", underline="single", bold=True)

# ----------------------------------------------------------------- REFERENCES
ws = wb.create_sheet("Reference Library")
ws.append(["Account", "Format", "What to copy from it", "Real result", "Used on", "Link"])
for r in D["referenceLibrary"]:
    ws.append([r["account"], r["format"], r["why"], r["metric"], r["usedOn"], r["url"]])
widths(ws, [22, 14, 82, 46, 9, 44]); head(ws); body(ws, 56, bold=(0,))
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    if row[5].value:
        row[5].hyperlink = row[5].value
        row[5].value = str(row[5].value).replace("https://www.", "")
        row[5].font = Font(size=9, color="0000EE", underline="single")

wb.save(OUT)
print("saved:", OUT)
print("sheets:", wb.sheetnames)
