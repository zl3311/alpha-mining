---
field: "anl4_ffo_flag"
dataset: "analyst4"
family: "analyst_revision_momentum"
mechanism: "analyst_revision_momentum"
status: "active"
coverage: 0.75
standalone_sharpe: 1.35
standalone_fitness: 1.39
best_form: "rank(ts_delta(anl4_ffo_flag, 5))"
in_submitted_book: False
---

# anl4_ffo_flag

Funds from operations revision flag (delta = revision momentum)

## Mechanism

FFO revision momentum captures acceleration in analyst estimate changes. The delta form (change in revision flag) amplifies the signal when revisions are clustering in time.
