from phimath.math import *

class Expression:
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op

    def __repr__(self):
        return f"({self.left}{self.op}{self.right})"

    def __add__(self, other):
        return Expression(self, "+", other)
    
    def __sub__(self, other):
        return Expression(self, "-", other)

    def __mul__(self, other):
        return Expression(self, "*", other)
    
    def __truediv__(self, other):
        return Expression(self, "/", other)
    
    def __pow__(self, other):
        return Expression(self, "**", other)
    
    def evaluate(self, context):

        l = self.left.evaluate(context) if hasattr(self.left, 'evaluate') else self.left
        r = self.right.evaluate(context) if hasattr(self.right, 'evaluate') else self.right
        ops = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: a / b,
            "**" : lambda a, b: a ** b,
        }
        return ops[self.op](l,r)
    def derive(self, var):
        """Returns a new Expression representing the derivative."""
       
        DERIVATIVE_RULES = {
            "+": lambda u, v, var: u.derive(var) + v.derive(var),
            "-": lambda u, v, var: u.derive(var) - v.derive(var),
            "*": lambda u, v, var: (u.derive(var) * v) + (u * v.derive(var)),
            "/": lambda u, v, var: ((u.derive(var) * v) - (u * v.derive(var))) / (v ** 2),
            "**": lambda u, n, var: n * (u ** (n - 1)) * u.derive(var),
            "sin": lambda u, var: Expression(u, "cos") * u.derive(var),
            "cos": lambda u, var: (Expression(u, "sin") * -1) * u.derive(var),
            "exp": lambda u, var: Expression(u, "exp") * u.derive(var),
            "ln": lambda u, var: (1 / u) * u.derive(var),
            "log": lambda u, var: (1 / u * ln(10)) * u.derive(var),
            
}

class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
    
    def __add__(self, other):
        return Expression(f"{self.name}+{other}")
    
    def __sub__(self, other):
        return Expression(f"{self.name}+{other}")
    
    def __mul__(self, other):
        return Expression(f"{self.name}+{other}")
    
    def __truediv__(self, other):
        return Expression(f"{self.name}+{other}")
    
    def __pow__(self, other):
        return Expression(f"{self.name}+{other}")
    
    def __getattribute__(self, index):
        return Symbol(f"{self.name}_{index}")
    
    def evaluate(self, context):
        if self.name in context: return context[self.name]
        raise ValueError(f"Symbol '{self.name}' has no value in the provided context")
    
class SymbolFactory:
    def __getattribute__(self, name):
        return Symbol(name)
    
symbols = SymbolFactory()