"""TMA annotate: draw teacher-style marks directly on a photo of handwritten work.

Usage:  python TMA_annotate.py photo.jpg marks.json out.png

marks.json is a list of marks. All positions are fractions (0..1) of the photo's
width and height, so estimate them by looking at the photo.

  red    {"color": "red", "shape": "box"|"circle", "box": [x0, y0, x1, y1],
          "label": "1", "note": "why it's wrong"}
  green  {"color": "green", "text": "the fix", "near": <index of the red mark>,
          "side": "right"|"left"|"below"|"above"}          (correction beside a red mark)
  green  {"color": "green", "shape": "check", "at": [x, y]} (a tick next to a correct line)
  yellow {"color": "yellow", "shape": "box", "box": [x0, y0, x1, y1],
          "label": "1", "note": "fine, but ... (option)"}

Optional on red/yellow: "note_side": "below" (default) | "right",
or "note_at": [x, y] to put the note in empty space; a thin line joins it to the mark.

Requires Pillow (pip install pillow). Works on phone photos (EXIF rotation is fixed).
"""
import json
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

COLORS = {"red": (220, 38, 38), "green": (22, 163, 74), "yellow": (217, 160, 0)}
FILL = {"red": (255, 255, 255), "green": (236, 253, 243), "yellow": (255, 249, 219)}


def load_font(size):
    for name in ("DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                 "Arial Bold.ttf", "arialbd.ttf", "Helvetica.ttc"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def text_box(d, xy, text, font, color, fill, lw):
    x, y = xy
    pad = max(6, lw * 2)
    lines = text.split("\n")
    lh = d.textbbox((0, 0), "Ag", font=font)[3] + pad // 2
    w = max(d.textbbox((0, 0), ln, font=font)[2] for ln in lines)
    box = (x - pad, y - pad, x + w + pad, y + lh * len(lines) + pad // 2)
    d.rounded_rectangle(box, radius=pad, fill=fill + (245,), outline=color + (255,), width=max(2, lw // 2 + 1))
    for i, ln in enumerate(lines):
        d.text((x, y + i * lh), ln, font=font, fill=color + (255,))
    return box


def annotate(img, marks):
    img = ImageOps.exif_transpose(img).convert("RGB")
    W, H = img.size
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    lw = max(3, W // 220)
    font = load_font(max(16, W // 34))
    small = load_font(max(13, W // 50))
    P = lambda fx, fy: (fx * W, fy * H)
    boxes = []
    for m in marks:
        c = m["color"]
        col = COLORS[c]
        if c in ("red", "yellow") and "box" in m:
            x0, y0 = P(*m["box"][:2])
            x1, y1 = P(*m["box"][2:])
            boxes.append((x0, y0, x1, y1))
            if c == "yellow":
                d.rounded_rectangle((x0, y0, x1, y1), radius=12, fill=col + (40,))
            if m.get("shape") == "circle":
                d.ellipse((x0, y0, x1, y1), outline=col + (255,), width=lw)
            else:
                d.rounded_rectangle((x0, y0, x1, y1), radius=12, outline=col + (255,), width=lw)
            if m.get("label"):
                r = max(14, W // 55)
                d.ellipse((x0 - r, y0 - r, x0 + r, y0 + r), fill=col + (255,))
                d.text((x0, y0), m["label"], font=small, fill=(255, 255, 255), anchor="mm")
            if m.get("note"):
                if m.get("note_at"):
                    nb = text_box(d, P(*m["note_at"]), m["note"], small, col, FILL[c], lw)
                    # leader line from note to the nearest edge of the mark
                    nx = min(max((nb[0] + nb[2]) / 2, x0), x1)
                    ny = y1 if nb[1] > y1 else (y0 if nb[3] < y0 else (y0 + y1) / 2)
                    sx = nb[0] if nb[0] > x1 else (nb[2] if nb[2] < x0 else (nb[0] + nb[2]) / 2)
                    sy = (nb[1] + nb[3]) / 2 if (nb[0] > x1 or nb[2] < x0) else (nb[1] if nb[1] > y1 else nb[3])
                    d.line((sx, sy, nx, ny), fill=col + (255,), width=max(2, lw // 2))
                elif m.get("note_side") == "right":
                    text_box(d, (x1 + lw * 4, y0 + (y1 - y0) * 0.2), m["note"], small, col, FILL[c], lw)
                else:
                    text_box(d, (x0, y1 + lw * 3), m["note"], small, col, FILL[c], lw)
        else:
            boxes.append(None)
    for m in marks:
        if m["color"] != "green":
            continue
        g = COLORS["green"]
        if m.get("shape") == "check":
            x, y = P(*m["at"])
            s = max(18, W // 45)
            d.line((x, y, x + s * 0.4, y + s * 0.45, x + s, y - s * 0.55), fill=g + (255,), width=lw + 1, joint="curve")
            continue
        tgt = boxes[m["near"]] if m.get("near") is not None and boxes[m["near"]] else (0.05 * W,) * 2 + (0.05 * W,) * 2
        x0, y0, x1, y1 = tgt
        side = m.get("side", "right")
        tw = d.textbbox((0, 0), m["text"], font=font)[2]
        if side == "right":
            pos = (min(x1 + 30, W - tw - 20), y0)
        elif side == "left":
            pos = (max(10, x0 - tw - 40), y0)
        elif side == "below":
            pos = (x0, y1 + 50)
        else:
            pos = (x0, max(10, y0 - 70))
        bx = text_box(d, pos, m["text"], font, g, FILL["green"], lw)
        sx, sy = (x1, (y0 + y1) / 2) if side == "right" else ((x0 + x1) / 2, y1 if side == "below" else y0)
        ex, ey = (bx[0], (bx[1] + bx[3]) / 2) if side == "right" else ((bx[0] + bx[2]) / 2, bx[1] if side == "below" else bx[3])
        d.line((sx, sy, ex, ey), fill=g + (255,), width=lw)
    return Image.alpha_composite(img.convert("RGBA"), over).convert("RGB")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    src, marks_path, out = sys.argv[1:]
    with open(marks_path, encoding="utf-8") as f:
        marks = json.load(f)
    annotate(Image.open(src), marks).save(out)
    print("saved", out)
