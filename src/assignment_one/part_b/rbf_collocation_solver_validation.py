import math

import matplotlib.pyplot as plt

from src.assignment_one.part_b.rbf_functions.gaussian_rbf import GaussianRbf
from src.assignment_one.part_b.rbf_functions.multiquadratic_rbf import \
    MultiquadraticRbf
from src.assignment_one.part_b.solver.rbf_collocation_solver import \
    RbfCollocationSolver

NUMBER_OF_COLLOCATION_POINTS = 15
DOMAIN = [0, 1]
NUMBER_OF_X_VALS = 100

sigma = 2.2 * RbfCollocationSolver.step_size(
    DOMAIN,
    NUMBER_OF_COLLOCATION_POINTS
)
gaussian_solution = RbfCollocationSolver.solve_with_homogenous_dirichlet(
    DOMAIN,
    NUMBER_OF_COLLOCATION_POINTS,
    GaussianRbf(),
    sigma
)
multiquadratic_solution = RbfCollocationSolver.solve_with_homogenous_dirichlet(
    DOMAIN,
    NUMBER_OF_COLLOCATION_POINTS,
    MultiquadraticRbf(),
    sigma
)

evaluation_step_size = RbfCollocationSolver.step_size(DOMAIN, NUMBER_OF_X_VALS)
x = [i * evaluation_step_size for i in range(NUMBER_OF_X_VALS)]

gaussian_y = gaussian_solution.evaluate(x)
multiquadratic_y = multiquadratic_solution.evaluate(x)
actual_y = [0.8509 * math.sinh(xi) - xi for xi in x]

plt.plot(x, gaussian_y, label="Gaussian RBF")
plt.plot(x, multiquadratic_y, label="Multiquadratic RBF")
plt.plot(x, actual_y, label="Actual Solution")
plt.legend()
plt.grid()
plt.show()