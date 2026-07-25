"""
Local alpha pre-screening: evaluate FASTEXPR expressions on yfinance data
to filter out dead signals before spending BRAIN simulation budget.

Public API:
    screen_expression(expr, region, universe) -> ScreenResult
    screen_batch(exprs, region, universe)     -> list[ScreenResult]
"""

from __future__ import annotations

from .screener import ScreenResult, screen_batch, screen_expression

__all__ = ["ScreenResult", "screen_batch", "screen_expression"]
