---
field: "fnd6_city"
dataset: "fundamental6"
family: "fundamental_rare_event"
mechanism: "fundamental_rare_event"
status: "active"
coverage: 0.5
standalone_sharpe: 1.55
standalone_fitness: 1.76
best_form: >
  trade_when(ts_std_dev(returns,20)>0.02, rank(ts_delta(fnd6_city, 3)), ts_std_dev(returns,20)<0.01)
in_submitted_book: False
note: "SPECTACULAR with MARKET neut (F=3.07) but fails CONCENTRATED_WEIGHT"
---

# fnd6_city

City where company HQ is located (delta detects relocations)

## Mechanism

HQ relocation is a rare corporate event signaling strategic shift (tax optimization, talent access, regulatory arbitrage). Market processes this information slowly. Extremely high fitness with MARKET neutralization but fails CONCENTRATED_WEIGHT.
