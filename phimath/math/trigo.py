import math
from phimath.math.constants import DEG_TO_RAD

def normalize_angle(x: float) -> float:
    """Reduce angle x to range [-pi, pi] using precise math.fmod"""
    return math.atan2(math.sin(x), math.cos(x))

# -------------------------------------------------
# Core Wrappers
# -------------------------------------------------

def sin(x: float) -> float:
    if x == 0:
        return 0.0
    if x == math.pi:
        return 0.0
    return math.sin(x)

def cos(x: float) -> float:
    if x == math.pi / 2:
        return 0.0
    if x == 3 * math.pi / 2:
        return 0.0
    return math.cos(x)

def tan(x: float) -> float:
    if x == math.pi / 2 or x == 3 * math.pi / 2:
        raise ValueError("tan(x) is undefined for x = (2n+1)*pi/2")
    return math.tan(x)

def sec(x: float) -> float:
    cos_x = cos(x)
    if cos_x == 0:
        raise ValueError("sec(x) is undefined for x = (2n+1)*pi/2")
    return 1 / cos_x

def csc(x: float) -> float:
    sin_x = sin(x)
    if sin_x == 0:
        raise ValueError("csc(x) is undefined for x = n*pi")
    return 1 / sin_x

def cot(x: float) -> float: 
    tan_x = tan(x)
    if tan_x == 0:
        raise ValueError("cot(x) is undefined for x = n*pi")
    return 1 / tan_x
# -------------------------------------------------
# Degree Helpers 
# -------------------------------------------------

def sin_deg(x: float) -> float:
    return sin(DEG_TO_RAD(x))

def cos_deg(x: float) -> float:
    return cos(DEG_TO_RAD(x))

def tan_deg(x: float) -> float:
    return tan(DEG_TO_RAD(x))

def sec_deg(x: float) -> float:
    return sec(DEG_TO_RAD(x))

def csc_deg(x: float) -> float:
    return csc(DEG_TO_RAD(x))

def cot_deg(x: float) -> float:
    return cot(DEG_TO_RAD(x))

# -------------------------------------------------
# Hyperbolic 
# -------------------------------------------------

def sinh(x: float) -> float:
    return math.sinh(x)

def cosh(x: float) -> float:
    return math.cosh(x)

def tanh(x: float) -> float:
    return math.tanh(x)

def sech(x: float) -> float:
    cosh_x = cosh(x)
    if cosh_x == 0:
        raise ValueError("sech(x) is undefined for x where cosh(x) = 0")
    return 1 / cosh_x

def csch(x: float) -> float:
    sinh_x = sinh(x)
    if sinh_x == 0:
        raise ValueError("csch(x) is undefined for x where sinh(x) = 0")
    return 1 / sinh_x

def coth(x: float) -> float:
    tanh_x = tanh(x)
    if tanh_x == 0:
        raise ValueError("coth(x) is undefined for x where tanh(x) = 0")
    return 1 / tanh_x
# -------------------------------------------------
# Inverse 
# -------------------------------------------------

def asin(x: float) -> float:
    return math.asin(x)

def acos(x: float) -> float:
    return math.acos(x)

def atan(x: float) -> float:
    return math.atan(x)

def atan2(y: float, x: float) -> float:
    return math.atan2(y, x)