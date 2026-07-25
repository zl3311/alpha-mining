"""
Pre-filter stage: validate expressions before expensive BRAIN simulation.

Performs syntax checking, complexity bounding, and expression deduplication.
Self-correlation gating happens *after* backtest using BRAIN's own check.
"""

from __future__ import annotations

import logging
import re

from ..brain.constants import (
    CROSS_SECTIONAL_OPS,
    DATA_QUALITY_OPS,
    GROUP_OPS,
    LOGICAL_OPS,
    PRICE_VOLUME_FIELDS,
    TIME_SERIES_OPS,
)
from ..storage.db import expression_hash

logger = logging.getLogger(__name__)

_ALL_OPERATORS = set()
for ops_dict in [CROSS_SECTIONAL_OPS, TIME_SERIES_OPS, GROUP_OPS, LOGICAL_OPS, DATA_QUALITY_OPS]:
    for sig in ops_dict:
        func_name = sig.split("(")[0]
        _ALL_OPERATORS.add(func_name)

# Common aliases used in 101 Alphas paper and BRAIN platform
_KNOWN_ALIASES = {
    "correlation", "ts_correlation", "ts_corr",
    "delta", "delay", "ts_delay", "decay_linear", "stddev",
    "sum", "mean", "product", "argmax", "argmin",
    "ts_argmax", "ts_argmin", "ts_arg_max", "ts_arg_min",
    "covariance", "regression", "backfill",
    "pow", "power", "not", "reverse",
    "vec_avg", "vec_sum", "vec_norm",
    "ts_entropy", "ts_decay_exp_window", "ts_moment", "ts_zscore",
}

_ALL_FIELDS = set(PRICE_VOLUME_FIELDS)

MAX_OPERATOR_DEPTH = 8
MAX_EXPRESSION_LENGTH_FASTEXPR = 500
MAX_EXPRESSION_LENGTH_PYTHON = 5000


class PreFilterResult:
    """Result of pre-filter validation."""

    def __init__(self) -> None:
        self.passed = True
        self.issues: list[str] = []

    def fail(self, reason: str) -> None:
        self.passed = False
        self.issues.append(reason)

    def __bool__(self) -> bool:
        return self.passed

    def __repr__(self) -> str:
        if self.passed:
            return "PreFilterResult(PASS)"
        return f"PreFilterResult(FAIL: {', '.join(self.issues)})"


def validate_expression(
    expression: str,
    known_hashes: set[str] | None = None,
    language: str = "FASTEXPR",
) -> PreFilterResult:
    """
    Run pre-filter checks on an expression. Language-aware:
    - FASTEXPR: full syntax validation (brackets, operators, depth)
    - PYTHON: basic checks only (length, dedup) -- arbitrary code is valid
    - EXPRESSION: same as FASTEXPR
    """
    result = PreFilterResult()

    if not expression or not expression.strip():
        result.fail("Empty expression")
        return result

    expr = expression.strip()

    _check_length(expr, result, language)
    _check_deduplication(expr, known_hashes, result)

    if language in ("FASTEXPR", "EXPRESSION"):
        _check_brackets(expr, result)
        _check_operators(expr, result)
        _check_depth(expr, result)

    if result.passed:
        logger.debug("Pre-filter PASS: %s", expr[:60])
    else:
        logger.info("Pre-filter FAIL: %s -- %s", expr[:60], result.issues)

    return result


def _check_length(expr: str, result: PreFilterResult, language: str = "FASTEXPR") -> None:
    limit = MAX_EXPRESSION_LENGTH_PYTHON if language == "PYTHON" else MAX_EXPRESSION_LENGTH_FASTEXPR
    if len(expr) > limit:
        result.fail(f"Expression too long ({len(expr)} > {limit})")


def _check_brackets(expr: str, result: PreFilterResult) -> None:
    depth = 0
    for ch in expr:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if depth < 0:
            result.fail("Unmatched closing parenthesis")
            return
    if depth != 0:
        result.fail(f"Unbalanced parentheses (depth={depth})")


def _check_operators(expr: str, result: PreFilterResult) -> None:
    """Warn (but don't fail) if expression uses unknown function names."""
    func_calls = re.findall(r"([a-z_]+)\s*\(", expr.lower())
    builtin_funcs = {"abs", "log", "sign", "sqrt", "min", "max", "signed_power", "pasteurize", "if_else", "trade_when"}
    for func in func_calls:
        if func not in _ALL_OPERATORS and func not in builtin_funcs and func not in _KNOWN_ALIASES:
            result.fail(f"Unknown operator: {func}")


def _check_depth(expr: str, result: PreFilterResult) -> None:
    max_depth = 0
    depth = 0
    for ch in expr:
        if ch == "(":
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == ")":
            depth -= 1
    if max_depth > MAX_OPERATOR_DEPTH:
        result.fail(f"Nesting depth too high ({max_depth} > {MAX_OPERATOR_DEPTH})")


def _check_deduplication(
    expr: str, known_hashes: set[str] | None, result: PreFilterResult
) -> None:
    if known_hashes is None:
        return
    h = expression_hash(expr)
    if h in known_hashes:
        result.fail("Duplicate expression (already in database)")
