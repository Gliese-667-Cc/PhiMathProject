"""
Mathematical constants for phimath.

All constants are computed numerically using series expansions
and controlled convergence.
"""

from phimath.control import MAX_ITER, has_converged


def compute_pi():
    """
    Compute pi using the Nilakantha series.

    pi = 3 + 4/(2·3·4) - 4/(4·5·6) + 4/(6·7·8) - ...
    """
    pi = 3.0
    sign = 1.0

    for n in range(1, MAX_ITER):
        term = 4.0 / ((2*n) * (2*n + 1) * (2*n + 2))
        pi += sign * term
        sign *= -1

        if has_converged(term):
            break

    return pi

def compute_e():
    """
    Compute e using the series expansion.

    e = 1 + 1/1! + 1/2! + 1/3! + ...
    """
    result = 1.0
    factorial = 1.0

    for n in range(1, MAX_ITER):
        factorial *= n
        term = 1.0 / factorial
        result += term

        if has_converged(term):
            break

    return result

# Core constants
PI = compute_pi()
TWO_PI = 2.0 * PI
HALF_PI = PI / 2.0
E = compute_e()

# Angle conversions
DEG_TO_RAD = PI / 180.0
RAD_TO_DEG = 180.0 / PI


print (PI, E)