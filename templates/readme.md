Top-left layout with two footers (one with info, the other for citation/copyright).

Different blocks (from darkest to lightest mono):

- Don't (red)
- Alert (yellow)
- Zoom (purple)
- Info (blue)
- Example (green)
- Note (slate)

Maths:

- Theorem (THM, red)
- Proposition (PRP, yellow)
- Lemmas (LEM, purple)
- Corollaries (COR, blue)
- Definition (DEF, green)
- Exercise (slate)

Code highlight per mode:

- Light: `monokai-sublime`
- Mono: `github`
- Dark: `ir-black`

Two-column display (see layouyt [here](https://rstudio-conf-2022.github.io/get-started-quarto/materials/07-plots-tables.html#/plots-graphics-and-tables)). For example, to create a 2x3 grid:

```md
## Slide

::: {layout="[[1, 1], [1, 1, 1]]"}

<!-- @ -->

Content

<!-- @ -->

Content

<!-- @ -->
```
