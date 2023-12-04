import numpy as np

from src.assignment_one.part_a.types.vector2d import Vector2d
from src.assignment_one.part_a.types.stiffness_matrix import StiffnessMatrix


class DisplacementSolver:

    @staticmethod
    def solve(stiffness_matrix: StiffnessMatrix) -> dict:
        """Solve for the displacements for global stiffness matrix.

        :param stiffness_matrix: Global stiffness matrix.
        :type stiffness_matrix: list.
        :return: Dictionary mapping nodes to their displacements.
        :rtype: dict.
        """

        partitioned_matrix = stiffness_matrix.partition_matrix()
        values = partitioned_matrix.values()
        nodes = partitioned_matrix.nodes()
        forces = DisplacementSolver._generate_force_vector(
            nodes
        )

        displacements = DisplacementSolver._solve_linear_system(
            values,
            forces
        )

        return DisplacementSolver._create_output(
            nodes,
            displacements
        )

    @staticmethod
    def _generate_force_vector(nodes: list) -> list:
        """Generate force vector.

        :param nodes: List of elements associated with the matrix.
        :type nodes: list.
        :return: List of force vector components.
        :rtype: list.
        """
        vector = []
        for node in nodes:
            vector.append(node.force().x())
            vector.append(node.force().y())
        return vector

    @staticmethod
    def _solve_linear_system(a: list, b: list) -> list:
        """Find the vector, x, such that ax=b.

        :param a: Matrix of local_matrix.
        :type a: list.
        :param b: Known output of the system.
        :type b: list.
        :return: Solution to the system of equations.
        :rtype: list.
        """
        return np.linalg.solve(a, b).tolist()

    @staticmethod
    def _create_output(nodes: list, displacements: list) -> dict:
        """Create dictionary output.

        :param nodes: List of partitioned elements.
        :type nodes: list.
        :param displacements: Nodal displacements.
        :type displacements: list.
        :return: Dictionary relating elements to displacement vectors.
        :rtype: dict.
        """
        output = {}
        for i, node in enumerate(nodes):
            output[node] = Vector2d(displacements[2 * i], displacements[2 * i + 1])
        return output
