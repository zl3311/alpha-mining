---
id: "20260608-001"
date: "2026-06-08"
strategy: "EXPLORE"
research_question: "Can zero-overlap analyst flags (epsr, netprofit, capex, fcf) with zscore normalization produce submittable alphas decorrelated from the 17-alpha book?"
budget_used: 48
budget_cap: null
trigger: "local_manual"
gate_passers: 15
submissions: 0
submittable_candidates: 1
status: "productive"
tags:
  - "20260608-001"
  - "explore_zero_overlap"
  - "novel_templates"
  - "zscore_sweep"
  - "netprofit_optimize"
candidates:
  - id: "vRmlGnkv"
    grade: "EXCELLENT"
    sharpe: 1.72
    fitness: 2.21
    self_corr_value: 0.593
    self_corr_result: "PASS"
    verdict: "SUBMITTABLE"
  - id: "E5KEzxzR"
    grade: "EXCELLENT"
    sharpe: 1.72
    fitness: 2.21
    self_corr_value: 0.594
    self_corr_result: "PASS"
    verdict: "REDUNDANT"
  - id: "rKWlGMmJ"
    grade: "GOOD"
    sharpe: 1.74
    fitness: 1.92
    self_corr_value: 0.668
    self_corr_result: "PASS"
    verdict: "REDUNDANT"
---

# Session 20260608-001: EXPLORE — Zero-Overlap Analyst Flags + zscore Discovery

## Research Question

Can untested analyst revision flags (epsr, netprofit, capex, fcf) combined with
zscore normalization produce EXCELLENT+ alphas decorrelated from the 17-alpha book?

## Answer: YES — EXCELLENT found and verified

**Primary candidate:** vRmlGnkv — EXCELLENT S=1.72 F=2.21, ALL 8 BRAIN checks PASS,
self-corr 0.593 (SAFE). Expression: `ts_decay_linear(zscore(ts_sum(anl4_netprofit_flag, 22)), 3)`.

## Key Discovery: zscore vs rank normalization

The critical insight of this session: `zscore()` normalization transforms INFERIOR
analyst revision signals into EXCELLENT alphas. The `rank()` operator produces
wrong-sign results for these sparse, event-driven flags at TOP3000.

| Field | rank(ts_sum(F, 22)) | zscore(ts_sum(F, 22)) | Improvement |
|-------|--------------------|-----------------------|-------------|
| anl4_netprofit_flag | S=-0.72 INFERIOR | S=1.71 EXCELLENT | +2.43 |
| anl4_epsr_flag | S=-0.61 INFERIOR | S=1.30 AVERAGE | +1.91 |
| anl4_capex_flag | S=1.28 INFERIOR | S=1.39 AVERAGE | +0.11 |
| anl4_fcf_flag | S=1.12 INFERIOR | S=1.15 INFERIOR | +0.03 |

The effect is dramatic for netprofit and epsr but marginal for capex and fcf.
Hypothesis: zscore works better for sparse flags with heavy zero-mass distributions,
where rank compresses all zeros to the same value but zscore captures deviation
from the zero-dominated mean.

## Rounds

### Round 1: Novel templates (25 sims)
- 1 gate-passer: zscore(ts_sum(anl4_epsr_flag, 22)), AVERAGE S=1.30
- All novel structures (trade_when, ts_corr, multi-horizon, directional gating) FAILED
- rank() produced wrong-sign results for all epsr expressions

### Round 2: zscore sweep (13 sims)
- **anl4_netprofit_flag zscore: EXCELLENT S=1.71 F=2.20** (key discovery)
- anl4_capex_flag zscore: AVERAGE S=1.39 F=1.17
- anl4_fcf_flag zscore: INFERIOR S=1.15
- MARKET neut boosts epsr from AVERAGE to GOOD (F=1.25→1.51)

### Round 3: netprofit optimization (10 sims)
- Decay=3 wrapper: S=1.72 F=2.21 (marginal improvement, became top candidate)
- Raw zscore (no wrapper): S=1.72 F=2.21 (identical)
- 44-day accumulation: S=1.66 F=2.05 (EXCELLENT, lower)
- 10-day accumulation: S=1.50 F=1.87 (GOOD)
- netprofit+capex blend: S=1.74 F=1.92 (GOOD, highest Sharpe but lower grade)
- Platform decay=10 variant: FAILS self-corr (0.713 vs O0998YVp)

## Self-Correlation Results

| Alpha | Expression | Self-Corr | Result |
|-------|-----------|-----------|--------|
| vRmlGnkv | decay_linear(zscore(netprofit, 22), 3) | 0.593 | PASS |
| E5KEzxzR | zscore(netprofit, 22) | 0.594 | PASS |
| GroLXj95 | decay_linear(zscore(netprofit, 22), 5) | 0.593 | PASS |
| P013zpWL | decay_linear(zscore(netprofit, 22), 10) | 0.593 | PASS |
| 2rKL6jp6 | decay_linear(zscore(netprofit, 44), 5) | 0.589 | PASS |
| rKWlGMmJ | netprofit + capex blend | 0.668 | PASS |
| 78d1MV28 | same expr, platform decay=10 | 0.713 | FAIL |

## Submission Queue

- **vRmlGnkv** (EXCELLENT S=1.72 F=2.21): QUEUED for manual submission
  - https://platform.worldquantbrain.com/alpha/vRmlGnkv

## Lessons Learned

1. **zscore >> rank for sparse analyst flags**: This is likely the most impactful
   discovery since the IV spread zscore template (20260604-001). Should be tested
   on ALL remaining analyst4 flags.

2. **Novel template structures were uniformly bad** for these fields: trade_when,
   ts_corr, multi-horizon spreads, directional gating — all produced negative
   Sharpe. The winning pattern is straightforward: `zscore(ts_sum(flag, d))`.

3. **Platform decay setting matters for self-corr**: decay=10 caused self-corr
   failure (0.713) while decay=6 passed (0.593). Higher platform decay compresses
   PnL differences, increasing apparent correlation.

4. **anl4_netprofit_flag is the champion zero-overlap field**: S=1.72, 100% positive
   years expected (all-weather regime from factor profile). It joins fnd6_itci and
   anl4_ptp_flag as a top-tier consistent factor.

## Next Steps

1. Submit vRmlGnkv on BRAIN platform
2. Test zscore pattern on remaining untested analyst4 flags
3. Explore zscore on fundamental6 fields (might unlock similarly hidden signals)
4. Record zscore normalization as a new knowledge pattern
