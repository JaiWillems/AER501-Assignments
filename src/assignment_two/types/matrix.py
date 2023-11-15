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

    def partition_matrix(self) -> 'Matrix':
        """Partition the matrix to not contain constrained nodes.

        :return: Partitioned matrix.
        """
        return Matrix(
            self._get_unconstrained_nodes(),
            self._remove_values_by_indices(
                self._get_matrix_indices_for_nodes(
                    self._get_constrained_nodes()
                )
            )
        )

    def _get_constrained_nodes(self) -> list:
        return list(filter(lambda node: node.is_constrained(), self._nodes))

    def _get_unconstrained_nodes(self) -> list:
        return list(filter(lambda node: not node.is_constrained(), self._nodes))

    def _get_matrix_indices_for_nodes(self, nodes: list) -> list:
        indices = []
        for node in nodes:
            indices.extend(self._get_matrix_indices_for_node(node))
        return indices

    def _get_matrix_indices_for_node(self, node: FrameNode) -> list:
        node_index = 3 * self._nodes.index(node)
        return [node_index, node_index + 1, node_index + 2]

    def _remove_values_by_indices(self, removal_indices):
        partitioned_matrix = self._values.copy()
        decreasing_indices = sorted(removal_indices, reverse=True)

        for row in partitioned_matrix:
            for i in decreasing_indices:
                row.pop(i)

        for i in decreasing_indices:
            partitioned_matrix.pop(i)

        return partitioned_matrix
