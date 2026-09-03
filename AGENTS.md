# AGENTS.md

Instructions for AI coding agents working in this repository. This is the canonical
file; it is read directly by Codex, Cursor, Jules, Amp and others. Claude Code reads
`CLAUDE.md`, which imports this file.

Humans: see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Project

SpaceDonkey is a research repository exploring sustainable launch platforms, including
equatorial orbital ring concepts. It contains written research, generated figures, and
supporting tooling. Companion repository:
[AlphaClaw](https://github.com/PaulTiffany/AlphaClaw).

## Layout

| Path                 | Contents                                     |
| -------------------- | -------------------------------------------- |
| `docs/`              | Written research and documentation           |
| `docs/figures/`      | Generated SVG figures. **Never hand-edit.**  |
| `tools/figures/`     | The figure generator and its parameter files |
| `.github/workflows/` | CI                                           |

## Commands

```bash
# figures: regenerate after changing any parameter file
python tools/figures/ringgen.py --all
python tools/figures/ringgen.py --all --check   # what CI runs

# documentation
npx prettier@3.3.3 --write "**/*.{md,json,yml,yaml}"
npx markdownlint-cli2@0.13.0 "**/*.md" "#node_modules"
npx cspell@8.13.1 lint --no-progress "**/*.{md,py,json}"

# python
ruff check tools/ && ruff format tools/ && mypy tools/
```

Run all of these before opening a pull request. CI runs the same commands.

## Conventions

- **Figures are generated, never drawn.** Edit the parameter file under
  `tools/figures/params/`, then re-run the generator and commit both. A hand-edited SVG
  will be overwritten and will fail CI.
- **Do not generate engineering figures with image models.** They cannot represent an
  orbital radius and produce confident-looking diagrams whose annotations correspond to
  nothing. See [`docs/figures/README.md`](docs/figures/README.md).
- **Units belong in the identifier**: `altitude_km`, `radius_px`. Not optional.
- **Standard library by default** in Python. A new dependency needs a stated
  justification in the pull request.
- **Type annotations on everything.** `mypy --strict` is enabled.
- **New domain vocabulary goes in `project-words.txt`**, never an inline
  `cspell:disable` comment.
- **State claims and non-claims** for anything technical. An estimate is not a result; a
  schematic is not a design. Say which you have.

## Pull requests

The rule depends on the target branch.

### Targeting `main` — human gate required

1. **Open as a draft.** Always. GitHub does not permit merging a draft, so this is a
   mechanical stop, not an honour system.
2. **Fill in the attribution section** of the pull request template, declaring that an
   agent produced the changes and naming the tool.
3. **Stop there.** Do not mark it ready for review, do not request a review, do not
   merge, and do not tick the human review checkbox. That checkbox is a human's
   statement about their own reading of the diff. An agent ticking it makes the artifact
   a lie and defeats the control.
4. Say in the pull request description what you were unsure about. Uncertainty flagged
   early is cheaper than uncertainty discovered in review.

A human promotes the pull request from draft to ready for review.

### Not targeting `main` — go ahead

Working branches, stacked branches, scratch branches used as persistence or context
between sessions: agent-opened and agent-merged pull requests are fine. No draft
requirement, no human gate. Use them freely for checkpointing work.

The distinction is deliberate. `main` is the reviewed record. Everything else is scratch
space.

## Attribution

Every commit an agent authors carries a trailer:

```text
Co-authored-by: Claude <noreply@anthropic.com>
```

Substitute the tool that actually did the work. If a human wrote part of it, the human
is the commit author and the agent is the co-author. Do not omit the trailer, and do not
add it to commits an agent did not touch.

## Do not

- Merge to `main`, or approve a pull request targeting `main`
- Tick the human review checkbox
- Modify `.github/workflows/`, `CODEOWNERS`, or branch protection settings without a
  human explicitly asking in that session
- Add secrets, tokens, or credentials to the repository in any form
- Hand-edit anything in `docs/figures/`
- Rewrite published history on `main`
- Introduce a numeric parameter without a source or an explicit "placeholder" label

## When stuck

Say so in the pull request description rather than guessing. A draft with an honest open
question is more useful than a confident wrong answer, and this repository would rather
review uncertainty than discover it later.
