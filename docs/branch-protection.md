# Branch protection

The repository settings that a pull request cannot configure. These have to be set by
hand in **Settings → Branches → Add branch ruleset** (or the classic branch protection
UI). Until they are, the pull request policy is advisory.

## Threat model, stated honestly

A checkbox in a pull request body is an **attestation**, not a control. An agent with
write access can tick it. The `pr-policy` workflow makes the process legible and catches
honest mistakes, but it is not a security boundary.

Two things are actual controls:

1. **GitHub refuses to merge a draft pull request.** This is enforced by the platform.
   It is why agents are instructed to open as drafts — the stop is mechanical, not an
   honour system.
2. **Branch protection requiring a CODEOWNERS review.** A pull request cannot merge
   without an approving review from a human owner, regardless of what the body claims.

Everything else is process hygiene. Useful, but do not mistake it for a lock.

## Recommended ruleset for `main`

Target branch: `main`

| Setting                                | Value | Why                                                                                               |
| -------------------------------------- | ----- | ------------------------------------------------------------------------------------------------- |
| Require a pull request before merging  | on    | No direct pushes to the reviewed record                                                           |
| Required approvals                     | 1     | The human gate                                                                                    |
| Require review from Code Owners        | on    | Makes `CODEOWNERS` binding                                                                        |
| Dismiss stale approvals on new commits | on    | An approval covers the diff that was read, not later additions                                    |
| Require conversation resolution        | on    | Review comments cannot be silently ignored                                                        |
| Require status checks to pass          | on    | See list below                                                                                    |
| Require branches to be up to date      | on    | Checks ran against what will actually land                                                        |
| Block force pushes                     | on    | History on `main` is a record                                                                     |
| Restrict deletions                     | on    |                                                                                                   |
| Do not allow bypassing the above       | on    | Including for administrators. The point of a gate you set for yourself is that it applies to you. |

### Required status checks

Add these by name once the workflows have run at least once:

- `markdown format and lint`
- `spell check`
- `python lint and types`
- `figures match their parameters`
- `svg well-formed`
- `human gate for main`

## Working branches

Deliberately unprotected. Agent-opened and agent-merged pull requests between working
branches are permitted and encouraged as a persistence mechanism — a branch is a
reasonable place for an agent to checkpoint work across sessions.

`main` is the reviewed record. Everything else is scratch space, and the ruleset above
is what draws that line.

## What this does not cover: the wiki

Everything above governs this repository. The project wiki is a **different repository**
— `SpaceDonkey.wiki.git`, with its own history and its own default branch — and none of
it applies there.

GitHub wikis support no pull requests, no required reviews, no `CODEOWNERS`, no branch
protection, and no Actions. There is no gate to configure. Anyone with write access
publishes on save, and publishing has so far been done by one-shot workflows in this
repository pushing into the wiki.

That matters because of where the content sits. The ruleset above protects the plumbing,
the tooling and the figures. The architecture prose — the part making claims about the
world — currently lives entirely in the wiki, outside all of it. This is not presented
as a defect to be fixed here; it may well be the right trade for a surface whose whole
value is that a non-programmer can contribute to it. But it should be said out loud
rather than discovered later by someone who assumed the review gate covered the
research. See [`ownership.md`](ownership.md) for where that decision is being made.

One consequence worth acting on regardless of that decision: the repository `LICENSE`
grants CC BY 4.0 over material **"in this repository."** The wiki is not this
repository, and no wiki page carries a licence notice of its own. Until one is added,
the wiki content is unlicensed by default — all rights reserved — which is the opposite
of the intent expressed here.

## If you add agent write access

Should an agent ever get a token that can push here, tighten further:

- Give it a **fine-grained personal access token** or GitHub App installation scoped to
  this repository only, with `contents: write` and `pull-requests: write` and nothing
  else. Never `administration`.
- Do not grant it the ability to approve pull requests. GitHub already refuses to count
  a pull request author's own approval; do not work around that.
- Add `Restrict who can push to matching branches` and leave the agent identity off the
  list for `main`.
- Review the audit log for force pushes and ruleset changes periodically.

## Verifying

After configuring, the check is simple: open a draft pull request against `main`, tick
nothing, and confirm GitHub shows the merge button disabled and the
`human gate for main` check present. Then promote it, tick the review box, and confirm
the checks go green.
