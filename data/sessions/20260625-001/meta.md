---
id: "20260625-001"
date: "2026-06-25"
strategy: "EXPLOIT + EXPLORE"
trigger: "manual"
status: "completed"
budget_used: 55
budget_cap: null
gate_passers: 15
submissions: 0
submittable_candidates: 2
branch: "session/20260625-001-explore-novel"
tags:
  - "20260625-001"
candidates:
  - id: "QPaG3OGM"
    grade: "SPECTACULAR"
    sharpe: 3.09
    fitness: 5.14
    self_corr_value: 0.8206
    self_corr_result: "PASS"
    verdict: "WINNER"
  - id: "kq3PVLXK"
    grade: "SPECTACULAR"
    sharpe: 2.91
    fitness: 4.93
    self_corr_value: 0.7344
    self_corr_result: "PASS"
    verdict: "BACKUP"
---

# Session 20260625-001: EXPLOIT + EXPLORE

## Phase 0 Context

50 new SPECTACULAR/EXCELLENT gate-passers appeared in 24h from cross-dataset
fundamental6 × IV60 blend family. All failed either BRAIN checks
(LOW_SUB_UNIVERSE_SHARPE) or self-correlation. Book is heavily saturated with
IV60 variants (KPbEeLez, kq33Gjqk, Gro21wWG, omY3pZq2, etc.).

STRATEGY: Two-track approach:
- Track A: Explore novel fundamental6 anchors (mrct, nopio, cld2) + IV60
- Track B: Fix SUB_UNIVERSE on proven high-Sharpe IV60 expressions

## Phase 1: Triage of Existing Gate-Passers (0 sims)

Checked top 12 SPECTACULAR gate-passers from --new-24h:
- ALL fail either LOW_SUB_UNIVERSE_SHARPE or self-corr (0.73-0.94)
- KPbEeLez (S=2.36) and kq33Gjqk (S=2.63) are ACTIVE in book
- Premium threshold to escape self-corr: S >= 2.893 (1.10x of kq33Gjqk)

## Round 1: Novel Fundamental6 Anchors (20 sims, 0 gate-passers EXCELLENT+)

Tested fnd6_mrct (S=1.53 standalone), fnd6_nopio (S=1.28), fnd6_cld2 (S=1.29),
fnd6_tlcf (S=1.10), anl4_rd_exp_flag, anl4_epsr_flag in combinations with IV60.

**All AVERAGE or INFERIOR.** Best: mrct * nopio + IV60 → AVERAGE S=1.42.
Key learning: Novel fundamental6 fields (mrct, nopio, cld2) have insufficient
standalone signal strength to anchor EXCELLENT+ blends. anl4_rd_exp_flag
actively HURTS performance (S drops 0.35+).

## Round 2: Alternative Tenors + Structures (10 sims, 0 gate-passers)

Tested IV30 spread, IV_put_90, inter-field ratios, MA zscore, volatility gate.
All AVERAGE or INFERIOR. Confirms the novel anchor fields are too weak.

## Round 3: Sharpe Maximization on Proven Template (15 sims, 13 SPECTACULAR)

Pivoted to proven IV60 + analyst/guidance components, varying leg count:

| Alpha | Legs | S | F | SUB_UNIVERSE | Self-Corr |
|-------|------|---|---|-------------|-----------|
| qMANjV02 | 3 (IV60+guid+bvps) | 3.09 | 5.20 | FAIL (1.32/1.34) | 0.821 PASS |
| 78wzZkqQ | 4 (+cshtr) | 3.05 | 4.68 | FAIL (1.08/1.32) | — |
| JjpGxgee | 4 (+cfi_flag) | 2.99 | 5.11 | FAIL (1.28/1.29) | — |
| kq3PVLXK | 4 (+totassets) | 2.91 | 4.93 | **ALL PASS** | 0.734 PASS |

Key insight: Fewer factors → higher Sharpe. 3-factor qMANjV02 (S=3.09) beats
all 4-5 factor variants but barely fails SUB_UNIVERSE (gap = 0.02).

## Round 4: SUB_UNIVERSE Fix via Parameter Sweep (10 sims, 2 ALL PASS)

Swept ts_mean window (22, 44, 66), inner decay (3, 5, 10), platform decay (5, 6, 8, 10).

**QPaG3OGM**: ts_mean window=22 (vs 44 in Round 3) → ALL PASS + S=3.09!
The shorter IV smoothing window increased sub-universe Sharpe ratio enough to
clear the threshold while maintaining identical overall Sharpe.

## Winner: QPaG3OGM

**Expression:**
```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 22)) + rank(max_adjusted_net_income_guidance) + rank(anl4_bvps_flag), 5)
```

**Settings:** SUBINDUSTRY, decay=6, USA TOP3000

**Metrics:**
- Grade: SPECTACULAR (S=3.09, F=5.14, T=7.9%)
- All 8 BRAIN checks: PASS
- Self-correlation: 0.8206 vs Gro21wWG (PASS via Sharpe premium, 3.09 > 2.849)

**Mechanism:** 3-factor cross-dataset blend combining:
1. IV60 call-put spread zscore (22-day smoothing) — directional options sentiment
2. Max adjusted net income guidance rank — forward-looking earnings quality
3. BVPS revision flag — balance sheet revaluation signal

The 22-day IV smoothing (vs 44-day) increases responsiveness to recent sentiment
while maintaining cross-sector uniformity (fixing SUB_UNIVERSE).

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total sims | 55 |
| Gate-passers (S >= 1.0) | 15 |
| SPECTACULAR | 14 |
| ALL PASS + Self-Corr PASS | 2 |
| Winner | QPaG3OGM SPECTACULAR S=3.09 F=5.14 |
| Backup | kq3PVLXK SPECTACULAR S=2.91 F=4.93 |

## Key Learnings

1. **Novel fundamental6 anchors (mrct, nopio, cld2) are too weak** for EXCELLENT+.
   Standalone S~1.3 is insufficient; the book's proven fields (itci, drlt, acdo)
   have S~1.4-1.5 which makes the critical difference.

2. **anl4_rd_exp_flag actively hurts blends** — drops Sharpe by 0.35+. Dead zone
   entry warranted.

3. **Fewer factors = higher Sharpe**: 3-factor (S=3.09) > 4-factor (S=2.91-3.05)
   > 5-factor (S=2.76-2.96). But fewer factors risk SUB_UNIVERSE failure.

4. **IV smoothing window is the key SUB_UNIVERSE lever**: 22-day (PASS) vs 44-day
   (FAIL by 0.02). Shorter smoothing increases cross-sector signal uniformity
   at the cost of slightly more noise.

5. **Self-corr can be escaped with high enough Sharpe**: QPaG3OGM corr=0.82
   vs Gro21wWG but passes because 3.09 > 1.10×2.59 = 2.849.
