from src.assignment_one.part_b.rbf_functions.rbf import Rbf


class RbfCollocationSolution:

    def __init__(self, coefficients: list, rbf: Rbf, center_points: list,
                 sigma: float) -> None:
        """Solution to the RBF collocation method.

        :param coefficients: List of solution coefficients.
        :type coefficients: list.
        :param rbf: Radial basis function for the solution.
        :type rbf: Rbf.
        :param center_points: List of basis function center points.
        :type center_points: list.
        :param sigma: Basis function width parameters.
        :type sigma: float.
        """
        self._coefficients = coefficients
        self._rbf = rbf
        self._center_points = center_points
        self._sigma = sigma

    def evaluate(self, x: list) -> list:
        """Evaluate the solution at multiple points in the solution domain.

        :param x: List of domain points to evaluate the solution at.
        :type x: list.
        :return: Evaluated solution points.
        :rtype: list.
        """
        return [self._evaluate_single_point(xi) for xi in x]

    def _evaluate_single_point(self, x: float) -> float:
        """Evaluate the solution at a single point in the solution domain.

        :param x: Domain point to evaluate the solution at.
        :type x: float.
        :return: Evaluated solution point.
        :rtype: float.
        """
        evaluated_point = 0
        for c, cp in zip(self._coefficients, self._center_points):
            evaluated_point += c * self._rbf.evaluate(x, cp, self._sigma)
        return evaluated_point
