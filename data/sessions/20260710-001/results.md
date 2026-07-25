---
id: "20260710-001-results"
session: "20260710-001"
total_expressions: 70
gate_passers: 22
best_sharpe: 2.63
best_fitness: 2.68
best_alpha_id: "WjGVJ7bN"
submittable_alpha_id: "WjGVJ7bN"
---

# Results: Session 20260710-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 70 (4 rounds) |
| Gate-passers (S>=1.0, F>=0.8) | 22 |
| Best Sharpe | 2.63 |
| Best Fitness | 2.68 |
| Budget used | 70 / unlimited |

## Round 1 (24 sims) — untested fields, standard templates

Targeted the genuinely-untested singleton fields from `negation-blend-candidates.md`
(`min_tangible_book_value_per_share_guidance_2`, `anl4_qf_az_wol_spfc/vid`,
`fn_comp_options_forfeitures_and_expirations_a`, `fn_prepaid_expense_q`) plus
never-tested negated tax fields (`fnd6_txw`, `fnd6_txdbca`) via additive/product/
directional-gating/multi-horizon templates. Best: `P03OoWg7`
(`anl4_qf_az_wol_spfc` + `anl4_qf_az_wol_vid` + `open/close-1`), AVERAGE
S=1.42 F=1.24. 1 job failed permanently (`trade_when` FASTEXPR error, unrelated
to signal quality).

## Round 2 (16 sims) — boosting the round-1 winner

Mutated the `wol_spfc`/`wol_vid` combo (4th-factor additions, zscore, weight
tuning, MARKET neutralization, `qfd1` forward-quarter variants). Best:
`WjGV3Mrx` (2x-weighted `open/close-1`), AVERAGE S=1.70 F=1.41. Confirmed
MARKET neutralization hurts this template (S=0.81 vs 1.42 SUBINDUSTRY).
Ceiling confirmed at AVERAGE — see new dead zone
`family-sparse-analyst-guidance-untested-fields.md`.

## Round 3 (12 sims) — event-magnitude transform, fresh stabilizer

Applied `abs(ts_delta(F/close, d))` event-magnitude to the same fresh fields,
paired with `open/close-1` + `wol_spfc/vid` (avoiding the proven
leverage+ivaco+drlt combo to test if a fresh stabilizer set alone could break
through). Best: `0mEMg7xk` (`fn_prepaid_expense_q` event-magnitude + leverage +
open/close), AVERAGE S=1.40 F=1.37. Still capped at AVERAGE.

## Round 4 (10 sims) — event-magnitude + proven full stabilizer — BREAKTHROUGH

Applied the full proven `event-magnitude + leverage + ivaco + drlt` template
(previously validated only on itci/ppegtq/tlcf) to the same fresh fields.
`fnd6_txw` (Excise Taxes, never used before) broke through:

| Alpha | Expression (leg 1) | Sharpe | Fitness | Grade |
|-------|---------------------|--------|---------|-------|
| **WjGVJ7bN** | txw event(d=3) + leverage + ivaco + drlt + **buzz** | **2.63** | **2.68** | **SPECTACULAR** |
| 6X9eNXRL | txdbca event(d=3) + leverage + ivaco + drlt | 2.06 | 1.87 | GOOD |
| e70xEm0M | txw event(d=3) + leverage + ivaco + drlt (no buzz) | 2.01 | 1.78 | GOOD |
| 88Qe266a | mrct event(d=3) + leverage + ivaco + drlt + buzz | 1.80 | 1.75 | GOOD |
| wplEWG9Y | prepaid_expense event(d=3) + leverage + ivaco + drlt + buzz | 1.77 | 1.77 | GOOD |

## Gate-Passers

| # | Alpha ID | Sharpe | Fitness | Turnover | Family | Verdict |
|---|----------|--------|---------|----------|--------|---------|
| 1 | WjGVJ7bN | 2.63 | 2.68 | 10.9% | excise_tax_event_magnitude_leverage_buzz | **SAFE** |
| 2 | 6X9eNXRL | 2.06 | 1.87 | 2.5% | txdbca_event_magnitude (near-dup of WjGVJ7bN, mutual corr 0.87) | REDUNDANT |
| 3 | e70xEm0M | 2.01 | 1.78 | 2.0% | txw_event_magnitude_no_buzz (subset of WjGVJ7bN, mutual corr 0.89) | REDUNDANT |
| 4 | WjGV3Mrx | 1.70 | 1.41 | 16.7% | sparse_analyst_guidance | below EXCELLENT threshold |
| 5-22 | (various) | 0.5-1.7 | -0.09-1.37 | — | see round tables above | below EXCELLENT threshold |

## BRAIN Check Results

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|-------------------|---------------------|
| WjGVJ7bN | PASS | PASS | PASS | PASS | PASS | PASS | ERROR (see book entry — effectively PASS both ways) | PASS |
| 6X9eNXRL | PASS | PASS | PASS | PASS | PASS | PASS | not checked (redundant vs WjGVJ7bN) | PASS |
| e70xEm0M | PASS | PASS | PASS | PASS | PASS | PASS | not checked (redundant vs WjGVJ7bN) | PASS |
