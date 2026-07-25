---
pattern: "volatility-gated-skew-news-product"
discovered: "20260616-001"
applicable_to: "option8 skew fields blended with news-flow / attention fields"
confidence: "medium"
---

# Pattern: Volatility-Gated Option-Skew News Product

## Template

```
trade_when(
  ts_std_dev(returns, 20) > 0.02,
  ts_decay_linear(rank(option_skew_field) * rank(ts_mean(news_flow_field, 22)), 5),
  ts_std_dev(returns, 20) < 0.01
)
```

Concrete discovery:

```
trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) * rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)
```

## When to Use

Use this when an option-skew field has weak standalone Sharpe but a decorrelated
news-flow partner in the factor-merge analysis. The volatility gate is essential:
plain additive blends were either turnover-heavy or low-fitness, while additive
volatility-gated variants stayed sub-universe blocked.

## Example

`YPpjReEW` reached AVERAGE grade with S=1.74, F=1.09, turnover 18.38%, all
computable BRAIN checks PASS, and BRAIN self-corr 0.4613 PASS.

## Caveat

This is a decorrelated filler pattern, not an EXCELLENT-grade breakthrough. Do
not spend a large budget mutating additive skew/news variants unless a new
mechanism explains why they should overcome the observed fitness and sub-universe
limits.
