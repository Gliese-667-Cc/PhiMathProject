"""
Numeric control parameters for phimath.

This module defines global numerical tolerances and limits used across the library to control precision, convergence,and numerical stability.

No mathematical logic should live here.
"""
# Global convergence tolerance for iterative algorithms
EPSILON = 1e-8

# Maximum number of iterations for iterative algorithms
MAX_ITERATIONS = 10000

# default step size for numerical differentiation
DELTA = 1e-6

def is_close(a:float, b:float, tol=EPSILON) -> bool:
    """
    Check if two floating-point numbers are close to each other within a specified tolerance.

    Parameters:
    a (float): First number.
    b (float): Second number.
    tol (float): Tolerance for closeness.

    Returns:
    bool: True if the numbers are close, False otherwise.
    """
    return abs(a - b) < tol

def has_converged(term:float, tol=EPSILON) -> bool:
    """
    Determine if an iterative algorithm has converged based on the term.

    Parameters:
    term (float): The current term value.
    tol (float): Tolerance for convergence.

    Returns:
    bool: True if the algorithm has converged, False otherwise.
    """
    return abs(term) < tol

def is_close_relative(a:float, b:float, rel_tol=EPSILON, abs_tol=EPSILON) -> bool:
    """
    Check if two floating-point numbers are close to each other within a specified relative tolerance.

    Parameters:
    a (float): First number.
    b (float): Second number.
    rel_tol (float): Relative tolerance for closeness.

    Returns:
    bool: True if the numbers are close, False otherwise.
    """
    return abs(a - b) < max(rel_tol * max(abs(a), abs(b)), abs_tol)

def is_zero(value:float, tol=EPSILON) -> bool:
    """
    Check if a floating-point number is effectively zero within a specified tolerance.

    Parameters:
    value (float): The number to check.
    tol (float): Tolerance for zero check.

    Returns:
    bool: True if the number is effectively zero, False otherwise.
    """
    return abs(value) < tol

def iteration_limit(iter_count: int, max_iter=MAX_ITERATIONS) -> None:
    """
    Check if the iteration count has exceeded the maximum allowed iterations.
    if so, raise a RuntimeError.
    """
    if iter_count >= max_iter:
        raise RuntimeError("Iteration limit reached.")

