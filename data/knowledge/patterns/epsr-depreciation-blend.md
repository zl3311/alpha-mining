---
pattern: "epsr-depreciation-blend"
discovered: "20260626-001"
refined: "20260627-001"
applicable_to: "analyst4 sparse flags + fundamental6 depreciation fields"
confidence: "high"
---

# Pattern: EPS Revision + Depreciation Value Blend

## Template

```
ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close) + rank(STABILIZER), 5)
```

| Parameter | Best | Alternatives |
|-----------|------|-------------|
| STABILIZER | open / close - 1 (S=2.08) | -1 * equity / assets (S=1.95), abs(ts_delta(dpactq/close, 3)) (S=1.95), fnd6_fatl / close (S=1.77) |
| ts_sum window | 22 | 44 (GOOD), 10 (GOOD) |
| Outer decay_linear | 3-5 | 10 (marginally worse) |
| Neutralization | SUBINDUSTRY | MARKET kills signal |
| Platform decay | 6 | Default |
| Universe | TOP3000 | |

## Stabilizer Comparison

| Stabilizer | Alpha | S | F | Self-Corr |
|-----------|-------|---|---|-----------|
| rank(open/close - 1) | XgpJGaL0 | 2.08 | 2.36 | 0.604 |
| rank(-1 * equity/assets) | MPp3WAd9 | 1.95 | 2.42 | 0.662 |
| rank(abs(ts_delta(dpactq/close, 3))) | E5wR7wN0 | 1.95 | 2.36 | 0.632 |

## Mechanism

Analyst EPS revision conviction (cumulative over 22 days) combined with capital
depreciation intensity (quarterly depreciation vs price). The depreciation leg
captures value from capital-heavy firms where replacement asset value diverges
from market cap. The stabilizer provides daily signal density to fill gaps
between sparse analyst and quarterly fundamental events.

## When to Use

- Need an EXCELLENT-grade candidate with moderate self-corr (0.59-0.66)
- Want to pair analyst revision signal with a novel fundamental leg
- Need a 3-factor blend where each leg operates at a different frequency
- The `zscore(ts_sum())` wrapper avoids the `flag*(-ret)` driver that saturates
  existing analyst revision entries, keeping self-corr well below 0.7

## Self-Correlation Profile

BRAIN self-corr 0.60-0.66 vs book (below 0.70 auto-PASS threshold). The
`zscore(ts_sum())` wrapper avoids the `flag*(-ret)` driver that saturates
existing analyst revision entries. BRAIN self-corr ≈ PnL return corr
(no inflation observed, confirming the 1.45-1.6x gap is IV270-specific).

## Anti-Patterns

- Multiplicative (epsr * depreciation): INFERIOR S=0.70
- MARKET neutralization: drops to GOOD S=1.34
- rank() instead of zscore() on epsr_flag: wrong-sign signals
- Adding buzz or drlt as 3rd factor: stays GOOD, doesn't lift to EXCELLENT
- Do NOT combine dpactq with dpactq event (abs(ts_delta(dpactq...))) as BOTH
  legs — redundant signal from same field
- Mutual corr between stabilizer variants is 0.90-0.95, so only ONE is
  submittable at a time; the others will be blocked after submission
