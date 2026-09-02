# The Donkeys

A **Donkey** is one independently controlled momentum-exchange stage hanging inward from the equatorial ring.

The payload does not jump onto a stationary rope. The engineering target is a **merge between two moving systems**.

## One-Donkey sequence

A useful stage looks like:

**approach → guidance/acquire → mechanical lock → powered ride → timed release → free flight**

The payload approaches a capture carriage already moving on a compatible trajectory. Relative position and relative velocity must already be small enough that the capture system is correcting a residual error, not rescuing a collision.

> **The swing does the acceleration. The magnet does the forgiveness.**

A plausible layered capture mechanism is:

1. **Trajectory geometry** gets the payload close to the correct place, speed, and direction.
2. **Electromagnetic guidance/acquisition** removes small residual mismatch and increases capture tolerance.
3. **Mechanical attachment** carries the real sustained load during the powered ride.

Magnets are not magic brakes. The relative kinetic energy that must be handled at capture is

$$
E_{\mathrm{rel}}=\frac12m\lVert\Delta\mathbf v\rVert^2.
$$

That square matters. Geometry must make $\Delta v$ small before contact.

## Powered ride

Once locked, the Donkey can add momentum over a finite arc rather than through one violent impulse.

For tip speed $v$ and effective swing radius $r$,

$$
a_c=\frac{v^2}{r}.
$$

At equal tip speed, a longer swing lowers centripetal acceleration and angular rate. That creates one possible reason lower Donkeys might be **longer, slower, and more forgiving**.

The best geometry is not known in advance. A Donkey might use:

- a simple rotating tether,
- controlled reeling,
- an articulated tip carriage,
- translated capture motion,
- active torque during the ride,
- or combinations of these.

A purely rotating tip traces a circle, so claims about a “linear capture path” are only locally true. A more complicated carriage may widen the near-co-moving corridor, but every extra degree of freedom adds mass, control burden, and failure modes.

## Capture set

For Donkey $D_i$, define a candidate capture region in state space:

$$
\mathcal C_i = \{(\mathbf r,\mathbf v,t):
\lVert\Delta\mathbf r\rVert\le r_{\max},\
\lVert\Delta\mathbf v\rVert\le v_{\max},\
\text{load and geometry constraints satisfied}\}.
$$

The exact set must eventually include attitude, angular rate, tether state, actuator state, and uncertainty.

The key design target is not merely “can the tip touch the payload?” It is:

> **Can the payload enter a robust capture corridor with low enough mismatch that attachment is survivable and useful?**

## Release

A Donkey should release into a **set of useful next states**, not necessarily the single fastest trajectory available.

A deliberately smaller throw may be better if it creates a much larger region reachable by the next Donkey.

This is why SpaceDonkey treats free flight as a feature. After release, the payload may climb, coast, glide, or dive before the next capture.

## Donkeys do not need to be uniform

A likely network would use differentiated stages:

- **Lower Donkeys:** long, slow, forgiving; constrained heavily by atmosphere.
- **Middle Donkeys:** optimized for transfer, correction, and recovery.
- **Upper Donkeys:** potentially faster after state uncertainty has been repeatedly reduced.
- **Final Donkey:** releases directly into the chosen orbital state.

This is a hypothesis to test, not a final design.

## First experiment

The correct first simulation is **one Donkey**, not the whole planet.

Test whether one reusable stage can:

1. meet a ballistic payload at low relative velocity,
2. capture without an unacceptable shock,
3. accelerate it over a useful finite arc,
4. release it into a recoverable free-flight trajectory,
5. and restore the stage's lost energy and momentum afterward.

If that fails, the planetary version is irrelevant.

[[Home]] · [[Grace-and-State-Space]] · [[Energy-and-Angular-Momentum]] · [[Research-Roadmap]]
