from phimath.math.trigo import *
from phimath.math.constants import *

class matrix:
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

        x, y, z = axis.x, axis.y, axis.z
        rotation_matrix = matrix([
            [t*x*x + c,   t*x*y - s*z, t*x*z + s*y],
            [t*x*y + s*z, t*y*y + c,   t*y*z - s*x],
            [t*x*z - s*y, t*y*z + s*x, t*z*z + c  ]
        ])
        return rotation_matrix * self

    def __repr__(self):
        rows = [str(row) for row in self.data]
        return "\n".join(rows)
    