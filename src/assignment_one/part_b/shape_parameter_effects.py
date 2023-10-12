import matplotlib.pyplot as plt

from src.assignment_one.part_b.solver.utils import collocation_solutions, \
    linearly_spaced_points, actual_solution, calculate_l2_error

NUMBER_OF_COLLOCATION_POINTS = 4
SHAPE_PARAMETERS = linearly_spaced_points([1e-5, 0.1], 100)
DOMAIN = [0, 1]
NUMBER_OF_X_VALS = 100

gaussian_error = []
multiquadratic_error = []

for sigma in SHAPE_PARAMETERS:
    gaussian_solution, multiquadratic_solution = collocation_solutions(
        DOMAIN,
        NUMBER_OF_COLLOCATION_POINTS,
        sigma=sigma
    )
    x = linearly_spaced_points(DOMAIN, NUMBER_OF_X_VALS)

    gaussian_y = gaussian_solution.evaluate(x)
    multiquadratic_y = multiquadratic_solution.evaluate(x)
    actual_y = actual_solution(x)

    gaussian_error.append(calculate_l2_error(gaussian_y, actual_y))
    multiquadratic_error.append(calculate_l2_error(multiquadratic_y, actual_y))

plt.plot(SHAPE_PARAMETERS, gaussian_error, label="Gaussian RBF")
plt.plot(SHAPE_PARAMETERS, multiquadratic_error, label="Multiquadratic RBF")
plt.title("Approximation Error and Shape Parameter Relationship")
plt.xlabel("Shape Parameter")
plt.ylabel("L2 Norm of Approximation Error")
plt.legend()
plt.grid()
plt.show()
