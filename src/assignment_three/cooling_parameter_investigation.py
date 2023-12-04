import math

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

from src.assignment_three.objective_functions import MichalewiczFunction2D
from src.assignment_three.optimizer import SimulatedAnnealingOptimizer

X0 = [0, 0]
LOWER_BOUNDS = [0, 0]
UPPER_BOUNDS = [math.pi, math.pi]
OBJECTIVE_FUNCTION = MichalewiczFunction2D(10)

MAX_ITERATIONS = 5000

EPSILON = 0.05
INITIAL_TEMPERATURE = 1000
COOLING_PARAMETERS = [0.87, 0.89, 0.91, 0.93, 0.95, 0.97, 0.99]
TRIALS_PER_COOLING_PARAMETER = 100

cmap = plt.cm.Spectral(np.linspace(0.15, 0.85, len(COOLING_PARAMETERS)))
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=cmap)

optimum = OBJECTIVE_FUNCTION.global_optimum_value()
for cooling_parameter in COOLING_PARAMETERS:

    trial_costs = []
    for _ in range(TRIALS_PER_COOLING_PARAMETER):
        results = SimulatedAnnealingOptimizer.optimize(
            X0,
            LOWER_BOUNDS,
            UPPER_BOUNDS,
            EPSILON,
            MAX_ITERATIONS,
            INITIAL_TEMPERATURE,
            cooling_parameter,
            OBJECTIVE_FUNCTION
        )

        trial_costs.append(results.costs())

    average_costs = np.average(trial_costs, axis=0)
    error = [abs(optimum - c) for c in average_costs]
    plt.plot(
        range(1, MAX_ITERATIONS + 1),
        error,
        label=f"C={cooling_parameter}"
    )

plt.title(f"Convergence for Different Cooling Parameters, epsilon={EPSILON}")
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.legend()
plt.grid()
plt.show()
