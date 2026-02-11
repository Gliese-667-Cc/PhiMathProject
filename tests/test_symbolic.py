import sys
import os

# Get the path to the parent directory (one level up)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import phimath as pm 

def run_symbolic_test():
    print("========================================")
    print("   PHIMATH SYMBOLIC ENGINE TEST         ")
    print("========================================")

    # 1. Symbolic Algebra
    print("\n[1] Algebraic Expansion & Evaluation")
    x = pm.Symbol("x")
    expr = (x + 2) ** 2
    print(f"    Expression: {expr}")
    
    # Evaluate at x=3 -> (3+2)^2 = 25
    ctx = {"x": 3}
    res = expr.evaluate(ctx)
    print(f"    Evaluate (x=3): {res}")
    
    if res == 25: print("    -> PASSED")
    else: print(f"    -> FAILED (Expected 25, got {res})")

    # 2. Calculus (Differentiation)
    print("\n[2] Symbolic Differentiation")
    # d/dx (x^3) -> 3*x^2
    y = pm.Symbol("y")
    expr_poly = y ** 3
    deriv = expr_poly.derive(y)
    print(f"    d/dy ({expr_poly}): {deriv}")
    
    # Check value at y=2 -> 3*(2^2) = 12
    ctx_y = {"y": 2}
    deriv_val = deriv.evaluate(ctx_y)
    print(f"    Value at y=2: {deriv_val}")
    
    if deriv_val == 12: print("    -> PASSED")
    else: print(f"    -> FAILED (Expected 12, got {deriv_val})")

    # 3. Vector Symbols (The Hybrid Engine)
    print("\n[3] Vector Symbolic Logic")
    try:
        # Create symbolic vectors using the unified pm.vector() API
        E = pm.vector("E")
        B = pm.vector("B")
        print(f"    Created Symbolic Vector: {E}")
        
        # Test Dot Product Logic
        # E . B
        dot_expr = E.dot(B)
        print(f"    Symbolic Dot: {dot_expr}")
        
        # Verify Orthogonality
        # E=(1,0,0), B=(0,1,0) -> Dot should be 0
        ctx_vec = {
            "E_x": 1, "E_y": 0, "E_z": 0,
            "B_x": 0, "B_y": 1, "B_z": 0
        }
        val = dot_expr.evaluate(ctx_vec)
        print(f"    Orthogonality Check: {val}")
        
        if val == 0: print("    -> PASSED")
        else: print(f"    -> FAILED (Expected 0)")
        
    except Exception as e:
        print(f"    -> CRITICAL FAIL: {e}")

if __name__ == "__main__":
    run_symbolic_test()