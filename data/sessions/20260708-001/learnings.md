---
id: "20260708-001-learnings"
session: "20260708-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260708-001

## What Worked

- **Event-magnitude pattern transfers beyond itci.** `abs(ts_delta(FIELD/close, 3))` +
  leverage + stabilizer produces GOOD+ signal on ppegtq, cshtr, drc, dd1q. The
  `event-magnitude-abs-ts-delta` pattern's "itci-only" constraint is disproved. New
  pattern recorded: `event-magnitude-novel-fields.md`.
- **4-factor ivaco boost reaches EXCELLENT.** Adding `fnd6_ivaco / close` as a 4th
  stabilizer (alongside drlt) lifted ppegtq from GOOD F=1.74 to EXCELLENT F=2.20
  (wpl5eP5v) while keeping self-corr PASS (0.6676). ivaco boosts Sharpe; drlt holds
  the itci-family corr down.
- **Saturating the EXCELLENT threshold.** EXCELLENT requires F>=~2.0 (confirmed:
  omnopQ9k S=2.64 F=1.79 is GOOD). 3-factor novel event caps at F~1.74; the 4th
  stabilizer is needed to cross 2.0.

## What Didn't Work

- **Negated fresh fundamental6 blends (rounds 1-2, 35 sims).** Additive blends of
  negated fnd6_intc/txw/txdbca/acqgdwl/dcvsub + value anchors all INFERIOR. The
  `negation-asymmetry-fundamentals` pattern's standalone Sharpes are STALE (2-3x
  overstated): intc negated S=-0.82 vs claimed 1.32. Dead zone recorded:
  `negated-fresh-fundamental6-blends.md`.
- **drc/cshtr event-magnitude self-corr FAIL** (0.75-0.79 vs 0m8GV1Pp). Not all novel
  event fields decorrelate; only ppegtq (0.660) and dd1q (0.680) PASS.
- **4th-factor self-corr tradeoff.** Adding dlto (np2n36VM) or ivaco-alone (781xJ3J2)
  pushes corr >0.7. Only the ivaco+drlt combination (wpl5eP5v) stayed under 0.7.
- **Dual-event blends** (ppegtq event + dd1q event) → AVERAGE (events cancel).
- **Longer delta/decay** (d=5, d=10, decay=10) on ppegtq → lower fitness.
- **trade_when(ts_std_dev(returns,20)>0.02, ...)** hit a unit error
  (TSPrice vs unitless) — avoid this gate pattern with current platform behavior.

## New Rules Discovered

- EXCELLENT grade threshold is **F >= ~2.0** (fitness is the binding metric; Sharpe
  secondary). GOOD caps at F~1.8 regardless of Sharpe. (Observational rule; already
  implicit in book data.)

## New Dead Zones

- `negated-fresh-fundamental6-blends.md` — additive blends of negated
  intc/txw/txdbca/acqgdwl/dcvsub (stale negation-asymmetry data).

## New Patterns

- `event-magnitude-novel-fields.md` — abs(ts_delta) event-magnitude works on ppegtq,
  dd1q (PASS self-corr), cshtr, drc (FAIL self-corr); EXCELLENT via ivaco 4th factor.

## Mechanism Insights

- PP&E gross (fnd6_newqv1300_ppegtq) has event dynamics similar to inventory (itci):
  discrete capex events (capacity expansion / writedowns) that markets underreact to
  in magnitude. This is why abs(ts_delta) works on ppegtq despite the original pattern
  claiming only itci has such dynamics.
- The leverage + drlt base creates a self-corr floor (~0.55-0.66) against the itci
  event-magnitude family. The event field's distinctness from itci determines whether
  total corr stays under 0.7. ppegtq/dd1q are sufficiently distinct; drc/cshtr are not.
- The book is near saturation: every decorrelated EXCELLENT path requires a delicate
  balance of boosting fitness (shared stabilizers) without crossing the 0.7 corr wall.
  wpl5eP5v sits at 0.6676 — barely passing.
