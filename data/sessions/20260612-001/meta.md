---
id: 20260612-001
date: 2026-06-12
strategy: EXPLOIT
trigger: local manual mining session via Cursor
status: completed
---

# Session 20260612-001

Local manual mining session started from the existing `session/20260611-001-event-detection` branch. The repo has a modified `server` submodule, so this session avoids branch switching and keeps changes scoped to session artifacts and mining records.

## Phase 0 Context

STRATEGY: EXPLOIT

TARGET: Structurally novel wrappers around the new event-magnitude family, anchored on `rank(abs(ts_delta(fnd6_itci / close, 3)))`, with regime gates and cross-family stabilizers rather than simple window/field variants.

BUDGET: No hard local simulation cap; start with a 10-expression first batch for queue latency and signal isolation, then iterate while results remain informative.

CONSTRAINTS: Use SUBINDUSTRY neutralization; avoid MARKET because it kills leverage/event signals; avoid volume weighting on fundamentals; avoid `flag * (-ret)`; avoid IV270 and PV reversal dead zones; treat shared-field self-correlation conservatively; keep at least half the batch structurally novel.

RATIONALE: No active non-submit opportunity remains open. Recent sessions already covered EXPLORE and RECOMBINE, while the new 24h discoveries are dominated by a genuinely new event-magnitude mechanism from session `20260611-001`; the first matching remaining decision-tree strategy is EXPLOIT, but simple refinements are mostly exhausted.

## Phase 1 Candidate Slate

Batch tag: `event_regime_exploit_r1`

1. `trade_when(zscore(ts_sum(anl4_netprofit_flag, 22)) > 0, rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), zscore(ts_sum(anl4_netprofit_flag, 22)) < 0)`
   - Mechanism: Inventory event magnitude only when net profit revisions confirm the regime.

2. `trade_when(zscore(ts_sum(anl4_epsr_flag, 22)) > 0, rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), zscore(ts_sum(anl4_epsr_flag, 22)) < 0)`
   - Mechanism: Inventory event magnitude only when EPS revisions confirm the regime.

3. `trade_when(ts_std_dev(returns, 30) > 0.025, rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), ts_std_dev(returns, 30) < 0.012)`
   - Mechanism: Event premium concentrated in higher realized-volatility regimes.

4. `trade_when(ts_std_dev(returns, 20) > 0.02, rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), ts_std_dev(returns, 20) < 0.01)`
   - Mechanism: Shorter volatility regime gate around the event premium.

5. `rank(abs(ts_delta(fnd6_itci / close, 3))) + zscore(-1 * equity / assets) + rank(fnd6_drlt / close)`
   - Mechanism: Test whether zscore leverage distribution improves checks without killing event Sharpe.

6. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22))`
   - Mechanism: Replace deferred revenue stabilizer with sparse analyst revision confirmation.

7. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`
   - Mechanism: Replace deferred revenue stabilizer with high-coverage sentiment reversal.

8. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), 3)`
   - Mechanism: Lightly smooth event plus analyst confirmation.

9. `rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
   - Mechanism: Nonlinear confirmation: event magnitude pays most in high-leverage names.

10. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close) + zscore(ts_sum(anl4_netprofit_flag, 22))`
    - Mechanism: Four-factor event blend testing whether analyst confirmation can offset lower-grade `fatl` stabilization.

Submitted 10 jobs to the HF queue with tags `20260612-001` and `event_regime_exploit_r1`, priority 5, decay 6, SUBINDUSTRY, USA TOP3000.

## Phase 2 Results

Batch completed with 9 gate-passers and 1 failed expression/simulation.

| Alpha | Grade | S | F | Turnover | BRAIN Checks | Self-Corr | Verdict |
|-------|-------|---|---|----------|--------------|-----------|---------|
| 6XEo91jO | SPECTACULAR | 3.08 | 2.53 | 27.9% | ALL PASS | 0.7181 PASS vs `omnopQ9k` | QUEUED; passes via Sharpe-premium escape |
| xAn2kvOp | EXCELLENT | 1.75 | 2.21 | 6.5% | ALL PASS | 0.5963 PASS vs `xAn1LqXm` | QUEUED |
| vRmpl57A | GOOD | 1.60 | 1.80 | 6.8% | ALL PASS | 0.6407 PASS | REDUNDANT with `xAn2kvOp` lower-grade decay wrapper |
| bl9rLraM | SPECTACULAR | 2.52 | 2.68 | 3.8% | ALL PASS | 0.9634 FAIL vs `0m8GV1Pp` | BLOCKED |
| j2gPZJwO | SPECTACULAR | 2.52 | 2.66 | 4.2% | ALL PASS | 0.9782 FAIL vs `0m8GV1Pp` | BLOCKED |
| xAn2x3zp | EXCELLENT | 2.47 | 2.48 | 4.2% | ALL PASS | 0.9793 FAIL | BLOCKED |
| 88LEQzrl | EXCELLENT | 2.42 | 2.36 | 3.3% | ALL PASS | 0.9386 FAIL vs `0m8GV1Pp` | BLOCKED |
| wpe2RWE6 | GOOD | 1.89 | 1.90 | 3.5% | ALL PASS | 0.7389 FAIL vs `0m8GV1Pp` | BLOCKED |
| omYJKLQ2 | EXCELLENT | 2.19 | 2.05 | 4.3% | LOW_SUB_UNIVERSE_SHARPE FAIL | self-corr output unusable | BLOCKED |

### Key Finding

The event family is highly self-correlated with `0m8GV1Pp`, so most event-regime
variants are blocked unless they either stay below 0.70 raw correlation or exceed
the Sharpe-premium escape. The social buzz reversal stabilizer is the best
discovery of the round: it lifts Sharpe to 3.08, enough for `6XEo91jO` to pass
despite raw self-corr 0.7181.

### Submission Queue

- `6XEo91jO`: SPECTACULAR, S=3.08, F=2.53, self-corr PASS via Sharpe premium.
- `xAn2kvOp`: EXCELLENT, S=1.75, F=2.21, self-corr 0.5963 PASS.

## Phase 3 Iteration Plan

Round 2 will exploit the `6XEo91jO` discovery: event magnitude + leverage +
social buzz reversal. The goal is to preserve the high Sharpe that unlocks the
Sharpe-premium escape while testing whether buzz smoothing, weighting, nonlinear
confirmation, or light decay can reduce turnover or increase fitness.

### Batch: event_buzz_exploit_r2

1. `rank(abs(ts_delta(fnd6_itci / close, 5))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`
2. `rank(abs(ts_delta(fnd6_itci / close, 3))) + zscore(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`
3. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns))`
4. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(scl12_buzz * (-1 * returns))`
5. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + ts_decay_linear(rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 3)`
6. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 3)`
7. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`
8. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`
9. `rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(ts_mean(scl12_buzz, 5) * (-1 * returns)) + rank(-1 * equity / assets)`
10. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) * rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`
11. `trade_when(ts_std_dev(returns, 20) > 0.02, rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), ts_std_dev(returns, 20) < 0.01)`
12. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)) + zscore(ts_sum(anl4_netprofit_flag, 22))`

Submitted 12 jobs to the HF queue with tags `20260612-001` and
`event_buzz_exploit_r2`, priority 5, decay 6, SUBINDUSTRY, USA TOP3000.

### Round 2 Outcome

Round 2 completed with 12/12 gate-passers. Eleven passed computable BRAIN checks;
`78dvzwn5` failed `LOW_SUB_UNIVERSE_SHARPE` by a narrow margin.

| Alpha | Grade | S | F | Turnover | BRAIN Checks | Self-Corr | Verdict |
|-------|-------|---|---|----------|--------------|-----------|---------|
| d5Q3ZmWv | SPECTACULAR | 2.97 | 2.92 | 18.3% | ALL PASS | 0.7163 PASS vs `0m8GV1Pp` | QUEUED; best variant |
| XgKvomKX | SPECTACULAR | 2.96 | 2.91 | 18.3% | ALL PASS | 0.7162 PASS vs `0m8GV1Pp` | REDUNDANT with `d5Q3ZmWv` |
| vRmpvWnQ | SPECTACULAR | 3.09 | 2.62 | 26.6% | ALL PASS | 0.7177 PASS vs `omnopQ9k` | REDUNDANT; lower fitness |
| MPxeGqan | SPECTACULAR | 2.90 | 3.09 | 15.0% | ALL PASS | 0.7399 FAIL | BLOCKED; Sharpe just misses premium |
| WjgoAprO | EXCELLENT | 2.75 | 2.50 | 19.7% | ALL PASS | 0.7730 FAIL | BLOCKED |
| RRrlmbp1 | EXCELLENT | 2.92 | 2.50 | 24.6% | ALL PASS | check timed out | not queued |
| vRmpvZMw | EXCELLENT | 3.04 | 2.48 | 28.0% | ALL PASS | check timed out | not queued |
| P01YOPbW | EXCELLENT | 2.03 | 2.06 | 13.9% | ALL PASS | check timed out | not queued |
| N1OJbn8p | GOOD | 2.85 | 1.94 | 45.3% | ALL PASS | check timed out | not queued |
| xAn2d7Yp | GOOD | 3.01 | 1.86 | 51.4% | ALL PASS | check timed out | not queued |
| e7rV3M1J | GOOD | 1.96 | 1.82 | 22.1% | ALL PASS | check timed out | not queued |
| 78dvzwn5 | SPECTACULAR | 3.01 | 2.69 | 21.0% | LOW_SUB_UNIVERSE_SHARPE FAIL | self-corr FAIL/invalid | BLOCKED |

`d5Q3ZmWv` supersedes `6XEo91jO`: the light decay wrapper improves fitness
2.53 -> 2.92 and reduces turnover 27.9% -> 18.3%, while preserving BRAIN
self-corr PASS via Sharpe premium.

## Phase 4 Iteration Plan

Round 3 targets the narrow miss `MPxeGqan`: F=3.09 and turnover 15.0%, but
self-corr FAIL at 0.7399 because Sharpe 2.90 is just under the premium threshold.
Test nearby decay windows and small third/fourth-factor perturbations to either
raise Sharpe above the premium requirement or reduce raw self-corr below 0.70.

### Batch: event_buzz_decay_refine_r3

1. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 4)`
2. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 6)`
3. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 7)`
4. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)`
5. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + ts_decay_linear(rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 3), 3)`
6. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + zscore(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`
7. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)) + zscore(ts_sum(anl4_netprofit_flag, 22)), 3)`
8. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)) + rank(fnd6_fatl / close), 3)`

Submitted 8 jobs to the HF queue with tags `20260612-001` and
`event_buzz_decay_refine_r3`, priority 5, decay 6, SUBINDUSTRY, USA TOP3000.

### Round 3 Outcome

Round 3 completed with 8/8 gate-passers. The round found higher-fitness decay
variants, but none superseded the verified `d5Q3ZmWv` candidate.

| Alpha | Grade | S | F | Turnover | Expression Variant | BRAIN Checks | Self-Corr | Verdict |
|-------|-------|---|---|----------|--------------------|--------------|-----------|---------|
| 78dvZ3r2 | SPECTACULAR | 2.90 | 3.27 | 13.5% | buzz mean 10, outer decay 5 | ALL PASS | 0.7378 FAIL vs `0m8GV1Pp` | BLOCKED |
| E5K8veRm | SPECTACULAR | 2.84 | 3.20 | 12.9% | outer decay 7 | ALL PASS | 0.7589 FAIL | BLOCKED |
| wpe2YYad | SPECTACULAR | 2.87 | 3.15 | 13.9% | outer decay 6 | ALL PASS | 0.7499 FAIL | BLOCKED |
| mLX0gm5x | SPECTACULAR | 2.93 | 3.02 | 16.4% | outer decay 4 | ALL PASS | check timed out twice | FOLLOW-UP only; not queued |
| QPQNb5MQ | SPECTACULAR | 2.60 | 3.05 | 14.1% | add `fnd6_fatl` | ALL PASS | not checked | likely blocked by low Sharpe premium |
| WjgoPZnx | SPECTACULAR | 2.85 | 2.99 | 15.2% | inner buzz decay + outer decay | ALL PASS | not checked | likely blocked |
| 6XEor5vK | GOOD | 1.92 | 1.99 | 8.7% | zscore leverage + outer decay | not checked | not checked | lower grade |
| 58vAzZ7M | GOOD | 1.86 | 1.98 | 15.9% | netprofit perturbation + outer decay | not checked | not checked | lower grade |

### Final Candidate Ranking

1. `d5Q3ZmWv` — QUEUED. Best verified candidate: SPECTACULAR S=2.97, F=2.92,
   self-corr 0.7163 PASS via Sharpe premium.
2. `xAn2kvOp` — QUEUED. EXCELLENT S=1.75, F=2.21, self-corr 0.5963 PASS; lower
   priority because it overlaps with pending `xAn1LqXm`.
3. `mLX0gm5x` — follow-up only. SPECTACULAR S=2.93, F=3.02, but self-corr did
   not return after two attempts.
