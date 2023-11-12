import numpy as np
import scipy

from src.assignment_two.types import Mesh, FreeVibrationResult


class FreeVibrationSolver:

    @staticmethod
    def solve(mesh: Mesh, number_of_modes: int) -> FreeVibrationResult:
        """Solve the free-vibration problem.

        :param mesh: Mesh representing the frame to solve.
        :param number_of_modes: The number of modes in the returned results.
        :return: The free-vibration analysis results.
        """
        eigenvalues, mode_shapes = FreeVibrationSolver._solve_generalized_eigenvalue_problem(
            mesh.stiffness_matrix().partition_matrix(),
            mesh.mass_matrix().partition_matrix(),
            number_of_modes
        )
        natural_frequencies = FreeVibrationSolver._convert_to_hertz(
            np.sqrt(eigenvalues)
        )

        return FreeVibrationResult(natural_frequencies, mode_shapes)

    @staticmethod
    def _solve_generalized_eigenvalue_problem(
            a: list,
            b: list,
            number_of_modes: int
    ) -> tuple:
        return scipy.linalg.eigh(
            a=a,
            b=b,
            subset_by_index=[0, number_of_modes-1]
        )

    @staticmethod
    def _convert_to_hertz(rad_per_second_array: list) -> list:
        return [i / (2 * np.pi) for i in rad_per_second_array]
