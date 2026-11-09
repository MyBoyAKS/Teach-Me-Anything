# Annotate my work

**What it is:** the learner sends a photo of what they wrote (notebook, worksheet, whiteboard). The AI marks it up like a teacher with three colours, then explains each mark. Works with every mode.

---

## When to use it

- The learner sends a photo of their work.
- The learner seems confused, says "I don't get it", or their answer doesn't match. **Ask them to send a photo of what they wrote** before explaining again: the mistake is usually in one specific line.

## The three colours

| Colour | Shape | Means | Always add |
|---|---|---|---|
| 🔴 **Red** | circle or box around the exact line, term or number | **wrong** | a short reason ("sign slip: − × − = +") |
| 🟢 **Green** | written right next to (or under) the red mark | **the corrected version** | exactly what to write instead |
| 🟡 **Yellow** | box | **not wrong, but could be better**: a shorter way, a missing step, unclear notation, a different method | the option(s), e.g. "fine, or factor first: shorter" |

Rules:
- Mark the **smallest** thing that is wrong (the one sign, not the whole page).
- Every red mark gets a green fix next to it.
- Yellow is optional advice, never a penalty.
- Number the marks (red 1, red 2, yellow 1…) and list them in the reply too.
- **Never invent lines the learner didn't write.** If a line is unreadable, ask.
- End with "what to write next".

## How to draw the marks (pick the first that works)

1. **AI can run code** (code interpreter / analysis tool): draw directly on the learner's photo, e.g. with [`../skills/annotate-mistakes/annotate.py`](../skills/annotate-mistakes/annotate.py), and send back the marked-up image.
2. **AI can make web pages but can't edit the photo:** rebuild the learner's page as a notebook-style HTML page (lined paper, their own lines and notation), with red boxes and strike-outs, green "write instead" boxes, and yellow suggestion boxes.
3. **Chat only:** quote each line and use 🔴 🟢 🟡 in the text:
   > 🔴 1. `b = −3(−3/2) = −9/2`: minus × minus is plus.
   > 🟢 1. write `b = 9/2`
   > 🟡 1. `a + (−3a) = 3` is fine; you can write `−2a = 3` directly.

## Reply template

```
Here's your page marked up (🔴 wrong · 🟢 fix · 🟡 could be better).

🔴 1  line …: …  →  🟢 write: …
🟡 1  line …: fine, but …  (option: …)

✓ Everything else is correct.
Next line to write: …
Check: your answer should be …
```
