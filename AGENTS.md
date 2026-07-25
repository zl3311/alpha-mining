# AGENTS.md

Rules and context for any AI agent working in this repository.

> **Historical document.** This is the operating manual the agent read at the start of every
> one of the 63 mining sessions recorded in `data/sessions/`. It is preserved as written,
> because it *is* the methodology — the instructions below are what produced the archive.
> The project is now archived and the infrastructure it refers to (the submission queue
> server, the scheduled automation, the BRAIN account) no longer exists. Read it as a record
> of how the system operated, not as instructions to follow. See `README.md` for orientation
> and `POSTMORTEM.md` for what happened.

## Project Identity

This is an **LLM-driven alpha mining pipeline** for the WorldQuant BRAIN platform.
It discovers, tests, and evaluates formulaic trading alphas using BRAIN's backtest
infrastructure. The goal is to **maximize BRAIN points and ranking** through
economics-driven, experiment-driven alpha generation.

**Submitted alphas**: 53 ACTIVE + 11 PENDING across 60 mechanism families (22 SPECTACULAR, 37 EXCELLENT, 1 GOOD, 4 AVERAGE). Run `uv run python3 scripts/parse_frontmatter.py --dir data/book --field status,grade,family` for counts straight from `data/book/`.
**Self-corr wall**: BRAIN threshold is 0.7 correlation + 1.10x Sharpe premium escape. Book is near saturation in the positive direction; negation direction opens 5x more independent dimensions (see `direction-diversification` pattern). Strategy is EXPLORE-first (negated building blocks, novel templates, and cross-family interactions).
**Submission strategy**: Maximize cumulative account points long-term. When multiple submittable candidates exist, submit lowest self-corr first (preserves correlation headroom for future alphas). Only EXCELLENT+ candidates warrant prioritized promotion. Flag EXCELLENT+ with self-corr < 0.4 as HIGH LONG-TERM VALUE — these contribute the most points per unit of correlation budget consumed.
**Autonomous session goal**: "Submittable" means the FIRST candidate that clears all gates (grade threshold + 8 BRAIN checks + self-corr PASS). Autonomous sessions should SATISFICE, not optimize — stop iterating as soon as a viable candidate is found. Do not burn additional budget searching for a marginally better alpha. The exception is when the user explicitly requests multiple candidates or specifies a budget to exhaust.

**Key URLs:**
- BRAIN platform: https://platform.worldquantbrain.com
- HF submission server: read from `$HF_SERVER_URL` (see `.env.example`)
- BRAIN account credentials live in `.env` (never commit)

## How to Start Any Mining Session

**Read the `mining-session` skill** (`.cursor/skills/mining-session/SKILL.md`).
It is the master orchestrator that chains all other skills in the correct order.

The skill hierarchy:

```
mining-session            <- Entry point for MINING (cloud or local)
├── context-gather        <- Phase 0: read state, pick strategy
├── signal-generation     <- Phase 1: generate candidates (HYPOTHESIS/EXPLORE/RECOMBINE/EXPLOIT/REFINE)
│   └── econ-reasoning    <- Mechanism analysis (referenced during HYPOTHESIS mode)
├── hf-server             <- Phase 2: submit to HF queue, poll results
├── result-analysis       <- Phase 3: filter, BRAIN checks, self-corr
│   ├── brain-check       <- 8 submission checks
│   └── pnl-correlation   <- Self-corr vs book
├── experiment-reporting  <- Phase 4: record, update knowledge, open PR
└── alpha-mining          <- Reference: operator syntax, CLI commands, sim settings

cloud-review              <- Entry point for REVIEW (cloud and local, on-demand)
├── (cloud PRs: scripts/weekly_review.py; local: data/sessions/ + transcripts)
└── trace-analysis        <- Deep dive into a single session (cloud or local)
    └── (cloud: scripts/audit_cloud_trace.py; local: agent-transcripts/*.jsonl)

distill-sessions          <- Consolidate draft mining PRs into one merge (on-demand)
```

## Two execution paths

The repository contains two independent ways to reach BRAIN. Confusing them is the most
common source of wrong assumptions about this codebase.

**1. The agent mining loop (what produced everything in `data/`).** Skills orchestrate
`scripts/hf_submit.py` → `hf_poll.py` → `hf_query.py` → `brain_check.py` /
`pnl_correlation.py`, with the submission queue server doing the actual BRAIN calls.
State lives in frontmatter markdown under `data/`. All 63 archived sessions used this
path. It never touches SQLite.

**2. The orchestrator CLI (`python3 -m alpha_mining`).** A direct-to-BRAIN path for
one-off expression tests (`--expression`), the local rank-IC prescreener (`--screen`),
and the paper-ingestion pipeline (`--ingest`, `--pdf`, `--batch`). This path **does**
persist to SQLite at `data/alpha_mining.db` via `src/alpha_mining/storage/`, and it
labels alphas on BRAIN automatically. It played no part in the archived mining work.

Neither path is dead code, but they do not share state. Earlier revisions of this file
described `storage/` as "legacy, not used" — that is true of path 1 and wrong for path 2.

## Data Layout (V2)

