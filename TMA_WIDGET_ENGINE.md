# TMA Widget engine: how to build the "video" page

*Part of TMA (Teach Me Anything). Read this only when building a Widget or Ultra page described in `TMA_SKILLS.md`.*

A recipe any AI (or person) can follow to build the Widget player. Working examples: `examples/widget-demo-basic.html` (on GitHub) and `examples/widget-demo-pointers.html` (on GitHub).

---

## 1. Data: chapters → frames → tokens

```js
const t  = (id, tex, cls) => ({id, tex, c: cls || ''});        // one token
const fr = (id, top, bot) => ({frac: true, id, top, bot});      // a fraction made of tokens
const BR = {br: true};                                         // line break

const CH = [
  { name: 'Substitute', frames: [
    { row: [t('A','a'), t('P','+'), t('B','b'), t('e1','='), t('T3','3'), BR,
            t('B2','b'), t('e2','='), t('m3','-3a')],
      say:  'Equation (2) says b is the same thing as −3a.',     // main sentence
      note: 'So wherever we see b in (1), we can put −3a.',      // note box
      hold: 7,                                                  // seconds to read
      g:    { a: -1 },                                          // graph state
      pt:   [ { from: 'm3', to: 'B', label: 'put −3a here' } ]  // pointers
    },
    { row: [t('A','a'), t('P','+'), t('B','(-3a)'), t('e1','='), t('T3','3')],
      say: 'b is replaced by (−3a).', note: '…', hold: 6,
      pt: [ { ids: ['B'], label: 'was b', side: 'top' } ] }
  ]}
];
```

**Token ids are the magic.** The same id in two frames = the same object, so it slides. Same id but different `tex` = it cross-fades. An id that vanishes = struck out. A new id = fades in.

## 2. Timeline

```js
const TR = 2.0;                       // transition seconds
let total = 0;
F.forEach((f, k) => { f.tr = k ? TR : 0; f.start = total; f.dur = f.tr + f.hold; total += f.dur; });
```

`render(T)` finds the frame k whose start ≤ T, then `p = (T − start) / tr` (0 → 1 during the transition).

## 3. Layout by measuring (FLIP idea)

1. For every frame, build a hidden layer with the tokens laid out normally (flexbox, fractions as a column with a bar token).
2. Measure each token's `offsetLeft / offsetTop / offsetWidth / offsetHeight`.
3. Draw visible copies absolutely positioned. During a transition, interpolate between the two measured boxes with an ease (e.g. ease-in-out quad).

Strike-outs: a red bar inside the token that scales from 0 to full width during the first ~45% of the transition, then the token fades.

## 4. Text inside the video

`say` and `note` are layered divs that cross-fade: old text fades out in the first half of the transition, new text fades in during the second half. Typeset maths in them once at build time.

## 5. Pointers

Draw in an SVG overlay that covers the maths area, using the **final** measured boxes of the current frame:

- `{ids:[…], label, side:'top'|'bottom', c}` → rounded rect around the union of those tokens + a curved arrow from a label above/below.
- `{from, to, label}` → filled box on `from`, dashed box on `to`, curved arrow routed around the side.

Opacity: old frame's pointers fade out in the first 30% of the transition; new ones fade in during the last 30%.

## 6. Graph

`drawG(g, u)` redraws an SVG from the frame's `g` object, where `u` is 0 → 1 across the frame. Use `u` to animate (a dot sweeping, a line sliding, a zoom). Put a small readout box inside the graph, placed where it doesn't cover the important point.

## 7. Player

- `<input type="range">` from 0 to total; on input → `render(value)`.
- Play loop with `requestAnimationFrame`, multiplying the time step by the speed.
- Chapter ticks at `chapter.start / total`; chapter buttons jump to `start + TR`.
- Re-measure on resize.

## 8. Checklist before sharing

- [ ] Test at phone width (≈ 390 px) in dark mode.
- [ ] Every frame: nothing overlaps, readout doesn't hide the key point.
- [ ] Arithmetic double-checked; answer plugged back in.
- [ ] Last chapter shows what to write in the notebook.
