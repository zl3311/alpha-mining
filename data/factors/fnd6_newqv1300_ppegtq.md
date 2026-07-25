---
field: "fnd6_newqv1300_ppegtq"
dataset: "fundamental6"
family: "ppe_capital_intensity"
discovery_session: "20260701-001"
best_sharpe: 2.84
best_fitness: 3.21
best_expression: "ts_decay_linear(rank(fnd6_newqv1300_ppegtq / close) + rank(anl4_ptpr_flag) + rank(fnd6_itci / close) + rank(open/close - 1), 5)"
mechanism: "PP&E gross / price captures replacement-cost value for capital-intensive firms"
status: "active"
---

# Factor: fnd6_newqv1300_ppegtq

## Economic Mechanism

Property, Plant & Equipment (gross) normalized by price measures the replacement cost of a firm's physical assets relative to its market value. When PP&E/price is high, the market is underpricing the firm's capital base — either because the assets generate cash flows the market hasn't fully valued, or because the firm's stock has been oversold relative to its physical asset backing.

Unlike net PP&E (which subtracts depreciation), gross PP&E captures total capital committed, making it a more stable measure of capital intensity that doesn't fluctuate with depreciation policy choices.

## Best Known Expression

```
ts_decay_linear(rank(fnd6_newqv1300_ppegtq / close) + rank(anl4_ptpr_flag) + rank(fnd6_itci / close) + rank(open/close - 1), 5)
```

SPECTACULAR S=2.84, F=3.21, T=17.8% at SUBINDUSTRY, decay=8, TOP3000

## Lessons

- Works best as one leg in a 3-4 factor additive blend, not standalone
- Decorrelates from dpactq (depreciation) and drc (deferred R&D) in PnL space despite same dataset
- Higher decay (8 vs 6) boosts Sharpe by ~0.09 for this capital-intensive signal
- Self-corr 0.7943 vs MPbgqZ7o (fundamental_sentiment) — passes only via Sharpe premium; margin is tight
