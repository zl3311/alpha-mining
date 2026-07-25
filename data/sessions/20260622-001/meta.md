---
id: "20260622-001"
date: "2026-06-22"
strategy: "EXPLORE + EXPLOIT"
trigger: "manual"
status: "completed"
budget_used: 67
gate_passers: 2
submitted: ["omVpwdqk"]
---

# Session 20260622-001

## Strategy

Mixed EXPLORE + EXPLOIT. The book was saturated (18 ACTIVE entries across ~10 families).
Self-corr wall blocks most high-Sharpe variants. Two-phase approach:

1. Triage existing EXCELLENT/SPECTACULAR candidates from HF server
2. Generate novel candidates with focus on event-magnitude transforms and cross-family blends

## Phase 1: Existing Candidate Triage

Checked top 16 existing EXCELLENT/SPECTACULAR candidates:

| Alpha | Grade | Sharpe | Fitness | Self-Corr Result | Top Peer |
|-------|-------|--------|---------|------------------|----------|
| vRmpvZMw | EXCELLENT | 3.04 | 2.48 | FAIL (0.982) | d5Q3ZmWv S=2.97 |
| RRrlmbp1 | EXCELLENT | 2.92 | 2.50 | FAIL (0.959) | d5Q3ZmWv S=2.97 |
| WjgoAprO | EXCELLENT | 2.75 | 2.50 | FAIL (0.938) | d5Q3ZmWv S=2.97 |
| xAn2x3zp | EXCELLENT | 2.47 | 2.48 | FAIL (0.979) | 0m8GV1Pp S=2.64 |
| **omVpwdqk** | **EXCELLENT** | **2.55** | **2.47** | **PASS (0.915)** | 6Xzm6PQP S=2.31 |
| 1YgMZ6OW | SPECTACULAR | 2.73 | 4.38 | FAIL (0.966) | Gro21wWG S=2.59 |
| zqOojxeK | SPECTACULAR | 2.59 | 3.00 | FAIL (0.891) | 0mzQQvX8 S=2.43 |
| blvvlQAR | SPECTACULAR | 2.14 | 2.75 | FAIL (0.832) | xARzmVEW S=2.05 |
| lerlAg5l | SPECTACULAR | 2.23 | 2.73 | FAIL (0.823) | xARzmVEW S=2.05 |

Key finding: omVpwdqk passes self-corr via Sharpe premium but with razor-thin margin
(2.55 vs 2.541 required, +0.009). Submitted by user during session.

## Phase 2: Signal Generation (67 sims)

Nine batches submitted targeting:
- **Batch A** (7): fn_accrued_liab_q Sharpe boosters (trade_when + event-magnitude)
- **Batch B** (6): omVpwdqk margin wideners
- **Batch C** (10): Novel structures (dynamic correlation, inter-field ratios, momentum acceleration)
- **Batch D** (4): MARKET neutralization variants
- **Batch E** (6): More fn_accrued_liab mutations
- **Batch F** (6): fn_accrued_liab blend variants
- **Batch G** (14): Novel field explorations (pcr_vol, est_tbv_ps, return_assets, etc.)
- **Batch H** (8): More novel fields (news_short_interest, composite_factor_score, etc.)
- **Batch I** (6): Fixed trade_when with ts_rank condition

### Key results (partial — batch still processing):

| Alpha | Grade | Sharpe | Fitness | Expression (abbrev) | Self-Corr |
|-------|-------|--------|---------|---------------------|-----------|
| **ZYpjKeKx** | **EXCELLENT** | **2.49** | **2.25** | abs(ts_delta(fn_accrued_liab_q/close, 3)) + cfi + bvps + buzz*ret | **PASS (0.750)** |
| RRpN1Rmg | EXCELLENT | 1.95 | 2.34 | abs(ts_delta(fn_accrued_liab_q/close, 5)) + cfi + bvps | not checked |

### Lessons learned:
- `trade_when(ts_std_dev(returns, 20) > 0.02, ...)` causes BRAIN unit error (TSPrice vs unitless)
- `trade_when(ts_rank(...) > 0.7, ...)` compiles but destroys signal (AVERAGE/INFERIOR)
- `abs(ts_delta(field/close, 3))` event-magnitude transform effectively boosts fn_accrued_liab_q
  Sharpe from 2.23 → 2.49 (+12%) while also reducing self-corr (novel tree shape)

## Outcomes

| Alpha | Grade | Sharpe | Status | Self-Corr Margin |
|-------|-------|--------|--------|------------------|
| omVpwdqk | EXCELLENT | 2.55 | SUBMITTED | +0.009 (thin) |
| ZYpjKeKx | EXCELLENT | 2.49 | CANDIDATE | +0.235 (robust) |

## Knowledge updates

- New pattern: `abs(ts_delta(field/close, d))` event-magnitude transform reduces self-corr
  by changing the operator tree shape while maintaining Sharpe. Filed in patterns/.
- Dead zone update: `trade_when(ts_std_dev(returns, d) > literal)` causes BRAIN unit error.
  Use `ts_rank(ts_std_dev(returns, d), 252)` condition instead, but this destroys signal
  quality for fundamental blends.
