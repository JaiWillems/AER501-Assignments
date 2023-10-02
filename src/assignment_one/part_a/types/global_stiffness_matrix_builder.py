from src.assignment_one.part_a.types.stiffness_matrix import StiffnessMatrix
from src.assignment_one.part_a.utils.utility_functions import zero_filled_matrix, \
    get_value_index


class GlobalStiffnessMatrixBuilder:

    def __init__(self, nodes: list) -> None:
        """Global stiffness matrix builder.

        :param nodes: Nodes of the system.
        :type nodes: list.
        """
        self._nodes = nodes
        self._values = zero_filled_matrix(2 * len(nodes))

    def add_stiffness_matrix(self, stiffness_matrix: StiffnessMatrix) -> None:
        """Add stiffness matrix to the global stiffness matrix.

        :param stiffness_matrix: Matrix to add to the global stiffness matrix.
        :type stiffness_matrix: StiffnessMatrix.
        """
        nodes = stiffness_matrix.nodes()
        values = stiffness_matrix.values()
        for row_node in nodes:

            local_row = get_value_index(nodes, row_node)
            global_row = get_value_index(self._nodes, row_node)

            for column_node in nodes:
                local_column = get_value_index(nodes, column_node)
                global_column = get_value_index(self._nodes, column_node)

                self._transfer_values(
                    global_column,
                    global_row,
                    local_column,
                    local_row,
                    values
                )

    def _transfer_values(
            self,
            global_column: int,
            global_row: int,
            local_column: int,
            local_row: int,
            local_matrix: list
    ) -> None:
        """Transfer values from local matrix to the global stiffness matrix.

        :param global_column: Column index of the global matrix.
        :type global_column: int.
        :param global_row: Row index of the global matrix.
        :type global_row: int.
        :param local_column: Column index of the local matrix.
        :type local_column: int.
        :param local_row: Row index of the local matrix.
        :type local_row: int.
        :param local_matrix: Local matrix of values.
        :type local_matrix: list.
        """
        self._values[global_row][global_column] += local_matrix[local_row][local_column]
        self._values[global_row][global_column + 1] += local_matrix[local_row][local_column + 1]
        self._values[global_row + 1][global_column] += local_matrix[local_row + 1][local_column]
        self._values[global_row + 1][global_column + 1] += local_matrix[local_row + 1][local_column + 1]

    def build(self) -> StiffnessMatrix:
        """Build the global stiffness matrix.

        :return: Assembled global stiffness matrix.
        :rtype StiffnessMatrix.
        """
        return StiffnessMatrix(self._nodes, self._values)
