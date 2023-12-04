

class OptimizationResult:

    def __init__(self, design_vectors: list, costs: list) -> None:
        self._design_vectors = design_vectors
        self._costs = costs

    def iterations(self) -> list:
        return list(range(1, len(self._design_vectors) + 1))

    def design_vectors(self) -> list:
        return self._design_vectors

    def costs(self) -> list:
        return self._costs

    def optimum(self) -> tuple:
        minimum_cost = min(self._costs)
        design_vector = self._design_vectors[self._costs.index(minimum_cost)]
        return design_vector, minimum_cost
