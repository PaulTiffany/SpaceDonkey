## What this changes

<!-- One or two sentences. -->

## Type

- [ ] Research or written content
- [ ] Figure or diagram
- [ ] Software, agent or tooling
- [ ] CI, build or repository plumbing

## Attribution

Tick exactly one. Required on every pull request targeting `main`.

- [ ] **Human-authored.** No coding agent involved.
- [ ] **Agent-assisted.** A human directed the work and wrote or substantially shaped
      the result.
- [ ] **Agent-authored.** An agent produced the changes.

Tool used (if any): <!-- e.g. Claude Code, Codex, Cursor -->

## Human review

**Agents must not tick this box.** It is a human's statement about their own reading of
the diff, and an agent ticking it makes the artifact a lie. Leave the pull request as a
draft; a human will read the changes, tick the box, and promote it to ready for review.

- [ ] I have reviewed my own changes.

## Checks

- [ ] `npx prettier@3.3.3 --write "**/*.{md,json,yml,yaml}"` run locally
- [ ] `npx markdownlint-cli2@0.13.0 "**/*.md" "#node_modules"` passes
- [ ] `npx cspell@8.13.1 lint --no-progress "**/*.{md,py,json}"` passes, with new domain
      terms added to `project-words.txt` rather than suppressed inline
- [ ] Figures: the parameter file changed too, and
      `python tools/figures/ringgen.py --all` was re-run
- [ ] Python: `ruff check tools/`, `ruff format --check tools/` and `mypy tools/` pass

## Claims and non-claims

<!--
For anything technical. An estimate is not a result. A schematic is not a design.
-->

**Establishes:**

**Does not establish:**

## Open questions

<!--
Anything you are unsure about. For agent-authored pull requests this section is
the most valuable part: flagged uncertainty is far cheaper than uncertainty
discovered during review.
-->
