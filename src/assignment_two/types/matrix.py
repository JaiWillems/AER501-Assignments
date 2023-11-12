
class Matrix:

    def __init__(self, nodes: list, values: list) -> None:
        """Matrix for frame data.

        :param nodes: List of nodes that relate to matrix values.
        :param values: Twice nested list representing matrix values.
        """
        self._nodes = nodes
        self._values = values

    def nodes(self) -> list:
        return self._nodes

    def values(self) -> list:
        return self._values
