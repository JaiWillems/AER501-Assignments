import math

from src.assignment_one.types.node import Node


class Element:

    def __init__(self, node_one: Node, node_two: Node, e: float, a: float, number: int) -> None:
        """Truss element.

        :param node_one: First node of the truss element.
        :type node_one: Node
        :param node_two: Second node of the truss element.
        :type node_two: Node
        :param e: Young's modulus in N/m^2.
        :type e: float
        :param a: Cross sectional area of element in m^2.
        :type a: float
        :param number: Unique global element number.
        :type number: int
        """
        self._node_one = node_one
        self._node_two = node_two
        self._E = e
        self._A = a
        self._number = number

    def node_one(self) -> Node:
        return self._node_one

    def node_two(self) -> Node:
        return self._node_two

    def youngs_modulus(self) -> float:
        return self._E

    def cross_sectional_area(self) -> float:
        return self._A

    def number(self) -> int:
        return self._number

    def stiffness(self) -> float:
        """Get the element stiffness.

        :return: Element stiffness in base SI units.
        :rtype: float
        """
        return self._E * self._A / self.length()

    def length(self) -> float:
        """Get length of the element.

        :return: Length of element in m.
        :rtype: float
        """
        return self._node_one.distance_to(self._node_two)

    def incline(self) -> float:
        """Get the inclination of the element.

        :return: Radian inclination of the element.
        :rtype: float

        ..note:: The inclination is the angle between the element and the
            horizontal where a positive inclination corresponds to the right
            node being higher than the left node.
        """
        if self._node_one.x() < self._node_two.x():
            left_node = self._node_one
            right_node = self._node_two
        else:
            left_node = self._node_two
            right_node = self._node_two

        return math.atan((right_node.y() - left_node.y()) / (
                right_node.x() - right_node.x()))
