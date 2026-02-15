from phimath.linalg.vectors import vector
from phimath.calculas.differentiate import differentiate

class VectorOps:
    """
    Numerical engine for Vector Calculus: Gradient, Divergence, and Curl.
    """
    def __init__(self, h=1e-5):
        self.h = h

    def gradient(self, scalar_field, point: vector):
        """Calculates the Gradient (grad f or ∇f) of a scalar field."""
        def f_x(x): return scalar_field(vector(x, point.y, point.z))
        def f_y(y): return scalar_field(vector(point.x, y, point.z))
        def f_z(z): return scalar_field(vector(point.x, point.y, z))

        gx = differentiate(f_x, point.x, self.h)
        gy = differentiate(f_y, point.y, self.h)
        gz = differentiate(f_z, point.z, self.h)
        return vector(gx, gy, gz)

    def divergence(self, vector_field, point: vector):
        """Calculates the Divergence (div F or ∇·F) of a vector field."""
        # F_x component relative to x, F_y to y, etc.
        def div_x(x): return vector_field(vector(x, point.y, point.z)).x
        def div_y(y): return vector_field(vector(point.x, y, point.z)).y
        def div_z(z): return vector_field(vector(point.x, point.y, z)).z

        return (differentiate(div_x, point.x, self.h) + 
                differentiate(div_y, point.y, self.h) + 
                differentiate(div_z, point.z, self.h))

    def curl(self, vector_field, point: vector):
        """Calculates the Curl (rot F or ∇×F) of a vector field."""
        # Component functions for partial derivatives
        def Fx_y(y): return vector_field(vector(point.x, y, point.z)).x
        def Fx_z(z): return vector_field(vector(point.x, point.y, z)).x
        
        def Fy_x(x): return vector_field(vector(x, point.y, point.z)).y
        def Fy_z(z): return vector_field(vector(point.x, point.y, z)).y
        
        def Fz_x(x): return vector_field(vector(x, point.y, point.z)).z
        def Fz_y(y): return vector_field(vector(point.x, y, point.z)).z

        # Curl components: (dFz/dy - dFy/dz)i + (dFx/dz - dFz/dx)j + (dFy/dx - dFx/dy)k
        cx = differentiate(Fz_y, point.y, self.h) - differentiate(Fy_z, point.z, self.h)
        cy = differentiate(Fx_z, point.z, self.h) - differentiate(Fz_x, point.x, self.h)
        cz = differentiate(Fy_x, point.x, self.h) - differentiate(Fx_y, point.y, self.h)
        
        return vector(cx, cy, cz)
    
class VectorField:
    """Represents a physical vector field"""
    def __init__(self, field_func):
        self.field = field_func
        self.ops = VectorOps()

    def value_at(self, point: vector):
        return self.field(point)

    def is_conservative(self, point: vector):
        """A field is conservative if its curl is zero."""
        curl_val = self.ops.curl(self.field, point)
        return curl_val.magnitude() < 1e-7