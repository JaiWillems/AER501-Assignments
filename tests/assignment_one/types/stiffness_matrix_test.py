from unittest import TestCase

from src.assignment_one.types.stiffness_matrix import StiffnessMatrix


class StiffnessMatrixTest(TestCase):

    def test_initialization_throws_error_for_empty_values(self):
        self.assertRaises(ValueError, StiffnessMatrix, [], [])

    def test_initialization_throws_error_for_non_square_values(self):
        self.assertRaises(ValueError, StiffnessMatrix, [], [[0, 0]])

    def test_initialization_throws_error_when_nodes_list_mismatches_values_list(self):
        self.assertRaises(ValueError, StiffnessMatrix, [], [[0, 0], [0, 0]])
