---
id: "20260624-001"
date: "2026-06-24"
strategy: "EXPLORE"
trigger: "local_manual_mining_session"
status: "completed"
budget_used: 45
gate_passers: 32
submitted: []
branch: "session/20260624-001-explore-novel-structures"
tags:
  - "20260624-001"
  - "explore_novel"
  - "cross_family"
  - "novel_structures"
  - "diverse_iv60"
candidates:
  - id: "3q7edgEQ"
    grade: "SPECTACULAR"
    sharpe: 2.53
    fitness: 3.29
    self_corr_value: 0.6013
    self_corr_result: "PASS"
    verdict: "WINNER"
  - id: "KPbEeLez"
    grade: "SPECTACULAR"
    sharpe: 2.36
    fitness: 2.94
    self_corr_value: 0.5428
    self_corr_result: "PASS"
    verdict: "BACKUP_SAFEST"
  - id: "WjpV8AxO"
    grade: "SPECTACULAR"
    sharpe: 2.96
    fitness: 4.38
    self_corr_value: null
    self_corr_result: "NOT_CHECKED"
    verdict: "BLOCKED_SUB_UNIVERSE"
  - id: "leV3X367"
    grade: "EXCELLENT"
    sharpe: 1.95
    fitness: 2.02
    self_corr_value: 0.547
    self_corr_result: "PASS"
    verdict: "SAFE_FALLBACK"
---

# Session 20260624-001: EXPLORE — Novel Structural Templates & Ultra-Diverse IV60

## Phase 0 Context

STRATEGY: EXPLORE
TARGET: Novel structural templates (multiplicative interactions, inter-field ratios, leverage hybrids) and ultra-diverse 6-factor IV60 blends with non-balance-sheet legs
BUDGET: No cap (iterate until EXCELLENT+ submittable found)
CONSTRAINTS: novelty-required (>=50% novel templates), avoid dead zones, avoid saturated families
RATIONALE: Default EXPLORE — book saturated (39 entries), need structural novelty to break self-corr wall vs 88z7MM37 (ACTIVE SPECTACULAR S=2.78)

## Round 1: Novel Structures (20 sims, 16 gate-passers)

Tested 20 expressions across 4 groups:
- Group A (5): Multiplicative `rank(F1) * rank(F2) + zscore(IV60) + rank(F3)` → SPECTACULAR S=2.02-2.42
- Group B (5): Inter-field ratios `rank(F1/F2) + zscore(IV60) + additives` → GOOD-SPECTACULAR
- Group C (5): Leverage premium `rank(-1*equity/assets) + zscore(IV60) + legs` → SPECTACULAR S=2.01-2.60
- Group D (5): Novel 5-factor additive with untested legs → SPECTACULAR S=1.86-2.12

**Key finding:** All high-Sharpe candidates use capital-intensity fundamental legs (fatl, ppegtq, fate, txdbca) which correlate too highly with 88z7MM37's legs (itci, drlt, acdo). Self-corr = 0.629-0.710 → BLOCKED.

## Round 2: Ultra-Diverse IV60 + Non-IV60 Paths (15 sims, 10 gate-passers, 5 failed)

Pivot to non-balance-sheet legs to decorrelate from 88z7MM37:
- Group E (5): IV60 + guidance/analyst coverage/revision legs → SPECTACULAR + EXCELLENT
- Group F (5): Event-magnitude transforms (no IV60) → ALL FAILED (compilation errors)
- Group G (5): Leverage + analyst (no IV60) → Mixed GOOD-EXCELLENT

**Breakthrough:** Ultra-diverse IV60 blends using analyst + guidance + coverage legs produce SPECTACULAR results with SAFE self-correlation:
- WjpV8AxO: SPECTACULAR S=2.96 F=4.38 (FAIL sub-universe by 0.25)
- gJ19pwbO: SPECTACULAR S=2.35 F=2.64 (FAIL sub-universe by 0.02)
- leV3X367: EXCELLENT S=1.95 F=2.02 ALL PASS, self-corr 0.547 SAFE

## Round 3: Fix Sub-Universe + Boost (10 sims, 6 gate-passers)

Added 6th dense-coverage legs (anl4_cfi_flag, anl4_netdebt_flag, anl4_ptp_flag) to fix sub-universe:

