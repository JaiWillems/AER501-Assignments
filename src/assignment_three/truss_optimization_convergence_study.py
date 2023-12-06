import random

import numpy as np
from matplotlib import pyplot as plt

from src.assignment_three.objective_functions import TrussObjectiveFunction
from src.assignment_three.optimizer import SimulatedAnnealingOptimizer

LOWER_BOUNDS = 10 * [0]
UPPER_BOUNDS = 10 * [5e-4]
EPSILON = 0.05
MAX_ITERATIONS = 1000
INITIAL_TEMPERATURE = 1000
COOLING_PARAMETER = 0.89

TRIALS_PER_PENALTY_PARAMETER = 25

MEMBER_YIELD_STRENGTH = 2.76e+8  # Pa.
MEMBER_DENSITY = 2700  # kg/m^3.
C = 0.5
ALPHA = [1, 1.5, 2]

for alpha in ALPHA:

    objective_function = TrussObjectiveFunction(
        MEMBER_YIELD_STRENGTH,
        MEMBER_DENSITY,
        C,
        alpha
    )

    trial_costs = []
    for _ in range(TRIALS_PER_PENALTY_PARAMETER):
        x0 = [1e-4 * random.random() for _ in range(10)]
        results = SimulatedAnnealingOptimizer.optimize(
            x0,
            LOWER_BOUNDS,
            UPPER_BOUNDS,
            EPSILON,
            MAX_ITERATIONS,
            INITIAL_TEMPERATURE,
            COOLING_PARAMETER,
            objective_function
        )

        trial_costs.append(results.costs())

    average_costs = np.average(trial_costs, axis=0)

    plt.plot(
        range(1, MAX_ITERATIONS + 1),
        average_costs,
        label=f"alpha={alpha}"
    )

plt.title(f"10 Bar Truss Objective Function")
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.legend()
plt.grid()
plt.show()
