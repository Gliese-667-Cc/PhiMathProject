import phimath as pm

E = pm.E
PI = pm.PI
a=pm.vector(3,60,30, mode="polar")                      # vector a in polar coordinates
b=pm.vector(1,2,0, mode=None)                           # vector b in Cartesian coordinates
c= pm.matrix([[1,2,3],[4,5,6]])                         # 2x3 Matrix c
d= pm.matrix([[7,8,9],[10,11,12]])                      # 2x3 Matrix b
print(PI, E)                                            # Print constants
print(pm.sin(PI/2.0))                                   # ≈ 1.0
print(pm.exp(0))                                        # ≈ 1.0
print(pm.exp(1))                                        # ≈ 2.71828
print(pm.ln(pm.E))                                      # ≈ 1.0
print(pm.log(100, 10))                                  # ≈ 2.0
print(pm.exp(pm.ln(5)))                                 # ≈ 5.0
print(b * 6)                                            # Scalar multiplication
print (c + d)                                           # Matrix addition
print (a + b)                                           # Vector addition
print (a.dot(b))                                        # Dot product
a = [1,1,7]                                             # Coefficients of equations 1
b=[2,-1,2]                                              # Coefficients of equations 2
print(pm.solve_linear_system(a,b))                      # Solve linear equations    
print(pm.quadratic_solver(1,-3,2))                      # Solve quadratic equations
print(pm.quadratic_solver(1,2,5))                       # Solve quadratic equations with complex roots