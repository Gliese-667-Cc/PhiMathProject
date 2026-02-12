class Expression:
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op

    def __repr__(self):
    # Handle Unary Operators (Trig, Exp, Log, etc.)
        unary_ops = ["sin", "cos", "tan", "sec", "csc", "cot", "exp", "ln", "log", "asin", "acos", "atan"]

        if self.op in unary_ops:
            return f"{self.op}({self.left})"

        # Handle Derivatives
        if self.op == "partial":
            return f"d({self.left})/d({self.right})"

        # Handle Integrals
        if self.op == "integral":
            return f"∫({self.left}) d{self.right}"
        
        if self.op == "sqrt":
            return f"sqrt({self.left})"
        
        # Handle Power with special syntax
        if self.op in ["**", "^"]:
            return f"({self.left} ^ {self.right})"
        
        # Handle standard binary operators
        binary_ops = ["+", "-", "*", "/", "%", "//"]
        if self.op in binary_ops:
            return f"({self.left} {self.op} {self.right})"
        
        if self.op =="abs":
            return f"|{self.left}|"

        # Standard Binary Operators (a + b, a * b, etc.)
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
        from phimath. math import sin, cos, tan, sec, csc, cot, exp, ln, asin, acos, atan, sqrt, log,  pow, abs
        l = self.left.evaluate(context) if hasattr(self.left, 'evaluate') else self.left
        r = self.right.evaluate(context) if hasattr(self.right, 'evaluate') else self.right
        
        ops = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: a / b,
            "**" : lambda a, b: pow(a, b),
            "^" : lambda a, b: pow(a, b),
            "partial": lambda a, b: 0, # Placeholder if evaluating raw derivative
            "sin": lambda a, _: sin(a),
            "cos": lambda a, _: cos(a),
            "tan": lambda a, _: tan(a),
            "sec": lambda a, _: sec(a),
            "csc": lambda a, _: csc(a),
            "cot": lambda a, _: cot(a),
            "exp": lambda a, _: exp(a),
            "ln": lambda a, _: ln(a),
            "log": lambda a, b: log(a, b),
            "asin": lambda a, _: asin(a),
            "acos": lambda a, _: acos(a),
            "atan": lambda a, _: atan(a),
            "sqrt": lambda a, _: sqrt(a),
            "abs": lambda a, _: abs(a)
        }
        return ops[self.op](l,r)

    def derive(self, var):
        from phimath.math import sin, cos, tan, sec, csc, cot, exp, ln, sqrt
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
        if self.op == "**" or self.op == "^": 
            # Power rule: d/dx(u^n) = n*u^(n-1)*u' 
            return v * (u ** (v-1)) * d(u, var)
        if self.op == "partial":
            if self.right == var:
                return 1
            return 0
        if self.op == "sin": return cos(u) * d(u, var)
        if self.op == "cos": return -sin(u) * d(u, var)
        if self.op == "tan": return (sec(u) ** 2) * d(u, var)
        if self.op == "sec": return sec(u) * tan(u) * d(u, var)
        if self.op == "csc": return -csc(u) * cot(u) * d(u, var)
        if self.op == "cot": return -1 * (csc(u) ** 2) * d(u, var)
        if self.op == "exp": return exp(u) * d(u, var)
        if self.op == "ln": return (1/u) * d(u, var)
        if self.op == "log": return (1/(u * ln(10))) * d(u, var)
        if self.op == "asin": return (1 / sqrt(1 - (u ** 2))) * d(u, var)
        if self.op == "acos": return (-1 / sqrt(1 - (u ** 2))) * d(u, var)
        if self.op == "atan": return (1 / (1 + (u ** 2))) * d(u, var)

        return Expression(self, "partial", var)
    
    def aderive(self, var):
        from phimath.math import sin, cos, tan, sec, exp, ln, asin, atan, sqrt

        """Returns a new Expression representing the integral."""
        u = self.left
        v = self.right

        def i(term, x):
            return term.aderive(x) if hasattr(term, 'aderive') else (term * x)

        def d(term, x):
            return term.derive(x) if hasattr(term, 'derive') else 0

        if self.op == "+": return i(u, var) + i(v, var)
        if self.op == "-": return i(u, var) - i(v, var)

        # Power Rule for Integration
        if self.op in ["**", "^"]:
            if u == var:
                # Check for 1/x case (n = -1)
                if v == -1: return ln(abs(u))
                return pow(u, v + 1) / (v + 1)
            if v == var:
                # Fixed: integral of a^x is a^x / ln(a)
                return pow(u, v) / ln(u)

        # Simple substitution check: only integrate if the inner term is just 'var'
        # This prevents the "+ i(u, var)" logic which was mathematically incorrect.
        if u != var:
            return Expression(self, "integral", var)

        if self.op == "sin":  return -cos(u)
        if self.op == "cos":  return sin(u)
        if self.op == "tan":  return -ln(abs(cos(u)))
        if self.op == "sec":  return ln(abs(sec(u) + tan(u)))
        if self.op == "csc":  return ln(abs(tan(u / 2)))
        if self.op == "cot":  return ln(abs(sin(u)))
        if self.op == "exp":  return exp(u)
        if self.op == "ln":   return (u * ln(u)) - u
        if self.op == "asin": return (u * asin(u)) + sqrt(1 - (u ** 2))
        if self.op == "atan": return (u * atan(u)) - (0.5 * ln(u ** 2 + 1))

        return Expression(self, "integral", var)
    
    def simplify(self):
        """Recursively simplifies the expression tree."""
        # 1. Simplify children first (Post-order traversal)
        u = self.left.simplify() if hasattr(self.left, 'simplify') else self.left
        v = self.right.simplify() if hasattr(self.right, 'simplify') else self.right

        # 2. Constant Folding (e.g., 2 + 3 -> 5)
        if isinstance(u, (int, float)) and isinstance(v, (int, float)):
            if self.op == "+": return u + v
            if self.op == "-": return u - v
            if self.op == "*": return u * v
            if self.op == "/": return u / v if v != 0 else self
            if self.op in ["**", "^"]: return u ** v

        # 3. Identity Rules (The "Common Sense" rules)
        if self.op == "+":
            if u == 0: return v

            if v == 0: return u

        if self.op == "-":
            if v == 0: return u
            if u == v: return 0

        if self.op == "*":
            if u == 0 or v == 0: return 0
            if u == 1: return v
            if v == 1: return u

        if self.op == "/":
            if u == 0: return 0
            if v == 1: return u
            if u == v: return 1
            if v == 0: return self  # Avoid division by zero

        if self.op in ["**", "^"]:
            if v == 0: return 1
            if v == 1: return u
            if u == 1: return 1

        # Return a new Expression with the simplified children
        return Expression(u, self.op, v)
    
    def to_numeric(self, *args):
        """
        Returns a fast, callable function for numerical evaluation.
        Usage: f = expr.to_numeric('x', 'y')
               result = f(3, 4)
            """
        # 1. Convert the expression to a Python-readable string
        # We replace our symbolic names with 'math.func' equivalents
        expr_str = str(self.simplify())

        # 2. Define the function wrapper string
        # We include 'math' and 'pm' to handle all function calls
        arg_list = ", ".join(args)
        func_code = f"lambda {arg_list}: {expr_str}"

        from phimath.math import sin, cos, tan, sec, csc, cot, exp, ln, log, sqrt, pow, abs
        # 3. Create the evaluation context
        context = {
            "sin": sin, "cos": cos, "tan": tan,
            "exp": exp, "ln": log, "log": log,
            "sqrt": sqrt, "abs": abs, "pow": pow,
            "sec": sec, "csc": csc, "cot": cot,
            "ln": ln
        }

        # 4. Compile the string into a real Python function
        return eval(func_code, context)


class Symbol:
    def __init__(self, name, is_function=False):
        self.name = name
        self.is_function = is_function

    def __repr__(self):
        return self.name
    
    def simplify(self):
        return self

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

    def simplify(self):
        return VectorSymbolComponents(
            self.x.simplify(), 
            self.y.simplify(), 
            self.z.simplify()
        )

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
    
    def simplify(self):
        """Simplifies the internal expressions of the components."""
        return VectorSymbolComponents(
            self.x.simplify() if hasattr(self.x, 'simplify') else self.x,
            self.y.simplify() if hasattr(self.y, 'simplify') else self.y,
            self.z.simplify() if hasattr(self.z, 'simplify') else self.z
        )
    
symbols = SymbolFactory()