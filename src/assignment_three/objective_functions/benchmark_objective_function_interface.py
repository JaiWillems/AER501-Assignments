import abc

from src.assignment_three.objective_functions import ObjectiveFunctionInterface


class BenchmarkObjectiveFunctionInterface(ObjectiveFunctionInterface, metaclass=abc.ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def global_optimum() -> list:
        """Get the global optimum vector of the benchmark function.

        :return: Global optimum vector.
        :rtype: list.
        """
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def global_optimum_value() -> float:
        """Get the global optimum value of the benchmark function.

        :return: Global optimum.
        :rtype: float.
        """
        raise NotImplementedError
