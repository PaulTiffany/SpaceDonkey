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
2. **The ruleset on `main` requiring an approving review.** A pull request cannot merge
   without one, regardless of what the body claims. GitHub does not let an author
   approve their own pull request, so this is what makes "two humans" real rather than
   attested.

`CODEOWNERS` is not on that list. It auto-requests a review from the owner, which is a
notification, not a gate. It only becomes a control if "require review from Code Owners"
is switched on, and it deliberately is not — see below.

Everything else is process hygiene. Useful, but do not mistake it for a lock.

## The ruleset on `main`

Configured 2026-09-04. Target branch: `main`. This section records what is actually set,
not a proposal — edit it if you change the settings, or the two will drift.

**Who configured it.** These settings were applied by an agent session — Claude Code,
[session record](https://claude.ai/code/session_01AvwZT6wQHRwjp9vDNc7DAJ) — acting with
a maintainer's credential at @derektiffany's direction. The organization audit log
attributes them to that maintainer's account, because GitHub cannot distinguish an agent
holding a credential from the person it belongs to. That is the same limitation that
removed the bypass below, and it is recorded here because the reviewed record is the
only place the difference can actually be stated. Anyone changing this ruleset should
say here who did it and how.

| Setting                                 | Value | Why                                                                                             |
| --------------------------------------- | ----- | ----------------------------------------------------------------------------------------------- |
| Require a pull request before merging   | on    | No direct pushes to the reviewed record                                                         |
| Required approvals                      | 1     | The human gate                                                                                  |
| Require review from Code Owners         | off   | Deliberate. `*` is @PaulTiffany, so `on` would make him a required reviewer on every change     |
| Dismiss stale approvals on new commits  | on    | An approval covers the diff that was read, not later additions                                  |
| Require conversation resolution         | on    | Review comments cannot be silently ignored                                                      |
| Require status checks to pass           | on    | See list below                                                                                  |
| Require branches to be up to date       | on    | Checks ran against what will actually land                                                      |
| Block force pushes                      | on    | History on `main` is a record                                                                   |
| Restrict deletions                      | on    |                                                                                                 |
| Anyone may bypass                       | off   | Nobody, admins included. See **Break glass** below                                              |
| Extra approval for unattributed commits | on    | GitHub default. A commit whose author email is not linked to an account needs a second approval |

### Break glass

There is **no standing bypass**. This is deliberate, and it is not only about
discipline: agents run with a maintainer's credential, and GitHub cannot tell an agent
holding that credential apart from the human it belongs to. A standing admin bypass is
therefore a standing agent bypass, which would make the gate inapplicable to the party
most likely to test it. Paul raised this on #6 and he was right.

So an override is not a click. It is a human editing this ruleset in **Settings →
Rules**, setting enforcement to `Disabled` or `Evaluate`, doing the thing, and putting
it back. That is deliberate, visible, and recorded in the organization audit log, which
is the point — the cost of an override should be that someone notices.

**When it is legitimate.** The test is that the cost of waiting for review exceeds the
cost of merging unreviewed. In practice:

1. **A secret or credential reached `main`.** Remove it now; rotate afterwards.
2. **Defacement, spam or malicious content on `main`.**
3. **A legal, licensing or takedown demand** with a deadline shorter than a review
   cycle.
4. **Runaway automation** — a workflow or agent burning resources or spamming, where
   landing a change is what stops it.

Two maintainers means one of them is sometimes asleep. That is a reason the route
exists; it is not by itself a reason to use it. "Nobody is around and I want this
merged" is not on the list.

**Whoever overrides writes it down** in the pull request description, in the Override
section of the template: which rule was relaxed, which of the reasons above applied, and
when enforcement went back on. The audit log records that the ruleset changed. It does
not record why, and the why is the part a human needs later.

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
repository, and no wiki page carries a license notice of its own. Until one is added,
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
