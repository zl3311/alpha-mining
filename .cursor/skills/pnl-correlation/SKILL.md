---
name: pnl-correlation
description: >-
  How to check self-correlation and submittability. Use before recommending any
  alpha for submission. Trigger on: correlation, self-corr, self-correlation,
  pnl, vs-book, decorrelation, brain-check, submittable.
---

# Self-Correlation Check

## BRAIN's Actual Self-Corr Model (confirmed)

BRAIN uses a **two-gate system**, not a single threshold:

1. **Gate 1**: Max correlation > **0.7** against any submitted alpha
2. **Gate 2**: If Gate 1 triggered, candidate Sharpe must be >= **1.10×** the
   max Sharpe among all peers with correlation > 0.7

If no peer exceeds 0.7 → auto-PASS. If peers exist above 0.7 but candidate
Sharpe clears the 10% premium → PASS (Sharpe premium override).

## Preferred Method: BRAIN API Check (authoritative)

```bash
# Get BRAIN's actual PASS/FAIL verdict (preferred — ground truth)
uv run python3 scripts/pnl_correlation.py --alphas <id1> <id2> --brain-check

# Longer wait under peak load (default is 900s = 15 min)
uv run python3 scripts/pnl_correlation.py --alphas <id1> --brain-check --max-wait-seconds 1800

# Get full correlation breakdown (which peers, their Sharpe)
uv run python3 scripts/pnl_correlation.py --alphas <id1> <id2> --brain-corr
```

`--brain-check` polls `GET /alphas/{id}/check` until `SELF_CORRELATION` is
terminal (`PASS` / `FAIL` / `ERROR`), then attaches peer detail from
`/correlations/self`. Typical payload when ready:
```json
{"name": "SELF_CORRELATION", "result": "PASS", "limit": 0.7, "value": 0.8241}
```
Note: `result: PASS` can coexist with `value > limit` when the Sharpe premium
is met. Always trust `result`, not `value` alone. Never treat `PENDING` as FAIL.

### Async lag and peak-load behavior

- `/check` long-polls like PnL: empty `200` + `Retry-After` means still computing.
- Off-peak resolve often takes ~1–9 minutes; under load, 20–90+ minutes and
  transient `HTTP 502` / `429` / `ConnectTimeout` are common (see sessions
  20260711–20260716). The CLI retries those and budgets `--max-wait-seconds`
  (default 900).
- `POST /alphas/{id}/check` returns **405** (as of 2026-07) — GET only.
- Submitted alphas: `/check` returns only `ALREADY_SUBMITTED` (no
  `SELF_CORRELATION`); use `/correlations/self` for peer corr.
- If the budget expires, the printer shows `TIMEOUT` and may list an
  `est` peer corr from `/correlations/self` — re-run later; do not invent FAIL.

See `data/knowledge/rules/self-corr-check-long-poll.md`.

`--brain-corr` queries `/alphas/{id}/correlations/self` which returns the full
peer breakdown: alpha ID, name, correlation, Sharpe, fitness, etc.

## Fallback Method: Local PnL Correlation

```bash
# Local PnL-based correlation (fallback pre-filter)
uv run python3 scripts/pnl_correlation.py --alphas <id1> --vs-book

# Server gate-passers with local PnL
uv run python3 scripts/pnl_correlation.py --from-server --vs-book
```

Downloads PnL from BRAIN API, computes Pearson correlation of daily returns
over a 4-year window. Useful as a cheap pre-filter but **underestimates**
BRAIN's actual self-corr by 1.45-1.6× when alphas share raw data fields.

See `data/knowledge/rules/self-corr-pnl-gap.md` for the calibration evidence.

### Local PnL Pre-Filter Thresholds

| Local PnL corr | Likely BRAIN verdict | Use as |
|----------------|---------------------|--------|
| < 0.50 | Almost certainly PASS | Quick pre-filter |
| 0.50 - 0.70 | Depends on shared fields and Sharpe premium | Must verify with `--brain-check` |
| > 0.70 | Likely triggers Gate 1; needs Sharpe premium | Must verify with `--brain-check` |

## Three Self-Corr Paths

| Path | When to use | Command |
|------|-------------|---------|
| **BRAIN API** (preferred) | Local manual, final verification | `--brain-check` or `--brain-corr` |
| **Server** (cloud) | Cloud agent sessions | `hf_query.py --gate-passers` (server calls BRAIN `/check` for gate-passers) |
| **Local PnL** (fallback) | Quick pre-filter, bulk screening | `--vs-book` |

## Greedy De-dup Procedure

When evaluating multiple candidates:

1. Sort by |Sharpe| descending
2. Keep first unconditionally
3. For each subsequent: run `--brain-check` — if PASS, keep
4. Remember: after submitting one alpha, the next check will re-evaluate
   against the updated book (the just-submitted alpha becomes a new peer)

### Long-Term Point Maximization: Submission Order

After de-dup identifies the "keep" set, the **submission order** matters for
maximizing cumulative account points over time:

- **Submit lowest self-corr candidates first.** Each submission adds a new peer
  to the book. A low-corr submission (e.g., 0.25) barely affects future checks,
  while a high-corr submission (e.g., 0.65) may block similar candidates later.
- **Only prioritize EXCELLENT+ candidates** (SPECTACULAR, EXCELLENT) — these
  justify the slot consumption with high per-alpha point yield.
- **Flag EXCELLENT+ with self-corr < 0.4 as "HIGH LONG-TERM VALUE"** — these
  are the best possible submissions: high points, minimal future constraint.
- Even barely-passing EXCELLENT+ alphas (self-corr just under 0.7) are worth
  submitting — points are points — but submit them AFTER lower-corr candidates
  in the queue to preserve optionality.

See `data/knowledge/rules/submission-priority-long-term.md` for the full rule.

## What Drives High Self-Corr

- Shared raw data fields (e.g., IV_270 spread) cause high position-level
  correlation even when PnL returns differ
- `flag * (-1 * returns)` is the #1 PnL driver across analyst revision alphas
- MARKET neutralization reduces cross-alpha correlation vs SUBINDUSTRY
