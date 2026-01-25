---
title: "Demo Slide Template (Jan 2026)"
display_name: "Demo"
date: "2026-01-23"
template: "templates/slides-template.html"
controls: true
progress: true
center: true
hash: true
transition: "slide"
zoom: true
fragments: true
---

## Slide Template

### Esteban NOCET-BINOIS

This is a demo to showcase [badaboum](https://github.com/esteban-nb/talks).

<!-- !!! -->

## Different Blocks

::: donot | Block Title
This is a `donot` block.
:::

::: alert | Block Title
This is a `alert` block.
:::

::: zoom | Block Title
This is a `zoom` block.
:::

<!-- ||| -->

## Different Blocks

::: info | Block Title
This is a `info` block.
:::

::: example | Block Title
This is a `example` block.
:::

::: note | Block Title
This is a `note` block.
:::

<!-- !!! -->

## Easy Lists

- First item
  - A subitem
    - A subsubitem
- Second item
- Third item

And ordered lists:

1. First item
   1. Subitem
   2. Subitem
1. First item?
1. Third item

<!-- !!! -->

## Math Rendering

**Definition.**

A sequence $(a_n)_{n=1}^\infty$ in a metric space $(X,d)$ is a _Cauchy sequence_ if

$$
\forall \varepsilon > 0, \ \exists N \in \mathbb{N} \ \text{s.t.} \ \forall m,n \geq N, \ d(a_m, a_n) < \varepsilon.
$$

A metric space $(X,d)$ is $complete$ if and only if every Cauchy sequence in $X$ converges in $X$.

**Property.**

Every Cauchy sequence is bounded:

$$
\text{Cauchy} \implies \exists M>0, \ \forall n, \ d(a_n, a_1) \le M
$$

**Exercise.**

Show that $a_n = (-1)^n$ is bounded yet not Cauchy.

**Theorem.**

The Banach fixed-point theorem relies on constructing a Cauchy sequence of iterates that converges to a unique fixed point.

Note:
This will only appear in the speaker view!
In particular, any metric space can be completed by adding the limits of all its Cauchy sequences.
For example, real numbers are constructed by defining them as equivalence classes of Cauchy sequences of rational numbers (Cauchy reals), filling the gaps in $\mathbb{Q}$.

[comment]: # "!!!"

## Code Blocks

```python
def newton_update(f, J; x0, tol=1e-10, max_iter=50):
    """Perform Newton update for solving f(x) = 0 where f: R^n -> R^n."""
    x = x0.copy()
    for i in range(max_iter):
        fx = f(x)
        res_norm = np.linalg.norm(fx)
        if res_norm < tol:
            return x, True

        Jx = J(x)
        try:
            delta = solve(Jx, -fx)  # Solve J δ = -f(x)
            x += delta
        except np.linalg.LinAlgError:
            return x, False

    return x, False
```

[comment]: # "!!!"

## Images from URL

![FP on sphere (from link)](https://raw.githubusercontent.com/esteban-nb/talks/main/media/images/fokker-planck-wuerzburg.jpg)

<figcaption>Visible Caption Text</figcaption>

Display media including images, videos and animations.

::: info | ^@
Do not use the blob https://github.com/esteban-nb/talks/blob/main/media/images/fokker-planck-wuerzburg.jpg to insert the image.
Either use `https://raw.githubusercontent.com/` or append `?raw=true` at the end.
:::

[comment]: # "|||"

## Images from URL

<figure>
  <img src="https://github.com/esteban-nb/talks/blob/main/media/images/fokker-planck-wuerzburg.jpg?raw=true" alt="FP on sphere (from link)">
  <figcaption>Visible Caption Text</figcaption>
</figure>

We can also use HTML with a standard `<img>` tag.

[comment]: # "|||"

## Images from Path

![FP on sphere (from path)](../media/images/fokker-plank-wuerzburg.jpg) <!-- .element: style="height:50vh; max-width:80vw; image-rendering: crisp-edges;" -->

[comment]: <> (!!! raw:)

<h2>Two Columns Slides</h2>

<div class="two-cols">
  <div data-markdown>
    <script type="text/template">
      ### Left Column
      - Item 1
      - Item 2
      - Item 3
    </script>
  </div>
  <div data-markdown>
    <script type="text/template">
      ### Right Column  
      - Item A
      - Item B
      - Item C
    </script>
  </div>
</div>

<div class="two-cols" style="--col1-width: 30%; --col2-width: 70%; --cols-gap:5em">
  <div data-markdown>
    ### Left Column @30%
    - Item 1
    - Item 2
    - Item 3
  </div>
  <div data-markdown>
    ### Right Column @70%
    - Item A
    - Item B
    - Item C
  </div>
</div>

[//]: # "!!!"

## Background Images...

<!-- !!! -->

## ... and Background Videos

<!-- !!! raw: data-background-iframe="https://www.youtube.com/embed/h1_nyI3z8gI" data-background-interactive -->

<h2 style="color: #fff;">Iframe Background</h2>

<!-- !!! -->

## Wolfram Powered Code

<!-- !!! -->

## Blackboard

<!-- !!! -->

## Citation Footer

<!-- !!! -->

## Keyboard Bindings

- **O**: Overview mode (or `Esc`)
- **P**: Previous slide navigation
- **S**: Speaker view window
- **F**: Full screen mode (if not already full screan via browser shortcut, e.g., `Fn+11`)
- **G**: Jump to slide prompt (indicate slide number, use slash `/` to specify vertical slides)
- **H**: Left slide navigation (Vim-style)
- **L**: Right slide navigation (Vim-style)
- **B**: Pause/resume presentation (or period `.`)
- **M**: Navigation menu (if the `reveal.js-menu` plugin is installed)
- **N**: Next slide navigation
- **?**: Help overlay with all available shortcuts (or `Fn+1`)
- **Ctrl + Click**: Zoom into a specific element
- **Space**: Next slide or fragment
- **Shift + Arrows**: Jump to the first or last slide in that direction
- **Alt + Arrows**: Skip all fragments on a slide and jump directly to the next/previous slide

<!-- ||| -->

## Keyboard Bindings

To add a shortcut that isn't included by default, use the keyboard config option in initialization:

```javascript
Reveal.initialize({
  keyboard: {
    13: "next", // Enter key goes to next slide
    67: () => {
      console.log("Custom action for C key");
    }, // Custom function
  },
});
```
