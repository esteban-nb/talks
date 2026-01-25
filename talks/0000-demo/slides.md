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
code_theme: "ir-black"
---

## Slide Template

### Esteban NOCET-BINOIS

This is a demo to showcase [badaboum](https://github.com/esteban-nb/talks).

<!-- !!! -->

## Different Blocks

::: example | Block Title
This is a `example` block.
:::

::: info | Block Title
This is a `info` block.
:::

::: zoom | Block Title
This is a `zoom` block.
:::

<!-- ||| -->

## Different Blocks

::: note | Block Title
This is a `note` block.
:::

::: alert | Block Title
This is a `alert` block.
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
In particular, any metric space can be completed by adding the limits of all its Cauchy sequences.
For example, real numbers are constructed by defining them as equivalence classes of Cauchy sequences of rational numbers (Cauchy reals), filling the gaps in $\mathbb{Q}$.

**Property.**

Every Cauchy sequence is bounded:

$$
\text{Cauchy} \implies \exists M>0, \ \forall n, \ d(a_n, a_1) \le M
$$

**Exercise.**

Show that $a_n = (-1)^n$ is bounded yet not Cauchy.

**Theorem.**

The Banach fixed-point theorem relies on constructing a Cauchy sequence of iterates that converges to a unique fixed point.

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

## Images

![FP on sphere](media/images/fokker-plank-wuerzburg.jpg) <!-- .element: style="height:50vh; max-width:80vw; image-rendering: crisp-edges;" -->

Display media including images, videos and animations.

[comment]: <> (!!!)

## Two Columns Slides

[//]: # "!!!"

## Background Images...

<!-- !!! -->

## ... and Background Videos

<!-- !!! -->

## Wolfram Powered Code

<!-- !!! -->

## Blackboard

<!-- !!! -->

## Citation Footer

<!-- !!! -->

## Keyboard Bindings
