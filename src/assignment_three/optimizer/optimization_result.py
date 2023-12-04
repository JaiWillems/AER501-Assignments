

class OptimizationResult:

    def __init__(self, design_vectors: list, costs: list) -> None:
        self._design_vectors = design_vectors
        self._costs = costs

    def design_vectors(self) -> list:
        return self._design_vectors

    def costs(self) -> list:
        return self._costs
