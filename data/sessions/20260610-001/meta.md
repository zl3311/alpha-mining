---
id: 20260610-001
date: 2026-06-10
strategy: RECOMBINE
trigger: local manual mining session
status: completed
---

# Manual Mining Session

Started from local `main` with an existing dirty working tree, so branch-changing
sync was skipped to avoid disturbing user and in-progress repository changes.

## Phase 0 Context

STRATEGY: RECOMBINE

TARGET: Cross-family recombination of the newly discovered leverage premium
(`zscore(-1 * equity / assets)` / `rank(-1 * equity / assets)`) with sparse
analyst revision zscore signals, especially `anl4_netprofit_flag`.

BUDGET: 8-12 candidate expressions initially; defer HF submission while the
worker reports `paused_budget` unless the user explicitly wants the jobs queued.

CONSTRAINTS: Respect structural novelty, avoid IV group-neutralize variants,
avoid volume weighting on fundamentals, avoid `flag * (-ret)` correlation
drivers, and treat shared-field self-correlation conservatively.

RATIONALE: No active non-submit opportunity remains open; the last three mining
sessions already used EXPLORE. The fresh gate-passers are leverage premium and
zscore accumulated analyst revision, so recombination is the first matching
decision-tree strategy.

## Phase 1 Candidate Slate

### Batch: leverage_x_revision_recombine_r1

1. `zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22))`
   - Mechanism: High-leverage firms with positive net profit estimate revisions.
   - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 5

2. `ts_decay_linear(zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), 3)`
   - Mechanism: Same leverage + netprofit confirmation with light smoothing.
   - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 5

3. `zscore(-1 * equity / assets) * zscore(ts_sum(anl4_netprofit_flag, 22))`
   - Mechanism: Nonlinear confirmation; leverage premium only pays when earnings revisions agree.
   - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 4

4. `trade_when(zscore(ts_sum(anl4_netprofit_flag, 22)) > 0, zscore(-1 * equity / assets) + rank(fnd6_itci / close), zscore(ts_sum(anl4_netprofit_flag, 22)) < 0)`
   - Mechanism: Use analyst netprofit revisions as a regime gate for the strongest leverage quality blend.
   - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 4

5. `trade_when(zscore(ts_sum(anl4_netprofit_flag, 22)) > 0, rank(-1 * equity / assets) + rank(fnd6_drlt / close), zscore(ts_sum(anl4_netprofit_flag, 22)) < 0)`
   - Mechanism: Gate the already-check-clean leverage + deferred revenue blend by positive earnings revisions.
   - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 4

6. `rank(-1 * equity / assets) + zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_drlt / close)`
   - Mechanism: Leverage plus deferred revenue with a less-booked sparse analyst EPS revision signal.
   - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 3

7. `zscore(-1 * equity / assets) + zscore(ts_sum(anl4_capex_flag, 22)) + rank(fnd6_itci / close)`
   - Mechanism: Capital-structure premium plus quality, confirmed by capex estimate revisions.
   - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 3

8. `trade_when(ts_std_dev(returns, 20) > 0.02, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.01)`
   - Mechanism: Leverage and revision premium concentrated in higher-volatility regimes.
   - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 3

9. `rank(ts_corr(-1 * equity / assets, anl4_netprofit_flag, 20))`
   - Mechanism: Dynamic alignment between leverage and netprofit revision events as a standalone signal.
   - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 2

10. `zscore(-1 * equity / assets) + rank(fnd6_itci / close) + zscore(ts_sum(anl4_netprofit_flag, 22))`
    - Mechanism: Replace the duplicated itci weight in `pw7j2MXg` with analyst confirmation to reduce sub-universe fragility.
    - Decay: 6; Neutralization: SUBINDUSTRY; Priority: 4

Submitted 10 jobs to HF queue with tags `20260610-001` and
`leverage_x_revision_recombine_r1`, priority 5, decay 6, SUBINDUSTRY,
TOP3000.

## Phase 2 Results

The batch completed with 10/10 simulations done, 0 failures, and 8 gate-passers.
All 8 gate-passers passed the 7 computable BRAIN checks. The HF query
`--self-corr-check` path reads server DB columns (`jobs.self_corr`,
`jobs.corr_result`) and did not return usable tagged rows for this batch, so
authoritative self-correlation was checked directly against BRAIN with:

```bash
uv run python3 scripts/pnl_correlation.py --alphas <alpha_id> --brain-check
```

### BRAIN Self-Correlation Results