```
data/
├── sessions/           # One dir per mining session (each PR = one session)
├── factors/            # One frontmatter MD per discovered factor
├── book/               # One frontmatter MD per submitted alpha
├── knowledge/
│   ├── rules/          # Hard constraints (never violate)
│   ├── dead_zones/     # Don't explore again
│   ├── patterns/       # Proven techniques
│   ├── opportunities/  # Promising ideas to test next (+ submit-*.md submission queue)
│   └── factor_profiles/ # Per-field simulation profiles (bulk analysis output, ~1600 files)
└── reference/          # Static: papers, data catalog, operator ref, platform constraints
```

All data files use **frontmatter markdown**: structured YAML header + prose body.
Greppable, parseable by `scripts/parse_frontmatter.py`, human-readable in PRs.

Query examples:
```bash
uv run python3 scripts/parse_frontmatter.py --book-ids              # List submitted alpha IDs
uv run python3 scripts/parse_frontmatter.py --dir data/book --field grade,sharpe,fitness
uv run python3 scripts/parse_frontmatter.py --dir data/factors --filter "status=active" --field field,family
```

## Known Gotchas

### Operator naming (will cause HTTP 400 if wrong)
| Wrong | Correct |
|-------|---------|
| `delay(x, d)` | `ts_delay(x, d)` |
| `correlation(x, y, d)` | `ts_corr(x, y, d)` |
| `ts_argmax(x, d)` | `ts_arg_max(x, d)` |
| `ts_argmin(x, d)` | `ts_arg_min(x, d)` |
| `delta(x, d)` | `ts_delta(x, d)` |
| `stddev(x, d)` | `ts_std_dev(x, d)` |
| `decay_linear(x, d)` | `ts_decay_linear(x, d)` |

### Platform quirks
- **Free tier is USA-only** -- EUR, ASI, JPN, CHN, KOR, GLB all return "Region not available"
- **"Needs Improvement"** on BRAIN means sub-period inconsistency, not aggregate failure
- **Fitness formula**: `sqrt(abs(returns) / max(turnover, 0.125)) * sharpe`
- **BRAIN API submit returns broken http:// redirect** -- use follow_redirects=False

### Code changes
- Run `uv run python3 -m pytest tests/ -q` after any code change
- All tests must pass before committing
- Test files go in `tests/` with `test_` prefix

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/hf_submit.py` | Submit expressions to HF server |
| `scripts/hf_query.py` | Query server stats, gate-passers (`--tag`), custom SQL |
| `scripts/hf_poll.py` | Poll a tagged batch to completion; flags stale jobs |
| `scripts/brain_check.py` | Check BRAIN alpha details and 8 submission checks |
| `scripts/brain_metadata.py` | Set alpha name/tags/description on BRAIN (no submit) |
| `scripts/pnl_correlation.py` | PnL self-correlation vs submitted book |
| `scripts/parse_frontmatter.py` | Query frontmatter markdown files |
| `scripts/server_watchdog.py` | HF Space health check / restart |
| `scripts/sync_server_book.py` | Sync `data/book/` ACTIVE entries to HF server `submitted_book` |
| `scripts/audit_cloud_trace.py` | Pull cloud agent trace, produce audit summary |
| `scripts/weekly_review.py` | Aggregate weekly cloud-agent PR audits into digest |
| `scripts/format_email_digest.py` | Format session meta.md into email subject/HTML (was driven by GHA) |

### Cloud agent audit (GHA) — removed in the public archive

While the project was live, three GitHub Actions workflows drove the automation:
`audit-cloud-trace.yml` (detected cloud-agent PRs by their `cursor.com/agents/bc-*`
footer, pulled the SSE trace via the Cursor API, posted an audit comment, and archived
the trace to HF storage), `nightly-context-sync.yml`, and `hourly-pnl-backfill.yml`.

All three were **deleted before publishing**: they run on a schedule against private
infrastructure that no longer exists, so on a public repo they would only produce
failing runs. `scripts/audit_cloud_trace.py` and `scripts/weekly_review.py` remain and
still work if you wire up your own automation.

**Secrets those workflows expected** (set under Settings → Secrets and variables → Actions):
- `CURSOR_API_KEY` — Cursor API key for trace access (generate at cursor.com/dashboard)
- `HF_TOKEN` — HuggingFace token for trace upload to a `<hf-user>/alpha-mining-traces` storage bucket
- `HF_API_KEY` — queue server API key for book sync and query access
- `RESEND_API_KEY` — Resend API key for email digest notifications
- `NOTIFICATION_EMAIL` — recipient email for session digest notifications

### HF queue path requires an explicit metadata step

Alphas simulated via the HF queue exist on the BRAIN platform but are
**unlabeled** (no name/tags/description) — unlike the direct `run_expression`
path which labels on completion. After result-analysis, push metadata for any
submission candidate with `scripts/brain_metadata.py` (metadata only; never
submits). A local `data/book/<id>.md` does NOT propagate to the platform.

## File Layout

```
alpha_mining/
├── AGENTS.md                    # This file
├── .cursor/skills/              # 13 skills (see hierarchy above)
├── data/                        # All artifacts (see Data Layout above)
├── src/alpha_mining/            # Python source
│   ├── brain/                   # BRAIN API client
│   ├── llm/                     # LLM provider + prompts
│   ├── local/                   # FASTEXPR parser + local prescreener
│   ├── storage/                 # SQLite DB (used by the orchestrator CLI, not the agent loop)
│   ├── pipeline/                # Paper ingestion pipeline
│   └── orchestrator.py          # CLI entry point
├── scripts/                     # Operational scripts
├── server/                      # HF submission queue (git submodule)
├── tests/                       # Test suite
└── context/                     # Project background docs
```
