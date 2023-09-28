from src.assignment_one.types.node import Node


class Element:
    """Element(node_one, node_two, e, a, number)

    Truess element.

    Parameters
    ----------
    node_one : Node
    node_two : Node
    e : float
        Young's modulus in N/m^2.
    a : float
        Cross sectional area in m^2.
    number : int
        Unique global element number.
    """

    def __init__(self, node_one: Node, node_two: Node, e: float, a: float, number: int):
        self._node_one = node_one
        self._node_two = node_two
        self._E = e
        self._A = a
        self._number = number

    def get_node_one(self) -> Node:
        return self._node_one

    def get_node_two(self) -> Node:
        return self._node_two

    def get_youngs_modulus(self) -> float:
        return self._E

    def get_cross_sectional_area(self) -> float:
        return self._A

    def get_number(self) -> int:
        return self._number
