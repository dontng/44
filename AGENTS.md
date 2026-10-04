# Codex Handoff

This repository has two modes of work:

1. Project maintenance: code, scripts, data layout, and documentation.
2. Study and review: solve, explain, retrieve without hints, vary conditions, and revisit in mixed practice.

## Sync discipline

GitHub is the shared source of truth. At the start of any maintenance or study turn, sync the local work copy before making decisions. Do not turn study work into sync management unless the user asks.

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

## Current study architecture

The active teaching artifact is `src/MMDD-answer.md` beside its unchanged question sheet. Read `src/answer-quality/quality-gate.md`, `learning-system.md`, and the relevant dated context before teaching. Their checks govern i+1, executable first steps, fallback reasoning, complete option adjudication, and the difference between explanations and demonstrated mastery. Do not impose their headings on every question.

`daily-network/YYYY/MMDD.md` holds the original image and source plus independently checked explanation, closed-book recall, a meaningful condition change, and a small number of useful related questions. Never derive an answer from the index keyword alone: inspect the original image. All subquestions in a composite problem must be closed. Ambiguous assumptions must be stated and investigated; never invent a video author's answer.

Review starts with a question, not an exposed solution. Explanations and check answers may be folded; necessary reasoning must remain complete. Reuse a previously taught mechanism through an explicit reference and test the new boundary. Subsequent independent application can reinforce an earlier mechanism; avoid duplicate review queues for the same skill. Do not label a whole ability line mastered after solving one representative question.

Keep real first attempts in `data/answers`, `data/results`, and `data/progress` as historical evidence. Never overwrite them or infer the user's mental process from a choice. New attempts are append-only and dated; distinguish independent work, prompted completion, uncertainty, and failure. No records means unverified, never mastered. Old due dates and box numbers do not schedule current study.

Choice sheets end at 0908. From 0914 onward, each full written problem is indivisible, including its shared stem and every subquestion. Preserve `bank/` images, `data/written_markers.json` boundaries and historical crop sources. The existing 59 PDFs are question-sheet exports, not explanation exports.

`navigator/` and `draft/` are retired from main and retained at branch `archive/pre-review-20261004`. TLDR is historical teaching evidence, not a second active protocol. Do not restore retired planning, chapter-writing, or fixed-template tasks unless the user explicitly requests it.

Keep build tools from overwriting manually improved study pages. Validate data separately from page regeneration. For batches, inspect first and last questions at the same depth, verify local links and folds, commit only completed scoped work, and publish small batches to main. Maintain a truthful content progress record; files existing or scripts passing do not prove instructional correctness or user learning.

## Review delivery

`review/README.md` is the active review entry; `review/main.md` and `review/network.md` are generated navigation/recall aids, not duplicate solution books. Edit the 59 curated cards in `data/review_prompts.json`, then run `python tools/build_review.py`. Existing daily-network lessons are hand-authored; do not replace them with generic summaries.

Use `tools/review.py` only with actual observed attempts. Ask for the missing answer evidence instead of inferring it from reading or project completion. The new queue starts empty, deduplicates original question IDs, keeps complete written problems indivisible, and credits a named earlier question only with explicit independently demonstrated transfer. Its intervals and budgets are adjustable heuristics, not validated mastery scores or promises of never forgetting. Keep future dates and test examples out of real events.
