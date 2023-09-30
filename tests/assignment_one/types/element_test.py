import math
from unittest import TestCase

from src.assignment_one.types.element import Element
from src.assignment_one.types.node import Node


class ElementTest(TestCase):
    elasticity = 1000
    area = 0.001

    def setUp(self):
        terminal_node = Node(0, 0)
        self.horizontal_element = self.create_element(terminal_node, Node(5, 0))
        self.vertical_element = self.create_element(terminal_node, Node(0, 5))
        self.up_sloped_element = self.create_element(terminal_node, Node(3, 4))
        self.down_sloped_element = self.create_element(terminal_node, Node(3, -4))

    def test_initializing_zero_length_node_throws_error(self):
        self.assertRaises(ValueError, self.create_element, Node(0, 0), Node(0, 0))

    def test_initializing_backwards_element_throws_error(self):
        self.assertRaises(ValueError, self.create_element, Node(5, 0), Node(0, 0))

    def test_length_for_horizontal_element(self):
        self.assertEqual(self.horizontal_element.length(), 5)

    def test_length_for_vertical_element(self):
        self.assertEqual(self.vertical_element.length(), 5)

    def test_length_for_inclined_element(self):
        self.assertEqual(self.up_sloped_element.length(), 5)

    def test_incline_for_horizontal_element(self):
        self.assertEqual(self.horizontal_element.incline(), 0)

    def test_incline_for_vertical_element(self):
        self.assertEqual(self.vertical_element.incline(), math.pi / 2)

    def test_incline_for_positive_inclined_element(self):
        self.assertEqual(self.up_sloped_element.incline(), 0.9272952180016122)

    def test_incline_for_negative_inclined_element(self):
        self.assertEqual(self.down_sloped_element.incline(), -0.9272952180016122)

    def create_element(self, node_one: Node, node_two: Node) -> Element:
        return Element(node_one, node_two, self.elasticity, self.area)
