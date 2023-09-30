

class Validator:

    @staticmethod
    def assert_node_order(left_node, right_node):
        if left_node.x() > right_node.x():
            raise ValueError("left_node is to the right of the right_node.")

    @staticmethod
    def assert_element_has_non_zero_width(left_node, right_node):
        if left_node.distance_to(right_node) == 0:
            raise ValueError("Cannot define zero width element.")

    @staticmethod
    def assert_side_length_of_square_matrix(matrix: list, side_length: int):
        Validator.assert_square_matrix(matrix)
        if len(matrix) != side_length or len(matrix[0]) != side_length:
            raise ValueError(f"Matrix does not have side length of: {side_length}")

    @staticmethod
    def assert_square_matrix(matrix: list) -> None:
        Validator.assert_non_empty_list(matrix)
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix is not square.")

    @staticmethod
    def assert_non_empty_list(array: list):
        if len(array) == 0:
            raise ValueError("List is empty.")
