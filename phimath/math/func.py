import math
from phimath.control.symbols import Expression

def sqrt(x: float) -> float:
    if hasattr(x, 'derive') or hasattr(x, 'evaluate'):
        return Expression(x, "sqrt", None)
    if x < 0:
        return x**0.5  # Handle negative inputs by returning complex result
    return math.sqrt(x)

def cbrt(x: float) -> float:
    if hasattr(x, 'derive') or hasattr(x, 'evaluate'):
        return Expression(x, "cbrt", None)
    return math.cbrt(x)

def pow(x: float, n: int) -> float:
    if hasattr(x, 'derive') or hasattr(x, 'evaluate'):
        return Expression(x, "**", n)
    return math.pow(x, n)

def abs(x: float) -> float:
    if hasattr(x, 'derive') or hasattr(x, 'evaluate'):
        return Expression(x, "abs", None)
    return math.fabs(x)

def make_function(xi: list[float], yi: list[float]):
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
