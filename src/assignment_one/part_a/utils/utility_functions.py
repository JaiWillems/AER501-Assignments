from src.assignment_one.part_a.types.node import Node


def zero_filled_matrix(side_length: int) -> list:
    """Generate a 2d list of zeros.

    :param side_length: Side length of zero matrix.
    :type side_length: int
    :return: zero filled list.
    :rtype: list.
    """
    return [side_length * [0] for _ in range(side_length)]


def get_value_index(nodes: list, node: Node) -> int:
    """Get the xx value index for row and column elements.

    :param nodes: List defining node positions.
    :type nodes: list.
    :param node: Node to determine the value index for.
    :type node: Node
    :return: Value index.
    :rtype: int.
    """
    return 2 * nodes.index(node)
