import math

from src.assignment_three.objective_functions import MichalewiczFunction2D
from src.assignment_three.optimizer import SimulatedAnnealingOptimizer

X0 = [0, 0]
LOWER_BOUNDS = [0, 0]
UPPER_BOUNDS = [math.pi, math.pi]
OBJECTIVE_FUNCTION = MichalewiczFunction2D(10)

MAX_ITERATIONS = 2000

EPSILON = 0.1
INITIAL_TEMPERATURE = 1000
COOLING_PARAMETER = 0.89

OBJECTIVE_PLOT_POINTS_PER_DIMENSION = 100

results = SimulatedAnnealingOptimizer.optimize(
    X0,
    LOWER_BOUNDS,
    UPPER_BOUNDS,
    EPSILON,
    MAX_ITERATIONS,
    INITIAL_TEMPERATURE,
    COOLING_PARAMETER,
    OBJECTIVE_FUNCTION
)

best_vector, best_cost = results.optimum()
print(f"Michalewicz Optimum is {best_cost} at {best_vector}")
