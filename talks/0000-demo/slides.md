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

## Internal slide Links

- Use hash:
  <a href="#/6/3" target="_self">Go to slide</a>
- Use labels:

<!-- !!! -->

## Slide Delimiters

### Horizontal Slides

- &lt;&excl;&ndash;&ndash; &excl;&excl;&excl; &ndash;&ndash;&gt;
- &lbrack;comment&rbrack;&colon; &num; &quot;&excl;&excl;&excl;&quot;
- &lbrack;comment&rbrack;&colon; &num; &lpar;&excl;&excl;&excl;&rpar;
- &lbrack;comment&rbrack;&colon; &lt;&gt; &lpar;&excl;&excl;&excl;&rpar;
- &lbrack;&sol;&sol;&rbrack;&colon; &num; &quot;&excl;&excl;&excl;&quot;
- &lbrack;&sol;&sol;&rbrack;&colon; &num; &lpar;&excl;&excl;&excl;&rpar;

### Vertical Slides

- &lt;&excl;&ndash;&ndash; &vert;&vert;&vert; &ndash;&ndash;&gt;
- &lbrack;comment&rbrack;&colon; &num; &quot;&vert;&vert;&vert;&quot;
- &lbrack;comment&rbrack;&colon; &num; &lpar;&vert;&vert;&vert;&rpar;
- &lbrack;comment&rbrack;&colon; &lt;&gt; &lpar;&vert;&vert;&vert;&rpar;
- &lbrack;&sol;&sol;&rbrack;&colon; &num; &quot;&vert;&vert;&vert;&quot;
- &lbrack;&sol;&sol;&rbrack;&colon; &num; &lpar;&vert;&vert;&vert;&rpar;

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

<!-- ||| -->

## Math Blocks

TODO

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

[comment]: # "|||"

## Code Blocks

### Sequential Display

```python [1-2|11,13-14|6-9|12,15-16|17]
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

### How this works:

- **Step 1 (`1-2`):** Defines the inputs ($f$, the Jacobian $J$, and initial guess $x_0$).
- **Step 2 (`10,12-13`):** Jumps straight to the main part of the algorithm, highlighting lines 11, 13, and 14.
- **Step 3 (`5-8`):** Explains the convergence check ($|f(x)| < \text{tol}$) after the student understands how $x$ is updated.
- **Step 4 (`11,14-15`):** Introduces real-world robustness (the `try/except` block) only after the ideal case is understood.
- **Step 5 (`17`):** Returns.

[comment]: # "!!!"

## Code Blocks

### Sequential Display

```js [1-2|3|4]
let a = 1;
let b = 2;
let c = (x) => 1 + 2 + x;
c(3);
```

[comment]: # "!!!"

## Image from URL

![FP on sphere (from link)](https://raw.githubusercontent.com/esteban-nb/talks/main/media/images/fokker-planck-wuerzburg.jpg) <!-- .element: style="width: 70%;" -->

<figcaption>Visible Caption Text</figcaption>

Display media including images, videos and animations.

::: info | ^@
Do not use the blob https://github.com/esteban-nb/talks/blob/main/media/images/fokker-planck-wuerzburg.jpg to insert the image.
Either use `https://raw.githubusercontent.com/` or append `?raw=true` at the end.
:::

[comment]: # "|||"

## Image from URL

<figure>
  <img src="https://github.com/esteban-nb/talks/blob/main/media/images/fokker-planck-wuerzburg.jpg?raw=true" alt="FP on sphere (from link)">
  <figcaption>Visible Caption Text</figcaption>
</figure>

We can also use HTML with a standard `<img>` tag.

[comment]: # "|||"

## Image from Path

![FP on sphere (from path)](@media/images/fokker-planck-wuerzburg.jpg) <!-- .element: style="width: 70%; max-height: 400px; image-rendering: crisp-edges;" -->

Use &commat;media to refer to the shared folder.

[comment]: # "||| raw:"

<section>
  <h2>Clickable Image</h2>
  <a href="https://link.springer.com/book/10.1007/978-1-4939-3028-9" target="_blank" rel="noopener noreferrer">
    <img src="https://media.springernature.com/full/springer-static/cover-hires/book/978-1-4939-3028-9?as=webp" alt="Linear Canonical Transforms Book Cover" style="max-width: 25%; height: auto;">
  </a>
  <p>Click the image above to visit <a href="https://doi.org/10.1007/978-1-4939-3028-9" target="_blank">Healy et al. (2016)</a>.</p>
</section>

[comment]: <> (!!! raw:)

<h2>Grid Layout</h2>

<!-- Root Grid: One column by default (acts as a vertical stack) -->
<div class="grid" style="--gap-rows: 2em;">

  <!-- "Row 1": 30/70 split -->
  <div class="grid" style="--cols: 0.3fr 0.7fr;">
    <div data-markdown>
      Left Content
      - Item 1
      - Item 2
      - Item 3
    </div>
    <div data-markdown>
      Right Content
      - Item 1
      - Item 2
      - Item 3
    </div>
  </div>

  <!-- "Row 2": three equal columns -->
  <div class="grid" style="--cols: 1fr 1fr 1fr;">
    <div data-markdown>
      Box A
      - Item A
      - Item B
      - Item C
    </div>
    <div data-markdown>
      Box B
      - Item A
      - Item B
      - Item C
    </div>
    <div data-markdown>
      Box C
      - Item A
      - Item B
      - Item C
    </div>
  </div>
