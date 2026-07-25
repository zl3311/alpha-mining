---
alpha_id: "d5Q3ZmWv"
name: "event3d_leverage_buzz_decay3"
tags:
  - "event_magnitude"
  - "leverage"
  - "sentiment_reversal"
  - "fundamental6"
  - "fnd6_itci"
  - "equity_assets"
  - "scl12_buzz"
  - "abs_ts_delta"
  - "decay_linear"
  - "session_20260612-001"
  - "spectacular"
  - "best_variant"
  - "sharpe_premium_escape"
expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 3)"
sharpe: 2.97
fitness: 2.92
turnover: 0.183
grade: "SPECTACULAR"
family: "event_leverage_sentiment_reversal"
mechanism: "Smoothed inventory event magnitude plus financial leverage premium and high-coverage social buzz reversal. A light ts_decay_linear wrapper lowers turnover and lifts fitness while preserving enough Sharpe to pass BRAIN self-correlation via the premium escape."
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
self_corr_max: 0.7163
self_corr_peer: "0m8GV1Pp"
self_corr_verdict: "PASS"
brain_checks: "ALL_PASS"
status: "ACTIVE"
session: "20260612-001"
discovered: "2026-06-12"
brain_url: "https://platform.worldquantbrain.com/alpha/d5Q3ZmWv"
supersedes:
  - "6XEo91jO"
---

# d5Q3ZmWv — Smoothed Event Magnitude + Leverage + Buzz Reversal

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 3)`

## Mechanism

This is the best Round 2 refinement of the event + leverage + buzz reversal
family. It keeps the same economic structure as `6XEo91jO` but adds a light
time-series decay wrapper, reducing turnover from 27.9% to 18.3% and increasing
fitness from 2.53 to 2.92.

## Why Submittable

- BRAIN self-corr check PASS at 0.7163 vs `0m8GV1Pp`; this relies on the
  Sharpe-premium escape because S=2.97 exceeds the 1.10x requirement.
- All computable BRAIN checks PASS.
- SPECTACULAR grade, S=2.97, F=2.92.
- Supersedes `6XEo91jO` as the best event + leverage + buzz reversal variant.

## Risk Assessment

This candidate depends on the Sharpe-premium escape rather than staying below
the raw 0.70 threshold. Recheck before official submission if `0m8GV1Pp` or
another event-family alpha is activated first.

## Post-Submission

BRAIN check reported this alpha as ACTIVE on 2026-06-17.
