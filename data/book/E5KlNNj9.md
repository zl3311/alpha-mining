---
alpha_id: "E5KlNNj9"
name: "leverage_drlt_blend"
tags:
  - "leverage"
  - "fundamental6"
  - "fnd6_drlt"
  - "equity_assets"
  - "session_20260609-001"
  - "good"
expression: "ts_decay_linear(rank(-1 * equity / assets) + rank(fnd6_drlt / close), 5)"
sharpe: 1.88
fitness: 1.58
turnover: 0.017
grade: "GOOD"
family: "leverage_fundamental"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.564
status: "SUPERSEDED"
session: "20260609-001"
brain_url: "https://platform.worldquantbrain.com/alpha/E5KlNNj9"
---

# E5KlNNj9

Leverage premium + deferred revenue quality blend. First leverage-family alpha in the book.

## Expression

```
ts_decay_linear(rank(-1 * equity / assets) + rank(fnd6_drlt / close), 5)
```

## Simulation Settings

| Setting | Value |
|---------|-------|
| Region | USA |
| Universe | TOP3000 |
| Delay | 1 |
| Decay | 6 |
| Neutralization | SUBINDUSTRY |
| Truncation | 0.08 |

## Pre-Submission Checks (2026-06-09)

| Check | Result |
|-------|--------|
| Sharpe | 1.88 (PASS, limit 1.25) |
| Fitness | 1.58 (PASS, limit 1.0) |
| Turnover | 1.7% (PASS) |
| LOW_SUB_UNIVERSE_SHARPE | PASS |
| CONCENTRATED_WEIGHT | PASS |
| All 8 BRAIN checks | PASS |
| Self-corr vs book (BRAIN) | 0.564 SAFE |

## Mechanism

High leverage (low equity/assets) combined with deferred revenue quality
(fnd6_drlt/close) captures an intra-industry capital structure risk premium.
Within the same subindustry, firms that choose higher financial leverage tend to
outperform — this is the classic leverage anomaly where the debt-equity risk
premium is not fully explained by systematic risk. The deferred revenue component
(fnd6_drlt) adds a quality tilt toward firms with predictable future revenue
recognition, which complements the risk-taking signal from leverage.

The leverage effect is purely intra-industry (S=1.55 SUBINDUSTRY vs S=0.72
MARKET), confirming that the risk premium operates within industry peer groups
where leverage is a deliberate strategic choice, not a cross-industry artifact.

## Self-Correlation Profile

| Book Alpha | Family | Corr |
|------------|--------|------|
| 6Xzm6PQP | guidance_fundamental | 0.564 |
| Top peer across all book entries | | 0.564 |

Novel mechanism family — first leverage/capital-structure alpha in the book.

## Alternatives (same session, same family — do NOT submit multiple)

| Alpha ID | Expression | S | F | Self-Corr |
|----------|-----------|---|---|-----------|
| j2gjVLWQ | rank(-1*equity/assets) + rank(fnd6_drlt/close) | 1.87 | 1.57 | 0.565 |
| 78djRjAO | rank(-1*equity/assets) + zscore(ts_sum(anl4_ptp_flag, 22)) | 1.77 | 1.74 | 0.595 |
| 1YgwAVxz | zscore(-1*equity/assets) + rank(fnd6_itci/close) | 1.72 | 1.66 | 0.350 |
| A13lQM7E | ts_decay_linear(rank(-1*equity/assets), 5) | 1.55 | 1.28 | 0.572 |
