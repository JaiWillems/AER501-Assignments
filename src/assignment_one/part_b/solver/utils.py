from src.assignment_one.part_b.rbf_functions.gaussian_rbf import GaussianRbf
from src.assignment_one.part_b.rbf_functions.multiquadratic_rbf import \
    MultiquadraticRbf
from src.assignment_one.part_b.solver.rbf_collocation_solver import \
    RbfCollocationSolver


def collocation_solutions(domain, number_of_collocation_points):
    sigma = 2.2 * RbfCollocationSolver.step_size(
        domain,
        number_of_collocation_points
    )
    gaussian_solution = RbfCollocationSolver.solve_with_homogenous_dirichlet(
        domain,
        number_of_collocation_points,
        GaussianRbf(),
        sigma
    )
    multiquadratic_solution = RbfCollocationSolver.solve_with_homogenous_dirichlet(
        domain,
        number_of_collocation_points,
        MultiquadraticRbf(),
        sigma
    )
    return gaussian_solution, multiquadratic_solution


def linearly_spaced_points(domain, number_of_points):
    step_size = RbfCollocationSolver.step_size(domain, number_of_points)
    return [i * step_size for i in range(number_of_points)]
