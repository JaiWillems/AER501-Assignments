import math

from src.assignment_one.part_a.types.node import Node, BoundaryCondition
from src.assignment_one.part_a.utils.validator import Validator
from src.assignment_one.part_a.types.element import Element


class StiffnessMatrix:

    def __init__(self, nodes: list, values: list):
        """Stiffness matrix.

        :param nodes: Nodes corresponding to the value entries.
        :type: list.
        :param values: Stiffness matrix local_matrix.
        :type: list.
        """
        Validator.assert_square_matrix(values)
        Validator.assert_side_length_of_square_matrix(values, 2 * len(nodes))

        self._nodes = nodes
        self._values = values

    def nodes(self) -> list:
        return self._nodes

    def values(self) -> list:
        return self._values

    def partition_matrix(self) -> 'StiffnessMatrix':
        """Partition the matrix to not contain constrained nodes.

        :return: Partitioned matrix.
        """
        return StiffnessMatrix(
            self._get_unconstrained_nodes(),
            self._remove_values_by_indices(
                self._get_matrix_indices_for_nodes(
                    self._get_constrained_nodes()
                )
            )
        )

    def _get_constrained_nodes(self) -> list:
        return list(filter(lambda node: self._is_node_constrained(node), self._nodes))

    def _is_node_constrained(self, node: Node) -> bool:
        return node.boundary_condition() == BoundaryCondition.ZERO_DISPLACEMENT

    def _get_unconstrained_nodes(self) -> list:
        return list(filter(lambda node: not self._is_node_constrained(node), self._nodes))

    def _get_matrix_indices_for_nodes(self, nodes: list) -> list:
        indices = []
        for node in nodes:
            indices.extend(self._get_matrix_indices_for_node(node))
        return indices

    def _get_matrix_indices_for_node(self, node: Node) -> list:
        node_index = 2 * self._nodes.index(node)
        return [node_index, node_index + 1]

    def _remove_values_by_indices(self, removal_indices):
        partitioned_matrix = self._values.copy()
        decreasing_indices = sorted(removal_indices, reverse=True)

        for row in partitioned_matrix:
            for i in decreasing_indices:
                row.pop(i)

        for i in decreasing_indices:
            partitioned_matrix.pop(i)

        return partitioned_matrix

    @staticmethod
    def from_element(element: Element):
        """Create element stiffness matrix from element.

        :param element: Element to determine the stiffness matrix for.
        :type: Element.
        :return: Element stiffness matrix.
        :rtype: StiffnessMatrix.
        """
        nodes = [element.left_node(), element.right_node()]
        k = StiffnessMatrix.calculate_stiffness(
            element.elasticity(),
            element.cross_sectional_area(),
            element.length()
        )
        l = math.cos(element.incline())
        m = math.sin(element.incline())
        values = [
            [k*l*l, k*l*m, -k*l*l, -k*l*m],
            [k*l*m, k*m*m, -k*l*m, -k*m*m],
            [-k*l*l, -k*l*m, k*l*l, k*l*m],
            [-k*l*m, -k*m*m, k*l*m, k*m*m]
        ]
        return StiffnessMatrix(nodes, values)

    @staticmethod
    def calculate_stiffness(
            elasticity: float,
            area: float,
            length: float
    ) -> float:
        """Calculate stiffness.

        :param elasticity: Young's modulus in base SI units.
        :type elasticity: float.
        :param area: Cross-sectional area in m^2.
        :type area: float.
        :param length: Length in m.
        :type length: float.
        :return: Stiffness in base SI units.
        :rtype: float.
        """
        return elasticity * area / length
