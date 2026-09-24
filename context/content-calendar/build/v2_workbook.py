# -*- coding: utf-8 -*-
import json, io, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SRC = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\data\calendar.json"
OUT = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\Venus-Content-Calendar-Sep-Dec-2026.xlsx"

D = json.load(io.open(SRC, encoding="utf-8"))
NAVY="12355B"; GOLD="9C7C2E"; LIGHT="EAEEEF"
FMT_COLOR = {
 "Case File":"12355B","The One Liner":"8C3A2B","Really Feels Like":"B5761E","The Machine":"2A5FA8",
 "Ask the Room":"12665F","Side by Side":"1B6B4C","Is This You":"57389C","The Room":"6E4A1F",
 "Off Duty":"93304A","In Real Life":"0F6B7A","The Course":"212121","Skin School":"57389C","The Menu":"2A5FA8","New at Venus":"1B6B4C","Men of Venus":"6B5B45","The Result":"12665F","The Offer Free Consultation":"8A5560"}
BLOCK_FILL = {"THE PROOF ENGINE":"FBF7EC","THE FULL MENU":"EEF3FA","SEASON AND PROOF":"F5EFF5"}

wb = openpyxl.Workbook()
thin = Side(style="thin", color="D9E0E2"); B = Border(left=thin,right=thin,top=thin,bottom=thin)

def head(ws):
    for c in range(1, ws.max_column+1):
        cell = ws.cell(row=1, column=c)
        cell.fill = PatternFill("solid", fgColor=NAVY)
        cell.font = Font(bold=True, color="FFFFFF", size=10)
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 32
    ws.freeze_panes = "C2"

def widths(ws, w):
    for i,x in enumerate(w,1): ws.column_dimensions[get_column_letter(i)].width = x

def body(ws, h, bold=()):
    for i,row in enumerate(ws.iter_rows(min_row=2, max_row=ws.max_row), start=0):
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True); cell.border=B; cell.font=Font(size=9)
        for bi in bold:
            if bi < len(row): row[bi].font = Font(size=9, bold=True, color=NAVY)
        ws.row_dimensions[i+2].height = h

