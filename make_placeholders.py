"""Generate placeholder assets so the site looks finished before you have
your own photos. Run with:  python make_placeholders.py
Delete this file once you have replaced everything."""

from PIL import Image, ImageDraw, ImageFilter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import math

# --- banner ------------------------------------------------------------
# A dusk sky with layered ridge silhouettes. Deliberately dark and
# low-contrast in the middle so white text stays readable on top of it.
W, H = 2400, 820
banner = Image.new("RGB", (W, H))
d = ImageDraw.Draw(banner)

top = (38, 52, 74)        # deep blue
mid = (96, 104, 118)      # haze
low = (196, 158, 122)     # warm amber near the horizon
for y in range(H):
    t = y / H
    if t < 0.62:
        u = t / 0.62
        c = tuple(int(top[i] + (mid[i] - top[i]) * u) for i in range(3))
    else:
        u = (t - 0.62) / 0.38
        c = tuple(int(mid[i] + (low[i] - mid[i]) * u) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)

def ridge(y_base, amp, freq, phase, colour):
    pts = [(x, y_base + amp * math.sin(x / freq + phase)
                  + amp * 0.4 * math.sin(x / (freq * 0.37) + phase * 2))
           for x in range(0, W + 10, 10)]
    d.polygon(pts + [(W, H), (0, H)], fill=colour)

ridge(H * 0.60, 46, 300, 0.0, (108, 112, 118))
ridge(H * 0.70, 58, 240, 1.7, (74, 79, 88))
ridge(H * 0.80, 44, 190, 3.1, (48, 53, 62))
ridge(H * 0.90, 34, 150, 5.0, (30, 34, 41))

banner = banner.filter(ImageFilter.GaussianBlur(1.2))

# darken the centre band so the overlaid title always has contrast
veil = Image.new("L", (W, H), 0)
vd = ImageDraw.Draw(veil)
for y in range(H):
    vd.line([(0, y), (W, y)], fill=int(90 * math.sin(math.pi * y / H)))
banner = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), banner, veil)
banner.save("images/banner.jpg", quality=88)

# --- profile photo placeholder ----------------------------------------
img = Image.new("RGB", (760, 950), (231, 233, 236))
p = ImageDraw.Draw(img)
p.ellipse((272, 208, 488, 424), fill=(203, 207, 213))
p.ellipse((176, 468, 584, 950), fill=(203, 207, 213))
p.text((236, 892), "replace with images/profile.jpg", fill=(122, 128, 135))
img.save("images/profile.jpg", quality=90)

# --- favicon -----------------------------------------------------------
fav = Image.new("RGB", (256, 256), (44, 62, 80))
fd = ImageDraw.Draw(fav)
fd.text((100, 112), "TF", fill=(255, 255, 255))
fav.save("images/favicon.png")

# --- placeholder PDFs --------------------------------------------------
pdfs = {
    "files/freshwater-consumption.pdf": "Unsustainable global freshwater consumption - placeholder",
    "files/animal-food-kuznets-curve.pdf": "Animal Food Kuznets Curve - placeholder",
    "files/economic-exposure.pdf": "Economic Exposure and Climate Policy Support - placeholder",
}
for path, title in pdfs.items():
    c = canvas.Canvas(path, pagesize=A4)
    c.setFont("Helvetica", 14)
    c.drawString(72, 760, title)
    c.setFont("Helvetica", 10)
    c.drawString(72, 735, "Replace this file with the real PDF, keeping the same filename.")
    c.save()

print("placeholders written")
