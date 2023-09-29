import math
from unittest import TestCase

from src.assignment_one.types.element import Element
from src.assignment_one.types.node import Node


class ElementTest(TestCase):
    youngs_modulus = 1000
    cross_sectional_area = 0.001

    def setUp(self):
        terminal_node = Node(0, 0, 1)
        self.horizontal_element = self.create_element(
            terminal_node,
            Node(5, 0, 2)
        )
        self.vertical_element = self.create_element(
            terminal_node,
            Node(0, 5, 2)
        )
        self.positive_inclined_element = self.create_element(
            terminal_node,
            Node(3, 4, 2)
        )
        self.negative_inclined_element = self.create_element(
            terminal_node,
            Node(3, -4, 2)
        )

    def test_initializing_zero_length_node_throws_error(self):
        self.assertRaises(
            ValueError,
            self.create_element,
            Node(0, 0, 1),
            Node(0, 0, 1)
        )

    def test_initializing_backwards_element_throws_error(self):
        self.assertRaises(
            ValueError,
            self.create_element,
            Node(5, 0, 1),
            Node(0, 0, 1)
        )

    def test_length_for_horizontal_element(self):
        self.assertEqual(self.horizontal_element.length(), 5)

    def test_length_for_vertical_element(self):
        self.assertEqual(self.vertical_element.length(), 5)

    def test_length_for_inclined_element(self):
        self.assertEqual(self.positive_inclined_element.length(), 5)

    def test_incline_for_horizontal_element(self):
        self.assertEqual(self.horizontal_element.incline(), 0)

    def test_incline_for_vertical_element(self):
        self.assertEqual(self.vertical_element.incline(), math.pi / 2)

    def test_incline_for_positive_inclined_element(self):
        self.assertEqual(
            self.positive_inclined_element.incline(),
            0.9272952180016122
        )

    def test_incline_for_negative_inclined_element(self):
        self.assertEqual(
            self.negative_inclined_element.incline(),
            -0.9272952180016122
        )

    def test_stiffness(self):
        expected_stiffness = self.positive_inclined_element.youngs_modulus()\
                             * self.positive_inclined_element.cross_sectional_area()\
                             / self.positive_inclined_element.length()
        self.assertEqual(
            self.positive_inclined_element.stiffness(),
            expected_stiffness
        )

    def test_stiffness_matrix(self):
        k = self.positive_inclined_element.stiffness()
        l = math.cos(self.positive_inclined_element.incline())
        m = math.sin(self.positive_inclined_element.incline())
        expected_stiffness_matrix = [
            [k*l*l, k*l*m, -k*l*l, -k*l*m],
            [k*l*m, k*m*m, -k*l*m, -k*m*m],
            [-k*l*l, -k*l*m, k*l*l, k*l*m],
            [-k*l*m, -k*m*m, k*l*m, k*m*m]]
        self.assertEquals(
            self.positive_inclined_element.stiffness_matrix(),
            expected_stiffness_matrix
        )

    def create_element(self, node_one: Node, node_two: Node) -> Element:
        return Element(
            node_one,
            node_two,
            self.youngs_modulus,
            self.cross_sectional_area,
            1
        )
