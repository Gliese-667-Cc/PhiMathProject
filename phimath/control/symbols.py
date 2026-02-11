from phimath.math import *

class Expression:
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op

    def __repr__(self):
        if self.op == "partial":
            return f"d({self.left})/d({self.right})"
        return f"({self.left} {self.op} {self.right})"

    # --- Forward Operators (Expression + other) ---
    def __add__(self, other): return Expression(self, "+", other)
    def __sub__(self, other): return Expression(self, "-", other)
    def __mul__(self, other): return Expression(self, "*", other)
    def __truediv__(self, other): return Expression(self, "/", other)
    def __pow__(self, other): return Expression(self, "**", other)

    # --- Reverse Operators (other + Expression) ---
    # These handle cases like "2 * x" or "2 + x"
    def __radd__(self, other): return Expression(other, "+", self)
    def __rsub__(self, other): return Expression(other, "-", self)
    def __rmul__(self, other): return Expression(other, "*", self)
    def __rtruediv__(self, other): return Expression(other, "/", self)
    def __rpow__(self, other): return Expression(other, "**", self)
    
    def evaluate(self, context):
        l = self.left.evaluate(context) if hasattr(self.left, 'evaluate') else self.left
        r = self.right.evaluate(context) if hasattr(self.right, 'evaluate') else self.right
        
        ops = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: a / b,
            "**" : lambda a, b: a ** b,
            "partial": lambda a, b: 0 # Placeholder if evaluating raw derivative
        }
        return ops[self.op](l,r)

    def derive(self, var):
        """Returns a new Expression representing the derivative."""
        u = self.left
        v = self.right
        
        # Helper to derive if object has the method, else return 0
        def d(term, x):
            return term.derive(x) if hasattr(term, 'derive') else 0

        if self.op == "+": return d(u, var) + d(v, var)
        if self.op == "-": return d(u, var) - d(v, var)
        if self.op == "*": return (d(u, var) * v) + (u * d(v, var))
        if self.op == "/": return ((d(u, var) * v) - (u * d(v, var))) / (v ** 2)
        if self.op == "**": 
            # Power rule: d/dx(u^n) = n*u^(n-1)*u' 
            # This line caused your error; now __rmul__ handles 'v * ...'
            return v * (u ** (v - 1)) * d(u, var)
            
        return Expression(self, "partial", var)

class Symbol:
    def __init__(self, name, is_function=False):
        self.name = name
        self.is_function = is_function

    def __repr__(self):
        return self.name
    
    # --- Forward Operators ---
    def __add__(self, other): return Expression(self, "+", other)
    def __sub__(self, other): return Expression(self, "-", other)
    def __mul__(self, other): return Expression(self, "*", other)
    def __truediv__(self, other): return Expression(self, "/", other)
    def __pow__(self, other): return Expression(self, "**", other)

    # --- Reverse Operators ---
    def __radd__(self, other): return Expression(other, "+", self)
    def __rsub__(self, other): return Expression(other, "-", self)
    def __rmul__(self, other): return Expression(other, "*", self)
    def __rtruediv__(self, other): return Expression(other, "/", self)
    def __rpow__(self, other): return Expression(other, "**", self)
    
    # --- Safe dynamic attributes ---
    def __getattr__(self, index):
        return Symbol(f"{self.name}_{index}")
    
    def evaluate(self, context):
        if self.name in context: return context[self.name]
        
        # Handle component lookups (e.g. context={"E_x": 0})
        if hasattr(self, 'name') and self.name in context:
            return context[self.name]
            
        raise ValueError(f"Symbol '{self.name}' has no value in the provided context")

    def derive(self, var):
        if self.name == var.name:
            return 1
        if self.is_function:
            return Expression(self, "partial", var)
        return 0

class VectorSymbol:
    def __init__(self, name):
        self.name = name
        self.x = Symbol(f"{name}_x", is_function=True)
        self.y = Symbol(f"{name}_y", is_function=True)
        self.z = Symbol(f"{name}_z", is_function=True)

    def __repr__(self):
        return f"Vec({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, VectorSymbol):
            return VectorSymbolComponents(self.x + other.x, self.y + other.y, self.z + other.z)
        return VectorSymbolComponents(self.x + other, self.y + other, self.z + other)

    # Added __rmul__ to allow "2 * v" scalar multiplication
    def __mul__(self, other):
        return VectorSymbolComponents(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other):
        return VectorSymbolComponents(other * self.x, other * self.y, other * self.z)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, other):
        return VectorSymbolComponents(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def evaluate(self, context):
        from phimath.linalg.vectors import vector
        return vector(
            self.x.evaluate(context),
            self.y.evaluate(context),
            self.z.evaluate(context)
        )

class VectorSymbolComponents:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"VecExpr(\n  x: {self.x},\n  y: {self.y},\n  z: {self.z}\n)"
    
    # Added scalar multiplication support for results
    def __mul__(self, other):
        return VectorSymbolComponents(self.x * other, self.y * other, self.z * other)
    def __rmul__(self, other):
        return VectorSymbolComponents(other * self.x, other * self.y, other * self.z)

    def evaluate(self, context):
        from phimath.linalg.vectors import vector
        return vector(
            self.x.evaluate(context) if hasattr(self.x, 'evaluate') else self.x,
            self.y.evaluate(context) if hasattr(self.y, 'evaluate') else self.y,
            self.z.evaluate(context) if hasattr(self.z, 'evaluate') else self.z
        )

class SymbolFactory:
    def __getattr__(self, name):
        return Symbol(name)
    
symbols = SymbolFactory()