# Teach Me Anything

[![Docs: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue)](LICENSE-CODE)
[![Works with: any AI](https://img.shields.io/badge/works%20with-any%20AI-green)](#3-ai-compatibility)
[![Made with: Claude](https://img.shields.io/badge/made%20with-Claude-d97757)](#2-how-this-repo-was-made)

**Three learning modes for AI tutors: Normal, Widget and Ultra.**
Paste one prompt into an AI assistant and it teaches step-by-step subjects (calculus, linear algebra, physics, chemistry, statistics, programming) the way that actually sticks: real numbers first, one idea per step, moving algebra synced with a graph, arrows on exactly what is being explained, and practice that proves you can do it alone.

> [!NOTE]
> **License:** the guides and prompts are **CC BY 4.0** (use, share and adapt freely, just credit **Kenzie / @MyBoyAKS**). The example code in `examples/` is **MIT**.

---

## Table of contents

1. [Teach Me Anything](#teach-me-anything)
2. [How this repo was made](#2-how-this-repo-was-made)
3. [AI compatibility](#3-ai-compatibility)
4. [The 3 modes](#4-the-3-modes)
5. [DOWNLOAD](#5-download)
6. [The core ideas](#6-the-core-ideas)
7. [Credit](#7-credit)

---

## 2. How this repo was made

While I was learning Calculus 1, I suddenly got inspired to turn my study sessions into a learning course with Claude. Every time something didn't click, I changed how I asked: more real numbers, slower steps, a graph next to the algebra, arrows on the exact term being explained, puzzles to test myself. I kept improving the prompt and the output until I could understand things **better and faster**.

This repo is the result: the prompt, the three modes, and the rules behind them, so anyone can learn the same way.

---

## 3. AI compatibility

| AI assistant | Normal | Widget / Ultra | Notes |
|---|---|---|---|
| **Claude** ⭐ recommended | ✅ | ✅ | Built and tested with Claude. It can create interactive pages (artifacts) directly in the chat. |
| ChatGPT | ✅ | ✅ if it can create an HTML page / canvas | Otherwise ask for a single `.html` file and open it in your browser. |
| Gemini | ✅ | ✅ if it can create an HTML page / canvas | Same fallback as above. |
| Other assistants | ✅ | ⚠️ depends | Any AI works for Normal mode. Widget and Ultra need one that can write a working web page. |

**Best subjects:** step-by-step STEM (calculus, linear algebra, physics, chemistry calculations, statistics, programming logic). Mostly-reading subjects, vocabulary and hands-on lab skills are not a good fit for Widget and Ultra, but Normal mode still helps.

---

## 4. The 3 modes

| | Normal | Widget | Ultra |
|---|---|---|---|
| Goal | read and fix | watch and understand | prove you can do it |
| Where | in the chat | one interactive page | one bigger interactive page |
| Moving algebra + synced graph | ✗ | ✓ | ✓ |
| Arrows + highlights on the term being explained | ✗ | ✓ | ✓ |
| "Pick the next step" puzzles | ✗ | ✗ | ✓ |
| Explore lab (sliders) | ✗ | ✗ | ✓ |
| Notebook page ("write this in your book") | short | last chapter | full, with ✓ ✗ marks |
| Quiz | check numbers | answer check | short quiz |
| Length | quick read | 1 to 4 min | 5 to 8 min + practice |

- **Normal:** a written, step-by-step explanation in the chat. It points to the exact wrong line in your work and tells you what to write next.
- **Widget:** a short "video" you can scrub with a slider. Terms slide, morph and get struck out; arrows point at what's being explained; a graph moves on the same timeline.
- **Ultra:** everything in Widget, plus puzzles between chapters, an explore lab, your notebook page remade with ✓ ✗ marks, and a quiz.

**Widget mode in action** (a real Calculus homework step):

<p align="center"><img src="assets/mode-widget.gif" width="340" alt="Widget mode: moving algebra with arrows and a synced graph"></p>

Full specs: [`modes/normal.md`](modes/normal.md) · [`modes/widget.md`](modes/widget.md) · [`modes/ultra.md`](modes/ultra.md) · Research behind the modes: [`evidence.md`](evidence.md)

---

## 5. DOWNLOAD

<p align="center">
  <a href="https://github.com/MyBoyAKS/Teach-Me-Anything/raw/main/Teach-Me-Anything-AI-pack.zip"><img src="https://img.shields.io/badge/Download%20AI%20pack%20(.zip)-2ea043?style=for-the-badge&logo=github&logoColor=white" alt="Download AI pack" height="42"></a>
</p>
<p align="center"><sub>The <b>AI pack</b> is tiny (about 14 KB, only the .md files the AI needs), so it uploads fully every time.<br>Want everything, including the GIFs and demo pages? <a href="https://github.com/MyBoyAKS/Teach-Me-Anything/archive/refs/heads/main.zip">Download the full repo ZIP</a> (about 4 MB, not for uploading to an AI).</sub></p>

<p align="center"><img src="assets/tutorial.gif" width="340" alt="Tutorial: download the ZIP, unzip, give the files to your AI, answer its questions, get your lesson"></p>

### Option A: give everything to the AI (recommended)
1. **Download:** click the green **Download AI pack** button above. You get `Teach-Me-Anything-AI-pack.zip`.
2. **Unzip:** right-click the file → **Extract All** (Windows) or double-click it (Mac). On a phone, open it in your Files app and tap **Extract**.
3. **Give it to your AI:** open a new chat and drag in all the **.md files** from the folder. Then send **`Start`**.
4. **Answer the AI:** it reads `START-HERE.md` and asks you:
   - what subject you're studying,
   - what you already know well,
   - what usually trips you up,
   - what you want to learn first, and which mode (**Normal**, **Widget** or **Ultra**).
5. **Learn:** it builds your lesson in the mode you picked.

> [!IMPORTANT]
> Upload the **AI pack** (or the .md files), not the full repo ZIP. The full ZIP is mostly GIFs and can get cut off during upload, so the AI ends up missing files.

> [!TIP]
> Using Claude? Put the files in a **Project** once, and every new chat in that project already knows the method.

### Option B: file by file (if you'd rather check everything yourself)
Don't want to download a ZIP from a stranger? Fair. Every file is plain text, so you can **read each one first** and download only what you want:

| File | What it is | Download |
|---|---|:-:|
| [`START-HERE.md`](START-HERE.md) | tells the AI what to do first | [⬇ download](https://github.com/MyBoyAKS/Teach-Me-Anything/raw/main/START-HERE.md) |
| [`quick-start.md`](quick-start.md) | the full prompt and the 3 modes | [⬇ download](https://github.com/MyBoyAKS/Teach-Me-Anything/raw/main/quick-start.md) |
| [`learner-profile.md`](learner-profile.md) | profile template + example | [⬇ download](https://github.com/MyBoyAKS/Teach-Me-Anything/raw/main/learner-profile.md) |
| [`modes/normal.md`](modes/normal.md) | Normal mode spec | [⬇ download](https://github.com/MyBoyAKS/Teach-Me-Anything/raw/main/modes/normal.md) |
| [`modes/widget.md`](modes/widget.md) | Widget mode spec | [⬇ download](https://github.com/MyBoyAKS/Teach-Me-Anything/raw/main/modes/widget.md) |
| [`modes/ultra.md`](modes/ultra.md) | Ultra mode spec | [⬇ download](https://github.com/MyBoyAKS/Teach-Me-Anything/raw/main/modes/ultra.md) |
| [`widget-engine.md`](widget-engine.md) | how to build the interactive page | [⬇ download](https://github.com/MyBoyAKS/Teach-Me-Anything/raw/main/widget-engine.md) |
| [`evidence.md`](evidence.md) | the research behind it | [⬇ download](https://github.com/MyBoyAKS/Teach-Me-Anything/raw/main/evidence.md) |

On a computer, the download link may open the file as text: press **Ctrl + S** (Mac: **Cmd + S**) to save it, or right-click the link → **Save link as…**

**Shortest version:** open [`quick-start.md`](quick-start.md), copy the text inside the grey box, paste it into your AI, and send. It will ask you the same questions as in Option A.

### If your AI can't make interactive pages
Ask for one `.html` file, save it, and open it in your browser. The working pages in [`examples/`](examples/) also open this way: download a file and double-click it.

---

## 6. The core ideas

These are the rules every lesson follows. Each one is shown in a short looping clip.

| # | Idea | See it in |
|:-:|---|:-:|
| 1 | **Real numbers first**, then letters. Every new idea starts with a concrete example. | <img src="assets/idea1-real-numbers.gif" width="210" alt="Solving 2x + 3 = 7 with real numbers"> |
| 2 | **One idea per step.** Each step has a short title and 1 to 2 sentences of *why*. | <img src="assets/idea2-one-idea.gif" width="210" alt="Chapters with one idea each"> |
| 3 | **Show every step.** Never skip arithmetic: "1a − 3a = −2a", then "3 ÷ (−2)". | <img src="assets/idea3-every-step.gif" width="210" alt="Every arithmetic step shown"> |
| 4 | **Point at it.** The term being explained gets a highlight box and an arrow. | <img src="assets/idea4-point-at-it.gif" width="210" alt="Arrow: put −3a here"> |
| 5 | **Picture and algebra move together** on one timeline. | <img src="assets/idea5-picture-algebra.gif" width="210" alt="Lines move but always cross at x = 2"> |
| 6 | **The learner does the last step.** Puzzles give hints, never the answer. | <img src="assets/idea6-puzzle.gif" width="210" alt="Puzzle: wrong pick gives a hint, right pick continues"> |
| 7 | **Write it down properly.** Every lesson ends with what to write in your notebook. | <img src="assets/idea7-notebook.gif" width="210" alt="Write it in your book chapter"> |

---

## 7. Credit

Created by **Kenzie** · GitHub [**@MyBoyAKS**](https://github.com/MyBoyAKS)

If you use or adapt this, please credit **Kenzie (@MyBoyAKS)** and link back to this repo.
