---
id: "20260618-001"
date: "2026-06-18"
strategy: "EXPLORE"
research_question: "Can depreciation/debt/PP&E fundamental backbones combined with EPS revision and breadth stabilizers produce a decorrelated EXCELLENT+ alpha that avoids the saturated event/leverage/IV/acdo families?"
budget_used: 24
budget_cap: null
trigger: "manual alpha-mining session via Cursor"
gate_passers: 12
submissions: 0
submittable_candidates: 1
status: "productive"
tags:
  - "20260618-001"
  - "depreciation_debt_eps"
  - "fate_totassets"
  - "EXPLORE"
candidates:
  - id: "blL55wRp"
    grade: "EXCELLENT"
    sharpe: 2.10
    fitness: 2.03
    self_corr_value: 0.6941
    self_corr_result: "PASS"
    verdict: "SUBMITTABLE"
  - id: "KPbjjWPx"
    grade: "EXCELLENT"
    sharpe: 2.07
    fitness: 2.30
    self_corr_value: 0.8383
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
---

# Session 20260618-001

Manual mining session targeting underexplored fundamental6 debt/depreciation/
capital-intensity clusters combined with `anl4_epsr_flag` and
`anl4_totassets_flag` analyst revision signals not present in the active book.

## Phase 0 Context

STRATEGY: EXPLORE (no EXPLORE in last 3 sessions; book saturated)

TARGET: Novel fundamental backbones (depreciation, long-term debt, PP&E,
capital intensity) combined with EPS revision, total-assets revision, intraday
dislocation, and buzz stabilizer. Includes volatility-regime gates and product
forms.

BUDGET: No cap. Used 24 simulations across 2 rounds.

CONSTRAINTS: Avoid fnd6_fatl (in np30Odjd), fn_accrued_liab_q (in zqOrkbbG),
anl4_bvps_flag/netdebt_flag (saturated), fnd6_itci (event family), IV spreads,
flag*(-ret) reversal. >=50% structurally novel templates.

## Phase 1 Round 1 (SUBINDUSTRY, 12 sims)

Batch tag: `depr_debt_eps_r1`

Tested 3 backbone families across 3/4-leg blends, volatility gates, products,
and dynamic correlations:
- **Depreciation** (`fnd6_newqv1300_dpactq/close`) + `anl4_epsr_flag`: AVERAGE
- **Long-term debt** (`debt_lt/close`) + `anl4_epsr_flag`: AVERAGE
- **PP&E** (`fnd6_newqv1300_ppegtq/close`) + `anl4_epsr_flag`: AVERAGE
- **Capital intensity** (`fnd6_fate/close`) + `anl4_totassets_flag`: **EXCELLENT**

6 gate-passers total. The `fnd6_fate + anl4_totassets_flag` family clearly
outperformed, producing 2 EXCELLENT and 1 GOOD. Depreciation/debt/PP&E
backbones capped at AVERAGE (S < 1.75).

### BRAIN Checks

All 3 top candidates (KPbjjWPx, blL55wRp, LLpAAoLa) passed all computable
BRAIN checks.

### Self-Correlation

- **KPbjjWPx** (3-leg ungated, EXCELLENT S=2.07 F=2.30): FAIL. Max corr
  0.8383 vs `6Xzm6PQP` (guidance_fundamental S=2.31). Needs S>=2.54 for
  Sharpe premium escape; only has 2.07. Also high vs pw8wNe76 (0.75) and
  0mzQQvX8 (0.73).

- **blL55wRp** (vol-gated 4-leg, EXCELLENT S=2.10 F=2.03): **PASS**. Max corr
  0.6941 vs `6Xzm6PQP`, below 0.70 threshold. The volatility gate dropped
  self-corr from 0.84 to 0.69, confirming the pattern from `0m7lnAEr`.

Key finding: The ungated `fnd6_fate + totassets_flag` signal correlates
with the guidance/fundamental book cluster (both pick similar quality stocks),
but the volatility regime gate changes position overlap enough to clear the
self-corr wall.

## Phase 2 Round 2 (MARKET, 12 sims)

Batch tag: `fate_refine_r2`

Tested MARKET neutralization variants to see if decorrelation could improve
further. Also tried field substitutions (fnd6_dd, fnd6_dpvieb, fnd6_cshtr,
anl4_fcf_high, anl4_epsr_flag, fnd6_newqv1300_dpactq), product forms,
threshold tuning, and 5-leg blends.

Result: All MARKET variants degraded to GOOD/AVERAGE (best: omKMem55 GOOD
S=1.29 F=1.70). MARKET neutralization destroys the EXCELLENT grade for this
family. Confirms SUBINDUSTRY is optimal.

## Winner

**blL55wRp** — EXCELLENT S=2.10, F=2.03, turnover 16.7%, all 8 BRAIN checks
PASS, self-corr 0.6941 PASS (authoritative BRAIN check). BRAIN metadata set;
book entry created as `status: PENDING`; submission queue entry created.

## Key Learnings

1. **Capital intensity + total-assets revision is a viable EXCELLENT backbone.**
   `fnd6_fate/close + anl4_totassets_flag` produces EXCELLENT (S>2.0) with
   SUBINDUSTRY neut, while depreciation/debt/PP&E cap at AVERAGE.

2. **Volatility gate remains the key self-corr lever.** Dropped max corr from
   0.84 to 0.69 (a 0.15 reduction), same magnitude as the 0m7lnAEr discovery.

3. **MARKET neutralization destroys this family.** Sharpe drops ~40% from
   SUBINDUSTRY. This family is fundamentally industry-relative.

4. **Self-corr margin is thin (0.006).** Future book additions could shift the
   corr boundary. Submit promptly.

5. **Depreciation/debt/PP&E are too weak for EXCELLENT.** These fields produce
   standalone S~0.8-1.0, insufficient to anchor an EXCELLENT blend even with
   strong analyst legs.
