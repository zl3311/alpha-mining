---
alpha_id: "omY3pZq2"
name: "sentiment_buzz_iv_spread_multiplicative"
tags:
  - "social"
  - "options"
  - "scl12"
  - "option8"
  - "iv_spread"
  - "multiplicative"
  - "spectacular"
  - "session_20260606-001"
expression: "ts_decay_linear(rank(ts_mean(scl12_buzz, 5)) * zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)), 5)"
sharpe: 2.13
fitness: 3.18
turnover: 0.112
grade: "SPECTACULAR"
family: "sentiment_iv_spread"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.824
self_corr_peer: "vRm07LP3"
self_corr_verdict: "PASS_SHARPE_PREMIUM"
status: "ACTIVE"
brain_checks: "ALL_PASS"
brain_url: "https://platform.worldquantbrain.com/alpha/omY3pZq2"
---

# omY3pZq2 — Sentiment Buzz × IV Spread

Multiplicative interaction between social media buzz (5-day smoothed) and options IV call-put spread (22-day smoothed). Captures when informed options positioning aligns with rising social attention.

## Expression

```
ts_decay_linear(rank(ts_mean(scl12_buzz, 5)) * zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)), 5)
```

## Self-Correlation Note

BRAIN self-corr = 0.824 vs `vRm07LP3` (options_iv_spread, S=1.82). Passes via Sharpe premium escape: 2.13 > 1.10 × 1.82 = 2.002. This is the first confirmed Sharpe premium pass in the book.

## Mechanism

Social media buzz (scl12_buzz) captures retail/institutional attention momentum. IV call-put spread reflects informed options traders pricing upside vs downside. The multiplicative interaction isolates stocks where BOTH attention is rising AND options markets tilt bullish — a stronger signal than either alone.
