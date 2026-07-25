---
field: "fnd6_tlcf"
dataset: "fundamental6"
family: "tlcf_event_magnitude_buzz_blend"
discovery_session: "20260709-001"
best_sharpe: 2.13
best_fitness: 2.22
best_expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_tlcf / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
mechanism: "Sudden change in Tax Loss Carry Forward balance signals a discrete tax event (loss recognition/utilization/expiration) that the market under-reacts to short-term"
status: "active"
---

# Factor: fnd6_tlcf (Tax Loss Carry Forward)

## Economic Mechanism

`fnd6_tlcf` is a low-community-usage fundamental6 field (alphaCount 419, coverage
0.5) tracking a firm's accumulated tax loss carryforward balance. A large
short-window change (`abs(ts_delta(tlcf/close, 3))`) captures discrete tax events
(e.g., a loss year creating new carryforward capacity, or utilization/expiration
consuming it) that are not immediately or fully priced by the market, similar in
spirit to the `event-magnitude-abs-ts-delta` mechanism already proven on `fnd6_itci`.

## Best Known Expression

```
ts_decay_linear(rank(abs(ts_delta(fnd6_tlcf / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)
```

EXCELLENT: S=2.13, F=2.22, T=10.7%, self-corr 0.6262 PASS vs `d5Q3ZmWv` (`rKlo39p1`).

## Lessons

- Works well in the `event-magnitude-novel-fields` 4-factor template
  (`abs(ts_delta(tlcf/close,3)) + leverage + ivaco + drlt`): GOOD grade,
  S=1.91/F=1.79, self-corr **0.6372 PASS** (`blqLGagK`) — this is the safer,
  slightly-lower-fitness variant if a lower self-corr margin is preferred.
- Adding a `buzz-stabilizer` 5th factor (`rank(ts_mean(scl12_buzz,5)*(-1*returns))`)
  boosts GOOD→EXCELLENT (S 1.91→2.13, F 1.79→2.22) at a modest self-corr cost
  (0.6372→0.6262 — actually *slightly lower* in this instance, within noise).
- Using the RAW field (no `/close` normalization) boosts fitness further
  (F=2.14, S=2.27, `omlK5Qkv`) but raises local-PnL self-corr estimate to ~0.71
  (vs ~0.586 for the `/close`-normalized version) — BRAIN's authoritative
  `/check` did not resolve during this session; treat as HIGHER self-corr risk
  and prefer the `/close`-normalized form until re-verified.
- 3-factor form (no ivaco): GOOD only (F=1.22). Ivaco is necessary for EXCELLENT.
- Swapping `drlt`→`dlto`: fitness drops (F=1.63). Keep `drlt`.
- 2x-weighting the event leg: fitness collapses (F=1.09, AVERAGE). Do not
  upweight the event component — matches the `event-magnitude-novel-fields`
  "what doesn't work" finding for `ppegtq`.
- d=5 window on the event leg: lower fitness (F=1.82) than d=3. Keep d=3.
- Additional stabilizers tried and did NOT reach EXCELLENT: `fnd6_mrct/close`
  (F=1.07), `fn_prepaid_expense_q/close` (F=1.18) as a 6th factor.
