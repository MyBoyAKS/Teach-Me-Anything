# Widget mode

**What it is:** one interactive web page that works like a short YouTube video. The learner can drag a timeline to any moment, pause, change speed and jump between chapters. Words, moving algebra, arrows and a graph all live on one "screen" and follow the same slider.

Goal: **watch and understand.**

---

## 1. The player

- A red timeline slider the learner can drag to any exact moment.
- Play / Pause, a speed button (0.5×, 0.75×, 1×, 1.5×), a time display.
- Chapter tick marks on the timeline and a chapter list to jump to.
- Buttons never move or resize.
- Everything on screen is a pure function of the slider time, so scrubbing backwards and forwards is smooth.

## 2. The screen (everything inside the video, no separate subtitle box)

Top to bottom:
1. **Chapter chip** (small label, e.g. "Step 2: f′ = 0").
2. **Main sentence** above the maths: what is happening and why.
3. **The moving maths** (equations, matrices, code, chemical equations…).
4. **Note box** below the maths: the small detail, the check, the trap.
5. **The graph or picture**, with a live number readout inside it.

Text fades in and out with the slider, just like the maths.

## 3. The moving maths ("equation morph" / matching transform)

Every term is a separate token with a name. Between two steps:
- a token that exists in both steps **slides** to its new place,
- a token that changes value **cross-fades** (e.g. 7 morphs into 4),
- a token that disappears gets **struck out in red**, then fades,
- a new token **fades/grows in**,
- the final answer is highlighted green.

## 4. Pointers (highlight + arrow)

Whenever a step talks about a specific term:
- a rounded **highlight box** goes around it,
- an **arrow** points at it with a short label: "put −3a here", "3 ÷ (−2)", "(−) × (−) = +", "from the point (1, 3)",
- for substitutions, a **curved arrow** goes from the source term to the spot it replaces,
- colours mean something: orange = what we're doing now, blue = the other piece, green = answer/check.

Pointers fade in **after** the terms finish moving, so the eye goes to the right place at the right moment.

## 5. The synced graph or picture

- Shows the same idea as the algebra, at the same moment.
- Can animate (a dot sliding along a curve, lines moving, a shape stretching) over the step's duration.
- Can switch picture mid-video if a different view explains better.
- Has a small readout with live numbers (x, slope, height, area…).
- Real drawings only (SVG/canvas). Never ASCII art.

## 6. Timing (slow is good)

- Moves about 1.4 to 2 s, strike-outs about 0.9 s.
- About 5 s to read each step (longer for important ones).
- Smooth, morph-like transitions; never slide whole pages.

## 7. Content rules

- Start from **real numbers** (or the learner's real homework problem).
- One idea per step, every arithmetic step shown.
- Call out the learner's own past mistakes in the note box.
- **Last chapter: "Write it in your book"**: the exact lines to copy.
- 1 to 4 minutes total, 4 to 8 chapters.

## 8. Technical requirements

- One self-contained HTML page (inline CSS/JS).
- Real typeset maths (e.g. MathJax 3) when the subject has formulas.
- Works on a phone and in dark mode; test at phone width (about 390 px).
- See [`../widget-engine.md`](../widget-engine.md) for how to build it, and [`../examples/`](../examples/) for working pages.

## Non-maths subjects

The same player works for anything with steps:
- **Programming:** code lines are tokens; a variable's value morphs; arrows point at the line running now; the "graph" panel shows memory/variables or output.
- **Chemistry:** balancing equations; coefficients morph; arrows point at the atom being counted; the picture shows molecules.
- **Physics:** formula rearranging + a diagram (forces, a moving object) on the same timeline.
- **Languages:** a sentence where words move into the new word order; arrows label the grammar rule.