| Alpha ID | Grade | Sharpe | Fitness | Self-Corr | Result | Expression |
|---|---:|---:|---:|---:|---|---|
| akOVggz6 | GOOD | 1.76 | 1.83 | 0.4676 | PASS | `zscore(-1 * equity / assets) + rank(fnd6_itci / close) + zscore(ts_sum(anl4_netprofit_flag, 22))` |
| QPQY6YGr | GOOD | 1.86 | 1.80 | 0.4968 | PASS | `zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22))` |
| 78dolL3O | GOOD | 1.86 | 1.80 | 0.4972 | PASS | `ts_decay_linear(zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), 3)` |
| mLXYlro6 | GOOD | 1.88 | 1.89 | 0.5062 | PASS | `trade_when(ts_std_dev(returns, 20) > 0.02, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.01)` |

The `/check` verdicts are authoritative. The optional `/correlations/self`
peer-breakdown polling timed out, so top correlated peer details are unavailable.

## Phase 3 Iteration Plan

User requested continued iteration until at least one EXCELLENT+ alpha passes all
checks. Round 2 refines the four BRAIN-self-corr-passing GOOD candidates,
focusing on:

- high-volatility gate threshold sweeps around `mLXYlro6`;
- light smoothing of the leverage + netprofit blend;
- controlled third-factor additions that may lift fitness without excessive
  self-correlation.

### Batch: leverage_x_revision_refine_r2

1. `trade_when(ts_std_dev(returns, 20) > 0.015, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.01)`
2. `trade_when(ts_std_dev(returns, 20) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.012)`
3. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), 3), ts_std_dev(returns, 20) < 0.01)`
4. `trade_when(ts_std_dev(returns, 20) > 0.02, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)) + rank(fnd6_itci / close), ts_std_dev(returns, 20) < 0.01)`
5. `trade_when(ts_std_dev(returns, 20) > 0.02, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)) + rank(fnd6_drlt / close), ts_std_dev(returns, 20) < 0.01)`
6. `trade_when(ts_std_dev(returns, 20) > 0.02, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)) + rank(fnd6_acdo), ts_std_dev(returns, 20) < 0.01)`
7. `trade_when(ts_std_dev(returns, 20) > 0.02, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)) + rank(fnd6_fatl / close), ts_std_dev(returns, 20) < 0.01)`
8. `ts_decay_linear(zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), 5)`
9. `zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 44))`
10. `zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)) + rank(ts_mean(scl12_buzz, 5))`
11. `trade_when(rank(ts_mean(scl12_buzz, 5)) > 0.5, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), rank(ts_mean(scl12_buzz, 5)) < 0.3)`
12. `zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)) + rank(fnd6_drlt / close)`

### Round 2 Outcome

Round 2 completed with 12/12 gate-passers but no EXCELLENT. Best result:

- `omYo0Mxn`: GOOD, S=1.88, F=1.97, T=4.3%
  - Expression: `trade_when(ts_std_dev(returns, 20) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.012)`
  - Near miss; use as Round 3 anchor.

### Batch: leverage_x_revision_refine_r3

1. `trade_when(ts_std_dev(returns, 20) > 0.023, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.012)`
2. `trade_when(ts_std_dev(returns, 20) > 0.027, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.012)`
3. `trade_when(ts_std_dev(returns, 20) > 0.030, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.012)`
4. `trade_when(ts_std_dev(returns, 20) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.010)`
5. `trade_when(ts_std_dev(returns, 20) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.015)`
6. `trade_when(ts_std_dev(returns, 10) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 10) < 0.012)`
7. `trade_when(ts_std_dev(returns, 30) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 30) < 0.012)`
8. `trade_when(ts_std_dev(returns, 20) > 0.027, ts_decay_linear(zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), 3), ts_std_dev(returns, 20) < 0.012)`
9. `trade_when(ts_std_dev(returns, 20) > 0.027, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)) + rank(fnd6_itci / close), ts_std_dev(returns, 20) < 0.012)`
10. `trade_when(ts_std_dev(returns, 20) > 0.027, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)) + rank(fnd6_drlt / close), ts_std_dev(returns, 20) < 0.012)`

### Round 3 Outcome

Round 3 completed with 10/10 gate-passers and two EXCELLENT candidates:

- `xAn1LqXm`: EXCELLENT, S=2.00, F=2.12, T=3.9%
  - Expression: `trade_when(ts_std_dev(returns, 30) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 30) < 0.012)`
  - BRAIN checks: all computable checks PASS.
  - BRAIN self-corr `/check`: 0.5022, PASS. Top peer from output:
    `vRmlGnkv` at corr 0.502, S=1.72.
  - Verdict: SAFE / QUEUED for manual submission.
- `d5QKJG2x`: EXCELLENT, S=1.87, F=2.03, T=5.3%
  - Expression: `trade_when(ts_std_dev(returns, 20) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 20) < 0.015)`
  - BRAIN checks: all computable checks PASS.
  - BRAIN self-corr check timed out; not queued.

Target achieved: at least one EXCELLENT alpha (`xAn1LqXm`) passed all computable
BRAIN checks and authoritative BRAIN self-correlation.

