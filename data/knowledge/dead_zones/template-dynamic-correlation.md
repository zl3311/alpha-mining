---
category: "dead_zone"
entity_type: "template"
template: "ts_corr(fundamental_field, returns, d)"
discovered: "20260626-001"
expressions_tested: 4
best_sharpe: 1.00
status: "dead_end"
confidence: "high"
---

# Template: Dynamic Correlation (fundamental × returns)

`rank(ts_corr(field / close, returns, d))` where field is any fundamental6 field
produces no actionable signal. Tested with fnd6_newqv1300_dpactq, fnd6_itci,
operating_income, and fnd6_drlt. Best result S=1.00 (INFERIOR).

Time-varying correlation between slow-moving fundamentals and daily returns is
noise at the 22-day horizon.
