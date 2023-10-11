import math

import matplotlib.pyplot as plt

from src.assignment_one.part_b.solver.utils import \
    collocation_solutions, linearly_spaced_points

NUMBER_OF_COLLOCATION_POINTS = 4
DOMAIN = [0, 1]
NUMBER_OF_X_VALS = 100

gaussian_solution, multiquadratic_solution = collocation_solutions(
    DOMAIN,
    NUMBER_OF_COLLOCATION_POINTS
)

x = linearly_spaced_points(DOMAIN, NUMBER_OF_X_VALS)
gaussian_y = gaussian_solution.evaluate(x)
multiquadratic_y = multiquadratic_solution.evaluate(x)
actual_y = [0.8509 * math.sinh(xi) - xi for xi in x]

plt.plot(x, gaussian_y, label="Gaussian RBF")
plt.plot(x, multiquadratic_y, label="Multiquadratic RBF")
plt.plot(x, actual_y, label="Actual Solution")
plt.title("Problem Solutions")
plt.legend()
plt.grid()
plt.show()
