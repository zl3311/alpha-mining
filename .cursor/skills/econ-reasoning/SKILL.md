---
name: econ-reasoning
description: >-
  Reason about economic mechanisms behind alpha signals. Use when you need to
  understand WHY a factor predicts returns, classify signals into mechanism
  families, predict self-correlation from economic logic, or evaluate whether
  a statistical discovery has a real economic basis.
  Trigger on: mechanism, why does this work, economic, fundamental, factor
  family, self-correlation prediction, signal classification, sweep discovery.
---

# Economic Reasoning for Alpha Mining

This skill teaches you to think about economic mechanisms rather than just
Sharpe numbers. Every factor that predicts returns does so for a reason --
understanding that reason helps you generate better signals, avoid redundant
submissions, and predict self-correlation without wasting simulation budget.

## Core Principle

A factor's economic mechanism determines its signal family more reliably than
its statistical correlation. Two factors can have low PnL correlation but share
the same mechanism (different proxies for the same effect). Conversely, two
factors can look statistically similar over a backtest window but be driven by
entirely different mechanisms (and thus diverge out-of-sample).

Always ask: **what economic behavior does this expression capture?**

## Mechanism Taxonomy for BRAIN Alphas

When classifying a factor, map it to one of these mechanism families. Each
family exploits a different market inefficiency, so cross-family signals are
likely to have low self-correlation.

### 1. Short-term reversal (mean reversion)
- **Why it works**: Liquidity provision and overreaction. Market makers demand a
  spread; retail order flow creates transient price pressure that reverts.
- **Fields**: `returns`, `open/close`, `high/low`, `volume`, `adv20`
- **Time horizon**: 1-5 days
- **Book status**: SATURATED (RRN1EM51, zq5RLWO8). New reversal variants will
  self-correlate at 0.80+. Do not submit more reversal signals.
- **Example**: `ts_decay_linear(rank(-1*returns)*rank(volume/adv20), 5)`

### 2. Analyst revision momentum
- **Why it works**: Analysts revise estimates incrementally. A revision today
  predicts further revisions in the same direction (information is released
  slowly, not all at once). Market underreacts to the first revision.
- **Fields**: `anl4_*_flag` (binary revision indicators), `anl4_*_ft` (estimates)
- **Time horizon**: 5-20 days
- **Book status**: PARTIALLY EXPLOITED (vR56vdYd uses ptp_flag + bvps_flag).
  Other revision flags (totassets, cfi, ptpr) are untapped.
- **Example**: `rank(anl4_ptp_flag) * 2 + rank(anl4_bvps_flag) + rank(buzz)`

### 3. Fundamental value / quality
- **Why it works**: Cheap stocks (relative to fundamentals) outperform expensive
  stocks over medium horizons. Quality signals (low debt, high profitability)
  predict returns because the market misprice distressed firms.
- **Fields**: `fnd6_*` (balance sheet, income statement), `sales_ps`, `bookvalue_ps`
- **Time horizon**: 5-60 days (slower)
- **Book status**: EXPLOITED via itci, acdo, dpactq, fate, ffo, netdebt_rev.
  But the family is broad -- many untapped fundamental fields exist.
- **Self-corr note**: Value-normalized fundamentals (`field / close`) tend to
  correlate with each other at 0.3-0.5. Blending with non-value signals reduces
  this. Pure fundamental blends need neutralization variation (MARKET vs
  SUBINDUSTRY) to reduce cross-signal correlation.

### 4. Company guidance / forward-looking
- **Why it works**: Management guidance signals private information about future
  earnings. The market reacts to guidance announcements but underweights the
  magnitude and persistence of the signal.
- **Fields**: `*_guidance` fields (min/max adjusted net income guidance, etc.)
- **Time horizon**: 5-20 days
- **Book status**: EXPLOITED (6Xzm6PQP uses guidance). But guidance + different
  combinations may still have room.

### 5. Sentiment / social media
- **Why it works**: Retail sentiment (buzz volume, bullishness) is a contrarian
  indicator at short horizons. High buzz + negative returns = overreaction.
- **Fields**: `scl12_buzz`, `scl12_*` (sentiment scores)
- **Time horizon**: 1-5 days
- **Book status**: Used as STABILIZER (buzz fixes SUB_UNIVERSE check due to
  100% coverage). Not exploited as a primary signal family.
- **Opportunity**: Pure sentiment signals (not just as stabilizer) are untested.

### 6. Rare events / structural changes
- **Why it works**: Discrete corporate events (HQ relocation, M&A, restatement)
  create information shocks that the market processes slowly.
