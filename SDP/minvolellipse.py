from cvxpy import *
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import ConvexHull

A = Semidef(2)
b = Variable(2)

x_1 = np.array([0.55, 0.7])
x_2 = np.array([0.25, 0.35])
x_3 = np.array([-0.25, -0.9])
x_4 = np.array([-0.2, 0.2])
X = np.vstack([x_1, x_2, x_3, x_4])

objective = Maximize(log_det(A))
constraints = [norm(A*x_1 + b, 2) <= 1, norm(A * x_2 + b, 2) <= 1,
 norm(A * x_3 + b, 2) <= 1, norm(A * x_4 + b, 2) <= 1]
prob = Problem(objective, constraints)
prob.solve()
print "status:", prob.status
print "optimal value", prob.value
print "A", A.value
print "b", b.value

numangles = 200
angles = np.linspace(0, 2*np.pi, numangles)
t = np.array([np.cos(angles) - b.value[0], np.sin(angles)-b.value[1]]).reshape(2,200)
ellipse = np.linalg.solve(A.value, t)

plt.plot(X[:,0], X[:,1], 'o')
plt.ylim(-1, 1)
plt.plot(ellipse[0,:].transpose(), ellipse[1,:].transpose(), 'r')
plt.show()


