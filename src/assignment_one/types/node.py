

class Node:
    """Node(x, y, number)

    Truss element nodes.

    Parameters
    ----------
    x : float
    y : float
    number : int
        Unique global node number.
    """

    def __init__(self, x: float, y: float, number: int):
        self._x = x
        self._y = y
        self._number = number

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def get_number(self) -> int:
        return self._number
