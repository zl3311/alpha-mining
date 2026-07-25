---
id: "20260626-001"
date: "2026-06-26"
strategy: "EXPLORE"
research_question: "Can EPS revision flags (anl4_epsr_flag) combined with novel depreciation fields and structurally novel operator trees produce EXCELLENT+ submittable alphas?"
budget_used: 41
budget_cap: null
trigger: "cron_automation"
gate_passers: 12
submissions: 0
submittable_candidates: 2
status: "productive"
tags:
  - "daily_20260626"
  - "explore"
candidates:
  - id: "XgpJGaL0"
    grade: "EXCELLENT"
    sharpe: 2.08
    fitness: 2.36
    self_corr_value: 0.604
    self_corr_result: "PASS"
    verdict: "SAFE"
  - id: "MPp3WAd9"
    grade: "EXCELLENT"
    sharpe: 1.95
    fitness: 2.42
    self_corr_value: 0.662
    self_corr_result: "PASS"
    verdict: "SAFE"
---

# Session 20260626-001: EPS Revision + Depreciation Exploration

## Research Question

Can novel combinations of EPS revision flags (anl4_epsr_flag) with depreciation
value (fnd6_newqv1300_dpactq) produce EXCELLENT+ alphas that pass the self-corr
wall? Both fields are absent from the existing book, offering low self-corr risk.

## Strategy Rationale

EXPLORE mode chosen as default. Book is saturated (29 ACTIVE + 5 PENDING across
33 families). Factor-merge analysis identified anl4_epsr_flag as the top
decorrelating connector with fnd6 fields at rho ~ -0.35 and S_comb ~ 2.0-2.2.
At session time, neither field had been the primary anchor of a submitted alpha.

## Key Findings

- **EPS revision + depreciation blend is a new submittable EXCELLENT family**:
  `zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close)`
  reaches EXCELLENT (S=1.74, F=2.11) as a 2-factor, and EXCELLENT (S=2.08, F=2.36)
  as a 3-factor with `rank(open/close - 1)`.

- **Dynamic correlation (ts_corr) templates are dead**: All 4 variants were
  INFERIOR (S=0.52 to -0.37). ts_corr with fundamental fields produces no
  actionable signal.

- **Inter-field ratios (F1/F2) are dead**: All 4 ratio variants were INFERIOR
  (S=0.17 to 0.26). Fundamental ratios within fundamental6 produce no signal.

- **Event-magnitude depreciation works but stays at GOOD**: abs(ts_delta(
  fnd6_newqv1300_dpactq/close, 3)) + leverage + drlt reaches GOOD (S=1.77-1.80)
  but not EXCELLENT.

- **ts_sum window=22 confirmed as sweet spot for sparse flags**: Window=10 drops
  to GOOD (S=1.51), window=44 also GOOD (S=1.66). Consistent with the
  zscore-accumulated-revision pattern.

- **Intraday gap (open/close-1) is the strongest 3rd factor**: Adding drlt, buzz,
  or fatl keeps at GOOD; only open/close-1 lifts to EXCELLENT with S=2.08.

## Results Summary

| Batch | Size | Strategy | Gate-Passers | Best |
|-------|------|----------|-------------|------|
| batch_r1 | 20 | Novel structures + fields | 5 | O0p80V3R EXCELLENT S=1.74 |
| batch_r2_exploit | 10 | Winner mutations | 5 | XgpJGaL0 EXCELLENT S=2.08 |
| batch_r2_market | 1 | MARKET neut variant | 1 | omKWpQdn GOOD S=1.34 |
| batch_r3 | 10 | 3-factor + event-magnitude | 4 | MPp3WAd9 EXCELLENT S=1.95 |

## Submittable Candidates

| Alpha | Grade | Sharpe | Fitness | Self-Corr | Top Peer | Verdict |
|-------|-------|--------|---------|-----------|----------|---------|
| XgpJGaL0 | EXCELLENT | 2.08 | 2.36 | 0.604 PASS | 6Xzm6PQP (S=2.31) | SAFE |
| MPp3WAd9 | EXCELLENT | 1.95 | 2.42 | 0.662 PASS | xAn1LqXm (S=2.00) | SAFE |

## Next Steps

- Submit XgpJGaL0 (preferred: higher Sharpe, lower self-corr)
- Consider submitting MPp3WAd9 afterward (higher fitness, but higher self-corr)
- Explore 4-factor blends adding epsr to existing proven templates
- Test anl4_epsr_flag with IV spread fields (different family interaction)
