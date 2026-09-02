# Prior Art

SpaceDonkey's posture is **inheritance, not novelty theater**.

The local mechanics — rotating tethers, payload capture, momentum exchange, reboost, circum-Earth infrastructure, and even multi-stage tether handoffs — all have serious prior art.

The question that may be distinctive is narrower:

> **What happens if very high stage count is used deliberately to trade maximum throw for capture grace, bounded loads, free-flight recovery, redundancy, and large reachable-state overlap?**

That needs a deeper literature review before any novelty claim.

## Paul Birch — Orbital Ring Systems and Jacob's Ladders (1982)

Paul Birch proposed low-Earth orbital rings in which a rapidly moving orbital ring supports geographically stationary stations electromagnetically. Shorter hanging cables can then descend from those stations instead of requiring one cable to geostationary altitude.

Source:

- Paul Birch, *Orbital Ring Systems and Jacob's Ladders — I*, Journal of the British Interplanetary Society 35 (1982), 475–497.
- https://nss.org/wp-content/uploads/Orbital-Rings.pdf

SpaceDonkey inherits the importance of **circum-Earth infrastructure and bounded hanging members**.

Important difference: SpaceDonkey's current backbone hypothesis is a **closed self-supporting compression hoop**, not Birch's fast-moving orbital rotor supporting stationary stations. Birch remains crucial prior art and may become relevant again if the compression-ring hypothesis fails, but the two support mechanisms should not be blurred together.

## HASTOL — 1999–2001

The Hypersonic Airplane Space Tether Orbital Launch system studied transfer from a hypersonic aircraft to a rotating orbital tether. A grapple at the tether tip meets the incoming vehicle, accepts a payload, rotates, and releases it into a higher-energy trajectory.

Sources:

- NIAC Phase I/interim report: https://www.niac.usra.edu/files/studies/final_report/355Bogar.pdf
- HASTOL Phase II final report: https://www.niac.usra.edu/files/studies/final_report/391Grant.pdf

HASTOL strongly supports the local mechanical motif of **matching a moving tether tip to an incoming suborbital payload**.

SpaceDonkey asks whether many smaller exchanges can make capture and recovery less severe than one large transfer.

## NASA MXER — Momentum Exchange / Electrodynamic Reboost

NASA's MXER work treats a rotating tether as a reusable in-space upper stage. The tether gives energy and momentum to a payload and then restores its own orbital state over time, including through electrodynamic interaction with Earth's magnetic field.

Sources:

- *A Model for Dynamic Simulation and Analysis of Tether Momentum Exchange*: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20020046691.pdf
- *Design Concept for a Reusable/Propellantless MXER Tether Space Transportation System*: https://ntrs.nasa.gov/citations/20060005548
- *MXER Simulation Study*: https://ntrs.nasa.gov/citations/20060051892
- *2006 Status of the MXER Tether Development*: https://ntrs.nasa.gov/citations/20060047739

A critical lesson for SpaceDonkey is that **rendezvous is hard**. Long flexible tethers are difficult to predict and control precisely, and studied capture windows can be only seconds wide.

SpaceDonkey therefore elevates rendezvous grace from an implementation nuisance to a primary optimization target.

## Sling-on-a-Ring — 2011

Meulenberg and Poston proposed an equatorial circum-Earth ring with rotating sling modules. Their slings periodically descend toward the atmosphere, with tip motion arranged to reduce relative velocity during payload pickup.

Source:

- Andrew Meulenberg & Paul S. Poston, *Sling-on-a-Ring: Structure for an elevator to LEO*, Physics Procedia 20 (2011), 222–231.
- https://doi.org/10.1016/j.phpro.2011.08.021

This is probably the closest visual prior art to SpaceDonkey.

The important proposed difference is design objective: Sling-on-a-Ring still seeks a very large transfer with a small number of major slings and explicitly faces split-second pickup timing. SpaceDonkey asks whether **many smaller ring-supported transfers** can intentionally buy softer capture and more recovery.

## Multi-stage rotating tether networks

Sequential tether handoff is also prior art.

A recent example is:

- Maksim A. Kazanskii, *Space-Clock Elevator: Multi-Stage Orbital Transport via Rotating Tethers and Elliptical Nodes* (2026).
- https://arxiv.org/abs/2604.11221

That work studies multiple synchronized rotating tethers connected by free-flight elliptical nodes.

So SpaceDonkey should **not** be described as “the first multi-tether elevator.”

## What remains worth testing

The research target is not ownership of the components. It is whether a particular system-level objective changes the trade space:

- very high stage count,
- deliberately bounded per-stage momentum exchange,
- long or shaped capture corridors,
- free-flight legs as recovery opportunities,
- redundant reachable next nodes,
- and optimization for robust overlap rather than maximum throw.

If prior literature already demonstrates that exact objective, excellent: SpaceDonkey should cite it and move forward from there.

[[Home]] · [[The-Idea]] · [[Grace-and-State-Space]] · [[Research-Roadmap]]
