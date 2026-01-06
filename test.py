import phimath as pm

E = pm.E
PI = pm.PI

a=pm.vector(3,60,30, mode="polar")
b=pm.vector(1,2,0, mode=None)

c= pm.matrix([[1,2,3],[4,5,6]])
d= pm.matrix([[7,8,9],[10,11,12]])

print(PI, E)
print(pm.sin(PI/2.0))

print(pm.exp(0))          # 1.0
print(pm.exp(1))          # ≈ 2.71828
print(pm.ln(pm.E))   # ≈ 1.0
print(pm.log(100, 10))    # ≈ 2.0
print(pm.exp(pm.ln(5)))  # ≈ 5.0
print(b * 6)        
print (c + d)
print (PI+2)

a = [1,1,7]
b=[2,-1,2]
print(pm.solve_linear_system(a,b))