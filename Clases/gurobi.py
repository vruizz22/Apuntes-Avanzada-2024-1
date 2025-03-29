from gurobipy import Model, GRB

m = Model("ejemplo")

x = m.addVar(name="x")

# printear el modelo

m.update()

m.setObjective(x, GRB.MAXIMIZE)

m.optimize()

print(x.x)
