---
name: brain-check
description: >-
  How to check BRAIN alpha details and all 8 submission checks. Use after
  simulation to verify submission viability. Trigger on: check, BRAIN check,
  submission check, alpha check, IS check, all pass.
---

# BRAIN Alpha Check

## Usage

```bash
uv run python3 scripts/brain_check.py --alpha-ids ABC123 DEF456
uv run python3 scripts/brain_check.py --top 20
uv run python3 scripts/brain_check.py --top 20 --json  # Machine-readable
```

## CRITICAL: "ALL PASS" from `brain_check.py` is not self-corr clearance

`scripts/brain_check.py` reads `GET /alphas/{id}` (alpha detail). On that
payload, `SELF_CORRELATION` is often stuck at `PENDING` even after the
dedicated check endpoint has already resolved. `brain_check.py` only counts
explicit `FAIL`s, so its "ALL PASS" / `f=0` summary can report success while
self-corr is still unverified. NEVER read "ALL PASS" as "self-corr is fine."

For authoritative self-corr, poll `GET /alphas/{id}/check` via:

```bash
uv run python3 scripts/pnl_correlation.py --alphas <id> --brain-check
```

That path waits for a terminal `PASS` / `FAIL` / `ERROR` (not `PENDING`). See
the `pnl-correlation` skill and `data/knowledge/rules/self-corr-check-long-poll.md`.

## The `/check` Endpoint

**Endpoint**: `GET /alphas/{id}/check` (GET only — `POST` returns **405**)

Returns the authoritative PASS/FAIL for all 8 submission checks once ready.
Each check includes:

- `result`: `PASS`, `FAIL`, `PENDING`, or `ERROR`
- `value`: the measured value (e.g. correlation coefficient for SELF_CORRELATION)
- `limit`: the threshold (e.g. 0.7 for SELF_CORRELATION)

While computing, BRAIN may return empty `200` + `Retry-After` (long-poll).
Under peak load this can take many minutes; also expect transient 502/429.
Submitted alphas typically return only `ALREADY_SUBMITTED` here (no
`SELF_CORRELATION` row) — peer corr still comes from `/correlations/self`.

**Important**: For SELF_CORRELATION, `result: PASS` can coexist with
`value > limit` when the **Sharpe premium escape** is met (candidate Sharpe
>= 1.10x the max Sharpe among correlated peers). The `result` field is
authoritative — trust it over comparing `value` vs `limit` manually.

### Related Endpoints

| Endpoint | Purpose | Free-tier |
|----------|---------|-----------|
| `/alphas/{id}/check` | Authoritative 8-check PASS/FAIL | Yes |
| `/alphas/{id}/correlations/self` | Full self-corr breakdown vs book | Yes |
| `/alphas/{id}/correlations/prod` | Correlation vs production alphas | **403** |

## The 8 Submission Checks

All must show PASS for a successful submission.

| Check | What it means | Limit | If it FAILS |
|-------|--------------|-------|-------------|
| LOW_SHARPE | Sharpe ratio too low | min 1.25 | Expression is too weak. Try different factors. |
| LOW_FITNESS | Fitness too low | min 1.0 | Usually turnover too high. Add ts_decay_linear or increase decay. |
| LOW_TURNOVER | Turnover too low | min 0.01 | Signal too stable (e.g., slow fundamental). Rare problem. |
| HIGH_TURNOVER | Turnover too high | max 0.70 | Signal changes too fast. Add ts_decay_linear, increase decay, use ts_mean. |
| CONCENTRATED_WEIGHT | Weights too concentrated | max 0.10 | Sparse data creates heavy bets. Simplify blend, add high-coverage factor, or switch universe. |
| LOW_SUB_UNIVERSE_SHARPE | Sub-universe Sharpe too low | ~43% of overall | Signal doesn't work in sub-groups. Add scl12_buzz stabilizer (100% coverage). |
| SELF_CORRELATION | Too correlated with existing alphas | 0.7 (+ 1.10x Sharpe premium escape) | Change signal family entirely. Try MARKET neut. Even above 0.7, can PASS if Sharpe >= 1.10x peer. See `pnl-correlation` skill. |
| MATCHES_COMPETITION | | must pass | Rarely fails. Expression too similar to public examples. |

## Yearly Breakdown

Always check the yearly breakdown on the platform after simulation. A signal can pass aggregate checks but have one terrible year. Look at the yearly stats on the platform URL.

## Platform URL Format

`https://platform.worldquantbrain.com/alpha/{alpha_id}`
