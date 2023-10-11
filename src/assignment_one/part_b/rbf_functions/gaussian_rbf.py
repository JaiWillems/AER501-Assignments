import abc
import math

from src.assignment_one.part_b.rbf_functions.rbf_function import RbfFunction


class GaussianRbf(abc.ABC, RbfFunction):

    def evaluate(self, x: float, c: float, sigma: float) -> float:
        """Evaluate the RBF with the given parameters.

        :param x: The domain point to evaluate the RBF at.
        :type x: float.
        :param c: RBF center point.
        :type c: float.
        :param sigma: RBF width parameter.
        :type sigma: float.
        :return: RBF evaluation result.
        :rtype: float.
        """
        return math.exp(-(x - c) ** 2 / sigma)

    def evaluate_ode(self, x: float, c: float, sigma: float) -> float:
        """Evaluate the model applied RBF with the given parameters.

        :param x: The domain point to evaluate the RBF at.
        :type x: float.
        :param c: RBF center point.
        :type c: float.
        :param sigma: RBF width parameter.
        :type sigma: float.
        :return: Model applied RBF evaluation result.
        :rtype: float.
        """
        return -(math.exp(- (x - c) ** 2 / sigma) * (-4 * c ** 2 + 8 * c * x +
            sigma ** 2 + 2 * sigma - 4 * x ** 2)) / sigma ** 2
