from unittest import TestCase

from src.assignment_one.types.node import Node


class NodeTest(TestCase):

    def test_distance_to_for_horizontal_displacement(self):
        node_one = Node(0, 0, 1)
        node_two = Node(5, 0, 2)
        self.assertEqual(node_one.distance_to(node_two), 5)

    def test_distance_to_for_vertical_displacement(self):
        node_one = Node(0, 0, 1)
        node_two = Node(0, 5, 2)
        self.assertEqual(node_one.distance_to(node_two), 5)

    def test_distance_to_for_inclined_displacement(self):
        node_one = Node(0, 0, 1)
        node_two = Node(3, 4, 2)
        self.assertEqual(node_one.distance_to(node_two), 5)

    def test_distance_to_for_coincident_nodes_is_zero(self):
        node = Node(0, 0, 1)
        self.assertEqual(node.distance_to(node), 0)
