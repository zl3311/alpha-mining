---
id: "20260717-001-learnings"
session: "20260717-001"
category: "pattern"
confidence: "high"
actionable: true
---

# Learnings: Session 20260717-001

## What Worked

- Fresh annual liability fair-value anchor `fn_liab_fair_val_a` with
  `anl4_ffo_flag` as the non-buzz*-ret densifier → self-corr-safe GOOD base.
- Pairing `open/close - 1` with `sales_estimate_count_quarterly` to clear
  EXCELLENT fitness **and** keep self-corr PASS (pattern promoted).
- Local BrainClient batch sims when HF queue is offline.

## What Didn't Work

- `fnd6_nopio` event-magnitude + standard leverage/ivaco/drlt/buzz*-ret:
  EXCELLENT/SPECTACULAR metrics but self-corr 0.79–0.82 vs tlcf/txw peers.
- `open/close` alone on the liab base: F≈2.00 but self-corr FAIL ~0.73.
- Most novel Round-1 trees (SNR, PCR gate, dyn_corr, convex trade_when,
  tbve densify) were INFERIOR or only GOOD.

## New Patterns

- `sales-count-densifier-decorrelates-oc` — see
  `data/knowledge/patterns/sales-count-densifier-decorrelates-oc.md`.

## Mechanism Insights

Annual liability fair-value aggregates capture a coarser MTM/reclassification
clock than quarterly L2. With FFO revision + sales-coverage densifiers, the
signal stays economically in the fair-value-event family but temporally and
cross-sectionally distinct enough to clear the book's 0.7 wall.
