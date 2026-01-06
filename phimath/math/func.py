from phimath.control.numeric import *

def sqrt(x: float) -> float:
    """
    find the square root of a number x using the Newton-Raphson method.

    """
    if x < 0:
        return x**0.5  # Handle negative inputs by returning complex result
    if x == 0:
        return 0.0

    guess = x / 2.0
    for _ in range(MAX_ITERATIONS):  # Limit iterations to prevent infinite loops
        next_guess = (guess + x / guess) / 2.0
        if has_converged(next_guess - guess, EPSILON):  # Convergence check
            return next_guess
        guess = next_guess

    return guess  # Return the best guess after value converges or max iterations

def cbrt(x: float) -> float:
    """
    find the cube root of a number x using the Newton-Raphson method.

    """
    if x == 0:
        return 0.0

    guess = x / 3.0
    for _ in range(MAX_ITERATIONS):  # Limit iterations to prevent infinite loops
        next_guess = (2 * guess + x / (guess * guess)) / 3.0
        if has_converged(next_guess - guess, EPSILON):  # Convergence check
            return next_guess
        guess = next_guess

    return guess  # Return the best guess after value converges or max iterations

def pow(x: float, n: int) -> float:
    """
    Compute x raised to the power of n (x^n) using exponentiation by squaring.
    Handles negative exponents as well.
    """
    if n == 0:
        return 1.0
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    current_product = x

    while n > 0:
        if n % 2 == 1:  # If n is odd
            result *= current_product
        current_product *= current_product
        n //= 2

    return result