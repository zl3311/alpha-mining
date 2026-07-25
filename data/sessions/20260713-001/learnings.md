---
id: "20260713-001-learnings"
session: "20260713-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260713-001

## What Worked

- **Dropping a shared skeleton leg, then switching neutralization, as a
  two-step decorrelation lever**: once a proven multi-leg template's
  stabilizer skeleton is fully saturated (3+ ACTIVE siblings share it
  verbatim), removing the ONE leg whose penalty-mechanism is
  neutralization-specific (`leverage`, penalized under MARKET) unlocks MARKET
  as a decorrelation lever without paying MARKET's usual leverage-specific
  fitness tax. This is a genuinely new move beyond the previously-known
  "swap one leg for a fresh field" trick (`event-magnitude-fresh-stabilizer.md`)
  — it combines leg removal AND neutralization switch.
- **Testing an economically-DISTINCT anchor as a diagnostic, not just a
  hopeful improvement**: using `current_ratio` (liquidity, unrelated to
  tax/debt/fair-value) on the event-magnitude template and finding it
  correlated WORSE (0.922) than `fnd6_newqv1300_msaq` (0.789-0.883) cleanly
  proved the correlation driver is the shared stabilizer skeleton, not the
  anchor's economic character — a decisive result that redirected the whole
  session away from more anchor-field hunting and toward skeleton surgery.
- **Confirming a novel structure's self-corr authoritatively even at
  below-target grade**: `QPVWnxKK`'s BRAIN-confirmed PASS at 0.5667 validates
  the directional-gating-by-fundamental-trend structure as genuinely safe and
  reusable, even though it didn't clear EXCELLENT this session — worth
  revisiting with a different base anchor (not leverage) in a future session.

## What Didn't Work

- **`ts_arg_max`/`ts_arg_min` recency-of-extreme, `quantile()` bucketing,
  non-return `ts_corr`, multi-horizon spreads, cross-dataset ratios**: all
  five genuinely novel operator-tree shapes from `novelty-required.md`
  produced INFERIOR results (best F=0.64) on two fresh fundamental fields.
  Structural novelty alone does not guarantee signal; these specific shapes
  appear to need either sparser/more event-driven fields (`ts_arg_max`) or
  fields with a documented co-movement rationale (`ts_corr`) to be worth
  revisiting.
- **Self-referential directional gating** (`rank(delta(F,5)) * sign(delta(F,60))`,
  gating a field by its OWN longer-window trend): negative Sharpe, unlike
  gating by a DIFFERENT slow fundamental (which works). The self-referential
  form creates a momentum-vs-mean-reversion ambiguity that nets to noise.
- **Removing BOTH `leverage` and `ivaco`** from the event-magnitude template:
  fitness collapses to INFERIOR (F<=0.67) regardless of which fresh fields
  replace them. `ivaco` specifically is load-bearing for this family's
  fitness, not just a correlation cost — it cannot be dropped, only
  `leverage` can (and only when compensated by switching to MARKET).
- **The directional-gating-hybrid structure has a firm GOOD-grade ceiling**:
  7+ variants (window sweeps 10/20/40, decay sweeps 3/5/8/10, leg swaps
  ivaco/drlt/current_ratio/ffo_flag, buzz window sweeps) all landed in
  F=1.19-1.88 regardless of tuning — turnover stays structurally 18-27%
  because the `sign()` gate flips too often for this 2-3 leg form.

## New Rules Discovered

- `data/knowledge/rules/event-magnitude-leverage-ivaco-skeleton-saturated.md`:
  the event-magnitude family's `leverage+ivaco+buzz` stabilizer skeleton is
  fully saturated regardless of anchor field novelty.

## New Dead Zones

- `data/knowledge/dead_zones/template-arg-max-recency-quantile-dynamic-corr.md`:
  five novel operator-tree shapes tested and confirmed weak on fresh
  fundamentals.

## New Patterns

- `data/knowledge/patterns/market-neutral-event-magnitude-escape.md`: drop
  `leverage`, then switch to MARKET, to escape the saturated skeleton.
- `data/knowledge/patterns/directional-gating-by-fundamental-trend.md`: gate a
  fundamental anchor by a SECOND slow fundamental's trend direction — novel,
  BRAIN-confirmed safe, but capped at GOOD grade.

## Mechanism Insights

- `fnd6_newqv1300_msaq` (Accumulated OCI — Marketable Security Adjustments):
  behaves like a mark-to-market/fair-value-adjustment signal economically
  adjacent to the family's existing tax/liability-remarking anchors — hence
  its persistently elevated correlation (0.79-0.88) even before accounting for
  the shared-skeleton effect.
- `anl4_ffo_flag` (funds-from-operations forecast-revision flag): weak
  standalone (best AVERAGE via `rank(delta(F,5))`, S=1.35 F=1.39,
  CONCENTRATED_WEIGHT risk 22F/10P) but effective as a raw-`rank()` densifier
  leg inside multi-factor blends, consistent with the
  `event-magnitude-fresh-stabilizer` pattern's general finding that a fresh
  analyst4 flag's VALUE as a blend leg is largely about correlation novelty,
  not standalone strength.
