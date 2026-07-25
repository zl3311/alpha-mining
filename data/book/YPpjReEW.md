---
alpha_id: "YPpjReEW"
name: "exp20260616-001_skew_news_vol_product"
tags:
  - "session_20260616-001"
  - "skew-news"
  - "volatility-regime"
submitted: null
session: "20260616-001"
grade: "AVERAGE"
sharpe: 1.74
fitness: 1.09
turnover: 0.1838
expression: "trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) * rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)"
family: "options_news_volatility_regime"
neutralization: "SUBINDUSTRY"
decay: 6
self_corr_max: 0.4613
status: "PENDING"
brain_url: "https://platform.worldquantbrain.com/alpha/YPpjReEW"
---

# Alpha: YPpjReEW

## Expression
```
trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) * rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)
```

## Mechanism

This alpha tests the option-skew/news-flow diversification thesis. It is long
stocks where 360-day implied-volatility mean skew is high and smoothed opening
news volatility is high, but only during elevated realized-volatility regimes.
The product form requires both option-market asymmetry and news-flow attention,
while the `trade_when` wrapper avoids trading the weak low-volatility regime.

## Self-Correlation Profile

BRAIN self-correlation check passed with max self-corr 0.4613, well below the
0.70 threshold. This is lower than recent AVERAGE filler candidates and supports
the hypothesis that option-skew/news-flow interactions add a genuinely
decorrelating book leg.

## Post-Submission

PENDING. Human decides whether to submit given the AVERAGE grade. If submitted,
flip status to ACTIVE and set the submitted date.
