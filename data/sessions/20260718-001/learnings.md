---
id: "20260718-001-learnings"
session: "20260718-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260718-001

## What Worked

- **Current vs total accrued liability as distinct event-magnitude anchors.**
  `fn_accrued_liab_curr_q` (current portion) combined with leverage + ivaco +
  fresh `anl4_fcf_flag` densifier + buzz reaches EXCELLENT with self-corr
  PASS 0.6826. The total accrued field `fn_accrued_liab_q` is already ACTIVE
  as `ZYpjKeKx`; naively cloning that analyst-flag recipe onto `_curr` yields
  corr 0.993 FAIL — stabilizer choice is the decorrelation lever.
- **`anl4_fcf_flag` as fresh densifier** (never in book before) follows the
  `event-magnitude-fresh-stabilizer` pattern (`anl4_gric_flag` / `anl4_cff_flag`
  precedents) and kept correlation under 0.70 vs the event-magnitude family.
- Round-1 satisficing worked: 20 sims, 1 SAFE EXCELLENT — no further rounds needed.

## What Didn't Work

- Novel tree shapes this round mostly failed to clear EXCELLENT:
  multi-horizon lease, MA crossover, IV-skew×lease/tax, debt-rate×pcr,
  regime-divergence interest, ts_arg_min lease recency, event×fcf product.
- `fn_liab_fair_val_l1_q` event-magnitude hits EXCELLENT aggregates but fails
  LOW_SUB_UNIVERSE (0.86 < 1.0) — Level-1 fair-value liability coverage is
  thinner than L2.
- L1−L2 fair-val level dispersion is a promising novel structure (GOOD,
  corr ~0.60) but fails LOW_SUB_UNIVERSE hard (0.32) — needs densification
  before it can be a submission candidate.
- op_lease / txfed / assets_fv_l3 / interest_paid / deferred-tax-carryfwd
  event-magnitude variants all hit self-corr FAIL against the saturated
  event-magnitude family (0.72–0.88).

## New Rules Discovered

None (no new hard constraints).

## New Dead Zones

None formalized this session (novel templates had weak but non-zero signal;
  insufficient evidence for high-confidence dead_zone entries).

## New Patterns

- Soft confirmation of `event-magnitude-fresh-stabilizer`: swapping in an unused
  analyst4 flag (`anl4_fcf_flag`) on a near-sibling accrued field produces a
  decorrelated EXCELLENT. Documented in factor file for `fn_accrued_liab_curr_q`.

## Mechanism Insights

Current accrued liabilities (`fn_accrued_liab_curr_q`) capture near-term
statutory/contractual obligations that reprice or reclassify more frequently
than the total accrued stock. Large 3-day absolute changes mark accrual
recognition / settlement events that the market underreacts to. Pairing with
leverage premium and investing-activities-other (`fnd6_ivaco`) plus an unused
analyst FCF-revision densifier spreads weights enough to clear SUB_UNIVERSE
while keeping PnL correlation with `wpl5eP5v` / `rKlo39p1` just under 0.70.
