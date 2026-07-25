---
alpha_id: "RRN1EM51"
expression: "trade_when(vol>0.02, rank(open/close-1), vol<0.01)"
sharpe: 2.07
fitness: 1.2
grade: "AVERAGE"
family: "pv_intraday_reversal"
neutralization: "SUBINDUSTRY"
decay: 5
status: "ACTIVE"
---

# RRN1EM51

Short-term reversal. Intraday overreaction (open-to-close return) mean-reverts, conditional on high-volatility regime.
