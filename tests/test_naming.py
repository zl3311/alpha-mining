"""
Tests for the naming module.

Covers brute-force combinations of:
- Various expression patterns (simple, complex, nested, multi-field)
- All source types (cursor, periodic, paper, manual, batch)
- Timestamp formatting
- Manual name override
- Summary truncation for long expressions
- Edge cases (empty, whitespace, no operators, no fields)
"""

import re
from datetime import datetime

import pytest

from alpha_mining.naming import _summarize_expression, generate_alpha_name

# ---------------------------------------------------------------------------
# Format: <source>-<timestamp>-<summary>
# ---------------------------------------------------------------------------

_NAME_PATTERN = re.compile(r"^[a-z]+-\d{8}_\d{4}-.+$")


def test_name_format_basic():
    name = generate_alpha_name("rank(close)", "manual")
    assert _NAME_PATTERN.match(name), f"Name doesn't match format: {name}"


SOURCES = ["cursor", "periodic", "paper", "manual", "batch"]


@pytest.mark.parametrize("source", SOURCES)
def test_source_prefix(source):
    name = generate_alpha_name("rank(close)", source)
    assert name.startswith(f"{source}-")


def test_timestamp_format():
    ts = datetime(2026, 5, 16, 0, 52)
    name = generate_alpha_name("rank(close)", "manual", timestamp=ts)
    assert "20260516_0052" in name


def test_timestamp_default_is_now():
    name = generate_alpha_name("rank(close)", "manual")
    today = datetime.now().strftime("%Y%m%d")
    assert today in name


# ---------------------------------------------------------------------------
# Summary extraction from various expressions
# ---------------------------------------------------------------------------

EXPRESSION_SUMMARY_CASES = [
    ("rank(close)", ["rank", "close"]),
    ("(-1 * ts_delta(close, 3))", ["delta", "close"]),
    ("(-1 * correlation(rank(open), rank(volume), 10))", ["correlation", "open"]),
    ("ts_decay_linear(ts_delta(close, 3), 8)", ["decay_linear", "delta"]),
    ("rank(ts_argmax(close, 30))", ["argmax", "close"]),
    ("(-1 * ts_std_dev(returns, 20))", ["std_dev", "returns"]),
    ("(rank((vwap - close)) / rank((vwap + close)))", ["rank", "vwap"]),
    ("ts_correlation(vwap, volume, 5)", ["correlation", "vwap"]),
    ("rank(ts_delta(close, 1)) * rank(ts_mean(volume, 20))", ["delta", "mean"]),
]


@pytest.mark.parametrize("expr,expected_keywords", EXPRESSION_SUMMARY_CASES)
def test_summary_contains_keywords(expr, expected_keywords):
    summary = _summarize_expression(expr)
    for kw in expected_keywords:
        assert kw in summary, f"Expected '{kw}' in summary '{summary}' for expr '{expr}'"


def test_summary_includes_window():
    summary = _summarize_expression("ts_delta(close, 5)")
    assert "5d" in summary


def test_summary_multiple_fields():
    summary = _summarize_expression("ts_correlation(close, volume, 10)")
    assert "close" in summary or "volume" in summary


# ---------------------------------------------------------------------------
# Full name generation from reference alphas
# ---------------------------------------------------------------------------

REFERENCE_ALPHAS = [
    "rank(close)",
    "(-1 * ts_delta(close, 3))",
    "(-1 * correlation(rank(open), rank(volume), 10))",
    "(-1 * ts_rank(rank(close), 9))",
    "rank(ts_argmax(close, 30))",
    "(rank((vwap - close)) / rank((vwap + close)))",
    "(-1 * ts_max(ts_delta(vwap, 2), 5))",
    "(-1 * correlation(close, volume, 5))",
    "(-1 * ts_std_dev(returns, 20))",
    "ts_decay_linear(ts_delta(close, 3), 8)",
    "rank(ts_correlation(vwap, volume, 5)) * (-1)",
]


@pytest.mark.parametrize("expr", REFERENCE_ALPHAS)
def test_reference_alphas_produce_valid_names(expr):
    name = generate_alpha_name(expr, "cursor")
    assert _NAME_PATTERN.match(name), f"Invalid name: {name}"
    parts = name.split("-", 2)
    assert len(parts) == 3
    assert parts[0] == "cursor"
    assert len(parts[2]) > 0  # summary is non-empty


@pytest.mark.parametrize("source", SOURCES)
@pytest.mark.parametrize("expr", REFERENCE_ALPHAS[:3])
def test_source_x_expression_combinations(source, expr):
    name = generate_alpha_name(expr, source)
    assert name.startswith(f"{source}-")
    assert _NAME_PATTERN.match(name)


# ---------------------------------------------------------------------------
# Manual name override (orchestrator level, but test the contract)
# ---------------------------------------------------------------------------

def test_manual_override_replaces_auto():
    auto_name = generate_alpha_name("rank(close)", "manual")
    assert "rank" in auto_name
    manual_name = "my_custom_alpha_name"
    # The orchestrator uses: name or generate_alpha_name(...)
    effective = manual_name or auto_name
    assert effective == manual_name


# ---------------------------------------------------------------------------
# Summary truncation
# ---------------------------------------------------------------------------

def test_summary_truncation():
    long_expr = "ts_correlation(ts_decay_linear(ts_delta(ts_mean(close, 5), 3), 8), ts_std_dev(volume, 20), 10)"
    summary = _summarize_expression(long_expr)
    assert len(summary) <= 40


def test_no_trailing_underscore_after_truncation():
    long_expr = "ts_correlation(ts_decay_linear(ts_delta(ts_mean(close, 5), 3), 8), ts_std_dev(volume, 20), 10)"
    summary = _summarize_expression(long_expr)
    assert not summary.endswith("_")


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------

def test_empty_expression():
    name = generate_alpha_name("", "manual")
    assert _NAME_PATTERN.match(name)
    assert "alpha" in name  # fallback summary


def test_whitespace_expression():
    name = generate_alpha_name("   ", "manual")
    assert _NAME_PATTERN.match(name)


def test_pure_arithmetic():
    name = generate_alpha_name("close - open", "manual")
    assert _NAME_PATTERN.match(name)
    summary = name.split("-", 2)[2]
    assert "close" in summary or "open" in summary


def test_no_operators_only_fields():
    summary = _summarize_expression("close * volume")
    assert "close" in summary or "volume" in summary


def test_deeply_nested():
    expr = "rank(rank(rank(rank(close))))"
    name = generate_alpha_name(expr, "cursor")
    assert _NAME_PATTERN.match(name)
