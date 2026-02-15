from array import array
from phimath.math.trigo import sin, cos
from phimath.math.constants import DEG_TO_RAD
from phimath.control.symbols import *

class vector:
    def __new__(cls, x=None, y=None, z=None, mode=None):
        is_symbolic = isinstance(x, str) or \
                      (hasattr(x, 'name') and hasattr(x, 'is_function')) or \
                      (isinstance(x, (list, tuple)) and any(hasattr(i, 'name') for i in x if i is not None))

        if is_symbolic:
            from phimath.control.symbols import VectorSymbol
            return VectorSymbol(x)
        
        return super(vector, cls).__new__(cls)
    
    def __init__(self, x=None, y=None, z=None, mode=None):
        # 'd' denotes double-precision floats (8 bytes) for high-precision mechanics
        self.data = array('d', [0.0, 0.0, 0.0])
        
        mode = mode.lower() if mode else None
        if mode == 'polar' or mode == 'spherical':
            r_val = float(x) if x is not None else 0.0
            theta = float(y) if y is not None else 0.0
            phi = float(z) if z is not None else 0.0
            
            self.data[0] = r_val * cos(DEG_TO_RAD * phi) * cos(DEG_TO_RAD * theta)
            self.data[1] = r_val * sin(DEG_TO_RAD * theta) * cos(DEG_TO_RAD * phi)
            self.data[2] = r_val * sin(DEG_TO_RAD * phi)
        else:
            self.data[0] = float(x) if x is not None else 0.0
            self.data[1] = float(y) if y is not None else 0.0
            self.data[2] = float(z) if z is not None else 0.0

    # Properties to maintain existing p.r.x syntax while using array storage
    @property
    def x(self): return self.data[0]
    @x.setter
    def x(self, value): self.data[0] = float(value)

    @property
    def y(self): return self.data[1]
    @y.setter
    def y(self, value): self.data[1] = float(value)

    @property
    def z(self): return self.data[2]
    @z.setter
    def z(self, value): self.data[2] = float(value)

    def __add__(self, other):
        return vector(self.data[0] + other.x, self.data[1] + other.y, self.data[2] + other.z)

    def __sub__(self, other):
        return vector(self.data[0] - other.x, self.data[1] - other.y, self.data[2] - other.z)

    def __mul__(self, scalar):
        return vector(self.data[0] * scalar, self.data[1] * scalar, self.data[2] * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        return vector(self.data[0] / scalar, self.data[1] / scalar, self.data[2] / scalar)
    
    def dot(self, other):
        return self.data[0] * other.x + self.data[1] * other.y + self.data[2] * other.z

    def cross(self, other):
        return vector(
            self.data[1] * other.z - self.data[2] * other.y,
            self.data[2] * other.x - self.data[0] * other.z,
            self.data[0] * other.y - self.data[1] * other.x
        )
    
    def magnitude(self):
        # Local variable access is faster than repeated property calls
        x, y, z = self.data
        return (x**2 + y**2 + z**2)**0.5
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return vector(0.0, 0.0, 0.0)
        return self.__truediv__(mag)
    
    def __repr__(self):
        return f"vector({self.data[0]}, {self.data[1]}, {self.data[2]})"