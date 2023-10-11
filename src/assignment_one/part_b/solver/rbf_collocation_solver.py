import numpy as np

from src.assignment_one.part_b.solver.rbf_collocation_solution import \
    RbfCollocationSolution
from src.assignment_one.part_b.rbf_functions.rbf import Rbf


class RbfCollocationSolver:

    @staticmethod
    def solve_with_homogenous_dirichlet(
            domain: list,
            n: int,
            rbf: Rbf,
            sigma: float
    ) -> RbfCollocationSolution:
        """Solve ode using the RBF collocation method with homogenous dirichlet
        boundary conditions.

        :param domain: Two element list containing the domain start and end.
        :type domain: list.
        :param n: Number of collocation points.
        :type n: int.
        :param rbf: Radial basis function for the gaussian_solution.
        :type Rbf.
        :param sigma: RBF width parameter.
        :type sigma: float.
        :return: Solution to the input problem.
        :rtype: RbfCollocationSolution.
        """
        collocation_points = RbfCollocationSolver._collocation_points(domain, n)
        coefficients = RbfCollocationSolver._solve_linear_system(
            RbfCollocationSolver._dynamics_matrix(
                domain,
                collocation_points,
                sigma,
                rbf
            ),
            RbfCollocationSolver._source_terms_vector(
                domain,
                collocation_points
            )
        )
        return RbfCollocationSolution(
            coefficients,
            rbf,
            collocation_points,
            sigma
        )

    @staticmethod
    def _collocation_points(domain: list, n: int) -> list:
        """Generate collocation points.

        :param domain: Two element list containing the domain start and end.
        :type domain: list.
        :param n: Number of collocation points.
        :type n: int.
        :return: List of collocation points.
        :rtype: list.
        """
        step_size = RbfCollocationSolver.step_size(domain, n)
        return [domain[0] + i * step_size for i in range(n)]

    @staticmethod
    def step_size(domain, n):
        """Calculate step-size.

        :param domain: Two element list containing the domain start and end.
        :type domain: list.
        :param n: Number of collocation points.
        :type n: int.
        :return: Step size.
        :rtype: float.
        """
        return (domain[1] - domain[0]) / (n - 1)

    @staticmethod
    def _dynamics_matrix(
            domain: list,
            x: list,
            sigma: float,
            rbf: Rbf
    ) -> list:
        """Generate dynamics matrix.

        :param domain: Two element list containing the domain start and end.
        :type domain: list.
        :param x: List of collocation points.
        :type x: list.
        :param sigma: RBF width parameter.
        :type sigma: float.
        :param rbf: Basis functions.
        :type Rbf.
        :return: Dynamics matrix.
        :rtype: list.
        """
        dynamics_matrix = []
        for xi in x:
            row = []
            for center_point in x:
                if xi in domain:
                    row.append(rbf.evaluate(xi, center_point, sigma))
                else:
                    row.append(rbf.evaluate_ode(xi, center_point, sigma))
            dynamics_matrix.append(row)
        return dynamics_matrix

    @staticmethod
    def _source_terms_vector(domain: list, x: list) -> list:
        """Generate source term vector.

        :param domain: Two element list containing the domain start and end.
        :type domain: list.
        :param x: List of collocation points.
        :type x: list.
        :return: Source term vector.
        :rtype: list.
        """
        return [0 if xi in domain else xi for xi in x]

    @staticmethod
    def _solve_linear_system(a: list, b: list) -> list:
        """Solve the system ax=b for x.

        :param a: Dynamics matrix.
        :type a: list.
        :param b: Source terms vector.
        :type b: list.
        :return: Solution vector to the system.
        :rtype: list.
        """
        return np.linalg.solve(a, b)
