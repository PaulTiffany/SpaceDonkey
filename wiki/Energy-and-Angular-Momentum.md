# Energy and Angular Momentum

SpaceDonkey does not get orbital energy or angular momentum for free.

The possible advantage is architectural: reusable machinery remains outside the payload and can accumulate energy slowly, deliver it mechanically, recover some of it later, and serve many payloads.

## Orbital energy

For payload mass $m$, specific mechanical energy in a two-body approximation is

$$
\epsilon=\frac{v^2}{2}-\frac{\mu_E}{r},
$$

with total payload energy

$$
E=m\epsilon.
$$

Across all Donkeys,

$$
\sum_i W_i
=\Delta E_{\mathrm{payload}}+E_{\mathrm{losses}}.
$$

The motors, power network, momentum reservoirs, and any regeneration system must account for that work.

## Angular momentum is the harder bookkeeping problem

Specific angular momentum is

$$
\mathbf h=\mathbf r\times\mathbf v.
$$

For a circular orbit of radius $R$,

$$
h=\sqrt{\mu_E R}.
$$

A payload initially co-rotating with Earth's equator has approximately

$$
h_0=\omega_E r_0^2.
$$

So a rough outbound angular-momentum requirement is

$$
\Delta L=m(h_f-h_0).
$$

Every prograde increment given to an outbound payload produces an equal and opposite change somewhere else in the full system.

A massive ring can absorb some of that temporarily, but repeated launches cannot simply drain its rotational state forever.

> **Electricity can replenish energy. Electricity by itself does not make angular momentum conservation disappear.**

## Possible momentum-return paths

A complete architecture needs an explicit external or reciprocal momentum pathway. Candidates include:

- inbound payloads returning angular momentum regeneratively,
- electromagnetic interaction that ultimately couples torque into Earth,
- dedicated torque links to Earth that do not carry the ring's main weight,
- reaction mass or propulsion,
- exchange with other orbital masses or momentum reservoirs,
- or a traffic pattern whose inbound and outbound flows substantially balance.

These are research directions, not solved subsystems.

## Efficiency must be measured at several levels

The absence of onboard propellant does not automatically make the system efficient.

### Transfer efficiency

$$
\eta_{\mathrm{transfer}}
=\frac{\Delta E_{\mathrm{payload}}}
{E_{\mathrm{mechanical/electrical\ input\ during\ transfer}}}.
$$

### Recharge efficiency

$$
\eta_{\mathrm{recharge}}
=\frac{\Delta E_{\mathrm{reservoir\ restored}}}
{E_{\mathrm{electrical/propulsive\ input}}}.
$$

### Full-system efficiency

$$
\eta_{\mathrm{system}}
=\frac{\Delta E_{\mathrm{payload}}}
{E_{\mathrm{transfer}}+E_{\mathrm{recharge}}+E_{\mathrm{support}}+E_{\mathrm{control}}+E_{\mathrm{losses}}}.
$$

The practical system also has to pay for:

- capital mass,
- standing structural/support costs,
- tether drag and atmospheric losses,
- maintenance,
- debris protection,
- control infrastructure,
- replacement hardware,
- and bootstrap construction.

## Why the concept could still be interesting

If the hard structural and momentum-return problems are solvable, external reusable machinery offers real architectural attractions:

- payloads need less onboard propulsion hardware,
- the same motors and tethers can serve many flights,
- electrical power can be accumulated between launches,
- large infrastructure can buffer short high-power events,
- inbound traffic may return useful energy and momentum,
- and the payload can be accelerated over many bounded interactions rather than one continuous burn.

That is a hypothesis about **transport infrastructure**, not perpetual motion.

[[Home]] · [[The-Ring]] · [[The-Donkeys]] · [[Kill-Tests]]
