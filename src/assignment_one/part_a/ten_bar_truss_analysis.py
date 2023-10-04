from src.assignment_one.part_a.solver.solver import Solver
from src.assignment_one.part_a.types.element import Element
from src.assignment_one.part_a.types.node import Node, BoundaryCondition
from src.assignment_one.part_a.types.vector2d import Vector2d

E = 7e10  # Pa.
A = 0.0001  # m^2.
P = 100  # N.

node_one = Node(0, 0, bc=BoundaryCondition.ZERO_DISPLACEMENT)
node_two = Node(1, 0)
node_three = Node(2, 0)
node_four = Node(0, -1, bc=BoundaryCondition.ZERO_DISPLACEMENT)
node_five = Node(1, -1, force=Vector2d(0, -P))
node_six = Node(2, -1, force=Vector2d(0, -P))

element_one = Element(node_one, node_two, E, A)
element_two = Element(node_two, node_three, E, A)
element_three = Element(node_one, node_five, E, A)
element_four = Element(node_four, node_two, E, A)
element_five = Element(node_five, node_two, E, A)
element_six = Element(node_two, node_six, E, A)
element_seven = Element(node_five, node_three, E, A)
element_eight = Element(node_six, node_three, E, A)
element_nine = Element(node_four, node_five, E, A)
element_ten = Element(node_five, node_six, E, A)

displacements, strains, stresses = Solver.solve([
    element_one,
    element_two,
    element_three,
    element_four,
    element_five,
    element_six,
    element_seven,
    element_eight,
    element_nine,
    element_ten
])

for key, value in displacements.items():
    print(f"Node at x={key.x()}, y={key.y()} has the displacements: x={value.x()}, y={value.y()}")

for element, strain in strains.items():
    left_node = element.left_node()
    right_node = element.right_node()
    print(f"Element from ({left_node.x()}, {left_node.y()}) to ({right_node.x()}, {right_node.y()}) has strain: {strain}, and stress: {stresses.get(element)}")