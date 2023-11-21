import numpy as np
from multipledispatch import dispatch

from src.assignment_two.types import Mesh, Matrix, ForcedVibrationResults
from src.assignment_two.types.nodal_displacement import NodalDisplacement


class ForcedVibrationFullOrderSolver:

    @staticmethod
    def solve(
        mesh: Mesh,
        frequency_hz: float,
        stiffness_damping_factor: float,
        mass_damping_factor: float
    ) -> ForcedVibrationResults:
        """Solve for the nodal displacements for a unit harmonic excitation.

        :param mesh: The mech representing the frame structure.
        :param frequency_hz: Excitation frequency in Hertz.
        :param stiffness_damping_factor: The proportional damping factor for the
            stiffness matrix.
        :param mass_damping_factor: The proportional damping factor for the mass
            matrix.
        :return: Dictionary with node keys and nodal-displacement values.
        """
        dynamic_stiffness_matrix = ForcedVibrationFullOrderSolver._dynamic_stiffness_matrix(
            mesh,
            frequency_hz,
            stiffness_damping_factor,
            mass_damping_factor
        ).partition_matrix()
        force_vector = ForcedVibrationFullOrderSolver._get_force_vector(
            dynamic_stiffness_matrix.nodes()
        )

        unconstrained_nodal_displacements = ForcedVibrationFullOrderSolver._solve_linear_system(
            dynamic_stiffness_matrix.values(),
            force_vector
        )
        unconstrained_nodes = dynamic_stiffness_matrix.nodes()

        results = {}
        for index, node in enumerate(unconstrained_nodes):
            results[node] = NodalDisplacement(
                unconstrained_nodal_displacements[3 * index],
                unconstrained_nodal_displacements[3 * index + 1],
                unconstrained_nodal_displacements[3 * index + 2]
            )

        return ForcedVibrationResults(results)

    @staticmethod
    @dispatch(Mesh, float, float, float)
    def _dynamic_stiffness_matrix(
        mesh: Mesh,
        frequency_hz: float,
        stiffness_damping_factor: float,
        mass_damping_factor: float
    ) -> Matrix:
        values = ForcedVibrationFullOrderSolver._dynamic_stiffness_matrix(
            mesh.stiffness_matrix().values(),
            mesh.mass_matrix().values(),
            2 * np.pi * frequency_hz,
            stiffness_damping_factor,
            mass_damping_factor
        )
        return Matrix(mesh.nodes(), values)

    @staticmethod
    @dispatch(list, list, float, float, float)
    def _dynamic_stiffness_matrix(
        stiffness_matrix: list,
        mass_matrix: list,
        angular_frequency: float,
        stiffness_damping_factor: float,
        mass_damping_factor: float
    ) -> list:
        k = np.array(stiffness_matrix)
        m = np.array(mass_matrix)
        values = k - angular_frequency ** 2 * m + angular_frequency * 1j * (
                stiffness_damping_factor * k + mass_damping_factor * m)
        return values.tolist()

    @staticmethod
    def _get_force_vector(nodes) -> list:
        force_vector = []
        for node in nodes:
            force_vector.append(node.harmonic_excitation_amplitude_x())
            force_vector.append(node.harmonic_excitation_amplitude_y())
            force_vector.append(node.harmonic_excitation_amplitude_m())
        return force_vector

    @staticmethod
    def _solve_linear_system(a: list, b: list) -> list:
        return np.linalg.solve(a, b)
