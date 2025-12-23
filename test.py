import phimath as pm

E = pm.E
PI = pm.PI
print(PI, E)
print(pm.sin(PI/2.0))

print(pm.exp(0))          # 1.0
print(pm.exp(1))          # ≈ 2.71828
print(pm.ln(pm.E))   # ≈ 1.0
print(pm.log(100, 10))    # ≈ 2.0
print(pm.exp(pm.ln(5)))  # ≈ 5.0