---
alpha_id: "omVpwdqk"
status: "ACTIVE"
grade: "EXCELLENT"
fields:
  - "min_adjusted_net_income_guidance"
  - "anl4_ptpr_flag"
  - "fnd6_fate"
  - "anl4_netdebt_flag"
  - "scl12_buzz"
expression: "ts_decay_linear(rank(min_adjusted_net_income_guidance) + rank(anl4_ptpr_flag) + rank(fnd6_fate / close) + rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns)) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
sharpe: 2.55
fitness: 2.47
turnover: 0.2448
neutralization: "SUBINDUSTRY"
decay: 6
region: "USA"
universe: "TOP3000"
self_corr_max: 0.915
self_corr_peer: "6Xzm6PQP"
self_corr_result: "PASS"
family: "guidance_analyst_fundamental_sentiment_blend"
session: "20260622-001"
submitted: "2026-06-22"
brain_url: "https://platform.worldquantbrain.com/alpha/omVpwdqk"
tags:
  - "guidance"
  - "analyst_revision"
  - "fundamental_capex"
  - "sentiment_reversal"
  - "blend"
---

# omVpwdqk — Guidance + Analyst + Capex + Sentiment Reversal Blend

## Expression

`ts_decay_linear(rank(min_adjusted_net_income_guidance) + rank(anl4_ptpr_flag) + rank(fnd6_fate / close) + rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns)) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## Mechanism

Five-factor blend capturing converging signals across distinct information channels:

1. **Earnings guidance floor** (`rank(min_adjusted_net_income_guidance)`): Companies with higher
   minimum net income guidance are signaling management confidence. Market underreacts to
   the downside protection implied by conservative guidance floors.

2. **Analyst pre-tax profit revision** (`rank(anl4_ptpr_flag)`): Upward revisions to
   pre-tax profit estimates signal improving fundamentals before they show up in reported numbers.

3. **Capital expenditure intensity** (`rank(fnd6_fate / close)`): Higher capex relative to
   price signals management willingness to invest, indicating confidence in future cash flows.

4. **Net debt revision reversal** (`rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns))`):
   Combines analyst net debt revisions with price reversal — stocks with improving debt
   outlook that have recently declined are oversold.

5. **Sentiment reversal** (`rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`): Stocks with
   positive social buzz but recent price declines — contrarian signal on attention-driven
   overselling.

Wrapped in `ts_decay_linear(..., 5)` for signal smoothing across rebalances.

## Self-Correlation

Max self-corr: 0.915 vs 6Xzm6PQP (SPECTACULAR, S=2.31). Passes via Sharpe premium
escape: 2.55 >= 2.31 * 1.10 = 2.541. Margin: +0.009 (razor thin).

Full correlation breakdown:
| Peer | Corr | Peer Sharpe | 1.1x Threshold | Status |
|------|------|-------------|----------------|--------|
| 6Xzm6PQP | 0.915 | 2.31 | 2.541 | PASS (2.55 > 2.541) |
| pw8wNe76 | 0.794 | 2.09 | 2.299 | PASS (2.55 > 2.299) |
| LLR0n261 | 0.659 | 2.51 | — | auto-PASS (corr < 0.7) |
| np30Odjd | 0.648 | 1.87 | — | auto-PASS (corr < 0.7) |
| blL55wRp | 0.647 | 2.10 | — | auto-PASS (corr < 0.7) |

## Submission

- All 7 computable BRAIN checks: PASS
- SELF_CORRELATION: PASS (authoritative BRAIN API check)
- Submitted: 2026-06-22
