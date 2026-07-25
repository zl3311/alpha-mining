"""
Tests for the local alpha pre-screener: tokenizer, parser, evaluator, and metrics.

Covers:
- Tokenizer: all token types, edge cases
- Parser: arithmetic, function calls, comparisons, nested expressions
- Evaluator: field resolution, all operator families, error handling
- Screener: IC computation, verdict classification
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from alpha_mining.local.data import MarketData
from alpha_mining.local.evaluator import (
    EvalError,
    FieldNode,
    FuncCallNode,
    NumberNode,
    Token,
    TokenType,
    evaluate_expression,
    parse_expression,
    tokenize,
)

# =====================================================================
# Test data fixtures
# =====================================================================


def _make_market_data(n_stocks: int = 10, n_days: int = 100) -> MarketData:
    """Build a synthetic MarketData for deterministic testing."""
    np.random.seed(42)
    dates = pd.bdate_range("2023-01-01", periods=n_days)
    tickers = [f"STK{i:02d}" for i in range(n_stocks)]

    close = pd.DataFrame(
        100 + np.cumsum(np.random.randn(n_days, n_stocks) * 0.5, axis=0),
        index=dates, columns=tickers,
    )
    open_ = close + np.random.randn(n_days, n_stocks) * 0.3
    high = pd.DataFrame(
        np.maximum(close.values, open_.values) + abs(np.random.randn(n_days, n_stocks) * 0.2),
        index=dates, columns=tickers,
    )
    low = pd.DataFrame(
        np.minimum(close.values, open_.values) - abs(np.random.randn(n_days, n_stocks) * 0.2),
        index=dates, columns=tickers,
    )
    volume = pd.DataFrame(
        abs(np.random.randn(n_days, n_stocks) * 1e6 + 5e6),
        index=dates, columns=tickers,
    )
    returns = close.pct_change()
    vwap = (high + low + close) / 3
    adv20 = volume.rolling(20).mean()
    adv60 = volume.rolling(60).mean()
    cap = close * volume.rolling(20).mean()

    sector_map = {t: f"Sector{i % 3}" for i, t in enumerate(tickers)}
    industry_map = {t: f"Industry{i % 5}" for i, t in enumerate(tickers)}

    return MarketData(
        open=open_, high=high, low=low, close=close, volume=volume,
        returns=returns, vwap=vwap, adv20=adv20, adv60=adv60, cap=cap,
        sector=sector_map, industry=industry_map,
        tickers=tickers, date_range="2023-01-01 to 2023-05-23",
    )


# =====================================================================
# Tokenizer tests
# =====================================================================


class TestTokenizer:
    def test_simple_field(self):
        tokens = tokenize("close")
        assert tokens[0] == Token(TokenType.IDENT, "close")
        assert tokens[1].type == TokenType.EOF

    def test_number(self):
        tokens = tokenize("42.5")
        assert tokens[0] == Token(TokenType.NUMBER, "42.5")

    def test_arithmetic(self):
        tokens = tokenize("a + b * c")
        idents = [t.value for t in tokens if t.type == TokenType.IDENT]
        ops = [t.value for t in tokens if t.type == TokenType.OP]
        assert idents == ["a", "b", "c"]
        assert ops == ["+", "*"]

    def test_comparison_operators(self):
        tokens = tokenize("x > 0.02")
        comparisons = [t for t in tokens if t.type == TokenType.COMPARE]
        assert len(comparisons) == 1
        assert comparisons[0].value == ">"

    def test_all_comparisons(self):
        for op in [">", "<", ">=", "<=", "==", "!="]:
            tokens = tokenize(f"x {op} y")
            assert any(t.value == op and t.type == TokenType.COMPARE for t in tokens)

    def test_parentheses(self):
        tokens = tokenize("(a + b)")
        types = [t.type for t in tokens[:-1]]
        assert TokenType.LPAREN in types
        assert TokenType.RPAREN in types

    def test_function_call(self):
        tokens = tokenize("rank(close)")
        values = [t.value for t in tokens[:-1]]
        assert values == ["rank", "(", "close", ")"]

    def test_comma(self):
        tokens = tokenize("ts_mean(close, 10)")
        assert any(t.type == TokenType.COMMA for t in tokens)

    def test_power_operator(self):
        tokens = tokenize("x ** 2")
        ops = [t for t in tokens if t.type == TokenType.OP]
        assert any(t.value == "**" for t in ops)

    def test_negative_as_unary(self):
        tokens = tokenize("close - 1")
        ops = [t for t in tokens if t.type == TokenType.OP]
        nums = [t for t in tokens if t.type == TokenType.NUMBER]
        assert len(ops) == 1
        assert ops[0].value == "-"
        assert nums[0].value == "1"

    def test_invalid_character(self):
        with pytest.raises(EvalError, match="Unexpected character"):
            tokenize("close @ 5")


# =====================================================================
# Parser tests
# =====================================================================


class TestParser:
    def test_simple_field(self):
        ast = parse_expression("close")
        assert isinstance(ast, FieldNode)
        assert ast.name == "close"

    def test_number(self):
        ast = parse_expression("42")
        assert isinstance(ast, NumberNode)
        assert ast.value == 42.0

    def test_arithmetic(self):
        ast = parse_expression("open / close - 1")
        assert hasattr(ast, "op")
        assert ast.op == "-"

    def test_function_call(self):
        ast = parse_expression("rank(close)")
        assert isinstance(ast, FuncCallNode)
        assert ast.name == "rank"
        assert len(ast.args) == 1

    def test_nested_function(self):
        ast = parse_expression("rank(ts_mean(close, 10))")
        assert isinstance(ast, FuncCallNode)
        assert ast.name == "rank"
        inner = ast.args[0]
        assert isinstance(inner, FuncCallNode)
        assert inner.name == "ts_mean"

    def test_complex_expression(self):
        expr = "trade_when(ts_std_dev(returns,20)>0.02, rank(open/close-1), ts_std_dev(returns,20)<0.01)"
        ast = parse_expression(expr)
        assert isinstance(ast, FuncCallNode)
        assert ast.name == "trade_when"
        assert len(ast.args) == 3

    def test_unary_minus(self):
        ast = parse_expression("-1 * close")
        assert hasattr(ast, "op")
        assert ast.op == "*"

    def test_power(self):
        ast = parse_expression("(high * low) ** 0.5")
        assert hasattr(ast, "op")
        assert ast.op == "**"

    def test_all_exp001_expressions(self):
        """Every expression from Experiment 001 should parse without error."""
        exprs = [
            "rank((-1 * ((1 - (open / close)) ** 1)))",
            "(((high * low) ** 0.5) - vwap)",
            "rank((vwap - close)) / rank((vwap + close))",
            "(-1 * ts_corr(high, rank(volume), 5))",
            "sign(ts_delta(volume,1)) * (-1 * ts_delta(close,1))",
            "rank((open/close-1)*(volume/adv20))",
            "ts_decay_linear(rank(open/close-1), 3)",
            "rank(ts_mean((open/close-1), 3))",
            "trade_when(ts_std_dev(returns,20)>0.02, rank(open/close-1), ts_std_dev(returns,20)<0.01)",
            "rank(((open/close-1)/ts_std_dev(returns,20))*(volume/adv20))",
        ]
        for expr in exprs:
            ast = parse_expression(expr)
            assert ast is not None, f"Failed to parse: {expr}"

    def test_unexpected_token_error(self):
        with pytest.raises(EvalError):
            parse_expression("rank(close) extra")


# =====================================================================
# Evaluator tests
# =====================================================================


class TestEvaluator:
    @pytest.fixture
    def data(self):
        return _make_market_data()

    def test_field_resolution(self, data):
        result = evaluate_expression("close", data)
        assert isinstance(result, pd.DataFrame)
        assert result.shape == data.close.shape
        pd.testing.assert_frame_equal(result, data.close)

    def test_unknown_field_error(self, data):
        with pytest.raises(EvalError, match="Unknown field"):
            evaluate_expression("unknown_field", data)

    def test_arithmetic(self, data):
        result = evaluate_expression("open / close - 1", data)
        expected = data.open / data.close - 1
        pd.testing.assert_frame_equal(result, expected)

    def test_rank(self, data):
        result = evaluate_expression("rank(close)", data)
        assert result.min().min() >= 0
        assert result.max().max() <= 1

    def test_ts_mean(self, data):
        result = evaluate_expression("ts_mean(close, 5)", data)
        expected = data.close.rolling(5, min_periods=2).mean()
        pd.testing.assert_frame_equal(result, expected)

    def test_ts_delta(self, data):
        result = evaluate_expression("ts_delta(close, 1)", data)
        expected = data.close - data.close.shift(1)
        pd.testing.assert_frame_equal(result, expected)

    def test_ts_delay(self, data):
        result = evaluate_expression("ts_delay(close, 1)", data)
        expected = data.close.shift(1)
        pd.testing.assert_frame_equal(result, expected)

    def test_ts_std_dev(self, data):
        result = evaluate_expression("ts_std_dev(returns, 20)", data)
        assert result.shape == data.returns.shape
        assert result.iloc[25:].notna().sum().sum() > 0

    def test_ts_sum(self, data):
        result = evaluate_expression("ts_sum(returns, 5)", data)
        expected = data.returns.rolling(5, min_periods=2).sum()
        pd.testing.assert_frame_equal(result, expected)

    def test_ts_corr(self, data):
        result = evaluate_expression("ts_corr(close, volume, 10)", data)
        assert result.shape == data.close.shape
        assert result.iloc[15:].notna().sum().sum() > 0
        assert result.max().max() <= 1.001
        assert result.min().min() >= -1.001

    def test_ts_decay_linear(self, data):
        result = evaluate_expression("ts_decay_linear(close, 3)", data)
        assert result.shape == data.close.shape

    def test_abs_log_sign_sqrt(self, data):
        for fn in ["abs(returns)", "sign(returns)", "sqrt(abs(close))"]:
            result = evaluate_expression(fn, data)
            assert result.shape == data.close.shape

    def test_comparison(self, data):
        result = evaluate_expression("close > 100", data)
        assert set(result.values.flatten()) <= {0.0, 1.0, np.nan}

    def test_trade_when(self, data):
        result = evaluate_expression(
            "trade_when(ts_std_dev(returns,20) > 0.01, rank(close), ts_std_dev(returns,20) < 0.005)",
            data,
        )
        assert result.shape == data.close.shape
        assert result.isna().sum().sum() > 0

    def test_if_else(self, data):
        result = evaluate_expression("if_else(returns > 0, close, volume)", data)
        assert result.shape == data.close.shape

    def test_group_neutralize(self, data):
        result = evaluate_expression("group_neutralize(close, sector)", data)
        assert result.shape == data.close.shape

    def test_group_rank(self, data):
        result = evaluate_expression("group_rank(close, industry)", data)
        assert result.shape == data.close.shape

    def test_zscore(self, data):
        result = evaluate_expression("zscore(close)", data)
        row_means = result.mean(axis=1)
        assert abs(row_means.dropna().mean()) < 0.1

    def test_scale(self, data):
        result = evaluate_expression("scale(close)", data)
        row_sums = result.abs().sum(axis=1)
        np.testing.assert_allclose(row_sums.dropna().values, 1.0, atol=1e-6)

    def test_complex_exp001_expression(self, data):
        """Full Exp001 winner expression should evaluate without error."""
        result = evaluate_expression(
            "trade_when(ts_std_dev(returns,20)>0.02, rank(open/close-1), ts_std_dev(returns,20)<0.01)",
            data,
        )
        assert isinstance(result, pd.DataFrame)
        assert result.shape == data.close.shape

    def test_unsupported_function_error(self, data):
        with pytest.raises(EvalError, match="Unsupported function"):
            evaluate_expression("weird_func(close)", data)

    def test_power_operator(self, data):
        result = evaluate_expression("(high * low) ** 0.5", data)
        expected = (data.high * data.low) ** 0.5
        pd.testing.assert_frame_equal(result, expected)

    def test_division_by_zero(self, data):
        result = evaluate_expression("close / (close - close)", data)
        assert result.isna().all().all()

    def test_min_max(self, data):
        result = evaluate_expression("min(open, close)", data)
        expected = pd.DataFrame(
            np.minimum(data.open.values, data.close.values),
            index=data.close.index, columns=data.close.columns,
        )
        pd.testing.assert_frame_equal(result, expected)


# =====================================================================
# Screener metric tests
# =====================================================================


class TestScreenerMetrics:
    def test_compute_rank_ic(self):
        from alpha_mining.local.screener import _compute_rank_ic

        np.random.seed(42)
        n_days, n_stocks = 100, 20
        dates = pd.bdate_range("2023-01-01", periods=n_days)
        tickers = [f"S{i}" for i in range(n_stocks)]

        signal = pd.DataFrame(np.random.randn(n_days, n_stocks), index=dates, columns=tickers)
        fwd_returns = signal * 0.01 + np.random.randn(n_days, n_stocks) * 0.02

        ic = _compute_rank_ic(signal, fwd_returns)
        assert len(ic) > 50
        assert abs(ic.mean()) > 0.01

    def test_compute_turnover(self):
        from alpha_mining.local.screener import _compute_turnover

        np.random.seed(42)
        signal = pd.DataFrame(np.random.randn(50, 10))
        turnover = _compute_turnover(signal)
        assert 0 < turnover < 1

    def test_compute_coverage(self):
        from alpha_mining.local.screener import _compute_coverage

        signal = pd.DataFrame(np.ones((10, 5)))
        assert _compute_coverage(signal) == 1.0

        signal.iloc[0, 0] = np.nan
        assert _compute_coverage(signal) < 1.0

    def test_classify_verdicts(self):
        from alpha_mining.local.screener import _classify

        assert _classify(0.02, 1.0) == "PROMISING"
        assert _classify(0.01, 0.5) == "WEAK"
        assert _classify(0.002, 0.1) == "DEAD"
        assert _classify(-0.02, -1.0) == "PROMISING"
        assert _classify(-0.003, -0.1) == "DEAD"

    def test_screen_expression_with_data(self):
        from alpha_mining.local.screener import screen_expression

        data = _make_market_data(n_stocks=20, n_days=200)
        result = screen_expression("rank(close)", data=data)
        assert result.expression == "rank(close)"
        assert result.verdict in ("PROMISING", "WEAK", "DEAD")
        assert 0 <= result.coverage <= 1

    def test_screen_expression_error(self):
        from alpha_mining.local.screener import screen_expression

        data = _make_market_data()
        result = screen_expression("bad_func(close)", data=data)
        assert result.verdict == "ERROR"
        assert result.error != ""

    def test_screen_batch_sorted_by_ic(self):
        from alpha_mining.local.screener import screen_expression

        data = _make_market_data(n_stocks=20, n_days=200)
        exprs = ["rank(close)", "rank(volume)", "rank(returns)"]
        results = [screen_expression(e, data=data) for e in exprs]
        results.sort(key=lambda r: abs(r.rank_ic), reverse=True)
        for i in range(len(results) - 1):
            assert abs(results[i].rank_ic) >= abs(results[i + 1].rank_ic)
