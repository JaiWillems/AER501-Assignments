from src.assignment_one.part_a.solver.solver import Solver
from src.assignment_one.part_a.types.element import Element
from src.assignment_one.part_a.types.node import Node, BoundaryCondition

from cProfile import Profile

from src.assignment_one.part_a.types.vector2d import Vector2d

E = 7e10  # Pa.
A = 0.0001  # m^2.
P = 100  # N.

node_1 = Node(0, 0, bc=BoundaryCondition.ZERO_DISPLACEMENT)
node_2 = Node(1, 0, force=Vector2d(0, -P))
node_3 = Node(2, 0)
node_4 = Node(3, 0, force=Vector2d(-P, -P))
node_5 = Node(0, -1)
node_6 = Node(1, -1)
node_7 = Node(2, -1, force=Vector2d(-P, -P))
node_8 = Node(3, -1)
node_9 = Node(0, -2)
node_10 = Node(1, -2, force=Vector2d(-P, P))
node_11 = Node(2, -2)
node_12 = Node(3, -2, force=Vector2d(P, 0))
node_13 = Node(0, -3, bc=BoundaryCondition.ZERO_DISPLACEMENT)
node_14 = Node(1, -3)
node_15 = Node(2, -3)
node_16 = Node(3, -3, force=Vector2d(P, 0))


def create_element(node_a, node_b):
    return Element(node_a, node_b, E, A)


element_1 = create_element(node_1, node_2)
element_2 = create_element(node_2, node_3)
element_3 = create_element(node_3, node_4)
element_4 = create_element(node_5, node_6)
element_5 = create_element(node_6, node_7)
element_6 = create_element(node_7, node_8)
element_7 = create_element(node_9, node_10)
element_8 = create_element(node_10, node_11)
element_9 = create_element(node_11, node_12)
element_10 = create_element(node_6, node_2)
element_11 = create_element(node_7, node_3)
element_12 = create_element(node_8, node_4)
element_13 = create_element(node_10, node_6)
element_14 = create_element(node_11, node_7)
element_15 = create_element(node_12, node_8)
element_16 = create_element(node_1, node_6)
element_17 = create_element(node_2, node_7)
element_18 = create_element(node_3, node_8)
element_19 = create_element(node_5, node_2)
element_20 = create_element(node_6, node_3)
element_21 = create_element(node_7, node_4)
element_22 = create_element(node_5, node_10)
element_23 = create_element(node_6, node_11)
element_24 = create_element(node_7, node_12)
element_25 = create_element(node_9, node_6)
element_26 = create_element(node_10, node_7)
element_27 = create_element(node_11, node_8)
element_28 = create_element(node_13, node_14)
element_29 = create_element(node_14, node_15)
element_30 = create_element(node_15, node_16)
element_31 = create_element(node_14, node_10)
element_32 = create_element(node_15, node_11)
element_33 = create_element(node_16, node_12)
element_34 = create_element(node_9, node_14)
element_35 = create_element(node_10, node_15)
element_36 = create_element(node_11, node_16)
element_37 = create_element(node_13, node_10)
element_38 = create_element(node_14, node_11)
element_39 = create_element(node_15, node_12)
element_40 = create_element(node_5, node_1)
element_41 = create_element(node_9, node_5)
element_42 = create_element(node_13, node_9)

with Profile() as profile:
    Solver.solve([
        element_1,
        element_2,
        element_3,
        element_4,
        element_5,
        element_6,
        element_7,
        element_8,
        element_9,
        element_10,
        element_11,
        element_12,
        element_13,
        element_14,
        element_15,
        element_16,
        element_17,
        element_18,
        element_19,
        element_20,
        element_21,
        element_22,
        element_23,
        element_24,
        element_25,
        element_26,
        element_27,
        element_28,
        element_29,
        element_30,
        element_31,
        element_32,
        element_33,
        element_34,
        element_35,
        element_36,
        element_37,
        element_38,
        element_39,
        element_40,
        element_41,
        element_42
    ])

profile.print_stats()
