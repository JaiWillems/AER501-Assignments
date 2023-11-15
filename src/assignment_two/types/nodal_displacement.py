
class NodalDisplacement:

    def __init__(self, x: complex, y: complex, m: complex) -> None:
        """Nodal displacements.

        :param x: Displacement in the x-direction.
        :param y: Displacement in the y-direction.
        :param m: Rotational displacement about the node.
        """
        self._x = x
        self._y = y
        self._m = m

    def x(self) -> complex:
        return self._x

    def absolute_x(self) -> float:
        return abs(self._x)

    def y(self) -> complex:
        return self._y

    def absolute_y(self) -> float:
        return abs(self._y)

    def m(self) -> complex:
        return self._m

    def absolute_m(self) -> float:
        return abs(self._m)