# ---------------------------------------------------------------- START HERE
ws = wb.active; ws.title = "START HERE"
widths(ws,[4,44,114])
rows = [
 ("","VENUS AESTHETICS","CONTENT CALENDAR"),
 ("","Period","Monday 7 September to Sunday 6 December 2026. 13 weeks, 91 posts, one per day."),
 ("","Live board","https://venus-content-calendar-production.up.railway.app  Two roles, named accounts, and an activity log showing who changed what."),
 ("","Built on","600 of your own Instagram posts and 19 competitor and clinic-chain accounts crawled from a logged-in session, the full 824 file Drive, 90 days of Meta Ads performance, and frame-by-frame review of the source footage."),
 ("","",""),
 ("","THE RULE THAT CHANGED THIS VERSION",""),
 ("","Nobody is quoted. Anywhere.","Audio in the Drive files cannot be verified, so no caption puts words in a patient's mouth. Where a patient speaks on camera, the edit brief tells the editor to subtitle what they actually said. An earlier draft invented a patient line. That is now structurally impossible: zero captions contain quoted speech."),
 ("","The footage was actually watched","Frames were pulled from the source files and reviewed. The finding that reshaped the calendar: treatment b-roll is SILENT, with no interview in it. So no format asks a patient to narrate. Session numbers and dates on screen carry the story instead."),
 ("","Lengths are measured, not guessed","Source durations were read off the real files. The Primelase vs Soprano explainer is 2m12s, the engaging clips are 2.8 to 4.7 seconds and must be stitched, testimonials run 18 to 28 seconds."),
 ("","Already-posted content is flagged","Primelase vs Soprano, Mehwish fat freeze, Kabeer PRP, Ayesha Kamran laser, Khurasa Party Peel and Daniah Neck Lift are all live on the page already. Where reused, they are re-cut into a different format, never rescheduled as new."),
 ("","",""),
 ("","WHAT IS IN IT",""),
 ("","Format mix","64 reels, 25 carousels, 2 statics. Carousels up from 18 percent to 27 percent, because carousels are what get saved and sent."),
 ("","Eleven new treatments","Venus SlimFit, AcneOUT Peel, Exosome Facial, masseter, lip flip, hyperhidrosis, Venus CelluLITE, Scalp Detox, Fusion PRP, melasma and alopecia. None had ever been scheduled."),
 ("","No discount posts","Zero. The only commercial post is the free consultation, which is a standing service, not a promotion."),
 ("","Treatment led, not doctor led","The founder is not the star. Treatments are, and where a person answers a question it is a named practitioner."),
 ("","",""),
 ("","THE SHEETS",""),
 ("","Calendar","All 91 days with hook, caption, CTA, Drive link, measured source length, edit spec, warnings and reference."),
 ("","Formats","The 16 recurring formats and the evidence behind each."),
 ("","Courses","The 5 treatment courses followed across the quarter and the footage behind each."),
 ("","Production","Everything that needs shooting, designing or editing."),
 ("","Reference Library","All 30 reference posts, what each demonstrates and its real engagement rate."),
 ("","Edit Specs","The full edit brief for each format, for the editor."),
]
for r in rows: ws.append(list(r))
ws["B1"].font = Font(bold=True, size=19, color=NAVY); ws["C1"].font = Font(bold=True, size=19, color=GOLD)
ws.row_dimensions[1].height = 28
for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=2, max_col=3):
    for cell in row:
        cell.alignment = Alignment(vertical="top", wrap_text=True)
        if cell.column == 2 and cell.value:
            v = str(cell.value)
            cell.font = Font(bold=True, size=12, color=GOLD) if v.isupper() else Font(bold=True, size=10, color=NAVY)

# ---------------------------------------------------------------- CALENDAR
ws = wb.create_sheet("Calendar")
ws.append(["#","Date","Day","Wk","Block","Format","Treatment","Type","HOOK","CAPTION","CTA",
           "SOURCE","DRIVE LINK","Len","Owner","EDIT: length","EDIT: cut","EDIT: on screen","EDIT: audio",
           "WATCH OUT","REFERENCE (same content type)","Ref account","Why that reference","Ref result","Note","Status"])
for it in D["items"]:
    ed = it.get("edit") or {}
    ws.append([
      it["id"], it["dateLabel"], it["dayFull"], it["week"], it["block"], it["show"], it["treatment"],
      it["creative"], it["hook"], it["caption"], it["cta"],
      (it["driveFolder"]+" / "+it["driveFile"]) if it["fromDrive"] else it["asset"],
      it["driveUrl"] or "", (str(it.get("seconds"))+"s" if it.get("seconds") else ""), it["owner"],
      ed.get("length",""), ed.get("cut",""), ed.get("onScreen",""), ed.get("audio",""),
      "\n\n".join(it.get("editWarnings") or []),
      it["ref"], it["refAccount"], it["refWhy"], it["refMetric"], it["note"], ""
    ])
widths(ws,[4,13,10,4,18,17,26,9,40,70,30,44,42,7,12,15,46,42,34,58,38,20,54,34,40,11])
head(ws)
for i,row in enumerate(ws.iter_rows(min_row=2, max_row=ws.max_row), start=0):
    it = D["items"][i]
    fill = BLOCK_FILL.get(it["block"], "FFFFFF")
    for cell in row:
        cell.alignment = Alignment(vertical="top", wrap_text=True); cell.border=B
        cell.font = Font(size=9); cell.fill = PatternFill("solid", fgColor=fill)
    row[5].font = Font(size=9, bold=True, color=FMT_COLOR.get(it["show"], NAVY))
    row[8].font = Font(size=9, bold=True)
    if not it["fromDrive"]: row[11].font = Font(size=9, bold=True, color="B5761E")
    if it["driveUrl"]:
        row[12].hyperlink = it["driveUrl"]; row[12].value = "Open in Drive"
        row[12].font = Font(size=9, color="12355B", underline="single", bold=True)
    if it.get("editWarnings"): row[18].font = Font(size=8, color="96303C")
    row[19].hyperlink = it["ref"]; row[19].value = it["ref"].replace("https://","")
    row[19].font = Font(size=8, color="12355B", underline="single")
    ws.row_dimensions[i+2].height = 128

