from src.assignment_three.optimizer import OptimizationResult


class OptimizationResultBuilder:

    def __init__(self) -> None:
        self._design_vectors = []
        self._costs = []

    def add_iteration(self, design_vector: list, cost: float) -> None:
        self._design_vectors.append(design_vector)
        self._costs.append(cost)

    def build(self) -> OptimizationResult:
        return OptimizationResult(self._design_vectors, self._costs)
