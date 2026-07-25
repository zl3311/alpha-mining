---
alpha_id: "6XEo91jO"
name: "event3d_leverage_buzz_reversal"
tags:
  - "event_magnitude"
  - "leverage"
  - "sentiment_reversal"
  - "fundamental6"
  - "fnd6_itci"
  - "equity_assets"
  - "scl12_buzz"
  - "abs_ts_delta"
  - "session_20260612-001"
  - "spectacular"
  - "sharpe_premium_escape"
expression: "rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))"
sharpe: 3.08
fitness: 2.53
turnover: 0.279
grade: "SPECTACULAR"
family: "event_leverage_sentiment_reversal"
mechanism: "Inventory event magnitude combined with financial leverage premium and high-coverage social buzz reversal. The buzz reversal stabilizer raises Sharpe enough to pass BRAIN self-correlation via the 1.10x Sharpe-premium escape."
fields:
  - "fnd6_itci"
  - "equity"
  - "assets"
  - "scl12_buzz"
  - "returns"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.7181
self_corr_peer: "omnopQ9k"
self_corr_verdict: "PASS"
brain_checks: "ALL_PASS"
status: "SUPERSEDED"
session: "20260612-001"
discovered: "2026-06-12"
brain_url: "https://platform.worldquantbrain.com/alpha/6XEo91jO"
superseded_by: "d5Q3ZmWv"
---

# 6XEo91jO — Event Magnitude + Leverage + Buzz Reversal

## Expression

`rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`

## Mechanism

Three-factor blend exploiting inventory event magnitude, intra-industry leverage
premium, and high-coverage social buzz reversal. The expression replaces the
deferred revenue stabilizer from `0m8GV1Pp` with `scl12_buzz * (-returns)`, which
raises Sharpe to 3.08 at the cost of higher but still acceptable turnover.

## Why Submittable

- Self-corr 0.7181 vs `omnopQ9k` would trigger the 0.70 gate, but BRAIN returns
  PASS because Sharpe 3.08 exceeds the 1.10x Sharpe-premium requirement.
- All computable BRAIN checks PASS.
- SPECTACULAR grade, S=3.08, F=2.53.
- Structurally distinct stabilizer from the existing event + deferred revenue
  candidate.

## Risk Assessment

The alpha depends on the Sharpe-premium escape rather than staying below the raw
0.70 correlation threshold. Recheck self-correlation immediately before official
submission if new event or sentiment alphas are activated first.

## Status

Superseded by `d5Q3ZmWv`, which keeps the same mechanism family but improves
fitness from 2.53 to 2.92 and reduces turnover from 27.9% to 18.3%.
