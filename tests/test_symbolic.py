import sys
import os
import math

# Path setup for PhiMath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import phimath as pm 

def assert_equal(actual, expected, label):
    if actual == expected:
        print(f"    [PASSED] {label}")
    else:
        print(f"    [FAILED] {label} | Expected {expected}, got {actual}")

def test_algebraic_simplification():
    print("\n--- Test 1: Algebraic Simplification ---")
    x = pm.Symbol("x")
    
    # Test Identity: x * 1 + 0 -> x
    expr = (x * 1) + 0
    simplified = expr.simplify()
    assert_equal(str(simplified), "x", "Identity Simplification")

    # Test Constant Folding: (2 + 3) * x -> 5 * x
    expr_fold = (2 + 3) * x
    assert_equal(str(expr_fold.simplify()), "(5 * x)", "Constant Folding")

def test_calculus_chain_rule():
    print("\n--- Test 2: Calculus & Chain Rule ---")
    x = pm.Symbol("x")
    
    # Test: d/dx (x^2 + 2x) -> 2*x + 2
    # Without simplify, this is a mess; with simplify, it's clean
    expr = (x ** 2) + (2 * x)
    deriv = expr.derive(x).simplify()
    
    # Value check at x = 5: 2(5) + 2 = 12
    val = deriv.evaluate({"x": 5})
    assert_equal(val, 12, "Polynomial Derivative at x=5")
    
    # Test: d/dx (sin(x)) -> cos(x)
    # Note: Requires pm.sin to be implemented or handled via symbols
    # Assuming pm.sin(x) returns an Expression with op="sin"
    try:
        s_expr = pm.sin(x)
        d_s_expr = s_expr.derive(x).simplify()
        # Evaluate: cos(0) = 1
        assert_equal(d_s_expr.evaluate({"x": 0}), 1.0, "Trig Derivative (sin->cos)")
    except AttributeError:
        print("    [SKIP] Trig functions not fully exposed in pm namespace yet.")

def test_vector_calculus():
    print("\n--- Test 3: Vector Symbolic Identities ---")
    # In Astrophysics, checking if B . (E x B) == 0 is fundamental
    E = pm.vector("E")
    B = pm.vector("B")
    
    # Triple product identity: B dot (E cross B) should always be 0
    cross = E.cross(B)
    triple_dot = B.dot(cross)
    
    # Test with arbitrary values
    ctx = {
        "E_x": 1.2, "E_y": -3.4, "E_z": 0.5,
        "B_x": 0.1, "B_y": 2.2, "B_z": 9.8
    }
    
    val = triple_dot.evaluate(ctx)
    # Using math.isclose for floating point precision
    is_zero = math.isclose(val, 0, abs_tol=1e-9)
    assert_equal(is_zero, True, "Vector Identity: B · (E × B) == 0")

def test_multivariable_numeric_gen():
    print("\n--- Test 4: Multivariable & Numeric Generation ---")
    x = pm.Symbol("x")
    y = pm.Symbol("y")
    
    # f(x, y) = x^2 * sin(y)
    expr = (x ** 2) * pm.sin(y)
    print(f"    Expression: {expr}")
    
    # 1. Symbolic Partial Derivative: df/dx = 2 * x * sin(y)
    df_dx = expr.derive(x).simplify()
    print(f"    df/dx: {df_dx}")
    
    # 2. Generate Numeric Function
    # We expect f(x, y) = 2 * x * sin(y)
    f_numeric = df_dx.to_numeric("x", "y")
    
    # 3. Evaluate at x=5, y=pi/2
    # Result should be 2 * 5 * sin(pi/2) = 10 * 1 = 10
    val = f_numeric(5, pm.HALF_PI)
    print(f"    Numerical Evaluation at (x=5, y=π/2): {val}")
    
    # Check with tolerance for float precision
    if math.isclose(val, 10.0, abs_tol=1e-9):
        print("    -> PASSED")
    else:
        print(f"    -> FAILED (Expected 10.0, got {val})")

# Don't forget to call it in run_all_tests()!

def run_all_tests():
    print("========================================")
    print("      PHIMATH SYMBOLIC ENGINE V2        ")
    print("========================================")
    
    test_algebraic_simplification()
    test_calculus_chain_rule()
    test_vector_calculus()
    test_multivariable_numeric_gen()
    
    print("\n========================================")
    print("            TESTING COMPLETE            ")
    print("========================================")

if __name__ == "__main__":
    run_all_tests()