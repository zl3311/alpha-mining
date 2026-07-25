---
type: "submit-candidate"
alpha_id: "6XEo91jO"
status: "SUPERSEDED"
priority: "high"
grade: "SPECTACULAR"
sharpe: 3.08
fitness: 2.53
turnover: 0.279
self_corr_max: 0.7181
neutralization: "SUBINDUSTRY"
decay: 6
family: "event_leverage_sentiment_reversal"
session: "20260612-001"
brain_url: "https://platform.worldquantbrain.com/alpha/6XEo91jO"
queued: "2026-06-12"
superseded_by: "d5Q3ZmWv"
---

# Submit 6XEo91jO (Event + Leverage + Buzz Reversal)

## Expression

`rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`

## Why Submittable

- BRAIN self-corr check PASS at 0.7181 vs `omnopQ9k`; this relies on the
  Sharpe-premium escape because S=3.08 exceeds the 1.10x requirement.
- All computable BRAIN checks PASS.
- SPECTACULAR grade, S=3.08, F=2.53.

## Risk Assessment

Recheck before official submission if `0m8GV1Pp`, `xAn2kvOp`, or another
event/sentiment alpha is activated first, because this candidate is already just
above the raw 0.70 self-correlation threshold.

## Reviewer Action

Do not submit by default. This candidate was superseded by `d5Q3ZmWv`, which has
higher fitness and lower turnover in the same mechanism family.
