---
category: "reference"
last_verified: "2026-05-28"
---

# Platform Constraints

## Free Tier Limitations

- **Regions**: USA only. EUR, ASI, JPN, CHN, KOR, GLB return 'Region not available'.
- **Language**: FASTEXPR only. PYTHON likely requires consultant tier.
- **Concurrent sims**: 3 slots.
- **Daily budget**: 5,000 simulations.

## Available Universes

TOP200, TOP500, TOP1000, TOP3000 (default).

## Available Neutralizations

SUBINDUSTRY (default), INDUSTRY, MARKET.

## Submission Checks (8 total)

| Check | Limit |
|-------|-------|
| LOW_SHARPE | min 1.25 |
| LOW_FITNESS | min 1.0 |
| LOW_TURNOVER | min 0.01 |
| HIGH_TURNOVER | max 0.70 |
| CONCENTRATED_WEIGHT | max 0.10 |
| LOW_SUB_UNIVERSE_SHARPE | ~43% of overall Sharpe |
| SELF_CORRELATION | 0.7 threshold + 1.10x Sharpe premium escape |
| MATCHES_COMPETITION | must pass |

