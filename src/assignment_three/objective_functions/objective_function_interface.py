import abc


class ObjectiveFunctionInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def evaluate(self, x: list, **kwargs: int) -> float:
        """Evaluate the objective function.

        :param x: Design vector.
        :type x: list.
        :param kwargs: keyword arguments, only option is 'i' for iteration.
        :type kwargs: dict.
        :return: Cost value.
        :rtype float:
        """
        raise NotImplementedError
