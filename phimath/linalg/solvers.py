from phimath.linalg.matrix import matrix
from phimath.math.func import sqrt

def gaussian_eleminator(A, B):
    # Ensure inputs are matrix objects
    a = A if isinstance(A, matrix) else matrix(A)
    b = B if isinstance(B, matrix) else matrix(B)
    
    n = a.rows()
    m = b.cols()

    # 1. FIX: Build the augmented matrix as a true list of lists
    # We need A (n x n) and B (n x m) combined into (n x n+m)
    augmented_data = []
    for i in range(n):
        # Accessing data[i] directly because it's a list
        row = list(a.data[i]) + list(b.data[i])
        augmented_data.append(row)
    
    aug = matrix(augmented_data)

    # 2. Forward Elimination (Row Echelon Form)
    for i in range(n):
        # Partial Pivoting: find the largest element in current column
        max_row = i
        for k in range(i + 1, n):
            if abs(aug[k, i]) > abs(aug[max_row, i]):
                max_row = k
        
        # Swap rows in the internal data
        aug.data[i], aug.data[max_row] = aug.data[max_row], aug.data[i]

        pivot = aug[i, i]
        if abs(pivot) < 1e-10: # Handle floating point near zero
            raise ValueError("Matrix is singular or nearly singular.")

        # Eliminate rows below
        for k in range(i + 1, n):
            factor = aug[k, i] / pivot
            for j in range(i, n + m):
                aug[k, j] -= factor * aug[i, j]

    # 3. Back Substitution
    # We create a result matrix for X (n x m)
    x_data = [[0.0] * m for _ in range(n)]
    res = matrix(x_data)

    for j in range(m): # Solve for each column in B
        for i in range(n - 1, -1, -1):
            sum_val = aug[i, n + j]
            for k in range(i + 1, n):
                sum_val -= aug[i, k] * res[k, j]
            res[i, j] = sum_val / aug[i, i]

    return res

def solve_linear_system(*equations):
    """
    Takes n equations as separate lists and solves the system.
    Example: solve_linear_systems([1, 1, 7], [2, -1, 2])
    Each list is: [coeff1, coeff2, ..., result]
    """
    # 1. Convert input equations into A (coefficients) and B (results)
    coeffs_data = []
    results_data = []
    
    for eq in equations:
        # The last element is the result (constant term)
        coeffs_data.append(eq[:-1])
        # We wrap the result in a list to make it a column in a 2D matrix
        results_data.append([eq[-1]])
        
    # 2. Create Matrix objects using your matrix class
    Co = matrix(coeffs_data)
    Re = matrix(results_data)
    
    # 3. Pass to the Gaussian Eliminator logic
    # (Assuming you renamed your logic or used the one we discussed)
    return gaussian_eleminator(Co, Re)

def quadratic_solver(a: float, b: float, c: float) -> tuple:
    """
    simple quadratic equation solver for equations of the form: ax^2 + bx + c = 0
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    d = b*b - 4*a*c
    root1 = (-b + sqrt(d))/(2*a) #using power operator, later will be changed to sqrt for better precision
    root2 = (-b - sqrt(d))/(2*a)
    return (root1,root2)
