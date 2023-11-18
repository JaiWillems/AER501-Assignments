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
        element_matrices = [element.mass_matrix() for element in self._elements]
        return Matrix(
            self.nodes(),
            Mesh._generate_global_matrix(self.nodes(), element_matrices)
        )

    def stiffness_matrix(self) -> Matrix:
        """Generate the global stiffness matrix for the mesh.

        :return: Global stiffness matrix.
        """
        element_matrices = [element.stiffness_matrix() for element in self._elements]
        return Matrix(
            self.nodes(),
            Mesh._generate_global_matrix(self.nodes(), element_matrices)
        )

    @staticmethod
    def _generate_global_matrix(nodes: list, matrices: list) -> list:
        values = zero_filled_matrix(3 * len(nodes))
        for matrix in matrices:

            local_values = matrix.values()

            for row_node in matrix.nodes():

                local_row = 3 * matrix.nodes().index(row_node)
                global_row = 3 * nodes.index(row_node)

                for column_node in matrix.nodes():
                    local_column = 3 * matrix.nodes().index(column_node)
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

        return values

    def nodes(self) -> list:
        unique_nodes = []
        for element in self._elements:
            if element.node_one() not in unique_nodes:
                unique_nodes.append(element.node_one())
            if element.node_two() not in unique_nodes:
                unique_nodes.append(element.node_two())
        return unique_nodes

    def unconstrained_nodes(self) -> list:
        unconstrained_nodes = []
        for node in self.nodes():
            if not node.is_constrained():
                unconstrained_nodes.append(node)
        return unconstrained_nodes
