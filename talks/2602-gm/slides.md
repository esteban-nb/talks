---
title: "Group Meeting Presentation (Feb 2026)"
display_name: "Group Meeting"
date: "2026-02-5"
template: "templates/slides-template.html"
transition: "slide"
---

<!-- conference-style presentation (15 minutes) -->

<center>

<h1>7-Story Building</h1>
<h3>Finite Strain Theory on Wasserstein Space</h3>

<div style="height:100px"></div>

<b>Est&eacute;ban Nocet&ndash;Binois</b>

<br><br>

<i>Feb 5, 2026</i>

</center>

<!-- !!! -->

## [Moaveni et al.](http://dx.doi.org/10.1016/j.strusafe.2010.03.006)'s paper

<br>

![frontcover](@media/images/moaveni-et-al.png) <!-- .element: style="width: 100%; max-height: 400px; image-rendering: crisp-edges;" -->

<!-- !!! -->

## The physical system

### Ideal dynamics

![fig from article](@media/images/kinematic-overstrength.jpg) <!-- .element: style="width: 30%; max-height: 400px; image-rendering: crisp-edges;" -->

Let $\Omega \subset \mathbb{R}^3$ denote the building domain.
The undamaged (material) building admits a continuum description via a displacement field

$$
u(x,t) : \Omega \times \mathbb{R}_+ \to \mathbb{R}^3
$$

