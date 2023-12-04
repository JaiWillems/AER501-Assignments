import math
import random

from src.assignment_three.objective_functions import ObjectiveFunctionInterface
from src.assignment_three.optimizer import OptimizationResultBuilder, \
    OptimizationResult


class SimulatedAnnealingOptimizer:

    @staticmethod
    def optimize(
            x0: list,
            lower_bounds: list,
            upper_bounds: list,
            epsilon: float,
            max_iterations: int,
            initial_temperature: float,
            cooling_parameter: float,
            objective_function: ObjectiveFunctionInterface
    ) -> OptimizationResult:

        results_builder = OptimizationResultBuilder()

        iteration = 0
        temperature = initial_temperature
        best_solution = x0
        best_cost = objective_function.evaluate(best_solution)

        while SimulatedAnnealingOptimizer.convergence_criteria_not_met(
                iteration,
                max_iterations
        ):

            current_solution = SimulatedAnnealingOptimizer.move(
                best_solution,
                lower_bounds,
                upper_bounds,
                epsilon
            )
            current_cost = objective_function.evaluate(current_solution)

            if SimulatedAnnealingOptimizer.accept_solution(
                    best_cost,
                    current_cost,
                    temperature
            ):
                best_solution = current_solution
                best_cost = current_cost

            results_builder.add_iteration(best_solution, best_cost)

            temperature = SimulatedAnnealingOptimizer.schedule(
                initial_temperature,
                cooling_parameter,
                iteration
            )
            iteration += 1

        return results_builder.build()

    @staticmethod
    def convergence_criteria_not_met(
            iteration: int,
            max_iterations: int
    ) -> bool:
        return iteration < max_iterations

    @staticmethod
    def move(
            x: list,
            lower_bound: list,
            upper_bound: list,
            epsilon: float
    ) -> list:
        while True:
            i = math.floor(random.random() * len(x))
            z = x.copy()
            z[i] = x[i] + epsilon * (-1 + random.random() * 2)
            if lower_bound[i] <= z[i] <= upper_bound[i]:
                return z

    @staticmethod
    def accept_solution(
            best_cost: float,
            current_cost: float,
            current_temperature: float
    ) -> bool:
        if current_cost < best_cost:
            return True

        p = math.exp((best_cost - current_cost) / current_temperature)
        return random.choices([0, 1], [1 - p, p])[0] > 0.5

    @staticmethod
    def schedule(
            initial_temperature: float,
            cooling_parameter: float,
            iteration: int
    ) -> float:
        return initial_temperature * cooling_parameter ** iteration
