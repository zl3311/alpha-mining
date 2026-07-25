---
field: "actuals_value_currency_code"
dataset: "analyst4"
family: "data_artifact"
mechanism: "data_artifact"
status: "active"
coverage: 0.5
standalone_sharpe: 1.26
standalone_fitness: 1.04
best_form: "rank(actuals_value_currency_code)"
in_submitted_book: False
---

# actuals_value_currency_code

Currency code of reported actuals

## Mechanism

UNKNOWN -- likely a data artifact rather than a real economic signal. Currency code is a categorical field; ranking it captures which currencies are assigned higher numeric codes. May proxy for geographic exposure or ADR status. Treat with skepticism.
