---
id: "20260604-001"
date: "2026-06-04"
strategy: "REFINE"
research_question: "Resolve H-006 IV spread CONCENTRATED_WEIGHT and find submittable uncorrelated options alpha"
budget_used: 68
budget_cap: null
trigger: "manual"
gate_passers: 8
submissions: 0
status: "productive"
tags:
  - "20260604-001"
  - "refine_iv_spread"
  - "zscore_r3"
  - "H-006"
---

# Session 20260604-001: IV Spread REFINE — Submittable EXCELLENT

## Research Question

Can call-put IV spread produce a submittable EXCELLENT alpha that passes all BRAIN checks and self-correlation vs the 14-alpha book?

## Strategy Rationale

H-006 was BLOCKED on CONCENTRATED_WEIGHT when blended with fundamentals. Session started with pure options REFINE (no fundamentals), then auto-iterated `group_neutralize` variants (EXCELLENT metrics but still blocked), then pivoted to the zscore + ts_mean path from 9qRoMPAo (GOOD, ALL PASS).

## Key Findings

- **Submittable candidate:** [vRm07LP3](https://platform.worldquantbrain.com/alpha/vRm07LP3) — EXCELLENT S=1.82 F=2.35, ALL PASS, self-corr 0.309
- `group_neutralize(IV spread)` hits EXCELLENT but fails CONCENTRATED_WEIGHT + SUB_UNIVERSE on all variants
- `zscore(ts_mean(IV spread, 22))` + MARKET + decay=10 is the winning template
- Longer ts_mean window (22 vs 5) upgrades GOOD → EXCELLENT while preserving check compliance
- pcr_oi_270 standalone is DEAD; buzz addition (`+ buzz`) causes unit errors

## Next Steps

- User submits vRm07LP3 manually on BRAIN
- Update book entry status to ACTIVE after submission
- Optional: test ts_mean windows 15–30 for marginal fitness gains (diminishing returns expected)
