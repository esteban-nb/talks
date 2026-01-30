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
---

## Slide Template

### Esteban NOCET-BINOIS

This is a demo to showcase [badaboum](https://github.com/esteban-nb/talks).

<!-- !!! -->

## Basic Use

This is fully markdown.

<!-- ||| raw: -->

<h2>Basic Use</h2>

<p>This is regular HTML.</p>

<!-- ||| raw: -->

<h2>Basic Use</h2>

<p>This is regular HTML.</p>

<div data-markdown>
  <textarea data-template>
    This is now markdown.
    ### Markdown Subheader
    - [Link to Google](https://google.com)
    - ![Lenna](https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png) <!-- .element: style="height: auto;" -->
  </textarea>
</div>

<!-- ||| raw: -->

<h2>Basic Use</h2>

<p>This is regular HTML.</p>

<div data-markdown class="seamless-block">
  <textarea data-template>
    This is now markdown in a `seamless-block`.
    ### Markdown Subheader
    - [Link to Google](https://google.com)
    - ![Lenna](https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png) <!-- .element: style="height: auto;" -->
  </textarea>
</div>

<!-- ||| raw: -->

<h2>Basic Use</h2>

<p>This is regular HTML.</p>

<md>
    This is now `<md>` (using the seamless-block class).
    ### Markdown Subheader
    - [Link to Google](https://google.com)
    - ![Lenna](https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png)
</md>

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

## Internal Slide Links

- Use hash:
  [Go to slide](#/6/1)
- Use labels:
  [Go to slide](#/math-rendering)
- Or using HTML's `<a>` tag:
  <a href="#/math-rendering">Jump to the slide</a>

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

<!-- !!! id="math-rendering" -->

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

[comment]: # "||| raw: data-markdown"

<textarea data-template>

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

</textarea>

[comment]: # "::: raw: data-markdown"

<textarea data-template>

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

</textarea>

[comment]: # "!!!"

## Code Blocks

Use `data-noescape` to put HTML tags inside the code block.

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

<!-- !!! -->

## HTML Figure

We can use HTML figures as well (including dynamic ones).

<figure>
  <object data="@media/html/bifurcation_static.html" width="700" height="400"></object>
  <figcaption>Static Bifurcation Map</figcaption>
</figure>

We use `<img>` strictly for images (JPG, PNG, GIF, SVG). To render HTML markup or scripts; use `<iframe>` or `<object>` instead.

<!-- ||| -->

For PDF use `<embed>`, `<object>`, or `<iframe>` (e.g., `<object data="file.pdf">`); amd while SVG are fully supported by `<img>`, `<object>` or `<iframe>` allows interactive/scripted SVGs.

<figure>
  <object data="@media/logos/princeton-logo-shield-bw.pdf" type="application/pdf" width="700" height="400">
    <a href="https://raw.githubusercontent.com/esteban-nb/talks/main/media/logos/princeton-logo-shield-bw.pdf">View PDF</a>
  </object>
  <figcaption>Princeton Logo (PDF)</figcaption>
</figure>

To avoids the viewer UI, convert PDF to PNG/JPG/SVG then use `<img src="logo.png" alt="Princeton Logo">` inside `<figure>`.
Retains vector quality if SVG output.

<!-- ||| -->

For example:

![FP on sphere (from path)](@media/logos/princeton-logo-shield-bw.svg) <!-- .element: style="width: 20%;" -->

<figcaption>Princeton Logo (SVG)</figcaption>

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

[//]: # "||||"

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

[//]: # "||| raw:"

<h2>Fragments</h2>

<h3>Division-level Fragments</h3>

<div class="fragment" data-fragment-index="1">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>

<div class="fragment" data-markdown data-fragment-index="2">
  <script type="data-template">
    ### Group Title
    - Line one
    - Line two
    - Line three
  </script>
</div>

[//]: # "!!!"

## Stacks

### Image Stack

<div class="r-stack">
  <img
    class="fragment fade-out"
    data-fragment-index="0"
    src="https://picsum.photos/450/300"
    width="450"
    height="300"
  />
  <img
    class="fragment current-visible"
    data-fragment-index="0"
    src="https://picsum.photos/300/450"
    width="300"
    height="450"
  />
  <img
    class="fragment"
    src="https://picsum.photos/400/400"
    width="400"
    height="400"
  />
</div>

Use sequences of `fade-out` (to start visible), paired with new fragment using `current-visible`.
Use a plain fragment (without extra classes like `current-visible` or `fade-out`) for the sequence endpoint so it appears on its `data-fragment-index` step and stays visible indefinitely as the top stack layer. 

[//]: # "|||"

## Stacks

### Mixed Stack

<div class="r-stack">
  <!-- Frame 0 outgoing: Image + text -->
  <div class="fragment fade-out" data-fragment-index="0" style="position:absolute; width:100%; height:100%;">
    <img src="https://picsum.photos/450/300" width="450" height="300" style="position:absolute;" />
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
  </div>
  
  <!-- Frame 0 incoming: Table -->
  <div class="fragment current-visible" data-fragment-index="0" style="position:absolute; width:100%; height:100%;">
    <table style="position:absolute; top:50px;">
      <tr><td>Row1 Col1</td><td>Row1 Col2</td></tr>
      <tr><td>Row2 Col1</td><td>Row2 Col2</td></tr>
    </table>
  </div>
  
  <!-- Frame 1: Final image -->
  <div class="fragment" data-fragment-index="1">
    <img src="https://picsum.photos/400/400" width="450" height="300" />
  </div>
</div>


[//]: # "|||"

## Stacks

### Image Stack

Using only fragment:

<div class="r-stack">
  <!-- First fragment -->
  <img class="fragment" data-fragment-index="1" 
       src="https://media.springernature.com/full/springer-static/cover-hires/book/978-3-031-80165-5?as=webp" 
       style="width: 40%;">
  <!-- Second fragment -->
  <img class="fragment" data-fragment-index="2" 
       src="https://media.springernature.com/full/springer-static/cover-hires/book/978-0-387-22757-3?as=webp" 
       style="width: 40%;">
  <!-- Third fragment -->
  <img class="fragment" data-fragment-index="3" 
       src="https://media.springernature.com/full/springer-static/cover-hires/book/978-3-031-68566-8?as=webp" 
       style="width: 40%;">
</div>

[//]: # "|||"

## Stacks

### With Links

<div class="r-stack">
  <!-- First fragment -->
  <a href="https://link.springer.com/book/10.1007/978-3-031-80165-5" 
     class="fragment" data-fragment-index="1">
    <img src="https://media.springernature.com/full/springer-static/cover-hires/book/978-3-031-80165-5?as=webp" 
         style="width: 40%;">
  </a>
  <!-- Second fragment -->
  <a href="https://link.springer.com/book/10.1007/978-0-387-22757-3" 
       class="fragment" data-fragment-index="2">
    <img src="https://media.springernature.com/full/springer-static/cover-hires/book/978-0-387-22757-3?as=webp" 
         style="width: 40%;">
  </a>
  <!-- Third fragment -->
  <a href="https://link.springer.com/book/10.1007/978-3-031-68566-8" 
       class="fragment" data-fragment-index="3">
    <img src="https://media.springernature.com/full/springer-static/cover-hires/book/978-3-031-68566-8?as=webp" 
         style="width: 40%;">
  </a>
</div>

[//]: # "||| raw:"

<md>
## Stacks
    
### With Image & Text

New try with md-div twice.
</md>

<div class="r-stack">
  <!-- First fragment -->
  <a href="https://link.springer.com/book/10.1007/978-3-031-80165-5" 
     class="fragment" data-fragment-index="1">
    <img src="https://media.springernature.com/full/springer-static/cover-hires/book/978-3-031-80165-5?as=webp" 
         style="width: 40%;">
  </a>
  <!-- Second fragment -->
  <div class="fragment" data-fragment-index="2">
    <a href="https://link.springer.com/book/10.1007/978-0-387-22757-3">
        <img src="https://media.springernature.com/full/springer-static/cover-hires/book/978-0-387-22757-3?as=webp"
             style="width: 40%;">
    </a>
    <md>
      Including a chapter on [Transformations of Functions and Signals](https://link.springer.com/chapter/10.1007/978-3-031-68566-8_5)!
    </md>
  </div>
  <!-- Third fragment -->
  <a href="https://link.springer.com/book/10.1007/978-3-031-68566-8" 
       class="fragment" data-fragment-index="3">
  <img src="https://media.springernature.com/full/springer-static/cover-hires/book/978-3-031-68566-8?as=webp" 
           style="width: 40%;">
  </a>
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
