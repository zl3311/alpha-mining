---
id: "20260614-003-learnings"
session: "20260614-003"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260614-003

## What Worked

- MARKET-neutral IV90/IV180 spread variants produced extremely strong aggregate
  metrics: 10/10 candidates gate-passed, with 9 SPECTACULAR grades.
- A volatility-regime gate solved the concentration problem for the IV90 spread:
  `Gro21wWG` passed all BRAIN checks with S=2.59 and F=4.33.
- The 90-day call-put IV spread is materially stronger than the previously
  documented 270-day template when the expression is gated by realized volatility.

## What Didn't Work

- Pure IV90 zscore/ts_mean templates with outer decay reached S=2.57-2.75 and
  F=4.14-4.63 but failed `CONCENTRATED_WEIGHT` at approximately 0.50.
- Adding `rank(historical_volatility_180)` to IV90/IV180 did not fix
  concentration.
- The older queue's stored self-correlation values are stale after recent
  submissions; `pw7j2MXg`, `mLX0gm5x`, and `78dvZ3r2` are now BRAIN self-corr
  blocked despite prior or local correlation evidence.

## New Pattern

Volatility-gated short-tenor IV spread:

`trade_when(ts_std_dev(returns, 20) > 0.02, zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), ts_std_dev(returns, 20) < 0.01)`

Use MARKET neutralization and platform decay 10. This preserves the short-tenor
options sentiment signal while avoiding the concentration failure that blocks
pure smoothed IV90 spread variants.

## Mechanism Insight

Short-tenor option skew appears most informative when realized volatility is
already elevated. In quiet regimes, the same smoothed spread creates stale,
concentrated positions; in higher-volatility regimes, it behaves like a
tradable options-market sentiment signal and earns enough Sharpe to pass
self-correlation via the premium escape.

## Next Steps

- Recheck `Gro21wWG` immediately before manual submission because its self-corr
  PASS depends on the Sharpe-premium escape.
- Follow up on `qMXa9XlP`, `pw72YJ8v`, `LLRvV6V1`, and `mLXGw2R2` with sequential
  BRAIN self-correlation checks after rate limits cool down.
- Explore IV90 regime gates with slightly different realized-volatility thresholds
  only after `Gro21wWG` is acted on, because variants may be mutually redundant.
