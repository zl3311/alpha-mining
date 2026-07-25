---
id: "20260614-001-results"
session: "20260614-001"
total_expressions: 22
gate_passers: 2
best_sharpe: 1.39
best_fitness: 3.06
best_alpha_id: "JjdJxrnx"
---

# Results: Session 20260614-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 22 |
| Gate-passers | 2 |
| Submittable candidates | 1 revalidated existing queue candidate |
| Submissions | 1 (`xAn2kvOp`) |
| Best Sharpe | 1.39 |
| Best Fitness | 3.06 |
| Strategy | EXPLOIT |

## Gate-Passers

| Alpha ID | Expression | Sharpe | Fitness | Turnover | Family | Verdict |
|----------|------------|--------|---------|----------|--------|---------|
| JjdJxrnx | `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)` | 1.39 | 3.06 | 10.0% | fundamental2_tax_benefit_leverage | BLOCKED: `CONCENTRATED_WEIGHT` 0.50 vs 0.10 |
| pw7e5w06 | `rank(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 63), 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)` | 1.39 | 3.06 | 10.0% | fundamental2_tax_benefit_leverage | BLOCKED: `CONCENTRATED_WEIGHT` 0.50 vs 0.10 |

## BRAIN Check Results

| Alpha ID | Grade | Sharpe | Fitness | Concentration | Sub-Universe | Verdict |
|----------|-------|--------|---------|---------------|--------------|---------|
| RRroP5ra | SPECTACULAR | 4.10 | 10.75 | FAIL 0.50 / 0.10 | FAIL -1.95 / 2.17 | Raw anchor blocked |
| JjdJxrnx | SPECTACULAR | 1.39 | 3.06 | FAIL 0.50 / 0.10 | PASS 1.39 / 0.60 | Blocked |
| pw7e5w06 | SPECTACULAR | 1.39 | 3.06 | FAIL 0.50 / 0.10 | PASS 1.39 / 0.60 | Blocked |

## Other Fresh Candidates Checked

| Alpha ID | Expression | Main Failures |
|----------|------------|---------------|
| le0YNxQ5 | `ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 22)` | `CONCENTRATED_WEIGHT` 0.50 |
| npWl5kpx | `-ts_zscore(fn_goodwill_acquired_during_period_a, 63)` | low Sharpe, `CONCENTRATED_WEIGHT`, low sub-universe |
| qMXpAZNK | `-ts_zscore(fn_comp_options_grants_fair_value_a, 63)` | low Sharpe, `CONCENTRATED_WEIGHT`, low sub-universe |
| YPAO7zGq | `-ts_zscore(fn_debt_instrument_carrying_amount_a, 63)` | `CONCENTRATED_WEIGHT` 0.50 |
| O09gJVxY | `rank(ts_rank(max_shareholders_equity_guidance, 22))` | `CONCENTRATED_WEIGHT`, low sub-universe |
| omYZEwKl | `rank(ts_rank(max_shares_outstanding_guidance, 22))` | `CONCENTRATED_WEIGHT`, low sub-universe |

## Interpretation

The strong aggregate tax-benefit metrics are real enough to gate-pass, but the
signal is too sparse for BRAIN's concentration check. Broad additive stabilizers,
time-series backfill, group backfill, winsorization, decay wrapping, and
multiplicative leverage confirmation did not produce a concentration-clean
candidate.

## Revalidated Submission Candidate

After the tax-benefit family was blocked, the existing EXCELLENT+ submission
queue was revalidated before spending more simulations.

| Alpha ID | Expression | Sharpe | Fitness | Turnover | Self-Corr | Verdict |
|----------|------------|--------|---------|----------|-----------|---------|
| xAn2kvOp | `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close) + zscore(ts_sum(anl4_netprofit_flag, 22))` | 1.75 | 2.21 | 6.47% | 0.5963 PASS vs `xAn1LqXm` | SUBMITTED / ACTIVE |

The BRAIN platform metadata for `xAn2kvOp` was refreshed from the corrected book
entry. The user submitted `xAn2kvOp` on BRAIN on 2026-06-14, and the local book
record is now ACTIVE.