| ID | Grade | S | F | Expression (key legs) | BRAIN | Self-Corr |
|---|---|---|---|---|---|---|
| **3q7edgEQ** | **SPECTACULAR** | **2.53** | **3.29** | **IV60 + guidance + sales_count + epsr + cshtr + cfi_flag** | **ALL PASS** | **0.6013 PASS** |
| **KPbEeLez** | **SPECTACULAR** | **2.36** | **2.94** | **IV60 + cfi_flag + sales_count + epsr + cshtr + rd_exp** | **ALL PASS** | **0.5428 PASS** |
| rKoPkJXj | SPECTACULAR | 2.27 | 2.78 | IV60 + diverse legs | ALL PASS | — |
| E5we3x90 | EXCELLENT | 2.02 | 2.19 | IV60 + diverse legs | ALL PASS | — |
| vRLv0gma | EXCELLENT | 2.04 | 2.13 | IV60 + diverse legs | ALL PASS | — |

## Winner: 3q7edgEQ (SPECTACULAR, SAFE Self-Corr)

**Expression:**
```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(max_adjusted_net_income_guidance) + rank(sales_estimate_count_quarterly) + rank(anl4_epsr_flag) + rank(fnd6_cshtr) + rank(anl4_cfi_flag), 5)
```

**Settings:** decay=6, SUBINDUSTRY, USA TOP3000

**Metrics:**
- Grade: SPECTACULAR (S=2.53, F=3.29, T=5.8%, Ret=?)
- All computable BRAIN checks: PASS
- BRAIN self-correlation: max 0.6013 vs kq33Gjqk; 0.5135 vs 88z7MM37 (AUTO PASS)
- Self-corr margin: 0.099 below 0.7 threshold

**Mechanism:** 6-factor additive blend combining:
1. IV60 call-put spread 44-day smoothed zscore — Near-term options directional sentiment
2. max_adjusted_net_income_guidance — Forward-looking earnings guidance (management confidence)
3. sales_estimate_count_quarterly — Analyst coverage breadth (attention/liquidity proxy)
4. anl4_epsr_flag — EPS revision signal (consensus estimate momentum)
5. fnd6_cshtr — Cash-to-total-revenue (revenue quality/cash conversion)
6. anl4_cfi_flag — Cash flow revision flag (operating quality momentum)

The 6-factor structure with legs from 4 different economic families (options, guidance, analyst coverage, fundamental revenue quality) provides maximum decorrelation from the balance-sheet-focused book entries.

## Backup: KPbEeLez (Lower Risk, Lower Sharpe)

**Expression:**
```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(anl4_cfi_flag) + rank(sales_estimate_count_quarterly) + rank(anl4_epsr_flag) + rank(fnd6_cshtr) + rank(anl4_rd_exp_flag), 5)
```

S=2.36, F=2.94, self-corr=0.5428 (wider margin, no guidance sparsity risk).

## Lessons Learned

1. **Capital-intensity fundamentals correlate heavily**: fatl, ppegtq, fate, txdbca are all correlated with 88z7MM37's itci/drlt/acdo in PnL space. Self-corr 0.629+.
2. **Analyst + guidance legs decorrelate effectively**: Replacing balance-sheet legs with analyst coverage, guidance, and revision flags drops self-corr from 0.63 to 0.51-0.60.
3. **6th dense leg fixes sub-universe**: Adding anl4_cfi_flag as a 6th leg fixed gJ19pwbO's 0.02 sub-universe gap AND boosted Sharpe from 2.35 to 2.53.
4. **Event-magnitude transforms failed compilation**: abs(ts_delta(fnd6_field/close, d)) style expressions caused server-side errors (5/5 failed).
5. **IV60 remains the power driver**: All SPECTACULAR candidates include IV60. Non-IV60 paths (leverage, multiplicative) cap at EXCELLENT S=2.04 max.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total sims | 45 |
| Gate-passers | 32 |
| SPECTACULAR candidates | 18 |
| ALL PASS + self-corr PASS | 2+ (3q7edgEQ, KPbEeLez confirmed) |
| Best alpha | 3q7edgEQ SPECTACULAR S=2.53 F=3.29 |
| Self-corr margin | 0.099 (below 0.70 threshold) |