</div>

[//]: # "|||"

## Color Themes

[//]: # "!!!"

## Fragments

### Single Line Fragments

- Line one <!-- .element: class="fragment" data-fragment-index="1" -->
- Line two <!-- .element: class="fragment" data-fragment-index="2" -->
- Line three <!-- .element: class="fragment" data-fragment-index="3" -->

[//]: # "!!!"

## Fragments

### Single Line Fragments

- Line one
- Line two <!-- .element: class="fragment" data-fragment-index="2" -->
- Line three

[//]: # "|||"

## Fragments

### Inline Fragments

This is a
<span class="fragment" data-fragment-index="1">fragment</span>
inside a sentence.

This turns <span class="fragment highlight" data-fragment-index="2" style="--highlight-color: green;">green</span>,
and this defaults to <span class="fragment highlight" data-fragment-index="3">red</span>.

[//]: # "|||"

## Fragments

### Division-level Fragments

<div class="fragment" data-fragment-index="1">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>

<div class="fragment" data-markdown data-fragment-index="2">
  <script type="text/template">
    ### Group Title
    - Line one
    - Line two
    - Line three
  </script>
</div>

[//]: # "|||"

## Stacks

<div class="r-stack">
  ![Figure A](https://media.springernature.com/full/springer-static/cover-hires/book/978-3-031-80165-5?as=webp) <!-- .element: class="fragment fade-out" data-fragment-index="1" -->
  ![Figure B](https://media.springernature.com/full/springer-static/cover-hires/book/978-0-387-22757-3?as=webp) <!-- .element: class="fragment" data-fragment-index="1" -->
  ![Figure C](https://media.springernature.com/full/springer-static/cover-hires/book/978-3-031-68566-8?as=webp) <!-- .element: class="fragment" data-fragment-index="3" -->
</div>

<!-- !!! data-background-color="#ff0000" -->

## Bacground Color... <!-- .element: style="color: white;" -->

<!-- !!! data-background-image="@media/images/fokker-planck-wuerzburg.jpg" -->

## ...Background Image... <!-- .element: style="color: black;" -->

<!-- !!! data-background-video="@media/videos/moving-dots.mp4" data-background-video-loop -->

## ...and Background Video <!-- .element: style="color: black;" -->

<!-- !!! data-background-iframe="https://www.youtube.com/embed/h1_nyI3z8gI?rel=0&modestbranding=1" data-background-interactive -->

<!-- .slide: style="color: white;" -->

## Iframe Background

- `rel=0`: Limits suggestions to your own channel.
- `modestbranding=1`: Removes the YouTube logo from the control bar.
- `controls=0`: Hides playback controls to reduce UI noise.
- `iv_load_policy=3`: Hides video annotations.

For complete control, use `enablejsapi=1` to use the YouTube IFrame Player API to detect when a video ends and hide the iframe.
See more on the [media](https://revealjs.com/media/) and [backgrounds](https://revealjs.com/backgrounds/) documentation.

<!-- !!! data-background-iframe="https://peertube.tv/videos/embed/d2bf34fc-6cee-455e-86dc-b7e8979fd1a2" data-background-interactive -->

Explore different hosting platforms and frontend options (e.g., PeerTube, AVideo, Odysee, Invidious, Piped, etc.)

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

<table>
  <thead>
    <tr>
      <th>KEY</th>
      <th>ACTION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>N, SPACE</td>
      <td>Next slide</td>
    </tr>
    <tr>
      <td>P, Shift SPACE</td>
      <td>Previous slide</td>
    </tr>
    <tr>
      <td>←, H</td>
      <td>Navigate left</td>
    </tr>
    <tr>
      <td>→, L</td>
      <td>Navigate right</td>
    </tr>
    <tr>
      <td>↑, K</td>
      <td>Navigate up</td>
    </tr>
    <tr>
      <td>↓, J</td>
      <td>Navigate down</td>
    </tr>
    <tr>
      <td>Alt + ←/↑/→/↓</td>
      <td>Navigate without fragments</td>
    </tr>
    <tr>
      <td>Shift + ←/↑/→/↓</td>
      <td>Jump to first/last slide</td>
    </tr>
    <tr>
      <td>B, .</td>
      <td>Pause</td>
    </tr>
    <tr>
      <td>F</td>
      <td>Fullscreen</td>
    </tr>
    <tr>
      <td>G</td>
      <td>Jump to slide</td>
    </tr>
    <tr>
      <td>ESC, O</td>
      <td>Slide overview</td>
    </tr>
    <tr>
      <td>S</td>
      <td>Speaker notes view</td>
    </tr>
  </tbody>
</table>

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
