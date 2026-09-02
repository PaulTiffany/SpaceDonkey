# Research Roadmap

SpaceDonkey should earn complexity one layer at a time.

The correct order is **local mechanics first, planetary infrastructure later**.

## Stage 0 — Literature map

Build and maintain a compact bibliography covering:

- orbital rings,
- rotovators and skyhooks,
- HASTOL,
- MXER,
- Sling-on-a-Ring,
- staged and multi-tether transfer,
- flexible-tether capture control,
- motorized/reeling tethers,
- tether materials,
- debris survivability,
- and large compression-ring stability.

The goal is not novelty theater. If a prior system already solves a SpaceDonkey subproblem, inherit it.

## Stage 1 — One ideal Donkey

Start in a 2D equatorial plane with:

- spherical Earth,
- point-mass payload,
- one prescribed pivot,
- massless rigid tether,
- adjustable tether length,
- bounded torque,
- explicit capture mismatch,
- finite-time constrained motion,
- and optimized release.

Reward a weighted combination of:

- useful prograde $\Delta v$,
- capture duration and tolerance,
- next-stage reachability,
- low peak acceleration,
- low peak tether tension,
- and low dissipative capture loss.

Subject to explicit bounds such as

$$
a_{\max}\le a_{\mathrm{limit}},
$$

and

$$
T_{\max}\le T_{\mathrm{limit}}.
$$

The optimizer should be rewarded for **grace**, not merely release speed.

## Stage 2 — Two Donkeys

This is the first direct test of the SpaceDonkey thesis.

Do not optimize Donkey 1 in isolation. Optimize the pair for robust overlap between Donkey 1's release set and Donkey 2's capture set.

Questions:

1. Does a larger first throw make the second capture harder?
2. Is a deliberately smaller first throw much more forgiving?
3. Can a downward free-flight leg improve capture geometry?
4. Can the first release create a long near-co-moving segment with Donkey 2?
5. Do timing and state uncertainties shrink after each controlled capture?
6. How much does reachable-set overlap change as stage workload decreases?

## Stage 3 — Compression-ring model

In parallel with the local transfer work, attack the backbone honestly.

Model:

- specific compressive stress versus radius,
- global buckling modes,
- centering/lateral stability,
- local Donkey reaction loads,
- dynamic wave propagation,
- thermal strain,
- and failure containment.

If the compression-hoop architecture fails, record the failure before considering a different support mechanism.

## Stage 4 — Atmosphere

Add:

- drag,
- lift where relevant,
- heating proxies,
- weather/operational exclusion zones,
- and realistic lower-altitude constraints.

This determines whether the first Donkey can plausibly reach into the atmosphere or whether SpaceDonkey begins only after a conventional/suborbital first stage.

## Stage 5 — Flexible tether

Replace the ideal rigid tether with distributed-mass elastic dynamics.

Add:

- vibration,
- taper,
- damping,
- fatigue,
- control delay,
- tip-position uncertainty,
- and capture-induced transients.

This stage should be expected to make the problem substantially harder.

## Stage 6 — Energy and momentum reservoirs

Give each Donkey and the ring finite reservoirs.

Track:

- motor power,
- mechanical energy,
- angular momentum,
- recovery time,
- heat losses,
- and explicit reboost / torque-return mechanisms.

The model must close the books after repeated launches, not merely one demonstration transfer.

## Stage 7 — Network search

Stop thinking in terms of one compulsory sequence.

Search many-node geometries for:

- overlapping capture basins,
- alternate next Donkeys,
- recoverable misses,
- bounded per-node workload,
- local isolation,
- and traffic routing.

The desired architecture is a **network of reachable states**.

## Stage 8 — Bootstrap and economics

Only after the physics survives should the project ask whether the system can be built incrementally.

Estimate:

- launched infrastructure mass,
- payload throughput,
- maintenance rate,
- replacement rate,
- energy cost,
- capital amortization,
- and the minimum useful partial network.

## Current strongest statement

SpaceDonkey does **not** presently establish that a many-swing Earth-to-orbit system is buildable, economical, safe, or superior to rockets.

It does identify a falsifiable question assembled from serious prior art:

> **Does increasing the number of momentum-exchange stages create enough rendezvous grace, bounded acceleration, redundancy, and recovery to outweigh the added tether, control, reliability, and infrastructure burden?**

The next meaningful result is not a prettier rendering.

It is a one-Donkey model, a two-Donkey composition test, and a serious compression-ring calculation.

[[Home]] · [[Prior-Art]] · [[Kill-Tests]] · [[Grace-and-State-Space]]
