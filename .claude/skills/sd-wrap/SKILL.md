---
name: sd-wrap
description: End a session in SpaceDonkey and write the handoff. Use when wrapping up, handing off, or asked what is left. Covers flagging stale memory, naming what dangles, auditing the public surfaces, and the shape of .scratch/NEXT-SESSION.md.
---

# Wrapping a session

The output is `.scratch/NEXT-SESSION.md`. It is gitignored, so it is the one place that
may hold environment-specific detail: absolute paths, which commands are on `PATH`,
which address to commit as. Keep that detail out of everything committed, including this
directory.

Work through the five steps below, then write the file.

## 1. Flag what has gone stale

Drift lives in documents as much as in memory, and a wrong pointer is worse than a
missing one because it gets followed.

Go looking for:

- memory entries and handoff lines describing work that this session **finished**
- pointers to the previous session's task, especially anything named "next"
- superseded scratch documents and earlier handoffs
- claims that were true when written and are not now — a check that has since been
  fixed, a count that has moved, a file that has been renamed

**Propose deletion or archival. Do not silently rewrite history**, and do not delete
someone's record of a decision because the decision was reversed. The reversal is the
interesting part.

## 2. Name what is dangling

Everything this session started and did not finish, plus everything it created that
somebody now has to deal with: a draft pull request awaiting a human, an open question
raised in review, a branch that can be deleted, a backup file left somewhere.

A half-done thing named in the handoff is a task. A half-done thing not named in the
handoff is a trap.

## 3. Audit the public surfaces

This repository publishes to more places than it used to: the default branch, every
pushed branch, pull request bodies, review comments, issues, project board cards, and
the wiki. Anything reachable by someone who is not you is in scope.

Check that nothing from an unrelated context reached any of them. A grep of the default
branch alone is not the audit — it is the cheapest sixth of it.

Report the counts. "Clean across six surfaces" is a result; "looks fine" is not.

## 4. Check the pickup prompt names the next task

This is the step that has failed most often. The prompt at the top of the handoff gets
copied forward from the previous one and keeps describing the task that is now **done**.

Read the prompt you just wrote as though you had no other context. Does it name what the
next session is for, or what this one was for? If it names a task, does anything in the
threads contradict it?

Say explicitly which decisions are open and **whose** they are. An open question with a
named owner gets answered; an open question addressed to nobody gets rediscovered.

## 5. Name one workflow improvement

Exactly one, and a small one. Something that would have saved this session time, not a
reorganisation of how the project works.

The threshold for building it is the third time it comes up, not the first. Say which
time this is.

## The file

Write `.scratch/NEXT-SESSION.md` with these sections, in this order:

| Section          | Contents                                                                  |
| ---------------- | ------------------------------------------------------------------------- |
| Pickup prompt    | Paste-ready. Names the next task, the constraints, and what not to assume |
| Validation block | A runnable shell block, plus what each check should return                |
| Pull requests    | A row per pull request, its state, and who it is waiting on               |
| Threads          | The live work. Reasoning, not just status                                 |
| Open, lower      | Real but not urgent                                                       |
| Dangling         | From step 2                                                               |
| Improvement      | From step 5                                                               |

Two rules about the validation block, both learned the hard way:

- **Record the expected value beside each check**, so the next session can tell "still
  dirty at 52" from "newly dirty at 52". A check whose expected output is not written
  down cannot be failed.
- **Say when something is known-dirty or known-inert, and why it was left.** A check
  that fails every session and is meant to trains everyone to ignore the block. Mark it,
  and name whose decision it is.

Write the threads for someone with no memory of the conversation. State what was
decided, what was deliberately **not** decided, and the reasoning. A thread that records
only the current status will be re-argued from scratch, which is exactly what this file
exists to prevent.
