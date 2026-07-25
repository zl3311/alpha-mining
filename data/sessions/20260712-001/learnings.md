---
session: "20260712-001"
type: "learnings"
---

# Learnings: Session 20260712-001

## Key Discoveries

### 1. gric_flag Multi-Horizon Spread — Blocked by Primary Signal Correlation

The `ts_delta(anl4_gric_flag, 5) - ts_delta(anl4_gric_flag, 22)` multi-horizon spread (EXCELLENT S=2.53 on the skeleton from prior sessions) gives 0.925 self-corr vs WjGVJ7bN when combined with leverage+ivaco+buzz. Root cause: the gric_flag spread is PnL-similar to the txw event-magnitude signal (both are corporate event detectors), AND the shared stabilizers compound this. **Do not retry gric_flag multi-horizon spread as a primary signal.**

### 2. Analyst Flag Event-Magnitude Also Fires at Earnings Time

`anl4_epsr_flag` event-magnitude (`abs(ts_delta(anl4_epsr_flag, 3))`) reaches SPECTACULAR S=2.68 but shows 0.908 self-corr vs WjGVJ7bN. Both `abs(ts_delta(analyst_flag, d))` and `abs(ts_delta(fundamental_quarterly, d))` fire primarily around earnings releases → highly correlated in PnL space regardless of the specific fields used. **Avoid analyst-flag event-magnitude as primary signal in the event-magnitude template family.**

### 3. The IV Spread Stabilizer Creates IV-Family Overlap

Using `zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22))` inside any blend creates 0.64-0.76 correlation with:
- vRm07LP3 (options_iv_spread, 0.582-0.647)
- omY3pZq2 (sentiment_iv_spread, which uses this EXACT expression × buzz, 0.670-0.758)
- npWYoqQz (iv_fundamental_analyst_blend, 0.697-0.716)

The max correlation peer depends on the primary signal and other stabilizers. With `cptmfmq_dlttq` event-magnitude + leverage (3-factor), the max is omY3pZq2 at 0.758.

### 4. Diluting IV Weight to 1/4 Breaks the Correlation Wall

Adding a 4th component (gric_flag) to the 3-factor cptmfmq+leverage+IV blend:
- Reduces IV from 1/3 → 1/4 of the blend weight
- Shifts timing via gric_flag's analyst guidance update cycle (decorrelated from buzz×IV)
- Drops omY3pZq2 corr: 0.758 → **0.670**
- Drops npWYoqQz corr: 0.716 → **0.697** (new max, AUTO-PASS)

**Pattern: Use a fresh non-IV 4th component to dilute the IV weight when the 3-factor IV blend exceeds 0.70 vs the IV family.**

### 5. Vol-Gated trade_when Fails for abs-delta Inner Expressions

Confirmed again: `trade_when(cond, ts_decay_linear(rank(abs(ts_delta(F/close, d))) + ...), exit)` causes BRAIN unit-type error ("Incompatible unit for input of..."). This is a structural limitation of the BRAIN type system. Vol-gate only works with LEVEL/RANK inner expressions (cf. 0m7lnAEr which uses `rank(field/close)` not `rank(abs(ts_delta(field/close,d)))`).

### 6. Fresh Fundamental × IV Spread Cross-Dataset Blends Are Productive

`fnd6_cptmfmq_dlttq` + leverage + IV spread zscore: SPECTACULAR S=2.33, F=2.96. This cross-dataset template (fundamental event-magnitude × options directional signal) is a genuinely novel mechanism family with low correlation to the event-magnitude book entries (WjGVJ7bN: 0.547; YP0bLdzA: 0.435) because the stabilizer (IV spread) is orthogonal to the event-magnitude family's stabilizers (ivaco/buzz/drlt).

## Dead Zones Updated

None new (existing dead zones correctly identified the blocked directions).

## Patterns to Record

A new pattern should be documented:
- **fresh-fundamental-event-magnitude-iv-gric**: `ts_decay_linear(rank(abs(ts_delta(FRESH_FIELD/close, 3))) + rank(-1 * equity/assets) + zscore(ts_mean(IV_call_270 - IV_put_270, 22)) + rank(anl4_gric_flag), 5)`
- Best result: VkPdaQ2b (SPECTACULAR S=2.18, F=2.65, T=7.2%, self-corr 0.697 AUTO-PASS)
- Applicable fresh fields: fnd6_cptmfmq_dlttq (tested), potentially fnd6_dlto, fnd6_fatl (need re-test without 4th component)

## Fields Profiled This Session

| Field | Template | Best S | Best F | Best Grade | Notes |
|-------|----------|--------|--------|------------|-------|
| anl4_gric_flag (spread) | multi-horizon spread + leverage + ivaco + buzz | 2.30 | 2.18 | EXCELLENT | 0.925 self-corr BLOCKED |
| anl4_epsr_flag | event-magnitude + leverage + gric + ivaco + buzz | 2.68 | 2.71 | SPECTACULAR | 0.908 self-corr BLOCKED |
| fnd6_fatl | event-magnitude + leverage + gric + ivaco + buzz | 2.28 | 2.52 | SPECTACULAR | 0.768 self-corr BLOCKED |
| fnd6_dlto | event-magnitude + leverage + gric + ivaco + buzz | 2.13 | 2.23 | EXCELLENT | 0.822 self-corr BLOCKED |
| fnd6_cptmfmq_dlttq | event-magnitude + leverage + IV_zscore + gric_flag | 2.18 | 2.65 | SPECTACULAR | 0.697 PASS ← winner |

## Open Questions for Future Sessions

1. Can `fnd6_dlto` or `fnd6_fatl` reach self-corr PASS with the 4-factor IV+gric template? (Not tested in this session)
2. Can higher-Sharpe variants of VkPdaQ2b be found (S>2.30) for better Sharpe premium escape headroom?
3. Does `fnd6_cptmfmq_dlttq` work in the negated direction (`rank(-1 * fnd6_cptmfmq_dlttq / close)`) for a different mechanism family?
