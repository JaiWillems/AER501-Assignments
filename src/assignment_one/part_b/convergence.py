import matplotlib.pyplot as plt

from src.assignment_one.part_b.solver.rbf_collocation_solver import \
    RbfCollocationSolver
from src.assignment_one.part_b.solver.utils import collocation_solutions, \
    linearly_spaced_points, actual_solution, calculate_l2_error

NUMBER_OF_COLLOCATION_POINTS = linearly_spaced_points([2, 30], 29)
DOMAIN = [0, 1]
NUMBER_OF_X_VALS = 100

step_size = []
gaussian_error = []
multiquadratic_error = []

for n in NUMBER_OF_COLLOCATION_POINTS:
    gaussian_solution, multiquadratic_solution = collocation_solutions(
        DOMAIN,
        int(n)
    )
    x = linearly_spaced_points(DOMAIN, NUMBER_OF_X_VALS)

    gaussian_y = gaussian_solution.evaluate(x)
    multiquadratic_y = multiquadratic_solution.evaluate(x)
    actual_y = actual_solution(x)

    step_size.append(RbfCollocationSolver.step_size(DOMAIN, n))
    gaussian_error.append(calculate_l2_error(gaussian_y, actual_y))
    multiquadratic_error.append(calculate_l2_error(multiquadratic_y, actual_y))

plt.plot(step_size, gaussian_error, label="Gaussian RBF")
plt.plot(step_size, multiquadratic_error, label="Multiquadratic RBF")
plt.title("Convergence")
plt.xlabel("Step Size")
plt.ylabel("L2 Norm of Approximation Error")
plt.legend()
plt.grid()
plt.show()

