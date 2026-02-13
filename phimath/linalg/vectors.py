from phimath.math.trigo import *
from phimath.math.constants import *
from phimath.control.symbols import *

class vector:
   
    def __new__(cls, x=None, y=None, z=None, mode=None):
        # Check if input is a string (e.g., vector("E")) or contains Symbols
        is_symbolic = isinstance(x, str) or \
                      (hasattr(x, 'name') and hasattr(x, 'is_function')) or \
                      (isinstance(x, (list, tuple)) and any(hasattr(i, 'name') for i in x if i is not None))

        if is_symbolic:
            # Lazy Import to avoid Circular Dependency errors
            from phimath.control.symbols import VectorSymbol
            # Delegate to the Symbolic backend
            return VectorSymbol(x)
        
        # Otherwise, create a standard efficient Numerical vector
        return super(vector, cls).__new__(cls)
    
    def __init__ (self,x=None,y=None,z=None,mode=None):
        self.mode = mode.lower() if mode else None
        if self.mode == 'polar' or self.mode == 'spherical':
            if z is None:
                z=0.0
            if x is not None and y is not None:
                self.x = x * cos(DEG_TO_RAD*z) * cos(DEG_TO_RAD*y) 
                self.y = x * sin(DEG_TO_RAD*y) * cos(DEG_TO_RAD*z)
                self.z = x * sin(DEG_TO_RAD*z)
        else:
            self.x = x if x is not None else 0.0
            self.y = y if y is not None else 0.0
            self.z = z if z is not None else 0.0

    def __add__(self,other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self,other):
        return vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self,scalar):
        return vector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __rmul__(self,scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self,scalar):
        return vector(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def dot(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self,other):
        return vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return vector(0.0, 0.0, 0.0)
        return vector(self.x / mag, self.y / mag, self.z / mag)
    
    def __repr__(self):
        return f"vector({self.x}, {self.y}, {self.z})"
    