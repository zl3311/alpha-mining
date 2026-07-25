---
category: "dead_zone"
discovered: "20260606"
updated: "20260606"
blocked_by: "npWYoqQz"
status: "conditional"
fields:
  - "implied_volatility_call_270"
  - "implied_volatility_put_270"
---

# IV 270-Day Call-Put Spread — Conditional Dead Zone

Any alpha using `implied_volatility_call_270 - implied_volatility_put_270` has
BRAIN self-correlation 0.82-0.93 against `npWYoqQz` (ACTIVE, SPECTACULAR,
S=2.09, F=3.02). This **blocks low-Sharpe variants** but does NOT block
high-Sharpe variants that meet the Sharpe premium escape.

## Sharpe Premium Escape

The required Sharpe depends on which book entry is the **highest-correlated peer
with correlation > 0.7** for the specific candidate. Two book entries use IV270:

| Book Entry | Sharpe | Required (1.10x) | Typical corr range |
|------------|--------|-------------------|--------------------|
| vRm07LP3 (pure IV spread) | 1.82 | **2.002** | 0.82-0.93 |
| npWYoqQz (IV + fundamental blend) | 2.09 | **2.30** | 0.57 (below 0.7 for current candidates) |

For current sentiment × IV candidates, the top peer is `vRm07LP3` (corr > 0.7)
while `npWYoqQz` stays below 0.7, so the bar is **2.002**. But future variants
that are more structurally similar to `npWYoqQz` could have its correlation
exceed 0.7, raising the bar to **2.30**. Always verify with `--brain-check`.

**Confirmed example**: `omY3pZq2` (BRAIN self-corr = 0.824, Sharpe = 2.13)
→ **PASS** because 2.13 > 2.002 (top peer: vRm07LP3).

**Confirmed failure**: `e7rdA5rM` (BRAIN self-corr = 0.926, Sharpe = 1.88)
→ **FAIL** because 1.88 < 2.002 (top peer: vRm07LP3).

## Tested and Blocked (Sharpe < 2.002)

- Sentiment × IV multiplicative: `rank(buzz) * zscore(ts_mean(IV270_spread, 22))`
- Pure IV spread: `zscore(ts_mean(IV270_spread, 22))`
- IV + fundamental blend (npWYoqQz itself uses this structure)
- All decay values (3, 5, 7, 10, 14, 20)
- All buzz smoothing (raw, 5d, 10d average)

## Still Viable

- **High-Sharpe IV270 variants** (Sharpe > 2.002) with novel wrappers or
  secondary signals that boost Sharpe above the 1.10x premium threshold
- Non-spread IV fields (e.g. pure call IV, pure put IV, PCR) → worth testing
  (different field means no 1.6x inflation)
- IV fields from different tenors (90, 180) WITHOUT 270 → risky (likely
  correlated cross-tenor) but no confirmed block
- IV rank/momentum (ts_delta of IV) rather than cross-sectional level → unknown
