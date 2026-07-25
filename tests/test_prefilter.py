"""
Tests for the pre-filter validation stage.

Covers brute-force combinations of valid and invalid expressions:
- Valid reference alphas (101 alphas)
- Bracket balancing (missing open/close, nested)
- Operator validation (known, unknown, aliases)
- Complexity bounds (depth, length)
- Deduplication (exact, normalized whitespace)
- Edge cases (empty, whitespace-only, special chars)
"""

import pytest

from alpha_mining.pipeline.prefilter import (
    MAX_EXPRESSION_LENGTH_FASTEXPR,
    MAX_OPERATOR_DEPTH,
    validate_expression,
)
from alpha_mining.storage.db import expression_hash

# ---------------------------------------------------------------------------
# Reference alphas from 101 Formulaic Alphas -- all should PASS
# ---------------------------------------------------------------------------

VALID_ALPHAS = [
    "rank(close)",
    "(-1 * ts_delta(close, 3))",
    "(-1 * correlation(rank(open), rank(volume), 10))",
    "(-1 * ts_rank(rank(close), 9))",
    "rank(ts_argmax(close, 30))",
    "(-1 * rank(ts_delta(close, 7)))",
    "(-1 * rank(ts_delta(returns, 3)))",
    "(-1 * ts_delta(close, 1))",
    "(rank((vwap - close)) / rank((vwap + close)))",
    "(-1 * ts_max(ts_delta(vwap, 2), 5))",
    "(-1 * ts_rank(ts_delta(volume, 1), 5))",
    "(-1 * correlation(close, volume, 5))",
    "rank(ts_covariance(rank(close), rank(volume), 5))",
    "(-1 * ts_std_dev(returns, 20))",
    "(-1 * ts_rank(ts_std_dev(close, 10), 10))",
    "rank(close / delay(close, 5))",
    "rank(ts_mean(close, 10) - close)",
    "(-1 * rank(ts_sum(returns, 5)))",
    "ts_decay_linear(ts_delta(close, 3), 8)",
    "(-1 * ts_decay_linear(rank(ts_delta(close, 5)), 10))",
    "(-1 * rank(ts_covariance(rank(close), rank(volume), 10)))",
    "rank(ts_correlation(vwap, volume, 5)) * (-1)",
    "rank(ts_delta(close, 1)) * rank(ts_mean(volume, 20))",
]


@pytest.mark.parametrize("expr", VALID_ALPHAS)
def test_valid_reference_alphas(expr):
    result = validate_expression(expr)
    assert result.passed, f"Expected PASS for '{expr}', got: {result.issues}"


# ---------------------------------------------------------------------------
# Bracket validation
# ---------------------------------------------------------------------------

BRACKET_INVALID = [
    ("rank(close", "missing closing paren"),
    ("rank close)", "missing opening paren"),
    ("((rank(close)", "unbalanced nested"),
    ("rank(close))", "extra closing paren"),
    ("(((", "all open"),
    (")))", "all close"),
]


@pytest.mark.parametrize("expr,desc", BRACKET_INVALID)
def test_bracket_invalid(expr, desc):
    result = validate_expression(expr)
    assert not result.passed, f"Expected FAIL for '{desc}': {expr}"
    assert any("paren" in issue.lower() for issue in result.issues)


BRACKET_VALID = [
    "(rank(close))",
    "((close + open))",
    "rank(ts_delta(ts_mean(close, 5), 1))",
]


@pytest.mark.parametrize("expr", BRACKET_VALID)
def test_bracket_valid(expr):
    result = validate_expression(expr)
    assert result.passed, f"Expected PASS for '{expr}', got: {result.issues}"


# ---------------------------------------------------------------------------
# Operator validation
# ---------------------------------------------------------------------------

UNKNOWN_OPS = [
    "foobar(close)",
    "magic_indicator(volume, 10)",
    "neural_net(close, open)",
    "predict(returns)",
]


@pytest.mark.parametrize("expr", UNKNOWN_OPS)
def test_unknown_operators_fail(expr):
    result = validate_expression(expr)
    assert not result.passed
    assert any("unknown operator" in issue.lower() for issue in result.issues)


KNOWN_ALIASES = [
    "correlation(close, volume, 10)",
    "delta(close, 5)",
    "decay_linear(close, 10)",
]


@pytest.mark.parametrize("expr", KNOWN_ALIASES)
def test_known_aliases_pass(expr):
    result = validate_expression(expr)
    assert result.passed, f"Alias should pass: {expr}, got: {result.issues}"


