import math

from src.assignment_one.validator import Validator
from src.assignment_one.types.element import Element


class StiffnessMatrix:

    def __init__(self, nodes: list, values: list):
        """Stiffness matrix.

        :param nodes: Nodes corresponding to the value entries.
        :type: list.
        :param values: Stiffness matrix values.
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
