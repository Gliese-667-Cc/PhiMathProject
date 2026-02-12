import math
from phimath.control.symbols import Expression
# -------------------------------------------------
# Exponential
# -------------------------------------------------

def exp(x: float) -> float:
    if hasattr(x, 'derive') or hasattr(x, 'evaluate'):
        return Expression(x, "exp", None)
    return math.exp(x)
# -------------------------------------------------
# Natural logarithm
# -------------------------------------------------

def ln(x: float) -> float:
    if hasattr(x, 'derive') or hasattr(x, 'evaluate'):
        return Expression(x, "ln", None)
    return math.log(x)

# -------------------------------------------------
# Logarithm with arbitrary base
# -------------------------------------------------
def log(x, base=10):
    """Logarithm handling both numeric and symbolic inputs."""
    if hasattr(x, 'derive') or hasattr(x, 'evaluate') or hasattr(base, 'derive'):
        # Use left for the argument and right for the base
        return Expression(x, "log", base)
    
    return math.log(x, base)
