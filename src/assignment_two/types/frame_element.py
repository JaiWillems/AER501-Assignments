import math

from src.assignment_two.types import FrameNode, Matrix
from src.assignment_two.utils import zero_filled_matrix


class FrameElement:

    def __init__(
            self,
            node_one: FrameNode,
            node_two: FrameNode,
            linear_density: float = 2.74,  # kg/m.
            ea: float = 6987000,  # N.
            ei: float = 12860  # Nm^2.
    ) -> None:
        """Element for frame structure.

        :param node_one: First node of the element.
        :param node_two: Second node of the element.
        :param linear_density: Density per unit length of the element in kg/m,
            default is 2.74 kg/m.
        :param ea: Young's Modulus times cross-sectional area in N, default is
            6.987x10^6 N.
        :param ei: Yonge's Modulus times moment of inertia in Nm^2, default is
            1.286x10^4.
        """
        self._node_one = node_one
        self._node_two = node_two
        self._linear_density = linear_density
        self._EA = ea
        self._EI = ei

    def node_one(self) -> FrameNode:
        return self._node_one

    def node_two(self) -> FrameNode:
        return self._node_two
    
    def length(self) -> float:
        dx = self._node_two.x() - self._node_one.x()
        dy = self._node_two.y() - self._node_one.y()
        return math.sqrt(dx ** 2 + dy ** 2)

    def mass_matrix(self) -> Matrix:
        """Generate the elemental mass matrix.

        Copied from the assignment provided MATLAB code, verified to have
        matching results.

        :return: Element mass matrix.
        """

        x1 = self._node_one.x()
        y1 = self._node_one.y()

        x2 = self._node_two.x()
        y2 = self._node_two.y()

        length = self.length()
        c = (x2 - x1) / length
        s = (y2 - y1) / length

        values = zero_filled_matrix(6)

        values[0][0] = 140. * c * c + 156. * s * s
        values[0][1] = -16. * c * s
        values[0][2] = -22. * length * s
        values[0][3] = 70. * c * c + 54. * s * s
        values[0][4] = -values[0][1]
        values[0][5] = 13. * length * s

        values[1][0] = values[0][1]
        values[1][1] = 156. * c * c + 140. * s * s
        values[1][2] = 22. * length * c
        values[1][3] = -values[0][1]
        values[1][4] = 54. * c * c + 70. * s * s
        values[1][5] = -13. * length * c

        values[2][0] = values[0][2]
        values[2][1] = values[1][2]
        values[2][2] = 4. * length * length
        values[2][3] = -values[0][5]
        values[2][4] = -values[1][5]
        values[2][5] = -3. * length * length

        values[3][0] = values[0][3]
        values[3][1] = values[1][3]
        values[3][2] = values[2][3]
        values[3][3] = values[0][0]
        values[3][4] = values[0][1]
        values[3][5] = -values[0][2]

        values[4][0] = values[0][4]
        values[4][1] = values[1][4]
        values[4][2] = values[2][4]
        values[4][3] = values[3][4]
        values[4][4] = values[1][1]
        values[4][5] = -values[1][2]

        values[5][0] = values[0][5]
        values[5][1] = values[1][5]
        values[5][2] = values[2][5]
        values[5][3] = values[3][5]
        values[5][4] = values[4][5]
        values[5][5] = values[2][2]

        for i in range(len(values)):
            for j in range(len(values[i])):
                values[i][j] = self._linear_density * length * values[i][j] / 420

        return Matrix([self._node_one, self._node_two], values)

    def stiffness_matrix(self) -> Matrix:
        """Generate the elemental stiffness matrix.

        Copied from the assignment provided MATLAB code, verified to have
        matching results.

        :return: Element stiffness matrix.
        """

        x1 = self._node_one.x()
        y1 = self._node_one.y()

        x2 = self._node_two.x()
        y2 = self._node_two.y()
        
        length = self.length()

        c = (x2 - x1) / length
        s = (y2 - y1) / length

        e1 = self._EA / length
        e2 = 12. * self._EI / (length * length * length)
        e3 = self._EI / length
        e4 = 6. * self._EI / (length * length)

        values = zero_filled_matrix(6)
    
        values[0][0] = c * c * e1 + s * s * e2
        values[3][3] = values[0][0]
        values[0][1] = s * c * (e1 - e2)
        values[1][0] = values[0][1]
        values[3][4] = values[0][1]
        values[4][3] = values[3][4]
        values[0][2] = -s * e4
        values[2][0] = values[0][2]
        values[0][5] = values[0][2]
        values[5][0] = values[0][5]
        values[2][3] = s * e4
        values[3][2] = values[2][3]
        values[3][5] = values[2][3]
        values[5][3] = values[3][5]
        values[0][3] = -values[0][0]
        values[3][0] = values[0][3]
        values[0][4] = s * c * (-e1 + e2)
        values[4][0] = values[0][4]
        values[1][3] = values[0][4]
        values[3][1] = values[1][3]
        values[1][1] = s * s * e1 + c * c * e2
        values[4][4] = values[1][1]
        values[1][4] = -values[1][1]
        values[4][1] = values[1][4]
        values[1][2] = c * e4
        values[2][1] = values[1][2]
        values[1][5] = values[1][2]
        values[5][1] = values[1][5]
        values[2][2] = 4. * e3
        values[5][5] = values[2][2]
        values[2][4] = -c * e4
        values[4][2] = values[2][4]
        values[4][5] = values[2][4]
        values[5][4] = values[4][5]
        values[2][5] = 2. * e3
        values[5][2] = values[2][5]
    
        return Matrix([self._node_one, self._node_two], values)
