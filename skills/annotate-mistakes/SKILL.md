---
name: annotate-mistakes
description: Mark up a photo of a learner's handwritten work like a teacher: red circles or boxes around mistakes, a green correction beside each, yellow boxes for "not wrong but could be better". Use when the learner sends a photo of their notebook, worksheet or whiteboard, or when they are confused and you asked to see what they wrote.
---

# Annotate mistakes

Use this whenever the learner shares a photo of their work, or seems stuck (then ask: "Can you send a photo of what you wrote?").

## Colours

- **Red** (circle or box): wrong. Mark the smallest wrong thing (one sign, one number, one line). Add a short reason.
- **Green** (text next to the red mark): the corrected version, exactly what to write instead.
- **Yellow** (box): not wrong, but could be better: a shorter method, a missing step, clearer notation. Give the option.

## Steps

1. Read the whole photo first. Check every line, not just the final answer.
2. Decide the marks. Number them: red 1, red 2, yellow 1, …
3. Draw them:
   - If you can run Python, use `annotate.py` in this folder (see below).
   - If you can only make web pages, rebuild the page as notebook-style HTML with the same colours.
   - Otherwise use 🔴 🟢 🟡 in text and quote each line.
4. Reply with the list of marks, "everything else is correct" if true, the next line to write, and check numbers.
5. Never invent lines the learner didn't write. If something is unreadable, ask.

## Using annotate.py

Positions are fractions of the image width/height (0 to 1), so you don't need exact pixels: estimate where the line is.

```bash
python annotate.py photo.jpg marks.json out.png
```

`marks.json`:

```json
[
  {"color": "red",    "shape": "box",    "box": [0.30, 0.62, 0.62, 0.68], "label": "1", "note": "− × − = +"},
  {"color": "green",  "text": "b = 9/2", "near": 0, "side": "right"},
  {"color": "yellow", "shape": "box",    "box": [0.08, 0.40, 0.55, 0.46], "label": "1", "note": "fine, or write −2a = 3 directly"}
]
```

- `shape`: `box` or `circle` (red/yellow). `note_side`: `below` (default) or `right`, to keep the note off the next line.
- `near`: index of the mark this green fix belongs to; `side`: `right`, `left`, `below` or `above`.
- Check the output image before sending: marks must sit on the right lines. Adjust the fractions and re-run if not.
