---
category: "dead_zone"
entity_type: "template"
template: "rank(ts_mean(scl12_buzz, 10)) * rank(abs(ts_delta(F / close, 5)))"
discovered: "20260715-001"
expressions_tested: 2
best_sharpe: 0.97
status: "dead_end"
confidence: "medium"
---

# Template: Buzz-Level x Event-Magnitude Product

Multiplying raw social-media attention LEVEL (`rank(ts_mean(scl12_buzz,10))`)
by a fundamental event-magnitude signal (`rank(abs(ts_delta(F/close,5)))`) —
a cross-family interaction distinct from the proven `buzz * (-1*returns)`
reversal stabilizer — produces weak, INFERIOR-grade signal.

## Evidence (session 20260715-001)

| Expression | S | F | T |
|-----------|---|---|---|
| `rank(ts_mean(scl12_buzz,10)) * rank(abs(ts_delta(fnd6_dpvieb/close,5)))` | 0.97 | 0.59 | 14.1% |
| `rank(ts_mean(scl12_buzz,10)) * rank(abs(ts_delta(fn_assets_fair_val_l2_q/close,5)))` | 0.51 | 0.22 | 10.9% |

## Why it fails

Attention LEVEL (how much a stock is being discussed) is largely
uninformative about direction or magnitude of expected returns on its own —
the proven buzz factor's power comes specifically from combining it with
`-1 * returns` (contrarian reversal on recent price moves), not from its raw
level. Multiplying two independently-weak-standalone rank signals (buzz level
alone is near-zero Sharpe; event-magnitude alone needs a leverage+stabilizer
blend to be usable) compounds their weaknesses rather than combining
strengths — neither component's "on" state reliably coincides with the
other's informative periods.

## Rule

Do not use raw `rank(ts_mean(scl12_buzz, d))` (attention level, no reversal
term) as a multiplicative gate/amplifier for other signals. Always pair
`scl12_buzz` with `-1 * returns` per the proven `buzz-stabilizer` and
`event-magnitude-buzz-boost` patterns.
