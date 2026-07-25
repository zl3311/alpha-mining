---
id: "20260614-003"
date: "2026-06-14"
strategy: "EXPLORE_RESULT_MINING"
research_question: "Can current HF server state, recent sessions, and the V2 knowledge base reveal or revalidate at least one EXCELLENT+ alpha that passes BRAIN checks and self-correlation while new simulations are paused?"
budget_used: 10
budget_cap: null
trigger: "local manual autonomous alpha-mining session via Cursor"
gate_passers: 10
submissions: 0
submittable_candidates: 1
status: "productive"
tags:
  - "20260614-003"
  - "iv90_market_r1"
  - "iv90_vol_regime"
candidates:
  - id: "Gro21wWG"
    grade: "SPECTACULAR"
    sharpe: 2.59
    fitness: 4.33
    self_corr_value: 0.8802
    self_corr_result: "PASS"
    verdict: "SUBMITTABLE"
  - id: "RRrOjRdn"
    grade: "SPECTACULAR"
    sharpe: 2.75
    fitness: 4.63
    self_corr_value: null
    self_corr_result: "not_checked_concentration_fail"
    verdict: "BLOCKED_CONCENTRATED_WEIGHT"
  - id: "qMXa9XlP"
    grade: "SPECTACULAR"
    sharpe: 2.57
    fitness: 3.80
    self_corr_value: null
    self_corr_result: "not_checked_timeout"
    verdict: "FOLLOW_UP"
---

# Session 20260614-003

Local manual mining session started from the existing dirty workspace on
`review/20260614-draft-pr-distillation`. `git fetch origin` succeeded, but
branch-changing sync to latest `main` was skipped to avoid disturbing the
modified `server` submodule and existing uncommitted session/book artifacts.

## Phase 0 Context

STRATEGY: EXPLORE_RESULT_MINING

TARGET: Structurally novel candidates or stale/incomplete HF discoveries that can
be validated without submitting new simulations while the HF worker is paused.

BUDGET: No new simulations while HF reports `worker_status=paused_budget`.
Allocate effort to current server state, recent sessions, queued candidates, and
authoritative BRAIN checks.

CONSTRAINTS: Respect the novelty rule, avoid sparse fundamental2 `ts_zscore`,
avoid IV270/group-neutralized variants, avoid PV reversal, avoid `flag *
(-ret)`, and treat self-correlation via BRAIN `/check` as the binding gate.

RATIONALE: Active opportunity files are closed or submit-candidate records. Recent
sessions have exploited event/leverage/guidance/tax-benefit families, and the HF
worker is paused, so the productive local path is to mine existing server/book
state for EXCELLENT+ candidates with current validation rather than adding jobs to
a paused queue.

## Existing Result Mining

HF server state at session start: 33,749 results, 4,848 pending jobs, budget 3,995,
worker `paused_budget`. The canned `--gate-passers` query is stale for the current
server schema because it expects a removed `corr_result` column, so explicit SQL
queries were used for candidate mining.

### Revalidated / Blocked

- `pw7j2MXg`: EXCELLENT, all computable BRAIN checks pass, but current BRAIN
  self-correlation FAILS at 0.7414 vs active `0m8GV1Pp`. The older 0.412 queue
  record is stale after recent submissions.
- `mLX0gm5x`: SPECTACULAR, all computable checks pass, but current BRAIN
  self-correlation FAILS at 0.9977.
- `78dvZ3r2`: SPECTACULAR, all computable checks pass, but current BRAIN
  self-correlation FAILS at 0.9882.
- `zqWPX91o`, `pw7VQNjX`, `bl9opWAp`: SPECTACULAR IV90/buzz variants, blocked by
  `CONCENTRATED_WEIGHT`.
- `0mAraOA2`, `6XRKZNzG`: SPECTACULAR `fnd6_city` volatility-gated candidates,
  blocked by `CONCENTRATED_WEIGHT` and `LOW_SUB_UNIVERSE_SHARPE`.
- Older stored-low-correlation rows (`LLkkPMz2`, `MPkMnnbn`, `78J7rG7O`,
  `QPEZAWwW`) either failed current BRAIN self-correlation or returned
  non-actionable self-correlation errors/timeouts.

### Platform State Mismatch

