import numpy as np

from src.assignment_one.part_a.types.node import BoundaryCondition
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
        nodes = stiffness_matrix.nodes()
        partitioned_nodes = DisplacementSolver._partition_nodes(nodes)

        partition_indices = DisplacementSolver._get_partition_indicies(nodes)

        partitioned_values = DisplacementSolver._partition_matrix(
            stiffness_matrix.values(),
            partition_indices
        )

        partitioned_forces = DisplacementSolver._partition_vector(
            DisplacementSolver._generate_force_vector(nodes),
            partition_indices
        )

        displacements = DisplacementSolver._solve_linear_system(
            partitioned_values,
            partitioned_forces
        )

        return DisplacementSolver._create_output(
            partitioned_nodes,
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
    def _get_partition_indicies(nodes: list) -> list:
        """Get indices with non-fixed elements.

        :param nodes: List of elements associated with the matrix.
        :type nodes: list
        :return: List of mobile node indices.
        :rtype: list.
        """
        indices = []
        partitioned_nodes = DisplacementSolver._partition_nodes(nodes)
        for i, node in enumerate(nodes):
            if node in partitioned_nodes:
                indices.append(2 * i)
                indices.append(2 * i + 1)
        return indices

    @staticmethod
    def _partition_nodes(nodes: list) -> list:
        """Get non-fixed nodes.

        :param nodes: List of nodes in truss.
        :param nodes: list.
        :return: Partitioned nodes.
        :rtype: list.
        """
        partitioned_nodes = []
        for node in nodes:
            if node.boundary_condition() == BoundaryCondition.NONE:
                partitioned_nodes.append(node)
        return partitioned_nodes

    @staticmethod
    def _partition_matrix(matrix: list, partition_indices: list) -> list:
        """Partition the matrix.

        :param matrix: Matrix to partition.
        :type matrix: list.
        :param partition_indices: Indices to partition by.
        :type partition_indices: list.
        :return: Partitioned matrix.
        :rtype: list.
        """
        partitioned_matrix = []
        for row_index in partition_indices:
            partitioned_matrix.append(
                DisplacementSolver._partition_vector(
                    matrix[row_index],
                    partition_indices
                )
            )
        return partitioned_matrix

    @staticmethod
    def _partition_vector(vector: list, partition_indices: list) -> list:
        """Partition vector based on list of indices.

        :param vector: Vector to partition.
        :type vector: list.
        :param partition_indices: Indicies to keep.
        :type partition_indices: list.
        :return: Partitioned vector.
        :rtype: list.
        """
        partitioned_vector = []
        for index in partition_indices:
            partitioned_vector.append(vector[index])
        return partitioned_vector

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
            output[node] = Vector2d(displacements[i], displacements[i + 1])
        return output
