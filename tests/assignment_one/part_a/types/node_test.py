from unittest import TestCase

from src.assignment_one.part_a.types.node import Node


class NodeTest(TestCase):

    def test_distance_to_for_horizontal_displacement(self):
        self.assertEqual(Node(0, 0).distance_to(Node(5, 0)), 5)

    def test_distance_to_for_vertical_displacement(self):
        self.assertEqual(Node(0, 0).distance_to(Node(0, 5)), 5)

    def test_distance_to_for_inclined_displacement(self):
        self.assertEqual(Node(0, 0).distance_to(Node(3, 4)), 5)

    def test_distance_to_for_coincident_nodes_is_zero(self):
        node = Node(0, 0)
        self.assertEqual(node.distance_to(node), 0)
