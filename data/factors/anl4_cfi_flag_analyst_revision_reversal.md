---
field: "anl4_cfi_flag"
dataset: "analyst4"
family: "analyst_revision_reversal"
mechanism: "analyst_revision_reversal"
status: "active"
coverage: 0.75
standalone_sharpe: 1.18
standalone_fitness: 1.07
best_form: "rank(anl4_cfi_flag * (-1 * returns))"
in_submitted_book: True
---

# anl4_cfi_flag

Cash flow investing revision flag × reversal. Dynamic component for EXCELLENT blends.

## Mechanism

When analysts revise cash flow from investing estimates AND the stock has recently declined, mean reversion is amplified. The revision confirms fundamental change while the price drop provides entry. Key dynamic component in F>2.0 blends.
