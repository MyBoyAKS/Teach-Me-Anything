"""Draw teacher-style marks on a photo of handwritten work.

Usage:  python annotate.py photo.jpg marks.json out.png

marks.json is a list of marks. Positions are fractions (0..1) of the image size.
  red / yellow: {"color": "red", "shape": "box"|"circle", "box": [x0, y0, x1, y1],
                 "label": "1", "note": "short reason", "note_side": "below"|"right"}
  green:        {"color": "green", "text": "the fix", "near": <index of a mark>,
                 "side": "right"|"left"|"below"|"above"}
Requires Pillow (pip install pillow).
"""
import json
import sys

from PIL import Image, ImageDraw, ImageFont

COLORS = {"red": (220, 38, 38), "green": (22, 163, 74), "yellow": (234, 179, 8)}


def load_font(size):
    for name in ("DejaVuSans-Bold.ttf", "Arial Bold.ttf", "arialbd.ttf", "Helvetica.ttc"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def text_box(draw, xy, text, font, fg, bg=(255, 255, 255), pad=6):
    x, y = xy
    l, t, r, b = draw.textbbox((x, y), text, font=font)
    draw.rounded_rectangle((l - pad, t - pad, r + pad, b + pad), radius=pad, fill=bg, outline=fg, width=3)
    draw.text((x, y), text, font=font, fill=fg)
    return (l - pad, t - pad, r + pad, b + pad)


def annotate(img, marks):
    img = img.convert("RGB")
    W, H = img.size
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    lw = max(3, W // 250)
    font = load_font(max(14, W // 40))
    small = load_font(max(12, W // 52))
    boxes = []
    for m in marks:
        col = COLORS[m["color"]]
        if m["color"] in ("red", "yellow"):
            x0, y0, x1, y1 = (m["box"][0] * W, m["box"][1] * H, m["box"][2] * W, m["box"][3] * H)
            boxes.append((x0, y0, x1, y1))
            if m["color"] == "yellow":
                d.rounded_rectangle((x0, y0, x1, y1), radius=10, fill=col + (45,))
            if m.get("shape") == "circle":
                d.ellipse((x0, y0, x1, y1), outline=col + (255,), width=lw)
            else:
                d.rounded_rectangle((x0, y0, x1, y1), radius=10, outline=col + (255,), width=lw)
            label = m.get("label")
            if label:
                r = max(12, W // 60)
                d.ellipse((x0 - r, y0 - r, x0 + r, y0 + r), fill=col + (255,))
                d.text((x0, y0), label, font=small, fill=(255, 255, 255), anchor="mm")
            if m.get("note"):
                if m.get("note_side") == "right":
                    text_box(d, (x1 + 16, y0 + (y1 - y0) * 0.25), m["note"], small, col + (255,))
                else:
                    text_box(d, (x0, y1 + lw * 3), m["note"], small, col + (255,))
        else:
            boxes.append(None)
    for m in marks:
        if m["color"] != "green":
            continue
        tgt = boxes[m["near"]] if m.get("near") is not None and boxes[m["near"]] else (0.05 * W, 0.05 * H, 0.05 * W, 0.05 * H)
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
            pos = (x0, max(10, y0 - 60))
        bx = text_box(d, pos, m["text"], font, COLORS["green"] + (255,), bg=(236, 253, 243))
        # arrow from the red mark to the green fix
        sx, sy = (x1, (y0 + y1) / 2) if side == "right" else ((x0 + x1) / 2, y1)
        ex, ey = (bx[0], (bx[1] + bx[3]) / 2) if side == "right" else ((bx[0] + bx[2]) / 2, bx[1])
        d.line((sx, sy, ex, ey), fill=COLORS["green"] + (255,), width=lw)
    return Image.alpha_composite(img.convert("RGBA"), over).convert("RGB")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    src, marks_path, out = sys.argv[1:]
    with open(marks_path, encoding="utf-8") as f:
        marks = json.load(f)
    annotate(Image.open(src), marks).save(out)
    print("saved", out)
