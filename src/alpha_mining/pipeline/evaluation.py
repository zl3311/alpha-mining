"""
Evaluation stage: score, rank, and select simulation results.

Computes fitness scores, identifies submission-ready alphas,
and selects top performers for the feedback loop.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from ..brain.models import SimulationResult

logger = logging.getLogger(__name__)


@dataclass
class EvaluationSummary:
    """Summary of an evaluation batch."""

    total: int = 0
    succeeded: int = 0
    failed: int = 0
    submittable: int = 0
    avg_sharpe: float = 0.0
    max_sharpe: float = 0.0
    avg_fitness: float = 0.0
    max_fitness: float = 0.0
    top_expressions: list[str] = None

    def __post_init__(self):
        if self.top_expressions is None:
            self.top_expressions = []


def evaluate_results(results: list[SimulationResult]) -> EvaluationSummary:
    """
    Evaluate a batch of simulation results.

    Returns a summary with aggregate statistics and identifies
    the top-performing expressions for feedback.
    """
    summary = EvaluationSummary(total=len(results))

    succeeded = [r for r in results if r.succeeded]
    summary.succeeded = len(succeeded)
    summary.failed = summary.total - summary.succeeded

    if not succeeded:
        return summary

    sharpes = [r.metrics.sharpe for r in succeeded]
    fitnesses = [r.metrics.fitness for r in succeeded]

    summary.avg_sharpe = sum(sharpes) / len(sharpes)
    summary.max_sharpe = max(sharpes)
    summary.avg_fitness = sum(fitnesses) / len(fitnesses)
    summary.max_fitness = max(fitnesses)

    summary.submittable = sum(1 for r in succeeded if r.submittable)

    ranked = sorted(succeeded, key=lambda r: r.metrics.fitness, reverse=True)
    top_n = max(1, len(ranked) // 4)  # top quartile
    summary.top_expressions = [r.config.expression for r in ranked[:top_n]]

    logger.info(
        "Evaluation: %d/%d succeeded, %d submittable, "
        "Sharpe avg=%.2f max=%.2f, Fitness avg=%.2f max=%.2f",
        summary.succeeded,
        summary.total,
        summary.submittable,
        summary.avg_sharpe,
        summary.max_sharpe,
        summary.avg_fitness,
        summary.max_fitness,
    )

    return summary


def rank_results(results: list[SimulationResult]) -> list[SimulationResult]:
    """Sort results by fitness score descending. Only includes successful sims."""
    return sorted(
        [r for r in results if r.succeeded],
        key=lambda r: r.metrics.fitness,
        reverse=True,
    )


def select_for_submission(results: list[SimulationResult]) -> list[SimulationResult]:
    """Filter results that pass all submission gates."""
    candidates = [r for r in results if r.submittable]
    logger.info(
        "Submission candidates: %d/%d pass all gates", len(candidates), len(results)
    )
    return candidates
