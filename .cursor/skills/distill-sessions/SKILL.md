---
name: distill-sessions
description: Consolidate open draft mining session PRs into a single clean PR. Copies book entries, sessions, knowledge patterns, dead zones, and factors; deduplicates overlapping artifacts; verifies alpha statuses against BRAIN; runs bugbot iteratively; creates a consolidated PR; then closes the originals. Use when asked to "consolidate PRs", "distill sessions", "merge draft PRs", or "clean up mining PRs".
disable-model-invocation: true
---

# Distill Sessions

Consolidate accumulated draft mining-session PRs into one merge-ready PR.

## Phase 0: Inventory

```bash
gh pr list --state open --draft
```

Identify mining session PRs (branch prefixes: `session/`, `exp/`, `cursor/alpha-mining-session-*`).
Exclude non-session PRs (e.g. `feature/`, analysis scripts, infra).

For each PR, collect:
```bash
gh pr view <N> --json body,title,files --jq '{title, body, files: [.files[].path]}'
```

Build a manifest of artifacts to merge, grouped by type:
- `data/book/*.md`
- `data/sessions/*/`
- `data/knowledge/patterns/*.md`
- `data/knowledge/dead_zones/*.md`
- `data/factors/*.md`

## Phase 1: Create Branch

```bash
git checkout main && git pull origin main
git checkout -b chore/distill-draft-prs-<start_date>-<end_date>
```

## Phase 2: Copy Artifacts

For each file in the manifest:
```bash
git show origin/<branch>:<path> > <path>
```

Create directories as needed (`mkdir -p`).

**Conflict resolution**:
- Same file appears in multiple PRs → use version from latest session date
- File already exists on main → diff branch version against main, merge new content

## Phase 3: Deduplicate Knowledge

Scan new pattern files for overlap:
- Same template/mechanism family → merge into single file
- Preserve all learnings from both sources (anti-patterns, stabilizer tables, etc.)
- Add exclusivity rules when template variants have mutual corr > 0.85

## Phase 4: Verify Against BRAIN

```bash
uv run python3 scripts/brain_check.py --alpha-ids <space-separated IDs of all new book entries>
```

For each alpha, reconcile book entry with BRAIN source of truth:
- BRAIN says ACTIVE → set `status: "ACTIVE"` in book entry
- BRAIN says UNSUBMITTED → set `status: "PENDING"`
- Never use `CANDIDATE` (not a valid book status)

Then propagate implications:
- Update session metas: `submissions` count, `submitted` list, candidate `verdict` fields
- Fix stale novelty claims (e.g. "field X absent from book" when it's now ACTIVE)
- Mark sibling companions as BLOCKED if their primary variant is ACTIVE
  (template variants with mutual corr ~0.90-0.95 are mutually exclusive)

## Phase 5: Update Docs

```bash
uv run python3 scripts/parse_frontmatter.py --dir data/book --field status,grade 2>&1 | rg -o 'status=\w+' | sort | uniq -c
uv run python3 scripts/parse_frontmatter.py --dir data/book --field family 2>&1 | rg -o 'family=\w+' | sort -u | wc -l
```

Update `AGENTS.md` "Submitted alphas" line with fresh counts.
Do NOT update README (immutable superficial info only).

## Phase 6: Validate

```bash
uv run python3 -m pytest tests/ -q
uv run python3 scripts/parse_frontmatter.py --dir data/book --field status,grade
```

All tests must pass. All book entries must parse without error.

## Phase 7: Create PR

Stage, commit, push:
```bash
git add -A
git commit -m "chore: distill draft mining PRs <date_range>"
git push -u origin HEAD
```

Create PR with structured body (follow PR #67 format):
- New book entries table (Alpha, Grade, Sharpe, Fitness, Self-Corr, Family, Session)
- New sessions list
- Knowledge base additions (patterns, dead zones, factors)
- Merged branches list with PR numbers
- Verification results (test count, book entry count)

## Phase 8: Close Drafts

For each source PR:
```bash
gh pr close <N> --comment "Consolidated into #<new_pr_number>"
```

## Phase 9: Bugbot Loop

Run bugbot review on the branch diff. For each iteration:
1. Fix all high-severity findings
2. Fix medium-severity findings that are factual errors (stale claims, schema mismatches)
3. Accept medium findings that are historical session documentation (accurate at session time)
4. Amend commit, force-push, re-run bugbot
5. Stop when no new high-severity findings remain

## Known Gotchas

- `CANDIDATE` is not a valid book status — normalize to `PENDING`
- Session candidate schema uses `self_corr_value` / `self_corr_result` / `verdict` (not `self_corr`)
- Valid verdicts: `SUBMITTABLE`, `SUBMITTED`, `BLOCKED`, `BACKUP`
- Skill directory is `cloud-review` (not `session-review` as AGENTS.md hierarchy shows)
- After submitting one template variant, siblings are blocked (mutual corr 0.90-0.95)
- `format_email_digest.py` reads `self_corr_value` and `self_corr_result` from session candidates
- BRAIN API is the source of truth for alpha status — always verify before setting ACTIVE