# ---------------------------------------------------------------- FORMATS
ws = wb.create_sheet("Formats")
ws.append(["Format","Slot","Creative","Posts","What it is","Why it works","Assets","Reference links"])
for s in D["shows"]:
    ws.append([s["name"], s["slot"], s["creative"], D["stats"]["byShow"].get(s["name"],0),
               s["what"], s["why"], s["assets"], "\n".join(s["refs"])])
widths(ws,[22,14,17,7,62,72,58,44]); head(ws); body(ws, 92, bold=(0,))
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    row[0].font = Font(size=10, bold=True, color=FMT_COLOR.get(row[0].value, NAVY))

# ---------------------------------------------------------------- CASE FILES
ws = wb.create_sheet("Courses")
ws.append(["ID","Patient","Treatment course","Sessions","Footage in Drive","What was verified","Posting dates"])
for cf in D["caseFiles"]:
    dates = [i["dateLabel"] for i in D["items"] if cf["patient"].split()[0].lower() in (i["driveFolder"] or "").lower()]
    ws.append([cf["id"], cf["patient"], cf["treatment"], cf["beats"], cf["assets"], cf["note"], ", ".join(dates)])
widths(ws,[7,15,32,7,52,74,58]); head(ws); body(ws, 66, bold=(1,))

# ---------------------------------------------------------------- PRODUCTION
ws = wb.create_sheet("Production")
ws.append(["Code","Owner","Posts","Brief","Used on"])
for p in D["production"]:
    ws.append([p["code"], p["owner"], p["posts"], p["brief"], ", ".join(p["dates"])])
widths(ws,[13,15,7,104,42]); head(ws); body(ws, 74, bold=(0,))
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    if str(row[0].value).startswith("SHOOT"):
        for c in row: c.fill = PatternFill("solid", fgColor="FBF3E6")
    if "PRIORITY" in str(row[3].value): row[3].font = Font(size=9, bold=True, color="96303C")

# ---------------------------------------------------------------- REFERENCE LIBRARY
ws = wb.create_sheet("Reference Library")
ws.append(["Content type","Account","What it demonstrates","Real result","Used on","Link"])
for r in D["referenceLibrary"]:
    ws.append([r["key"].replace("_"," "), r["account"], r["why"], r["metric"], r["usedOn"], r["url"]])
widths(ws,[22,22,74,46,9,44]); head(ws); body(ws, 46, bold=(0,))
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    u = row[5].value
    if u:
        row[5].hyperlink = u; row[5].value = u.replace("https://","")
        row[5].font = Font(size=9, color="12355B", underline="single")

# ---------------------------------------------------------------- EDIT SPECS
ws = wb.create_sheet("Edit Specs")
ws.append(["Format","Target length","How to cut it","What goes on screen","Audio"])
for name, spec in D["editSpecs"].items():
    ws.append([name, spec["length"], spec["cut"], spec["onScreen"], spec["audio"]])
widths(ws,[22,20,80,74,58]); head(ws); body(ws, 80, bold=(0,))
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    row[0].font = Font(size=10, bold=True, color=FMT_COLOR.get(row[0].value, NAVY))

wb.save(OUT)
print("saved:", OUT)
print("sheets:", wb.sheetnames)
print("calendar columns:", 25, "| drive links:", sum(1 for i in D["items"] if i["driveUrl"]),
      "| warnings:", sum(1 for i in D["items"] if i.get("editWarnings")))
