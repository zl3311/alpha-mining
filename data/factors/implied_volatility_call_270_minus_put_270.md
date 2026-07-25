---
field: "implied_volatility_call_270_minus_put_270"
dataset: "option8"
family: "options_iv_spread"
mechanism: "options_sentiment"
status: "active"
coverage: 0.97
standalone_sharpe: 1.79
standalone_fitness: 0.87
best_sharpe: 1.82
best_fitness: 2.35
best_expression: "ts_decay_linear(zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)), 10)"
best_alpha_id: "vRm07LP3"
in_submitted_book: true
discovery_session: "20260604-001"
note: "Submittable via zscore+ts_mean template (MARKET). group_neutralize path blocked on CONCENTRATED_WEIGHT."
---

# implied_volatility_call_270_minus_put_270

Call-put IV spread (270-day maturity). Forward-looking options sentiment.

## Mechanism

When call IV exceeds put IV, the options market prices upside potential above downside risk. Standalone `rank(spread)` is strong (S=1.79) but sub-gate on fitness. The submittable form smooths with `ts_mean(..., 22)`, cross-sectionally z-scores, and decay-wraps — passing all BRAIN checks at EXCELLENT grade with self-corr 0.309.

## Best Known Expression

```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)), 10)
```

Alpha vRm07LP3 — EXCELLENT S=1.82 F=2.35, MARKET neut, decay=10.

## Lessons

- Pure options only — fundamental blends fail CONCENTRATED_WEIGHT
- `group_neutralize` achieves higher Sharpe but cannot pass BRAIN checks
- Longer ts_mean window (22) is the key upgrade from GOOD to EXCELLENT
