import math
from unittest import TestCase

from src.assignment_one.part_a.types.global_stiffness_matrix_builder import \
    GlobalStiffnessMatrixBuilder
from src.assignment_one.part_a.types.element import Element
from src.assignment_one.part_a.types.node import Node
from src.assignment_one.part_a.types.stiffness_matrix import StiffnessMatrix
from src.assignment_one.part_a.utils.utility_functions import zero_filled_matrix


class GlobalStiffnessMatrixBuilderTest(TestCase):
    node_one = Node(0, 0)
    node_two = Node(1, 0)
    node_three = Node(2, 1)
    nodes = [node_one, node_two, node_three]

    def test_building_empty_matrix_has_proper_dimensions(self):
        matrix = GlobalStiffnessMatrixBuilder(self.nodes).build()

        number_of_rows = len(matrix.values())
        self.assertEqual(number_of_rows, 6)

        number_of_columns = len(matrix.values()[0])
        self.assertEqual(number_of_columns, 6)

    def test_building_empty_matrix_produces_a_zero_filled_matrix(self):
        self.assertEqual(
            GlobalStiffnessMatrixBuilder(self.nodes).build().values(),
            zero_filled_matrix(6)
        )

    def test_building_matrix_properly_adds_two_element_matricies_together(self):
        builder = GlobalStiffnessMatrixBuilder(self.nodes)

        builder.add_stiffness_matrix(
            StiffnessMatrix.from_element(
                Element(self.node_one, self.node_two, 1, 1)
            )
        )
        builder.add_stiffness_matrix(
            StiffnessMatrix.from_element(
                Element(self.node_two, self.node_three, 1, 1)
            )
        )

        a = math.sqrt(2) / 4
        expected_matrix = [
            [1, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [-1, 0, 1+a, a, -a, -a],
            [0, 0, a, a, -a, -a],
            [0, 0, -a, -a, a, a],
            [0, 0, -a, -a, a, a]
        ]

        self.assertEqual(builder.build().values(), expected_matrix)
