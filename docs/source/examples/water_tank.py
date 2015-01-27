from gpkit import Variable, VectorVariable, GP
M   = Variable("M", 100, "kg", "Mass of Water in the Tank")
rho = Variable("\\rho", 1000, "kg/m^3", "Density of Water in the Tank")
A   = Variable("A", "m^2", "Surface Area of the Tank")
V   = Variable("V", "m^3", "Volume of the Tank")
d   = VectorVariable(3, "d", "m", "Dimension Vector")

constraints = (A >= 2*(d[0]*d[1] + d[0]*d[2] + d[1]*d[2]),
               V == d[0]*d[1]*d[2],
               M == V*rho
               )

gp = GP(A, constraints)
sol = gp.solve(printing=False)
print sol(A)
print sol(V)
print sol(d)