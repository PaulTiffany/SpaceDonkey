#!/usr/bin/env python3
"""Generate orbital-ring schematics as SVG from a parameter file.

Figures in this repository are computed, not drawn and not prompted. Every
radius, angle and anchor position below follows from the numbers in the
parameter file, so a figure can be regenerated, reviewed as a diff, and checked
in CI.

Usage:
    python tools/figures/ringgen.py --all
    python tools/figures/ringgen.py --all --check
    python tools/figures/ringgen.py tools/figures/params/orbital-ring-equatorial.json

Standard library only. No dependencies, no network, deterministic output.
"""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys
from typing import Any

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
PARAM_DIR = pathlib.Path(__file__).resolve().parent / "params"


# --------------------------------------------------------------------------
# geometry
# --------------------------------------------------------------------------


def polar(cx: float, cy: float, radius: float, deg: float) -> tuple[float, float]:
    """Point on a circle. Angle in degrees, counter-clockwise, 0 deg = +x.

    Screen y grows downward, so the sine term is subtracted.
    """
    rad = math.radians(deg)
    return (cx + radius * math.cos(rad), cy - radius * math.sin(rad))


def tangent_unit(deg: float) -> tuple[float, float]:
    """Unit vector for counter-clockwise motion at `deg`, in screen coords."""
    rad = math.radians(deg)
    return (-math.sin(rad), -math.cos(rad))


def display_ring_radius(
    planet_px: float, planet_km: float, altitude_km: float, exaggeration: float
) -> float:
    """Ring radius in pixels, with altitude exaggerated for legibility.

    A true-scale 300 km ring around a 6371 km planet sits at 1.047 planet
    radii, which renders as a line almost touching the limb. The exaggeration
    factor scales only the *altitude*, never the planet, and the figure states
    the factor on its face so nobody mistakes it for a scale drawing.
    """
    true_ratio = (planet_km + altitude_km) / planet_km
    return planet_px * (1.0 + (true_ratio - 1.0) * exaggeration)


# --------------------------------------------------------------------------
# svg emit
# --------------------------------------------------------------------------


def fmt(value: float) -> str:
    """Fixed 2dp so output is byte-stable across platforms."""
    return f"{value:.2f}".rstrip("0").rstrip(".")


def text(x: float, y: float, content: str, fill: str, size: int = 14, anchor: str = "start") -> str:
    return (
        f'<text x="{fmt(x)}" y="{fmt(y)}" text-anchor="{anchor}" '
        f'font-family="system-ui, -apple-system, Segoe UI, sans-serif" '
        f'font-size="{size}" fill="{fill}">{content}</text>'
    )


def leader(x1: float, y1: float, x2: float, y2: float, stroke: str) -> str:
    return (
        f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" '
        f'stroke="{stroke}" stroke-width="0.5" stroke-dasharray="3 3"/>'
    )