BRAIN currently reports `d5Q3ZmWv`, `zqOrkbbG`, `xAn1LqXm`, and `0m8GV1Pp` as
ACTIVE, even though some local V2 book/queue records still show PENDING. Treat
BRAIN as authoritative for self-correlation and submission status.

## Phase 1 Fresh Batch

The HF worker resumed after a watchdog restart (`at_capacity`, budget 3,971), so a
small priority-9 batch was submitted.

Batch tag: `iv90_market_r1`

Settings: USA TOP3000, MARKET neutralization, platform decay 10.

1. `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), 10)`
2. `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 40)), 10)`
3. `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 60)), 10)`
4. `ts_decay_linear(zscore(ts_mean(implied_volatility_call_180 - implied_volatility_put_180, 22)), 10)`
5. `ts_decay_linear(zscore(ts_mean(implied_volatility_call_180 - implied_volatility_put_180, 40)), 10)`
6. `ts_decay_linear(zscore(ts_mean(implied_volatility_call_180 - implied_volatility_put_180, 60)), 10)`
7. `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)) + rank(ts_mean(scl12_buzz, 5)), 5)`
8. `trade_when(ts_std_dev(returns, 20) > 0.02, zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), ts_std_dev(returns, 20) < 0.01)`
9. `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)) + rank(historical_volatility_180), 5)`
10. `ts_decay_linear(zscore(ts_mean(implied_volatility_call_180 - implied_volatility_put_180, 22)) + rank(historical_volatility_180), 5)`

Mechanism: the prior multiplicative IV90/IV180 × buzz tree had very high fitness
but failed concentration. This batch keeps the successful IV zscore/ts_mean
template, changes to MARKET neutralization for decorrelation, and tests pure or
additive high-coverage variants intended to repair concentration.

## Phase 2 Results

The batch completed with 10/10 gate-passers and no expression failures. Pure IV90
zscore/ts_mean variants produced the highest aggregate fitness but failed
`CONCENTRATED_WEIGHT` at ~0.50. The volatility-regime gated IV90 expression
preserved SPECTACULAR quality while passing all computable BRAIN checks.

| Alpha | Grade | S | F | Turnover | BRAIN Checks | Self-Corr | Verdict |
|-------|-------|---|---|----------|--------------|-----------|---------|
| Gro21wWG | SPECTACULAR | 2.59 | 4.33 | 6.08% | ALL PASS | PASS 0.8802 | SUBMITTABLE |
| qMXa9XlP | SPECTACULAR | 2.57 | 3.80 | 9.20% | ALL PASS | timed out | FOLLOW-UP |
| pw72YJ8v | SPECTACULAR | 2.35 | 3.56 | 2.64% | ALL PASS | timed out | FOLLOW-UP |
| LLRvV6V1 | SPECTACULAR | 2.34 | 3.53 | 3.33% | ALL PASS | timed out | FOLLOW-UP |
| mLXGw2R2 | SPECTACULAR | 2.10 | 2.96 | 4.57% | ALL PASS | timed out / rate limited | FOLLOW-UP |
| RRrOjRdn | SPECTACULAR | 2.75 | 4.63 | 4.09% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |
| WjgZ1Evd | SPECTACULAR | 2.68 | 4.51 | 3.30% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |
| pw72Yqeq | SPECTACULAR | 2.57 | 4.14 | 5.52% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |
| qMXa90ev | SPECTACULAR | 1.83 | 2.69 | 5.80% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |
| O09LQAKv | EXCELLENT | 1.58 | 2.13 | 5.15% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |

## Final Candidate

`Gro21wWG` is a SPECTACULAR submittable alpha:

- Expression: `trade_when(ts_std_dev(returns, 20) > 0.02, zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), ts_std_dev(returns, 20) < 0.01)`
- BRAIN URL: https://platform.worldquantbrain.com/alpha/Gro21wWG
- Metrics: S=2.59, F=4.33, turnover 6.08%.
- Checks: all computable BRAIN checks PASS.
- Self-correlation: BRAIN `/check` returns PASS at 0.8802; this relies on the
  1.10x Sharpe-premium escape.

The alpha was recorded in `data/book/Gro21wWG.md`, queued in
`data/knowledge/opportunities/submit-gro21wwg.md`, and metadata was pushed to the
BRAIN platform with `scripts/brain_metadata.py` (metadata only, no official
submission).
