import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import phimath as pm

def run_performance_test():
    print("========================================")
    print("   PHIMATH MEMORY & STRESS TEST         ")
    print("========================================")
    
    tracemalloc.start()
    start_time = time.time()

    # 1. Matrix Stress Test
    print("\n[1] Allocating 1,000 Vectors...")
    vectors = []
    for i in range(1000):
        # Create vectors with varying data
        vectors.append(pm.vector(i, i+1, i+2))
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"    - Vectors Created.")
    print(f"    - Current RAM: {current / 1024:.2f} KB")

    # 2. Heavy Computation (Matrix Rotation Loop)
    print("\n[2] Performing 10,000 Matrix Rotations...")
    base_matrix = pm.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    axis = pm.vector(0, 1, 0)
    angle = 0.01
    
    # Rotate the matrix cumulatively
    temp_mat = base_matrix
    for _ in range(10000):
        temp_mat = temp_mat.rotate(angle, axis)
        
    end_time = time.time()
    
    # 3. Final Report
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print("\n" + "-"*40)
    print(f"FINAL METRICS:")
    print(f"Execution Time: {end_time - start_time:.4f} sec")
    print(f"Peak Memory:    {peak / (1024*1024):.6f} MB")
    print("-"*40)
    
    if (peak / (1024*1024)) < 1.0:
        print("RESULT: PASSED (Under 1 MB Limit)")
    else:
        print("RESULT: WARNING (Exceeded 1 MB Target)")

if __name__ == "__main__":
    run_performance_test()