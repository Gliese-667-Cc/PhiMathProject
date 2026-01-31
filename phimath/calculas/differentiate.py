def differentiate(f, x, h=1e-5):
    """
    Numerically differentiates the function f at point x using central difference.
    f: function to differentiate
    x: point at which to differentiate
    h: small step size
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def fdifferentiate(f, x, h=1e-5):
    """
    Numerically differentiates the function f at point x using forward difference.
    f: function to differentiate
    x: point at which to differentiate
    h: small step size
    """
    return (f(x + h) - f(x)) / h

def bdifferentiate(f, x, h=1e-5):
    """
    Numerically differentiates the function f at point x using backward difference.
    f: function to differentiate
    x: point at which to differentiate
    h: small step size
    """
    return (f(x) - f(x - h)) / h

def second_derivative(f, x, h=1e-5):
    """
    Numerically computes the second derivative of the function f at point x.
    f: function to differentiate
    x: point at which to differentiate
    h: small step size
    """
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

def nth_derivative(f, x, n, h=1e-5):
    """
    Numerically computes the n-th derivative of the function f at point x.
    f: function to differentiate
    x: point at which to differentiate
    n: order of the derivative
    h: small step size
    """
    if n == 0:
        return f(x)
    elif n == 1:
        return differentiate(f, x, h)
    else:
        return (nth_derivative(f, x + h, n - 1, h) - nth_derivative(f, x - h, n - 1, h)) / (2 * h)
