---
id: "20260606-002"
date: "2026-06-06"
strategy: "EXPLORE"
research_question: "Can cash flow quality, earnings yield, and analyst CF revision fields produce EXCELLENT+ alphas decorrelated from the 14-alpha book?"
budget_used: 0
budget_cap: null
trigger: "local_manual"
gate_passers: 0
submissions: 0
submittable_candidates: 0
status: "abandoned"
tags:
  - "20260606-002"
  - "explore_cashflow"
  - "zero_overlap"
---

# Session 20260606-002: EXPLORE — Cash Flow / Earnings Yield (Zero Book Overlap)

> **Abandoned before any simulations ran** (`budget_used: 0`). Only the plan below was
> written. Retained because the target-field selection shows how zero-overlap field sets
> were chosen.

## Research Question

After discovering that BRAIN self-corr uses a ~1.5x multiplier on shared-field
alphas (session 20260606-001), can we find EXCELLENT+ alphas using fields that have
ZERO overlap with the 14-alpha book?

## Target Fields

Cash flow: cashflow_op, capex, cashflow_fin
Earnings yield: ebitda, eps, operating_income  
Balance sheet: bookvalue_ps, equity, assets, debt
Analyst CF revisions: anl4_capex_flag, anl4_fcf_flag, anl4_epsr_flag, anl4_netprofit_flag
Sentiment direction: scl12_sentiment
Historical vol: parkinson_volatility_120
