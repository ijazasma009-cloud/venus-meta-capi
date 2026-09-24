# Reel cover / thumbnail - built separately so the IG feed crop stays clean.
from PIL import Image, ImageDraw, ImageFilter
import numpy as np, math, json, re

W, H = 1080, 1920
INK = (8, 8, 10)
IVORY = (245, 240, 232)
GOLD = (201, 162, 75)
GOLDHI = (232, 200, 116)

# real verified total, read straight from data.js so it can never drift
src = open('data.js', encoding='utf8').read()
counts = [int(m) for m in re.findall(r'count:(\d+)', src)]
TOTAL = sum(counts)
DATE = re.search(r"CAPTURE_DATE = '([^']+)'", src).group(1)

def font(path, size, wght=None, ital=False):
    from PIL import ImageFont
    f = ImageFont.truetype(path, size)
    try:
        if wght is not None:
            axes = f.get_variation_axes()
            vals = []
            for a in axes:
                nm = a['name'].decode() if isinstance(a['name'], bytes) else str(a['name'])
                vals.append(wght if 'eight' in nm or 'wght' in nm.lower() else a['default'])
            f.set_variation_by_axes(vals)
    except Exception:
        pass
    return f

AR = 'fonts/Archivo.ttf'
CG = 'fonts/CormorantGaramond.ttf'

img = Image.new('RGB', (W, H), INK)
d = ImageDraw.Draw(img)

# --- brand texture background: soft gold field + fine grain ---
glow = Image.new('RGB', (W, H), INK)
gd = ImageDraw.Draw(glow)
for r in range(900, 0, -12):
    a = (1 - r / 900) ** 2.1
    c = (int(8 + 42 * a), int(8 + 33 * a), int(10 + 14 * a))
    gd.ellipse([W // 2 - r, int(H * 0.40) - r, W // 2 + r, int(H * 0.40) + r], fill=c)
glow = glow.filter(ImageFilter.GaussianBlur(70))
img = Image.blend(img, glow, 0.95)
d = ImageDraw.Draw(img)

# fine diagonal line pattern (Venus brand line motif), very low contrast
lp = Image.new('L', (W, H), 0)
ld = ImageDraw.Draw(lp)
for xk in range(-H, W + H, 26):
    ld.line([(xk, 0), (xk + H, H)], fill=16, width=1)
img = Image.composite(Image.new('RGB', (W, H), (60, 50, 32)), img, lp.point(lambda v: v))

d = ImageDraw.Draw(img)

def track_text(dr, txt, cy, f, sp, fill, cx=W // 2):
    widths = [dr.textlength(ch, font=f) for ch in txt]
    tot = sum(widths) + sp * (len(txt) - 1)
    x = cx - tot / 2
    for ch, w in zip(txt, widths):
        dr.text((x, cy), ch, font=f, fill=fill, anchor='lm')
        x += w + sp

# --- top line ---
track_text(d, 'A VENUS MILESTONE', H * 0.235, font(AR, 26, 500), 11, (245, 240, 232, 255))

# hairline
d.line([(W / 2 - 150, H * 0.272), (W / 2 + 150, H * 0.272)], fill=GOLD, width=2)

# --- hero number ---
num = '10,000+'
size = 300
while size > 60:
    fnum = font(AR, size, 800)
    if d.textlength(num, font=fnum) <= W - 110:
        break
    size -= 4
print('  hero mark fitted at', size, 'px  width',
      round(d.textlength(num, font=fnum)), '/', W - 110)
d.text((W / 2, H * 0.383), num, font=fnum, fill=IVORY, anchor='mm')

# --- subline ---
track_text(d, 'TIMES YOU CHOSE VENUS.', H * 0.502, font(AR, 44, 600), 5, IVORY)

# --- gratitude ---
fit = font(CG, 68)
d.text((W / 2, H * 0.567), 'THANK YOU, PAKISTAN.', font=fit, fill=GOLDHI, anchor='mm')

# --- stars ---
def star(dr, cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r * 0.45 if i % 2 else r
        pts.append((cx + math.cos(ang) * rr, cy + math.sin(ang) * rr))
    dr.polygon(pts, fill=fill)

sy = H * 0.648
gap = 40
sx = W / 2 - gap * 2
for i in range(5):
    star(d, sx + i * gap, sy, 15, (245, 179, 1))

# --- micro proof line ---
track_text(d, f'{TOTAL:,} GOOGLE REVIEWS', H * 0.690, font(AR, 26, 500), 8, (200, 195, 186))
track_text(d, f'VERIFIED {DATE}', H * 0.727, font(AR, 20, 400), 4, (120, 116, 110))

# --- logo ---
logo = Image.open('img/logo.png').convert('RGBA')
lw = 560
lh = int(lw * logo.height / logo.width)
logo = logo.resize((lw, lh), Image.LANCZOS)
img.paste(logo, (W // 2 - lw // 2, int(H * 0.815) - lh // 2), logo)

# --- vignette + grain ---
a = np.asarray(img).astype(np.float32)
yy, xx = np.mgrid[0:H, 0:W]
r = np.sqrt(((xx - W / 2) / (W * 0.78)) ** 2 + ((yy - H * 0.46) / (H * 0.62)) ** 2)
a *= np.clip(1.06 - 0.62 * r ** 2.1, 0, 1)[..., None]
rng = np.random.default_rng(3)
a += rng.normal(0, 2.6, a.shape)
Image.fromarray(np.clip(a, 0, 255).astype('uint8')).save('cover.jpg', quality=95, subsampling=0)
print('cover.jpg written | mark 10,000+ | verified total', f'{TOTAL:,}')
