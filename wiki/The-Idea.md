# The Idea

SpaceDonkey is a staged momentum-exchange transport concept.

The payload does **not** ride one elevator cable and it does **not** receive one heroic throw from a single skyhook. It moves through a sequence of locally reachable states:

**approach → capture → powered ride → release → free flight → next capture**

Then repeat.

## Orbit is not height

Getting high is only part of getting to orbit. The hard part is acquiring enough **horizontal velocity** that the payload continually falls around Earth instead of back into it.

That changes the design problem. A useful stage does not need to increase altitude monotonically. It only needs to move the payload into a state from which another useful stage can take over.

A release may therefore lead to:

- a climb,
- a coast,
- a glide,
- a dive,
- or a long sideways free-flight leg.

The rule is simple:

> **The goal is not to keep climbing. The goal is to keep reaching the next legal move.**

## The video-game picture

Imagine a gigantic tree whose main branches wrap around Earth's equator.

Many vines hang inward toward Earth. A player grabs one vine, swings, lets go, flies freely, catches another, and keeps brachiating through the available geometry.

The last release is different only in degree: instead of reaching another vine, the payload enters orbit.

The tree is a joke. The geometry is not.

## The architecture

SpaceDonkey currently assumes three layers:

1. A **continuous self-supporting equatorial ring** that carries the global structural burden and provides pivots, power, and control infrastructure.
2. Many independently powered **Donkeys** hanging inward from the ring.
3. A payload that spends much of the route in **free flight**, moving between overlapping capture regions.

The Donkeys do not need to be identical or evenly spaced. Lower stages may be long, slow, and forgiving; higher stages may be shorter or faster as the payload state becomes better controlled.

## Why many stages?

A single large transfer demands enormous throw, narrow timing, high structural loads, and a difficult rendezvous.

SpaceDonkey asks whether **multiplicity can buy grace**:

- lower relative capture velocity,
- longer interaction time,
- smaller momentum jumps,
- bounded local acceleration,
- alternate reachable next nodes,
- recoverable missed handoffs,
- and smaller local failures.

More stages also mean more hardware, more coordination, and more opportunities to fail. That trade is the core experiment, not an assumption.

## What would count as success?

Not a pretty orbital-ring rendering.

The idea earns another step only if simple models show that one Donkey can perform a useful capture–carry–release maneuver under bounded loads, and then that two Donkeys can produce a robust overlap between the first release region and the second capture region.

If that fails, SpaceDonkey fails cheaply.

If it works, add another Donkey.

[[Home]] · [[The-Ring]] · [[The-Donkeys]] · [[Grace-and-State-Space]]
