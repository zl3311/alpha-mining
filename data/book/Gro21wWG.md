---
alpha_id: "Gro21wWG"
name: "iv90_vol_gated_spread"
tags:
  - "options"
  - "iv_spread"
  - "iv90"
  - "vol_regime"
  - "trade_when"
  - "market_neutral"
  - "session_20260614-003"
  - "spectacular"
  - "sharpe_premium_escape"
expression: "trade_when(ts_std_dev(returns, 20) > 0.02, zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), ts_std_dev(returns, 20) < 0.01)"
sharpe: 2.59
fitness: 4.33
turnover: 0.0608
grade: "SPECTACULAR"
family: "iv90_vol_regime_spread"
mechanism: "Short-tenor call-put implied volatility spread traded only in elevated realized-volatility regimes. The signal captures option-market upside/downside pricing when volatility is high enough for the 90-day spread to be informative, while the exit gate avoids low-volatility stale positioning."
fields:
  - "implied_volatility_call_90"
  - "implied_volatility_put_90"
  - "returns"
neutralization: "MARKET"
decay: 10
universe: "TOP3000"
region: "USA"
self_corr_max: 0.8802
self_corr_peer: null
self_corr_verdict: "PASS"
brain_checks: "ALL_PASS"
status: "PENDING"
session: "20260614-003"
discovered: "2026-06-14"
brain_url: "https://platform.worldquantbrain.com/alpha/Gro21wWG"
---

# Gro21wWG — IV90 Volatility-Gated Spread

## Expression

`trade_when(ts_std_dev(returns, 20) > 0.02, zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), ts_std_dev(returns, 20) < 0.01)`

## Mechanism

This alpha uses the 90-day call-put implied volatility spread as an options-market
sentiment signal, but only holds it during elevated realized-volatility regimes.
The regime gate appears to solve the concentration problem that blocked pure
IV90 zscore/ts_mean variants while preserving the short-tenor options signal.

## Why Submittable

- BRAIN `/check` reports all computable checks PASS.
- BRAIN `SELF_CORRELATION` reports PASS at 0.8802; the pass depends on the
  Sharpe-premium escape because S=2.59 is high enough despite raw correlation
  above 0.70.
- SPECTACULAR grade, S=2.59, F=4.33, turnover 6.08%.

## Risk Assessment

The full `/correlations/self` peer breakdown timed out during the session, so the
top correlated peer is not recorded. The `/check` endpoint is authoritative and
returned PASS, but recheck immediately before official submission if another
options/IV alpha is activated first.
