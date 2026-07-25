"""
FASTEXPR evaluator: parse and evaluate BRAIN Fast Expression language
on local pandas DataFrames for alpha pre-screening.

Architecture:
    1. Tokenizer: expression string -> token stream
    2. Parser: token stream -> AST (recursive descent)
    3. Evaluator: AST + MarketData -> signal DataFrame (stocks x dates)

Supports ~25 core operators covering 95%+ of typical alpha expressions.
Unsupported operators raise EvalError with a descriptive message.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum, auto
from typing import TYPE_CHECKING

import numpy as np
import pandas as pd

if TYPE_CHECKING:
    from .data import MarketData


class EvalError(Exception):
    """Raised when expression evaluation fails."""


# =====================================================================
# Tokenizer
# =====================================================================

class TokenType(Enum):
    NUMBER = auto()
    IDENT = auto()
    LPAREN = auto()
    RPAREN = auto()
    COMMA = auto()
    OP = auto()
    COMPARE = auto()
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: str

    def __repr__(self) -> str:
        return f"Token({self.type.name}, {self.value!r})"


_TOKEN_PATTERN = re.compile(
    r"""
    (?P<number>\d+\.?\d*(?:e[+-]?\d+)?)     |
    (?P<compare>==|!=|>=|<=|>|<)             |
    (?P<op>\*\*|[+\-*/])                     |
    (?P<ident>[a-zA-Z_][a-zA-Z0-9_]*)       |
    (?P<lparen>\()                            |
    (?P<rparen>\))                            |
    (?P<comma>,)                              |
    (?P<ws>\s+)
    """,
    re.VERBOSE,
)


def tokenize(expr: str) -> list[Token]:
    """Convert expression string to a list of tokens."""
    tokens = []
    pos = 0
    while pos < len(expr):
        m = _TOKEN_PATTERN.match(expr, pos)
        if not m:
            raise EvalError(f"Unexpected character at position {pos}: {expr[pos:][:20]!r}")
        pos = m.end()
        if m.group("ws"):
            continue
        if m.group("number") is not None:
            tokens.append(Token(TokenType.NUMBER, m.group("number")))
        elif m.group("compare"):
            tokens.append(Token(TokenType.COMPARE, m.group("compare")))
        elif m.group("op"):
            tokens.append(Token(TokenType.OP, m.group("op")))
        elif m.group("ident"):
            tokens.append(Token(TokenType.IDENT, m.group("ident")))
        elif m.group("lparen"):
            tokens.append(Token(TokenType.LPAREN, "("))
        elif m.group("rparen"):
            tokens.append(Token(TokenType.RPAREN, ")"))
        elif m.group("comma"):
            tokens.append(Token(TokenType.COMMA, ","))
    tokens.append(Token(TokenType.EOF, ""))
    return tokens


# =====================================================================
# AST nodes
# =====================================================================

@dataclass
class NumberNode:
    value: float

@dataclass
class FieldNode:
    name: str

@dataclass
class BinOpNode:
    op: str
    left: object
    right: object

@dataclass
class UnaryMinusNode:
    operand: object

@dataclass
class CompareNode:
    op: str
    left: object
    right: object

@dataclass
class FuncCallNode:
    name: str
    args: list


# =====================================================================
# Parser (recursive descent)
# =====================================================================

class Parser:
    """Parse FASTEXPR token stream into an AST."""

    def __init__(self, tokens: list[Token]) -> None:
        self._tokens = tokens
        self._pos = 0

    def _peek(self) -> Token:
        return self._tokens[self._pos]

    def _advance(self) -> Token:
        tok = self._tokens[self._pos]
        self._pos += 1
        return tok

    def _expect(self, ttype: TokenType) -> Token:
        tok = self._advance()
        if tok.type != ttype:
            raise EvalError(f"Expected {ttype.name}, got {tok}")
        return tok

    def parse(self) -> object:
        node = self._expr()
        if self._peek().type != TokenType.EOF:
            raise EvalError(f"Unexpected token after expression: {self._peek()}")
        return node

    def _expr(self) -> object:
        return self._comparison()

    def _comparison(self) -> object:
        left = self._additive()
        while self._peek().type == TokenType.COMPARE:
            op = self._advance().value
            right = self._additive()
            left = CompareNode(op, left, right)
        return left

    def _additive(self) -> object:
        left = self._multiplicative()
        while self._peek().type == TokenType.OP and self._peek().value in "+-":
            op = self._advance().value
            right = self._multiplicative()
            left = BinOpNode(op, left, right)
        return left

    def _multiplicative(self) -> object:
        left = self._power()
        while self._peek().type == TokenType.OP and self._peek().value in "*/":
            op = self._advance().value
            right = self._power()
            left = BinOpNode(op, left, right)
        return left

    def _power(self) -> object:
        base = self._unary()
        if self._peek().type == TokenType.OP and self._peek().value == "**":
            self._advance()
            exp = self._unary()
            return BinOpNode("**", base, exp)
        return base

    def _unary(self) -> object:
        if self._peek().type == TokenType.OP and self._peek().value == "-":
            self._advance()
            operand = self._unary()
            return UnaryMinusNode(operand)
        return self._primary()

    def _primary(self) -> object:
        tok = self._peek()

        if tok.type == TokenType.NUMBER:
            self._advance()
            return NumberNode(float(tok.value))

        if tok.type == TokenType.LPAREN:
            self._advance()
            node = self._expr()
            self._expect(TokenType.RPAREN)
            return node

        if tok.type == TokenType.IDENT:
            self._advance()
            if self._peek().type == TokenType.LPAREN:
                self._advance()
                args = []
                if self._peek().type != TokenType.RPAREN:
                    args.append(self._expr())
                    while self._peek().type == TokenType.COMMA:
                        self._advance()
                        args.append(self._expr())
                self._expect(TokenType.RPAREN)
                return FuncCallNode(tok.value, args)
            return FieldNode(tok.value)

        raise EvalError(f"Unexpected token: {tok}")


def parse_expression(expr: str) -> object:
    """Parse a FASTEXPR string into an AST."""
    tokens = tokenize(expr)
    return Parser(tokens).parse()


# =====================================================================
# Evaluator
# =====================================================================

_FIELD_NAMES = {"open", "high", "low", "close", "volume", "vwap", "returns", "adv20", "adv60", "cap"}


def _to_df(val, ref_df: pd.DataFrame) -> pd.DataFrame:
    """Coerce a scalar or Series to a DataFrame matching ref_df shape."""
    if isinstance(val, pd.DataFrame):
        return val
    if isinstance(val, (int, float, np.integer, np.floating)):
        return pd.DataFrame(val, index=ref_df.index, columns=ref_df.columns)
    return val


class Evaluator:
    """Evaluate a FASTEXPR AST on MarketData, producing a signal DataFrame."""

    def __init__(self, data: MarketData) -> None:
        self._data = data
        self._ref = data.close

    def evaluate(self, node: object) -> pd.DataFrame:
        if isinstance(node, NumberNode):
            return pd.DataFrame(node.value, index=self._ref.index, columns=self._ref.columns)

        if isinstance(node, FieldNode):
            return self._resolve_field(node.name)

        if isinstance(node, UnaryMinusNode):
            return -self.evaluate(node.operand)

        if isinstance(node, BinOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            return self._binop(node.op, _to_df(left, self._ref), _to_df(right, self._ref))

        if isinstance(node, CompareNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            return self._compare(node.op, _to_df(left, self._ref), _to_df(right, self._ref))

        if isinstance(node, FuncCallNode):
            return self._call_func(node.name, node.args)

        raise EvalError(f"Unknown AST node: {type(node)}")

    def _resolve_field(self, name: str) -> pd.DataFrame:
        if name in _FIELD_NAMES and hasattr(self._data, name):
            return getattr(self._data, name).copy()
        raise EvalError(f"Unknown field: {name!r}. Available: {sorted(_FIELD_NAMES)}")

    def _binop(self, op: str, left: pd.DataFrame, right: pd.DataFrame) -> pd.DataFrame:
        ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
               "*": lambda a, b: a * b, "/": lambda a, b: a / b.replace(0, np.nan),
               "**": lambda a, b: a ** b}
        if op not in ops:
            raise EvalError(f"Unknown operator: {op}")
        return ops[op](left, right)

    def _compare(self, op: str, left: pd.DataFrame, right: pd.DataFrame) -> pd.DataFrame:
        ops = {">": lambda a, b: a > b, "<": lambda a, b: a < b,
               ">=": lambda a, b: a >= b, "<=": lambda a, b: a <= b,
               "==": lambda a, b: a == b, "!=": lambda a, b: a != b}
        if op not in ops:
            raise EvalError(f"Unknown comparison: {op}")
        return ops[op](left, right).astype(float)

    def _call_func(self, name: str, arg_nodes: list) -> pd.DataFrame:
        dispatch = {
            "rank": self._fn_rank, "zscore": self._fn_zscore,
            "abs": self._fn_abs, "log": self._fn_log,
            "sign": self._fn_sign, "sqrt": self._fn_sqrt,
            "min": self._fn_min, "max": self._fn_max,
            "signed_power": self._fn_signed_power,
            "ts_mean": self._fn_ts_mean, "ts_sum": self._fn_ts_sum,
            "ts_std_dev": self._fn_ts_std_dev, "ts_delta": self._fn_ts_delta,
            "ts_delay": self._fn_ts_delay, "ts_rank": self._fn_ts_rank,
            "ts_min": self._fn_ts_min, "ts_max": self._fn_ts_max,
            "ts_arg_max": self._fn_ts_arg_max, "ts_arg_min": self._fn_ts_arg_min,
            "ts_decay_linear": self._fn_ts_decay_linear,
            "ts_corr": self._fn_ts_corr, "ts_covariance": self._fn_ts_covariance,
            "ts_zscore": self._fn_ts_zscore, "ts_product": self._fn_ts_product,
            "ts_backfill": self._fn_ts_backfill,
            "group_neutralize": self._fn_group_neutralize,
            "group_rank": self._fn_group_rank,
            "trade_when": self._fn_trade_when,
            "if_else": self._fn_if_else,
            "reverse": self._fn_reverse, "scale": self._fn_scale,
            "normalize": self._fn_normalize,
        }
        if name not in dispatch:
            raise EvalError(
                f"Unsupported function: {name!r}. Supported: {sorted(dispatch.keys())}"
            )
        return dispatch[name](arg_nodes)

    def _eval_args(self, arg_nodes: list, count: int | None = None) -> list[pd.DataFrame]:
        args = [self.evaluate(n) for n in arg_nodes]
        if count is not None and len(args) != count:
            raise EvalError(f"Expected {count} args, got {len(args)}")
        return args

    def _get_int_arg(self, node) -> int:
        if isinstance(node, NumberNode):
            return int(node.value)
        raise EvalError(f"Expected integer argument, got {type(node).__name__}")

    def _get_str_arg(self, node) -> str:
        if isinstance(node, FieldNode):
            return node.name
        raise EvalError(f"Expected string argument, got {type(node).__name__}")

    # --- Cross-sectional ---
    def _fn_rank(self, args):
        (x,) = self._eval_args(args, 1)
        return x.rank(axis=1, pct=True)

    def _fn_zscore(self, args):
        (x,) = self._eval_args(args, 1)
        mu = x.mean(axis=1)
        sigma = x.std(axis=1)
        return x.sub(mu, axis=0).div(sigma.replace(0, np.nan), axis=0)

    def _fn_reverse(self, args):
        (x,) = self._eval_args(args, 1)
        return -x.rank(axis=1, pct=True)

    def _fn_scale(self, args):
        (x,) = self._eval_args(args, 1)
        return x.div(x.abs().sum(axis=1).replace(0, np.nan), axis=0)

    def _fn_normalize(self, args):
        (x,) = self._eval_args(args, 1)
        return self._fn_zscore(args)

    # --- Arithmetic ---
    def _fn_abs(self, args):
        (x,) = self._eval_args(args, 1)
        return x.abs()

    def _fn_log(self, args):
        (x,) = self._eval_args(args, 1)
        return np.log(x.clip(lower=1e-10))

    def _fn_sign(self, args):
        (x,) = self._eval_args(args, 1)
        return np.sign(x)

    def _fn_sqrt(self, args):
        (x,) = self._eval_args(args, 1)
        return np.sqrt(x.clip(lower=0))

    def _fn_min(self, args):
        a, b = self._eval_args(args, 2)
        return pd.DataFrame(np.minimum(a.values, b.values), index=a.index, columns=a.columns)

    def _fn_max(self, args):
        a, b = self._eval_args(args, 2)
        return pd.DataFrame(np.maximum(a.values, b.values), index=a.index, columns=a.columns)

    def _fn_signed_power(self, args):
        x, e = self._eval_args(args, 2)
        return np.sign(x) * (x.abs() ** e)

    # --- Time-series ---
    def _fn_ts_mean(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.rolling(d, min_periods=max(1, d // 2)).mean()

    def _fn_ts_sum(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.rolling(d, min_periods=max(1, d // 2)).sum()

    def _fn_ts_std_dev(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.rolling(d, min_periods=max(1, d // 2)).std()

    def _fn_ts_delta(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x - x.shift(d)

    def _fn_ts_delay(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.shift(d)

    def _fn_ts_rank(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.rolling(d, min_periods=max(1, d // 2)).apply(
            lambda s: pd.Series(s).rank(pct=True).iloc[-1], raw=False
        )

    def _fn_ts_min(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.rolling(d, min_periods=max(1, d // 2)).min()

    def _fn_ts_max(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.rolling(d, min_periods=max(1, d // 2)).max()

    def _fn_ts_arg_max(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.rolling(d, min_periods=max(1, d // 2)).apply(
            lambda s: np.argmax(s), raw=True
        )

    def _fn_ts_arg_min(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.rolling(d, min_periods=max(1, d // 2)).apply(
            lambda s: np.argmin(s), raw=True
        )

    def _fn_ts_decay_linear(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        weights = np.arange(1, d + 1, dtype=float)
        weights /= weights.sum()
        return x.rolling(d, min_periods=max(1, d // 2)).apply(
            lambda s: np.dot(s[-len(weights):], weights[-len(s):]) if len(s) >= 1 else np.nan,
            raw=True,
        )

    def _fn_ts_corr(self, args):
        x = self.evaluate(args[0])
        y = self.evaluate(args[1])
        d = self._get_int_arg(args[2])
        return x.rolling(d, min_periods=max(1, d // 2)).corr(y)

    def _fn_ts_covariance(self, args):
        x = self.evaluate(args[0])
        y = self.evaluate(args[1])
        d = self._get_int_arg(args[2])
        return x.rolling(d, min_periods=max(1, d // 2)).cov(y)

    def _fn_ts_zscore(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        mu = x.rolling(d, min_periods=max(1, d // 2)).mean()
        sigma = x.rolling(d, min_periods=max(1, d // 2)).std()
        return (x - mu) / sigma.replace(0, np.nan)

    def _fn_ts_product(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.rolling(d, min_periods=max(1, d // 2)).apply(np.prod, raw=True)

    def _fn_ts_backfill(self, args):
        x = self.evaluate(args[0])
        d = self._get_int_arg(args[1])
        return x.ffill(limit=d)

    # --- Group ---
    def _fn_group_neutralize(self, args):
        x = self.evaluate(args[0])
        group_name = self._get_str_arg(args[1])
        group_map = self._data.sector if group_name in ("sector", "subindustry") else self._data.industry
        if not group_map:
            return x - x.mean(axis=1).values[:, None]
        groups = pd.Series({t: group_map.get(t, "Unknown") for t in x.columns})
        result = x.copy()
        for g in groups.unique():
            cols = groups[groups == g].index.tolist()
            valid = [c for c in cols if c in result.columns]
            if valid:
                result[valid] = result[valid].sub(result[valid].mean(axis=1), axis=0)
        return result

    def _fn_group_rank(self, args):
        x = self.evaluate(args[0])
        group_name = self._get_str_arg(args[1])
        group_map = self._data.sector if group_name in ("sector", "subindustry") else self._data.industry
        if not group_map:
            return x.rank(axis=1, pct=True)
        groups = pd.Series({t: group_map.get(t, "Unknown") for t in x.columns})
        result = x.copy()
        for g in groups.unique():
            cols = groups[groups == g].index.tolist()
            valid = [c for c in cols if c in result.columns]
            if valid:
                result[valid] = result[valid].rank(axis=1, pct=True)
        return result

    # --- Conditional ---
    def _fn_trade_when(self, args):
        if len(args) != 3:
            raise EvalError("trade_when requires 3 arguments: (condition, alpha, exit_condition)")
        cond = self.evaluate(args[0])
        alpha = self.evaluate(args[1])
        result = alpha.where(cond > 0, np.nan)
        return result

    def _fn_if_else(self, args):
        if len(args) != 3:
            raise EvalError("if_else requires 3 arguments: (condition, then, else)")
        cond = self.evaluate(args[0])
        then = self.evaluate(args[1])
        else_ = self.evaluate(args[2])
        return then.where(cond > 0, else_)


def evaluate_expression(expr: str, data: MarketData) -> pd.DataFrame:
    """Parse and evaluate a FASTEXPR expression on local market data."""
    ast = parse_expression(expr)
    evaluator = Evaluator(data)
    return evaluator.evaluate(ast)
