---
id: "20260701-001-learnings"
session: "20260701-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260701-001

## What Worked

- **PP&E gross (fnd6_newqv1300_ppegtq)** as a novel anchor field — produces SPECTACULAR in 4-factor blends with analyst revision + fundamental + overnight gap
- **Decay=8 platform setting** increases Sharpe from 2.75 (decay=6) to 2.84 by reducing turnover without significantly hurting signal strength
- **Sharpe premium escape** is a viable path when correlation is just above 0.7 — ZYpVLGZj passes at 0.7943 corr because S=2.84 >= 1.10×2.58
- **Systematic field replacement** to decorrelate: removing itci dropped corr vs MPbgqZ7o from 0.778 to 0.675

## What Didn't Work

- **IV mean skew (option8)** as primary anchor — max GOOD grade (S=1.48-2.25). The skew measures vol surface shape but doesn't predict returns well enough alone for EXCELLENT+
- **Sales estimate count** — reaches EXCELLENT S=2.10-2.32 but structurally fails LOW_SUB_UNIVERSE_SHARPE (coverage is uneven across sub-industries)
- **Novel analyst4 fields (afv4_dts_spe, tbvps_high, fcf_high, afv4_eps_number)** as blend legs — all stay GOOD when combined with PP&E. These fields have insufficient standalone signal
- **Zero-overlap strategy** for self-corr: using ONLY novel fields in all 4 legs avoids the itci/drlt/bvps correlation problem but produces GOOD-tier results (S=1.48-1.76), not EXCELLENT+
- **Replacing itci with drlt** created a NEW blocker: 0.796 vs 3q7JQK16 (which uses drlt+bvps+gap). Field substitution can swap one blocker for another

## New Patterns

- **Decay=8 as Sharpe multiplier**: For capital-intensive value blends, decay=8 meaningfully boosts Sharpe (2.75→2.84) by reducing turnover without killing signal. This is a useful lever when a candidate is near but below a premium escape threshold.

## Mechanism Insights

- **PP&E gross / price** captures replacement-cost value: firms where physical asset value (property, plant, equipment) exceeds market cap are undervalued. This is conceptually similar to book value but uses the gross (pre-depreciation) figure, capturing total capital committed rather than net book value.

- **The PP&E signal decorrelates from depreciation (dpactq) and deferred R&D (drc)** in PnL space because it captures asset LEVEL while dpactq captures depreciation FLOW and drc captures R&D capitalization. Despite being from the same fundamental6 dataset, they pick up different economic mechanisms.

- **The self-corr wall is driven by analyst+fundamental blend patterns**, not individual fields. Any 3-4 factor blend using analyst revision + fundamental value + overnight gap will correlate at 0.65-0.80 with existing book entries regardless of the specific fields chosen. The only escape is the Sharpe premium.
