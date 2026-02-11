from phimath.math.func import pow

def reimann_sum(f: callable, a: float, b: float, dx=1e-4)-> float:
    integral = 0.0
    n = int((b - a) / dx)
    for i in range(n):
        integral += f(a + i * dx) * dx
    return integral

def trapezoidal_rule(f: callable, a: float, b: float, dx=1e-4)-> float:
    n = int((b - a) / dx)
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * dx)
    return integral * dx

def simpsons_rule(f: callable, a: float, b: float, dx=1e-4)-> float:
    n = int((b - a) / dx)
    if n % 2 == 1:
        n += 1  # n must be even
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(a + i * dx)
    for i in range(2, n-1, 2):
        integral += 2 * f(a + i * dx)
    return integral * dx / 3

def boole_rule(f: callable, a: float, b: float, dx=1e-4)-> float:
    n = int((b - a) / dx)
    if n % 4 != 0:
        n += 4 - (n % 4)  # n must be multiple of 4
    integral = 0.0
    for i in range(0, n, 4):
        x0 = a + i * dx
        x1 = a + (i + 1) * dx
        x2 = a + (i + 2) * dx
        x3 = a + (i + 3) * dx
        x4 = a + (i + 4) * dx
        integral += (2 * dx / 45) * (7 * f(x0) + 32 * f(x1) + 12 * f(x2) + 32 * f(x3) + 7 * f(x4))
    return integral

def romberg_integration(f: callable, a: float, b: float, max_order=5):
    R = [[0] * (max_order + 1) for _ in range(max_order + 1)]
    for k in range(max_order + 1):
        n = pow(2, k)
        R[k][0] = trapezoidal_rule(f, a, b, n)
        for j in range(1, k + 1):
            R[k][j] = (pow(4, j) * R[k][j - 1] - R[k - 1][j - 1]) / (pow(4, j) - 1)
    return R[max_order][max_order]


def integrate(f: callable, a: float, b: float, method='simpson', dx=1e-4)-> float:
    """
    Numerically integrates the function f from a to b using specified method.
    f: function to integrate
    a: lower limit
    b: upper limit
    method: integration method ('riemann', 'trapezoidal', 'simpson', 'boole')
    n: number of subintervals (for methods that require it)
    """
    if method == 'riemann':
        return reimann_sum(f, a, b, dx)
    elif method == 'trapezoidal':
        return trapezoidal_rule(f, a, b, dx)
    elif method == 'simpson':
        return simpsons_rule(f, a, b, dx)
    elif method == 'boole':
        return boole_rule(f, a, b, dx)
    else:
        return simpsons_rule(f, a, b, dx)