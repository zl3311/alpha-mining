---
type: "submit-candidate"
alpha_id: "d5Q3ZmWv"
status: "SUBMITTED"
priority: "high"
grade: "SPECTACULAR"
sharpe: 2.97
fitness: 2.92
turnover: 0.183
self_corr_max: 0.7163
neutralization: "SUBINDUSTRY"
decay: 6
family: "event_leverage_sentiment_reversal"
session: "20260612-001"
brain_url: "https://platform.worldquantbrain.com/alpha/d5Q3ZmWv"
queued: "2026-06-12"
supersedes: "6XEo91jO"
---

# Submit d5Q3ZmWv (Smoothed Event + Leverage + Buzz Reversal)

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 3)`

## Why Submittable

- BRAIN self-corr check PASS at 0.7163 vs `0m8GV1Pp`; this relies on the
  Sharpe-premium escape because S=2.97 exceeds the 1.10x requirement.
- All computable BRAIN checks PASS.
- SPECTACULAR grade, S=2.97, F=2.92.
- Supersedes `6XEo91jO` with materially better fitness and lower turnover.

## Risk Assessment

Recheck before official submission if `0m8GV1Pp`, `6XEo91jO`, or another
event-family alpha is activated first, because the raw self-correlation is above
0.70 and the PASS depends on the Sharpe-premium escape.

## Reviewer Action

BRAIN check reported this alpha as ACTIVE on 2026-06-17. `data/book/d5Q3ZmWv.md`
has been flipped to `status: ACTIVE`.
