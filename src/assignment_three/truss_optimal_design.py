from matplotlib import pyplot as plt

from src.assignment_three.api import AssignmentOneApi
from src.assignment_three.objective_functions import TrussObjectiveFunction
from src.assignment_three.optimizer import SimulatedAnnealingOptimizer

X0 = 10 * [0.01]
LOWER_BOUNDS = 10 * [0]
UPPER_BOUNDS = 10 * [1]
EPSILON = 0.05
MAX_ITERATIONS = 1000
INITIAL_TEMPERATURE = 1000
COOLING_PARAMETER = 0.89

MEMBER_YIELD_STRENGTH = 2.76e+8  # Pa.
MEMBER_DENSITY = 2700  # kg/m^3.
C = 0.5
ALPHA = 1.5

objective_function = TrussObjectiveFunction(
    MEMBER_YIELD_STRENGTH,
    MEMBER_DENSITY,
    C,
    ALPHA
)

result = SimulatedAnnealingOptimizer.optimize(
    X0,
    LOWER_BOUNDS,
    UPPER_BOUNDS,
    EPSILON,
    MAX_ITERATIONS,
    INITIAL_TEMPERATURE,
    COOLING_PARAMETER,
    objective_function
)

best_areas, best_cost = result.optimum()
print(f"Optimum: Cost={best_cost}, Areas={best_areas}")

plt.plot(
    result.iterations(),
    result.costs()
)
plt.title(f"10 Bar Truss Objective Function")
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.grid()
plt.show()
