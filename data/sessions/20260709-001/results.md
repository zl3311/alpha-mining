---
id: "20260709-001-results"
session: "20260709-001"
total_expressions: 59
gate_passers: 17
best_sharpe: 2.27
best_fitness: 2.22
best_alpha_id: "rKlo39p1"
---

# Results: Session 20260709-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 59 (across 5 rounds) |
| Gate-passers (S>=1.25, F>=1.0) | 17 |
| Best Sharpe | 2.27 (`omlK5Qkv`, tlcf-raw variant — higher self-corr risk, not chosen) |
| Best Fitness (chosen candidate) | 2.22 (`rKlo39p1`) |
| Budget used | 59 / unlimited |

## Gate-Passers (submittable-tier only, S>=1.25 F>=1.0)

| # | Alpha ID | Expression (abbrev.) | Sharpe | Fitness | Turnover | Verdict |
|---|----------|-----------------------|--------|---------|----------|---------|
| 1 | rKlo39p1 | tlcf event-mag + leverage + ivaco + drlt + **buzz** | 2.13 | 2.22 | 10.7% | **SAFE — chosen candidate** |
| 2 | omlK5Qkv | tlcf event-mag (raw, no /close) + leverage + ivaco + drlt | 2.27 | 2.14 | 2.8% | RISKY (est. self-corr ~0.71, unconfirmed) |
| 3 | blqLGagK | tlcf event-mag (4-factor base, no buzz) | 1.91 | 1.79 | 4.6% | SAFE but GOOD grade only (self-corr confirmed PASS 0.6372) |
| 4 | P03pNJx7 | dcvsub event-mag + leverage + ivaco + drlt | 2.09 | 1.89 | 2.5% | BLOCKED — self-corr FAIL 0.7693 |
| 5 | 3qR7wQXg | dcvsub event-mag (3-factor) | 1.86 | 1.57 | 2.5% | BLOCKED — self-corr FAIL 0.8066 |
| 6 | omlKezl2 | tlcf event-mag, 2x leverage weight | 2.02 | 1.93 | 4.0% | Below EXCELLENT threshold |
| 7 | mLbXEdn1 | mrct product-interaction-blend (netdebt_flag) | 1.79 | 1.71 | 14.3% | BLOCKED — self-corr FAIL 0.759 |
| 8-17 | various | mrct/tlcf/acqgdwl event-mag & dispersion variants | 1.24-1.94 | 1.04-1.96 | 2-7% | Below EXCELLENT or not corr-checked (deprioritized once winner found) |

## All Expressions Tested (by round)

### Round 1 (16 sims): Novel templates on low-usage fields — directional gating, multi-horizon spread, non-linear, product-blend control
Best: `mLbXEdn1` mrct product-blend, S=1.79 F=1.71 GOOD, self-corr FAIL 0.759.
All directional-gating (`sign(ts_delta(...))`) variants: negative Sharpe. See
`dead_zones/template-directional-gating-sign-delta.md`.

### Round 2 (17 sims): Continuous-momentum interaction, convex self-product, dispersion, cross-family flag×sentiment on strong standalone fields
All 17 candidates INFERIOR or AVERAGE at best (max F=1.06). See
`dead_zones/template-convex-dispersion-flag-sentiment.md`.

### Round 3 (14 sims): Extend proven `event-magnitude-novel-fields` template to tlcf/mrct/dcvsub/acqgdwl + probe 2 fresh ultra-low-usage analyst estimate fields
Best: `P03pNJx7` dcvsub 4-factor S=2.09 F=1.89 GOOD (self-corr FAIL 0.7693);
`blqLGagK` tlcf 4-factor S=1.91 F=1.79 GOOD (self-corr **PASS 0.6372**).
`anl4_qf_az_wol_spfc`/`anl4_qf_az_wol_vid` (very low coverage, alphaCount ~100):
all INFERIOR.

### Round 4 (8 sims): Refine tlcf recipe for higher fitness while preserving self-corr
Best: `rKlo39p1` (+buzz stabilizer) EXCELLENT S=2.13 F=2.22, self-corr **PASS
0.6262**. `omlK5Qkv` (raw tlcf, no /close) EXCELLENT S=2.27 F=2.14 but est.
self-corr ~0.71 (higher risk, not chosen).

### Round 5 (4 sims): Backup fitness boosters (mrct/prepaid_expense stabilizers, weight variants)
None reached EXCELLENT; confirmed round 4's `rKlo39p1` as the best available.

## BRAIN Check Results

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|-------------------|----------------------|
| rKlo39p1 | PASS | PASS | PASS | PASS | PASS | PASS | PENDING on `/check`; **0.6262 PASS** via `/correlations/self` (auto-pass, <=0.7) | PASS |
| blqLGagK | PASS | PASS | PASS | PASS | PASS | PASS | **0.6372 PASS** (confirmed via `/check`) | PASS |
| P03pNJx7 | PASS | PASS | PASS | PASS | PASS | PASS | **0.7693 FAIL** | PASS |
