# Teach Me Anything

**Three learning modes for AI tutors: Normal, Widget and Ultra.**
Paste one prompt into any AI assistant (ChatGPT, Gemini, Claude, …) and it teaches step-by-step subjects the way that actually sticks: real numbers first, one idea per step, moving algebra synced with a graph, arrows on exactly what is being explained, and practice that proves you can do it alone.

🌐 **Website:** https://myboyaks.github.io/Teach-Me-Anything/
▶️ **50-second how-to video:** [examples/how-to-use.html](https://myboyaks.github.io/Teach-Me-Anything/examples/how-to-use.html)

Created by **Kenzie** (GitHub: [@MyBoyAKS](https://github.com/MyBoyAKS)). Built while learning Calculus 1.

---

## Best for (and not for)

It shines when a topic has **steps that transform something** (equations, matrices, code, reactions) and **something you can draw** (a graph or diagram).

| ✅ Great | 🟡 Okay | ❌ Not ideal |
|---|---|---|
| Calculus · Linear algebra · Physics · Chemistry calculations · Statistics & probability · Programming logic | Economics models · Chemistry theory/mechanisms | Mostly-reading subjects (history, literature, biology facts) · Vocabulary and speaking in languages · Hands-on lab skills |

**Normal mode** still helps with almost anything. **Widget** and **Ultra** are built for the ✅ column.

---

## The 3 modes at a glance

| | Normal | Widget | Ultra |
|---|---|---|---|
| Where | in the chat | one interactive page | one bigger interactive page |
| Style | written, step by step | a short "video" you can scrub | the video + things you do yourself |
| Moving algebra / diagrams | no | yes | yes |
| Synced graph or picture | small table or chart at most | yes | yes, plus a second view if useful |
| Arrows + highlights on the term being explained | no | yes | yes |
| "Pick the next step" puzzles | no | no | yes |
| Explore lab (sliders) | no | no | yes |
| Notebook page ("write this in your book") | short version | final chapter | full page with ✓ ✗ marks |
| Quiz | quick check numbers | answer check | short quiz |
| Length | quick read | 1 to 4 minutes | 5 to 8 minutes + practice |

Full specs: [`modes/normal.md`](modes/normal.md) · [`modes/widget.md`](modes/widget.md) · [`modes/ultra.md`](modes/ultra.md)
Learner profile template: [`learner-profile.md`](learner-profile.md)
How to build the Widget page: [`widget-engine.md`](widget-engine.md)
What the research says: [`evidence.md`](evidence.md)

---

## How to use it

▶️ Watch the [50-second walkthrough](https://myboyaks.github.io/Teach-Me-Anything/examples/how-to-use.html) first, or follow these steps:

### Option A: one paste (any AI)
1. Open [`quick-start.md`](quick-start.md) (or press **Copy prompt** on the [website](https://myboyaks.github.io/Teach-Me-Anything/#quick-start)).
2. Open a new chat in your AI and paste it.
3. Replace the `[brackets]` with your own profile: subject, what you know, what trips you up.
4. Send it, then ask your question and name a mode:
   > "Widget mode: teach me row reduction."
   > "Ultra mode: teach me how to balance Fe + O₂ → Fe₂O₃."
   > "Normal mode: check my answer (photo attached)."

### Option B: upload once
Add the `.md` files as project files / knowledge (Projects, custom GPTs, Gems, …), or paste [`learner-profile.md`](learner-profile.md) into custom instructions. Then just ask.

### If your AI can't make interactive pages
Widget and Ultra need an AI that can create a web page (an artifact / canvas / file). If yours can't, ask for **one `.html` file**, save it and open it in your browser, or fall back to Normal mode.

---

## The core ideas (the principles behind every lesson)

These are the **rules** every mode follows. The demos are where you can **see** them in action:

| # | Idea | See it in |
|---|---|---|
| 1 | **Real numbers first**, then letters (r = 3, x = 0.1). | [basic demo](examples/widget-demo-basic.html): solving with real numbers |
| 2 | **One idea per step**: short title + 1 to 2 sentences of *why*. | every chapter of both demos |
| 3 | **Show every step.** Never skip arithmetic ("4 + (−4)(1) = 0", not "0"). | [pointer demo](examples/widget-demo-pointers.html): "1a − 3a = −2a" |
| 4 | **Point at it**: the term being explained gets a highlight box and an arrow. | [pointer demo](examples/widget-demo-pointers.html): "put −3a here" |
| 5 | **Picture and algebra move together** on one timeline. | [basic demo](examples/widget-demo-basic.html): the lines move but always cross at x = 2 |
| 6 | **The learner does the last step**: hints before answers, check numbers. | Ultra puzzles ([`modes/ultra.md`](modes/ultra.md)) |
| 7 | **Write it down properly**: always ends with what to write in your notebook. | last chapter of every Widget lesson |

Why these work, with research: [`evidence.md`](evidence.md).

---

## Credits

- Concept, learning style and testing: **Kenzie** (GitHub: [@MyBoyAKS](https://github.com/MyBoyAKS))
- Built with help from Claude (Anthropic)

## License

To be added. (Until a license is chosen, all rights are reserved by the author.)
