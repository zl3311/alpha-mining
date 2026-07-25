---
category: "pattern"
discovered: "20260614-003"
applicable_to: "options_iv_spread, option8, implied_volatility_90"
best_alpha_id: "Gro21wWG"
best_sharpe: 2.59
best_fitness: 4.33
---

# IV90 Volatility-Gated Spread

## Template

```
trade_when(
  ts_std_dev(returns, 20) > 0.02,
  zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)),
  ts_std_dev(returns, 20) < 0.01
)
```

Use MARKET neutralization and platform decay 10.

## When to Use

Use this template for short-tenor option spread signals when pure
`zscore(ts_mean(...))` variants have strong aggregate metrics but fail
`CONCENTRATED_WEIGHT`. The realized-volatility gate removes low-volatility stale
positioning and allows the 90-day call-put spread to trade only when option skew is
informative.

## Example

`Gro21wWG`:

- SPECTACULAR, S=2.59, F=4.33, turnover 6.08%.
- BRAIN checks: all pass.
- Self-correlation: PASS at 0.8802 via Sharpe-premium escape.

## Anti-Patterns

- Pure IV90 zscore/ts_mean with outer decay reached higher aggregate fitness but
  failed `CONCENTRATED_WEIGHT` at approximately 0.50.
- Adding `rank(historical_volatility_180)` did not repair concentration.
- Treat variants as likely mutually correlated until BRAIN `/check` verifies the
  Sharpe-premium escape.
