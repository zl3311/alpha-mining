---
name: hf-server
description: >-
  How to use the HF submission queue server for BRAIN simulations. Covers
  submitting jobs, querying results, polling, health checks, and priority
  rules. Trigger on: submit, server, HF, queue, hf_submit, hf_query.
---

# HF Submission Queue Server

## Server URL

Read from env `HF_SERVER_URL` (e.g. `https://<hf-user>-brain-submission-queue.hf.space`)

## Authentication

Requires `HF_TOKEN` and `HF_API_KEY` in `.env`.

## Submit Expressions

```bash
uv run python3 scripts/hf_submit.py --expressions "expr1" "expr2" --priority 5 --tags daily_20260603 session_013
```

Always tag with session ID for tracking.

## Query Results

```bash
uv run python3 scripts/hf_query.py --stats                                        # Server health
uv run python3 scripts/hf_query.py --gate-passers                                 # S>=1.0, F>=0.8 (default)
uv run python3 scripts/hf_query.py --gate-passers --min-fitness 1.0 --min-sharpe 1.25  # Strict (matches submission gates)
uv run python3 scripts/hf_query.py --new-24h                                      # Last 24h discoveries
uv run python3 scripts/hf_query.py --sql "SELECT ..."                             # Custom SQL
```

## Priority Rules

Higher number = processed first.

| Priority | Use |
|----------|-----|
| 0 | Background sweep (hands-off) |
| 3-5 | Normal session work |
| 6-10 | Urgent / time-sensitive |

## Rate Limits

The server has 3 concurrent BRAIN sim slots. Do NOT submit multiple batches simultaneously -- they compete for slots and trigger 429s. Submit one batch, wait for results, then submit the next.

## Health Check

Before submitting, run `--stats`. If `worker_status` is `paused_backoff` or budget is near zero, do not submit.

## Polling for Results

Use the canonical poller — do NOT write ad-hoc heredoc poll loops:

```bash
uv run python3 scripts/hf_poll.py --tag <session_tag>
uv run python3 scripts/hf_poll.py --tag <session_tag> --interval 60 --stale-min 12 --json
```

It polls until every tagged job is terminal (`done|failed|failed_permanent`),
flags STALE jobs (stuck in `running` past `--stale-min`), and prints a
gate-passer table on completion.

**Gate threshold note**: `hf_poll` uses stricter thresholds (S>=1.25, F>=1.0)
in its completion summary than `hf_query --gate-passers` defaults (S>=1.0,
F>=0.8). If the poll summary shows zero gate-passers, always double-check with
`hf_query --gate-passers --tag <tag>` at the default thresholds -- there may be
candidates worth inspecting between the two thresholds.

Or filter completed gate-passers directly:

```bash
uv run python3 scripts/hf_query.py --gate-passers --tag <session_tag>
```

### Realistic latency

A single sim averages ~2-3 minutes. BUT the background sweep keeps the queue
deep: when `/v1/stats` shows `pending_jobs` in the thousands, even priority-9
session jobs wait behind in-flight work and can take 10-30 min to drain. Size
your poll patience to the queue depth, not to a fixed "2-5 min". Submitting at
higher priority jumps the PENDING line but cannot preempt RUNNING jobs.

### WARNING != slow sim

If a job lingers, check its status. A BRAIN poll status of `WARNING` (or
`ERROR`/`FAILED`) is a terminal EXPRESSION error, not a slow simulation — most
often a FASTEXPR unit error (e.g. adding a unitless `rank()` to a price-unit
term). The server now marks these `failed_permanent` immediately. If you ever
see a job stuck in `running` for >12 min with `concurrent_running: 0` in stats,
it is a stale/zombie record — restart the Space with
`uv run python3 scripts/server_watchdog.py --restart`.

## Config

Default decay=6, neut=SUBINDUSTRY, universe=TOP3000. Override with `--decay`, `--neutralization`, `--universe`.
