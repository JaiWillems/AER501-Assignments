import numpy as np
import scipy

from src.assignment_two.types import Mesh, FreeVibrationResult, Matrix


class FreeVibrationSolver:

    @staticmethod
    def solve(mesh: Mesh, number_of_modes: int) -> FreeVibrationResult:
        eigenvalues, mode_shapes = FreeVibrationSolver._solve_generalized_eigenvalue_problem(
            mesh.stiffness_matrix(),
            mesh.mass_matrix(),
            number_of_modes
        )

        # TODO: The absolute value should be removed once the Mass and stiffness matrices are partitioned.
        natural_frequencies = FreeVibrationSolver._convert_to_hertz(
            np.sqrt(np.abs(eigenvalues))
        )

        return FreeVibrationResult(natural_frequencies, mode_shapes)

    @staticmethod
    def _solve_generalized_eigenvalue_problem(
            a: Matrix,
            b: Matrix,
            number_of_modes: int
    ) -> tuple:
        return scipy.linalg.eigh(
            a=a.values(),
            b=b.values(),
            subset_by_index=[0, number_of_modes-1]
        )

    @staticmethod
    def _convert_to_hertz(rad_per_second_array: list) -> list:
        return [i / (2 * np.pi) for i in rad_per_second_array]
