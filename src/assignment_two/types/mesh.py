from src.assignment_two.types import Matrix
from src.assignment_two.utils import zero_filled_matrix


class Mesh:

    def __init__(self, elements: list) -> None:
        """Mesh representing a frame structure.

        :param elements: List of frame elements composing the structure.
        """
        self._elements = elements

    def elements(self) -> list:
        return self._elements

    def mass_matrix(self) -> Matrix:
        """Generate the global mass matrix for the mesh.

        :return: Global mass matrix.
        """

        nodes = self._unique_nodes()
        values = zero_filled_matrix(3 * self._number_of_nodes())

        for element in self._elements:

            element_matrix = element.mass_matrix()
            local_values = element_matrix.values()

            for row_node in element_matrix.nodes():

                local_row = 3 * element_matrix.nodes().index(row_node)
                global_row = 3 * nodes.index(row_node)

                for column_node in element_matrix.nodes():
                    local_column = 3 * element_matrix.nodes().index(column_node)
                    global_column = 3 * nodes.index(column_node)

                    values[global_row][global_column] += local_values[
                        local_row][local_column]
                    values[global_row][global_column + 1] += local_values[
                        local_row][local_column + 1]
                    values[global_row][global_column + 2] += local_values[
                        local_row][local_column + 2]

                    values[global_row + 1][global_column] += local_values[
                        local_row + 1][local_column]
                    values[global_row + 1][global_column + 1] += local_values[
                        local_row + 1][local_column + 1]
                    values[global_row + 1][global_column + 2] += local_values[
                        local_row + 1][local_column + 2]

                    values[global_row + 2][global_column] += local_values[
                        local_row + 2][local_column]
                    values[global_row + 2][global_column + 1] += local_values[
                        local_row + 2][local_column + 1]
                    values[global_row + 2][global_column + 2] += local_values[
                        local_row + 2][local_column + 2]

        return Matrix(nodes, values)

    def stiffness_matrix(self) -> Matrix:
        """Generate the global stiffness matrix for the mesh.

        :return: Global stiffness matrix.
        """

        nodes = self._unique_nodes()
        values = zero_filled_matrix(3 * self._number_of_nodes())

        for element in self._elements:

            stiffness_matrix = element.stiffness_matrix()
            local_values = stiffness_matrix.values()

            for row_node in stiffness_matrix.nodes():

                local_row = 3 * stiffness_matrix.nodes().index(row_node)
                global_row = 3 * nodes.index(row_node)

                for column_node in stiffness_matrix.nodes():
                    local_column = 3 * stiffness_matrix.nodes().index(column_node)
                    global_column = 3 * nodes.index(column_node)

                    values[global_row][global_column] += local_values[
                        local_row][local_column]
                    values[global_row][global_column + 1] += local_values[
                        local_row][local_column + 1]
                    values[global_row][global_column + 2] += local_values[
                        local_row][local_column + 2]

                    values[global_row + 1][global_column] += local_values[
                        local_row + 1][local_column]
                    values[global_row + 1][global_column + 1] += local_values[
                        local_row + 1][local_column + 1]
                    values[global_row + 1][global_column + 2] += local_values[
                        local_row + 1][local_column + 2]

                    values[global_row + 2][global_column] += local_values[
                        local_row + 2][local_column]
                    values[global_row + 2][global_column + 1] += local_values[
                        local_row + 2][local_column + 1]
                    values[global_row + 2][global_column + 2] += local_values[
                        local_row + 2][local_column + 2]

        return Matrix(nodes, values)

    def _unique_nodes(self):
        unique_nodes = []
        for element in self._elements:
            if element.node_one() not in unique_nodes:
                unique_nodes.append(element.node_one())
            if element.node_two() not in unique_nodes:
                unique_nodes.append(element.node_two())
        return unique_nodes

    def _number_of_nodes(self):
        return len(self._unique_nodes())
