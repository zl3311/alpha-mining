---
category: "rule"
severity: "critical"
discovered: "20260606"
source: "manual_verification_vs_brain"
updated: "20260606"
---

# PnL Correlation Underestimates BRAIN Self-Correlation When Alphas Share Data Fields

## The Rule

**NEVER trust pnl_correlation.py as the sole self-corr gate.** When a candidate
shares raw data fields (e.g. `implied_volatility_call_270`) with a book entry,
BRAIN's self-correlation can be **1.45-1.6x higher** than PnL return correlation.

## BRAIN Self-Correlation Check Model (confirmed)

The BRAIN self-corr check is a **TWO-GATE system**:

1. **Gate 1 (correlation threshold = 0.7)**: PnL return correlation > 0.7
   against any submitted alpha in your book.
2. **Gate 2 (Sharpe premium = 1.10x)**: If Gate 1 triggers, the candidate's
   Sharpe must be >= 1.10x the max Sharpe among all peers with corr > 0.7.

Decision logic:
- If **no peer** has corr > 0.7: **auto PASS** regardless of Sharpe.
- If peers exist > 0.7 **and** candidate Sharpe >= 1.10x max peer Sharpe: **PASS**.
- If peers exist > 0.7 **and** candidate Sharpe < 1.10x max peer Sharpe: **FAIL**.

Source: https://github.com/WeidongFang1985/WorldQuant-SelfCorrelation-UserStage

## Key API Endpoints

| Endpoint | Purpose | Free-tier access |
|----------|---------|-----------------|
| `/alphas/{id}/check` | Authoritative PASS/FAIL for all 8 submission checks including SELF_CORRELATION. Returns `result`, `value`, `limit` per check. | Yes |
| `/alphas/{id}/correlations/self` | Full breakdown of self-correlation vs every alpha in your book. | Yes |
| `/alphas/{id}/correlations/prod` | Correlation vs production alphas (platform-wide). | **403 Forbidden** on free tier |

The `/check` endpoint is authoritative: `result: PASS` can coexist with
`value > limit` when the Sharpe premium escape is met.

## Local PnL Correlation vs BRAIN Self-Correlation

**When candidate shares NO data fields with book entries:**
- PnL return corr ≈ BRAIN self-corr (multiplier ≈ 1.0x, verified)
- Use 0.7 as the effective threshold
- Below 0.7: SAFE. Above 0.7: need 1.10x Sharpe premium.

**When candidate shares data fields with book entries:**
- BRAIN self-corr is 1.45-1.59x higher than PnL return corr
- PnL corr 0.40-0.50 → BRAIN sees 0.65-0.80 → likely triggers Gate 1
- PnL corr < 0.35 with shared fields → BRAIN sees ~0.55 → likely SAFE

## Evidence (2026-06-06, session 20260606-002)

Submitted `npWYoqQz` (IV270 spread + fundamentals blend, SPECTACULAR, S=2.09).
Then tested 6 candidates from the sentiment × IV family (all use
`ts_mean(IV_call_270 - IV_put_270, 22)`):

### Correlation multiplier (local PnL vs BRAIN)

| Alpha | PnL Corr vs Book | BRAIN Self-Corr | Multiplier |
|-------|-----------------|-----------------|------------|
| omY3pZq2 | 0.568 | 0.824 | 1.45x |
| xAnPMaZw | 0.584 | 0.891 | 1.53x |
| e7rdA5rM | 0.588 | 0.926 | 1.57x |
| XgK2qEOX | 0.582 | 0.889 | 1.53x |
| MPxKOZmM | 0.576 | 0.914 | 1.59x |
| WjgaMznd | 0.571 | 0.909 | 1.59x |

Control cases (no shared fields with the correlated book entry):

| Alpha | PnL Corr | BRAIN Self-Corr | Multiplier |
|-------|----------|-----------------|------------|
| ZYrr25Mx | 0.748 | 0.748 | 1.00x |
| pw8XoonV | 0.988 | 0.988 | 1.00x |

### Sharpe premium PASS/FAIL evidence

The peer alpha `npWYoqQz` (a.k.a. `vRm07LP3`) has Sharpe = 1.82.
The 1.10x premium threshold is therefore **2.002**.

| Alpha | BRAIN Self-Corr | Candidate Sharpe | 1.10x Threshold | BRAIN Check |
|-------|----------------|-----------------|-----------------|-------------|
| omY3pZq2 | 0.824 | 2.13 | 2.002 | **PASS** (Sharpe premium met) |
| e7rdA5rM | 0.926 | 1.88 | 2.002 | **FAIL** (Sharpe below premium) |

## Implication for Mining

Before calling any candidate "submittable":
1. Check whether it shares ANY raw data field with ANY book entry.
2. If yes, apply the 1.6x safety factor to PnL correlation.
   The effective PnL threshold becomes **~0.44** (0.7 / 1.6) for shared-field alphas.
3. Even if corr > 0.7 on BRAIN, the candidate can still pass if its Sharpe
   exceeds 1.10x the max peer Sharpe. Check via `/alphas/{id}/check`.

## Why the Local-vs-BRAIN Gap Exists

BRAIN likely computes self-correlation at the **position/weight level**, not at the
return level. Two alphas using the same data field produce similar cross-sectional
rankings (and therefore similar portfolio weights) even when their daily PnL streams
differ due to different wrapper logic (multiplicative vs additive, different decay,
different secondary signals).
