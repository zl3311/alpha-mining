---
pattern: "event-magnitude-fresh-stabilizer"
discovered: "20260711-001"
applicable_to: "event-magnitude-abs-ts-delta family (fundamental6/fundamental2 anchors + leverage/ivaco/drlt/buzz stabilizers)"
confidence: "high"
best_alpha_id: "YP0bLdzA"
best_sharpe: 2.32
best_fitness: 2.22
best_self_corr: 0.673
---

# Pattern: Swap a Shared Stabilizer Leg for a Fresh One to Decorrelate Within an Already-Saturated Template Family

## The problem

The `event-magnitude-abs-ts-delta` template (`rank(abs(ts_delta(FIELD/close,D)))
+ rank(-1*equity/assets) + rank(fnd6_ivaco/close) + rank(fnd6_drlt/close) [+
rank(ts_mean(scl12_buzz,5)*(-1*returns))]`) is highly reliable — by session
20260711-001 it had already produced 5 ACTIVE book entries across different
anchor fields (`fnd6_itci`, `fnd6_newqv1300_ppegtq`, `fnd6_tlcf`, `fnd6_txw`,
plus 2 original itci variants). Applying it to a 6th fresh anchor
(`fn_liab_fair_val_l2_q`) reproduced the template's usual SPECTACULAR/EXCELLENT
metrics immediately, but self-correlation vs the existing 5 family members sat
at 0.69-0.71 — because `leverage + ivaco + drlt (+ buzz)` are 3-4 legs shared
**verbatim** with every existing member. Swapping `drlt` for other already-used
fundamentals (`fatl`, `dlto`) only nudged correlation to 0.68-0.70 — still an
uncomfortably thin margin, because `ivaco` and `buzz` remained shared.

## The fix

Swap ONE of the shared stabilizer legs for a field that has **zero prior usage
anywhere in this template family** (not just zero usage in the book overall —
specifically not used by any of the 5+ family siblings). In this case, swapping
`fnd6_drlt` for `anl4_gric_flag` (a never-before-used analyst4 flag, used in
raw `rank()` form purely as a sub-universe densifier, not for its revision
signal per se):

- Correlation vs the closest family sibling (`WjGVJ7bN`) dropped from 0.69-0.71
  (drlt/fatl/dlto variants) to **0.673**.
- Sharpe improved (2.16→2.32) while fitness decreased modestly (2.33→2.22)
  versus the fatl-stabilized variant. The fresh leg traded a small amount of
  fitness for safer correlation while remaining EXCELLENT.

## When to use

- Applying a proven multi-leg template to a new anchor field, when the template
  already has 3+ ACTIVE siblings sharing the same non-anchor legs.
- Before assuming "this template is now blocked" after seeing 0.65-0.75
  correlation with siblings — try substituting exactly ONE shared leg for an
  unused field from an orthogonal dataset (here: analyst4, vs. the family's
  usual all-fundamental6 stabilizers) before abandoning the template.

## Anti-patterns observed en route

- Swapping the anchor's `abs(ts_delta(...))` window (d=3→5→10) or the outer
  `ts_decay_linear` window (5→8→10) or the buzz smoothing window (5→10→20) all
  left correlation pinned at 0.69-0.70 — these are minor tuning knobs, not
  decorrelation levers, for this family.
- `trade_when` realized-volatility gating (the proven `LOW_SUB_UNIVERSE_SHARPE`
  fix per `volatility-gate-fixes-sub-universe.md`) failed **permanently** with a
  BRAIN unit-type error (`Incompatible unit for input of "greater"`) on this
  exact expression shape across all 4 variants tried. Root cause not
  identified; avoid combining `trade_when(ts_std_dev(returns,20) > x, ...)`
  with an `abs(ts_delta(F/close,d))` inner term inside `ts_decay_linear` until
  this is understood.
