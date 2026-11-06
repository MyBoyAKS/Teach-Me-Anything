# Teach Me Anything

**Three learning modes for AI tutors: Normal, Widget and Ultra.**
Paste these files into any AI assistant (Claude, ChatGPT, Gemini, …) and it will teach you the way that actually sticks: real numbers first, one idea per step, moving algebra synced with a graph, arrows on exactly what is being explained, and practice that proves you can do it alone.

🌐 **Website:** https://myboyaks.github.io/Teach-Me-Anything/

Created by **Kenzie** (GitHub: [@MyBoyAKS](https://github.com/MyBoyAKS)).
Built while learning Calculus 1, but written for **any subject**: maths, physics, programming, chemistry, economics, languages.

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

Full specs:
- [`modes/normal.md`](modes/normal.md)
- [`modes/widget.md`](modes/widget.md)
- [`modes/ultra.md`](modes/ultra.md)

Who the learner is and how they learn best: [`learner-profile.md`](learner-profile.md) (a template, with Kenzie's version as the example).

How to build the Widget "video" page: [`widget-engine.md`](widget-engine.md) (the technical recipe, so any AI can rebuild it).

Working examples you can open in a browser: [`examples/`](examples/).

---

## How to use it

### Option A: one-paste quick start (works with any AI)
Copy everything in [`quick-start.md`](quick-start.md) into a new chat, fill in your own learner profile, then ask your question and say which mode you want, e.g.:

> "Ultra mode: teach me how to find where two lines cross."

### Option B: as project files / custom instructions
Upload the whole folder as project knowledge (Claude Projects, ChatGPT custom GPT, Gemini Gems, etc.), or paste `learner-profile.md` into custom instructions and keep the `modes/` files as reference.

### If your AI cannot make interactive pages
Widget and Ultra need an AI that can create a web page (an HTML artifact / canvas / file). If it cannot:
1. ask it to write the page as a single `.html` file, then save it and open it in your browser, or
2. fall back to Normal mode with a written step list and a description of the picture.

---

## The core ideas (why it works)

1. **Real numbers first.** Every new idea starts with a concrete example (r = 3, x = 0.1), then the letters come back.
2. **One idea per step.** Each step has a short title and 1 to 2 plain sentences saying *why*.
3. **Show every step.** Never skip arithmetic: write "4 + (−4)(1) = 0", not just "0".
4. **Point at it.** When a step talks about one term, that term gets a highlight box and an arrow with a short label.
5. **Picture and algebra move together.** The graph follows the same timeline as the equations, so every sentence connects to something you can see.
6. **The learner does the last step.** Hints before answers; check numbers so you can test yourself.
7. **Write it down properly.** The last part always shows exactly what to write in your notebook.

---

## Credits

- Concept, learning style and testing: **Kenzie** (GitHub: [@MyBoyAKS](https://github.com/MyBoyAKS))
- Built with help from Claude (Anthropic)

## License

To be added. (Until a license is chosen, all rights are reserved by the author.)
