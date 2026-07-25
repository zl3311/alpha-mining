"""
Tests for BRAIN data models.

Covers SimulationConfig, AlphaMetrics, SimulationResult, CheckResult, and AlphaLanguage:
- API payload generation
- Multi-language support
- Submission gate checks (Sharpe, fitness, turnover thresholds)
- Fitness score computation
- Self-correlation extraction from checks
- Status predicates (succeeded, submittable)
"""

import pytest

from alpha_mining.brain.models import (
    AlphaMetrics,
    CheckResult,
    SimulationConfig,
    SimulationResult,
    SimulationStatus,
)

# ---------------------------------------------------------------------------
# SimulationConfig
# ---------------------------------------------------------------------------


class TestSimulationConfig:
    def test_defaults(self):
        cfg = SimulationConfig(expression="rank(close)")
        assert cfg.region.value == "USA"
        assert cfg.universe.value == "TOP3000"
        assert cfg.delay == 1
        assert cfg.decay == 6
        assert cfg.neutralization.value == "SUBINDUSTRY"
        assert cfg.language.value == "FASTEXPR"

    def test_to_api_payload_structure(self):
        cfg = SimulationConfig(expression="rank(close)")
        payload = cfg.to_api_payload()
        assert payload["regular"] == "rank(close)"
        assert payload["type"] == "REGULAR"
        assert "settings" in payload
        settings = payload["settings"]
        assert settings["instrumentType"] == "EQUITY"
        assert settings["language"] == "FASTEXPR"
        assert settings["region"] == "USA"
        assert settings["universe"] == "TOP3000"

    def test_python_language(self):
        cfg = SimulationConfig(expression="close / delay(close, 5)", language="PYTHON")
        payload = cfg.to_api_payload()
        assert payload["settings"]["language"] == "PYTHON"

    def test_expression_language(self):
        cfg = SimulationConfig(expression="rank(close)", language="EXPRESSION")
        payload = cfg.to_api_payload()
        assert payload["settings"]["language"] == "EXPRESSION"

    def test_custom_params(self):
        cfg = SimulationConfig(
            expression="rank(volume)",
            region="CHN",
            universe="TOP1000",
            decay=10,
            truncation=0.05,
            neutralization="MARKET",
        )
        payload = cfg.to_api_payload()
        assert payload["settings"]["region"] == "CHN"
        assert payload["settings"]["universe"] == "TOP1000"
        assert payload["settings"]["decay"] == 10
        assert payload["settings"]["truncation"] == 0.05
        assert payload["settings"]["neutralization"] == "MARKET"

    def test_frozen_immutable(self):
        cfg = SimulationConfig(expression="rank(close)")
        with pytest.raises(Exception):
            cfg.expression = "rank(volume)"


# ---------------------------------------------------------------------------
# AlphaMetrics
# ---------------------------------------------------------------------------


class TestAlphaMetrics:
    def test_passes_submission_gates_good(self):
        metrics = AlphaMetrics(
            sharpe=1.5,
            fitness=1.2,
            turnover=0.3,
            checks=[CheckResult(name="TEST", result="PASS")],
        )
        assert metrics.passes_submission_gates

    def test_fails_low_sharpe(self):
        metrics = AlphaMetrics(sharpe=0.8, fitness=1.2, turnover=0.3)
        assert not metrics.passes_submission_gates

    def test_fails_low_fitness(self):
        metrics = AlphaMetrics(sharpe=1.5, fitness=0.5, turnover=0.3)
        assert not metrics.passes_submission_gates

    def test_fails_high_turnover(self):
        metrics = AlphaMetrics(sharpe=1.5, fitness=1.2, turnover=0.8)
        assert not metrics.passes_submission_gates

    def test_fails_low_turnover(self):
        metrics = AlphaMetrics(sharpe=1.5, fitness=1.2, turnover=0.005)
        assert not metrics.passes_submission_gates

    def test_fails_check_failure(self):
        metrics = AlphaMetrics(
            sharpe=1.5,
            fitness=1.2,
            turnover=0.3,
            checks=[
                CheckResult(name="CONCENTRATED_WEIGHT", result="FAIL"),
            ],
        )
        assert not metrics.passes_submission_gates

    def test_all_checks_pass(self):
        metrics = AlphaMetrics(
            checks=[
                CheckResult(name="A", result="PASS"),
                CheckResult(name="B", result="PASS"),
            ]
        )
        assert metrics.all_checks_pass

    def test_all_checks_pass_with_failure(self):
        metrics = AlphaMetrics(
            checks=[
                CheckResult(name="A", result="PASS"),
                CheckResult(name="B", result="FAIL"),
            ]
        )
        assert not metrics.all_checks_pass

    def test_self_correlation_extraction(self):
        metrics = AlphaMetrics(
            checks=[
                CheckResult(name="OTHER", result="PASS", value=0.1),
                CheckResult(name="SELF_CORRELATION", result="PASS", value=0.45),
            ]
        )
        assert metrics.self_correlation == 0.45

    def test_self_correlation_missing(self):
        metrics = AlphaMetrics(checks=[CheckResult(name="OTHER", result="PASS")])
        assert metrics.self_correlation is None

    def test_fitness_score_computation(self):
        import math

        metrics = AlphaMetrics(sharpe=1.5, returns=0.1, turnover=0.4)
        expected = math.sqrt(abs(0.1) / max(0.4, 0.125)) * 1.5
        assert abs(metrics.fitness_score() - expected) < 1e-6

    def test_fitness_score_low_turnover_floor(self):
        import math

        metrics = AlphaMetrics(sharpe=2.0, returns=0.05, turnover=0.01)
        expected = math.sqrt(abs(0.05) / 0.125) * 2.0
        assert abs(metrics.fitness_score() - expected) < 1e-6


# ---------------------------------------------------------------------------
# SimulationResult
# ---------------------------------------------------------------------------


class TestSimulationResult:
    def test_succeeded_true(self):
        result = SimulationResult(
            config=SimulationConfig(expression="rank(close)"),
            status=SimulationStatus.DONE,
            metrics=AlphaMetrics(sharpe=1.0),
        )
        assert result.succeeded

    def test_succeeded_false_no_metrics(self):
        result = SimulationResult(
            config=SimulationConfig(expression="rank(close)"),
            status=SimulationStatus.DONE,
        )
        assert not result.succeeded

    def test_succeeded_false_wrong_status(self):
        result = SimulationResult(
            config=SimulationConfig(expression="rank(close)"),
            status=SimulationStatus.FAILED,
            metrics=AlphaMetrics(sharpe=1.0),
        )
        assert not result.succeeded

    def test_submittable(self):
        result = SimulationResult(
            config=SimulationConfig(expression="rank(close)"),
            status=SimulationStatus.DONE,
            metrics=AlphaMetrics(
                sharpe=1.5, fitness=1.2, turnover=0.3,
                checks=[CheckResult(name="X", result="PASS")],
            ),
        )
        assert result.submittable

    def test_not_submittable_failed(self):
        result = SimulationResult(
            config=SimulationConfig(expression="rank(close)"),
            status=SimulationStatus.FAILED,
            error_message="timeout",
        )
        assert not result.submittable
