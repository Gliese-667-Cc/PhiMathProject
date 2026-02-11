from phimath.math.func import make_function

def rk2(f: callable, x0: float, y0: float, h: float, n: int)-> callable:
    """
    Second-order Runge-Kutta method (Heun's method) for solving ODEs.

    Parameters:
    f : function
        The function defining the ODE (dy/dx = f(x, y)).
    x0 : float
        The initial x value.
    y0 : float
        The initial y value.
    h : float
        The step size.
    n : int
        The number of steps to perform.
    Returns: 
        list of values      
    """
    x, y = x0, y0
    xi=[]
    yi=[]
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y += (h / 2) * (k1 + k2)
        x += h
        xi.append(x)
        yi.append(y)
    return make_function(xi,yi)

def rk4(f: callable, x0: float, y0: float, h: float, n: int)-> callable:
    """
    Fourth-order Runge-Kutta method for solving ODEs.

    Parameters:
    f : function
        The function defining the ODE (dy/dx = f(x, y)).
    x0 : float
        The initial x value.
    y0 : float
        The initial y value.
    h : float
        The step size.  
    n : int
        The number of steps to perform.
    Returns: function
        returns the function f.       
    """
    x, y = x0, y0
    xi=[]
    yi=[]
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + (h / 2) * k1)
        k3 = f(x + h / 2, y + (h / 2) * k2)
        k4 = f(x + h, y + h * k3)
        y += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xi.append(x)
        yi.append(y)
    return make_function(xi,yi)

def rkf45(f: callable, x0: float, y0: float, h: float, n: int)-> callable:
    """
    Runge-Kutta-Fehlberg method (RKF45) for solving ODEs with adaptive step size.

    Parameters:
    f : function
        The function defining the ODE (dy/dx = f(x, y)).
    x0 : float
        The initial x value.
    y0 : float
        The initial y value.
    h : float
        The initial step size.
    n : int
        The number of steps to perform.
    Returns: function
        returns the function f.        
    """
    x, y = x0, y0
    xi=[]
    yi=[]
    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 4, y + k1 / 4)
        k3 = h * f(x + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2 / 32)
        k4 = h * f(x + 12 * h / 13, y + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197)
        k5 = h * f(x + h, y + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104)
        k6 = h * f(x + h / 2, y - 8 * k1 / 27 + 2 * k2 - 3544 * k3 / 2565 + 1859 * k4 / 4104 - 11 * k5 / 40)

        y4th = y + (25 * k1 / 216 + 1408 * k3 / 2565 + 2197 * k4 / 4104 - k5 / 5)
        y5th = y + (16 * k1 / 135 + 6656 * k3 / 12825 + 28561 * k4 / 56430 - 9 * k5 / 50 + 2 * k6 / 55)

        # Estimate the error
        error = abs(y5th - y4th)
        # Adjust step size based on error (simple strategy)
        if error < 1e-6:
            x += h
            y = y5th
            h *= 1.5  # Increase step size
            xi.append(x)
            yi.append(y)
        else:
            h *= 0.5  # Decrease step size
        
    return make_function(xi,yi)
def euler(f: callable, x0: float, y0: float, h: float, n: int)-> callable:
    """
    Euler's method for solving ODEs.

    Parameters:
    f : function
        The function defining the ODE (dy/dx = f(x, y)).
    x0 : float
        The initial x value.
    y0 : float
        The initial y value.
    h : float
        The step size.
    n : int
        The number of steps to perform.
    Returns: function
        returns the function f.
    """
    x, y = x0, y0
    xi=[]
    yi=[]
    for _ in range(n):
        y += h * f(x, y)
        x += h
        xi.append(x)
        yi.append(y)
    return make_function(xi,yi)

def ode_solver(f: callable, x0: float, y0: float, h: float, n: int, method: str='rk4')-> callable:
    """
    General ODE solver that selects the method based on the input string.

    Parameters:
    method : str
        The method to use ('euler', 'rk2', 'rk4', 'rkf45').
    f : function
        The function defining the ODE (dy/dx = f(x, y)).
    x0 : float
        The initial x value.
    y0 : float
        The initial y value.
    h : float
        The step size.
    n : int
        The number of steps to perform.
    Returns: function
        returns the function f.
    """
    if method == 'euler':
        return euler(f, x0, y0, h, n)
    elif method == 'rk2':
        return rk2(f, x0, y0, h, n)
    elif method == 'rk4':
        return rk4(f, x0, y0, h, n)
    elif method == 'rkf45':
        return rkf45(f, x0, y0, h, n)
    else:
        raise ValueError(f"Unknown method: {method}")