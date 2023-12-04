import math
from abc import ABC

from src.assignment_three.objective_functions import BenchmarkObjectiveFunctionInterface


class MichalewiczFunction2D(BenchmarkObjectiveFunctionInterface, ABC):

    def __init__(self, m: float):
        self._m = m

    def evaluate(self, x: list, **kwargs: dict) -> float:
        s = 0
        for i, xi in enumerate(x):
            s -= math.sin(xi) * math.sin((i + 1) * xi ** 2 / math.pi) ** (2 * self._m)
        return s

    @staticmethod
    def global_optimum() -> list:
        return [2.20, 1.57]

    @staticmethod
    def global_optimum_value() -> float:
        return -1.8013
