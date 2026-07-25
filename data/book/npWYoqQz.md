---
alpha_id: "npWYoqQz"
name: "iv_spread_fundamental_analyst_blend"
tags:
  - "options"
  - "fundamental"
  - "analyst"
  - "option8"
  - "fundamental6"
  - "analyst4"
  - "blend"
  - "spectacular"
expression: "ts_decay_linear(zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)) + rank(fnd6_dlto / close) + rank(fnd6_itci / close) + rank(anl4_netdebt_flag), 5)"
sharpe: 2.09
fitness: 3.02
turnover: 0.049
grade: "SPECTACULAR"
family: "iv_fundamental_analyst_blend"
neutralization: "MARKET"
decay: 6
universe: "TOP3000"
region: "USA"
status: "ACTIVE"
brain_checks: "ALL_PASS"
---

# npWYoqQz — IV Spread + Fundamental + Analyst Blend

Additive blend of three signals: z-scored smoothed IV call-put skew (270-day), two fundamental price ratios (dlto/close, itci/close), and analyst net-debt flag. Wrapped in ts_decay_linear(5).

## Platform URL

https://platform.worldquantbrain.com/alpha/npWYoqQz
