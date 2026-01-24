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

::: block | Block Title
This is a block.
:::

::: alert | Important Title
This is an alert block.
:::

::: example | Example Title
This is an example block.
:::

<!-- !!! -->

## Lists

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

A sequence $(a_n)_{n=1}^\infty$ in a metric space $(X,d)$ is a _Cauchy sequence_ if

$$
\forall \varepsilon > 0, \ \exists N \in \mathbb{N} \ \text{s.t.} \ \forall m,n \geq N, \ d(a_m, a_n) < \varepsilon.
$$

For $\mathbb{R}^n$ with Euclidean norm $|\cdot|_2$, this becomes:

$$
\forall \varepsilon > 0, \ \exists N \in \mathbb{N} \ \text{s.t.} \ \forall m,n \geq N, \ \|a_m - a_n\|_2 < \varepsilon.
$$

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
