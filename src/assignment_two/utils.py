

def zero_filled_matrix(side_length: int) -> list:
    """Generate a 2d list of zeros.

    :param side_length: Side length of zero matrix.
    :type side_length: int
    :return: zero filled list.
    :rtype: list.
    """
    return [side_length * [0] for _ in range(side_length)]
