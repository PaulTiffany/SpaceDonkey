@AGENTS.md

# Claude Code notes

The shared, cross-tool instructions are imported above from [`AGENTS.md`](AGENTS.md).
That file is canonical: other agents read it directly, and Claude Code reads it through
this import. Put anything tool-neutral there, not here, so the two never drift.

Only Claude Code specifics belong below.

## Session start

Read [`docs/figures/README.md`](docs/figures/README.md) before touching anything under
`docs/figures/` or `tools/figures/`. It explains why figures are computed rather than
drawn, and that reasoning is the thing most likely to be re-litigated from first
principles by an agent who has not read it.

## Plan mode

Use plan mode before:

- changing the geometry in `tools/figures/ringgen.py`
- adding a physical parameter, or changing the meaning of an existing one
- anything touching `.github/workflows/`

Figure geometry is easy to change and hard to verify. A plan is cheaper than a wrong
diagram that looks right.

## Pull requests

`AGENTS.md` has the full policy. The short version: anything targeting `main` opens as a
**draft**, with the attribution section filled in and the human review checkbox left
alone. A human promotes it.

Branch-to-branch pull requests need none of that. Open and merge them freely as
checkpoints.

## Commits

```text
Co-authored-by: Claude <noreply@anthropic.com>
```

## Verifying your own work

Before handing back, run the full local suite from `AGENTS.md` under "Commands". The
figure check in particular catches a common failure: editing a generated SVG directly
instead of its parameter file. That change will be silently reverted by the next
generator run, so a green `--check` is the only evidence the figure is real.
