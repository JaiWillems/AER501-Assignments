import math

from src.assignment_one.part_a.types.node import Node
from src.assignment_one.part_a.utils.validator import Validator


class Element:

    def __init__(
            self,
            left_node: Node,
            right_node: Node,
            elasticity: float,
            area: float
    ) -> None:
        """Truss element.

        :param left_node: First node of the truss element.
        :type left_node: Node
        :param right_node: Second node of the truss element.
        :type right_node: Node
        :param elasticity: Young's modulus in N/m^2.
        :type elasticity: float
        :param area: Cross sectional area of element in m^2.
        :type area: float
        """
        Validator.assert_element_has_non_zero_width(left_node, right_node)
        Validator.assert_node_order(left_node, right_node)

        self._left_node = left_node
        self._right_node = right_node
        self._elasticity = elasticity
        self._area = area

    def left_node(self) -> Node:
        return self._left_node

    def right_node(self) -> Node:
        return self._right_node

    def elasticity(self) -> float:
        return self._elasticity

    def cross_sectional_area(self) -> float:
        return self._area

    def length(self) -> float:
        """Get length of the element.

        :return: Length of element in m.
        :rtype: float
        """
        return self._left_node.distance_to(self._right_node)

    def incline(self) -> float:
        """Get the inclination of the element.

        :return: Radian inclination of the element.
        :rtype: float

        ..note:: The inclination is the angle between the element and the
            horizontal where area positive inclination corresponds to the right
            node being higher than the left node.
        """
        return math.atan2(
            self._right_node.y() - self._left_node.y(),
            self._right_node.x() - self._left_node.x()
        )
