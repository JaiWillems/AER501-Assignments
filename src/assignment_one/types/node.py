import math


class Node:

    def __init__(self, x: float, y: float) -> None:
        """Truss element nodes.

        :param x: Global x-cooridinate in m.
        :type x: float
        :param y: Global y-coordinate in m.
        :type y: float
        """
        self._x = x
        self._y = y

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y

    def distance_to(self, other: 'Node') -> float:
        """Get the L2 norm between two nodes.

        :param other: Node to calculate_element_stiffness_matrix distance to.
        :type other: Node

        :return: L2 norm between `self` and `other`.
        :rtype: float
        """
        return math.sqrt((self.x() - other.x()) ** 2 + (
                self.y() - other.y()) ** 2)
