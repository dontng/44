# Codex Handoff

This repository has two modes of work:

1. Project maintenance: code, scripts, data layout, and documentation.
2. Study and review: solve, explain, retrieve without hints, vary conditions, and revisit in mixed practice.

## Opt-in reference archives: answer and answer-quality

`src/answer/` and `src/answer-quality/`, including every file and subdirectory beneath them, are retained reference archives. They are not default teaching instructions, required reading, or an authority for judging new answers.

- By default, do not open, read, search, summarize, index, or load their contents into context. Exclude both directories from broad repository content searches and automatic context gathering. A link to an archived file does not authorize following it.
- Consult archived content only when the user explicitly requests it, or after proposing a specific reference and receiving the user's agreement. A proposal alone is not permission. Read only the agreed files for the agreed purpose; permission is not permanent for the whole archive.
- Develop new answers and assess their quality from the current user requirements, original question, and independent reasoning. Do not import archive-derived rules, remembered summaries, conclusions, templates, or judgments as default requirements.
- Preserve these files and the user's chosen locations. Explicitly requested file maintenance may use paths, metadata, hashes, and existing Git blob references without exposing or interpreting archived prose. Do not scan the archives merely to verify this policy.
- This rule supersedes older mandatory-reading guidance in repository documents, archived material, and remembered project workflows. Other documents' reference links remain optional and do not reinstate priority.

## Sync discipline

GitHub is the shared source of truth. At the start of any maintenance or study turn, sync the local work copy before making decisions. Do not turn study work into sync management unless the user asks.

For this repository, the user has granted standing permission to publish completed work. When a task is clear, its scoped changes are complete, and relevant checks pass, commit and push directly to the current shared branch without asking for a separate `commit` or `push` instruction. Keep work local only while it is incomplete, unverified, blocked, or the requested scope is genuinely ambiguous. Never use this standing permission to include unrelated changes.

The scheduled safety net is the sole automatic exception: `tools/autocommit.sh` runs at 02:00 and 20:00 local time. A recovery commit is created only when both conditions hold: a scheduled time has arrived and the worktree has changes. Before committing, it waits for ten minutes without project activity; agents refresh the ignored activity marker with `bash tools/mark-activity.sh` at the start of active project work and before long operations, while direct file edits are detected from their modification time. The wait has a hard cutoff: 04:00 for the 02:00 run and 21:00 for the 20:00 run; at that cutoff it commits even if activity continues, except that an in-progress Git operation must finish first. It then pushes one checkpoint containing all non-ignored changes. Its purpose is off-machine recovery, not normal delivery; agents and workflow commands must not invoke it early or treat a changed worktree as permission for an immediate commit.

## Agent commit standard

Agent-created commits are collaborative records, not opaque user commits. Attribution depends on the publishing path:

- For a local Git commit, keep the configured agent identity as the commit author and add the user as co-author.
- When a connected GitHub interface necessarily records the user as the commit author, do not repeat the user as co-author. Instead, identify the agent in the commit body and add the agent as co-author.

Use the applicable trailer, never both for the same person, and always match the actual agent performing the commit:

```text
Co-authored-by: dontng <djology.w@icloud.com>
Co-authored-by: Codex <codex@openai.com>
Co-authored-by: Gemini <176961590+gemini-code-assist[bot]@users.noreply.github.com>
```

When `dontng` is recorded as the commit author:
- For commits completed by **Codex**, include `Generated with Codex` immediately before `Co-authored-by: Codex <codex@openai.com>`.
- For commits completed by **Antigravity / Gemini**, include `Generated with Antigravity` immediately before `Co-authored-by: Gemini <176961590+gemini-code-assist[bot]@users.noreply.github.com>` (which resolves on GitHub to Google's official `gemini-code-assist[bot]` account and Gemini avatar; never use `antigravity@google.com` or `noreply@google.com`, and never misattribute Gemini work to Codex).

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

Start study and answer-writing work from the current user request and original question sheet in `src/`. Existing answer pages and quality notes remain in the opt-in archives described above; they are not prerequisites for teaching, writing, or review. Follow the current task requirements without automatically applying archived protocols.

`daily-network/YYYY/MMDD.md` holds the original image and source plus independently checked explanation, closed-book recall, a meaningful condition change, and a small number of useful related questions. Never derive an answer from the index keyword alone: inspect the original image. All subquestions in a composite problem must be closed. Ambiguous assumptions must be stated and investigated; never invent a video author's answer.

Review starts with a question, not an exposed solution. Explanations and check answers may be folded; necessary reasoning must remain complete. Reuse a previously taught mechanism through an explicit reference and test the new boundary. Subsequent independent application can reinforce an earlier mechanism; avoid duplicate review queues for the same skill. Do not label a whole ability line mastered after solving one representative question.

Keep real first attempts in `data/answers`, `data/results`, and `data/progress` as historical evidence. Never overwrite them or infer the user's mental process from a choice. New attempts are append-only and dated; distinguish independent work, prompted completion, uncertainty, and failure. No records means unverified, never mastered. Old due dates and box numbers do not schedule current study.

Choice sheets end at 0908. From 0914 onward, each full written problem is indivisible, including its shared stem and every subquestion. Preserve `bank/` images, `data/written_markers.json` boundaries and historical crop sources. The redundant src/pdf exports have been removed at the user's request; do not regenerate them unless requested.

`navigator/` and `draft/` are retired from main and retained at branch `archive/pre-review-20261004`. TLDR is historical teaching evidence, not a second active protocol. Do not restore retired planning, chapter-writing, or fixed-template tasks unless the user explicitly requests it.

Keep build tools from overwriting manually improved study pages. Validate data separately from page regeneration. For batches, inspect first and last questions at the same depth, verify local links and folds, commit only completed scoped work, and publish small batches to main. Maintain a truthful content progress record; files existing or scripts passing do not prove instructional correctness or user learning.

### Deep teaching & explanation standard

When explaining problems or reviewing conceptual friction:
- Address the counter-intuitive friction first: directly state why the learner naturally falls into the trap instead of reciting formal definitions.
- Ban superficial analogies and psychological guessing: avoid everyday life metaphors and avoid speculating about the examiner's motives; analyze the naked mathematical, architectural, and algorithmic mechanics directly.
- Ban utilitarian slogans and hollow formulas: eliminate gimmicky phrasing like "十秒看破", "秒杀", or mechanical tricks that degrade into empty templates; keep explanations sober, pragmatic, and strictly grounded in the problem's mechanics.
- Ban unnecessary formalisms and jargon: explain naturally in plain human language ("说人话"); avoid piling up heavy mathematical symbols (like $\sum$ summation notation) or pseudo-academic buzzwords ("降维坍缩", "互逆抵消", "跨步") when concrete code iteration and intuitive arithmetic make the underlying principle immediately obvious.
- Anchor twin past-exam contrasts side-by-side in a table: pair the confusing problem against its classic counterpart (e.g. 2014-01 vs 2022-01) where code is nearly identical except for the single decisive variable.
- Provide a closed decision model rather than piece-meal enumeration: give the learner the overarching physical invariant so they never have to exhaustively enumerate edge cases.

## Retired components

`navigator/`, `draft/`, `review/`, `tldr/`, `paper_html/`, and `daily-network/2025/` are retired from main and retained in Git history. Do not restore retired planning, flashcard reviews, chapter-writing, or fixed-template tasks unless the user explicitly requests it.
