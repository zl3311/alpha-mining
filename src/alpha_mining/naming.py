"""
Structured naming for alpha simulations.

Format: <source>-<timestamp>-<summary>
  - source: origin of the alpha (cursor, periodic, paper, manual, batch)
  - timestamp: YYYYMMDD_HHMM in local time
  - summary: keywords extracted from the expression, joined by _

Examples:
  cursor-20260516_0052-rank_close
  paper-20260516_0930-ts_delta_close_3d
  manual-20260516_0100-correlation_open_volume_10d
"""

from __future__ import annotations

import re
from datetime import datetime

_MAX_SUMMARY_LEN = 40

_WINDOW_OPS = {
    "ts_rank", "ts_delta", "ts_mean", "ts_sum", "ts_std_dev",
    "ts_min", "ts_max", "ts_argmax", "ts_argmin", "ts_decay_linear",
    "ts_product", "ts_skewness", "ts_kurtosis", "ts_covariance",
    "ts_correlation", "ts_regression", "ts_backfill", "delay",
    "correlation", "delta", "decay_linear",
}

_DATA_FIELDS = {
    "open", "high", "low", "close", "volume", "vwap",
    "returns", "adv20", "adv60", "cap",
}


def generate_alpha_name(
    expression: str,
    source: str = "manual",
    *,
    timestamp: datetime | None = None,
) -> str:
    """
    Generate a structured name for an alpha simulation.

    Args:
        expression: BRAIN Fast Expression formula.
        source: Origin tag (cursor, periodic, paper, manual, batch).
        timestamp: Optional override; defaults to now.

    Returns:
        Formatted name like "manual-20260516_0052-rank_close_5d".
    """
    ts = timestamp or datetime.now()
    ts_str = ts.strftime("%Y%m%d_%H%M")
    summary = _summarize_expression(expression)
    return f"{source}-{ts_str}-{summary}"


def _summarize_expression(expression: str) -> str:
    """
    Extract meaningful keywords from a BRAIN expression.

    Pulls operators (prioritizing time-series ops with windows),
    data fields, and numeric window parameters to build a
    compact human-readable summary.
    """
    expr_lower = expression.lower()

    func_calls = re.findall(r"([a-z_]+)\s*\(", expr_lower)

    fields_found = [f for f in _DATA_FIELDS if re.search(rf"\b{f}\b", expr_lower)]

    windows = re.findall(r",\s*(\d+)\s*\)", expr_lower)

    meaningful_ops = []
    other_ops = []
    for func in func_calls:
        if func in _WINDOW_OPS:
            meaningful_ops.append(func)
        elif func not in {"abs", "log", "sign", "sqrt", "min", "max", "pasteurize"}:
            other_ops.append(func)

    parts: list[str] = []

    ops_to_use = meaningful_ops or other_ops
    if ops_to_use:
        seen = set()
        for op in ops_to_use:
            short = _shorten_op(op)
            if short not in seen:
                parts.append(short)
                seen.add(short)
            if len(parts) >= 2:
                break

    seen_fields = set()
    for f in fields_found:
        if f not in seen_fields:
            parts.append(f)
            seen_fields.add(f)
        if len(parts) >= 4:
            break

    if windows:
        primary_window = windows[0]
        parts.append(f"{primary_window}d")

    if not parts:
        parts = ["alpha"]

    summary = "_".join(parts)

    if len(summary) > _MAX_SUMMARY_LEN:
        summary = summary[:_MAX_SUMMARY_LEN].rstrip("_")

    return summary


def _shorten_op(op: str) -> str:
    """Shorten common operator prefixes for readability."""
    if op.startswith("ts_"):
        return op[3:]
    if op.startswith("group_"):
        return op[6:]
    return op
