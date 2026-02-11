from matplotlib.pylab import angle
from phimath.math.trigo import *
from phimath.math.constants import *


class matrix:

    __slots__ = ['data', '_rows', '_cols']

    def __init__(self, data):
        self.data = data

    def __getitem__(self, idx):
        i, j = idx
        return self.data[i][j]

    def __setitem__(self, idx, value):
        i, j = idx
        self.data[i][j] = value

    def shape(self):
        return len(self.data), len(self.data[0]) if self.data else 0
    
    def rows(self):
        return self.shape()[0]
    
    def cols(self):
        return self.shape()[1]

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ValueError("Matrices must have the same dimensions to add.")
        result = [
            [
                self.data[i][j] + other.data[i][j]
                for j in range(self.shape()[1])
            ]
            for i in range(self.shape()[0])
        ]
        return matrix(result)

    def __sub__(self, other):
        if self.shape() != other.shape():
            raise ValueError("Matrices must have the same dimensions to subtract.")
        result = [
            [
                self.data[i][j] - other.data[i][j]
                for j in range(self.shape()[1])
            ]
            for i in range(self.shape()[0])
        ]
        return matrix(result)

    def __mul__(self, other):
        if self.shape()[1] != other.shape()[0]:
            raise ValueError("Incompatible dimensions for matrix multiplication.")
        result = [
            [
                sum(
                    self.data[i][k] * other.data[k][j]
                    for k in range(self.shape()[1])
                )
                for j in range(other.shape()[1])
            ]
            for i in range(self.shape()[0])
        ]
        return matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(self.shape()[0])]
            for i in range(self.shape()[1])
        ]
        return matrix(result)
    
    def determinant(self):
        if self.shape()[0] != self.shape()[1]:
            raise ValueError("Determinant is only defined for square matrices.")
        n = self.shape()[0]
        if n == 1:
            return self.data[0][0]
        if n == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        for c in range(n):
            minor = matrix([
                [self.data[i][j] for j in range(n) if j != c]
                for i in range(1, n)
            ])
            det += ((-1) ** c) * self.data[0][c] * minor.determinant()
        return det
    
    def rotate(self, angle, axis):
        c = cos(angle)
        s = sin(angle)
        t = 1 - c
                # Ensure axis is normalized for consistent rotation
        axis = axis.normalize() 
        x, y, z = axis.x, axis.y, axis.z
                # Standard Rodriguez Rotation Formula (Active / Right-Hand Rule)
        rotation_matrix = matrix([
            [t*x*x + c,   t*x*y - s*z, t*x*z + s*y], 
            [t*x*y + s*z, t*y*y + c,   t*y*z - s*x],
            [-t*x*z + s*y, t*y*z + s*x, t*z*z + c ] # Note the sign changes here
        ])
        return rotation_matrix * self

    def __repr__(self):
        rows = [str(row) for row in self.data]
        return "\n".join(rows)
    
    def solve(self, b):
        from phimath.linalg.solvers import gaussian_eleminator
    # 1. If 'b' is a list [1, 2, 3], turn it into a Column Matrix [[1], [2], [3]]
        if isinstance(b, list):
            b = matrix([[val] for val in b])

        # 2. If 'b' is your custom Vector object, extract its components into a Column Matrix
        elif hasattr(b, 'x'): # Checking if it's a Vector(x, y, z)
            b = matrix([[b.x], [b.y], [b.z]])

        # Now gaussian_eleminator gets two Matrix objects: (N x N) and (N x 1)
        return gaussian_eleminator(self, b)
    
    def lu_decomposition(A):
        """
        Performs LU Decomposition of matrix A.
        Returns matrices L and U such that A = LU.
        """
        n = A.rows()
        L = matrix([[0 if i != j else 1 for j in range(n)] for i in range(n)])
        U = matrix([[0 for _ in range(n)] for _ in range(n)])
    
        for i in range(n):
            for j in range(i, n):
                U[i, j] = A[i, j]
                for k in range(i):
                    U[i, j] -= L[i, k] * U[k, j]
            for j in range(i + 1, n):
                L[j, i] = A[j, i]
                for k in range(i):
                    L[j, i] -= L[j, k] * U[k, i]
                L[j, i] /= U[i, i]
    
        return L, U