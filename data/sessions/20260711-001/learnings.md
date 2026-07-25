---
id: "20260711-001-learnings"
session: "20260711-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260711-001

## What Worked

- **Bulk-scanning `data/knowledge/factor_profiles/` for fresh anchor fields**:
  filtering 1,669 profiles for standalone Sharpe 0.9-1.5, excluding used
  fields and confirmed-weak datasets, surfaced `fn_liab_fair_val_l2_q` and
  `anl4_gric_flag` — two clean, never-used fields — in minutes, versus
  guessing at field names.
- **Applying the proven `event-magnitude-abs-ts-delta` template to a fresh
  anchor** reliably reproduces SPECTACULAR/EXCELLENT aggregate metrics
  immediately (6th anchor field in a row to do so: itci, ppegtq, tlcf, txw,
  fn_liab_fair_val_l2_q, dltis). This template is now extremely well-proven
  for *fitness*; the remaining risk is entirely in *self-correlation* against
  its own growing family of siblings.
- **Swapping a shared stabilizer leg for a genuinely cross-dataset-fresh field**
  (here, an analyst4 flag replacing a second fundamental6 stabilizer) is a
  cheap, effective decorrelation lever within an already-saturated template
  family — it improved both Sharpe/Fitness AND correlation simultaneously,
  rather than trading one for the other.
- **Decomposing "vs_book" correlation into per-alpha peer identity** (not just
  reading the aggregate verdict) was essential — it revealed that several
  round-1/2 candidates were near-exact duplicates (2 of 3 legs identical) of
  specific book entries, which the aggregate number alone wouldn't have made
  obvious as a *skeleton*-level problem versus an anchor-level problem.

## What Didn't Work

- **Fresh anchor + the standard `open/close-1 + {ptpr_flag|netdebt_flag}`
  skeleton**: produces excellent aggregate metrics but 0.74-0.91 correlation
  regardless of anchor freshness, because this exact 2-leg skeleton is shared
  verbatim by 5+ existing book entries. Confirmed across 8+ anchor-field
  variants over multiple sessions (this session added `dltis` and a
  `gric_flag` multi-horizon spread to that list). See new rule
  `overnight-gap-flag-skeleton-saturated.md`.
- **Pure fresh-anchor combinations avoiding the skeleton entirely** (Round 3):
  successfully decorrelated but capped at AVERAGE grade (F~1.0-1.14) — novel
  orthogonal-theme fields are individually too weak to reach EXCELLENT+
  fitness without the proven catalyst legs, confirming the same finding from
  session 20260702-002.
- **`fnd6_dltis` on the event-magnitude-abs-ts-delta template**: SPECTACULAR
  metrics but 0.94 correlation with `WjGVJ7bN` (the `fnd6_txw`-anchored
  sibling) — both are debt/tax-related flow items with similar event
  dynamics. Field-level economic proximity to existing family members matters
  more than raw novelty.
- **Minor parameter tuning (event window d, outer decay, buzz smoothing
  window) within the already-marginal `fn_liab + leverage + fatl/dlto + ivaco
  + buzz` combo**: every variant tested landed in the same 0.685-0.703 band
  regardless of tuning — confirms these are fitness/turnover knobs, not
  decorrelation levers, once 3+ legs are shared with a specific sibling.
- **`trade_when(ts_std_dev(returns,20) > x, ts_decay_linear(abs(ts_delta(...))
  + ...), ts_std_dev(returns,20) < y)`**: failed permanently with a BRAIN
  unit-type parser error (`Incompatible unit for input of "greater"`) across
  4/4 variants, despite this exact `trade_when` structure working fine
  elsewhere in the book (`Gro21wWG`). Root cause not identified — possibly an
  interaction between the inner `abs(ts_delta(F/close,d))` term's implicit
  unit and the outer gate; not investigated further this session.

## New Rules Discovered

- `data/knowledge/rules/overnight-gap-flag-skeleton-saturated.md`: the
  `open/close-1 + {ptpr_flag|netdebt_flag}` 2-leg skeleton is fully saturated
  and correlation-blocking regardless of the third/fourth leg's novelty.

## New Dead Zones

- `data/knowledge/dead_zones/field-dltis-event-magnitude.md`: `fnd6_dltis` on
  the event-magnitude-abs-ts-delta template is self-corr-blocked against
  `WjGVJ7bN` (0.94).

## New Patterns

- `data/knowledge/patterns/event-magnitude-fresh-stabilizer.md`: when a
  proven multi-leg template already has 3+ ACTIVE siblings sharing the same
  non-anchor legs, substitute exactly one shared leg for a field unused
  anywhere in that family (ideally from an orthogonal dataset) to decorrelate
  cheaply without sacrificing fitness.

## Mechanism Insights

- `fn_liab_fair_val_l2_q` (Level-2 fair-value liabilities): large
  quarter-over-quarter revaluations of model-priced (not market-quoted)
  liabilities signal a re-marking event — rate/credit-spread shock, hedge
  restructuring, or valuation-assumption change — that the market
  underreacts to regardless of direction. Economically distinct enough from
  inventory (itci), PP&E (ppegtq), tax-loss carryforward (tlcf), and excise
  tax (txw) events to correlate meaningfully lower (0.67-0.71 vs 0.94 for
  `dltis`) with the existing event-magnitude family while still fitting the
  same template mechanically.
- `anl4_gric_flag` (gross-income forecast-type revision): a standard sparse
  analyst-revision flag (needs `ts_mean` smoothing to reach AVERAGE
  standalone), but valuable here in raw form as a decorrelated
  `LOW_SUB_UNIVERSE_SHARPE`-fixing densifier precisely because no other book
  alpha uses it — the choice of *which* densifier field to use matters as
  much for correlation as for the check itself.
