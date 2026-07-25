"""
Tests for the evaluation stage.

Covers result scoring, ranking, and submission selection.
"""


from alpha_mining.brain.models import (
    AlphaMetrics,
    CheckResult,
    SimulationConfig,
    SimulationResult,
    SimulationStatus,
)
from alpha_mining.pipeline.evaluation import (
    evaluate_results,
    rank_results,
    select_for_submission,
)


def _make_result(
    expr: str = "rank(close)",
    sharpe: float = 1.0,
    fitness: float = 0.8,
    turnover: float = 0.3,
    status: SimulationStatus = SimulationStatus.DONE,
    checks_pass: bool = True,
) -> SimulationResult:
    checks = [CheckResult(name="TEST", result="PASS" if checks_pass else "FAIL")]
    return SimulationResult(
        config=SimulationConfig(expression=expr),
        status=status,
        metrics=AlphaMetrics(
            sharpe=sharpe, fitness=fitness, turnover=turnover, checks=checks
        ),
    )


class TestEvaluateResults:
    def test_empty_batch(self):
        summary = evaluate_results([])
        assert summary.total == 0
        assert summary.succeeded == 0

    def test_all_failed(self):
        results = [
            SimulationResult(
                config=SimulationConfig(expression="rank(close)"),
                status=SimulationStatus.FAILED,
                error_message="timeout",
            )
            for _ in range(3)
        ]
        summary = evaluate_results(results)
        assert summary.total == 3
        assert summary.succeeded == 0
        assert summary.failed == 3

    def test_mixed_batch(self):
        results = [
            _make_result(sharpe=1.5, fitness=1.2),
            _make_result(sharpe=0.5, fitness=0.3),
            SimulationResult(
                config=SimulationConfig(expression="bad"),
                status=SimulationStatus.FAILED,
            ),
        ]
        summary = evaluate_results(results)
        assert summary.total == 3
        assert summary.succeeded == 2
        assert summary.failed == 1
        assert summary.max_sharpe == 1.5

    def test_submittable_count(self):
        results = [
            _make_result(sharpe=1.5, fitness=1.2, turnover=0.3),  # passes
            _make_result(sharpe=0.8, fitness=0.5, turnover=0.3),  # fails sharpe
            _make_result(sharpe=1.5, fitness=1.2, turnover=0.3, checks_pass=False),  # fails check
        ]
        summary = evaluate_results(results)
        assert summary.submittable == 1

    def test_top_expressions(self):
        results = [
            _make_result(expr="alpha_a", fitness=3.0),
            _make_result(expr="alpha_b", fitness=2.0),
            _make_result(expr="alpha_c", fitness=1.0),
            _make_result(expr="alpha_d", fitness=0.5),
        ]
        summary = evaluate_results(results)
        assert "alpha_a" in summary.top_expressions


class TestRankResults:
    def test_rank_order(self):
        results = [
            _make_result(expr="low", fitness=0.5),
            _make_result(expr="high", fitness=2.0),
            _make_result(expr="mid", fitness=1.0),
        ]
        ranked = rank_results(results)
        assert ranked[0].config.expression == "high"
        assert ranked[-1].config.expression == "low"

    def test_rank_excludes_failed(self):
        results = [
            _make_result(expr="good", fitness=1.0),
            SimulationResult(
                config=SimulationConfig(expression="bad"),
                status=SimulationStatus.FAILED,
            ),
        ]
        ranked = rank_results(results)
        assert len(ranked) == 1


class TestSelectForSubmission:
    def test_filters_submittable(self):
        results = [
            _make_result(sharpe=1.5, fitness=1.2, turnover=0.3),
            _make_result(sharpe=0.5, fitness=0.3, turnover=0.3),
        ]
        candidates = select_for_submission(results)
        assert len(candidates) == 1

    def test_empty_when_none_pass(self):
        results = [
            _make_result(sharpe=0.5, fitness=0.3, turnover=0.3),
        ]
        candidates = select_for_submission(results)
        assert len(candidates) == 0
