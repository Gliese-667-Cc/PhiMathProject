import phimath as pm

E = pm.E
PI = pm.PI
a=pm.vector(3,60,30, mode="polar")                      # vector a in polar coordinates
b=pm.vector(1,2,0, mode=None)                           # vector b in Cartesian coordinates
c= pm.matrix([[1,2,3],[4,5,6],[12,41,36]])                         # 2x3 Matrix c
d= pm.matrix([[7,8,9],[10,11,12],[12,46,78]])
e = d.rotate(PI/2, pm.vector(0,1,0))                    # Rotate matrix d by 90 degrees around z-axis
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
e = [2, 3, -1, 4, 25]                                   # Coefficients of equations 1
f = [1, 5, 2, -1, 14] 
g = [3, -1, 4, 2, 22]   
h = [4, 2, -3, 1, 11]      
equations = pm.matrix([[2, 3, -1, 4],
             [1, 5, 2, -1],
             [3, -1, 4, 2],
             [4, 2, -3, 1]])  
re = [25, 14, 22, 11]                                               
print(pm.solve_linear_system(e,f,g,h))                      # Solve linear equations    
print(pm.quadratic_solver(1,-3,2))                      # Solve quadratic equations
print(pm.quadratic_solver(1,2,5))                       # Solve quadratic equations with complex roots
print(equations.solve(re))
print(type(a))