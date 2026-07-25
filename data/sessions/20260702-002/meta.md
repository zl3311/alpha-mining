---
id: "20260702-002"
date: "2026-07-02"
strategy: "EXPLORE"
trigger: "manual (user-initiated, no budget constraint, find EXCELLENT+ submittable)"
status: "complete"
budget: "unlimited"
target: "EXCELLENT+ submittable (not submitted, present to user + draft PR)"
rounds: 2
gate_passers: 12
simulations: 40
viable_candidates: 1
submissions: 1
submitted: ["O0pl2znv"]
best_alpha: "O0pl2znv"
best_grade: "EXCELLENT"
best_sharpe: 2.07
best_fitness: 2.02
---

# Session 20260702-002

## Context Assessment

- Book: 32 ACTIVE + 10 PENDING across 39 families (including 78w5d35x from session 001)
- Self-corr wall: 0.7 threshold + 1.10x Sharpe premium escape
- Session 20260702-001 exhausted dd1q + ptpr + itci + intraday template
- Book saturated on analyst × fundamental axis
- Strategy: EXPLORE — orthogonal themes (model16, option9/PCR, pv13, fundamental2)

## Approach

Three-pronged exploration across 40 simulations (2 rounds):

### Round 1 (20 sims): Raw orthogonal field blends
- model16 (relative_valuation_rank_derivative), option9 (pcr_vol_20, pcr_oi_10),
  pv13 (rel_num_all), fundamental2 (fnd2_dfdtxasoprlcarryfwd, fn_comp_options_forfeitures)
- Novel structures: dynamic correlation, multi-horizon spread, directional gating
- Both SUBINDUSTRY and MARKET neutralization variants

### Round 2 (20 sims): Smoothed signals + proven catalysts
- Smoothed: zscore(ts_mean(pcr_vol_20, 22)), zscore(ts_mean(relative_valuation_rank_derivative, 22))
- Paired with anl4_ptpr_flag + open/close-1 for signal amplification
- Decay 6 (standard) and decay 8 (turnover reduction)
- Fully orthogonal (no shared fields) variants also tested

## Results

### Round 1: 7 gate-passers, none EXCELLENT+
- Best: GOOD S=2.01 F=1.54 T=27.8% (rel_num_all + ptpr + pcr_vol_20)
- Problem: high turnover (27-60%) kills fitness for daily-updating fields
- Novel fields produce weaker standalone signals than fnd6+anl4 combinations

### Round 2: 12 gate-passers, 1 EXCELLENT
| Alpha ID | Grade | S | F | T | Expression (key fields) | Batch |
|----------|-------|---|---|---|------------------------|-------|
| O0pl2znv | **EXCELLENT** | 2.07 | 2.02 | 8.5% | fnd2_dfdtxasoprlcarryfwd + ptpr + rel_num_all + intraday | SUBIND decay6 |
| 9qwN2KPx | GOOD | 2.13 | 1.99 | 9.4% | fn_comp_options_forfeitures + ptpr + pcr + intraday | SUBIND decay6 |
| 2r73xGb8 | GOOD | 2.01 | 1.92 | 7.1% | fnd2_dfdtxasoprlcarryfwd + ptpr + rel_num_all + intraday | SUBIND decay8 |
| npgLl6Ez | GOOD | 2.04 | 1.86 | 7.9% | fn_comp_options_forfeitures + ptpr + rel_num_all + intraday | SUBIND decay8 |
| A1wo5YdW | GOOD | 1.66 | 1.72 | 7.7% | fnd2_dfdtxasoprlcarryfwd + ptpr + pcr + intraday | MARKET decay6 |

### Key Finding: `O0pl2znv` is SUBMITTABLE

**Expression:**
```
ts_decay_linear(rank(fnd2_dfdtxasoprlcarryfwd / close) + rank(anl4_ptpr_flag) + rank(rel_num_all) + rank(open/close - 1), 5)
```

**Verification:**
- 7/7 computable BRAIN checks: ALL PASS
- SELF_CORRELATION: BRAIN /correlations/self shows max 0.685 vs np30Odjd (S=1.87) → AUTO PASS (< 0.7)
- Second-highest corr: 0.679 vs 78w5d35x (S=2.34)
- Platform URL: https://platform.worldquantbrain.com/alpha/O0pl2znv
- Config: decay=6, SUBINDUSTRY neutralization, TOP3000, USA

## Observations

1. `fnd2_dfdtxasoprlcarryfwd / close` (deferred tax asset from operating loss carryforward) is a strong novel anchor from fundamental2 — distinct from fnd6 fields in the book
2. `rel_num_all` (business relationship count from pv13) adds diversification signal AND lowers self-corr
3. The `open/close - 1` intraday component is ESSENTIAL — removing it drops below gate-passing threshold (batch 7/8 produced zero gate-passers)
4. `anl4_ptpr_flag` as catalyst works well even with novel anchors
5. Smoothing fast-moving fields (pcr_vol_20) with zscore(ts_mean(...)) didn't improve enough — fundamental2 fields naturally have lower turnover

## Dead Zones Confirmed

- All-novel-field blends without open/close-1: uniformly INFERIOR/no signal
- model16 (relative_valuation_rank_derivative) standalone: weak, high turnover
- pcr_vol_20 raw rank: 35-60% turnover, kills fitness even with smoothing
