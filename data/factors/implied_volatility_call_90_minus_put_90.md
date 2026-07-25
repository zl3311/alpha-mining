---
field: "implied_volatility_call_90_minus_put_90"
dataset: "option8"
family: "options_iv_spread"
mechanism: "short_tenor_options_sentiment"
discovery_session: "20260614-003"
best_sharpe: 2.59
best_fitness: 4.33
best_expression: "trade_when(ts_std_dev(returns, 20) > 0.02, zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), ts_std_dev(returns, 20) < 0.01)"
best_alpha_id: "Gro21wWG"
status: "active"
in_submitted_book: false
---

# Factor: implied_volatility_call_90_minus_put_90

## Economic Mechanism

The 90-day call-put implied volatility spread measures short-tenor option-market
pricing of upside versus downside risk. It is most predictive during elevated
realized-volatility regimes, when option skew is actively repriced and less likely
to reflect stale low-volatility positioning.

## Best Known Expression

```
trade_when(ts_std_dev(returns, 20) > 0.02, zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), ts_std_dev(returns, 20) < 0.01)
```

Settings: USA TOP3000, MARKET neutralization, platform decay 10.

## Lessons

- Pure smoothed IV90 spread variants can produce SPECTACULAR aggregate metrics but
  fail BRAIN `CONCENTRATED_WEIGHT`.
- A realized-volatility trade gate repairs concentration while retaining
  SPECTACULAR quality.
- The current best candidate, `Gro21wWG`, passes self-correlation only through the
  Sharpe-premium escape, so recheck before official submission.