In the **linear elastic, conservative limit**, the the system is described by the following (homogeneous) [hyperbolic PDE](https://en.wikipedia.org/wiki/Linear_elasticity#Direct_tensor_form):

$$
\rho\ \ddot{\mathbf{u}} - \nabla \cdot \boldsymbol{\sigma}(u) = \mathbf{0}, \qquad \boldsymbol{\sigma} = \mathsf{C}\ \colon \boldsymbol{\varepsilon}
$$

Note:
The presence of $\ddot{\mathbf{u}} = \partial^2 \mathbf{u}/\partial t^2$ makes the system hyperbolic, as opposed to parabolic (first-order in time, like the heat equation) or elliptic (no time dependence, like Laplace’s equation).

<!-- ||| -->

## The physical system

### Ideal dynamics

Let $\Omega \subset \mathbb{R}^3$ denote the building domain.
The undamaged (material) building admits a continuum description via a displacement field

$$
u(x,t) : \Omega \times \mathbb{R}_+ \to \mathbb{R}^3
$$

In the **linear elastic, conservative limit**, the the system is described by the following (homogeneous) [hyperbolic PDE](https://en.wikipedia.org/wiki/Linear_elasticity#Direct_tensor_form):

$$
\rho\ \ddot{\mathbf{u}} - \nabla \cdot \boldsymbol{\sigma}(u) = \mathbf{0}, \qquad \boldsymbol{\sigma} = \mathsf{C}\ \colon \boldsymbol{\varepsilon}
$$

with suitable boundary conditions, and where:

- $\mathbf{u}(\mathbf{x}, t)$ is the displacement vector field,
- $\rho$ is the mass density,
- $\ddot{\mathbf{u}} = \frac{\partial^2 \mathbf{u}}{\partial t^2}$ is the acceleration,
- $\boldsymbol{\sigma}$ is the Cauchy stress tensor,
  - $\mathsf{C}$ is the fourth-order elasticity (stiffness) tensor,
  - $\boldsymbol{\varepsilon} = \frac{1}{2}(\nabla \mathbf{u} + (\nabla \mathbf{u})^T$ is the infinitesimal strain tensor

Note:
It describes an elastic wave without energy loss, whose speed depends only on stiffness.

The colon ($\colon\!$) denotes the double contraction (inner product) of two tensors.

Note that in the space of second-order tensors, the double contraction
defines an inner product that induces the Frobenius norm.

<!-- ||| -->

## The physical system

### Dynamics under damping and damage

Since we consider a system under damage-induced dissipation, stochastic forcing and thus time-irreversibility:

- The symplectic structure is broken.
- There is no invariant phase-space volume.
- Modal amplitudes do not evolve unitarily.
- Generators are not self-adjoint.

::: alert | ^@
The Panagiotou shake-table experiment forces us into:

- non-Hamiltonian geometry,
- non-scalar state spaces,
- transport with dissipation.
  :::

We therefore abandon pure symplectic mechanics and move toward entropic, operator-valued transport with directional structure.

<!-- ||| -->

## The physical system

### Effective dynamics

A better representation is the damped system (homogeneous)

$$
\rho \ddot{\mathbf{u}} + \mathcal{D}[\dot{\mathbf{u}}] - \nabla \cdot \boldsymbol{\sigma}(\mathbf{u}) = \mathbf{0}
$$

where:

- $\rho$: mass density (scalar)
- $\ddot{\mathbf{u}}$: acceleration (vector)
- $\mathcal{D}[\dot{\mathbf{u}}]$: damping operator
<!-- typically $\mathcal{C} = \eta_M \rho \dot{\mathbf{u}} + \eta_K \nabla \cdot (\mathbb{C} : \nabla \mathbf{u})$ for Rayleigh damping -->
- $\boldsymbol{\sigma}(\mathbf{u}) = \mathsf{C} : \nabla \mathbf{u}$: elastic stress (same second-order tensor)

Waves decay in amplitude due to $D \dot{u}$, and may travel slower because damping dissipates energy.

<!-- Phase velocity is the speed at which a single wave's phase (e.g., its crest) propagates $v_p = \omega/k$.
Group velocity is the speed at which the envelope of a wave packet (or group of waves) travels, representing the propagation of energy or information: $v_g = \mathrm{d}k / \mathrm{\omega}$.
In dispersive media (e.g., light in glass, water waves), different frequencies travel at different speeds, causing the wave packet to spread. -->

::: alert | ^@
This is the tensor form of

$$
\rho \ddot u + D \dot u + K u = 0, \quad D \succeq 0
$$

:::

<!-- !!! -->

## Experimental forcing and damage

The system is driven by:

- base excitation $f(t)$ (shake table),
- stochastic variability between runs,
- progressive damage events.

::: alert | ^@
This introduces **nonlinear, time-irreversible operators**, beaking the following structures:

- **Liouville volume preservation** (invariance of phase-space measure under Hamiltonian flow)
- **Unitarity of modal evolution** (norm-preserving time evolution in a Hilbert space)
- **self-adjointness of generators** (symmetry of the infinitesimal generator)
:::

Without volume preservation, there are no invariant measure on phase space and no reversible dynamics.
Without unitarity, modes are not orthogonal, eigenvalues are complex.


<!-- ||| -->

## Why symplectic structure fails

### Definition

A system is Hamiltonian if it can be written as

$$
\dot z = J \nabla H(z),
$$

with:

- $z = (q,p)$,
- $J$ skew-symmetric, nondegenerate,
- flow preserving the symplectic form.

Our system **cannot admit a symplectic structure** on any state space compatible with the data.
\

1. Symplectic dynamics require **even-dimensional phase space** with canonical conjugate variables.

2. Our observations:
   - provide only scalar accelerations,
   - lack displacement $q$ and momentum $p$,
   - are orientation-projected.

::: note | ^@
We can attempt to define a phase space from ${x_i(t)}$, e.g.:

- When there is no clear phase space, one can reconstruct it from observed data using techniques like delay-coordinate embedding ([Takens' theorem](https://en.wikipedia.org/wiki/Takens%27s_theorem)). This allows to extract physically meaningful modes and conserve system structure in noise reduction and feature extraction techniques.
<!-- This reconstructed attractor can then be analyzed using symplectic tools like symplectic principal component analysis (SPCA) or symplectic geometry mode decomposition (SGMD) to extract physically meaningful modes and conserve system structure in noise reduction and feature extraction. -->
- Manifold learning techniques like [Isomap](https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction#Isomap) or [LLE](https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction#Locally-linear_embedding) can reconstruct **statistical states** from high-dimensional data, effectively creating a low-dimensional representation (manifold) that captures essential dynamics.

However, these embeddings:

- are **not canonical**,
- still would not define a closed 2-form preserved by the flow.

Arguably, no symplectic form exists that is intrinsic and invariant, while being compatible with the observations.

Importantly, these methods are meant for:

- Systems that lack clear physical variables
- Systems without explicit temporal structure
- Processing high-dimensional and noisy data
  :::

<!-- ||| -->

## Why time reversibility fails

Time reversibility requires:

$$
x(t) \mapsto x(-t)
$$

to also be a solution.

However:

1. Damping introduces terms:

   $$
   \rho \ddot u + D \dot u + K u = f(t),
   \quad D \succeq 0
   $$

   which are **odd under time reversal**.

2. Hysteresis implies:

   $$
   \sigma(t) \neq \sigma(-t)
   \quad \text{for the same strain path}.
   $$

3. Damage introduces **state-dependent operators** with memory.

Thus the evolution operator is **non-invertible in time**.

<!-- ||| -->

## Why energy conservation fails

Define nominal energy:

$$
E(t) = \tfrac12 \int_\Omega \rho |\dot u|^2 + \langle \mathbb{C} \nabla u, \nabla u \rangle.
$$

Then:

$$
\frac{dE}{dt}
= - \int_\Omega \langle D \dot u, \dot u \rangle

* \int_\Omega \text{dissipation}

- \int_{\partial\Omega} f \cdot \dot u.
$$

- $D \succeq 0$,
- crack dissipation $>0$,
- forcing stochastic.

Hence:

$$
\mathbb{E}[E(t_2)] < \mathbb{E}[E(t_1)]
\quad \text{without forcing}.
$$

Energy conservation fails structurally.

<!-- ||| -->

## Other broken structures

Additionally broken:

- **Liouville volume preservation**,
- **unitarity of modal evolution**,
- **self-adjointness of generators**.

These kill classical spectral mechanics.

<!-- !!! -->

## Covariance selection (Gaussian graphical models)

Let $X(t) = (x_1(t),\dots,x_N(t))$.

Assume local stationarity and define:

$$
\Sigma = \mathbb{E}[X X^\top].
$$

Covariance selection infers sparsity in:

$$
\Theta = \Sigma^{-1}.
$$

::: alert | ^@
Covariance selection can detect _statistical coupling_ but **cannot detect directional transport or torsion**.
:::

Indeed

- $\Sigma$ is symmetric.
- $\Theta$ is symmetric.
- Ant1isymmetric flow information is lost.

Note:
Thus:

- torsional effects,
- orientation-dependent phase transport,
- non-reciprocal coupling

are lost.

<!-- ||| -->

## Graph Laplacian models

1. Laplacians act on scalar functions.
2. They encode only **diffusive coupling**.
3. They annihilate antisymmetric components.

Therefore:

- longitudinal vs transversal mixing,
- twisting modes,
- circulation

are projected out.

::: alert | ^@
Covariance/Laplacian methods are good _statistical baselines_ but are **blind** to what we care about.
:::

<!-- !!! -->

## Geometric construction

::: alert | ^@
Thoe goal is to construct an **inference geometry on observables** that does not require unitarity or volume preservation.
:::

We model the sensor network as a **graph endowed with an orientation-dependent vector bundle** and a data-driven connection; signals are sections of this bundle, and structural damage is detected as a change in the induced transport geometry (torsion, curvature, and entropy production)

In the next slides we

  - formalize the operator-valued configuration space
  - define torsion explicitly as a non-integrability of transport on that space
  - construct a probabilistic space

<!-- ||| -->

## How axis information must be retained

To retain axis information, geometry must live on **vector- or operator-valued objects**, not scalars.

We consider $\mu \in \mathcal{M}(\Omega \times \mathbb{S}^2)$ not $\mathcal{M}(\Omega)$.

This is where:

- vector-valued OT,
- Schrödinger bridges with orientation cost,
- connection-based operators

become necessary.

Note:
A uniaxial accelerometer consists of a proof mass constrained to move along one mechanical axis.
By Newton’s law $F=m(\ddot u \cdot e_i)$, the sensor cannot respond to acceleration orthogonal to its axis.
Therefore the sensor implements a linear functional

$$
\mathbb R^3 \to \mathbb R,\; v\mapsto v\cdot e_i
$$

The inner product is the only rotationally invariant linear way to measure along an axis.

<!-- ||| -->

## What is the state variable?

Here is where torsion enters _inevitably_.

The state is **not**:

- a displacement field $u(x)$,
- a phase space point $(q,p)$,
- a vector field on the graph.

Those objects are unobservable.

Instead we need a measure or operator-valued field on the tuple $(\text{sensor index } i,\; \text{orientation } e_i,\; \omega)$

This means:

- operator-valued spectral density,
- vector-valued probability measure,
- Schrödinger bridge flow on a directed, oriented graph.

This state already **lives on a bundle-like structure**:

- base: sensor graph,
- fiber: orientation space.

<!-- ||| -->

## What are the observables

We have a finite sensor set $\{s_i\}_{i=1}^N \subset \Omega$, each with:

- a fixed orientation vector $e_i \in \mathbb{S}^2$, the unit sphere $\mathbb{S}^2 = \{v\in\mathbb R^2\ \colon \|v\|=1\}$
- a uniaxial acceleration measurement
  $$
  x_i(t) = \langle \ddot u(s_i,t),\ e_i \rangle + \eta_i(t),
  $$
  where $\eta_i$ is sensor noise.

**Observables** are therefore:

$$
\mathcal O = { x_i(t) }_{i=1}^N
$$

rahter than vector-valued observables at nodes.

From $x_i(t)$, we can construct:

1. Time–frequency distributions $\mu_i(\omega,t)$,
2. Cross-spectral densities $C_{ij}(\omega)$,
3. Transport plans between spectral measures,
4. Phase lags and coherence.

Note:
Key elements:

1. **Projection**: we never observe $\ddot u$, only its projection.
2. **Heterogeneous orientations**: $e_i \neq e_j$ in general.
3. **Sparse spatial sampling**.
4. **No displacement or velocity**, only acceleration.

This already prevents reconstruction of a canonical phase space.

What we construct from it must remain **functions of operator-valued channels** (rather than scalars indexed by orientation metadata).

<!-- ||| -->

## Orientation lives in the _fiber_, not in the data

Each sensor has a known axis:

$$
e_i \in \mathbb S^2 \subset \mathbb R^3
$$

We define at each node a **one-dimensional oriented vector space**

$$
F_i := \mathrm{span}\ \{e_i\} \subset \mathbb R^3
$$

This is crucial:

  - the signal is scalar,
  - but the _space it belongs to_ is oriented.

So we now have a **rank-1 vector bundle over a graph**:

$$
\pi:\ \bigsqcup_{i\in V} F_i \ \to\ V
$$

<!-- ||| -->

## Observables as sections of the bundle

At time $t$, define the observed section:

$$
s(t): i \mapsto y_i(t)\, e_i \in F_i
$$

This is not a scalar field on $V$, it is a **vector-valued section with spatially varying orientation**.

::: question | ^@
One question is to see how this non-scalar structure already impacts covariance models and diffusion models (can it be isotropic anymore?).
:::

<!-- !!! -->

## How coupling could be integrable

::: example | ^@
Torsion arises from **non-integrability of directional coupling**, not from sensor orientation alone.
The question is can we integrate couplings or do we deal with torsion?

<!-- here we mean geometric torsion of the observation–coupling structure -->

We can try to show that a network of single-axis sensors with heterogeneous orientation will generically exhibit torsion (even if the building is perfectly intact).
Meaning that we have a non trivial geometry.
:::

Suppose there exists a global potential $\Phi$ such that:

$$
x_i(t) \approx \partial_{e_i} \Phi(s_i,t)
$$

Then:

- transport between channels is gradient-driven,
- loops close,
- no torsion exists.

This corresponds to:

- intact structure,
- symmetric stiffness,
- reciprocal coupling.

<!-- ||| -->

## What non-integrability means here

Define a discrete connection $\nabla$ between sensor channels.

Transport around a loop $\ell$:

$$
\mathcal{P}*\ell = \prod*{(i\to j)\in \ell} T_{ij}
$$

If $\mathcal{P}_\ell \neq I$ then coupling is **non-integrable**.

This defect is torsion / curvature.

<!-- ||| -->

## What integrability would mean

Integrability would mean:

- existence of a global latent vector field $v(x,t)$,
- such that all observations are projections:
  $$
  y_i(t) = \langle v(s_i,t),\ e_i \rangle
  $$
- and all transport is gradient-driven.

This requires:

- isotropy,
- perfect reciprocity,
- no modal mixing.

This is **non-generic** in multi-story shear-wall buildings where

- different modes dominate at different floors,
- longitudinal and transverse responses mix,
- vertical excitation induces horizontal motion via geometry.

<!-- ||| -->

## Torsion as non-commutativity of directional transport

Take three sensors $i,j,k$ with different orientations.
In general:

$$
T_{ij} \circ T_{jk} \neq T_{ik}
$$

even in a perfectly elastic, undamaged building because

- projections onto different axes do not commute,
- modal content mixes orientation-dependent components,
- the observation map itself is non-integrable.

This is **purely geometric torsion of the sensing network**.

<!-- !!! -->

## Transport requires a connection

To compare signals at different nodes, we need a way to move vectors between fibers.

We define a **connection on the graph**:

$$
\nabla_{ij} : F_i \to F_j
$$

via the orientation-aware projection

$$
\nabla_{ij}(v) = \langle v, e_j \rangle e_j
= (e_i \cdot e_j)\, v_j,
\quad v \in F_i
$$

Key elements:

- $\nabla_{ij}$ is generally **not symmetric**,
- $\nabla_{ij}\nabla_{jk} \neq \nabla_{ik}$ in general,
- this non-associativity is **geometric torsion**.

Take a loop $i\to j\to k\to i$ and compute parallel transport:

$$
P_\ell = \nabla_{ij}\nabla_{jk}\nabla_{ki}
$$

In general, $P_\ell \neq \mathrm{Id}$.

<!-- !!! -->

## Dynamics / statistics live on this bundle

Now we can define meaningful operators.

### Oriented graph gradient

$$
(\nabla s)_{ij} = \nabla_{ij}s_i - s_j \in F_j
$$

### Bundle Laplacian (connection Laplacian)

$$
(\Delta^\nabla s)_i
= \sum_{j\sim i} \left( s_i - \nabla_{ji}s_j \right)
$$

This operator:

- preserves orientation,
- mixes longitudinal / transverse channels correctly,
- reduces to scalar Laplacian **only if all (e_i) align**.

<!-- !!! -->

# Probabilistic / transport lifting

We need a mapping that respects the connection (i.e., does not collapse orientation or coupling geometry), where we fall back on the covariance/Laplacian models only if we _quotient out the fiber_.

In particular, we do not want to use scalar OT on marginal densities, build Laplacians on $y_i(t)$ alone, or treat $e_i$ as mere metadata.

Codomain elements can be either

1. time signals $s_i(t)$,
2. spectral / statistical objects,
3. distributional / transport objects,

<!-- |||| -->

# Operator-valued measures

We define the **generalized [cross-spectral](https://en.wikipedia.org/wiki/Spectral_density#Cross_power_spectral_density) operator** expressed as an operator-valued tensor (in components):

$$
\Sigma(\omega) = \mathbb E\left[
    \sum_{i,j} \hat y_i(\omega)\,\overline{\hat y_j(\omega)}\, e_i \otimes e_j
\right]
$$

This form lifts the [standard CSD](https://doi.org/10.1088/1464-4258/11/8/085706) (with scalar or matrix quantity) to an operator encoding directional coupling and geometric structure.
Now it lives in:

$$
\Sigma(\omega)\in \mathcal L\!\left(\bigoplus_i F_i\right)^+
$$

the set of PSD bounded linear operators on the direct sum of Hilbert spaces $F_i$.

::: info | ^@
Key elements:

- orientation enters via $e_i\otimes e_j$,
- coupling is explicit,
- antisymmetry survives.
  :::

<!-- Some work needed: prove
- Positive semi-definiteness: The operator must satisfy
   $$
   \langle v, \Sigma(\omega)\ v \rangle \geq 0 \quad \forall v
   $$
   This follows from the fact that $\Sigma(\omega)$ is the expectation of a positive semi-definite outer product $\hat{y}(\omega) \otimes \hat{y}(\omega)^\star$, analogous to the covariance matrix. Note that $\hat{y}(\omega)^\star$ denotes the complex conjugate of $\hat{y}(\omega)$ and $\hat{y}(\omega) \otimes \hat{y}(\omega)^\star$ is the coordinate-free (operator or tensor) notation of $\hat y_i(\omega)\,\overline{\hat y_j(\omega)}$. The proof should mirror that of [covariance matrices](https://statproofbook.github.io/P/covmat-psd.html): for any vector $a$, $a^ \Sigma(\omega) a = \mathbb{E}[|a^* \hat{y}(\omega)|^2] \geq 0$.
- Measurability and integrability: The Fourier transform $\hat{y}_i(\omega)$ must exist (i.e., $y_i(t)$ square-integrable), and the expectation must converge. This requires stationarity or ergodicity of the process to ensure $\mathbb{E}[\hat{y}_i \overline{\hat{y}_j}]$ is well-defined. -->

<!-- Some literature to look at on CSD:
- [Novelli et al., 2024](https://doi.org/10.1162/netn_a_00348)
- [Bakhshali et al., 2019](https://doi.org/10.1016/j.measurement.2019.04.023)
- [Besserve et al., 2013](https://doi.org/10.5555/2999792.2999895)
- [Friston et al., 2012](https://doi.org/10.1016/j.neuroimage.2011.07.048)
- [Gori et al., 2009](https://doi.org/10.1088/1464-4258/11/8/085706) -->

<!-- ||| -->

## Mapping to distributions

We define the positive operator-valued measure ([POVM](https://en.wikipedia.org/wiki/POVM)):

$$
\mu(d\omega) = \Sigma(\omega)\,\mathrm{d}\omega
$$

<!-- To ensure the operator-valued measure $\mu(d\omega) = \Sigma(\omega),d\omega$ is well-defined, key proofs include:

- Positive semi-definiteness: Show $\langle v, \Sigma(\omega) v \rangle \geq 0$ for all $v$, which follows from $\Sigma(\omega) = \mathbb{E}[\hat{y}(\omega) \otimes \hat{y}(\omega)^*]$ being an expectation of a positive semi-definite outer product.
- Bochner integrability: Prove $\Sigma(\omega)$ is measurable and $\int |\Sigma(\omega)|,d\omega < \infty$, ensuring the integral $\mu(E) = \int_E \Sigma(\omega),d\omega$ converges in the operator norm.
- Operator-valued Bochner or Pettis integral: Use functional analytic results to define the integral of operator-valued functions with respect to scalar or spectral measures.

As a standard result in operator-valued measure theory: For any Borel set $E \subset \mathbb{R}$, the mapping $E \mapsto \langle v, \mu(E) v \rangle$ defines a non-negative scalar measure for each vector $v$, satisfying countable additivity. -->

Now:

- entropy = von Neumann entropy,
- transport = operator-valued OT,
- damage = loss of coherence.

This **strictly preserves the bundle**, because operators act _between fibers_.

<!-- ||| -->

## Emergent connection from coupling

### Connection in the probabilistic space

Define a data-driven transport operator:

$$
T_{ij} : \mu_i \to \mu_j
$$

describing how spectral energy / coherence moves between sensors.

This defines a **connection on the graph**:

- edges carry transport maps,
- composition along paths is meaningful.

### Transport between fibers

Between nodes (i) and (j), define some **transport cost** using the connection.

Note:

$$
c_{ij}(v_i,v_j) = \| v_j - \nabla_{ij} v_i \|^2
$$

<!-- !!! -->

## Sanity check

::: question | ^@
If Liouville preservation, unitarity, and self-adjointness are broken, in what sense are we allowed to talk about generators, transport, connections, Laplacians?
:::

### Volume preservation

Fails because:

- dissipation,
- stochastic forcing,
- damage-induced irreversibility.

Instead of:

$$
\text{vol}(\Phi_t(A)) = \text{vol}(A)
$$

we have:

$$
\frac{d}{dt} \mathrm{Ent}(\mu_t \mid \mu_\mathrm{ref}) \ge 0
$$

Damage shows up as **entropy production**, not volume loss.

<!-- ||| -->

## Sanity check

::: question | ^@
If Liouville preservation, unitarity, and self-adjointness are broken, in what sense are we allowed to talk about generators, transport, connections, Laplacians?
:::

### Unitarity of modal evolution

Fails because:

- damping,
- mode coupling,
- non-normal operators,
- time-varying stiffness.

Instead of:

$$
|U_t\psi| = |\psi|
$$

we have:

$$
|\mu_t - \nu_t| \le e^{-\lambda t}|\mu_0-\nu_0|
$$

in Wasserstein / KL geometry.

Dissipation is encoded as **contraction**.

<!-- ||| -->

## Sanity check

::: question | ^@
If Liouville preservation, unitarity, and self-adjointness are broken, in what sense are we allowed to talk about generators, transport, connections, Laplacians?
:::

### Self-adjointness of generators

Fails because:

- damping,
- hysteresis (history dependence),
- damage (operator drift).

The generator decomposes as:

$$
\mathcal L = \underbrace{\mathcal L_\text{sym}}_{\text{diffusion}}

* \underbrace{\mathcal L_\text{anti}}_{\text{circulation / torsion}}
$$

Neither part needs to be self-adjoint.

This is where torsion _lives_.

<!-- ||| -->

E.g., note that the Fokker–Planck operator

$$
\mathcal L \rho
= \nabla\cdot(\rho\nabla V)
* \beta^{-1}\Delta\rho
$$

- is **not self-adjoint** in (L^2),
- does **not generate unitary flow**,
- does **not preserve volume**,

yet it:

- generates a valid semigroup,
- defines a geometry (via gradient flow),
- underlies optimal transport.

<!-- !!! -->

## Next Steps

- Formally define a _reference connection_.
- Define a statistically robust torsion-change functional / sort of "strain" measure.
- Define **torsion and curvature observables** computable from data,
- Show explicitly how Laplacian / covariance methods arise as projections.

The goal is to construct a sort of finite strain theory on Wasserstein space.

<!-- Potentially look at cosserat continua, and gauge theories of defects -->
