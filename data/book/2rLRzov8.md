---
alpha_id: "2rLRzov8"
name: "negated_enterprise_value_netdebt_cshtr_blend"
status: "ACTIVE"
submitted: "2026-07-08"
grade: "EXCELLENT"
sharpe: 2.06
fitness: 2.13
turnover: 0.128
expression: "ts_decay_linear(rank(-1 * enterprise_value / close) + rank(anl4_netdebt_flag) + rank(fnd6_cshtr) + rank(fnd6_drlt) + rank(open/close - 1), 5)"
fields:
  - "enterprise_value"
  - "anl4_netdebt_flag"
  - "fnd6_cshtr"
  - "fnd6_drlt"
  - "open"
  - "close"
family: "negated_enterprise_value_blend"
neutralization: "SUBINDUSTRY"
decay: 6
delay: 1
truncation: 0.08
region: "USA"
universe: "TOP3000"
self_corr_max: 0.6495
self_corr_peer: "O0ZOJbaq"
self_corr_result: "PASS"
self_corr_method: "brain_check"
session: "20260706-002"
verified_session: "20260707-001"
brain_url: "https://platform.worldquantbrain.com/alpha/2rLRzov8"
tags:
  - "enterprise_value"
  - "negated_fundamental"
  - "analyst_revision"
  - "cash_quality"
  - "session_20260707-001"
---

# Alpha: 2rLRzov8 — Negated Enterprise-Value Blend

## Expression

`ts_decay_linear(rank(-1 * enterprise_value / close) + rank(anl4_netdebt_flag) + rank(fnd6_cshtr) + rank(fnd6_drlt) + rank(open/close - 1), 5)`

## Mechanism

Five-factor blend anchored on the **negated** enterprise-value-to-price ratio — a
negated-direction fundamental signal (the book-saturation rule's recommended
diversification axis, since the positive-direction `rank(field/close)` core is
saturated):

1. **Negated enterprise value** (`rank(-1 * enterprise_value / close)`): Stocks with
   low enterprise value relative to price (i.e. expensive on EV basis) are shorted /
   underweighted. Equivalently, the signal rewards cheap-EV names. Negating EV (rather
   than the book's usual positive `rank(field/close)`) opens a decorrelated direction
   distinct from the existing fundamental-value book entries.

2. **Net debt revision** (`rank(anl4_netdebt_flag)`): Upward net-debt estimate revisions
   signal improving leverage expectations. Replaces the saturated `anl4_ptpr_flag` core
   — `netdebt_flag` is a less-used analyst flag that decorrelates from the LLR0n261 /
   O0ZOJbaq / O0pl2znv ptpr cluster.

3. **Cash-to-revenue quality** (`rank(fnd6_cshtr)`): Cash conversion efficiency — firms
   generating more cash per unit of revenue are higher quality. This is the same field
   used in O0ZOJbaq and is the main source of the 0.6495 correlation (kept below the
   0.7 auto-pass threshold).

4. **Long-term deferred revenue** (`rank(fnd6_drlt)`): Backlog and revenue
   visibility at the reported level. This is a balance-sheet companion to the
   net-debt revision flag and matches the submitted expression exactly.

5. **Overnight gap** (`rank(open/close - 1)`): The irreplaceable intraday component
   (per 20260702-002 / 20260703-001 lessons: removing it drops below the gate). Captures
   overnight sentiment / opening-order imbalance.

## Self-Correlation Profile

Authoritative BRAIN `/check`: **PASS**, max self-corr **0.6495** vs `O0ZOJbaq`
(S=2.36, coverage_cshtr_ptpr). Below the 0.7 auto-pass threshold — no Sharpe premium
required.

| Peer | Corr | Peer Sharpe | Status |
|------|------|-------------|--------|
| O0ZOJbaq | 0.6495 | 2.36 | auto-PASS (< 0.7) |
| e7O5EQbJ | 0.6115 | 2.50 | auto-PASS (< 0.7) |
| 3q7JQK16 | 0.5111 | 2.40 | auto-PASS (< 0.7) |
| 3q7lm2p6 | 0.5036 | 2.95 | auto-PASS (< 0.7) |
| LLR0n261 | 0.5031 | 2.51 | auto-PASS (< 0.7) |

The correlation is driven by the shared `fnd6_cshtr` + `open/close - 1` components.
Using `anl4_netdebt_flag` (instead of the saturated `anl4_ptpr_flag`) and the negated
EV anchor keeps the signal below the 0.7 wall.

## BRAIN Checks

All 7 computable checks PASS (LOW_SHARPE, LOW_FITNESS, LOW_TURNOVER,
HIGH_TURNOVER, CONCENTRATED_WEIGHT, LOW_SUB_UNIVERSE_SHARPE, MATCHES_COMPETITION).
SELF_CORRELATION: authoritative PASS (0.6495).

## Post-Submission

Submitted on 2026-07-08 by the user (manual submission on the BRAIN platform).
Status flipped from PENDING to ACTIVE.
