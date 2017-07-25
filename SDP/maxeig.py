from cvxpy import *
import numpy as np

t = Variable()

A_1 = np.random.rand(2,2)
A = (A_1 + A_1.transpose())/2

objective = Minimize(t)
constraints = [t*np.identity(2) - A >> 0]
prob = Problem(objective, constraints)
prob.solve()
print "status:", prob.status
print "optimal value", prob.value
print "A matrix:", A
print np.linalg.eig(A)