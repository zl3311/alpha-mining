---
category: "dead_zone"
entity_type: "template"
template: "rank(fnd6_F1 / fnd6_F2)"
discovered: "20260626-001"
expressions_tested: 4
best_sharpe: 0.26
status: "dead_end"
confidence: "high"
---

# Template: Inter-Field Fundamental Ratios

`rank(F1 / F2)` where F1 and F2 are both fundamental6 fields produces no signal.
Tested: newqv1300_dpactq/fate, operating_income/dlto, newqv1300_dpactq/dlto,
txs/dlto. Best result S=0.26 (INFERIOR).

Within-dataset fundamental ratios do not generate cross-sectional signal because
both numerator and denominator scale similarly across firms.
