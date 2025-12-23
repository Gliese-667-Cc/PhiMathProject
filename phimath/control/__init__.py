"""
Numerical control layer for phimath.

This package defines global tolerances, iteration limits,
and helper checks used across the library to ensure
consistent numerical behavior.
"""

from .numeric import (
    EPSILON,
    MAX_ITERATIONS as MAX_ITER,
    DELTA,
    is_close,
    is_close_relative as is_close_rel,
    is_zero,
    has_converged,
    iteration_limit,
)

__all__ = [
    "EPSILON",
    "MAX_ITER",
    "DELTA",
    "is_close",
    "is_close_rel",
    "is_zero",
    "has_converged",
    "iteration_limit",
]
