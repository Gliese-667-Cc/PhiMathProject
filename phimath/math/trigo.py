"""
Trigonometric functions for phimath.

Implements sine and cosine using Taylor series expansions
with explicit convergence control. All core functions
expect angles in radians.

Degree-based helpers are provided explicitly.
"""

from phimath.control import MAX_ITER, has_converged
from phimath.math.constants import PI, TWO_PI, DEG_TO_RAD, HALF_PI


# -------------------------------------------------
# Angle normalization
# -------------------------------------------------

def normalize_angle(x:float) -> float:
    """
    Reduce angle x to the range [-pi, pi] for better convergence.
    """
    while x > PI:
        x -= TWO_PI
    while x < -PI:
        x += TWO_PI
    return x


# -------------------------------------------------
# Sine (radians)
# -------------------------------------------------

def sin(x:float) -> float:
    """
    Compute sin(x), where x is in radians.
    """
    x = normalize_angle(x)
    #if angle is smaller than threshold, return x directly
    if abs(x) < 1e-3:
        return x
    
    else:
        term = x          # first term of the series
        result = 0.0
        n = 0

        while n < MAX_ITER:
            result += term

            if has_converged(term):
                break

            # term_{n+1} = -term_n * x^2 / ((2n+2)(2n+3))
            term *= -1 * x * x / ((2*n + 2) * (2*n + 3))
            n += 1

        return result

# -------------------------------------------------
# Cosine (radians)
# -------------------------------------------------

def cos(x:float) -> float:
    """
    Compute cos(x), where x is in radians.
    """
    x = normalize_angle(x)
    term = 1.0        # first term of the series
    result = 0.0
    n = 0

    while n < MAX_ITER:
        result += term
        if has_converged(term):
            break

        # term_{n+1} = -term_n * x^2 / ((2n+1)(2n+2))
        term *= -1 * x * x / ((2*n + 1) * (2*n + 2))
        n += 1

    return result


# -------------------------------------------------
# Degree-based helpers (explicit)
# -------------------------------------------------

def sin_deg(x:float) -> float:
    """
    Compute sine of an angle given in degrees.
    """
    return sin(x * DEG_TO_RAD)


def cos_deg(x:float) -> float:
    """
    Compute cosine of an angle given in degrees.
    """
    return cos(x * DEG_TO_RAD)

#-------------------------------------------------
# Tangent (radians and degrees)
#-------------------------------------------------

def tan(x:float) -> float:
    """
    Compute tan(x), where x is in radians.
    """
    #if angle is smaller than threshold, return x directly
    if abs(x) < 1e-3:
        return x
    
    else:
        cosine = cos(x)
        if abs(cosine) < 1e-15:
            raise ValueError("Tangent undefined for angles where cosine is zero.")
        return sin(x) / cosine

def tan_deg(x:float) -> float:
    """
    Compute tangent of an angle given in degrees.
    """
    return tan(x * DEG_TO_RAD)

# -------------------------------------------------
# Hyperbolic and Inverse Trigonometric Functions
# -------------------------------------------------

def sinh(x:float) -> float:
    """
    Compute sinh(x) using its Taylor series expansion.
    """
    term = x          # first term of the series
    result = 0.0
    n = 0

    while n < MAX_ITER:
        result += term

        if has_converged(term):
            break

        # term_{n+1} = term_n * x^2 / ((2n+2)(2n+3))
        term *= x * x / ((2*n + 2) * (2*n + 3))
        n += 1

    return result

def cosh(x:float) -> float:
    """
    Compute cosh(x) using its Taylor series expansion.
    """
    term = 1.0        # first term of the series
    result = 0.0
    n = 0

    while n < MAX_ITER:
        result += term

        if has_converged(term):
            break

        # term_{n+1} = term_n * x^2 / ((2n+1)(2n+2))
        term *= x * x / ((2*n + 1) * (2*n + 2))
        n += 1

    return result

def asin(x:float) -> float:
    """
    Compute arcsin(x) using its Taylor series expansion.
    Valid for |x| <= 1.
    """
    if abs(x) > 1:
        raise ValueError("arcsin is only defined for |x| <= 1")

    term = x          # first term of the series
    result = 0.0
    n = 0

    while n < MAX_ITER:
        result += term

        if has_converged(term):
            break

        # term_{n+1} = term_n * (2n+1)^2 * x^2 / (2(n+1)(2n+3))
        term *= (2*n + 1)**2 * x * x / (2 * (n + 1) * (2*n + 3))
        n += 1

    return result

def acos(x:float) -> float:
    """
    Compute arccos(x) using the relationship acos(x) = pi/2 - asin(x).
    Valid for |x| <= 1.
    """
    if abs(x) > 1:
        raise ValueError("arccos is only defined for |x| <= 1")
    return HALF_PI - asin(x)

def atan(x:float) -> float:
    """
    Compute arctan(x) using its Taylor series expansion.
    Valid for all real x.
    """
    term = x          # first term of the series
    result = 0.0
    n = 0

    while n < MAX_ITER:
        result += term

        if has_converged(term):
            break

        # term_{n+1} = -term_n * x^2 * (2n+1)/(2n+2)
        term *= -1 * x * x * (2*n + 1) / (2*n + 2)
        n += 1

    return result

def atan2(y:float, x:float) -> float:
    """
    Compute arctan2(y, x) to get the angle in the correct quadrant.
    """
    if x > 0:
        return atan(y / x)
    elif x < 0 and y >= 0:
        return atan(y / x) + PI
    elif x < 0 and y < 0:
        return atan(y / x) - PI
    elif x == 0 and y > 0:
        return HALF_PI
    elif x == 0 and y < 0:
        return -HALF_PI
    else:
        raise ValueError("atan2 undefined for (0, 0)")
    
