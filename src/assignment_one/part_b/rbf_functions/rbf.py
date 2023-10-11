import abc


class Rbf(metaclass=abc.ABCMeta):
    """Framework for Radial Basis Functions."""

    @classmethod
    def __subclasshook__(cls, subclass) -> bool:
        return (
            hasattr(subclass, 'evaluate') and callable(subclass.evaluate) and
            hasattr(subclass, 'evaluate_ode') and callable(subclass.evaluate_ode) or
            NotImplemented
        )

    @abc.abstractmethod
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
        raise NotImplementedError

    @abc.abstractmethod
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
        raise NotImplementedError
