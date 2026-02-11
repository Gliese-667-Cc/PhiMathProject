import sys
import os

# Get the path to the parent directory (one level up)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import phimath as pm

def assert_close(val1, val2, tolerance=1e-10, name="Check"):
    diff = abs(val1 - val2)
    status = "PASSED" if diff < tolerance else "FAILED"
    print(f"[{status}] {name}: |{val1} - {val2}| = {diff:.2e}")
    if status == "FAILED":
        return False
    return True

def run_precision_test():
    print("========================================")
    print("   PHIMATH NUMERICAL PRECISION SUITE    ")
    print("========================================")

    # 1. Constants
    print("\n--- Fundamental Constants ---")
    assert_close(pm.PI, 3.141592653589793, name="PI Accuracy")
    assert_close(pm.E, 2.718281828459045, name="Euler's Constant")

    # 2. Transcendental Functions
    print("\n--- Transcendental Identities ---")
    # Identity: exp(ln(x)) == x
    val = 123.456
    res = pm.exp(pm.ln(val))
    assert_close(res, val, name=f"exp(ln({val})) Identity")

    # Identity: sin^2 + cos^2 == 1
    angle = pm.PI / 6 # 30 degrees
    trig_id = pm.sin(angle)**2 + pm.cos(angle)**2
    assert_close(trig_id, 1.0, name="sin^2 + cos^2 == 1")

    # 3. Vector Normalization
    print("\n--- Linear Algebra Precision ---")
    v = pm.vector(3, 4, 0)
    v_norm = v.normalize()
    mag = v_norm.magnitude()
    assert_close(mag, 1.0, name="Unit Vector Magnitude")

    # 4. Matrix Inversion / Solver
    # Solve Ax = B where answer is known
    # 2x + y = 5 -> x=2, y=1
    coeffs = [2, 1, 5]
    eq2 = [1, -1, 1]
    sol = pm.solve_linear_system(coeffs, eq2)
    
    x_calc = sol[0, 0]
    y_calc = sol[1, 0]
    assert_close(x_calc, 2.0, name="Gaussian Solver X")
    assert_close(y_calc, 1.0, name="Gaussian Solver Y")

if __name__ == "__main__":
    run_precision_test()