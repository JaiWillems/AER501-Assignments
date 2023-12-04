import abc


class ObjectiveFunctionInterface(metaclass=abc.ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def evaluate(x: list) -> float:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def global_optimum() -> list:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def global_optimum_value() -> float:
        raise NotImplementedError
