---
alpha_id: "O0pl2znv"
status: "ACTIVE"
grade: "EXCELLENT"
sharpe: 2.07
fitness: 2.02
turnover: 0.085
decay: 6
neutralization: "SUBINDUSTRY"
universe: "TOP3000"
region: "USA"
family: "deferred_tax_relationship_intraday_blend"
self_corr_max: 0.685
self_corr_peer: "np30Odjd"
self_corr_result: "PASS"
session: "20260702-002"
brain_url: "https://platform.worldquantbrain.com/alpha/O0pl2znv"
expression: "ts_decay_linear(rank(fnd2_dfdtxasoprlcarryfwd / close) + rank(anl4_ptpr_flag) + rank(rel_num_all) + rank(open/close - 1), 5)"
---

# O0pl2znv — Deferred Tax + PTPR + Relationships + Intraday

## Expression

```
ts_decay_linear(rank(fnd2_dfdtxasoprlcarryfwd / close) + rank(anl4_ptpr_flag) + rank(rel_num_all) + rank(open/close - 1), 5)
```

## Mechanism

Four orthogonal components from four distinct data families:

1. **fnd2_dfdtxasoprlcarryfwd / close** (fundamental2): Deferred tax asset from operating
   loss carryforward normalized by price. Companies with large prior-period tax shields
   relative to market cap are underpriced — the market undervalues future cash flow
   benefits from accumulated loss carryforwards.

2. **anl4_ptpr_flag** (analyst4): Pre-tax profit revision flag. Confirms that analyst
   community recognizes improving profitability outlook, catalyzing the fundamental
   tax asset signal.

3. **rel_num_all** (pv13): Total business relationships count. Captures network
   breadth and revenue diversification — more relationships indicate stable cash flows
   and reduced idiosyncratic risk.

4. **open/close - 1** (price): Intraday gap/momentum. Captures daily price action
   confirmation and market microstructure effects.

## Self-Correlation

- Max BRAIN self-corr: 0.685 vs `np30Odjd` (S=1.87)
- Second: 0.679 vs `78w5d35x` (S=2.34)
- Threshold: 0.7 → AUTO PASS (no Sharpe premium needed)
- Novel anchors (fnd2, pv13) keep decorrelation from fnd6-dominated book

## BRAIN Checks

All 7 computable checks PASS:
- LOW_SHARPE: 2.07 > 1.25 ✓
- LOW_FITNESS: 2.02 > 1.0 ✓
- LOW_TURNOVER: 8.5% > 1% ✓
- HIGH_TURNOVER: 8.5% < 70% ✓
- CONCENTRATED_WEIGHT: PASS ✓
- LOW_SUB_UNIVERSE_SHARPE: 1.14 > 0.90 ✓
- MATCHES_COMPETITION: PASS ✓
- SELF_CORRELATION: 0.685 < 0.7 → PASS ✓
