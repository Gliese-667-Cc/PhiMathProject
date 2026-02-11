# PhiMath

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-0.1.2-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)

**PhiMath** is a high‑precision, zero‑dependency numerical and symbolic
mathematics library for Python.

Built entirely from first principles using only the Python standard
library, PhiMath recreates core mathematical functionality commonly
provided by libraries such as NumPy, SciPy, and SymPy --- while
remaining lightweight, transparent, and physics-oriented.

The long-term vision of PhiMath is to become a mathematical engine for
computational physics, astrophysics simulations, and general relativity
research workflows.

------------------------------------------------------------------------

## Philosophy

Most scientific workflows begin with:

``` python
import numpy
```

PhiMath instead asks:

> *How does mathematics work underneath the abstraction?*

PhiMath is designed for students, researchers, and developers who want
mathematical transparency while retaining practical computational power.

The project focuses on:

-   Understanding before optimization
-   Mathematical correctness
-   Physics-oriented abstractions
-   Minimal external dependencies

------------------------------------------------------------------------

## Key Features

### ✅ Zero Dependencies

Pure Python implementation using only the standard library.

### ✅ Hybrid Numerical + Symbolic Engine

Unified interface for both numerical computation and symbolic algebra.

### ✅ Physics-Oriented Linear Algebra

Coordinate systems, active rotations, and vector operations designed
with physics workflows in mind.

### ✅ Lightweight Core

Extremely small memory footprint suitable for educational and embedded
environments.

------------------------------------------------------------------------

## Installation

### From TestPyPI

``` bash
pip install -i https://test.pypi.org/simple/ phimath
```

### From Source

``` bash
git clone https://github.com/Gliese-667-Cc/PhiMathProject.git
cd PhiMathProject
pip install .
```

------------------------------------------------------------------------

## Quick Examples

### Unified Vector API

``` python
import phimath as pm

v1 = pm.vector(1, 2, 3)
print(v1.normalize())
```

Symbolic usage:

``` python
E = pm.vector("E")
B = pm.vector("B")

print(E.dot(B))
```

------------------------------------------------------------------------

### Linear System Solver

``` python
solution = pm.solve_linear_system(eq1, eq2, eq3, eq4)
print(solution)
```

Uses Gaussian Elimination with Partial Pivoting for numerical stability.

------------------------------------------------------------------------

### ODE Solver (Runge--Kutta)

``` python
def func(t, y):
    return y - t

solution = pm.ode_solver(
    func,
    x0=0,
    y0=1,
    h=0.1,
    n=10,
    method="rk4"
)
```

------------------------------------------------------------------------

### Symbolic Differentiation

``` python
import phimath as pm

x = pm.Symbol("x")
expr = (x + 2) ** 3

print(expr.derive(x))
```

------------------------------------------------------------------------

## Performance

PhiMath prioritizes precision and clarity while maintaining efficiency.

  Metric                Result
  --------------------- --------------------
  Peak Memory           \~0.18 MB
  Numerical Precision   1e-14
  Rotation Benchmark    10k ops in \~0.55s

------------------------------------------------------------------------

## Project Roadmap

Development progresses in physics-driven stages:

-   ✅ Phase 0 --- Core Mathematics (Trig, Exp, Constants)
-   ✅ Phase 1 --- Linear Algebra & Symbolic Engine
-   🚧 Phase 2 --- Classical Mechanics (Lagrangian Solver)
-   ⏳ Phase 3 --- Electromagnetism (Maxwell Solver)
-   ⏳ Phase 4 --- General Relativity (Metric Tensor & Geodesics)

------------------------------------------------------------------------

## Architecture Overview

    PhiMath
    │
    ├── Core Math Engine
    │   ├── Trigonometry
    │   ├── Exponentials
    │   └── Constants
    │
    ├── Linear Algebra
    │   ├── Vectors
    │   ├── Matrix
    │   └── Solvers
    │
    ├── Calculas
    │   ├── Differentiation
    │   ├── Integration
    │   └── ODE Solver
    │
    ├── Symbolic Engine
    │   ├── Expressions
    │   └── Symbolic Math
    │
    └── Physics Layer (Planned)
        ├── Mechanics
        ├── Electromagnetism
        ├── Thermodynamics
        └── General Relativity

------------------------------------------------------------------------

## Contributing

Contributions and discussions are welcome.

1.  Fork the repository
2.  Create a feature branch
3.  Add tests where applicable
4.  Submit a pull request

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.\
See the `LICENSE` file for details.

------------------------------------------------------------------------

## Author

**Aditya Modi**

Mathematical Physics • Computational Physics • Astrophysics