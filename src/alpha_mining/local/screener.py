"""
Alpha signal screener: compute rank IC and related metrics on locally
evaluated signals to determine whether an expression is worth submitting
to BRAIN for official backtesting.

Metrics:
    - Rank IC: Spearman correlation between signal rank and next-day returns
    - IC IR: mean(IC) / std(IC) -- signal consistency, reported but not gated on
    - Estimated turnover: mean absolute daily change in cross-sectional rank
    - Coverage: fraction of stocks with non-NaN signal values

Verdict thresholds (calibrated against Exp001/002 results). The verdict depends on
|rank IC| alone; IC IR is computed and returned for inspection but does not affect
classification:
    - PROMISING: |IC| > 0.015 -- worth submitting to BRAIN
    - WEAK: 0.005 < |IC| <= 0.015 -- iterate locally first
    - DEAD: |IC| <= 0.005 -- skip entirely

Scope limit: this screener runs on locally downloaded price-volume data only (see
`data.py` for the field list). Expressions referencing BRAIN fundamental or analyst
fields cannot be screened here and must go straight to BRAIN.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

import numpy as np
import pandas as pd

from .data import MarketData, load_market_data
from .evaluator import EvalError, evaluate_expression

logger = logging.getLogger(__name__)


@dataclass
class ScreenResult:
    """Result of local alpha pre-screening."""

    expression: str
    rank_ic: float
    ic_ir: float
    est_turnover: float
    coverage: float
    verdict: str
    ic_series: pd.Series | None = None
    error: str = ""

    @property
    def is_promising(self) -> bool:
        return self.verdict == "PROMISING"

    def summary_line(self) -> str:
        if self.error:
            return f"ERROR: {self.error}"
        return (
            f"Rank IC: {self.rank_ic:+.4f} | "
            f"IC IR: {self.ic_ir:.2f} | "
            f"Turnover: {self.est_turnover:.1%} | "
            f"Coverage: {self.coverage:.0%} | "
            f"Verdict: {self.verdict}"
        )


def _compute_rank_ic(signal: pd.DataFrame, forward_returns: pd.DataFrame) -> pd.Series:
    """
    Compute daily rank IC: Spearman correlation between cross-sectional
    signal rank and next-day returns across the universe.
    """
    ic_values = []
    dates = signal.index.intersection(forward_returns.index)

    for date in dates:
        sig_row = signal.loc[date].dropna()
        ret_row = forward_returns.loc[date].reindex(sig_row.index).dropna()
        common = sig_row.index.intersection(ret_row.index)
        if len(common) < 10:
            continue
        ic = sig_row[common].rank().corr(ret_row[common].rank())
        if not np.isnan(ic):
            ic_values.append((date, ic))

    if not ic_values:
        return pd.Series(dtype=float)
    return pd.Series(dict(ic_values))


def _compute_turnover(signal: pd.DataFrame) -> float:
    """Estimate daily turnover as mean absolute change in cross-sectional rank."""
    ranked = signal.rank(axis=1, pct=True)
    daily_change = ranked.diff().abs().mean(axis=1)
    return float(daily_change.mean()) if not daily_change.empty else 0.0


def _compute_coverage(signal: pd.DataFrame) -> float:
    """Fraction of (date, stock) entries that are non-NaN."""
    total = signal.size
    if total == 0:
        return 0.0
    return float(signal.notna().sum().sum() / total)


def _classify(rank_ic: float, ic_ir: float) -> str:
    """
    Assign a verdict from IC magnitude.

    `ic_ir` is accepted so callers can pass the full metric set and so a consistency
    term can be added later, but the current thresholds key off |rank_ic| only.
    """
    abs_ic = abs(rank_ic)
    if abs_ic > 0.015:
        return "PROMISING"
    elif abs_ic > 0.005:
        return "WEAK"
    else:
        return "DEAD"


def screen_expression(
    expression: str,
    region: str = "us",
    universe: int = 200,
    data: MarketData | None = None,
    refresh: bool = False,
) -> ScreenResult:
    """
    Screen a single FASTEXPR expression locally.

    Args:
        expression: FASTEXPR formula to evaluate.
        region: Market region for data download.
        universe: Number of stocks in the local universe.
        data: Pre-loaded MarketData (avoids re-downloading).
        refresh: Force data refresh.

    Returns:
        ScreenResult with IC metrics and verdict.
    """
    if data is None:
        data = load_market_data(region=region, universe=universe, refresh=refresh)

    try:
        signal = evaluate_expression(expression, data)
    except EvalError as e:
        return ScreenResult(
            expression=expression, rank_ic=0.0, ic_ir=0.0,
            est_turnover=0.0, coverage=0.0, verdict="ERROR", error=str(e),
        )

    forward_returns = data.returns.shift(-1)

    ic_series = _compute_rank_ic(signal, forward_returns)

    if ic_series.empty:
        return ScreenResult(
            expression=expression, rank_ic=0.0, ic_ir=0.0,
            est_turnover=0.0, coverage=0.0, verdict="DEAD",
            error="No valid IC observations",
        )

    rank_ic = float(ic_series.mean())
    ic_std = float(ic_series.std())
    ic_ir = rank_ic / ic_std if ic_std > 0 else 0.0
    est_turnover = _compute_turnover(signal)
    coverage = _compute_coverage(signal)
    verdict = _classify(rank_ic, ic_ir)

    return ScreenResult(
        expression=expression,
        rank_ic=rank_ic,
        ic_ir=ic_ir,
        est_turnover=est_turnover,
        coverage=coverage,
        verdict=verdict,
        ic_series=ic_series,
    )


def screen_batch(
    expressions: list[str],
    region: str = "us",
    universe: int = 200,
    refresh: bool = False,
) -> list[ScreenResult]:
    """
    Screen multiple expressions, sharing data download across all.
    Returns results sorted by absolute rank IC (best first).
    """
    data = load_market_data(region=region, universe=universe, refresh=refresh)
    results = [screen_expression(expr, data=data) for expr in expressions]
    results.sort(key=lambda r: abs(r.rank_ic), reverse=True)
    return results
