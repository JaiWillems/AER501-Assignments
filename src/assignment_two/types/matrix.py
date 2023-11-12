from src.assignment_two.types import FrameNode


class Matrix:

    def __init__(self, nodes: list, values: list) -> None:
        """Matrix for frame data.

        :param nodes: List of nodes that relate to matrix values.
        :param values: Twice nested list representing matrix values.
        """
        self._nodes = nodes
        self._values = values

    def nodes(self) -> list:
        return self._nodes

    def values(self) -> list:
        return self._values

    def partition_matrix(self) -> list:
        """Partition the matrix for unconstrained nodes.

        :return: Partitioned matrix.
        """
        partitioned_matrix = self._values.copy()
        reversed_nodes = self._nodes.copy()
        reversed_nodes.reverse()

        # Remove constrained columns.
        for row in partitioned_matrix:
            for node in reversed_nodes:
                if node.is_constrained():
                    node_index = self._get_node_index(node)
                    row.pop(node_index)
                    row.pop(node_index)
                    row.pop(node_index)

        # Remove constrained rows.
        for node in reversed_nodes:
            if node.is_constrained():
                node_index = self._get_node_index(node)
                partitioned_matrix.pop(node_index)
                partitioned_matrix.pop(node_index)
                partitioned_matrix.pop(node_index)

        return partitioned_matrix

    def _get_active_dof_indices(self):
        indices = []
        for i, node in enumerate(self._nodes):
            if not node.is_constrained():
                indices.extend([3 * i, 3 * i + 1, 3 * i + 2])
        return indices

    def _get_node_index(self, node: FrameNode) -> int:
        return 3 * self._nodes.index(node)
