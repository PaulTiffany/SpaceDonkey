---
name: sd-pr
description: Open a pull request in SpaceDonkey. Use when about to open, describe, or split a PR here. Covers the draft gate, the checkbox contract, pinned-version checks, and how to split a mixed PR.
---

# Opening a pull request

`AGENTS.md` has the policy. This is the working method, plus the things that have
actually gone wrong.

## Keep the body short

**The checkboxes do the mechanical work. The prose does not.** Aim for something that
fits on one screen.

Paul reviews these and is not a programmer — he was a contracts administrator. A long
body does not make a change more reviewable, it makes it less likely to be read. He has
asked for PRs to stay approachable, and for best-practice ceremony not to take over the
repository.

What earns its place in the body:

- one or two sentences on what changed
- anything you deliberately left out, and why
- anything you are unsure about
- claims and non-claims, when the change is technical

What does not: restating the diff, tables of every word you touched, or explaining
reasoning the code already shows. If you find yourself writing a third heading of
justification, the PR is either too big or the body is doing the diff's job.

This has gone wrong twice. Both times the fix was deleting two thirds of the body.

## The two boxes that matter

- **Open as a draft** when targeting `main`. Always. GitHub will not merge a draft, so
  it is a real stop rather than an honour system.
- **Never tick "I have reviewed my own changes."** It is a human's statement about their
  own reading of the diff. An agent ticking it makes the artifact a lie.

Tick the attribution box that is true, and name the tool.

## Merging takes two humans

`main` has a ruleset: pull request required, **one approving review**, the six CI checks
green, branch up to date, conversations resolved, no force pushes or deletions.

GitHub does not let an author approve their own pull request. So the checkbox is the
author's attestation and the required review is the second human. Repository admins can
bypass; that is deliberate, and using it should be rare enough to be worth mentioning.

`CODEOWNERS` is a notification mechanism here, not a control — it auto-requests a review
from the owner. The ruleset is the control. "Require review from Code Owners" is off on
purpose: with `*` assigned to @PaulTiffany it would turn that notification into a hard
block on every change. Leave it off unless a human asks.

## Run the checks at the pinned versions

Not newer ones. Two pull requests have now shipped check claims based on whatever
version `npx` resolved to, which is a guess wearing a tick mark.

```bash
npx -y prettier@3.3.3 --check "**/*.{md,json,yml,yaml}"
npx -y markdownlint-cli2@0.13.0 "**/*.md" "#node_modules"
npx -y cspell@8.13.1 lint --no-progress "**/*.{md,py,json}"
python3 tools/figures/ringgen.py --all --check
uvx ruff check tools/ && uvx ruff format --check tools/ && uvx mypy tools/
```

On this machine `python`, `ruff` and `mypy` are not on `PATH` — use `python3` and `uvx`.
A "command not found" here is a missing tool, not a failing check; do not report it as
either passing or failing.

If a check is genuinely not applicable, leave the box unticked and say why. An unticked
box with a reason is honest; a ticked box you did not verify is not.

## Splitting a mixed pull request

When a reviewer asks for concerns to be separated:

1. Branch from `origin/main`, not from the mixed branch.
2. Apply only the changes for one concern.
3. **Split by hunk, not by file, when a file straddles both.** A file-level split looks
   clean and can be wrong — one file held back wholesale left a flagged spelling error
   in the tree and would have shipped the "spelling fix" PR with a red spell check.
4. Prove there is no drift before opening:

   ```bash
   git diff origin/<original-branch> --stat -- <files you meant to carry>
   ```

   Only the files you intentionally held back should appear. Anything else is a change
   you made by accident, in content someone already approved.

5. Say in the body what you held back and where it went.

## House rules worth remembering

- **US English.** `cspell.json` loads `en_US`. British spellings are errors here, not
  vocabulary — fix the prose rather than growing the dictionary.
- **Commit identity is personal**: `derektiffany@live.com`, set repo-locally. The global
  git config points at a work address.
- **State claims and non-claims** for anything technical. An estimate is not a result.
- Never bundle a governance, workflow, or repository-settings change with a mechanical
  one. That is what caused the split above.