- **Fields**: `fnd6_city` (HQ location delta), other flag/indicator fields
- **Time horizon**: variable
- **Book status**: NOT SUBMITTED. fnd6_city had F=3.07 SPECTACULAR with MARKET
  neut but fails CONCENTRATED_WEIGHT (too sparse). Needs blending or a
  different conditional structure.

### 7. Options-implied / volatility
- **Why it works**: Options prices embed forward-looking information about
  expected moves. Implied vol spreads, skew, and put-call ratios can predict
  returns when they diverge from realized patterns.
- **Fields**: `option8_*` (implied vol, greeks, put/call ratios)
- **Time horizon**: 1-10 days
- **Book status**: EXPLOITED (vRm07LP3 uses IV spread; omY3pZq2 uses
  sentiment-IV spread; 88z7MM37 / ZYpk2kx8 use IV60 fundamental blends;
  Gro21wWG PENDING uses IV90 vol-regime spread). IV spread variants are a
  known saturated family. Novel IV structures or cross-family IV interactions
  may still have room.

### 8. Earnings / financial reporting
- **Why it works**: Post-earnings announcement drift (PEAD) is one of the most
  robust anomalies. Stocks with positive earnings surprises continue to drift
  up for 20-60 days. Accruals anomaly: high accruals predict negative returns.
- **Fields**: `fnd6_eps*`, `fnd6_ni*` (net income), accrual-related fields
- **Time horizon**: 5-60 days
- **Book status**: PARTIALLY EXPLORED via fundamental blends. Pure earnings
  surprise / accruals signals not directly tested.

## How to Reason About Self-Correlation

Self-correlation on BRAIN is measured via PnL Pearson correlation over a 4-year
window. Two signals self-correlate when they generate similar daily portfolio
returns -- which happens when they rank stocks similarly.

**Predict self-correlation from mechanisms:**

| Comparison | Expected self-corr | Why |
|------------|-------------------|-----|
| Same mechanism, same fields | > 0.80 | Near-identical portfolio weights |
| Same mechanism, different fields | 0.40 - 0.70 | Similar but not identical rankings |
| Different mechanisms, no shared fields | < 0.20 | Uncorrelated portfolio weights |
| Different mechanisms, shared stabilizer (buzz) | 0.20 - 0.40 | Stabilizer creates modest correlation |
| Same expression, different neutralization | 0.50 - 0.80 | Neutralization shifts weights materially |

**Rules of thumb from experiments:**
- All PV reversal variants correlate at 0.80+ (saturated family)
- Cross-family (reversal vs fundamental) correlates at < 0.10
- Blends sharing `* (-1 * returns)` reversal component correlate at 0.60-0.80
  regardless of other factors (the reversal dominates PnL)
- Pure analyst revision blends correlate at ~0.51 with the submitted book
- Neutralization variation (SUBINDUSTRY → MARKET) can reduce self-corr by 0.10-0.15

## Classifying Sweep Discoveries

When a new factor appears from the background sweep, classify it:

1. **Read the field name and dataset.** The naming convention reveals the source:
   - `fnd6_*` → fundamental6 (balance sheet / income statement)
   - `anl4_*` → analyst4 (analyst estimates and revisions)
   - `scl12_*` → socialmedia12 (sentiment)
   - `option8_*` → options data
   - `news12_*` → news sentiment
   - `*_guidance` → company forward guidance

2. **Identify the mechanism family** from the taxonomy above. If a field is
   `anl4_totassets_flag`, it's an analyst revision signal (family 2). If it's
   `fnd6_dlto / close`, it's a fundamental value signal (family 3).

3. **Check for overlap** with the submitted book. If the factor belongs to an
   already-exploited family, self-corr risk is elevated. Check `data/book/`
   and `data/factors/` for which families have submitted alphas.

4. **If no mechanism is apparent**, label it as `mechanism: UNKNOWN` in the
   factor file (`data/factors/`) and deprioritize it relative to
   mechanism-backed factors. Statistical signals without economic backing are
   more likely to be data-mined artifacts that won't persist out-of-sample.

## When You See a High-Sharpe Signal

Before recommending submission, always ask:

1. **What mechanism drives this?** If you can't name one, be skeptical.
2. **Is this mechanism independent of the submitted book?** Check the taxonomy.
3. **Does the sign make economic sense?** A long-cheap/short-expensive signal
   should have a positive sign on value metrics. Opposite sign = suspicious.
4. **Would this mechanism survive a regime change?** A factor that only works
   during low-rate environments (2020-2021) may not persist.
5. **Is the coverage appropriate for the mechanism?** Rare-event factors should
   have low coverage. A "rare event" factor with 100% coverage is not rare.
