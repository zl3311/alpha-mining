---
pattern: "event-magnitude-recency-arg-max"
discovered: "20260715-001"
applicable_to: "event-magnitude family (fundamental6/fundamental2 anchors), structural-novelty search"
confidence: "medium (1 anchor field tested, 2 window variants)"
best_alpha_id: "blqKkP2l (BLOCKED, not submitted — see caveat)"
---

# Pattern: `ts_arg_max`-Based Recency-of-Shock Is a Viable But Higher-Self-Corr Alternative to Additive Event-Magnitude

## The finding

Wrapping the event-magnitude anchor in `ts_arg_max` to measure RECENCY of the
largest recent shock, instead of the event's raw magnitude, is a genuinely
novel operator-tree shape (not present anywhere in `data/factors/` or prior
`data/knowledge/patterns/` entries) that reaches comparable-or-better
aggregate Sharpe/Fitness than the standard additive form, but correlates
noticeably HIGHER with the book than the additive `ts_decay_linear(rank(...) +
rank(...) + ...)` form on the identical anchor + stabilizer set.

## Template

```
rank(-1 * ts_arg_max(abs(ts_delta(FIELD / close, 1)), WINDOW)) + rank(-1 * equity / assets) + rank(STABILIZER_1 / close) + rank(STABILIZER_2 / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))
```

`ts_arg_max(x, d)` returns the number of trading days since the max of `x`
occurred within the trailing window (0 = today). Negating and ranking makes
"a large event happened very recently" score high — the economic hypothesis
is that markets underreact fastest right after a shock and the mispricing
decays as the event ages out of memory, a genuinely different mechanism from
the additive form's "the event size itself is the signal, regardless of
recency."

## Evidence (session 20260715-001, anchor `fn_assets_fair_val_l2_q`)

| Variant | S | F | T | Self-corr vs book | Verdict |
|---------|---|---|---|--------------------|---------|
| `ts_arg_max` + leverage + ivaco + drlt + buzz (WINDOW=20) | 2.55 | 2.03 | 20.9% | **0.701** vs `YP0bLdzA` | BLOCKED (0.001 over threshold; Sharpe 2.55 falls 0.002 short of the 1.10x=2.552 premium escape) |
| `ts_arg_max` + leverage + ivaco + buzz (no drlt, WINDOW=20) | 2.53 | 1.83 | 23.4% | not checked (lower fitness, deprioritized) | n/a |
| `ts_arg_max` + leverage + drlt + buzz (no ivaco, WINDOW=20) | 2.26 | 1.65 | 23.6% | not checked | n/a |
| `ts_arg_max` + leverage + drlt + buzz (WINDOW=40) | 2.01 | 1.44 | 21.8% | not checked | AVERAGE, window=40 clearly worse than 20 |
| **Additive form, same anchor+stabilizers** (`lelNqEZl`) | 2.01 | 2.01 | 11.0% | **0.567** vs `YP0bLdzA` | **SAFE** |

The `ts_arg_max` form has ~2x the turnover of the additive form (21-23% vs
11%) on the identical field set — recency-gating trades much more often than
smoothed magnitude-ranking, which is the likely driver of both its higher raw
Sharpe (more trades = more compounding of the same edge) AND its higher
self-correlation (more overlapping trade days with the book's other
high-turnover event-magnitude members).

## When to use

- As a genuinely novel structural variant when the additive form on a given
  anchor is already self-corr BLOCKED and a different wrapper might shift the
  correlation profile enough to pass — worth trying, but do NOT assume it will
  be LOWER corr than the additive form; empirically it was higher here.
- Prefer the additive form when self-corr margin matters more than raw
  Sharpe, since it achieved equal fitness at much lower turnover and
  correlation on the same anchor+stabilizer set in this test.

## Open questions

- Only tested on ONE anchor field; unclear if the higher-corr result
  generalizes or is specific to `fn_assets_fair_val_l2_q`'s particular
  interaction with `ts_arg_max`'s turnover profile.
- `WINDOW` sensitivity: only 20 vs 40 tested; 20 was clearly better. Shorter
  windows (5, 10) untested.
