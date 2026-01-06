# PhiMath: 

A Computational Physics & Mathematics LibraryPhiMath is a modular Python library designed for high-precision mathematical computations and physics simulations. Built with a focus on numerical stability and future portability to C/C++, it implements core mathematical functions, linear algebra structures, and systems solvers from the ground up. 

# Current Status: 
Core Engine CompleteThe library currently features a fully functional mathematical and linear algebra core, capable of handling complex vector calculus and systems of linear equations.

# Project Structure:
1. phimath/math/: Custom implementations of constants (pi ,e), trigonometry, and logarithmic functions using iterative series.
2. phimath/linalg/: High-level vector and matrix classes with support for operator overloading and coordinate transformations.
3. phimath/linalg/solvers.py: Robust equation solvers including Gaussian Elimination with partial pivoting and Quadratic solvers handling complex roots.

# Key Features:
1. Advanced Linear AlgebraVector Operations: Supports rectangular and polar coordinate systems. Includes magnitude, normalization, and scalar multiplication.Matrix Logic: Implements matrix addition, subtraction, multiplication, and transposition.Dunder Methods: Full support for Python magic methods (__add__, __mul__, __repr__, etc.) for an intuitive, math-like syntax.
2. Robust Systems SolverLinear Systems: Solves $Ax = B$ using Gaussian Elimination with partial pivoting to ensure numerical stability.Quadratic Solver: Handles real and complex roots, providing clean string formatting for imaginary units ($i$).Flexible Input: The solve_linear_systems function accepts individual equation lists for ease of use.
3. Custom Math ImplementationsHand-built sin, cos, exp, ln, and log functions to reduce dependency on external libraries and prepare for low-level C porting.High-precision constants (15 decimal places). 

# Usage Example 

import phimath as pm
# Vector in Polar Coordinates (magnitude, theta, phi)
v1 = pm.vector(10, 45, 0, mode="polar")
# Solving a Linear System: 
# x + y = 7
# 2x - y = 2
solution = pm.solve_linear_systems([1, 1, 7], [2, -1, 2])
print(solution)  # Output: [[3.0], [4.0]]
# Solving a Quadratic: x^2 - 3x + 2 = 0
roots = pm.quadratic_solver(1, -3, 2)
print(roots)  # Output: (2.0, 1.0)

# Roadmap:
Mechanics: Projectile motion and dynamics simulations.
Electromagnetism: Field calculations and Lorentz force vectors.
Relativity: Lorentz transformations and Schwarzschild radius calculations.
