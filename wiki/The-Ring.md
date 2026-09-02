# The Ring

SpaceDonkey currently assumes a **closed self-supporting compression hoop** around Earth's equator.

That is deliberately stronger than saying “some orbital-ring-like backbone.” The ring is part of the hypothesis and therefore gets its own kill test.

It is **not** silently replaced by a fast-moving Birch rotor. Prior orbital-ring work matters enormously, but the present SpaceDonkey architecture asks whether a roughly Earth-fixed / co-rotating closed hoop can support itself while carrying many inward-hanging Donkeys.

## What the ring does

The backbone has three jobs:

1. **Structural support** — carry its own global gravitational load and the local loads introduced by Donkeys.
2. **Reaction structure** — provide pivots and reaction paths for powered swings.
3. **Power and control distribution** — move electrical power, timing, sensing, and coordination around the network.

The conceptual inversion is:

> **The ring fights gravity globally in compression. The Donkeys use gravity locally in tension. The payload never fights either one globally at all.**

## First-order compression requirement

Take a small ring arc subtending $d\theta$.

Let:

- $R$ be ring radius from Earth's center,
- $\lambda$ be ring mass per unit length,
- $C$ be circumferential compressive force,
- $g_{\mathrm{eff}}$ be inward effective acceleration in the ring's rotating frame.

The arc mass is

$$
dm = \lambda R\,d\theta.
$$

Its inward effective weight is

$$
dm\,g_{\mathrm{eff}}.
$$

The two circumferential compression forces on the ends of the small arc produce an outward radial resultant of approximately

$$
C\,d\theta.
$$

Balancing them gives

$$
C = \lambda R g_{\mathrm{eff}}.
$$

If $\lambda = \rho A$, then

$$
\sigma = \frac{C}{A} = \rho R g_{\mathrm{eff}},
$$

so the required compressive **specific strength** is

$$
\frac{\sigma}{\rho}=R g_{\mathrm{eff}}.
$$

For a ring co-rotating with Earth,

$$
g_{\mathrm{eff}}(R)=\frac{\mu_E}{R^2}-\omega_E^2R,
$$

therefore

$$
\frac{\sigma}{\rho}
=\frac{\mu_E}{R}-\omega_E^2R^2.
$$

Near Earth's surface this is on the order of

$$
6\times10^7\ \mathrm{J/kg}.
$$

That is a severe material demand **before** solving buckling, imperfections, joints, dynamic loading, Donkey reaction loads, thermal gradients, construction, or failure containment.

## Why simply making it thicker does not solve the first problem

Increasing cross-sectional area increases both load capacity and self-weight. In the idealized membrane calculation above, the required $\sigma/\rho$ is therefore a **specific-strength** requirement rather than something that disappears by scaling the whole ring up.

A larger section may help local buckling and stiffness, but it does not erase the fundamental gravity-versus-material scaling.

## The nastier structural questions

Even if a material satisfies the simple stress estimate, the ring still has to survive:

- global and local buckling,
- imperfect circularity,
- centering and lateral stability,
- dynamic loads from independently moving Donkeys,
- resonances and wave propagation around a planetary circumference,
- thermal expansion and day/night gradients,
- local damage without progressive collapse,
- assembly and maintenance,
- debris impacts,
- and the transfer of torque and angular momentum through the structure.

The ring therefore has a clean falsification criterion:

> If a closed compression hoop cannot be made materially and dynamically credible at a useful radius, **this version of SpaceDonkey dies or the architecture must explicitly change.**

That is preferable to quietly changing the support mechanism while keeping the same picture.

[[Home]] · [[The-Idea]] · [[Kill-Tests]] · [[Energy-and-Angular-Momentum]]
