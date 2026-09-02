# Grace and State Space

The distinctive SpaceDonkey hypothesis is not “tethers can exchange momentum.” That is old and serious prior art.

The question is whether **using many smaller stages changes the rendezvous problem enough to matter**.

We call that possible advantage **grace**.

## What grace means

Informally, grace is:

> **How much error can the architecture tolerate while still preserving a useful next move?**

It may eventually combine:

- position tolerance,
- velocity tolerance,
- timing-window width,
- attitude tolerance,
- acceleration margin,
- tether-load margin,
- uncertainty growth,
- and the size of the next reachable region.

Grace is not yet a finalized scalar metric.

The qualitative objective is already clear:

> **Maximize robust overlap, not maximum throw.**

## Payload state

A useful full payload state is

$$
S=(\mathbf r,\mathbf v,q,\boldsymbol\omega,t),
$$

where $\mathbf r$ and $\mathbf v$ are position and velocity, $q$ is attitude, $\boldsymbol\omega$ is angular rate, and $t$ is time.

A minimal translational model can begin with

$$
S=(\mathbf r,\mathbf v,t).
$$

For Donkey $D_i$, define a **capture set**

$$
C_i\subset\mathcal S
$$

containing states from which capture is possible under specified limits on mismatch, acceleration, load, geometry, and timing.

Define a **release set**

$$
R_i\subset\mathcal S
$$

containing states reachable after safe capture and bounded manipulation by that Donkey.

A useful handoff exists when

$$
R_i\cap C_{i+1}\neq\varnothing.
$$

A route to orbit exists when repeated handoffs eventually reach a useful orbital set $\mathcal O$:

$$
R_N\cap\mathcal O\neq\varnothing.
$$

That is the formal version of **swing, release, catch the next one**.

## Robust overlap

An abstract future grace metric might depend on the measure of the robust overlap region:

$$
G_i\propto\mu\left(R_i^{\mathrm{robust}}\cap C_{i+1}^{\mathrm{robust}}\right).
$$

This is only a research placeholder. The state dimensions need sensible normalization before such a number means anything.

The more important design principle is that the optimizer should be rewarded for leaving **many survivable next moves**, not for extracting every possible meter per second from the current stage.

## Why more stages might help

At the equator, Earth already provides roughly $0.465\ \mathrm{km/s}$ eastward surface speed. Low Earth orbital speed is roughly $7.8\ \mathrm{km/s}$, so a crude intuition leaves about $7.3\ \mathrm{km/s}$ of additional horizontal speed to acquire.

If that were divided equally — it will not be in a real trajectory — the arithmetic would look like:

- 10 stages: about $730\ \mathrm{m/s}$ each,
- 100 stages: about $73\ \mathrm{m/s}$ each,
- 1000 stages: about $7.3\ \mathrm{m/s}$ each.

This is **not** a trajectory design and does not imply equal energy increments. It only shows why high stage count is worth asking about: the local burden can become qualitatively different even though the global orbital requirement does not disappear.

## Dives are legal

A path solver must not impose monotonic altitude.

A payload released from one Donkey may descend while gaining speed, changing flight-path angle, and moving toward a much better next capture corridor.

The useful question is not:

> Did the payload go down?

It is:

> **Did the free trajectory place the payload inside a larger or safer next capture set?**

## Reliability is a network problem

A naive linear chain with per-stage reliability $p$ has success probability approximately

$$
p^N,
$$

which becomes terrible for large $N$ unless $p$ is extremely close to one.

So high stage count only becomes attractive if the system is **not merely one brittle chain**.

The architecture should search for:

- multiple reachable next Donkeys,
- recoverable missed captures,
- alternate free-flight routes,
- local isolation of failed hardware,
- and overlapping reachable-state envelopes.

The desired object is therefore closer to a **transport network in phase space** than a ladder in physical space.

[[Home]] · [[The-Idea]] · [[The-Donkeys]] · [[Kill-Tests]]
