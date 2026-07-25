---
id: "20260702-001"
date: "2026-07-02"
strategy: "EXPLORE"
trigger: "manual (user-initiated, no budget constraint)"
status: "complete"
budget: "unlimited"
target: "EXCELLENT+ submittable"
rounds: 1
gate_passers: 3
simulations: 33
viable_candidates: 1
submissions: 1
submitted: ["78w5d35x"]
best_alpha: "78w5d35x"
best_grade: "SPECTACULAR"
best_sharpe: 2.34
best_fitness: 3.10
---

# Session 20260702-001

## Context Assessment

- Book: 31 ACTIVE + 10 PENDING across 39 families
- Self-corr wall: 0.7 threshold + 1.10x Sharpe premium escape
- Recent 24h: 46 results from ppegtq exploration, ALL blocked by self-corr
- Server: healthy, 5000 budget, idle worker
- Strategy: EXPLORE — novel fields + orthogonal themes to escape self-corr wall

## Approach

Three-pronged strategy across 33 simulations:
1. **Novel fundamental anchors**: fnd6_dd1q, debt_lt, fnd6_txs, fnd6_dn, fnd6_tlcf, fnd6_cshtr, fnd6_dpvieb, fnd6_esopct, fnd6_aqc
2. **Orthogonal theme blends**: IV skew + novel fields, relationship counts
3. **MARKET neutralization variants**: decorrelation via neutralization switch

## Round 1 Results (33 simulations)

### Gate-passers (EXCELLENT+, ALL PASS)

| Alpha ID | Grade | S | F | T | Neut | Self-Corr | Result |
|----------|-------|---|---|---|------|-----------|--------|
| 88z0OPwW | SPECTACULAR | 2.75 | 3.37 | 11.9% | SUBINDUSTRY | 0.837 vs ZYpVLGZj | FAIL |
| 78w5d35x | SPECTACULAR | 2.34 | 3.10 | 10.4% | MARKET | 0.797 vs np30Odjd | **PASS** |
| A1wp3Gjg | EXCELLENT | 1.63 | 2.14 | 9.8% | MARKET | 0.787 vs np30Odjd | FAIL |

### Key Finding

**`78w5d35x` is submittable** — SPECTACULAR grade with self-corr PASS via Sharpe premium (2.34 >= 1.10 × 1.87). Uses novel `fnd6_dd1q` (deferred development costs quarterly) as anchor with MARKET neutralization for decorrelation.

Expression:
```
ts_decay_linear(rank(fnd6_dd1q / close) + rank(anl4_ptpr_flag) + rank(fnd6_itci / close) + rank(open/close - 1), 5)
```

### Observations

1. `fnd6_dd1q / close` is a strong novel anchor — SPECTACULAR grade when combined with proven catalysts
2. MARKET neutralization was crucial: same expression under SUBINDUSTRY hit self-corr FAIL (corr 0.837 vs ZYpVLGZj), but MARKET neut shifted the peer from ZYpVLGZj to np30Odjd (lower Sharpe → lower escape bar)
3. IV skew fields (implied_volatility_mean_skew_*) suffered from CONCENTRATED_WEIGHT — not viable as blend components with current templates
4. All-novel-field combinations (dd1q + tlcf + rd_exp) were too weak standalone (INFERIOR)
5. Debt fields (debt_lt, cptmfmq_dlttq, newa1v1300_dltt) produced only AVERAGE grade — less distinctive than dd1q

### Dead Zones Confirmed

- `fnd6_tlcf` + `fnd6_dd1q` standalone: INFERIOR (S=0.61)
- `fnd6_esopct`: INFERIOR (S=0.80)
- `fnd6_aqc`: INFERIOR (S=0.40)
- IV skew + novel fields (raw rank): CONCENTRATED_WEIGHT structural block
