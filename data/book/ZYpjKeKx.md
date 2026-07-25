---
alpha_id: "ZYpjKeKx"
status: "ACTIVE"
submitted: "2026-07-06"
grade: "EXCELLENT"
fields:
  - "fn_accrued_liab_q"
  - "anl4_cfi_flag"
  - "anl4_bvps_flag"
  - "scl12_buzz"
expression: "rank(abs(ts_delta(fn_accrued_liab_q / close, 3))) + rank(anl4_cfi_flag) + rank(anl4_bvps_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))"
sharpe: 2.49
fitness: 2.25
turnover: 0.278
neutralization: "SUBINDUSTRY"
decay: 6
region: "USA"
universe: "TOP3000"
self_corr_max: 0.750
self_corr_peer: "zqOrkbbG"
self_corr_result: "PASS"
self_corr_method: "brain_check"
family: "accrued_liability_event_magnitude"
session: "20260622-001"
verified_session: "20260706-001"
brain_url: "https://platform.worldquantbrain.com/alpha/ZYpjKeKx"
tags:
  - "fn_accrued_liab_q"
  - "event_magnitude"
  - "analyst_revision"
  - "sentiment_reversal"
---

# ZYpjKeKx — Accrued Liability Event-Magnitude Blend

## Expression

`rank(abs(ts_delta(fn_accrued_liab_q / close, 3))) + rank(anl4_cfi_flag) + rank(anl4_bvps_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`

## Mechanism

Four-factor blend using the event-magnitude transform on accrued liabilities:

1. **Accrued liability event magnitude** (`rank(abs(ts_delta(fn_accrued_liab_q / close, 3)))`):
   Captures the absolute magnitude of 3-day changes in accrued liabilities relative to price.
   Large changes in either direction signal active balance sheet management. The `abs()` wrapper
   converts this from directional (bullish/bearish) to a volatility-of-fundamentals signal:
   firms with large accrued liability movements are more actively restructuring, and this
   cross-sectional spread predicts returns.

2. **Cash flow revision** (`rank(anl4_cfi_flag)`): Upward cash flow estimate revisions signal
   improving operational quality before it hits reported numbers.

3. **Book value revision** (`rank(anl4_bvps_flag)`): Rising book value per share estimates
   indicate balance sheet strengthening, confirmed by multiple analysts.

4. **Sentiment reversal** (`rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`): Stocks with
   positive social buzz but recent price declines — contrarian signal on attention-driven
   overselling.

## Self-Correlation

Max self-corr: 0.750 vs zqOrkbbG (S=1.82). Passes via Sharpe premium (2.49 > 2.002).

| Peer | Corr | Peer Sharpe | 1.1x Threshold | Status |
|------|------|-------------|----------------|--------|
| zqOrkbbG | 0.750 | 1.82 | 2.002 | PASS (+0.488 margin) |
| xARzmVEW | 0.736 | 2.05 | 2.255 | PASS (+0.235 margin) |
| 0mzQQvX8 | 0.595 | 2.43 | — | auto-PASS (< 0.7) |
| np30Odjd | 0.557 | 1.87 | — | auto-PASS (< 0.7) |
| pw8wNe76 | 0.553 | 2.09 | — | auto-PASS (< 0.7) |

## Key Insight

The `abs(ts_delta(field/close, d))` event-magnitude wrapper changes the operator tree shape
compared to the raw `rank(field/close)` template used in existing book entries (zqOrkbbG,
xARzmVEW). This structural novelty reduces BRAIN self-corr from 0.83 (raw form, blvvlQAR)
to 0.75 (event-magnitude form) while maintaining EXCELLENT grade. The wider Sharpe premium
margin (+0.235 vs xARzmVEW) makes this substantially more robust than omVpwdqk (+0.009).
