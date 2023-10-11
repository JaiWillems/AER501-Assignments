import abc
import math

from src.assignment_one.part_b.rbf_functions.rbf_function import RbfFunction


class MultiquadraticRbf(abc.ABC, RbfFunction):

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
        return math.sqrt(1 + (x - c) ** 2 / sigma)

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
        a = (x - c) ** 2 / sigma + 1
        return -(sigma ** 2 * a ** 2 - 2 * c * x - sigma * a + c ** 2 + x ** 2) / \
               (sigma ** 2 * a ** (3 / 2))
