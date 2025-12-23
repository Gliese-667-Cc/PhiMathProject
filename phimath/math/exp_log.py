"""
Exponential and logarithmic functions for phimath.

All implementations are fundamental:
- no external math library
- series based
- explicit convergence control
"""

from .constants import E
from phimath.control import MAX_ITER, has_converged


# -------------------------------------------------
# Exponential
# -------------------------------------------------

def exp(x: float) -> float:
    """
    Compute e^x using Taylor series expansion.

    e^x = 1 + x + x^2/2! + x^3/3! + ...
    """
    term = 1.0      # x^0 / 0!
    result = 1.0
    n = 1

    while n < MAX_ITER:
        term *= x / n
        result += term

        if has_converged(term):
            break

        n += 1

    return result


# -------------------------------------------------
# Natural logarithm
# -------------------------------------------------

def ln(x: float) -> float:
    """
    Compute natural logarithm ln(x), x > 0.

    Uses the series:
    ln(x) = 2 * [ y + y^3/3 + y^5/5 + ... ]
    where y = (x - 1) / (x + 1)

    Range reduction is applied for stability.
    """
    if x <= 0:
        raise ValueError("ln is undefined for x <= 0")

    # Range reduction: bring x close to 1
    k = 0
    while x > 1.5:
        x /= E
        k += 1
    while x < 0.75:
        x *= E
        k -= 1

    y = (x - 1) / (x + 1)

    term = y
    result = 0.0
    n = 1

    while n < MAX_ITER:
        result += term / (2*n - 1)

        if has_converged(term):
            break

        term *= y * y
        n += 1

    return 2.0 * result + k


# -------------------------------------------------
# Logarithm with arbitrary base
# -------------------------------------------------

def log(x: float, base: float = 10.0) -> float:
    """
    Compute logarithm with arbitrary base.

    log_base(x) = ln(x) / ln(base)
    """
    if base <= 0 or base == 1:
        raise ValueError("log base must be positive and not equal to 1")

    return ln(x) / ln(base)

