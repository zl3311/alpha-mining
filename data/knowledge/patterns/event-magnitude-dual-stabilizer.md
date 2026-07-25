---
pattern: "event-magnitude-dual-stabilizer"
discovered: "20260715-001"
applicable_to: "event-magnitude-abs-ts-delta family (fundamental6/fundamental2 anchors + leverage/ivaco/drlt/buzz stabilizers)"
confidence: "medium (1 anchor field tested)"
best_alpha_id: "lelNqEZl"
best_sharpe: 2.01
best_fitness: 2.01
best_self_corr: 0.567
---

# Pattern: Using BOTH `drlt` AND `ivaco` as Dual Stabilizers (6-Factor Form) Lifts Fitness Without Raising Correlation

## The problem

Every prior event-magnitude-abs-ts-delta family member (`0m8GV1Pp`,
`le0gY6Ze`, `wpl5eP5v`, `WjGVJ7bN`, `rKlo39p1`, `YP0bLdzA`) used exactly ONE
of `fnd6_drlt` or `fnd6_ivaco` as the `LOW_SUB_UNIVERSE_SHARPE` stabilizer
leg, never both together, alongside a fresh anchor + fresh analyst4 flag +
buzz (5-factor form, per `event-magnitude-fresh-stabilizer.md` and
`event-magnitude-buzz-boost.md`). On the fresh anchor `fn_assets_fair_val_l2_q`,
the standard 5-factor form (event + leverage + `anl4_cff_flag` + `drlt` +
buzz) capped at GOOD (S=1.79, F=1.75, self-corr PASS 0.572) — short of
EXCELLENT.

## The fix

Add the OTHER stabilizer as a 6th leg instead of swapping:

```
ts_decay_linear(rank(abs(ts_delta(FIELD / close, 3))) + rank(-1 * equity / assets) + rank(FRESH_ANALYST_FLAG) + rank(fnd6_drlt / close) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)
```

- Fitness: 1.75 → **2.01** (GOOD → EXCELLENT), Sharpe: 1.79 → 2.01.
- Self-correlation: 0.572 → **0.567** — essentially unchanged (marginally
  LOWER), not the fitness-for-correlation tradeoff normally expected from
  adding a 6th shared leg.

## Why it doesn't cost correlation

Both `drlt` and `ivaco` are already shared with 4-6 other book members
individually, so adding the second one does not introduce a NEW correlated
component — the family's correlation floor with any given peer is already
set by whichever of the two that peer also uses, plus the leverage/buzz legs.
Since `fn_assets_fair_val_l2_q` itself sits in a small, orthogonal redundancy
cluster (#21, see `data/factors/fn_assets_fair_val_l2_q.md`), the anchor's own
low correlation dominates and the extra shared stabilizer leg has little
marginal effect on the correlation ceiling — while both legs' individually
proven fitness contributions stack additively.

## When to use

- When a fresh, low-corr anchor's 5-factor event-magnitude form reaches only
  GOOD (F 1.5-1.85) and self-corr already has comfortable margin (<0.6):
  try adding the OTHER standard stabilizer as a 6th leg before assuming the
  anchor is capped at GOOD. This is a cheaper lever than hunting for a new
  fresh stabilizer field (per `event-magnitude-fresh-stabilizer.md`), since it
  reuses two already-validated legs.
- Verify self-corr after adding — this pattern held for one anchor
  (`fn_assets_fair_val_l2_q`); it is not yet confirmed whether it holds for
  anchors already closer to the 0.7 boundary (adding any shared leg could tip
  a borderline candidate over).

## Anti-pattern observed en route

- Wrapping the SAME anchor+stabilizer set in `ts_arg_max` recency-of-shock
  instead of additive `ts_decay_linear` reached similar fitness (2.03) at
  MUCH higher turnover (20.9% vs 11.0%) and correlation (0.701 BLOCKED vs
  0.567 SAFE) — see `event-magnitude-recency-arg-max.md`. The additive,
  low-turnover wrapper is the more efficient use of the anchor's
  decorrelation headroom.
