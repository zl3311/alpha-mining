---
id: "20260716-001-results"
session: "20260716-001"
total_expressions: 88
gate_passers: 48
best_sharpe: 2.29
best_fitness: 2.26
best_alpha_id: "aknmG1M6"
---

# Results: Session 20260716-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 88 |
| Gate-passers (S>=1.0, F>=0.8, loose) | 48 |
| Best Sharpe | 2.29 |
| Best Fitness | 2.26 |
| Budget used | 88 / unlimited |

## Top Candidates (EXCELLENT grade, S>=1.25 F>=1.0)

| # | Alpha ID | Expression (truncated) | Sharpe | Fitness | Turnover | Local Self-Corr | Verdict |
|---|----------|------------------------|--------|---------|----------|------------------|---------|
| 1 | aknmG1M6 | cld2+fopo+2*ivaco+2*buzz(w10) | 2.29 | 2.26 | 11.9% | 0.618 | **RISKY (best)** |
| 2 | aknmGlax | cld2+fopo+ivaco+2*buzz(w20) | 2.23 | 2.13 | 15.1% | 0.641 | REDUNDANT (0.93 corr w/ #1) |
| 3 | 3qRmkvjZ | cld2+fopo+ivaco+2*buzz(w5) | 2.25 | 2.03 | 17.0% | 0.643 | REDUNDANT (0.95 corr w/ #4) |
| 4 | 781PMO7v | cld2+fopo+ivaco+2*buzz(w10) | 2.22 | 2.10 | 15.5% | 0.644 | REDUNDANT |
| 5 | 0mEZNqM8 | cld2+fopo+ivaco+drlt+2*buzz(w5) | 2.21 | 2.05 | 15.8% | 0.655 | REDUNDANT (superseded by #1) |
| 6 | GrLjgZrx | event-mag(fopo)+leverage+ivaco+drlt+buzz | 2.16 | 2.21 | 10.6% | 0.926 | **BLOCKED** |
| 7 | mLbnoxP2 | cld2+leverage+ivaco+buzz(no drlt) | 2.01 | 2.03 | 11.1% | 0.776 | **BLOCKED** |
| 8 | lelwMPGl | event-mag(cld2)+leverage+ivaco+drlt+buzz | 1.97 | 2.00 | 10.9% | 0.775 (est.) | **BLOCKED** |

## Family/Structure Ablation Summary (fnd6_cld2 + fnd6_fopo anchors)

| Stabilizer set | Best F | Local self-corr |
|---|---|---|
| leverage + ivaco + drlt + flag/buzz (full stack) | 2.00-2.21 | 0.775-0.926 BLOCKED |
| Full stack, MARKET neutralization | 1.87 | 0.664-0.679 (RISKY, but grade dropped to GOOD) |
| ivaco + drlt + buzz (no leverage) | 1.93-1.96 | 0.637 |
| **2x ivaco + 2x buzz(w10) (no leverage, no drlt)** | **2.26** | **0.618 (best)** |
| ivaco + buzz (1x each, no leverage/drlt) | 1.65-1.86 | not individually checked (subset of above) |
| leverage only (no ivaco/drlt/buzz) | 1.06-1.19 | not checked (AVERAGE, too weak) |
| ivaco only / drlt only (no leverage/buzz) | 0.84-1.17 | not checked (too weak) |
| buzz only (no ivaco/leverage/drlt) | 1.42-1.65 | not checked |
| No shared leg (2-3 fresh anchors only) | 0.64-0.98 | not checked (too weak) |

## All Rounds

| Round | # Sims | Focus | Best F this round |
|---|---|---|---|
| 1 | 18 | Novel operator trees (multi-horizon, MA-crossover, regime-divergence, decay-wrap, fresh blends, negation, sentiment) | 0.94 (INFERIOR) |
| 2 | 12 | Untapped model51 risk dataset | 0.71 (INFERIOR) |
| 3 | 8 | Fresh anchor + leverage only (2-leg minimal) | 1.19 (AVERAGE) |
| 4 | 8 | Product forms, dual quality legs (cash/assets, debt_lt/assets) | 1.18 (AVERAGE) |
| 5 | 6 | Full proven stabilizer stack on fresh anchors | 2.21 (EXCELLENT, BLOCKED) |
| 6 | 3 | MARKET neutralization escape | 1.75 (GOOD) |
| 7 | 4 | MARKET neut without leverage leg | 1.87 (GOOD) |
| 8 | 6 | Isolate single shared leg (ivaco-only, drlt-only, buzz-only, 3-fresh-anchor) | 1.93 (GOOD) |
| 9 | 5 | Push leverage-free 5-leg toward EXCELLENT via weighting | 2.05 (EXCELLENT) |
| 10 | 4 | Drop drlt too; vary weight distribution | 2.03 (EXCELLENT) |
| 11 | 4 | Volatility-gate + buzz-window sweep | 2.10 (EXCELLENT) |
| 12 | 4 | No-buzz, ivaco-weighted low-turnover variants | 1.27 (AVERAGE) |
| 13 | 3 | Fine-tune buzz window + ivaco weight | 2.26 (EXCELLENT, best) |
| 14 | 3 | Further weight/anchor-count variations around the peak | 2.00 (GOOD) |

## BRAIN Check Results

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|-------------------|---------------------|
| aknmG1M6 | PASS | PASS | PASS | PASS | PASS | PASS | **UNRESOLVED** (API timeout during platform degradation) | PASS |
| aknmGlax | PASS | PASS | PASS | PASS | PASS | PASS | UNRESOLVED | PASS |
