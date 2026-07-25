---
session: "20260618-001"
---

# Learnings: Session 20260618-001

## Confirmed Patterns

### Volatility-Gate Self-Corr Reduction (strengthened)

The `trade_when(ts_std_dev(returns, 20) > 0.02, ..., < 0.01)` gate is now
confirmed as a reliable self-corr reducer across TWO different mechanism
families:

| Alpha | Family | Ungated Corr | Gated Corr | Reduction |
|-------|--------|-------------|------------|-----------|
| 0m7lnAEr | IV+event multi-leg | ~0.61 | 0.548 | -0.06 |
| blL55wRp | capital-intensity+totassets | 0.838 | 0.694 | **-0.14** |

This is the single most valuable lever for breaking the self-corr wall.

### SUBINDUSTRY vs MARKET for Fundamental Blends

MARKET neutralization destroyed the signal for the `fnd6_fate + totassets_flag`
family. Sharpe dropped ~40% (2.10 -> 1.29). This family's alpha is
fundamentally industry-relative — capital intensity and total-assets revision
are meaningful within industries, not across the broad market.

## New Findings

### Capital Intensity + Total-Assets Revision = Novel EXCELLENT Backbone

`fnd6_fate/close + anl4_totassets_flag` is a new viable EXCELLENT backbone that
shares zero raw fields with the binding self-corr peers (`d5Q3ZmWv`,
`0m8GV1Pp`, `LLR0n261`, `vR56vdYd`). The `anl4_totassets_flag` field was not
in any active book entry prior to this session.

### Depreciation/Debt/PP&E Are Too Weak for EXCELLENT

Three alternative fundamental anchors were tested:
- `fnd6_newqv1300_dpactq` (depreciation): capped at AVERAGE S=1.75
- `debt_lt` (long-term debt): capped at AVERAGE S=1.49
- `fnd6_newqv1300_ppegtq` (PP&E): capped at AVERAGE S=1.50

These fields have standalone Sharpe ~0.8-1.0, insufficient to anchor an
EXCELLENT blend. They might still serve as decorrelating stabilizer legs in
other structures, but they cannot be the backbone.

## Dead Zone Updates

No new dead zones recorded. The depreciation/debt/PP&E weakness as backbones
is noted above but they may still have utility as blend legs.

## Opportunity for Future Sessions

The `fnd6_fate + totassets_flag` family with vol gate is now exploited (blL55wRp).
Further mutations of this exact family would likely hit the same self-corr wall
as KPbjjWPx (0.84 ungated). The vol gate is the only viable escape, and it was
found this session. A future session could explore:
- `fnd6_fate + anl4_totassets_flag + <orthogonal 5th leg>` to push self-corr lower
- Different analyst flags with fnd6_fate (but anl4_epsr_flag MARKET was AVERAGE)
