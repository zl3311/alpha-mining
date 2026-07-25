---
id: "20260715-001-learnings"
session: "20260715-001"
category: "discovery"
confidence: "medium-high"
actionable: true
---

# Learnings: Session 20260715-001

## What Worked

- **`fn_assets_fair_val_l2_q` as an anchor**: the asset-side counterpart to
  the already-ACTIVE `fn_liab_fair_val_l2_q` sits in a genuinely small,
  orthogonal redundancy cluster (#21, 2 members) rather than the book's
  dominant fundamental-value/analyst-revision mega-clusters. Every template
  variant tried on it this session correlated <0.60 with the book (except the
  higher-turnover `ts_arg_max` structure) — the lowest correlation ceiling of
  any anchor used in the event-magnitude family to date.
- **Dual-stabilizer 6-factor form** (`event-magnitude + leverage +
  fresh_flag + drlt + ivaco + buzz`): using BOTH proven stabilizer legs
  together instead of picking one lifted GOOD (F=1.75) to EXCELLENT (F=2.01)
  at essentially zero self-corr cost (0.572→0.567). New reusable lever, see
  `event-magnitude-dual-stabilizer.md`.
- **`ts_arg_max` recency-of-shock structure** is a genuinely novel,
  functioning operator-tree shape (not previously in `data/factors/` or
  `data/knowledge/patterns/`) — reached EXCELLENT metrics, just not a safe
  self-corr margin on this particular anchor. See
  `event-magnitude-recency-arg-max.md`.

## What Didn't Work

- **Signal-to-noise ratio** (`ts_delta(F,5)/ts_std_dev(F,20)`) on sparse
  quarterly fundamentals: near-zero/negative Sharpe, 36-44% turnover. The
  trailing std-dev window is dominated by a few discrete update days,
  making the ratio spike unpredictably. New dead zone.
- **Buzz-LEVEL x event-magnitude product** (`rank(ts_mean(buzz,10)) *
  rank(abs(ts_delta(F,5)))`): INFERIOR, S<1.0. Buzz needs the `-1*returns`
  reversal pairing to be informative; raw level is uninformative alone. New
  dead zone.
- **Fundamental-trend-gated `trade_when`** (gating by
  `ts_delta(OTHER_FUNDAMENTAL, 20) > 0`, as opposed to the proven
  realized-volatility gate): collapsed Sharpe to 0.01. Low confidence (1
  data point) but a discouraging signal. New dead zone.
- **Multi-horizon spread** (`ts_delta(F,5) - ts_delta(F,22)`) and
  **regime-divergence** (`ts_zscore(F,10) - ts_zscore(F,60)`), when combined
  with the standard leverage+drlt+buzz stabilizer set: both capped at
  AVERAGE (F=1.08-1.38) on 3 different fields — weaker than the standard
  `abs(ts_delta(F,d))` event-magnitude transform on the same anchors. Not
  promoted to a formal dead zone (only 2-3 data points each, and the
  `dcvsub` multi-horizon variant DID reach GOOD S=2.62 F=1.93 aggregate
  metrics, just blocked on self-corr not on the template itself) — flagged
  here for awareness, not yet conclusive.
- **`ts_arg_max` recency structure runs ~2x the turnover and noticeably
  higher self-corr than the additive form** on the identical anchor +
  stabilizer set (0.701 vs 0.567) despite similar Sharpe/Fitness — a
  reminder that WRAPPER CHOICE, not just field freshness, materially affects
  self-correlation within a template family.

## New Rules Discovered

- None promoted to `data/knowledge/rules/` this session (findings were
  field/template-specific dead zones and patterns, not universal hard
  constraints).

## New Dead Zones

- `data/knowledge/dead_zones/template-signal-to-noise-ratio.md`
- `data/knowledge/dead_zones/template-buzz-level-event-magnitude-product.md`
- `data/knowledge/dead_zones/template-fundamental-trend-gated-trade-when.md`

## New Patterns

- `data/knowledge/patterns/event-magnitude-recency-arg-max.md`
- `data/knowledge/patterns/event-magnitude-dual-stabilizer.md`

## Mechanism Insights

- The event-magnitude-abs-ts-delta family's self-correlation ceiling is
  driven primarily by the ANCHOR field's redundancy-cluster membership, not
  by the choice of stabilizer legs (which are necessarily shared with prior
  family members either way). `fn_assets_fair_val_l2_q`'s membership in a
  tiny 2-field cluster is what let it clear self-corr comfortably even while
  reusing both standard stabilizers simultaneously — a structural
  confirmation of the `event-magnitude-fresh-stabilizer.md` pattern's
  original hypothesis, now with a second, even-more-orthogonal anchor as
  supporting evidence.
- Within a fixed anchor+stabilizer set, ADDITIVE `ts_decay_linear(rank(...)+...)`
  wrappers appear to produce lower turnover and lower self-correlation than
  `ts_arg_max`-based recency wrappers — turnover itself may be a proxy for
  how much a candidate's trading days overlap with the book's (mostly
  additive, low-turnover) existing event-magnitude members.
