---
id: "20260712-001-results"
session: "20260712-001"
total_expressions: 44
gate_passers: 39
winner: "VkPdaQ2b"
winner_grade: "SPECTACULAR"
winner_sharpe: 2.18
winner_fitness: 2.65
winner_self_corr: 0.697
winner_self_corr_result: "PASS (local estimate ≤ 0.70 auto-pass threshold)"
---

# Results: Session 20260712-001 (EXPLORE)

## Summary

| Metric | Value |
|--------|-------|
| Total expressions | 44 |
| Rounds | 4 |
| Gate-passers (S≥1.25, F≥1.0) | 39 |
| EXCELLENT+ with BRAIN ALL PASS | 8 |
| Self-corr PASS | 1 (VkPdaQ2b) |
| Winner | **VkPdaQ2b** — SPECTACULAR S=2.18, F=2.65, T=7.2% |

## Round-by-Round Summary

### Round 1 (10 sims, tag: r1_gric_spread)
**Target:** `anl4_gric_flag` multi-horizon spread + leverage + fresh stabilizers (avoiding saturated skeleton)

Best results:
- **1Ydj7VzJ**: EXCELLENT S=2.30, F=2.18, T=12.9% — `gric_flag spread + leverage + ivaco + buzz`
  - Self-corr: 0.925 vs WjGVJ7bN → BLOCKED (gric_flag spread is PnL-similar to txw event-magnitude; 3 shared stabilizers compounded the correlation)
- wpl9RVw2: GOOD S=2.27, F=1.99 — spread + leverage + buzz (no ivaco)
- O0ZJpK9J: GOOD S=1.93, F=1.69 — spread + leverage + ivaco + drlt

**Learning:** The `anl4_gric_flag` multi-horizon spread fires at the same timing as the `fnd6_txw` event-magnitude signal (both around earnings/corporate events), creating high base correlation. Without buzz+ivaco, grade drops to AVERAGE. Direction abandoned.

### Round 2 (12 sims, tag: r2_epsr_fatl_dlto)
**Target:** `anl4_epsr_flag` event-magnitude (fresh analyst anchor) + {YP0bLdzA, WjGVJ7bN} stabilizer sets

Best results:
- **LL15dWke**: SPECTACULAR S=2.68, F=2.71 — `epsr + leverage + ivaco + drlt + buzz` → BRAIN ALL PASS
- **kq0JZQ9d**: SPECTACULAR S=2.63, F=2.64 → BRAIN ALL PASS
- **6X9AeZOO**: SPECTACULAR S=2.28, F=2.52 — `fatl event + gric + ivaco + buzz` → BRAIN ALL PASS
- **omlogmVl**: EXCELLENT S=2.40, F=2.29 — `epsr event + gric + ivaco + buzz`
- **LL15GVAm**: EXCELLENT S=2.13, F=2.23 — `dlto event + gric + ivaco + buzz`

Self-corr check on omlogmVl, 6X9AeZOO, LL15GVAm, N1rerYEo: ALL BLOCKED (0.768-0.908 vs WjGVJ7bN).

**Learning:** `anl4_epsr_flag` event-magnitude is also earnings-timed → 0.908 vs WjGVJ7bN. ALL event-magnitude fundamentals using {ivaco+buzz} stabilizers correlate 0.7-0.9 with WjGVJ7bN/wpl5eP5v/YP0bLdzA.

### Round 3 (12 sims, tag: r3_ivfresh)
**Target:** Fresh fundamentals + IV spread stabilizer (orthogonal to event-magnitude book family); reduced-stabilizer blends (no ivaco/drlt)

Best results:
- **9qrEVpMV**: SPECTACULAR S=2.33, F=2.96, T=7.0% — `cptmfmq_dlttq event + leverage + zscore(IV_270, 22)`
  - BRAIN ALL PASS. Self-corr: 0.758 vs omY3pZq2 → BLOCKED (escape threshold 2.343, we have 2.33 — 0.013 short!)
- **WjGL7GPj**: EXCELLENT S=2.06, F=2.47, T=7.0% — `dlto event + leverage + zscore(IV_270, 22)`
  - BRAIN ALL PASS. Self-corr: 0.733 → BLOCKED
- **6X9ArRjY**: EXCELLENT S=1.94, F=2.02 — `cptmfmq event + gric + buzz` → BLOCKED 0.775

**Learning:** The IV zscore(22) stabilizer overlaps with `omY3pZq2` (sentiment_buzz_iv_spread) which uses the EXACT same expression `zscore(ts_mean(IV_call_270 - IV_put_270, 22))`. A 3-factor blend (1/3 IV weight) gives 0.758 max corr.

### Round 4 (10 sims, tag: r4_iv_variants)
**Target:** Push 9qrEVpMV's correlation with omY3pZq2 below 0.70 by changing IV form or adding 4th component

Results:
- **mLbY6OGE**: SPECTACULAR S=2.31, F=2.91 — `cptmfmq event (d=5) + leverage + zscore(IV, 22)` → BRAIN ALL PASS, self-corr 0.758 (still BLOCKED)
- **VkPdaQ2b**: SPECTACULAR S=2.18, F=2.65 — `cptmfmq event + leverage + zscore(IV, 22) + gric_flag` → BRAIN ALL PASS, **self-corr 0.697 vs npWYoqQz → AUTO-PASS** ← **WINNER**
- Other IV form variants (IV delta, IV 10-day, IV 180-day): GOOD grade only (S=1.67-1.85)
- 2 trade_when vol-gated expressions: FAILED (BRAIN unit type error for abs-delta inside trade_when)

**Learning:** Adding gric_flag as 4th component dilutes the IV weight from 1/3 to 1/4, dropping omY3pZq2 correlation from 0.758 → 0.670 and shifting the max peer to npWYoqQz at 0.697 (AUTO-PASS).

## Winner: VkPdaQ2b

**Expression:**
```
ts_decay_linear(rank(abs(ts_delta(fnd6_cptmfmq_dlttq / close, 3))) + rank(-1 * equity / assets) + zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)) + rank(anl4_gric_flag), 5)
```

**Metrics:** SPECTACULAR S=2.18, F=2.65, T=7.2%

**BRAIN checks:** ALL PASS (7 checks; SELF_CORRELATION PENDING at session end)

**Self-corr (local PnL vs 46 ACTIVE book entries):**
- Max: 0.697 vs `npWYoqQz` (iv_fundamental_analyst_blend, S=2.09) → AUTO-PASS (≤ 0.70)
- 2nd: 0.670 vs `omY3pZq2` (sentiment_iv_spread, S=2.13) → AUTO-PASS
- All other 44 entries: ≤ 0.622

**Platform URL:** https://platform.worldquantbrain.com/alpha/VkPdaQ2b
