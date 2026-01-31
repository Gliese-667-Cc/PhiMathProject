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

def make_function(xi: list[float], yi: list[float]) -> function:
    """
    Create a function that interpolates the given data points (xi, yi)
    using Lagrange interpolation.

    Parameters:
    xi : list of float
        The x-coordinates of the data points.
    yi : list of float
        The y-coordinates of the data points.

    Returns:
    function
        A function that takes a single argument x and returns the interpolated value at x.
    """
    def linear_interpolation(x):
       # boundary checks
        if x <= xi[0]:
            return yi[0]
        if x >= xi[-1]:
            return yi[-1]
        
        #binary search to find the interval
        low, high = 0, len(xi) - 1
        while low <= high:
            mid = (low + high) // 2
            if xi[mid] <= x <= xi[mid + 1]:
                i = mid
                break
            elif xi[mid] > x:
                high = mid - 1
            else:
                low = mid + 1

            i = high  # high is the index of the interval containing x
            if i < 0:
                i = 0
            if i >= len(xi) - 1:
                i = len(xi) - 2

        # perform linear interpolation
        x0, x1 = xi[i], xi[i + 1]
        y0, y1 = yi[i], yi[i + 1]
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    
    return linear_interpolation