# Codex Handoff

This repository has two modes of work:

1. Project maintenance: code, scripts, data layout, and documentation.
2. TLDR study: turning real 408 attempts into usable mechanisms, verification, and transfer.

## Sync discipline

GitHub is the shared source of truth. At the start of any maintenance or TLDR turn, sync the local work copy before making decisions. Do not turn study work into sync management unless the user asks.

For this repository, the user has granted standing permission to publish completed work. When a task is clear, its scoped changes are complete, and relevant checks pass, commit and push directly to the current shared branch without asking for a separate `commit` or `push` instruction. Keep work local only while it is incomplete, unverified, blocked, or the requested scope is genuinely ambiguous. Never use this standing permission to include unrelated changes.

The scheduled safety net is the sole automatic exception: `tools/autocommit.sh` runs at 02:00 and 20:00 local time. A recovery commit is created only when both conditions hold: a scheduled time has arrived and the worktree has changes. Before committing, it waits for ten minutes without project activity; agents refresh the ignored activity marker with `bash tools/mark-activity.sh` at the start of active project work and before long operations, while direct file edits are detected from their modification time. The wait has a hard cutoff: 04:00 for the 02:00 run and 21:00 for the 20:00 run; at that cutoff it commits even if activity continues, except that an in-progress Git operation must finish first. It then pushes one checkpoint containing all non-ignored changes. Its purpose is off-machine recovery, not normal delivery; agents and workflow commands must not invoke it early or treat a changed worktree as permission for an immediate commit.

## Agent commit standard

Agent-created commits are collaborative records, not opaque user commits. Attribution depends on the publishing path:

- For a local Git commit, keep the configured agent identity as the commit author and add the user as co-author.
- When a connected GitHub interface necessarily records the user as the commit author, do not repeat the user as co-author. Instead, identify the agent in the commit body and add the agent as co-author.

Use the applicable trailer, never both for the same person:

```text
Co-authored-by: dontng <djology.w@icloud.com>
Co-authored-by: Codex <codex@openai.com>
```

For GitHub-interface commits completed by Codex, include `Generated with Codex` immediately before the Codex trailer. This mirrors agent-assisted commit attribution without claiming that Codex is a linked GitHub account.

Every commit message must contain a specific subject and these non-empty sections:

```text
<area>: <completed result>

Implemented:
- files and behavior changed

Why:
- problem or learning/workflow effect addressed

Verified:
- checks run, or why no automated check applies
```

Before committing, inspect the staged diff and stage only work in scope. Install the repository commit policy with `bash tools/setup-git-policy.sh`; it supplies the template and rejects messages without the required implementation, rationale, and verification sections.

## Question-chain and TLDR architecture

`src/MMDD.md` contains the current ability-line question chain. `tldr/README.md` is the authority for analysis quality; `tldr/TEMPLATE.md` fixes the minimum per-question shape, and completed analysis lives under `tldr/sessions/YYYY-MM/MMDD-tldr.md`.

Interactive teaching has a separate calibration source under `src/answer-quality/`. Before explaining questions from `src/MMDD.md`, read `src/answer-quality/quality-gate.md` and the relevant dated context when it exists; use the adjacent `src/MMDD-answer.md` as the study artifact and concrete calibration. The context files preserve the useful teaching dialogue without copying its noise. They govern explanation order, scope, error handling, and presentation; do not force interactive answers into the TLDR structure or infer the user's reasoning from a historical choice.

The sealed choice chain ends at `0908`. Files from `0914` onward are large-question lines built from `data/written_lines.json`. A large question is an indivisible attempt unit: do not distribute its subquestions across dates. `data/written_markers.json` is the reviewed 2009—2025 boundary table; historical crops listed there must be preserved, and all other images must close at the next question marker (with cross-page stitching where needed).

For a study turn, read only:

```text
tldr/README.md
data/question_chain.json
data/results/MMDD.json
src/MMDD.md
tldr/sessions/YYYY-MM/MMDD-tldr.md  # when continuing an existing session
```

The user's first attempt is evidence and must never be overwritten. Independently solve and diagnose before consulting the reference answer. Build only the mechanism needed to read the problem, adjudicate every option, and survive a nearby change of conditions. Use external authority to settle facts or boundaries, not to display research.

After a complete `data/results/MMDD.json` exists, create the analysis scaffold with `./tldr.sh MMDD`. A generated `draft` is not a study state and must not be delivered. After every question is independently closed, run `./tldr.sh --check MMDD`; treat a passing structural check as necessary but not sufficient, then perform the protocol's content review.

Writing an explanation can advance a problem only to `explained`. Advance it to `verified`, `transferred`, or `automatic` only after the corresponding user performance exists. Never ask whether the user understood; design the cheapest falsifiable check instead.

The tenth problem in a batch receives the same standard as the first. If that quality cannot fit in one pass, split the delivery and preserve explicit progress rather than compressing later problems.
