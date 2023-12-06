import random

from matplotlib import pyplot as plt

from src.assignment_three.api import AssignmentOneApi
from src.assignment_three.objective_functions import TrussObjectiveFunction
from src.assignment_three.optimizer import SimulatedAnnealingOptimizer

LOWER_BOUNDS = 10 * [0]
UPPER_BOUNDS = 10 * [5e-4]
EPSILON = 0.05
MAX_ITERATIONS = 6000
INITIAL_TEMPERATURE = 1000
COOLING_PARAMETER = 0.89

NUMBER_OF_TRIALS = 100

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

best_cost = 1e8
best_result = None
best_initial_condition = None

for _ in range(NUMBER_OF_TRIALS):

    x0 = [1e-4 * random.random() for _ in range(10)]

    result = SimulatedAnnealingOptimizer.optimize(
        x0,
        LOWER_BOUNDS,
        UPPER_BOUNDS,
        EPSILON,
        MAX_ITERATIONS,
        INITIAL_TEMPERATURE,
        COOLING_PARAMETER,
        objective_function
    )

    current_solution, current_cost = result.optimum()
    if current_cost < best_cost:
        best_cost = current_cost
        best_result = result
        best_initial_condition = x0

best_areas, best_cost = best_result.optimum()
_, _, stresses = AssignmentOneApi.solve_10_bar_truss(best_areas)
print(f"Optimum: Cost={best_cost}\nInitial Condition: {best_initial_condition}")
for i, member in enumerate(stresses.keys()):
    print(f"Member {i + 1} has area {1e6 * best_areas[i]} mm^2 and stress {1e-6 * stresses[member]} Mpa")

plt.plot(
    best_result.iterations(),
    best_result.costs()
)
plt.title(f"10 Bar Truss Objective Function")
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.grid()
plt.show()
