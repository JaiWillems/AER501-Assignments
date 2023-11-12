

class FrameNode:

    def __init__(
            self,
            x: float,
            y: float,
            constrained: bool = False
    ) -> None:
        """Node for a frame structure.

        :param x: X-coordinate of node.
        :param y: Y-coordinate of node.
        :param constrained: True if the node is constrained, False by default.
            All degrees of freedom for constrained nodes are assumed inactive.
        """
        self._x = x
        self._y = y
        self._constrained = constrained

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y