KNOWN_BUILTINS = [
    "abs(close - open)",
    "log(volume)",
    "sign(returns)",
    "sqrt(abs(close))",
    "max(close, open)",
    "min(close, open)",
]


@pytest.mark.parametrize("expr", KNOWN_BUILTINS)
def test_known_builtins_pass(expr):
    result = validate_expression(expr)
    assert result.passed, f"Builtin should pass: {expr}, got: {result.issues}"


# ---------------------------------------------------------------------------
# Complexity bounds
# ---------------------------------------------------------------------------

def test_expression_too_long():
    expr = "rank(" * 50 + "close" + ")" * 50
    result = validate_expression(expr)
    if len(expr) > MAX_EXPRESSION_LENGTH_FASTEXPR:
        assert not result.passed
        assert any("too long" in issue.lower() for issue in result.issues)


def test_nesting_depth_exceeded():
    depth = MAX_OPERATOR_DEPTH + 2
    expr = "rank(" * depth + "close" + ")" * depth
    result = validate_expression(expr)
    assert not result.passed
    assert any("depth" in issue.lower() for issue in result.issues)


def test_nesting_at_limit():
    expr = "rank(" * MAX_OPERATOR_DEPTH + "close" + ")" * MAX_OPERATOR_DEPTH
    result = validate_expression(expr)
    bracket_issues = [i for i in result.issues if "depth" in i.lower()]
    assert len(bracket_issues) == 0, f"Should not fail at limit: {result.issues}"


# ---------------------------------------------------------------------------
# Empty / whitespace
# ---------------------------------------------------------------------------

EMPTY_INPUTS = [
    "",
    "   ",
    "\n",
    "\t",
]


@pytest.mark.parametrize("expr", EMPTY_INPUTS)
def test_empty_expressions_fail(expr):
    result = validate_expression(expr)
    assert not result.passed


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def test_dedup_exact_match():
    known = {expression_hash("rank(close)")}
    result = validate_expression("rank(close)", known_hashes=known)
    assert not result.passed
    assert any("duplicate" in issue.lower() for issue in result.issues)


def test_dedup_normalized_whitespace():
    known = {expression_hash("rank(close)")}
    result = validate_expression("rank( close )", known_hashes=known)
    assert not result.passed


def test_dedup_different_expression():
    known = {expression_hash("rank(close)")}
    result = validate_expression("rank(volume)", known_hashes=known)
    assert result.passed


def test_dedup_none_hashes_skips_check():
    result = validate_expression("rank(close)", known_hashes=None)
    assert result.passed


# ---------------------------------------------------------------------------
# Multi-language support
# ---------------------------------------------------------------------------


def test_python_skips_operator_check():
    result = validate_expression("foobar(close)", language="PYTHON")
    assert result.passed, f"Python should skip operator validation: {result.issues}"


def test_python_skips_bracket_check():
    result = validate_expression("df['close'].rolling(5).mean(", language="PYTHON")
    assert result.passed, f"Python should skip bracket validation: {result.issues}"


def test_python_skips_depth_check():
    deep = "rank(" * 20 + "close" + ")" * 20
    result = validate_expression(deep, language="PYTHON")
    depth_issues = [i for i in result.issues if "depth" in i.lower()]
    assert len(depth_issues) == 0


def test_python_still_checks_empty():
    result = validate_expression("", language="PYTHON")
    assert not result.passed


def test_python_still_checks_dedup():
    known = {expression_hash("some_code")}
    result = validate_expression("some_code", known_hashes=known, language="PYTHON")
    assert not result.passed


def test_python_longer_length_limit():
    long_code = "x = close\n" * 400  # ~4000 chars, over FASTEXPR limit but under PYTHON limit
    result = validate_expression(long_code, language="PYTHON")
    length_issues = [i for i in result.issues if "too long" in i.lower()]
    assert len(length_issues) == 0


def test_fastexpr_rejects_long():
    long_expr = "rank(" * 60 + "close" + ")" * 60
    result = validate_expression(long_expr, language="FASTEXPR")
    assert not result.passed


def test_expression_language_same_as_fastexpr():
    result = validate_expression("foobar(close)", language="EXPRESSION")
    assert not result.passed  # EXPRESSION uses same validation as FASTEXPR


LANGUAGES = ["FASTEXPR", "PYTHON", "EXPRESSION"]


@pytest.mark.parametrize("lang", LANGUAGES)
def test_valid_alpha_passes_all_languages(lang):
    result = validate_expression("rank(close)", language=lang)
    assert result.passed
