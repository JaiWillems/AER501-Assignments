import math

from src.assignment_one.part_b.rbf_functions.gaussian_rbf import GaussianRbf
from src.assignment_one.part_b.rbf_functions.multiquadratic_rbf import \
    MultiquadraticRbf
from src.assignment_one.part_b.solver.rbf_collocation_solver import \
    RbfCollocationSolver


def collocation_solutions(domain: list, n: int, sigma: float=None) -> tuple:
    """Generate the gaussian and multiquadratic RBF collocation solutions.

    :param domain: Two element list representing the problem domain.
    :type domain: list.
    :param n: Number of collocation points to use.
    :type n: int.
    :param sigma: Basis function shape parameter, optional.
    :type sigma: float.
    :return: Two element tuple containing the RBF collocation solutions.
    :rtype: tuple.
    """
    if sigma is None:
        sigma = 2.2 * RbfCollocationSolver.step_size(domain, n)
    gaussian_solution = RbfCollocationSolver.solve_with_homogenous_dirichlet(
        domain,
        n,
        GaussianRbf(),
        sigma
    )
    multiquadratic_solution = RbfCollocationSolver.solve_with_homogenous_dirichlet(
        domain,
        n,
        MultiquadraticRbf(),
        sigma
    )
    return gaussian_solution, multiquadratic_solution


def linearly_spaced_points(domain: list, n: int) -> list:
    """Generate linearly spaced list.

    :param domain: Two element list representing the problem domain.
    :type domain: list.
    :param n: Number of points to use.
    :type n: int.
    :return: List of linearly spaced points.
    :rtype: float.
    """
    step_size = RbfCollocationSolver.step_size(domain, n)
    return [domain[0] + i * step_size for i in range(n)]


def actual_solution(x: list) -> list:
    """Problem solution.

    :param x: Values to evaluate the solution at.
    :type x: list.
    :return: The solutions at `x`.
    :rtype: list.
    """
    return [0.8509 * math.sinh(xi) - xi for xi in x]


def calculate_l2_error(expected: list, actual: list) -> float:
    """Calculate the L2 error norm for the given arrays.

    :param expected: List of expected data.
    :type expected: list.
    :param actual: List of actual data.
    :type actual: list.
    :return: L2 error norm.
    :rtype: float.
    """
    return sum([(e - a) ** 2 for e, a in zip(expected, actual)])
