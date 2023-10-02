import math
from enum import Enum

from src.assignment_one.part_a.types.vector2d import Vector2d


class BoundaryCondition(Enum):
    NONE = 1
    ZERO_DISPLACEMENT = 2


class Node:

    def __init__(
            self,
            x: float,
            y: float,
            bc: BoundaryCondition = BoundaryCondition.NONE,
            force: Vector2d = Vector2d.zero()
    ) -> None:
        """Truss element elements.

        :param force:
        :param x: Global x-cooridinate in m.
        :type x: float
        :param y: Global y-coordinate in m.
        :type y: float
        :param bc: Nodal boundary condition.
        :type bc: BoundaryCondition.
        :param force: Force vector applied to the node.
        :type force: Vector2d.
        """
        self._x = x
        self._y = y
        self._bc = bc
        self._force = force

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y

    def boundary_condition(self) -> BoundaryCondition:
        return self._bc

    def force(self) -> Vector2d:
        return self._force

    def distance_to(self, other: 'Node') -> float:
        """Get the L2 norm between two elements.

        :param other: Node to calculate_element_stiffness_matrix distance to.
        :type other: Node

        :return: L2 norm between `self` and `other`.
        :rtype: float
        """
        return math.sqrt((self.x() - other.x()) ** 2 + (
                self.y() - other.y()) ** 2)
