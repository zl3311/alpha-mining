---
alpha_id: "vRmlGnkv"
name: "netprofit_revision_zscore_accumulated"
grade: "EXCELLENT"
sharpe: 1.72
fitness: 2.21
turnover: 0.081
returns: null
family: "analyst_revision_zscore"
mechanism: "Accumulated analyst net profit revision intensity via cross-sectional zscore normalization"
fields:
  - "anl4_netprofit_flag"
expression: "ts_decay_linear(zscore(ts_sum(anl4_netprofit_flag, 22)), 3)"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.593
self_corr_peer: "vR56vdYd"
brain_url: "https://platform.worldquantbrain.com/alpha/vRmlGnkv"
status: "ACTIVE"
session: "20260608-001"
discovered: "2026-06-08"
tags:
  - "analyst4"
  - "netprofit"
  - "zscore"
  - "accumulated_revision"
  - "zero_overlap"
---

# vRmlGnkv — Accumulated Net Profit Revision (zscore)

## Expression

```
ts_decay_linear(zscore(ts_sum(anl4_netprofit_flag, 22)), 3)
```

## Mechanism

Captures accumulated analyst net profit revision momentum over 22 trading days.
The `ts_sum` accumulates revision flags (each occurrence adds +1 or -1),
measuring persistent positive/negative revision trends. The `zscore`
normalization is critical — `rank()` produces wrong-sign results at TOP3000
because the flag distribution is sparse (mostly zeros with discrete events).
`zscore` better captures the deviation from the cross-sectional mean.

## Key Discovery

This field was previously profiled as INFERIOR (S=0.72 with `rank`, S=-0.55
with `ts_decay_linear(rank(...))` at TOP3000). The zscore normalization
transforms it into EXCELLENT (S=1.72, F=2.21) — a 2.4x Sharpe improvement.
The same pattern applies to anl4_epsr_flag (S=-0.61 with rank → S=1.30 with
zscore) and anl4_capex_flag (S=1.28 with rank → S=1.39 with zscore).

## Self-Correlation

- Max self-corr: 0.593 vs vR56vdYd (analyst_revision, S=2.86)
- BRAIN check: PASS (below 0.70 threshold)
- Uses anl4_netprofit_flag (not in any existing book entry)

## BRAIN Checks

All 8 checks PASS (7 computable + SELF_CORRELATION confirmed via API).

## Alternatives (same mechanism, de-duplicated)

- E5KEzxzR: `zscore(ts_sum(anl4_netprofit_flag, 22))` — S=1.72, F=2.21, simpler
- GroLXj95: decay=5 variant — S=1.71, F=2.20
- P013zpWL: decay=10 variant — S=1.70, F=2.18
- 2rKL6jp6: 44-day accumulation — S=1.66, F=2.05
