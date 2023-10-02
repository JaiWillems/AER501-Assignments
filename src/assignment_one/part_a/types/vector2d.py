

class Vector2d:

    def __init__(self, x: float, y: float) -> None:
        """2-dimensional vector quantity.

        :param x: X vector component.
        :param y: Y vector component.
        """
        self._x = x
        self._y = y

    @staticmethod
    def zero() -> 'Vector2d':
        return Vector2d(0, 0)

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y
