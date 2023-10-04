from src.assignment_one.part_a.solver.displacement_solver import DisplacementSolver
from src.assignment_one.part_a.solver.post_processer import PostProcessor
from src.assignment_one.part_a.types.global_stiffness_matrix_builder import \
    GlobalStiffnessMatrixBuilder
from src.assignment_one.part_a.types.stiffness_matrix import StiffnessMatrix


class Solver:

    @staticmethod
    def solve(elements: list) -> tuple:
        """Solve the truss defined by a list of elements.

        :param elements: List of elements forming the truss.
        :type elements: list.
        :return: Tuple containing displacements, strains, and stresses.
        :rtype: tuple.
        """
        builder = GlobalStiffnessMatrixBuilder(
            Solver._get_unique_nodes(elements)
        )
        for element in elements:
            builder.add_stiffness_matrix(
                StiffnessMatrix.from_element(element)
            )
        global_stiffness_matrix = builder.build()

        displacements = DisplacementSolver.solve(global_stiffness_matrix)
        strains = PostProcessor.calculate_strains(elements, displacements)
        stresses = PostProcessor.calculate_stresses(elements, strains)

        return displacements, strains, stresses

    @staticmethod
    def _get_unique_nodes(elements: list) -> list:
        """Get the list of unique nodes found in a list of elements.

        :param elements: List of elements forming a truss.
        :type elements: list.
        :return: List of unique nodes.
        :rtype: list.
        """
        unique_nodes = []
        for element in elements:
            if element.left_node() not in unique_nodes:
                unique_nodes.append(element.left_node())
            if element.right_node() not in unique_nodes:
                unique_nodes.append(element.right_node())
        return unique_nodes
