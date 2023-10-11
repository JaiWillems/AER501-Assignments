import matplotlib.pyplot as plt

from src.assignment_one.part_b.solver.utils import \
    collocation_solutions, linearly_spaced_points, actual_solution

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
actual_y = actual_solution(x)

plt.plot(x, gaussian_y, label="Gaussian RBF")
plt.plot(x, multiquadratic_y, label="Multiquadratic RBF")
plt.plot(x, actual_y, label="Actual Solution")
plt.title(f"Problem Solutions (n={NUMBER_OF_COLLOCATION_POINTS})")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
