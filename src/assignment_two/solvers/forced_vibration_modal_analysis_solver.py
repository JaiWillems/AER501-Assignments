import numpy as np
from multipledispatch import dispatch

from src.assignment_two.solvers import FreeVibrationSolver
from src.assignment_two.types import Mesh, ForcedVibrationResults, NodalDisplacement


class ForcedVibrationModalAnalysisSolver:

    @staticmethod
    @dispatch(Mesh, int, float, float, float)
    def solve(
            mesh: Mesh,
            number_of_modes: int,
            frequency_hz: float,
            stiffness_damping_factor: float,
            mass_damping_factor: float
    ) -> ForcedVibrationResults:
        mode_shapes, natural_frequencies = ForcedVibrationModalAnalysisSolver._free_vibration_results(
            mesh,
            number_of_modes
        )
        return ForcedVibrationModalAnalysisSolver.solve(
            natural_frequencies,
            mode_shapes,
            mesh.unconstrained_nodes(),
            frequency_hz,
            stiffness_damping_factor,
            mass_damping_factor
        )

    @staticmethod
    @dispatch(list, list, list, float, float, float)
    def solve(
            natural_frequencies: list,
            mode_shapes: list,
            unconstrained_nodes: list,
            frequency_hz: float,
            stiffness_damping_factor: float,
            mass_damping_factor: float
    ) -> ForcedVibrationResults:

        force_vector = ForcedVibrationModalAnalysisSolver._get_force_vector(
            unconstrained_nodes
        )

        modal_contribution_factors = ForcedVibrationModalAnalysisSolver._modal_contribution_factors(
            force_vector,
            natural_frequencies,
            mode_shapes,
            frequency_hz,
            mass_damping_factor,
            stiffness_damping_factor
        )

        nodal_displacement = list(np.dot(mode_shapes, modal_contribution_factors))

        return ForcedVibrationResults(
            ForcedVibrationModalAnalysisSolver._format_results(
                nodal_displacement,
                unconstrained_nodes
            )
        )

    @staticmethod
    def _modal_contribution_factors(
            force_vector: list,
            natural_frequencies: list,
            mode_shapes: list,
            excitation_frequency_rad_per_s: float,
            mass_damping_factor: float,
            stiffness_damping_factor: float
    ) -> list:
        modal_contribution_factors = []
        for natural_frequency, mode_shape in zip(natural_frequencies, np.transpose(mode_shapes)):
            modal_contribution_factors.append(
                ForcedVibrationModalAnalysisSolver._modal_contribution_factor(
                    force_vector,
                    mode_shape,
                    natural_frequency,
                    excitation_frequency_rad_per_s,
                    mass_damping_factor,
                    stiffness_damping_factor
                )
            )
        return modal_contribution_factors

    @staticmethod
    def _modal_contribution_factor(
            force_vector: list,
            mode_shape: list,
            natural_frequency: float,
            excitation_frequency_rad_per_s: float,
            mass_damping_factor,
            stiffness_damping_factor: float
    ) -> float:
        return np.dot(mode_shape, force_vector) / (natural_frequency ** 2 -
            excitation_frequency_rad_per_s ** 2 + 1j * excitation_frequency_rad_per_s * (
            stiffness_damping_factor * natural_frequency ** 2 + mass_damping_factor))

    @staticmethod
    def _free_vibration_results(mesh: Mesh, number_of_modes: int) -> tuple:
        free_vibration_results = FreeVibrationSolver.solve(
            mesh,
            number_of_modes
        )
        return list(free_vibration_results.mode_shapes()), \
            free_vibration_results.natural_frequencies()

    @staticmethod
    def _get_force_vector(nodes: list) -> list:
        force_vector = []
        for node in nodes:
            force_vector.append(node.harmonic_excitation_amplitude_x())
            force_vector.append(node.harmonic_excitation_amplitude_y())
            force_vector.append(node.harmonic_excitation_amplitude_m())
        return force_vector

    @staticmethod
    def _format_results(
            nodal_displacement: list,
            unconstrained_nodes: list
    ) -> dict:
        results = {}
        for i, node in enumerate(unconstrained_nodes):
            results[node] = NodalDisplacement(
                nodal_displacement[3 * i],
                nodal_displacement[3 * i + 1],
                nodal_displacement[3 * i + 2]
            )
        return results
