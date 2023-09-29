import math

from src.assignment_one.types.node import Node


class Element:

    def __init__(
            self,
            left_node: Node,
            right_node: Node,
            e: float,
            a: float,
            number: int
    ) -> None:
        """Truss element.

        :param left_node: First node of the truss element.
        :type left_node: Node
        :param right_node: Second node of the truss element.
        :type right_node: Node
        :param e: Young's modulus in N/m^2.
        :type e: float
        :param a: Cross sectional area of element in m^2.
        :type a: float
        :param number: Unique global element number.
        :type number: int
        """
        self._validate_nodes(left_node, right_node)

        self._left_node = left_node
        self._right_node = right_node
        self._E = e
        self._A = a
        self._number = number

    def _validate_nodes(self, left_node, right_node):
        if left_node.distance_to(right_node) == 0:
            raise ValueError("Cannot define zero width element.")
        if left_node.x() > right_node.x():
            raise ValueError("left_node is to the right of the right_node.")

    def left_node(self) -> Node:
        return self._left_node

    def right_node(self) -> Node:
        return self._right_node

    def youngs_modulus(self) -> float:
        return self._E

    def cross_sectional_area(self) -> float:
        return self._A

    def number(self) -> int:
        return self._number

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
            horizontal where a positive inclination corresponds to the right
            node being higher than the left node.
        """
        return math.atan2(
            self._right_node.y() - self._left_node.y(),
            self._right_node.x() - self._left_node.x()
        )

    def stiffness(self) -> float:
        """Get the element stiffness.

        :return: Element stiffness in base SI units.
        :rtype: float
        """
        return self._E * self._A / self.length()

    def stiffness_matrix(self) -> list:
        """Get the element stiffness matrix.

        :return: Element stiffness matrix in base SI units.
        :rtype: list
        """
        k = self.stiffness()
        l = math.cos(self.incline())
        m = math.sin(self.incline())
        return [
            [k * l * l, k * l * m, -k * l * l, -k * l * m],
            [k * l * m, k * m * m, -k * l * m, -k * m * m],
            [-k * l * l, -k * l * m, k * l * l, k * l * m],
            [-k * l * m, -k * m * m, k * l * m, k * m * m]
        ]
