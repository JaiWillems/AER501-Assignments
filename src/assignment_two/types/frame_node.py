

class FrameNode:

    def __init__(
            self,
            x: float,
            y: float,
            constrained: bool = False,
            dof_active: list = [True, True, True]
    ) -> None:
        """Node for a frame structure.

        :param x: X-coordinate of node.
        :param y: Y-coordinate of node.
        :param constrained: True if the node is constrained, False by default.
        :param dof_active: List of booleans denoting if the x, y, and rotational
            degrees of freedom are active or not, all active by default.
        """
        self._x = x
        self._y = y
        self._constrained = constrained
        self._dof_active = dof_active

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y
