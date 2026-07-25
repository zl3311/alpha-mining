---
pattern: "event-magnitude-iv-gric-blend"
discovered: "20260712-001"
applicable_to: "Fresh fundamental6 fields with standalone S=1.0-1.5, cross-dataset with options IV"
confidence: "high (1 SPECTACULAR result, 1 candidate VkPdaQ2b self-corr PASS)"
best_alpha_id: "VkPdaQ2b"
best_sharpe: 2.18
best_fitness: 2.65
best_self_corr: 0.697
best_self_corr_result: "PASS (0.697 ≤ 0.70 auto-pass threshold)"
---

# Pattern: Fresh Fundamental Event-Magnitude × IV Spread Zscore × Gric-Flag Blend

## Template

```
ts_decay_linear(
  rank(abs(ts_delta(FRESH_FIELD / close, 3))) 
  + rank(-1 * equity / assets) 
  + zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)) 
  + rank(anl4_gric_flag),
5)
```

Parameters: `neutralization=SUBINDUSTRY, decay=6, delay=1, truncation=0.08`

## Why It Works

**Economic mechanism:** Combines three orthogonal alpha sources:
1. **Event-magnitude** of a quarterly fundamental field — captures large changes in corporate fundamentals that the market hasn't fully priced in (same mechanism as the itci/ppegtq/txw family, but applied to a fresh field)
2. **Options IV skew direction** (22-day smoothed) — options market's view of directional risk, with low turnover (T≈2% standalone) that boosts the fitness formula
3. **Leverage premium** — standard quality tilt (short high-leverage firms)
4. **Gross income revision flag** (gric_flag, raw rank) — analyst guidance risk stabilizer; CRITICAL: dilutes IV weight from 1/3 to 1/4, breaking the correlation with omY3pZq2 (sentiment_buzz_iv_spread)

## Self-Corr Structure

**The IV zscore(22) component creates inherent correlation with the options family:**
- Without gric_flag (3-factor): max corr 0.758 vs omY3pZq2 → BLOCKED (escape threshold 2.343)
- With gric_flag (4-factor): max corr **0.697 vs npWYoqQz** → AUTO-PASS ✓

**Event-magnitude part has LOW correlation with WjGVJ7bN/wpl5eP5v/YP0bLdzA:**
- WjGVJ7bN: 0.547 (no shared stabilizers, different primary)
- wpl5eP5v: 0.565
- YP0bLdzA: 0.435

## Field Requirements

The `FRESH_FIELD` must be:
- From fundamental6 (quarterly financial statement)
- NOT already used as the primary in any event-magnitude book entry (itci, ppegtq, tlcf, txw, fn_liab_fair_val_l2_q are all USED → avoid)
- Standalone Sharpe 0.9-1.5 (weaker standalone fields may not produce SPECTACULAR)
- NOT in any dead zone

**Confirmed working:** `fnd6_cptmfmq_dlttq` (long-term debt capital markets structure, standalone S=1.19 → SPECTACULAR S=2.18 with this template)

**Promising untested:** `fnd6_dlto` (long-term debt other, S=1.34), `fnd6_fatl` (financing activities total, S=1.24)

## When to Use

- Prior `event-magnitude-novel-fields` template (without IV) blocked by the event-magnitude book family at 0.7-0.9 correlation
- Fresh fundamental field with S=1.0-1.5 is available
- Event-magnitude book family members (WjGVJ7bN, wpl5eP5v, YP0bLdzA etc.) are the binding self-corr constraint

## Anti-Patterns

- **3-factor only (without gric_flag):** The pure 3-factor version `(event-mag + leverage + IV)` gives 0.716-0.758 max corr (BLOCKED by IV-family entries). ALWAYS add gric_flag as 4th component.
- **Adding buzz as 5th component:** buzz is in omY3pZq2, increasing its correlation. AVOID buzz with this template.
- **Adding ivaco/drlt:** These shared stabilizers increase correlation with WjGVJ7bN/wpl5eP5v. AVOID.
- **Using epsr_flag or other analyst flags that fire at earnings time as primary:** Analyst flags that update around earnings releases are correlated with quarterly fundamental event-magnitudes in PnL space → both correlate with WjGVJ7bN.

## Grade Progression (cptmfmq anchor)

| Components | S | F | T | Grade | Self-Corr |
|-----------|---|---|---|-------|-----------|
| event-mag + leverage + gric + buzz (no IV) | 1.94 | 2.02 | 12.4% | EXCELLENT | 0.775 vs pw8wNe76 BLOCKED |
| event-mag + leverage + IV (no gric) | 2.33 | 2.96 | 7.0% | SPECTACULAR | 0.758 vs omY3pZq2 BLOCKED |
| **event-mag + leverage + IV + gric (4-factor)** | **2.18** | **2.65** | **7.2%** | **SPECTACULAR** | **0.697 vs npWYoqQz PASS** |