def build_svg(p: dict[str, Any]) -> str:
    c = p["colors"]
    w, h = p["canvas"]["width"], p["canvas"]["height"]
    pad = p["canvas"]["padding"]
    cx, cy = w / 2.0, (h - pad) / 2.0 + pad / 2.0

    planet_px = p["render"]["planet_radius_px"]
    ring_px = display_ring_radius(
        planet_px,
        p["physical"]["planet_radius_km"],
        p["physical"]["ring_altitude_km"],
        p["render"]["altitude_exaggeration"],
    )
    stream_px = ring_px - p["render"]["mass_stream_offset_px"]
    n = p["physical"]["tether_count"]

    out: list[str] = []
    add = out.append

    add(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" role="img">'
    )
    add(f"<title>{p['meta']['title']}</title>")
    add(f"<desc>{p['meta']['description']}</desc>")
    add(
        '<defs><marker id="flow" viewBox="0 0 10 10" refX="8" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" '
        'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'
        "</marker></defs>"
    )

    # panel: self-contained dark background so the figure reads on light and
    # dark hosts without a theme-aware stylesheet
    add(
        f'<rect x="{fmt(pad)}" y="{fmt(pad)}" width="{fmt(w - 2 * pad)}" '
        f'height="{fmt(h - 2 * pad)}" rx="12" fill="{c["space"]}"/>'
    )

    # starfield: fixed positions, no RNG, so output stays byte-stable
    for sx, sy, sr, so in p["render"]["stars"]:
        add(f'<circle cx="{sx}" cy="{sy}" r="{sr}" fill="#FFFFFF" opacity="{so}"/>')

    # planet
    add(f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(planet_px)}" fill="{c["planet"]}"/>')
    lx, _ly = polar(cx, cy, planet_px, 135)
    tx, ty = polar(cx, cy, planet_px, 90)
    add(
        f'<path d="M {fmt(tx)} {fmt(ty)} A {fmt(planet_px)} {fmt(planet_px)} 0 0 0 '
        f'{fmt(lx - planet_px * 0.293)} {fmt(cy)}" fill="none" '
        f'stroke="{c["limb"]}" stroke-width="3" opacity="0.55"/>'
    )
    for ex, ey, erx, ery, eo in p["render"]["landmasses"]:
        add(
            f'<ellipse cx="{fmt(cx + ex)}" cy="{fmt(cy + ey)}" rx="{erx}" ry="{ery}" '
            f'fill="{c["land"]}" opacity="{eo}"/>'
        )

    # tethers and equatorial anchors
    for i in range(n):
        deg = 360.0 * i / n + p["render"]["tether_phase_deg"]
        ax, ay = polar(cx, cy, planet_px, deg)
        bx, by = polar(cx, cy, ring_px, deg)
        add(
            f'<line x1="{fmt(ax)}" y1="{fmt(ay)}" x2="{fmt(bx)}" y2="{fmt(by)}" '
            f'stroke="{c["tether"]}" stroke-width="2"/>'
        )
        add(f'<circle cx="{fmt(ax)}" cy="{fmt(ay)}" r="5" fill="{c["accent"]}"/>')

    # mass stream: the load-bearing element. moves above orbital velocity, so
    # its surplus centrifugal force supports the stationary sheath above it
    add(
        f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(stream_px)}" fill="none" '
        f'stroke="{c["accent"]}" stroke-width="1.5" stroke-dasharray="7 6" opacity="0.9"/>'
    )
    for deg in p["render"]["flow_marker_deg"]:
        px, py = polar(cx, cy, stream_px, deg)
        ux, uy = tangent_unit(deg)
        add(
            f'<line x1="{fmt(px - ux * 7)}" y1="{fmt(py - uy * 7)}" '
            f'x2="{fmt(px + ux * 7)}" y2="{fmt(py + uy * 7)}" '
            f'stroke="{c["accent"]}" stroke-width="2" marker-end="url(#flow)"/>'
        )

    # stationary ring sheath
    add(
        f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(ring_px)}" fill="none" '
        f'stroke="{c["ring"]}" stroke-width="4"/>'
    )
    for deg in p["render"]["platform_deg"]:
        px, py = polar(cx, cy, ring_px, deg)
        add(
            f'<rect x="{fmt(px - 8)}" y="{fmt(py - 8)}" width="16" height="16" '
            f'rx="3" fill="{c["ring"]}"/>'
        )

    # annotation
    rx, ry = polar(cx, cy, ring_px, 135)
    add(leader(150, ry + 1, rx - 4, ry, c["leader"]))
    add(text(pad + 12, ry + 5, "Stationary ring", c["label"]))

    sx2, sy2 = polar(cx, cy, stream_px, 225)
    add(leader(125, sy2 + 8, sx2 - 3, sy2, c["leader"]))
    add(text(pad + 12, sy2 + 13, "Mass stream", c["accent"]))
    add(text(pad + 12, sy2 + 30, "above orbital velocity", c["muted"], size=12))

    # "Static" is load-bearing on this label. In review a reader took the radial
    # lines for a payload trajectory and asked about the swings getting shorter
    # through the flight path. Nothing in this figure moves except the mass
    # stream; the tethers are structure under tension.
    ttx, tty = polar(cx, cy, ring_px, 60)
    add(leader(ttx + 56, tty - 20, ttx + 3, tty - 3, c["leader"]))
    add(text(ttx + 62, tty - 24, "Static tether", c["label"]))
    add(text(ttx + 62, tty - 8, "structural, not a path", c["muted"], size=12))

    anx, any_ = polar(cx, cy, planet_px, -60)
    add(leader(anx, h - pad - 40, anx, any_ + 10, c["leader"]))
    add(text(anx, h - pad - 24, "Equatorial anchor", c["accent"], anchor="middle"))

    add(text(cx, cy + 6, "viewed down polar axis", c["axis"], size=12, anchor="middle"))

    # scale honesty: the figure states what it exaggerated
    add(
        text(
            pad + 12,
            pad + 26,
            f"Planet radius {p['physical']['planet_radius_km']:,} km &#183; "
            f"ring altitude {p['physical']['ring_altitude_km']:,} km &#183; "
            f"altitude exaggerated {p['render']['altitude_exaggeration']}&#215;",
            c["muted"],
            size=12,
        )
    )
    add("</svg>")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------


def render(param_path: pathlib.Path, check: bool) -> bool:
    """Return True if the on-disk figure matches what we would generate."""
    params = json.loads(param_path.read_text(encoding="utf-8"))
    svg = build_svg(params)
    out_path = REPO_ROOT / params["meta"]["output"]

    if check:
        if not out_path.exists():
            print(f"MISSING  {params['meta']['output']}", file=sys.stderr)
            return False
        if out_path.read_text(encoding="utf-8") != svg:
            print(f"STALE    {params['meta']['output']}", file=sys.stderr)
            return False
        print(f"ok       {params['meta']['output']}")
        return True

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(svg, encoding="utf-8")
    print(f"wrote    {params['meta']['output']}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate orbital-ring figures from parameters.")
    ap.add_argument("params", nargs="*", type=pathlib.Path, help="parameter files to render")
    ap.add_argument("--all", action="store_true", help="render every file in tools/figures/params")
    ap.add_argument(
        "--check",
        action="store_true",
        help="verify committed figures match their parameters; do not write",
    )
    args = ap.parse_args()

    targets = sorted(PARAM_DIR.glob("*.json")) if args.all else list(args.params)
    if not targets:
        ap.error("give one or more parameter files, or --all")

    ok = all([render(t, args.check) for t in targets])
    if args.check and not ok:
        print(
            "\nFigures are out of date. Run:  python tools/figures/ringgen.py --all",
            file=sys.stderr,
        )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
